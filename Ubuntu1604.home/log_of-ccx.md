## Status: Passing 
Build: [1030](https://travis-ci.org/precice/systemtests/builds/603395419) 

Job: [1030.19](https://travis-ci.org/precice/systemtests/jobs/603395438) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                      5% |*                               | 1338k  0:01:30 ETA
[0m[91m-                      7% |**                              | 1892k  0:01:15 ETA
[0m[91m-                      9% |***                             | 2468k  0:01:05 ETA
[0m[91m-                     11% |***                             | 2972k  0:01:00 ETA
[0m[91m-                     13% |****                            | 3531k  0:00:56 ETA
[0m[91m-                     16% |*****                           | 4108k  0:00:52 ETA
[0m[91m-                     18% |*****                           | 4671k  0:00:49 ETA[0m[91m
[0m[91m-                     20% |******                          | 5172k  0:00:47 ETA
[0m[91m-                    [0m[91m 22% |*******                         | 5748k  0:00:44 ETA
[0m[91m-                     23% |*******                         | 5915k  0:00:46 ETA
[0m[91m-                     24% |*******                         | 6242k  0:00:46 ETA
[0m[91m-                     25% |********                        | [0m[91m6642k  0:00:45 ETA
[0m[91m-                     28% |********                        | 7204k  0:00:43 ETA
[0m[91m-                     28% |*********                       | 7392k  0:00:44 ETA
[0m[91m-                     29% |*********                       | 7673k  0:00:44 ETA
[0m[91m-                     31% |**********                      | 8136k  0:00:43 ETA
[0m[91m-                     33% |**********                      | 8708k  0:00:40 ETA
[0m[91m-                     36% |***********                     | 9275k  0:00:38 ETA
[0m[91m-                    [0m[91m 38% [0m[91m|************                    | 9779k  0:00:37 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:35 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:33 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:32 ETA
[0m[91m-                     46% |**************                  | 11.7M  0:00:30 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:29 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:27 ETA
[0m[91m-                     53% [0m[91m|*****************               | 13.3M  0:00:26 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:25 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:23 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:21 ETA
[0m[91m-                     63% |********************            | 16.0M  0:00:19 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:17 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:14 ETA
[0m[91m-                    [0m[91m 75% |************************        | 18.9M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.5M  0:00:12 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:09 ETA
[0m[91m-                    [0m[91m 84% |**************************      | 21.1M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:06 ETA
[0m[91m-                    [0m[91m 90% [0m[91m|*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | [0m[91m23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                    [0m[91m 99% [0m[91m|******************************* | 24.8M  0:00:00 ETA[0m[91m
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA
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
 ---> b63d4ac34b08
Removing intermediate container 998c7ef85a70
Step 10/13 : WORKDIR /
 ---> f522ba099421
Removing intermediate container 13ee85377144
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 793b0068efaa
 ---> 9b3fd08b0116
Removing intermediate container 793b0068efaa
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b301514276c2
 ---> 29eaf8614319
Removing intermediate container b301514276c2
Step 13/13 : USER [secure]
 ---> Running in 90ed0b734b14
 ---> 03df53e862e3
Removing intermediate container 90ed0b734b14
Successfully built 03df53e862e3
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d8a5bfbc8deb1b0507d1dc8aa3f8ccef96ebe5eb58582e4d759442585182293c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:5ecc74285614abcb7648c79bcfa63c162f7e7df01d6be606971299ee9847947f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/603395438/log.txt)