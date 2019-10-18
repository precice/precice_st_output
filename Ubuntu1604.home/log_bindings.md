 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599414120) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/67d504057297...430ac8e48acf) 
## Last 100 lines of the job log at the moment of push...
```
                                                                       _GLOBAL |          1 |       1291 |       1291 |       1291 |       1291 |          1 |
                                                                      advance |         30 |       1159 |         40 |          0 |         38 |      0.898 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0612 |
                                                                   initialize |          1 |         43 |         43 |         43 |         43 |     0.0333 |
                                        initialize/m2n.acceptMasterConnection |          1 |          7 |          7 |          7 |          7 |    0.00542 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         32 |         32 |         32 |         32 |     0.0248 |
                                                               initializeData |          1 |          5 |          5 |          5 |          5 |    0.00387 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          2 |          2 |          2 |          2 |    0.00155 |



                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1297 |       1297 |       1297 |       1297 |          1 |
                                     advance |         30 |       1241 |         83 |         39 |         41 |      0.957 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         40 |         40 |         40 |         40 |     0.0308 |
                                  initialize |          1 |         12 |         12 |         12 |         12 |    0.00925 |
      initialize/m2n.requestMasterConnection |          1 |         11 |         11 |         11 |         11 |    0.00848 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000771 |
                           solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1291 |          0 |       1291 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         43 |          0 |         43 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          7 |          0 |          7 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         32 |          0 |         32 |          0 |          1 |
                                                               initializeData |          5 |          0 |          5 |          0 |          1 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          2 |          0 |          2 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1297 |          0 |       1297 |          0 |          1 |
                                     advance |         83 |          0 |         39 |          0 |    0.46988 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         40 |          0 |         40 |          0 |          1 |
                                  initialize |         12 |          0 |         12 |          0 |          1 |
      initialize/m2n.requestMasterConnection |         11 |          0 |         11 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> 581cdbdd62cb
Removing intermediate container 43815813aee5
Step 29/29 : RUN mkdir /Output
 ---> Running in 02bd54456e54
 ---> 196741c78948
Removing intermediate container 02bd54456e54
Successfully built 196741c78948
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
fe187f35ceccf681d403a597509442e6cbb652cffb7eb3ed86a38196a84d10b9
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:0345fcd8:start=1571361000412645578,finish=1571361150812573898,duration=150399928320,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:175c2312[0K$ python push.py -s -t bindings
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599414137/log.txt)