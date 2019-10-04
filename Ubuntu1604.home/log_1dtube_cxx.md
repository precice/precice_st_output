 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593511816) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/ac9e17230162...f01784f81bb4) 
## Last 100 lines of the job log at the moment of push...
```
  ---> Running in 11c1fa6c8441
 ---> ebab0ce482e5
Removing intermediate container 11c1fa6c8441
Step 6/11 : RUN mkdir -p /Output/Postproc
 ---> Running in af3a742d5666
 ---> 687ec1b009c3
Removing intermediate container af3a742d5666
Step 7/11 : WORKDIR /home/[secure]/
 ---> 6cf19e61aecf
Removing intermediate container d8e8c8430d84
Step 8/11 : RUN git clone https://github.com/Eder-K/elastictube1d.git
 ---> Running in 3b763879655f
[91mCloning into 'elastictube1d'...
[0m ---> 9c019c65b943
Removing intermediate container 3b763879655f
Step 9/11 : WORKDIR /home/[secure]/elastictube1d/elastictube1d-cxx
 ---> fe5e6750aa85
Removing intermediate container d2520f3babf6
Step 10/11 : RUN cmake . && make all && ./Allrun-cxx
 ---> Running in c158055752bf
-- The CXX compiler identification is GNU 5.4.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Build configuration: Debug
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Found MPI_CXX: /usr/lib/openmpi/lib/libmpi_cxx.so (found version "3.0") 
-- Found MPI: TRUE (found version "3.0") found components:  CXX 
[91m/usr/lib/openmpi/lib/libmpi_cxx.so/usr/lib/openmpi/lib/libmpi.so
[0m-- Looking for sgemm_
-- Looking for sgemm_ - not found
-- Looking for sgemm_
-- Looking for sgemm_ - found
-- Found BLAS: /usr/lib/libblas.so  
-- Looking for cheev_
-- Looking for cheev_ - found
-- A library with LAPACK API found.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/[secure]/elastictube1d/elastictube1d-cxx
Scanning dependencies of target FluidSolver
[  7%] Building CXX object CMakeFiles/FluidSolver.dir/FluidSolver_Serial/fluid_solver.cpp.o
[ 15%] Building CXX object CMakeFiles/FluidSolver.dir/FluidSolver_Serial/fluid_nl.cpp.o
[ 23%] Linking CXX executable FluidSolver
[ 23%] Built target FluidSolver
Scanning dependencies of target StructureSolver
[ 30%] Building CXX object CMakeFiles/StructureSolver.dir/StructureSolver_Serial/structure_solver.cpp.o
[ 38%] Linking CXX executable StructureSolver
[ 38%] Built target StructureSolver
Scanning dependencies of target StructureSolverParallel
[ 46%] Building CXX object CMakeFiles/StructureSolverParallel.dir/StructureSolver_Parallel/structureDataDisplay.cpp.o
[ 53%] Building CXX object CMakeFiles/StructureSolverParallel.dir/StructureSolver_Parallel/StructureSolver.cpp.o
[ 61%] Building CXX object CMakeFiles/StructureSolverParallel.dir/StructureSolver_Parallel/structureComputeSolution.cpp.o
[ 69%] Linking CXX executable StructureSolverParallel
[ 69%] Built target StructureSolverParallel
Scanning dependencies of target FluidSolverParallel
[ 76%] Building CXX object CMakeFiles/FluidSolverParallel.dir/FluidSolver_Parallel/fluidDataDisplay.cpp.o
[ 84%] Building CXX object CMakeFiles/FluidSolverParallel.dir/FluidSolver_Parallel/FluidSolver.cpp.o
[ 92%] Building CXX object CMakeFiles/FluidSolverParallel.dir/FluidSolver_Parallel/fluidComputeSolution.cpp.o
[100%] Linking CXX executable FluidSolverParallel
[100%] Built target FluidSolverParallel
Starting Fluid participant...
Starting Structure participant...

Waiting for participants to finish...
(you may run 'tail -f Fluid.log' in another terminal to check the progress)
Fluid participant finished. Waiting for Structure participant...
Structure participant finished.

Simulation completed successfully! Output files of the simulation were written to 'Postproc/out_fluid_*.vtk'.
 ---> 9d2b725c433d
Removing intermediate container c158055752bf
Step 11/11 : RUN cp *.json *.log /Output/ &&     cp Postproc/*.vtk /Output/Postproc/
 ---> Running in c4b16b2aa85e
 ---> 1677d6baa887
Removing intermediate container c4b16b2aa85e
Successfully built 1677d6baa887
Successfully tagged st_1dtube_cxx-ubuntu1604.home-develop:latest
3fcc3d50be39cf2c31352af3dcf1cbfef2623609283cec5523fc5d0dcb1a6e21
awk: cmd. line:6: (FILENAME=- FNR=2) fatal: division by zero attempted
EXECUTING: docker build --network=host --file Dockerfile --tag st_1dtube_cxx-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_1dtube_cxx-ubuntu1604.home-develop st_1dtube_cxx-ubuntu1604.home-develop
EXECUTING: docker cp st_1dtube_cxx-ubuntu1604.home-develop:Output . 
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/Test_1dtube_cxx/referenceOutput /home/travis/build/[secure]/systemtests/tests/Test_1dtube_cxx/Output
travis_time:end:066cbc80:start=1570204791804409031,finish=1570204861420136837,duration=69615727806,event=script[0K[32;1mThe command "python system_testing.py -s 1dtube_cxx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:19f74f60[0K$ python push.py -s -t 1dtube_cxx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593511842/log.txt)