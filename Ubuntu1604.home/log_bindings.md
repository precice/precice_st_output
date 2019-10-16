 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598566611) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/2f42d88d1871...b7b408e19d9a) 
## Last 100 lines of the job log at the moment of push...
```
 preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 11 of 10 | t 10 | dt 1 | max dt 1 | ongoing no | dt complete yes | 
 DUMMY: Advancing in time
Run finished at Wed Oct 16 10:27:21 2019
Global runtime       = 1295ms / 1.295s
Number of processors = 1
# Rank: 0

                                                                        Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |       1295 |       1295 |       1295 |       1295 |          1 |
                                                                      advance |         30 |       1159 |         40 |          0 |         38 |      0.895 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |         30 |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |         29 |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |          1 |         79 |         79 |         79 |         79 |      0.061 |
                                                                   initialize |          1 |         45 |         45 |         45 |         45 |     0.0347 |
                                        initialize/m2n.acceptMasterConnection |          1 |          4 |          4 |          4 |          4 |    0.00309 |
                                        initialize/m2n.acceptSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         39 |         39 |         39 |         39 |     0.0301 |
                                                               initializeData |          1 |          7 |          7 |          7 |          7 |    0.00541 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          1 |          2 |          2 |          2 |          2 |    0.00154 |


Run finished at Wed Oct 16 10:27:21 2019
Global runtime       = 1307ms / 1.307s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |       1307 |       1307 |       1307 |       1307 |          1 |
                                     advance |         30 |       1244 |         85 |         39 |         41 |      0.952 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |         42 |         42 |         42 |         42 |     0.0321 |
                                  initialize |          1 |         17 |         17 |         17 |         17 |      0.013 |
      initialize/m2n.requestMasterConnection |          1 |         16 |         16 |         16 |         16 |     0.0122 |
      initialize/m2n.requestSlavesConnection |          1 |          0 |          0 |          0 |          0 |          0 |
   initialize/partition.feedbackMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000765 |
                           solver.initialize |          1 |          1 |          1 |          1 |          1 |   0.000765 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1295 |          0 |       1295 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          0 |          0 |          0 |          0 |          0 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         45 |          0 |         45 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          4 |          0 |          4 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         39 |          0 |         39 |          0 |          1 |
                                                               initializeData |          7 |          0 |          7 |          0 |          1 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          2 |          0 |          2 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> 9d4a43e57773
Removing intermediate container 22df27ec5171
Step 29/29 : RUN mkdir /Output
 ---> Running in ce32bad9b4fc
 ---> 134ab32d5a7f
Removing intermediate container ce32bad9b4fc
Successfully built 134ab32d5a7f
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
6593d5e4114b39e756533cd46e03b65925b345938b26bcb5790dba91fdd6717b
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:1a6caea8:start=1571221493849947045,finish=1571221642555381070,duration=148705434025,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0ae34a6c[0K$ python push.py -s -t bindings
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598566628/log.txt)