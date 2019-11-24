## Status: Passing 
Build: [1132](https://travis-ci.org/precice/systemtests/builds/616148321) 

Job: [1132.21](https://travis-ci.org/precice/systemtests/jobs/616148344) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```

                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1332 |       1332 |       1332 |       1332 |          1 |
                                                                      advance |         30 |       1162 |         43 |          0 |         38 |      0.872 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |     0.0593 |
                                                                   initialize |          1 |         87 |         87 |         87 |         87 |     0.0653 |
                                        initialize/m2n.acceptMasterConnection |          1 |         47 |         47 |         47 |         47 |     0.0353 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         38 |         38 |         38 |         38 |     0.0285 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000751 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1287 |          0 |       1287 |          0 |          1 |
                                     advance |         82 |          0 |         39 |          0 |    0.47561 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         39 |          0 |         39 |          0 |          1 |
                                  initialize |          3 |          0 |          3 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          2 |          0 |          2 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1332 |          0 |       1332 |          0 |          1 |
                                                                      advance |         43 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         87 |          0 |         87 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |         47 |          0 |         47 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         38 |          0 |         38 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> e4ba800a9ade
Removing intermediate container af85ac0d9252
Step 29/29 : RUN mkdir /Output
 ---> Running in a8c17b093fcb
 ---> 0a9e02857b0f
Removing intermediate container a8c17b093fcb
Successfully built 0a9e02857b0f
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
10fa59f8d935fa92b3ce0ee978e5c5bb65514284e3e95a443a9ee57bb9319ec8
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:28aac130:start=1574563945672291885,finish=1574564095104340419,duration=149432048534,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0d4df79b[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0d4df79b:start=1574564100300206523,finish=1574564102048021726,duration=1747815203,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:14e0f9c6[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/616148344/log.txt)