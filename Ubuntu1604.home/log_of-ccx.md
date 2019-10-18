 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599812196) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63f291b1fec7...efe9b440d9b6) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     10% |***                             | 2757k  0:00:49 ETA
[0m[91m-                     12% |****                            | 3321k  0:00:47 ETA
[0m[91m-                     15% |****                            | 3895k  0:00:44 ETA
[0m[91m-                    [0m[91m 17% |*****                           | 4399k  0:00:43 ETA
[0m[91m-                     19% |******                          | 4961k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5532k  0:00:39 ETA
[0m[91m-                     23% |*******                         | 6101k  0:00:38 ETA
[0m[91m-                     25% |********                        | 6603k  0:00:37 ETA
[0m[91m-                     27% |********                        | 7174k  0:00:36 ETA
[0m[91m-                     30% [0m[91m|*********                       | 7746k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8248k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8818k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9383k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9954k  0:00:29 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:29 ETA
[0m[91m-                     43% |*************                   | 10.7M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.2M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                    [0m[91m 71% |**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 31be1890aa09
Removing intermediate container 366771c15aeb
Step 10/13 : WORKDIR /
 ---> 97831a6db276
Removing intermediate container 68b9b3250916
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in be2eccb51445
 ---> b0cc488e2cf1
Removing intermediate container be2eccb51445
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 4844634ca72c
 ---> a3a5306caec9
Removing intermediate container 4844634ca72c
Step 13/13 : USER [secure]
 ---> Running in 927277ff9dc8
 ---> 632e3f6a0049
Removing intermediate container 927277ff9dc8
Successfully built 632e3f6a0049
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8e9ef052033a14d0f1539684ea21cf608caecbb20bc75664dcdb75cf1c3a9b4b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:07b8b50aacfe68aa4259ba130991437a93f96fa2a4812bd6c7cea1d8e9948aa2
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/599812214/log.txt)