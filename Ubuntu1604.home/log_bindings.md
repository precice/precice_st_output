## Status: Passing 
Build: [978](https://travis-ci.org/precice/systemtests/builds/599812617) 

Job: [978.17](https://travis-ci.org/precice/systemtests/jobs/599812634) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 

---
Last 100 lines of the job log at the moment of push:
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
preCICE:[0m it 1 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 10 of 10 | t 9 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
pr   75 |         39 |         41 |      0.956 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         39 |         39 |         39 |         39 |     0.0302 |
                                  initialize |          1 |         14 |         14 |         14 |         14 |     0.0108 |
      initialize/m2n.requestMasterConnection |          1 |         12 |         12 |         12 |         12 |     0.0093 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000775 |
                           solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000775 |


                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1285 |       1285 |       1285 |       1285 |          1 |
                                                                      advance |         30 |       1158 |         40 |          0 |         38 |      0.901 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          1 |          1 |          1 |          1 |   0.000778 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0615 |
                                                                   initialize |          1 |         45 |         45 |         45 |         45 |      0.035 |
                                        initialize/m2n.acceptMasterConnection |          1 |          7 |          7 |          7 |          7 |    0.00545 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         36 |         36 |         36 |         36 |      0.028 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1291 |          0 |       1291 |          0 |          1 |
                                     advance |         75 |          0 |         39 |          0 |       0.52 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         39 |          0 |         39 |          0 |          1 |
                                  initialize |         14 |          0 |         14 |          0 |          1 |
      initialize/m2n.requestMasterConnection |         12 |          0 |         12 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |   initialize |         45 |          0 |         45 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          7 |          0 |          7 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         36 |          0 |         36 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> deb2b95d9f11
Removing intermediate container 386c75ef4018
Step 29/29 : RUN mkdir /Output
 ---> Running in 03fe790c81ef
 ---> 8804fc18294a
Removing intermediate container 03fe790c81ef
Successfully built 8804fc18294a
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
3e6c96792938ace92602e6c5f9966ef387452b5dbbdf87e63d3a61650a7656e3
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:21c6f500:start=1571438788594780701,finish=1571438934007601048,duration=145412820347,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0170a4d8[0K$ python push.py -s -t bindings
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/599812634/log.txt)