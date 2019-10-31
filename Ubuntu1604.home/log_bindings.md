## Status: Passing 
Build: [1048](https://travis-ci.org/precice/systemtests/builds/605292585) 

Job: [1048.21](https://travis-ci.org/precice/systemtests/jobs/605292606) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
preCICE:[0m it 2 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 8 of 10 | t 7 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m it 1 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 9 of 10 | t 8 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m it 1 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          3 |          3 |          3 |          3 |    0.00232 |


Run finished at Thu Oct 31 02:41:26 2019
Global runtime       = 1287ms / 1.287s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1287 |       1287 |       1287 |       1287 |          1 |
                                     advance |         30 |       1238 |         80 |         39 |         41 |      0.962 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         41 |         41 |         41 |         41 |     0.0319 |
                                  initialize |          1 |          4 |          4 |          4 |          4 |    0.00311 |
      initialize/m2n.requestMasterConnection |          1 |          2 |          2 |          2 |          2 |    0.00155 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000777 |
                           solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000777 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------------p.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          2 |          0 |          2 |          0 |          1 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         37 |          0 |         37 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          3 |          0 |          3 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
                        0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 6da2000dea51
Removing intermediate container 790a4a0470f0
Step 29/29 : RUN mkdir /Output
 ---> Running in 45f270d687ba
 ---> 4164b5304fa0
Removing intermediate container 45f270d687ba
Successfully built 4164b5304fa0
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
c4677459da215a0c5837e3b3627c1eddf218d3b901e3e1b5945d448161b9f3c3

```
[
Full job log](https://api.travis-ci.org/v3/job/605292606/log.txt)