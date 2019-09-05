 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581134218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     10% |***                             | 2789k  0:00:57 ETA
[0m[91m-                     12% |****                            | 3222k  0:00:55 ETA
[0m[91m-                     14% |****                            | 3715k  0:00:53 ETA
[0m[91m-                     16% |*****                           | 4282k  0:00:49 ETA
[0m[91m-                     18% [0m[91m|******                          | 4842k  0:00:47 ETA
[0m[91m-                     21% |******                          | 5414k  0:00:44 ETA
[0m[91m-                     23% |*******                         | 5921k  0:00:43 ETA
[0m[91m-                     25% |********                        | 6485k  0:00:41 ETA
[0m[91m-                    [0m[91m 27% |********                        | 7053k  0:00:39 ETA
[0m[91m-                     29% |*********                       | 7628k  0:00:37 ETA
[0m[91m-                     31% |**********                      | 8132k  0:00:36 ETA
[0m[91m-                     33% |**********                      | 8691k[0m[91m  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9258k  0:00:33 ETA
[0m[91m-                     38% [0m[91m|************                    | 9771k  0:00:32 ETA
[0m[91m-                     38% [0m[91m|************                    | 9945k  0:00:33 ETA
[0m[91m-                     39% |************                    | 10.0M  0:00:33 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:32 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:30 ETA[0m[91m
[0m[91m-                     45% |**************                  | 11.4M  0:00:29 ETA
[0m[91m-                    [0m[91m 48% |***************                 | 12.0M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:27 ETA
[0m[91m-                     52% |****************                | 13.0M[0m[91m  0:00:26 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:25 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:24 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:23 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:22 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:21 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:19 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:18 ETA
[0m[91m-                    [0m[91m 68% |**********************          | 17.2M  0:00:17 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:14 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:12 ETA
[0m[91m-                    [0m[91m 79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:09 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 25.0M[0m[91m  0:00:00 ETA
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
 ---> 7ce0e8987d65
Removing intermediate container 26a58d2d9421
Step 10/13 : WORKDIR /
 ---> 2cafd9b4f3c7
Removing intermediate container 7ecb71f23c1f
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7068f6fed59f
 ---> 05d0601bb6e6
Removing intermediate container 7068f6fed59f
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 3f74419a6b10
 ---> 958bdaec6905
Removing intermediate container 3f74419a6b10
Step 13/13 : USER [secure]
 ---> Running in 720054a9cce3
 ---> 828c721467e1
Removing intermediate container 720054a9cce3
Successfully built 828c721467e1
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e4ceba9207e6feb6ba7b138c24c9fcf8811fbdf85c4fdb6ce35ca4f26b272e3a
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
[Full job log](https://api.travis-ci.org/v3/job/581134232/log.txt)