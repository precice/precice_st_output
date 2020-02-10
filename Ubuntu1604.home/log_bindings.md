## Status: Passing 
Build: [1650](https://travis-ci.org/precice/systemtests/builds/648350351) 

Job: [1650.21](https://travis-ci.org/precice/systemtests/jobs/648350372) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |          6 |          6 |          6 |          6 |      0.037 |
                                                                   initialize |          1 |         91 |         91 |         91 |         91 |      0.562 |
                                        initialize/m2n.acceptMasterConnection |          1 |          9 |          9 |          9 |          9 |     0.0556 |
                                        initialize/m2n.acceptSlavesConnection |          1 |         42 |         42 |         42 |         42 |      0.259 |
                                  initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0123 |
                                    initialize/m2n.exchangeVertexDistribution |          1 |         40 |         40 |         40 |         40 |      0.247 |
                                                   initialize/m2n.receiveData |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                     initialize/partition.prepareMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         35 |         35 |         35 |         35 |      0.216 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |    0.00617 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        162 |          0 |        162 |          0 |          1 |
                                                                      advance |         38 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         38 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          6 |          0 |          6 |          0 |          1 |
                                                                   initialize |         91 |          0 |         91 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          9 |          0 |          9 |          0 |          1 |
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
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> c5fd844bd8fd
Removing intermediate container f6c1b5ee577c
Step 34/36 : USER root
 ---> Running in 822c1ee67023
 ---> c6d1c23dd4b9
Removing intermediate container 822c1ee67023
Step 35/36 : RUN mkdir /Output
 ---> Running in 958a227ace41
 ---> 5c69e348b3d7
Removing intermediate container 958a227ace41
Step 36/36 : USER [secure]
 ---> Running in f872ed3b9705
 ---> 41a435dde297
Removing intermediate container f872ed3b9705
Successfully built 41a435dde297
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
7c90ede00441a3bcf7360e7f28ededf243617b8d3877d9699de0ad1a34939292
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:14cab6b0:start=1581335254417516747,finish=1581335375872281510,duration=121454764763,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:3a8d32fc[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:3a8d32fc:start=1581335380224741653,finish=1581335381683447785,duration=1458706132,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:200ca854[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/648350372/log.txt)