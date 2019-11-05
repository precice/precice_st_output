## Status: Passing 
Build: [1057](https://travis-ci.org/precice/systemtests/builds/607431677) 

Job: [1057.19](https://travis-ci.org/precice/systemtests/jobs/607431696) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                      4% |*                               | 1204k  0:01:00 ETA
[0m[91m-                      6% |**                              | 1762k  0:00:54 ETA
[0m[91m-                      8% |**                              | 2152k  0:00:54 ETA
[0m[91m-                      8% |**                              | 2293k  0:01:01 ETA
[0m[91m-                     10% |***                             | 2644k  0:01:00 ETA
[0m[91m-                     12% |***                             | 3097k  0:00:58 ETA
[0m[91m-                     14% |****                            | 3597k  0:00:55 ETA
[0m[91m-                     16% |*****                           | 4165k  0:00:51 ETA
[0m[91m-                     18% |*****                           | 4745k  0:00:48 ETA
[0m[91m-                     20% |******                          | 5306k  0:00:45 ETA
[0m[91m-                     22% |*******                         | 5807k[0m[91m  0:00:44 ETA
[0m[91m-                    [0m[91m 24% |*******                         | 6378k  0:00:42 ETA
[0m[91m-                    [0m[91m 27% |********                        | 6949k  0:00:40 ETA
[0m[91m-                     29% |*********                       | 7519k  0:00:38 ETA
[0m[91m-                     31% |**********                      | 8011k  0:00:37 ETA
[0m[91m-                     33% |**********                      | 8589k  0:00:35 ETA
[0m[91m-                    [0m[91m 35% |***********                     | 9152k  0:00:34 ETA
[0m[91m-                     37% |************                    | 9721k  0:00:32 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:28 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M[0m[91m  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 17.0M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                    [0m[91m 85% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% [0m[91m|*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> c973d840ef91
Removing intermediate container b8927d3dbe59
Step 10/13 : WORKDIR /
 ---> f561e9f62215
Removing intermediate container 75ba528c6448
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 82e80d97af5a
 ---> 2577f7c4d9e6
Removing intermediate container 82e80d97af5a
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ab44afdbebf3
 ---> 4c9af5f27b16
Removing intermediate container ab44afdbebf3
Step 13/13 : USER [secure]
 ---> Running in d35fff3f5562
 ---> d5703725d5d8
Removing intermediate container d35fff3f5562
Successfully built d5703725d5d8
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:05fe1ccc5198ad34e3a536b114ccdb3c99481211760a11e8e6218a3edb849bae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:97215fe769d49677591d97e4c7bb4a144df24670c9667fbd182902d04772d327
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!

```
[
Full job log](https://api.travis-ci.org/v3/job/607431696/log.txt)