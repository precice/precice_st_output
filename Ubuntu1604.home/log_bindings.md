 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583929538) 
## Triggered by: [cron](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4) 
## Last 100 lines of the job log at the moment of push...
```
 Global runtime       = 1286ms / 1.286s
Number of processors = 1
# Rank: 0

Run finished at Thu Sep 12 02:16:34 2019
Global runtime       = 1281ms / 1.281s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1281 |       1281 |       1281 |       1281 |          1 |
                                     advance |         30 |       1233 |         75 |         39 |         41 |      0.963 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         40 |         40 |         40 |         40 |     0.0312 |
                                  initialize |          1 |          3 |          3 |          3 |          3 |    0.00234 |
      initialize/m2n.requestMasterConnection |          1 |          2 |          2 |          2 |          2 |    0.00156 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          2 |          0 |          0 |          0 |    0.00156 |
                           solver.initialize |          1 |          2 |          2 |          2 |          2 |    0.00156 |


                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
--------------------------------------------------------         0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         37 |         37 |         37 |         37 |     0.0288 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000778 |
                                                            solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000778 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |       1281 |          0 |       1281 |          0 |          1 |
                                     advance |         75 |          0 |         39 |          0 |       0.52 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |         40 |          0 |         40 |          0 |          1 |
                                  initialize |          3 |          0 |          3 |          0 |          1 |
      initialize/m2n.requestMasterConnection |          2 |          0 |          2 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          2 |          0 |          2 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1286 |          0 |       1286 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         46 |          0 |         46 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          7 |          0 |          7 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         37 |          0 |         37 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          0 |          1 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 6275c84b3832
Removing intermediate container af5c0906286b
Step 29/29 : RUN mkdir /Output
 ---> Running in c8ae65d0a51d
 ---> ae0cb7286d75
Removing intermediate container c8ae65d0a51d
Successfully built ae0cb7286d75
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
866920edfee1aeb8bbccb000e445b415d7d0d2e3c60c882ed5e4a3fd6a5f6f54
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:0dcf1068:start=1568254449561786021,finish=1568254595249409884,duration=145687623863,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0adef620[0K$ python push.py -s -t bindings
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583929559/log.txt)