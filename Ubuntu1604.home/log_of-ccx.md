## Status: Passing 
Build: [1047](https://travis-ci.org/precice/systemtests/builds/604758622) 

Job: [1047.19](https://travis-ci.org/precice/systemtests/jobs/604758648) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     17% |*****                           | 4593k  0:00:59 ETA
[0m[91m-                    [0m[91m 19% [0m[91m|******                          | 5087k  0:00:56 ETA
[0m[91m-                     22% |*******                         | 5666k  0:00:52 ETA
[0m[91m-                     24% |*******                         | 6219k  0:00:49 ETA
[0m[91m-                     25% |********                        | 6554k  0:00:49 ETA
[0m[91m-                     26% |********                        | 6693k  0:00:50 ETA
[0m[91m-                     27% |********                        | 7040k  0:00:50 ETA
[0m[91m-                     29% |*********                       | 7507k  0:00:48 ETA
[0m[91m-                     31% |**********                      | 8072k  0:00:45 ETA
[0m[91m-                     33% |**********                      | 8627k  0:00:43 ETA
[0m[91m-                     35% |***********                     | 9136k  0:00:41 ETA
[0m[91m-                     37% |************                    | 9705k  0:00:39 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:37 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:35 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:33 ETA
[0m[91m-                     46% [0m[91m|**************                  | 11.6M  0:00:32 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:30 ETA
[0m[91m-                     50% [0m[91m|****************                | 12.7M  0:00:28 ETA
[0m[91m-                     53% |****************                | 13.2M  0:00:27 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:25 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:24 ETA
[0m[91m-                     59% [0m[91m|*******************             | 14.8M  0:00:23 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:21 ETA
[0m[91m-                     63% |********************            | 16.0M  0:00:20 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:18 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:17 ETA
[0m[91m-                    [0m[91m 70% |**********************          | 17.6M  0:00:16 ETA
[0m[91m-                    [0m[91m 72% |***********************         | 18.1M  0:00:15 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:11 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                    [0m[91m 86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:05 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% [0m[91m|******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 3270d0ee46f5
Removing intermediate container 9dfaa139eadd
Step 10/13 : WORKDIR /
 ---> 7acc1b1a75fc
Removing intermediate container 3f9cd8887c36
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e7accc80e134
 ---> db13621cfffd
Removing intermediate container e7accc80e134
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 14c4b7d443d8
 ---> ac4404a6ff89
Removing intermediate container 14c4b7d443d8
Step 13/13 : USER [secure]
 ---> Running in 464378138d7e
 ---> 26205dbed89d
Removing intermediate container 464378138d7e
Successfully built 26205dbed89d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:a1923cb1231d1cc4e515c0bc821b7531290bcdde9aa979b85e6c7f36d0b76068
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b7b39f72b803dc8dacd3af263ce1e925216b080393c15c17b583d342ca06b8f5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1079dad1:start=1572403214138844123,finish=1572403566467757617,duration=352328913494,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:04b2a3e0[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/604758648/log.txt)