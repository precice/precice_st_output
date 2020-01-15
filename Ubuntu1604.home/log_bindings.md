## Status: Passing 
Build: [1457](https://travis-ci.org/precice/systemtests/builds/637357729) 

Job: [1457.22](https://travis-ci.org/precice/systemtests/jobs/637357753) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          5 |          0 |          5 |          0 |          1 |
Number of processors = 1
# Rank: 0

                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |        185 |        185 |        185 |        185 |          1 |
                                                                      advance |         30 |         55 |         37 |          0 |          1 |      0.297 |
                                                      advance/m2n.receiveData |         29 |         42 |         37 |          0 |          1 |      0.227 |
                                                         advance/m2n.sendData |         30 |          1 |          0 |          0 |          0 |    0.00541 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         12 |         12 |         12 |         12 |     0.0649 |
                                                                   initialize |          1 |        114 |        114 |        114 |        114 |      0.616 |
                                        initialize/m2n.acceptMasterConnection |          1 |         29 |         29 |         29 |         29 |      0.157 |
                                        initialize/m2n.acceptSlavesConnection |          1 |         42 |         42 |         42 |         42 |      0.227 |
                                  initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0108 |
                                    initialize/m2n.exchangeVertexDistribution |          1 |         40 |         40 |         40 |         40 |      0.216 |
                                                   initialize/m2n.receiveData |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         36 |         36 |         36 |         36 |      0.195 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          1 |          0 |          0 |          0 |    0.00541 |
                                                            solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


 DUMMY: Closing Fortran solver dummy...
                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        185 |          0 |        185 |          0 |          1 |
                                                                      advance |         37 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         37 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         12 |          0 |         12 |          0 |          1 |
                                                                   initialize |        114 |          0 |        114 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |         29 |          0 |         29 |          0 |          1 |
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
                               initialize/partition.receiveGlobalMesh.MeshOne |         36 |          0 |         36 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> 12b49acf5d29
Removing intermediate container 9c08c018842e
Step 27/29 : USER root
 ---> Running in 9650c45aa51c
 ---> d6cc67d2fac2
Removing intermediate container 9650c45aa51c
Step 28/29 : RUN mkdir /Output
 ---> Running in f3dd4757da5e
 ---> 781095e09f1e
Removing intermediate container f3dd4757da5e
Step 29/29 : USER [secure]
 ---> Running in de385bb317df
 ---> 9d04a425a0ee
Removing intermediate container de385bb317df
Successfully built 9d04a425a0ee
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
93bedf9d28e3e2e9f26ba8a650eda84335df1900a5caf766dd6002c43c3ffa37
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:02b8236d:start=1579090052421164549,finish=1579090157441532875,duration=105020368326,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:3182ea70[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:3182ea70:start=1579090161378171154,finish=1579090162725448655,duration=1347277501,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:017533ef[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/637357753/log.txt)