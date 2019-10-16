 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598441565) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/478596e1ce45) 
## Last 100 lines of the job log at the moment of push...
```
 [91m-                      1% |                                |  322k  0:02:37 ETA
[0m[91m-                      3% |*                               |  894k  0:01:22 ETA
[0m[91m-                      5% |*                               | 1420k  0:01:08 ETA
[0m[91m-                      7% |**                              | 1986k  0:00:59 ETA
[0m[91m-                      9% |***                             | 2555k  0:00:54 ETA
[0m[91m-                     12% |***                             | 3097k  0:00:50 ETA
[0m[91m-                     14% |****                            | 3626k  0:00:48 ETA
[0m[91m-                     16% |*****                           | 4203k  0:00:45 ETA
[0m[91m-                     18% |*****                           | 4760k  0:00:43 ETA
[0m[91m-                     20% [0m[91m|******                          | 5293k  0:00:42 ETA
[0m[91m-                     22% |*******                         | 5837k  0:00:40 ETA
[0m[91m-                     24% |*******                         | 6406k  0:00:39 ETA
[0m[91m-                     27% |********                        | 6965k  0:00:37 ETA
[0m[91m-                     28% |*********                       | 7290k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7472k  0:00:38 ETA
[0m[91m-                     30% |*********                       | 7855k  0:00:38 ETA
[0m[91m-                     32% |**********                      | 8362k  0:00:37 ETA
[0m[91m-                     34% |***********                     | 8938k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9446k  0:00:34 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:31 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | [0m[91m16.8M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA[0m[91m
[0m[91m-                     77% |************************        | 19.5M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | [0m[91m22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
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
 ---> 5062e6aeb537
Removing intermediate container 517d8c9dc2ef
Step 10/13 : WORKDIR /
 ---> 8f787233dd58
Removing intermediate container 0a34209fc356
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 94d0a8e6ccdd
 ---> c048e2fee28a
Removing intermediate container 94d0a8e6ccdd
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b6d768ff85b1
 ---> 2f27bc3a7011
Removing intermediate container b6d768ff85b1
Step 13/13 : USER [secure]
 ---> Running in 52c544edd070
 ---> ccc8e4a958f4
Removing intermediate container 52c544edd070
Successfully built ccc8e4a958f4
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8c28a96b26585c04af5ec1ea6f96daea73118195658df2bf9cf7cb3dd45ac81a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:901c31a0c4089f729541bd46b51f88be48f235078d311ca750d119166f0aec8e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/598441587/log.txt)