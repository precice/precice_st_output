## Status: Passing 
Build: [1415](https://travis-ci.org/precice/systemtests/builds/634678414) 

Job: [1415.22](https://travis-ci.org/precice/systemtests/jobs/634678438) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
                                                   initialize/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         39 |          0 |         39 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializRun finished at Thu Jan  9 12:10:10 2020
Global runtime       = 206ms / 0.206s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |        206 |        206 |        206 |        206 |          1 |
                                     advance |         30 |         79 |         37 |          0 |          2 |      0.383 |
                     advance/m2n.receiveData |         30 |          3 |          0 |          0 |          0 |     0.0146 |
                        advance/m2n.sendData |         30 |          1 |          0 |          0 |          0 |    0.00485 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |          8 |          8 |          8 |          8 |     0.0388 |
                                  initialize |          1 |        110 |        110 |        110 |        110 |      0.534 |
 initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |    0.00971 |
   initialize/m2n.exchangeVertexDistribution |          1 |         83 |         83 |         83 |         83 |      0.403 |
      initialize/m2n.requestMasterConnection |          1 |         22 |         22 |         22 |         22 |      0.107 |
      initialize/m2n.requestSlavesConnection |          1 |         86 |         86 |         86 |         86 |      0.417 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          3 |          0 |          0 |          0 |     0.0146 |
                           solver.initialize |          1 |          2 |          2 |          2 |          2 |    0.00971 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        206 |          0 |        206 |          0 |          1 |
                                     advance |         37 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          8 |          0 |          8 |          0 |          1 |
                                  initialize |        110 |          0 |        110 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         83 |          0 |         83 |          0 |          1 |
      initialize/m2n.requestMasterConnection |         22 |          0 |         22 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         86 |          0 |         86 |          0 |          1 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          2 |          0 |          2 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> e58c49a53af2
Removing intermediate container bd09a686c75c
Step 27/29 : USER root
 ---> Running in a8cb46055508
 ---> 1a375255d900
Removing intermediate container a8cb46055508
Step 28/29 : RUN mkdir /Output
 ---> Running in 8940a445f820
 ---> 362d8fb72586
Removing intermediate container 8940a445f820
Step 29/29 : USER [secure]
 ---> Running in cd69b7635155
 ---> 4617418a448c
Removing intermediate container cd69b7635155
Successfully built 4617418a448c
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
da3be76b85ffdfa99c8d62e437aa6a1aa9a9aea46ca776234255e51b55a06135
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:10988d74:start=1578571699931434173,finish=1578571811513411556,duration=111581977383,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:27cc6fdd[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:27cc6fdd:start=1578571815660089979,finish=1578571817034707369,duration=1374617390,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0b170f5c[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

```
[
Full job log](https://api.travis-ci.org/v3/job/634678438/log.txt)