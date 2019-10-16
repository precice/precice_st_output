 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598441565) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/478596e1ce45) 
## Last 100 lines of the job log at the moment of push...
```
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
preCI | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
Run finished at Wed Oct 16 02:58:12 2019
Global runtime       = 1292ms / 1.292s
Number of processors = 1
# Rank: 0

                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1292 |       1292 |       1292 |       1292 |          1 |
                                                                      advance |         30 |       1158 |         40 |          0 |         38 |      0.896 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0611 |
                                                                   initialize |          1 |         52 |         52 |         52 |         52 |     0.0402 |
                                        initialize/m2n.acceptMasterConnection |          1 |         13 |         13 |         13 |         13 |     0.0101 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         29 |         29 |         29 |         29 |     0.0224 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
     shOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         52 |          0 |         52 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |         13 |          0 |         13 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         29 |          0 |         29 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1285 |          0 |       1285 |          0 |          1 |
                                     advance |         75 |          0 |         39 |          0 |       0.52 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         43 |          0 |         43 |          0 |          1 |
                                  initialize |          3 |          0 |          3 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          1 |          0 |          1 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> ead899849b06
Removing intermediate container 14510055b63b
Step 29/29 : RUN mkdir /Output
 ---> Running in a4d0524a9879
 ---> cc386b7d21f7
Removing intermediate container a4d0524a9879
Successfully built cc386b7d21f7
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
2c93664b2ec22bb38edd42fe4cefff8b75b4689122108564b0e7c54e0a449597
 ```
[Full job log](https://api.travis-ci.org/v3/job/598441589/log.txt)