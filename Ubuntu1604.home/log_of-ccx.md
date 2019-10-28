## Status: Passing 
Build: [1036](https://travis-ci.org/precice/systemtests/builds/603688824) 

Job: [1036.19](https://travis-ci.org/precice/systemtests/jobs/603688852) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                      2% |                                |  766k  0:01:04 ETA
[0m[91m-                      4% |*                               | 1265k  0:00:57 ETA
[0m[91m-                      7% |**                              | 1833k  0:00:51 ETA
[0m[91m-                      9% |***                             | 2411k  0:00:48 ETA
[0m[91m-                     11% |***                             | 2968k  0:00:45 ETA
[0m[91m-                     13% |****                            | 3481k  0:00:44 ETA
[0m[91m-                     15% |*****                           | 4045k  0:00:42 ETA
[0m[91m-                     17% |*****                           | 4600k  0:00:41 ETA
[0m[91m-                     20% |******                          | 5169k  0:00:39 ETA
[0m[91m-                     22% |*******                         | 5677k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6249k  0:00:37 ETA
[0m[91m-                     26% [0m[91m|********                        | 6811k  0:00:35 ETA
[0m[91m-                     28% |*********                       | 7309k  0:00:35 ETA
[0m[91m-                    [0m[91m 30% [0m[91m|*********                       | 7885k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8449k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 9014k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9512k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:28 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 12.0M[0m[91m  0:00:24 ETA
[0m[91m-                     50% [0m[91m|****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:22 ETA
[0m[91m-                     54% [0m[91m|*****************               | 13.5M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA[0m[91m
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% [0m[91m|******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                     99% |******************************* | 25.0M  0:00:00 ETA
-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> e16425980b1d
Removing intermediate container 8932afd49f64
Step 10/13 : WORKDIR /
 ---> bd63ca74f6d5
Removing intermediate container e5570621b9b2
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in ce799d82232f
 ---> d309dccd65ec
Removing intermediate container ce799d82232f
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ac2fb5adde42
 ---> 67475677d105
Removing intermediate container ac2fb5adde42
Step 13/13 : USER [secure]
 ---> Running in 4ffab5f21872
 ---> 1a9129002d42
Removing intermediate container 4ffab5f21872
Successfully built 1a9129002d42
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:107316668f285cf4c40b471c4616ea1a6e56b3f2b88abd4e706e18828b74fafb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:12014ffefeb11b95c696c067518a51d5052d2c7726ba8681e6818f5bad1adef3
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/603688852/log.txt)