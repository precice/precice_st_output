 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598541158) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/478596e1ce45...2f42d88d1871) 
## Last 100 lines of the job log at the moment of push...
```
  DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
 Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1287 |       1287 |       1287 |       1287 |          1 |
                                                                      advance |         30 |       1158 |         40 |          0 |         38 |        0.9 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          1 |          1 |          1 |          1 |   0.000777 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0614 |
                                                                   initialize |          1 |         46 |         46 |         46 |         46 |     0.0357 |
                                        initialize/m2n.acceptMasterConnection |          1 |          7 |          7 |          7 |          7 |    0.00544 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         37 |         37 |         37 |         37 |     0.0287 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000777 |


Run finished at Wed Oct 16 09:33:11 2019
Global runtime       = 1282ms / 1.282s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1282 |       1282 |       1282 |       1282 |          1 |
                                     advance |         30 |       1231 |         73 |         39 |         41 |       0.96 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         39 |         39 |         39 |         39 |     0.0304 |
                                  initialize |          1 |          6 |          6 |          6 |          6 |    0.00468 |
      initialize/m2n.requestMasterConnection |          1 |          1 |          1 |          1 |          1 |    0.00078 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |    0.00078 |
                           solver.initialize |          1 |          2 |          2 |          2 |          2 |    0.00156 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1282 |          0 |       1282 |          0 |          1 |
                                     advance |         73 |          0 |                                  _GLOBAL |       1287 |          0 |       1287 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          1 |          0 |          1 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         46 |          0 |         46 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          7 |          0 |          7 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         37 |          0 |         37 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 8a5a809f348a
Removing intermediate container 86c2d3fb4bc3
Step 29/29 : RUN mkdir /Output
 ---> Running in 73bdc1065281
 ---> 46588286769b
Removing intermediate container 73bdc1065281
Successfully built 46588286769b
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
208c0aa87b0ec1f7e17c34aaa58930e998790d7822dc2d15b08d6b0250e2a77b
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:1081fd80:start=1571218243108388012,finish=1571218392012790084,duration=148904402072,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:3926bbd8[0K$ python push.py -s -t bindings
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598541175/log.txt)