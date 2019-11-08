## Status: Passing 
Build: [1061](https://travis-ci.org/precice/systemtests/builds/609034257) 

Job: [1061.21](https://travis-ci.org/precice/systemtests/jobs/609034278) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
 DUMMY: Closing Fortran solver dummy...
                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1291 |          0 |       1291 |          0 |          1 |
                                     advance |         87 |          0 |         39 |          0 |   0.448276 |
                                   configure |          2 |          0 |          2 |          0 |          1 |
                                    finalize |         40 |          0 |         40 |          0 |          1 |
                                  initialize |          2 |          0 |          2 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          1 |          0 |          1 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
communication to coupling partner/s
preCICE:[0m Slaves are connected
preCICE:[0m Compute read mapping from mesh "MeshOne" to mesh "MeshTwo".
preCICE:[36mWARNING: [0m 2D Mesh "MeshOne" does not contain edges. Nearest projection mapping falls back to nearest neighbor mapping.
preCICE:[0m Mapping distance min:0 max:0 avg: 0 var: 0 cnt: 1
preCICE:[0m it 1 of 3 | dt# 1 of 10 | t 0 | dt 1 | max dt 1 | ongoing yes | dt complete no | write-iteration-checkpoint | 
preCICE:[0m Compute write mapping from mesh "MeshTwo" to mesh "MeshOne".
preCICE:[0m Mapping distance min:0 max:0 avg: 0 var: 0 cnt: 1
preCICE:[0m initializeData is skipped since no data has to be initialized
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 1 of 10 | t 0 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 1 of 10 | t 0 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 1 of 10 | t 0 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 1 of 10 | t 0 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestation-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
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
preCImputeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         39 |         39 |         39 |         39 |     0.0304 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000778 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1289 |          0 |       1289 |          0 |          1 |
                                     advance |         79 |          0 |         39 |          0 |   0.493671 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         39 |          0 |         39 |          0 |          1 |
                                  initialize |          9 |          0 |          9 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          8 |          0 |          8 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |        ---> 1e854726cf1c
Removing intermediate container 55abe380d6cf
Step 29/29 : RUN mkdir /Output
 ---> Running in 134d1fd2de22
 ---> ef27720294c4
Removing intermediate container 134d1fd2de22
Successfully built ef27720294c4
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
e91ab063ecb19c2368ae9310b004aba438b140b7afdbdc682c29d7a6290aa69b

```
[
Full job log](https://api.travis-ci.org/v3/job/609034278/log.txt)