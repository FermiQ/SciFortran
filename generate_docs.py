import argparse
import os
import re

def parse_fortran_file(fortran_filepath):
    module_info = {
        "name": None, # This will be module name found in code
        "original_filename": os.path.splitext(os.path.basename(fortran_filepath))[0], # Store original filename
        "overview": "Overview not automatically extracted.",
        "components": []
    }
    active_comments = []
    module_overview_lines = []

    try:
        with open(fortran_filepath, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"Error: Fortran file not found at {fortran_filepath}")
        return None
    except Exception as e:
        print(f"Error reading Fortran file {fortran_filepath}: {e}")
        return None

    i = 0
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()

        module_match = re.match(r"^\s*module\s+([a-zA-Z_][a-zA-Z0-9_]*)", line_stripped, re.IGNORECASE)
        if module_match:
            if module_info["name"] is None: # Capture the first module name encountered
                module_info["name"] = module_match.group(1)

            # Overview parsing logic (remains the same)
            k = i + 1
            temp_overview_ahead = []
            while k < len(lines) and lines[k].strip().startswith("!"):
                comment_content = lines[k].strip()[1:].strip()
                if comment_content and not comment_content.startswith("---"):
                    temp_overview_ahead.append(comment_content)
                k += 1

            k = i - 1
            temp_overview_behind = []
            while k >= 0 and lines[k].strip().startswith("!"):
                comment_content = lines[k].strip()[1:].strip()
                if comment_content and not comment_content.startswith("---"):
                    temp_overview_behind.append(comment_content)
                elif not lines[k].strip().startswith("!") and lines[k].strip():
                    break
                k -= 1

            current_overview = ""
            if temp_overview_ahead:
                 current_overview = "\n".join(temp_overview_ahead)
            elif temp_overview_behind:
                 current_overview = "\n".join(reversed(temp_overview_behind))

            if not module_info["overview"] or module_info["overview"] == "Overview not automatically extracted.":
                module_info["overview"] = current_overview

            active_comments = []
            i += 1
            continue

        if line_stripped.startswith("!"):
            comment_content = line_stripped[1:].strip()
            if comment_content and not re.match(r"^-+$", comment_content) and comment_content.lower() != "purpose:":
                active_comments.append(comment_content)
            elif not comment_content and active_comments and active_comments[-1]:
                active_comments.append("")
            i += 1
            continue

        proc_match = re.match(
            r"^\s*(?:(?:elemental|recursive|pure|impure)\s+)*"
            r"(function|subroutine)\s+"
            r"([a-zA-Z_][a-zA-Z0-9_]*)"
            r"\s*\((.*?)\)",
            line_stripped, re.IGNORECASE
        )
        if proc_match:
            proc_type = proc_match.group(1).lower()
            proc_name = proc_match.group(2)
            proc_args = proc_match.group(3).strip()

            post_signature_comments = []
            k = i + 1
            # Look for comments immediately AFTER the signature line
            comment_block_for_proc_ended = False
            while k < len(lines) and not comment_block_for_proc_ended:
                current_proc_line_stripped = lines[k].strip()
                if current_proc_line_stripped.startswith("!"):
                    comment_content = current_proc_line_stripped[1:].strip()
                    if comment_content and not re.match(r"^-+$", comment_content) and comment_content.lower() != "purpose:":
                        post_signature_comments.append(comment_content)
                    elif not comment_content and post_signature_comments and post_signature_comments[-1]:
                        post_signature_comments.append("")
                # Stop if we hit non-comment line that's not part of type declaration or 'implicit none' etc.
                elif current_proc_line_stripped and \
                     not re.match(r"^\s*(real|integer|character|logical|type|class|implicit|contains|end)\b", current_proc_line_stripped, re.IGNORECASE) and \
                     not comment_block_for_proc_ended:
                    comment_block_for_proc_ended = True # Real code line, stop comment gathering
                elif not current_proc_line_stripped : # empty line can also signify end of comment block if followed by code
                    if k+1 < len(lines) and lines[k+1].strip() and not lines[k+1].strip().startswith("!"):
                        comment_block_for_proc_ended = True

                if comment_block_for_proc_ended and not post_signature_comments and active_comments: # if no post comments, check if pre-comments were right before a non-declaration line
                    pass # allow pre_comments to be used
                elif comment_block_for_proc_ended:
                    break # Exit comment gathering loop

                k += 1


            description_lines = post_signature_comments if post_signature_comments else active_comments
            description = "\n".join(description_lines).strip()
            if not description or description.lower() == "purpose:":
                description = "No specific description available."

            is_public = True
            # Simplified public/private check (remains as is, can be enhanced later if needed)
            for j_idx in range(i -1, max(0, i-30), -1): # Check preceding lines for private/public attributes
                 if lines[j_idx].strip().lower() == "private":
                    is_public = False
                    for l_scan in range(j_idx + 1, i):
                        if re.search(r"\bpublic\b", lines[l_scan].strip(), re.IGNORECASE):
                             if re.search(r"::\s*" + re.escape(proc_name) , lines[l_scan], re.IGNORECASE) or not "::" in lines[l_scan]:
                                is_public = True; break
                    if is_public: break
                 if re.search(r"private\s*::\s*([a-zA-Z0-9_,\s]+)", lines[j_idx].strip(), re.IGNORECASE):
                     if proc_name in re.search(r"private\s*::\s*([a-zA-Z0-9_,\s]+)", lines[j_idx].strip(), re.IGNORECASE).group(1).replace(" ",""):
                        is_public = False; break
                 if re.search(r"public\s*::\s*([a-zA-Z0-9_,\s]+)", lines[j_idx].strip(), re.IGNORECASE):
                     if proc_name in re.search(r"public\s*::\s*([a-zA-Z0-9_,\s]+)", lines[j_idx].strip(), re.IGNORECASE).group(1).replace(" ",""):
                        is_public = True; break

            if is_public:
                module_info["components"].append({
                    "type": proc_type, "name": proc_name, "args": proc_args,
                    "signature": f"{proc_type.capitalize()} {proc_name}({proc_args})",
                    "description": description
                })

            active_comments = []
            i = k if post_signature_comments else i + 1 # Advance index correctly
            continue # End of processing proc_match

        # If it's not a comment, not a proc, and not empty, reset active_comments
        if line_stripped:
            active_comments = []
        i += 1

    # If no module statement was found, module_info["name"] will be None.
    # The original_filename is already set.
    if module_info["name"] is None:
        print(f"Warning: No module declaration found in {fortran_filepath}. Using filename for module name in docs.")
        module_info["name"] = module_info["original_filename"] # Use original filename if no module name

    return module_info

def generate_markdown_doc(template_content, module_info, output_dir):
    if not module_info or not module_info["original_filename"]: # check original_filename
        print("Error: Invalid module_info provided (missing original_filename).")
        return False

    escaped_module_overview = module_info["overview"].replace('\\', '\\\\')

    content = template_content
    # Use module_info["name"] for display, which might be from module statement or filename fallback
    display_module_name = module_info["name"] if module_info["name"] else module_info["original_filename"]

    content = content.replace("[Provide a brief overview of the Fortran source file's purpose and functionality.]", escaped_module_overview, 1)

    components_md_parts = []
    module_purpose_escaped = escaped_module_overview
    components_md_parts.append(f"### Module: `{display_module_name}`") # Use display_module_name
    components_md_parts.append(f"- **Purpose:** {module_purpose_escaped}")
    component_names = [f"`{c['name']}`" for c in module_info["components"]]
    if component_names:
        components_md_parts.append(f"- **Contains:** {', '.join(component_names)}")
    components_md_parts.append("\n")

    if module_info["components"]:
        for comp in module_info["components"]:
            components_md_parts.append(f"### {comp['type'].capitalize()}: `{comp['name']}`")
            components_md_parts.append(f"- **Signature:** `{comp['signature']}`")

            raw_description = comp['description']
            escaped_description = raw_description.replace('\\', '\\\\')
            has_newline = '\n' in escaped_description
            description_to_render = escaped_description
            if has_newline:
                desc_lines = escaped_description.split('\n')
                description_to_render = "\n  ".join(desc_lines)
            components_md_parts.append(f"- **Purpose:** {description_to_render}")
            components_md_parts.append(f"- **Inputs:** [Details to be filled manually or by more advanced parsing]")
            components_md_parts.append(f"- **Outputs:** [Details to be filled manually or by more advanced parsing]")
            components_md_parts.append("")
    else:
        components_md_parts.append("No public functions or subroutines found or extracted.")

    full_components_replacement_text = "\n".join(components_md_parts)
    key_components_section_regex = r"(## Key Components\s*\n)(?:.*?)(\n##|$)"

    def replace_section(match_obj):
        return match_obj.group(1) + full_components_replacement_text + match_obj.group(2)

    if re.search(key_components_section_regex, content, re.DOTALL | re.IGNORECASE):
        content = re.sub(key_components_section_regex, replace_section, content, 1, re.DOTALL | re.IGNORECASE)
    else:
        content += "\n## Key Components\n" + full_components_replacement_text

    content = re.sub(r"### Subroutine/Function \d+.*?\n(- \*\*Purpose:\*\* \[Description\]\n(?:- \*\*Inputs:\*\*.*?(\n|\Z))?(?:- \*\*Outputs:\*\*.*?(\n|\Z))?)", "", content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r"### Module 1.*?\n(- \*\*Purpose:\*\* \[Description\]\n(?:- \*\*Contains:\*\*.*?(\n|\Z))?)", "", content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'\n\s*\n', '\n\n', content)

    # Use original_filename for the output MD file to ensure uniqueness
    output_filename = f"{module_info['original_filename']}.md"
    output_filepath = os.path.join(output_dir, output_filename)

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Documentation successfully generated: {output_filepath}")
        return True
    except Exception as e:
        print(f"Error writing documentation file {output_filepath}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Generate Markdown documentation from Fortran source files.")
    parser.add_argument("fortran_file", help="Path to the Fortran source file.")
    parser.add_argument("template_file", help="Path to the Markdown documentation template.")
    parser.add_argument("-o", "--output_dir", default="documentation", help="Directory to save generated Markdown files (default: documentation).")
    args = parser.parse_args()
    try:
        with open(args.template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {args.template_file}")
        return
    except Exception as e:
        print(f"Error reading template file {args.template_file}: {e}")
        return

    # Pass the fortran_file path to parse_fortran_file
    module_info = parse_fortran_file(args.fortran_file)

    if module_info:
        generate_markdown_doc(template_content, module_info, args.output_dir)

if __name__ == "__main__":
    main()
