## Status: Failure 
Build: [1362](https://travis-ci.org/precice/systemtests/builds/629344851) 

Job: [1362.19](https://travis-ci.org/precice/systemtests/jobs/629344874) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
polyMesh.org/
Downloading and extracting the Outer-Fluid mesh...
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      0% |                                |  115k  0:03:41 ETA
[0m[91m-                      2% |                                |  680k  0:01:13 ETA
[0m[91m-                      4% |*                               | 1266k  0:00:57 ETA
[0m[91m-                      7% |**                              | 1876k  0:00:50 ETA
[0m[91m-                      9% |***                             | 2462k  0:00:47 ETA
[0m[91m-                     11% |***                             | 3026k  0:00:44 ETA
[0m[91m-                     14% |****                            | 3649k  0:00:42 ETA
[0m[91m-                     16% |*****                           | 4235k  0:00:40 ETA
[0m[91m-                     18% |******                          | 4840k  0:00:38 ETA
[0m[91m-                     21% |******                          | 5429k  0:00:37 ETA
[0m[91m-                     23% |*******                         | 5999k  0:00:35 ETA
[0m[91m-                     25% |********                        | 6607k  0:00:34 ETA
[0m[91m-                     28% |********                        | 7202k  0:00:33 ETA
[0m[91m-                     30% |*********                       | 7767k  0:00:32 ETA
[0m[91m-                     32% |**********                      | 8398k  0:00:30 ETA
[0m[91m-                     34% |***********                     | 8970k  0:00:29 ETA
[0m[91m-                     37% |***********                     | 9579k  0:00:28 ETA
[0m[91m-                     38% |************                    | 9765k  0:00:29 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:26 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:24 ETA
[0m[91m-                     50% |****************                | [0m[91m12.7M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:20 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:18 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:15 ETA[0m[91m
[0m[91m-                     69% |**********************          | 17.3M[0m[91m  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     76% |************************        | [0m[91m19.0M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:09 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA
written to stdout
[0mpolyMesh.org/neighbour.gz
polyMesh.org/points.gz
polyMesh.org/cellZones.gz
polyMesh.org/owner.gz
polyMesh.org/pointZones.gz
polyMesh.org/faceZones.gz
polyMesh.org/faces.gz
polyMesh.org/blockMeshDict
polyMesh.org/
Completed.
 ---> 9b82c56a3b6d
Removing intermediate container d13017709835
Step 11/14 : WORKDIR /
 ---> 1bea5061c607
Removing intermediate container 793398bb057c
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in b549d6fb3967
 ---> 9f71181276f6
Removing intermediate container b549d6fb3967
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 04b09e313890
 ---> 12cacde90ac0
Removing intermediate container 04b09e313890
Step 14/14 : USER [secure]
 ---> Running in 6522a74cee2d
 ---> a55fd0d19e58
Removing intermediate container 6522a74cee2d
Successfully built a55fd0d19e58
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:16b94ae5c4de8bd2512ad80b95088637775c1122d6d63de4bfa00f1defdf566a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:eb586f79928eeaf8d8769a6c1179df8f42588ebbc5715d4aff4fe67dfce0618b
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/629344874/log.txt)