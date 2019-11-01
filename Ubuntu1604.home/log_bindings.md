## Status: Passing 
Build: [1052](https://travis-ci.org/precice/systemtests/builds/605812235) 

Job: [1052.21](https://travis-ci.org/precice/systemtests/jobs/605812256) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
preCICE:[0m it 3 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
Run finished at Fri Nov  1 02:42:20 2019
Global runtime       = 1288ms / 1.288s
Run finished at Fri Nov  1 02:42:20 2019
Global runtime       = 1289ms / 1.289s
Number of processors = 1
Number of processors = 1
# Rank: 0
# Rank: 0


                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1289 |       1289 |       1289 |       1289 |          1 |
                                     advance |         30 |       1237 |         79 |         39 |         41 |       0.96 |
                                   configure |          1 |          5 |          5 |          5 |          5 |    0.00388 |
                                    finalize |          1 |         40 |         40 |         40 |         40 |      0.031 |
                                  initialize |          1 |          4 |          4 |          4 |          4 |     0.0031 |
      initialize/m2n.requestMasterConnection |          1 |          2 |          2 |          2 |          2 |    0.00155 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          3 |          3 |          3 |          3 |    0.00233 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000776 |
                           solver.initialize |          1 |          2 |          2 |          2 |          2 |    0.00155 |


                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1288 |       1288 |       1288 |       1288 |          1 |
                                                                      advance |         30 |       1158 |         40 |          0 |         38 |      0.899 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0613 |
                                                                   initialize |          1 |         47 |         47 |         47 |         47 |     0.0365 |
                                        initialize/m2n.acceptMasterConnection |          1 |          6 |          6 |          6 |          6 |    0.00466 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         39 |         39 |         39 |         39 |     0.0303 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000776 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1289 |          0 |       1289 |          0 |          1 |
                                     advance |         79 |          0 |         39 |          0 |   0.493671 |
                                   configure |          5 |          0 |          5 |          0 |          1 |
                                    finalize |         40 |          0 |         40 |          0 |          1 |
                                  initialize |          4 |          0 |          4 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          2 |          0 |          2 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |    79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         47 |          0 |         47 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          6 |          0 |          6 |          0 |          1 |
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
 ---> a7a423b00c79
Removing intermediate container 12beba19afb7
Step 29/29 : RUN mkdir /Output
 ---> Running in 9c7b9a53e1b0
 ---> 68c7cfc51b56
Removing intermediate container 9c7b9a53e1b0
Successfully built 68c7cfc51b56
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
60132f872f6ea386bcfdf537bb57ff9046d9c8f306eea53deab8a2f71da307f7

```
[
Full job log](https://api.travis-ci.org/v3/job/605812256/log.txt)