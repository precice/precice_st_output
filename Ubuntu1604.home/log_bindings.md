## Status: Passing 
Build: [1520](https://travis-ci.org/precice/systemtests/builds/641980444) 

Job: [1520.22](https://travis-ci.org/precice/systemtests/jobs/641980466) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |  Run finished at Sun Jan 26 11:58:53 2020
Global runtime       = 184ms / 0.184s
Number of processors = 1
# Rank: 0

        0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |        184 |        184 |        184 |        184 |          1 |
                                     advance |         30 |         91 |         40 |          1 |          3 |      0.495 |
                     advance/m2n.receiveData |         30 |          5 |          0 |          0 |          0 |     0.0272 |
                        advance/m2n.sendData |         30 |          7 |          4 |          0 |          0 |      0.038 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |          1 |          1 |          1 |          1 |    0.00543 |
                                  initialize |          1 |         87 |         87 |         87 |         87 |      0.473 |
 initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0109 |
   initialize/m2n.exchangeVertexDistribution |          1 |         82 |         82 |         82 |         82 |      0.446 |
      initialize/m2n.requestMasterConnection |          1 |          1 |          1 |          1 |          1 |    0.00543 |
      initialize/m2n.requestSlavesConnection |          1 |         85 |         85 |         85 |         85 |      0.462 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          2 |          2 |          2 |          2 |     0.0109 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        198 |          0 |        198 |          0 |          1 |
                                                                      advance |         38 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         38 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          7 |          0 |          7 |          0 |          1 |
                                                                   initialize |         99 |          0 |         99 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |         10 |          0 |         10 |          0 |          1 |
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
                               initialize/partition.receiveGlobalMesh.MeshOne |         42 |          0 |         42 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> aba37bbc917a
Removing intermediate container eeaa4a419d6c
Step 27/29 : USER root
 ---> Running in 8f2f510b5c3a
 ---> ed8efd7be9fc
Removing intermediate container 8f2f510b5c3a
Step 28/29 : RUN mkdir /Output
 ---> Running in 43037598a2fe
 ---> f203c1b179ed
Removing intermediate container 43037598a2fe
Step 29/29 : USER [secure]
 ---> Running in ad13a78b6c04
 ---> 68f4af693c74
Removing intermediate container ad13a78b6c04
Successfully built 68f4af693c74
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
b16bcdfbedaa0d7c9f57a959e67227b0f1a769386f05c889a6ca67ecc538e001
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:151ff684:start=1580039819637549133,finish=1580039934777797196,duration=115140248063,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01a9db34[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01a9db34:start=1580039939106225124,finish=1580039940465807072,duration=1359581948,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:01d478c3[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/641980466/log.txt)