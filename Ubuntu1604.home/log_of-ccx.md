## Status: Passing 
Build: [1032](https://travis-ci.org/precice/systemtests/builds/603568985) 

Job: [1032.15](https://travis-ci.org/precice/systemtests/jobs/603569000) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e6ee51b6890c...5e709cade038) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                      4% |*                               | 1067k  0:02:18 ETA
[0m[91m-                      4% |*                               | 1067k  0:02:41 ETA
[0m[91m-                      4% |*                               | 1125k  0:02:54 ETA
[0m[91m-                      6% |*                               | 1569k  0:02:17 ETA
[0m[91m-                      8% |**                              | 2079k  0:01:53 ETA
[0m[91m-                     10% |***                             | 2650k  0:01:35 ETA
[0m[91m-                     12% |****                            | 3221k  0:01:23 ETA
[0m[91m-                     14% |****                            | 3721k  0:01:16 ETA
[0m[91m-                     16% |*****                           | 4284k[0m[91m  0:01:09 ETA
[0m[91m-                     18% |*****                           | 4792k  0:01:05 ETA
[0m[91m-                     20% |******                          | 5356k  0:01:00 ETA
[0m[91m-                     23% |*******                         | 5932k  0:00:56 ETA
[0m[91m-                     25% |********                        | 6437k  0:00:53 ETA[0m[91m
[0m[91m-                     27% |********                        | 7001k  0:00:50 ETA
[0m[91m-                     29% |*********                       | 7495k  0:00:48 ETA[0m[91m
[0m[91m-                     31% |**********                      | 8063k  0:00:45 ETA
[0m[91m-                    [0m[91m 33% [0m[91m|**********                      | 8626k  0:00:43 ETA
[0m[91m-                     35% |***********                     | 9136k  0:00:41 ETA
[0m[91m-                     37% |************                    | 9709k  0:00:39 ETA
[0m[91m-                     39% [0m[91m|************                    |  9.9M  0:00:37 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:35 ETA
[0m[91m-                     44% [0m[91m|**************                  | 11.0M  0:00:34 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:32 ETA
[0m[91m-                     48% [0m[91m|***************                 | 12.1M  0:00:30 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:29 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:27 ETA
[0m[91m-                     54% [0m[91m|*****************               | 13.7M  0:00:26 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:25 ETA
[0m[91m-                     59% [0m[91m|******************              | 14.7M  0:00:23 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:22 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:20 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:19 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:18 ETA
[0m[91m-                    [0m[91m 69% |**********************          | 17.4M  0:00:17 ETA
[0m[91m-                    [0m[91m 71% |**********************          | 17.9M  0:00:15 ETA[0m[91m
[0m[91m-                    [0m[91m 73% |***********************         | 18.4M  0:00:14 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:13 ETA
[0m[91m-                    [0m[91m 77% |************************        | 19.5M  0:00:12 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:08 ETA
[0m[91m-                    [0m[91m 85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:07 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M[0m[91m  0:00:01 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 0709369f426b
Removing intermediate container 084e7fc41b62
Step 10/13 : WORKDIR /
 ---> 6dbd36eaa9bb
Removing intermediate container 54bbab12346c
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 6f6270f20883
 ---> 3c2e34062c2d
Removing intermediate container 6f6270f20883
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 78d0b6fb1e47
 ---> c374e042d3a5
Removing intermediate container 78d0b6fb1e47
Step 13/13 : USER [secure]
 ---> Running in 573c267a67da
 ---> 500219fa8c49
Removing intermediate container 573c267a67da
Successfully built 500219fa8c49
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:97bb7e6e100569ab857c2847a688e902aeedb81af15a98a336fc9272ade3829f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:a59c48444b2c74cb0ec38c888f212a18fa25b7c1c1263ec3f18dad4b8018ebd2
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/603569000/log.txt)