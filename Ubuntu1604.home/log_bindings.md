## Status: Passing 
Build: [1603](https://travis-ci.org/precice/systemtests/builds/646122956) 

Job: [1603.18](https://travis-ci.org/precice/systemtests/jobs/646122974) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646122956) 

---
Last 100 lines of the job log at the moment of push:
```
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |     0.0068 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        147 |          0 |        147 |          0 |          1 |
                                                                      advance |         36 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         36 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          2 |          0 |          2 |          0 |          1 |
                                                                   initialize |         85 |          0 |         85 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          5 |          0 |          5 |          0 |          1 |
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
                               initialize/partition.receiveGlobalMesh.MeshOne |         36 |          0 |         36 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializ                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        150 |          0 |        150 |          0 |          1 |
                                     advance |         37 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          0 |          0 |          0 |          0 |          0 |
                                  initialize |         90 |          0 |         90 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         77 |          0 |         77 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          7 |          0 |          7 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         80 |          0 |         80 |          0 |          1 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          1 |          0 |          1 |
    initialize/partition.prepareMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> ed35498dffcc
Removing intermediate container 6c31d614bbba
Step 34/36 : USER root
 ---> Running in 6a05482d73a2
 ---> 45c23466a830
Removing intermediate container 6a05482d73a2
Step 35/36 : RUN mkdir /Output
 ---> Running in 212dc95c8c6a
 ---> 92b2e4628de1
Removing intermediate container 212dc95c8c6a
Step 36/36 : USER [secure]
 ---> Running in 9018db74730a
 ---> 5ce7d55963d5
Removing intermediate container 9018db74730a
Successfully built 5ce7d55963d5
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
cb2bb0825822cf5d46df70b0d97ebe8e66d8d9acc65869103cd85596c5ad511d
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:32ec0b94:start=1580851257431013745,finish=1580851372977075137,duration=115546061392,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1a4e23ef[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1a4e23ef:start=1580851377084857858,finish=1580851378411625934,duration=1326768076,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:25233447[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646122974/log.txt)