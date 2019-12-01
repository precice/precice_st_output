## Status: Passing 
Build: [1237](https://travis-ci.org/precice/systemtests/builds/619351844) 

Job: [1237.17](https://travis-ci.org/precice/systemtests/jobs/619351861) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5cd65d21e48f...60b68152f174) 

---
Last 100 lines of the job log at the moment of push:
```
                                  initialize |          1 |         12 |         12 |         12 |         12 |    0.00925 |
      initialize/m2n.requestMasterConnection |          1 |          9 |          9 |          9 |          9 |    0.00694 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          1 |          1 |          1 |          1 |   0.000771 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000771 |
                           solver.initialize |          1 |          3 |          3 |          3 |          3 |    0.00231 |


                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1290 |       1290 |       1290 |       1290 |          1 |
                                                                      advance |         30 |       1156 |         40 |          0 |         38 |      0.896 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0612 |
                                                                   initialize |          1 |         48 |         48 |         48 |         48 |     0.0372 |
                                        initialize/m2n.acceptMasterConnection |          1 |          5 |          5 |          5 |          5 |    0.00388 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         38 |         38 |         38 |         38 |     0.0295 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          4 |          4 |          4 |          4 |     0.0031 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1290 |          0 |       1290 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         48 |          0 |         48 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          5 |          0 |          5 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         38 |          0 |         38 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          4 |          0 |          4 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1297 |          0 |       1297 |          0 |          1 |
                                     advance |         81 |          0 |         39 |          0 |   0.481481 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         40 |          0 |         40 |          0 |          1 |
                                  initialize |         12 |          0 |         12 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          9 |          0 |          9 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          1 |          0 |          1 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          3 |          0 |          3 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> f6e74904aba0
Removing intermediate container 57d26742e044
Step 25/25 : RUN mkdir /Output
 ---> Running in 91f1f20c397f
 ---> ae865fb0f488
Removing intermediate container 91f1f20c397f
Successfully built ae865fb0f488
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
7cead82e6560bcd883cf610c028c7aa2066387100b807a25fb3beb645575a497
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:0a546dd6:start=1575240445139213422,finish=1575240571820244796,duration=126681031374,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1a1f4800[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1a1f4800:start=1575240576392108333,finish=1575240578048938161,duration=1656829828,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1572cfb2[0KCloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/619351861/log.txt)