## Status: Passing 
Build: [1521](https://travis-ci.org/precice/systemtests/builds/642317432) 

Job: [1521.22](https://travis-ci.org/precice/systemtests/jobs/642317454) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
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
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         33 |          0 |         33 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializRun finished at Mon Jan 27 11:42:28 2020
Global runtime       = 163ms / 0.163s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |        163 |        163 |        163 |        163 |          1 |
                                     advance |         30 |         66 |         40 |          0 |          2 |      0.405 |
                     advance/m2n.receiveData |         30 |         10 |          7 |          0 |          0 |     0.0613 |
                        advance/m2n.sendData |         30 |          0 |          0 |          0 |          0 |          0 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |          9 |          9 |          9 |          9 |     0.0552 |
                                  initialize |          1 |         85 |         85 |         85 |         85 |      0.521 |
 initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0123 |
   initialize/m2n.exchangeVertexDistribution |          1 |         73 |         73 |         73 |         73 |      0.448 |
      initialize/m2n.requestMasterConnection |          1 |          5 |          5 |          5 |          5 |     0.0307 |
      initialize/m2n.requestSlavesConnection |          1 |         78 |         78 |         78 |         78 |      0.479 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        163 |          0 |        163 |          0 |          1 |
                                     advance |         40 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          7 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          9 |          0 |          9 |          0 |          1 |
                                  initialize |         85 |          0 |         85 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         73 |          0 |         73 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          5 |          0 |          5 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         78 |          0 |         78 |          0 |          1 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> 09c35b630a43
Removing intermediate container 4ca893541809
Step 27/29 : USER root
 ---> Running in 7cd5da1f6886
 ---> b56a8e1666c2
Removing intermediate container 7cd5da1f6886
Step 28/29 : RUN mkdir /Output
 ---> Running in 6d63ca08caee
 ---> fe4948f6c257
Removing intermediate container 6d63ca08caee
Step 29/29 : USER [secure]
 ---> Running in 0851b780bef9
 ---> 845ecf1975d6
Removing intermediate container 0851b780bef9
Successfully built 845ecf1975d6
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
3b5cfe41a02e152484b38f2f84d06d7e86f0bd747a4ae71934e0bd75d553c186
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:031f3800:start=1580125234958486517,finish=1580125349247559308,duration=114289072791,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:097cf994[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:097cf994:start=1580125353526012022,finish=1580125354958095154,duration=1432083132,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:038928c6[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/642317454/log.txt)