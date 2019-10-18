 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599707111) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/677b242d01cf...3df000d61aa4) 
## Last 100 lines of the job log at the moment of push...
```
 preCICE:[0m it 3 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m it 1 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m it 1 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 |  | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
Run finished at Fri Oct 18 16:55:51 2019
Global runtime       = 1298ms / 1.298s
Number of processors = 1
# Rank: 0

                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1298 |       1298 |       1298 |       1298 |          1 |
                                                                      advance |         30 |       1158 |         40 |          0 |         38 |      0.892 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0609 |
                                                                   initialize |          1 |         57 |         57 |         57 |         57 |     0.0439 |
                                        initialize/m2n.acceptMasterConnection |          1 |         13 |         13 |         13 |         13 |       0.01 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         39 |         39 |         39 |         39 |       0.03 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
         advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         57 |          0 |         57 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |         13 |          0 |         13 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         39 |          0 |         39 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 DUMMY: Closing Fortran solver dummy...
 ---> faaa5cfefbef
Removing intermediate container 286292c19476
Step 29/29 : RUN mkdir /Output
 ---> Running in a7001296da8b
 ---> e34d51d0e660
Removing intermediate container a7001296da8b
Successfully built e34d51d0e660
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
85a74a83aa6d99d0003523dbb1882a880d81c2f016fe2fa985779a8348ac97be
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:1642 ```
[Full job log](https://api.travis-ci.org/v3/job/599707128/log.txt)