## Status: Passing 
Build: [1598](https://travis-ci.org/precice/systemtests/builds/645892844) 

Job: [1598.21](https://travis-ci.org/precice/systemtests/jobs/645892871) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/07c487419fcd18bdb04b9d9fef13c8b1318f3bef...6213c52a25101c0051df0fbc215ba9f941209daa) 

---
Last 100 lines of the job log at the moment of push:
```
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          1 |          0 |          0 |          0 |    0.00513 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |    0.00513 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        195 |          0 |        195 |          0 |          1 |
                                                                      advance |         37 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         35 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          1 |          0 |          1 |
                                                                     finalize |         21 |          0 |         21 |          0 |          1 |
                                                                   initialize |         90 |          0 |         90 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          1 |          0 |          1 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |         42 |          0 |         42 |          0 |          1 |
                                  initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
                                    initialize/m2n.exchangeVertexDistribution |         40 |          0 |         40 |          0 |          1 |
                                                   initialize/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          1 |          0 |          1 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                     initialize/partition.prepareMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         37 |          0 |         37 |          0 |          1 |
                                                               initializeData |          1 |          0 |          1 |          0 |          1 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializ                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        182 |          0 |        182 |          0 |          1 |
                                     advance |         42 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |          0 |          1 |          0 |          1 |
                                  initialize |         90 |          0 |         90 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         74 |          0 |         74 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          9 |          0 |          9 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         77 |          0 |         77 |          0 |          1 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
    initialize/partition.prepareMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          2 |          0 |          2 |          0 |          1 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> cacb5e5347a3
Removing intermediate container 2a754e3762a8
Step 34/36 : USER root
 ---> Running in 94b6aeb1e862
 ---> df0f3210623b
Removing intermediate container 94b6aeb1e862
Step 35/36 : RUN mkdir /Output
 ---> Running in 0041ff98441d
 ---> fae39b5f2483
Removing intermediate container 0041ff98441d
Step 36/36 : USER [secure]
 ---> Running in 653b76c8ea94
 ---> 04337f24039d
Removing intermediate container 653b76c8ea94
Successfully built 04337f24039d
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
bcb716946679b6bc6e3c470ce79118363bf066e08b122a34745d1c0dd53230cc
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:03349368:start=1580817980566321027,finish=1580818097639343498,duration=117073022471,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04c7b443[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04c7b443:start=1580818101894771215,finish=1580818103382669638,duration=1487898423,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:281065c8[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/645892871/log.txt)