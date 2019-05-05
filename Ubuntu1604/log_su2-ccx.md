System testing at Sun May  5 12:23:43 2019
 # Status : Failing
 # [Job url](https://travis-ci.org/shkodm/systemtests/builds/528423596)
## Triggered by: [push](https://github.com/shkodm/systemtests/compare/b16a26eb6775...fb2d43b9934d)
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/57b164a8d4112c5e57a4eef1f636d3c109524d69...269012c2748bf5513bc244ad9f50d886de05a18b)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/01ae247b442d...9a98e5f79463)
## Last 100 lines of the job log at the moment of push...
```
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/stress_sen_dv.c -o bin/stress_sen_dv.o
[91m/CalculiX/ccx_2.15/src/stress_sen_dv.c: In function 'stress_sen_dv':
/CalculiX/ccx_2.15/src/stress_sen_dv.c:50:15: warning: unused variable 'kspart' [-Wunused-variable]
     *eme=NULL,kspart,dksper;
               ^
/CalculiX/ccx_2.15/src/stress_sen_dv.c:46:28: warning: unused variable 'unperturbflag' [-Wunused-variable]
       *inum=NULL,nprintl=0,unperturbflag,nfield,ndim,iorienglob,
                            ^
/CalculiX/ccx_2.15/src/stress_sen_dv.c:46:18: warning: unused variable 'nprintl' [-Wunused-variable]
       *inum=NULL,nprintl=0,unperturbflag,nfield,ndim,iorienglob,
                  ^
[0m[91m/CalculiX/ccx_2.15/src/stress_sen_dv.c:44:35: warning: unused variable 'iactpos' [-Wunused-variable]
   ITG symmetryflag=0,mt=mi[1]+1,i,iactpos,calcul_fn,list,
                                   ^
/CalculiX/ccx_2.15/src/stress_sen_dv.c:44:33: warning: unused variable 'i' [-Wunused-variable]
   ITG symmetryflag=0,mt=mi[1]+1,i,iactpos,calcul_fn,list,
                                 ^
/CalculiX/ccx_2.15/src/stress_sen_dv.c:44:7: warning: variable 'symmetryflag' set but not used [-Wunused-but-set-variable]
   ITG symmetryflag=0,mt=mi[1]+1,i,iactpos,calcul_fn,list,
       ^
[0mmpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/stress_sen_dx.c -o bin/stress_sen_dx.o
[91m/CalculiX/ccx_2.15/src/stress_sen_dx.c: In function 'stress_sen_dx':
/CalculiX/ccx_2.15/src/stress_sen_dx.c:49:15: warning: unused variable 'kspart' [-Wunused-variable]
     *eme=NULL,kspart,dksper;
               ^
/CalculiX/ccx_2.15/src/stress_sen_dx.c:45:28: warning: unused variable 'unperturbflag' [-Wunused-variable]
       *inum=NULL,nprintl=0,unperturbflag,nfield,ndim,iorienglob,
                            ^
/CalculiX/ccx_2.15/src/stress_sen_dx.c:45:18: warning: unused variable 'nprintl' [-Wunused-variable]
       *inum=NULL,nprintl=0,unperturbflag,nfield,ndim,iorienglob,
                  ^
/CalculiX/ccx_2.15/src/stress_sen_dx.c:43:35: warning: unused variable 'iactpos' [-Wunused-variable]
   ITG symmetryflag=0,mt=mi[1]+1,i,iactpos,calcul_fn,list,
                                   ^
/CalculiX/ccx_2.15/src/stress_sen_dx.c:43:33: warning: unused variable 'i' [-Wunused-variable]
   ITG symmetryflag=0,mt=mi[1]+1,i,iactpos,calcul_fn,list,
                                 ^
/CalculiX/ccx_2.15/src/stress_sen_dx.c:43:7: warning: variable 'symmetryflag' set but not used [-Wunused-but-set-variable]
   ITG symmetryflag=0,mt=mi[1]+1,i,iampicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/strsplt.c -o bin/strsplt.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/tau.c -o bin/tau.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/thicknessmain.c -o bin/thicknessmain.o
[91mIn file included from /CalculiX/ccx_2.15/src/thicknessmain.c:23:0:
/CalculiX/ccx_2.15/src/thicknessmain.c: In function 'thicknessmt':
[0m[91m/CalculiX/ccx_2.15/src/thicknessmain.c:176:13: warning: implicit declaration of function 'thickness_' [-Wimplicit-function-declaration]
     FORTRAN(thickness,(dgdx1,nobject1,nodedesiboun1,&ndesiboun1,objectset1,
             ^
/CalculiX/ccx_2.15/src/CalculiX.h:27:22: note: in definition of macro 'FORTRAN'
 #define FORTRAN(A,B) A##_  B
                      ^
/CalculiX/ccx_2.15/src/thicknessmain.c:165:9: warning: variable 'indexr' set but not used [-Wunused-but-set-variable]
     ITG indexr,ndesia,ndesib,ndesidelta;
         ^
[0mmpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/tiedcontact.c -o bin/tiedcontact.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/transitionmain.c -o bin/transitionmain.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/u_calloc.c -o bin/u_calloc.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/u_free.c -o bin/u_free.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/u_realloc.c -o bin/u_realloc.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/v_betrag.c -o bin/v_betrag.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/v_prod.c -o bin/v_prod.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/v_result.c -o bin/v_result.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/writeheading.c -o bin/writeheading.o
mpicc -Wall -O3 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c nonlingeo_precice.c -o bin/nonlingeo_precice.o
[91mIn file included from adapter/CCXHelpers.h:17:0,
                 from adapter/PreciceInterface.h:15,
                 from nonlingeo_precice.c:36:
nonlingeo_precice.c: In function 'nonlingeo_precice':
[0m[91mnonlingeo_precice.c:2189:13: warning: implicit declaration of function 'predgmres_struct_' [-Wimplicit-function-declaration]
     FORTRAN(predgmres_struct,(&neq[1],b,sol,&nelt,irow,jq,au,
             ^
adapter/../CalculiX.h:27:22: note: in definition of macro 'FORTRAN'
 #define FORTRAN(A,B) A##_  B
                      ^
[0m[91mnonlingeo_precice.c:2236:8: warning: implicit declaration of function 'matrixstorage' [-Wimplicit-function-declaration]
        matrixstorage(ad,&au,adb,aub,&sigma,icol,&irow,&neq[1],&nzs[1],
        ^
[0m[91mnonlingeo_precice.c:127:64: warning: unused variable 'ielblk' [-Wunused-variable]
       *iendblk=NULL,*nblket=NULL,*nblkze=NULL,nblk,*konf=NULL,*ielblk=NULL,
                                                                ^
nonlingeo_precice.c:127:47: warning: unused variable 'nblk' [-Wunused-variable]
       *iendblk=NULL,*nblket=NULL,*nblkze=NULL,nblk,*konf=NULL,*ielblk=NULL,
                                               ^
nonlingeo_precice.c:127:35: warning: unused variable 'nblkze' [-Wunused-variable]
       *iendblk=NULL,*nblket=NULL,*nblkze=NULL,nblk,*konf=NULL,*ielblk=NULL,
                                   ^
nonlingeo_precice.c:127:22: warning: unused variable 'nblket' [-Wunused-variable]
       *iendblk=NULL,*nblket=NULL,*nblkze=NULL,nblk,*konf=NULL,*ielblk=NULL,
                      ^
nonlingeo_precice.c:127:8: warning: unused variable 'iendblk' [-Wunused-variable]
       *iendblk=NULL,*nblket=NULL,*nblkze=NULL,nblk,*konf=NULL,*ielblk=NULL,
        ^
nonlingeo_precice.c:126:54: warning: unused variable 'istartblk' [-Wunused-variable]
       j=0,*ifatie=NULL,n,inoelsize=0,isensitivity=0,*istartblk=NULL,
                                                      ^
nonlingeo_precice.c:125:62: warning: unused variable 'nrhs' [-Wunused-variable]
       *nelemload=NULL,*iamload=NULL,ncontacts=0,inccontact=0,nrhs=1,
                                                              ^
nonlingeo_precice.c:116:69: warning: variable 'iex' set but not used [-Wunused-but-set-variable]
       *nelemface=NULL,*ipoface=NULL,*nodface=NULL,*ifreestream=NULL,iex,
                                                                     ^
[0m```
[Full job log](https://api.travis-ci.org/v3/job/528423600/log.txt)