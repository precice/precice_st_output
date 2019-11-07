## Status: Passing 
Build: [1059](https://travis-ci.org/precice/systemtests/builds/608519809) 

Job: [1059.19](https://travis-ci.org/precice/systemtests/jobs/608519828) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     49% |***************                 | 12.3M  0:00:40 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:40 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:39 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:40 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:40 ETA
[0m[91m-                     51% |****************                | 13.0M  0:00:40 ETA
[0m[91m-                     53% |****************                | 13.2M  0:00:39 ETA
[0m[91m-                     53% [0m[91m|*****************               | 13.3M  0:00:40 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:39 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:38 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:37 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:34 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:32 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:31 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:30 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:31 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:31 ETA
[0m[91m-                     64% [0m[91m|********************            | 16.1M  0:00:30 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:29 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:28 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:28 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:27 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:25 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:23 ETA
[0m[91m-                    [0m[91m 74% [0m[91m|***********************         | 18.6M  0:00:21 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:19 ETA
[0m[91m-                     78% |************************        | 19.5M  0:00:18 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:18 ETA
[0m[91m-                     79% |*************************       | 19.7M  0:00:17 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:16 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:16 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:16 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:16 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:16 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:15 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:14 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:14 ETA
[0m[91m-                     84% |**************************      | 21.1M  0:00:14 ETA
[0m[91m-                     85% [0m[91m|***************************     | 21.3M  0:00:13 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:12 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:11 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:10 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:09 ETA
[0m[91m-                    [0m[91m 91% |*****************************   | 22.8M  0:00:07 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:07 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:06 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:04 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA
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
 ---> 47833107b54b
Removing intermediate container e4141b4ac844
Step 10/13 : WORKDIR /
 ---> 2dc35c3681a3
Removing intermediate container d100d96fffa7
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 017395052f17
 ---> 2bc988d87347
Removing intermediate container 017395052f17
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1e043d236fce
 ---> 55f4a24812c5
Removing intermediate container 1e043d236fce
Step 13/13 : USER [secure]
 ---> Running in 6f65d67b4daa
 ---> a7ca6863fd32
Removing intermediate container 6f65d67b4daa
Successfully built a7ca6863fd32
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d472ecf92550f3e4c0d9a2fa3aebe24121d0c77410191a820853bd326e430cf0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0b0c9e4109a8c4a5d8f19810698cace2d96f98fffde339b2dbf801e77c3c3add
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/608519828/log.txt)