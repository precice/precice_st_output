## Status: Passing 
Build: [1467](https://travis-ci.org/precice/systemtests/builds/638371833) 

Job: [1467.22](https://travis-ci.org/precice/systemtests/jobs/638371857) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |        151 |        151 |        151 |        151 |          1 |
                                                                      advance |         30 |         45 |         38 |          0 |          1 |      0.298 |
                                                      advance/m2n.receiveData |         29 |         41 |         38 |          0 |          1 |      0.272 |
                                                         advance/m2n.sendData |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         15 |         15 |         15 |         15 |     0.0993 |
                                                                   initialize |          1 |         88 |         88 |         88 |         88 |      0.583 |
                                        initialize/m2n.acceptMasterConnection |          1 |          8 |          8 |          8 |          8 |      0.053 |
                                        initialize/m2n.acceptSlavesConnection |          1 |         42 |         42 |         42 |         42 |      0.278 |
                                  initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0132 |
                                    initialize/m2n.exchangeVertexDistribution |          1 |         39 |         39 |         39 |         39 |      0.258 |
                                                   initialize/m2n.receiveData |          1 |          2 |          2 |          2 |          2 |     0.0132 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         34 |         34 |         34 |         34 |      0.225 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |        151 |          0 |        151 |          0 |          1 |
                                                                      advance |         38 |          0 |          0 |          0 |          0 |
                                                      advance/m2n.receiveData |         38 |          0 |          0 |          0 |          0 |
                                                         advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         15 |          0 |         15 |          0 |          1 |
                                                                   initialize |         88 |          0 |         88 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          8 |          0 |          8 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |         42 |          0 |         42 |          0 |          1 |
                                  initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
                                         initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
                                          initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
                                    initialize/m2n.exchangeVertexDistribution |         39 |          0 |         39 |          0 |          1 |
                                                   initialize/m2n.receiveData |          2 |          0 |          2 |          0 |          1 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         34 |          0 |         34 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
 ---> 2deac725b18c
Removing intermediate container 4a4ccee17aba
Step 27/29 : USER root
 ---> Running in 05e22c4e20e8
 ---> e809277fe06b
Removing intermediate container 05e22c4e20e8
Step 28/29 : RUN mkdir /Output
 ---> Running in 9234d5508166
 ---> 27096ebc872b
Removing intermediate container 9234d5508166
Step 29/29 : USER [secure]
 ---> Running in bd58dc5a81d6
 ---> 56e9a90929ec
Removing intermediate container bd58dc5a81d6
Successfully built 56e9a90929ec
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
3134c8581d4e82f3799b11319f6eacdd6438be000b60b9675d32d53eb25ef374
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:07464c72:start=1579260973842938244,finish=1579261083997612375,duration=110154674131,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:22646208[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/638371857/log.txt)