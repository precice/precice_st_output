System testing at Sat Mar 30 18:44:30 2019
 # Status :  Passing 
 # [Job url](https://travis-ci.org/shkodm/systemtests/builds/513524773)
## Triggered by: [push](https://github.com/shkodm/systemtests/compare/2218cb89898b^...77160b8c85dc)
## Last 100 lines of the job log...
```
 #define FORTRAN(A,B) A##_  B
                      ^
[0m[91m/CalculiX/ccx_2.15/src/objectivemain_se.c:1566:21: warning: implicit declaration of function 'fixnode_' [-Wimplicit-function-declaration]
             FORTRAN(fixnode,(nobject,nk,set,nset,istartset,iendset,ialset,
                     ^
/CalculiX/ccx_2.15/src/CalculiX.h:27:22: note: in definition of macro 'FORTRAN'
 #define FORTRAN(A,B) A##_  B
                      ^
/CalculiX/ccx_2.15/src/objectivemain_se.c:106:57: warning: unused variable 'nrhs' [-Wunused-variable]
         l,idesvarbref,idesvara,idesvarb,inode,node,idof,nrhs=1,
                                                         ^
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/pardiso.c -o bin/pardiso.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/pardiso_as.c -o bin/pardiso_as.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/pcgsolver.c -o bin/pcgsolver.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/precontact.c -o bin/precontact.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/predgmres_struct_mt.c -o bin/predgmres_struct_mt.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/prediction.c -o bin/prediction.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/prediction_em.c -o bin/prediction_em.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/preiter.c -o bin/preiter.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/projectgradmain.c -o bin/projectgradmain.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0m[91m/CalculiX/ccx_2.15/src/projectgradmain.c: In function 'projectgradmain':
[0m[91m/CalculiX/ccx_2.15/src/projectgradmain.c:136:9: warning: implicit declaration of function 'mastructnmatrix' [-Wic/readfrd.c -o bin/readfrd.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/readinput.c -o bin/readinput.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/refinemesh.c -o bin/refinemesh.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/resultsstr.c -o bin/resultsstr.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0m[91m/CalculiX/ccx_2.15/src/resultsstr.c: In function 'resultsstr':
/CalculiX/ccx_2.15/src/resultsstr.c:74:32: warning: variable 'calcul_f' set but not used [-Wunused-but-set-variable]
     ITG intpointvarm,calcul_fn,calcul_f,calcul_qa,calcul_cauchy,ikin,
                                ^
[0m[91m/CalculiX/ccx_2.15/src/resultsstr.c: In function 'resultsmechmtstr':
/CalculiX/ccx_2.15/src/resultsstr.c:263:42: warning: variable 'nedelta' set but not used [-Wunused-but-set-variable]
     ITG indexfn,indexqa,indexnal,nea,neb,nedelta,list,*ilist=NULL;
                                          ^
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/results_se.c -o bin/results_se.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/rhspmain.c -o bin/rhspmain.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0m[91m/CalculiX/ccx_2.15/src/rhspmain. In function 'sensitivity':
/CalculiX/ccx_2.15/src/sensitivity.c:91:50: warning: variable 'ithickness' set but not used [-Wunused-but-set-variable]
       *iponor=NULL,*iponoelfa=NULL,*inoelfa=NULL,ithickness,iscaleflag,
                                                  ^
/CalculiX/ccx_2.15/src/sensitivity.c:90:20: warning: unused variable 'index' [-Wunused-variable]
       *nnodes=NULL,index,iregion=0,*konfa=NULL,*ipkonfa=NULL,nsurfs,
                    ^
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/sensitivity_out.c -o bin/sensitivity_out.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/stof.c -o bin/stof.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/stoi.c -o bin/stoi.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/storecontactdof.c -o bin/storecontactdof.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/stos.c -o bin/stos.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/strcmp1.c -o bin/strcmp1.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/strcmp2.c -o bin/strcmp2.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0mmpicc -g -Wall -std=c++11 -O0 -fopenmp -I./ -I./adapter -I/CalculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c /CalculiX/ccx_2.15/src/strcpy1.c -o bin/strcpy1.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0malculiX/ccx_2.15/src -I/spooles.2.2 -I/precice/src -I/usr/local/ARPACK  -DARCH="Linux" -DSPOOLES -DARPACK -DMATRIXSTORAGE -c adapter/CCXHelpers.c -o bin/CCXHelpers.o
[91mcc1: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C
[0m[91madapter/CCXHelpers.c: In function 'getXloadIndices':
adapter/CCXHelpers.c:274:6: warning: implicit declaration of function 'strcmp' [-Wimplicit-function-declaration]
  if( strcmp( loadType, "DFLUX" ) == 0 )
      ^
[0m[91madapter/CCXHelpers.c: In function 'getXbounIndices':
adapter/CCXHelpers.c:320:2: warning: enumeration value 'HEAT_FLUX' not handled in switch [-Wswitch]
  switch( couplDataType )
  ^
adapter/CCXHelpers.c:320:2: warning: enumeration value 'CONVECTION' not handled in switch [-Wswitch]
adapter/CCXHelpers.c:320:2: warning: enumeration value 'FORCES' not handled in switch [-Wswitch]
adapter/CCXHelpers.c:320:2: warning: enumeration value 'DISPLACEMENTDELTAS' not handled in switch [-Wswitch]
[0m[91madapter/CCXHelpers.c: In function 'getXloadIndexOffset':
adapter/CCXHelpers.c:416:6: warning: unused variable 'indexOffset' [-Wunused-variable]
  int indexOffset;
      ^
[0m[91madapter/CCXHelpers.c: In function 'setXload':
adapter/CCXHelpers.c:435:10: warning: unused variable 'temp' [-Wunused-variable]
   double temp = xload[xloadIndices[i] + indexOffset];
          ^
[0m[91madapter/CCXHelpers.c: In function 'setNodeForces':
adapter/CCXHelpers.c:471:7: warning: unused variable 'nodeIdx' [-Wunused-variable]
   int nodeIdx = nodes[i] - 1;
       ^
[0m[91madapter/CCXHelpers.c: In function 'concat':
adapter/CCXHelpers.c:505:19: ```
