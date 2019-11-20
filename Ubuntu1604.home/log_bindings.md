## Status: Passing 
Build: [1124](https://travis-ci.org/precice/systemtests/builds/614316725) 

Job: [1124.21](https://travis-ci.org/precice/systemtests/jobs/614316754) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          2 |          2 |          0 |          0 |    0.00154 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000771 |


Run finished at Wed Nov 20 02:55:16 2019
Global runtime       = 1307ms / 1.307s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1307 |       1307 |       1307 |       1307 |          1 |
                                     advance |         30 |       1245 |         75 |         39 |         41 |      0.953 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         42 |         42 |         42 |         42 |     0.0321 |
                                  initialize |          1 |         14 |         14 |         14 |         14 |     0.0107 |
      initialize/m2n.requestMasterConnection |          1 |         11 |         11 |         11 |         11 |    0.00842 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000765 |
                           solver.initialize |          1 |          3 |          3 |          3 |          3 |     0.0023 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1297 |          0 |       1297 |          0 |          1 |
                                                                      advance |         44 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         45 |          0 |         45 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          8 |          0 |          8 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         35 |          0 |         35 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          2 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1307 |          0 |       1307 |          0 |          1 |
                                     advance |         75 |          0 |         39 |          0 |       0.52 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         42 |          0 |         42 |          0 |          1 |
                                  initialize |         14 |          0 |         14 |          0 |          1 |
      initialize/m2n.requestMasterConnection |         11 |          0 |         11 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          3 |          0 |          3 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 10e7a8cef73c
Removing intermediate container cddbec91d971
Step 29/29 : RUN mkdir /Output
 ---> Running in bf78c31225da
 ---> 73f06260af60
Removing intermediate container bf78c31225da
Successfully built 73f06260af60
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
ae6c39eaa6bb22f17979276816684d11f639c670a0d3e6965d5308b467eb16eb
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:05ddb368:start=1574218367498324828,finish=1574218518076788585,duration=150578463757,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:24faa3fe[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:24faa3fe:start=1574218523387453324,finish=1574218525208967197,duration=1821513873,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:06728634[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/614316754/log.txt)