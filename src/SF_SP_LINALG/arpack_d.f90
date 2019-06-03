subroutine lanczos_arpack_d(MatVec,eval,evec,Nblock,Nitermax,which,v0,tol,iverbose,vrandom)
  !Interface to Matrix-Vector routine:
  interface
     subroutine MatVec(Nloc,vin,vout)
       integer                 :: Nloc
       real(8),dimension(Nloc) :: vin
       real(8),dimension(Nloc) :: vout
     end subroutine MatVec
  end interface
  !Arguments
  real(8)                   :: eval(:)![Neigen]
  real(8)                   :: evec(:,:)![Ns,Neigen]
  integer,optional          :: Nblock
  integer,optional          :: Nitermax
  character(len=2),optional :: which
  real(8),optional          :: v0(size(evec,1))!(ns)
  real(8),optional          :: tol
  logical,optional          :: iverbose
  logical,optional          :: vrandom
  !Dimensions:
  integer                   :: Ns
  integer                   :: Neigen
  integer                   :: maxn,maxnev,maxncv,ldv
  integer                   :: n,nconv,ncv,nev
  !Arrays:
  real(8),allocatable       :: ax(:),d(:,:)
  real(8),allocatable       :: resid(:)
  real(8),allocatable       :: workl(:),workd(:)
  real(8),allocatable       :: v(:,:)
  logical,allocatable       :: select(:)
  integer                   :: iparam(11)
  integer                   :: ipntr(11)
  !Control Vars:
  integer                   :: ido,ierr,info,ishfts,j,lworkl,maxitr,mode1
  logical                   :: rvec,verb,vran
  integer                   :: i
  real(8)                   :: sigma
  real(8)                   :: tol_
  character                 :: bmat  
  character(len=2)          :: which_
  real(8),external          :: dnrm2
  !
  Ns     = size(evec,1)
  Neigen = size(eval)
  call assert_shape(Evec,[Ns,Neigen],"Arpack_d","Evec")
  !
  maxn   = Ns
  maxnev = Neigen
  !
  maxncv = 10*Neigen ; if(present(Nblock))maxncv = Nblock
  maxitr = 512       ; if(present(Nitermax))maxitr = Nitermax
  which_='SA'        ; if(present(which))which_=which
  tol_  = 0d0        ; if(present(tol))tol_=tol
  verb  =.false.     ; if(present(iverbose))verb=iverbose
  vran  =.true.      ; if(present(vrandom))vran=vrandom
  !
  ldv    = Ns        ; if(maxncv>Ns)maxncv=Ns
  n      = maxn
  nev    = maxnev
  ncv    = maxncv
  bmat   = 'I'
  ! 
  allocate(ax(n))
  allocate(d(ncv,2))
  allocate(resid(n))
  allocate(workl(ncv*(ncv+8)))
  allocate(workd(3*n))
  allocate(v(ldv,ncv))
  allocate(select(ncv))
  ax        = 0d0
  d         = 0d0
  resid     = 0d0
  workl     = 0d0
  workd     = 0d0
  v         = 0d0
  lworkl    = ncv*(ncv+8)
  info      = 1
  ido       = 0
  ishfts    = 1
  mode1     = 1
  iparam(1) = ishfts
  iparam(3) = maxitr
  iparam(7) = mode1
  if(present(v0))then
     resid=v0
  else
     if(vran)then
        ! call random_seed(size=nrandom)
        ! if(allocated(seed_random))deallocate(seed_random)
        ! allocate(seed_random(nrandom))
        ! seed_random=1234567
        ! call random_seed(put=seed_random)
        ! call random_number(resid)
        ! deallocate(seed_random)
        call mt_random(resid)
     else
        resid = 1d0             !start with unitary vector 1/sqrt(Ndim)
     endif
  endif
  resid=resid/sqrt(dot_product(resid,resid))
  !
  !MAIN LOOP, REVERSE COMMUNICATION
  do
     call dsaupd(ido,bmat,n,which_,nev,tol_,resid,ncv,v,ldv,&
          iparam,ipntr,workd,workl,lworkl,info)
     if(ido/=-1.AND.ido/=1)then
        exit
     end if
     !  Perform matrix vector multiplication: y <--- OP*x ; workd(ipntr(1))=input, workd(ipntr(2))=output
     call MatVec(N,workd(ipntr(1)),workd(ipntr(2)) )
  end do
  !
  !POST PROCESSING:
  if(info/=0)then
     write(*,'(a,i6)')'Warning/Error in DSAUPD, info = ', info
     include "error_msg_arpack.h90"
  else
     rvec = .true.
     call dseupd(rvec,'All',select,d,v,ldv,sigma,bmat,n,which_,&
          nev,tol_,resid,ncv,v,ldv,iparam,ipntr,workd,workl,lworkl,ierr)
     do j=1,neigen
        eval(j)=d(j,1)
        do i=1,ns
           evec(i,j)=v(i,j)
        enddo
     enddo
     !
     !  Compute the residual norm ||  A*x - lambda*x ||
     !  for the NCONV accurately computed eigenvalues and eigenvectors.
     if(ierr/=0)then
        write(*,'(a,i6)')'Error with DSEUPD, IERR = ',ierr
        write(*,'(a)')'Check the documentation of DSEUPD.'
        stop
     else
        nconv =  iparam(5)
     end if
     !
     include "info_msg_arpack.h90"
     !
     !if(nconv == 0) stop "ARPACK:: no converged eigenvalues have been found."
     !
  endif
  deallocate(ax,d,resid,workl,workd,v,select)
end subroutine lanczos_arpack_d
