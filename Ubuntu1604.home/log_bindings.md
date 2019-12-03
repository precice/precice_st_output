## Status: Passing 
Build: [1250](https://travis-ci.org/precice/systemtests/builds/620248621) 

Job: [1250.17](https://travis-ci.org/precice/systemtests/jobs/620248638) 

Triggered by: [push](https://github.com/precice/systemtests/compare/25da98cf068b...23fe0b4a3d6a) 

---
Last 100 lines of the job log at the moment of push:
```
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1296 |       1296 |       1296 |       1296 |          1 |
                                     advance |         30 |       1233 |         75 |         39 |         41 |      0.951 |
                                   configure |          1 |          1 |          1 |          1 |          1 |   0.000772 |
                                    finalize |          1 |         43 |         43 |         43 |         43 |     0.0332 |
                                  initialize |          1 |         16 |         16 |         16 |         16 |     0.0123 |
      initialize/m2n.requestMasterConnection |          1 |         11 |         11 |         11 |         11 |    0.00849 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          1 |          1 |          1 |          1 |   0.000772 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000772 |
                           solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000772 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1296 |          0 |       1296 |          0 |          1 |
                                     advance |         75 |          0 |         39 |          0 |       0.52 |
                                   configure |          1 |          0 |          1 |          0 |          1 |
                                    finalize |         43 |          0 |         43 |          0 |          1 |
                                  initialize |         16 |          0 |         16 |          0 |          1 |
      initialize/m2n.requestMasterConnection |         11 |          0 |         11 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          1 |          0 |          1 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1285 |          0 |       1285 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         45 |          0 |         45 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          3 |          0 |          3 |          0 |          1 |
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
                                                            solver.initialize |          2 |          0 |          2 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 30bbe5f71a5e
Removing intermediate container 92f649e551cb
Step 28/30 : USER root
 ---> Running in f2bc978c7147
 ---> b2ace27e4f8c
Removing intermediate container f2bc978c7147
Step 29/30 : RUN mkdir /Output
 ---> Running in de38ca67c1cf
 ---> dd2c54cdee3f
Removing intermediate container de38ca67c1cf
Step 30/30 : USER [secure]
 ---> Running in d7141dc94ec6
 ---> 0fff1e493345
Removing intermediate container d7141dc94ec6
Successfully built 0fff1e493345
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
1dfe57b4ba62c8e3d538f1a13590e884206160d2e111bcb20038ecd88a1ada49
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:0b4adc18:start=1575404614886639421,finish=1575404752897243572,duration=138010604151,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:23acd320[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:23acd320:start=1575404758290395022,finish=1575404760079553529,duration=1789158507,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:003ed090[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620248638/log.txt)