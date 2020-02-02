## Status: Passing 
Build: [1580](https://travis-ci.org/precice/systemtests/builds/645031917) 

Job: [1580.21](https://travis-ci.org/precice/systemtests/jobs/645031938) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
                                     initialize/partition.prepareMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         39 |          0 |         39 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                           initializRun finished at Sun Feb  2 15:40:13 2020
Global runtime       = 172ms / 0.172s
Number of processors = 1
# Rank: 0

                                       Event |      Count |  Total[ms] |    Max[ms] |    Min[ms] |    Avg[ms] | Time Ratio |
----------------------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |          1 |        172 |        172 |        172 |        172 |          1 |
                                     advance |         30 |         52 |         41 |          0 |          1 |      0.302 |
                     advance/m2n.receiveData |         30 |          1 |          0 |          0 |          0 |    0.00581 |
                        advance/m2n.sendData |         30 |          0 |          0 |          0 |          0 |          0 |
                                   configure |          1 |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          1 |          4 |          4 |          4 |          4 |     0.0233 |
                                  initialize |          1 |        114 |        114 |        114 |        114 |      0.663 |
 initialize/m2n.broadcastVertexDistributions |          1 |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          1 |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          1 |          2 |          2 |          2 |          2 |     0.0116 |
   initialize/m2n.exchangeVertexDistribution |          1 |         79 |         79 |         79 |         79 |      0.459 |
      initialize/m2n.requestMasterConnection |          1 |         32 |         32 |         32 |         32 |      0.186 |
      initialize/m2n.requestSlavesConnection |          1 |         81 |         81 |         81 |         81 |      0.471 |
     initialize/partition.gatherMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
    initialize/partition.prepareMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                        Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
---------------------------------------------------------------------------------------------------------------
                                     _GLOBAL |        172 |          0 |        172 |          0 |          1 |
                                     advance |         41 |          0 |          0 |          0 |          0 |
                     advance/m2n.receiveData |          0 |          0 |          0 |          0 |          0 |
                        advance/m2n.sendData |          0 |          0 |          0 |          0 |          0 |
                                   configure |          0 |          0 |          0 |          0 |          0 |
                                    finalize |          4 |          0 |          4 |          0 |          1 |
                                  initialize |        114 |          0 |        114 |          0 |          1 |
 initialize/m2n.broadcastVertexDistributions |          0 |          0 |          0 |          0 |          0 |
        initialize/m2n.buildCommunicationMap |          0 |          0 |          0 |          0 |          0 |
         initialize/m2n.createCommunications |          2 |          0 |          2 |          0 |          1 |
   initialize/m2n.exchangeVertexDistribution |         79 |          0 |         79 |          0 |          1 |
      initialize/m2n.requestMasterConnection |         32 |          0 |         32 |          0 |          1 |
      initialize/m2n.requestSlavesConnection |         81 |          0 |         81 |          0 |          1 |
     initialize/partition.gatherMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
    initialize/partition.prepareMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
 initialize/partition.sendGlobalMesh.MeshOne |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |          0 |          0 |          0 |          0 |          0 |
                           solver.initialize |          0 |          0 |          0 |          0 |          0 |
 DUMMY: Closing Fortran solver dummy...
eData/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |          0 |          0 |          0 |          0 |          0 |
                                                            solver.initialize |          4 |          0 |          4 |          0 |          1 |
 DUMMY: Closing Fortran solver dummy...
 ---> f2508a0b80f8
Removing intermediate container c11454bb6a33
Step 34/36 : USER root
 ---> Running in 555689120ed3
 ---> 94ced7ff6392
Removing intermediate container 555689120ed3
Step 35/36 : RUN mkdir /Output
 ---> Running in 475460e81f4d
 ---> 060a215de7fc
Removing intermediate container 475460e81f4d
Step 36/36 : USER [secure]
 ---> Running in fe6583693530
 ---> 7575c2070db1
Removing intermediate container fe6583693530
Successfully built 7575c2070db1
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
90a56c6d8d98f2ea0f010babe2ed5a3db02ffe69c9fbcc52c6b16333b8d910ee
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:262437cc:start=1580657904307503897,finish=1580658014615010554,duration=110307506657,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:048132a0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:048132a0:start=1580658018845140651,finish=1580658020174000665,duration=1328860014,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:3698aa80[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/645031938/log.txt)