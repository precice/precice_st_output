## Status: Passing 
Build: [993](https://travis-ci.org/precice/systemtests/builds/600693901) 

Job: [993.15](https://travis-ci.org/precice/systemtests/jobs/600693917) 

Triggered by: [push](https://github.com/precice/systemtests/compare/a84a139c2665...500cfbb53a97) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     16% |*****                           | 4172k  0:00:46 ETA
[0m[91m-                     18% |*****                           | 4735k  0:00:44 ETA
[0m[91m-                     20% |******                          | 5309k  0:00:42 ETA
[0m[91m-                     22% |*******                         | 5877k  0:00:40 ETA
[0m[91m-                     24% |*******                         | 6385k  0:00:39 ETA
[0m[91m-                     27% |********                        | 6944k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7518k  0:00:36 ETA
[0m[91m-                     31% |**********                      | 8071k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8592k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9168k  0:00:32 ETA
[0m[91m-                     37% |************                    | 9736k  0:00:31 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:25 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:24 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                    [0m[91m 95% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
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
 ---> 9d277c1b99b9
Removing intermediate container 66747fde57ae
Step 10/13 : WORKDIR /
 ---> 8c01b4ad3ae5
Removing intermediate container f0ca22297260
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 6d076fcb95ed
 ---> c9ac22c08cb5
Removing intermediate container 6d076fcb95ed
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fd99ec648329
 ---> 49e677b2fc03
Removing intermediate container fd99ec648329
Step 13/13 : USER [secure]
 ---> Running in 88b7e53058ea
 ---> 4ef69b4c2728
Removing intermediate container 88b7e53058ea
Successfully built 4ef69b4c2728
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:04602e91508ea2c3b26d367af5b44dc79b28546a9dc09a0543218d00fc13e338
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:a037ebade1e93452033a25e5fc3cc6da25a668b53a8160b052ae3c744ccee4aa
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1e9159f6:start=1571660729888954375,finish=1571661083785664382,duration=353896710007,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0a3a41d4[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/600693917/log.txt)