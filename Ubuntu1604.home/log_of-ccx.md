 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581200523) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/a5fe66e3237c...5b9de68efcd3) 
## Last 100 lines of the job log at the moment of push...
```
 [91m-                      0% |                                |  238k  0:03:32 ETA
[0m[91m-                      3% |*                               |  810k  0:01:31 ETA
[0m[91m-                    [0m[91m  5% |*                               | 1321k  0:01:13 ETA
[0m[91m-                      7% |**                              | 1882k  0:01:03 ETA
[0m[91m-                      9% |***                             | 2439k  0:00:57 ETA
[0m[91m-                     11% |***                             | 2961k  0:00:53 ETA
[0m[91m-                     13% |****                            | 3500k  0:00:50 ETA
[0m[91m-                     15% |*****                           | 4026k  0:00:48 ETA
[0m[91m-                     17% |*****                           | 4581k  0:00:45 ETA
[0m[91m-                     19% |******                          | 5100k  0:00:44 ETA
[0m[91m-                     22% |*******                         | 5679k  0:00:42 ETA
[0m[91m-                     24% |*******                         | 6183k  0:00:40 ETA[0m[91m
[0m[91m-                     26% |********                        | 6745k  0:00:39 ETA
[0m[91m-                    [0m[91m 28% |*********                       | 7247k  0:00:38 ETA
[0m[91m-                     30% [0m[91m|*********                       | 7812k[0m[91m  0:00:36 ETA[0m[91m
[0m[91m-                     32% |**********                      | 8370k  0:00:35 ETA
[0m[91m-                     34% |***********                     | 8890k  0:00:33 ETA
[0m[91m-                     36% |***********                     | 9438k  0:00:32 ETA
[0m[91m-                    [0m[91m 38% |************                    | 9955k  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.2M  0:00:30 ETA
[0m[91m-                     43% |*************                   | 10.7M  0:00:29 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     53% [0m[91m|*****************               | 13.4M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     59% |*******************             | 15.0M  0:00:20 ETA
[0m[91m-                    [0m[91m 61% [0m[91m|*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                    [0m[91m 68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA[0m[91m
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M[0m[91m  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 25.0M  0:00:00 ETA
-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> b6a193fc7197
Removing intermediate container 532359d208c2
Step 10/13 : WORKDIR /
 ---> 8c8141ae5b04
Removing intermediate container 84010c4d3235
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 5489ac8e8be4
 ---> c95d68aeb88b
Removing intermediate container 5489ac8e8be4
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0e3f861b3df0
 ---> d4d4f8363082
Removing intermediate container 0e3f861b3df0
Step 13/13 : USER [secure]
 ---> Running in d41ba422c6ec
 ---> c2c783090219
Removing intermediate container d41ba422c6ec
Successfully built c2c783090219
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
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581200537/log.txt)