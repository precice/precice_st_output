 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598566611) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/2f42d88d1871...b7b408e19d9a) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                      8% |**                              | 2242k  0:00:52 ETA
[0m[91m-                     10% |***                             | 2805k  0:00:48 ETA
[0m[91m-                     13% |****                            | 3374k  0:00:46 ETA
[0m[91m-                     15% |****                            | 3891k  0:00:44 ETA
[0m[91m-                     17% |*****                           | 4459k  0:00:42 ETA
[0m[91m-                     19% |******                          | 5001k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5530k  0:00:39 ETA
[0m[91m-                     23% |*******                         | 6101k  0:00:38 ETA
[0m[91m-                     25% |********                        | 6662k  0:00:37 ETA
[0m[91m-                     28% |*********                       | 7211k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7740k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8310k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8857k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9374k[0m[91m  0:00:31 ETA
[0m[91m-                     38% |************                    | 9944k  0:00:29 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:28 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:29 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:30 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:29 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:28 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:26 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:25 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:24 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:21 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:14 ETA
[0m[91m-                     75% |************************        | 18.9M[0m[91m  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.5M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.1M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                    [0m[91m 88% |****************************    | 22.1M  0:00:05 ETA[0m[91m
[0m[91m-                    [0m[91m 90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | [0m[91m23.8M  0:00:02 ETA
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
 ---> a123560da7f5
Removing intermediate container 9892b56a5a40
Step 10/13 : WORKDIR /
 ---> 84e6f7c5d6d2
Removing intermediate container 01bff4d4ed5b
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 36eb193a4120
 ---> 37caf6953b01
Removing intermediate container 36eb193a4120
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e2680ee956f7
 ---> 4719754ba281
Removing intermediate container e2680ee956f7
Step 13/13 : USER [secure]
 ---> Running in 5fdb4c18b0c3
 ---> 5c7de737ec1f
Removing intermediate container 5fdb4c18b0c3
Successfully built 5c7de737ec1f
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9f4bea0bd5475298880a55c225f8884daa36eb25aa4cd548dd6844eef5407e40
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:c9a72c5280818cdd4315a20905f00ad8c69e8a651ef2aa9ecee4d33e0f161901
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
Running the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/598566626/log.txt)