## Status: Passing 
Build: [1574](https://travis-ci.org/precice/systemtests/builds/644725337) 

Job: [1574.21](https://travis-ci.org/precice/systemtests/jobs/644725358) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4999f333493e1d71bc360afa644a77d2630ce82e...b42adf2e689a763071326fd2ccb4fad54589f1aa) 

---
Last 100 lines of the job log at the moment of push:
```
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          2 |          2 |          2 |          2 |     0.0137 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        146 |          0 |        146 |          0 |          1 |
                                                                      advance |         37 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         36 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          0 |          0 |          0 |          0 |          0 |
                                                                   initialize |         91 |          0 |         91 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          2 |          0 |          2 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |         42 |          0 |         42 |          0 |          1 |
                                  initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
                                    initialize/m2n.exchangeVertexDistribution |         40 |          0 |         40 |          0 |          1 |
                                                   initialize/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          4 |          0 |          4 |          0 |          1 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          1 |          0 |          1 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                     initialize/partition.prepareMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         38 |          0 |         38 |          0 |          1 |
                                                               initializeData |          3 |          0 |          3 |          0 |          1 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializ                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        151 |          0 |        151 |          0 |          1 |
                                     advance |         49 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          0 |          0 |          0 |          0 |          0 |
                                  initialize |         89 |          0 |         89 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         75 |          0 |         75 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          9 |          0 |          9 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         77 |          0 |         77 |          0 |          1 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
    initialize/partition.prepareMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          2 |          0 |          2 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 8e1fc470f65f
Removing intermediate container 3a428ee4d70c
Step 34/36 : USER root
 ---> Running in 0077e59559b0
 ---> 9a5678e9117e
Removing intermediate container 0077e59559b0
Step 35/36 : RUN mkdir /Output
 ---> Running in a5e9a3c1aec8
 ---> d09649e659a5
Removing intermediate container a5e9a3c1aec8
Step 36/36 : USER [secure]
 ---> Running in cfdbbea0086f
 ---> 62f57e60f15d
Removing intermediate container cfdbbea0086f
Successfully built 62f57e60f15d
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
443873a2869a6636dfb59f9e5269d5851833ebffe6234f3d740f3589f5af5b8b
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:0020c698:start=1580557689200240776,finish=1580557799960579792,duration=110760339016,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01e77b5f:start=1580557803850418216,finish=1580557805209514585,duration=1359096369,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:11a88a34[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/644725358/log.txt)