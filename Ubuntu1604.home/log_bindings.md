## Status: Passing 
Build: [1613](https://travis-ci.org/precice/systemtests/builds/647273995) 

Job: [1613.21](https://travis-ci.org/precice/systemtests/jobs/647274016) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |    0.00714 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        140 |          0 |        140 |          0 |          1 |
                                                                      advance |         38 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         38 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          0 |          0 |          0 |          0 |          0 |
                                                                   initialize |         86 |          0 |         86 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          1 |          0 |          1 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |         42 |          0 |         42 |          0 |          1 |
                                  initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
                                    initialize/m2n.exchangeVertexDistribution |         40 |          0 |         40 |          0 |          1 |
                                                   initialize/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                     initialize/partition.prepareMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         35 |          0 |         35 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializRun finished at Fri Feb  7 12:27:53 2020
Global runtime       = 146ms / 0.146s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |        146 |        146 |        146 |        146 |          1 |
                                     advance |         30 |         50 |         39 |          0 |          1 |      0.342 |
                     advance/m2n.receiveData |         30 |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |         30 |          3 |          1 |          0 |          0 |     0.0205 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |          2 |          2 |          2 |          2 |     0.0137 |
                                  initialize |          1 |         89 |         89 |         89 |         89 |       0.61 |
 initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0137 |
   initialize/m2n.exchangeVertexDistribution |          1 |         78 |         78 |         78 |         78 |      0.534 |
      initialize/m2n.requestMasterConnection |          1 |          7 |          7 |          7 |          7 |     0.0479 |
      initialize/m2n.requestSlavesConnection |          1 |         80 |         80 |         80 |         80 |      0.548 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
    initialize/partition.prepareMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          3 |          3 |          3 |          3 |     0.0205 |


eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        146 |          0 |        146 |          0 |          1 |
                                     advance |         39 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          1 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          2 |          0 |          2 |          0 |          1 |
                                  initialize |         89 |          0 |         89 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         78 |          0 |         78 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          7 |          0 |          7 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         80 |          0 |         80 |          0 |          1 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
    initialize/partition.prepareMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          3 |          0 |          3 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 DUMMY: Closing Fortran solver dummy...
 ---> 08f2ffbd1d2b
Removing intermediate container 4bb8f30e7a85
 ---> Running in a8ce878e448d
 ---> ac95bd8ed6d7
Removing intermediate container a8ce878e448d
Successfully built ac95bd8ed6d7
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
f3ed82da1799c3df54445b7cde1362aeed533df523a1c56b1a30f44774242e3f
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:11293046:start=1581078351559726578,finish=1581078474365319671,duration=122805593093,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/647274016/log.txt)