## Status: Passing 
Build: [1059](https://travis-ci.org/precice/systemtests/builds/608519809) 

Job: [1059.21](https://travis-ci.org/precice/systemtests/jobs/608519830) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |          1 |  
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |          1 |         39 |         39 |         39 |         39 |     0.0304 |
                                                               initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexOnVertices |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.nn.mapData.FromMeshTwoToMeshOne |          1 |          0 |          0 |          0 |          0 |          0 |
                           initializeData/map.np.mapData.FromMeshOneToMeshTwo |          1 |          0 |          0 |          0 |          0 |          0 |
                                                               solver.advance |         30 |          0 |          0 |          0 |          0 |          0 |
                                                            s |          1 |          0 |          0 |          0 |          0 |          0 |
                              initializeData |          1 |          0 |          0 |          0 |          0 |          0 |
                              solver.advance |         30 |          1 |          0 |          0 |          0 |   0.000772 |
                           solver.initialize |          1 |          0 |          0 |          0 |          0 |          0 |


                                                                         Name |        Max |  MaxOnRank |        Min |  MinOnRank |    Min/Max |
------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      _GLOBAL |       1285 |          0 |       1285 |          0 |          1 |
                                                                      advance |         40 |          0 |          0 |          0 |          0 |
                                  advance/map.nn.mapData.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
                                  advance/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                                                    configure |          1 |          0 |          1 |          0 |          1 |
                                                                     finalize |         79 |          0 |         79 |          0 |          1 |
                                                                   initialize |         44 |          0 |         44 |          0 |          1 |
                                        initialize/m2n.acceptMasterConnection |          3 |          0 |          3 |          0 |          1 |
                                        initialize/m2n.acceptSlavesConnection |          0 |          0 |          0 |          0 |          0 |
                        initialize/map.np.computeMapping.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
        initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnEdges |          0 |          0 |          0 |          0 |          0 |
     initialize/map.np.computeMapping.FromMeshOneToMeshTwo.getIndexOnVertices |          0 |          0 |          0 |          0 |          0 |
                               initialize/map.np.mapData.FromMeshOneToMeshTwo |          0 |          0 |          0 |          0 |          0 |
                                    initialize/partition.feedbackMesh.MeshTwo |          0 |          0 |          0 |          0 |          0 |
                               initialize/partition.receiveGlobalMesh.MeshOne |         39 |          0 |         39 |          0 |          1 |
                                                               initializeData |          0 |          0 |          0 |          0 |          0 |
                    initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne |          0 |          0 |          0 |          0 |          0 |
 initializeData/map.nn.computeMapping.FromMeshTwoToMeshOne.getIndexO/lib/docker/overlay2/l/I43XRAWJD2TC6QRBFXJI6H5WTJ,upperdir=/var/lib/docker/overlay2/69'
[0m[91mUnexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/2EJ2FTX3VQZOFYNYJYWUOAZOX7:/var/lib/docker/overlay2/l/QRWZFPGTJDCWXG3BR4SA4COHNL:/var/lib/docker/overlay2/l/KGB53UNUQGSZMMACNEG2B66MU6:/var/lib/docker/overlay2/l/44TOOTQGXY6DCLBGWQUXOEUCGO:/var/lib/docker/overlay2/l/X6HTLWB32OHH7UWVMNPXIFREIO:/var/lib/docker/overlay2/l/K2HUXUA7L7MI2FZ6YB6QS74NH2:/var/lib/docker/overlay2/l/DS6DY64SVCO5FTBYB3CLL6ITX6:/var/lib/docker/overlay2/l/7YLXSU6U7MXAEILA3YZ2Q76XSO:/var/lib/docker/overlay2/l/MAM5JTW5MLKNE'
Unexpected end of /proc/mounts line `KBQ5BQ56RMXRQ:/var/lib/docker/overlay2/l/NSMSFTLQKL3DOT4EBNDVUZHOF2:/var/lib/docker/overlay2/l/YXT46P2QOKXPTTQE4NHY46OEZS:/var/lib/docker/overlay2/l/IPXDQJFPDDWANZYVZ7536EN4GA:/var/lib/docker/overlay2/l/34SATLR5NJSXZAU6PKAO5VVIMW:/var/lib/docker/overlay2/l/ECWLD5T6G4M6Z4BZNSWN7KDWS3:/var/lib/docker/overlay2/l/IXO36PJLLKXSYFRH4KNISNSV7K:/var/lib/docker/overlay2/l/DHQERSH6VURCOTH53YTPQFOCIQ:/var/lib/docker/overlay2/l/3JKTSNS4NX24LQCC32BJTCYNF2:/var/lib/docker/overlay2/l/NFJLWNLAZ46UZVZF57XLHPRBJ3:/var/lib/do'
Unexpected end of /proc/mounts line `cker/overlay2/l/35Y2IJTOSYMSW4R2R3NL5GKLNC:/var/lib/docker/overlay2/l/FEIA3DFVLCNDLBPADWYGCE3DT7:/var/lib/docker/overlay2/l/SALZEJ4W7LG2I4Y2NLNVF4GRGI:/var/lib/docker/overlay2/l/NJXOPKSPYWGCUF6EQ2QGYI3ELF:/var/lib/docker/overlay2/l/LTND2BSQXD3EEG2VTLAAB2SSLH:/var/lib/docker/overlay2/l/ARF427KI7QRIVJH3LMNTHCG3KH:/var/lib/docker/overlay2/l/IIEBHVYOKOLR3O44VUTXAQR6IH:/var/lib/docker/overlay2/l/XST3BS2LBJ4IUHKAZQFQ5MpreCICE:[0m it 2 of 3 | dt# 3 of 10 | t 2 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 3 of 10 | t 2 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 3 of 10 | t 2 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 3 of 10 | t 2 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 4 of 10 | t 3 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m it 1 of 3 | dt# 4 of 10 | t 3 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 4 of 10 | t 3 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 4 of 10 | t 3 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCIad-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m it 1 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpoint | 
 DUMMY: Advancing in time
 DUMMY: Writing iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 1 of 5, conv = false
preCICE:[0m it 2 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 2 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 2 of 5, conv = false
preCICE:[0m it 3 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m it 3 of 3 | dt# 6 of 10 | t 5 | dt 1 | max dt 1 | ongoing yes | dt complete no | read-iteration-checkpoint | 
 DUMMY: Reading iteration checkpoint
preCICE:[0m min iteration convergence measure: #it = 3 of 5, conv = false
preCICE:[0m Timestep completed
preCICE:[0m Timestep completed
preCICE:[0m it 1 of 3 | dt# 7 of 10 | t 6 | dt 1 | max dt 1 | ongoing yes | dt complete yes | write-iteration-checkpointeM ---> dc325e6c8001
Removing intermediate container 7d1270aec4f8
Successfully built dc325e6c8001
Successfully tagged st_bindings-ubuntu1604.home-develop:latest
5f5719beec6221c9164fac67b7e8fd77ced10314c8fdf9ed5c4b4d2f184785b4
EXECUTING: docker build --network=host --file Dockerfile --tag st_bindings-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_bindings-ubuntu1604.home-develop st_bindings-ubuntu1604.home-develop
EXECUTING: docker cp st_bindings-ubuntu1604.home-develop:Output . 
travis_time:end:021b281a:start=1573094602840920481,finish=1573094748832158379,duration=145991237898,event=script[0K[32;1mThe command "python system_testing.py -s bindings" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:07ac6cdf[0K$ python push.py -s -t bindings
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/608519830/log.txt)