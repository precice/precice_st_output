## Status: Passing 
Build: [1048](https://travis-ci.org/precice/systemtests/builds/605292585) 

Job: [1048.19](https://travis-ci.org/precice/systemtests/jobs/605292604) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[91m-                      1% |                                |  414k  0:02:01 ETA
[0m[91m-                      3% [0m[91m|*                               |  941k  0:01:18 ETA
[0m[91m-                      5% |*                               | 1499k  0:01:04 ETA
[0m[91m-                      8% |**                              | 2061k  0:00:57 ETA[0m[91m
[0m[91m-                     10% |***                             | 2616k  0:00:52 ETA
[0m[91m-                     12% |***                             | 3133k  0:00:50 ETA
[0m[91m-                     14% |****                            | 3702k  0:00:47 ETA
[0m[91m-                     16% |*****                           | 4272k  0:00:44 ETA
[0m[91m-                     18% |******                          | 4835k  0:00:43 ETA
[0m[91m-                     20% |******                          | 5343k  0:00:41 ETA
[0m[91m-                     23% |*******                         | 5913k  0:00:40 ETA
[0m[91m-                     25% [0m[91m|********                        | 6483k  0:00:38 ETA
[0m[91m-                     27% |********                        | 7029k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7554k  0:00:35 ETA
[0m[91m-                     31% |**********                      | 8124k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8686k  0:00:33 ETA
[0m[91m-                     36% |***********                     | 9270k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9764k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.2M[0m[91m  0:00:27 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% [0m[91m|******************              | 14.4M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:14 ETA
[0m[91m-                     71% [0m[91m|**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M[0m[91m  0:00:12 ETA
[0m[91m-                     78% |************************        | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% [0m[91m|******************************* | 24.6M  0:00:00 ETA
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
 ---> a6f9958086aa
Removing intermediate container 3f6ccacef9fb
Step 10/13 : WORKDIR /
 ---> 8f0995c0c0a7
Removing intermediate container 5eb1d8f0efeb
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 6a1484cb8709
 ---> bfefdc77ae87
Removing intermediate container 6a1484cb8709
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1723771e4838
 ---> 0ebb44bc31fd
Removing intermediate container 1723771e4838
Step 13/13 : USER [secure]
 ---> Running in 950a03425b5c
 ---> 2494070619cd
Removing intermediate container 950a03425b5c
Successfully built 2494070619cd
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:fb635a84da883c6511a60b5b910a60599e4ef789b46704d8959215aa07274e1c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:711f476fc18badf51c238a19f23c63991b879e7c29d89d5a56418d0becaab9f5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/605292604/log.txt)