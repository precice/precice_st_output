## Status: Passing 
Build: [1470](https://travis-ci.org/precice/systemtests/builds/638788530) 

Job: [1470.22](https://travis-ci.org/precice/systemtests/jobs/638788555) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        166 |          0 |        166 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         39 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          2 |          0 |          2 |          0 |          1 |
                                                                   initialize |         89 |          0 |         89 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          4 |          0 |          4 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |         42 |          0 |         42 |          0 |          1 |
                                  initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
                                    initialize/m2n.exchangeVertexDistribution |         40 |          0 |         40 |          0 |          1 |
                                                   initialize/m2n.receiveData |          2 |          0 |          2 |          0 |          1 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         37 |          0 |         37 |          0 |          1 |
                                                               initializeData |          1 |          0 |          1 |          0 |          1 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializRun finished at Sat Jan 18 11:38:16 2020
Global runtime       = 183ms / 0.183s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |        183 |        183 |        183 |        183 |          1 |
                                     advance |         30 |         74 |         44 |          0 |          2 |      0.404 |
                     advance/m2n.receiveData |         30 |          1 |          0 |          0 |          0 |    0.00546 |
                        advance/m2n.sendData |         30 |         10 |          1 |          0 |          0 |     0.0546 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         10 |         10 |         10 |         10 |     0.0546 |
                                  initialize |          1 |         93 |         93 |         93 |         93 |      0.508 |
 initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0109 |
   initialize/m2n.exchangeVertexDistribution |          1 |         77 |         77 |         77 |         77 |      0.421 |
      initialize/m2n.requestMasterConnection |          1 |         10 |         10 |         10 |         10 |     0.0546 |
      initialize/m2n.requestSlavesConnection |          1 |         82 |         82 |         82 |         82 |      0.448 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          2 |          0 |          0 |          0 |     0.0109 |
                           solver.initialize |          1 |          1 |          1 |          1 |          1 |    0.00546 |


eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> c2767158b4c6
Removing intermediate container 1aa69f080d01
Step 27/29 : USER root
 ---> Running in dd2166cedc4f
 ---> 3c5121450858
Removing intermediate container dd2166cedc4f
Step 28/29 : RUN mkdir /Output
 ---> Running in 788350d71b2e
 ---> 7245d83f2595
Removing intermediate container 788350d71b2e
Step 29/29 : USER [secure]
 ---> Running in a149c1b4a978
 ---> 0950254f08cc
Removing intermediate container a149c1b4a978
Successfully built 0950254f08cc
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
2421e017a68aa6e460c9e6bd1c47149fba3481fa9b5cada4a398661b25a7198e
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:2b2db29d:start=1579347389014887450,finish=1579347497188919145,duration=108174031695,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:06d8ecee[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:06d8ecee:start=1579347501298253256,finish=1579347502721947733,duration=1423694477,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0fe8e44e[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/638788555/log.txt)