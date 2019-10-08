 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/594964989) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/92a2d96de651...58fea094b8a4) 
## Last 100 lines of the job log at the moment of push...
```
 [91m-                      0% |                                | 33628  0:13:01 ETA
[0m[91m-                      1% |                                |  465k  0:01:48 ETA
[0m[91m-                      4% |*                               | 1031k  0:01:11 ETA
[0m[91m-                      5% |*                               | 1536k  0:01:02 ETA
[0m[91m-                      8% |**                              | 2100k  0:00:56 ETA
[0m[91m-                     10% |***                             | 2672k  0:00:51 ETA
[0m[91m-                     12% |****                            | 3232k  0:00:48 ETA
[0m[91m-                     14% |****                            | 3734k  0:00:46 ETA
[0m[91m-                    [0m[91m 16% |*****                           | 4305k[0m[91m  0:00:44 ETA
[0m[91m-                     17% |*****                           | 4582k  0:00:45 ETA
[0m[91m-                     18% |******                          | 4842k  0:00:47 ETA
[0m[91m-                     20% |******                          | 5270k  0:00:46 ETA
[0m[91m-                     22% |*******                         | 5749k  0:00:44 ETA
[0m[91m-                     24% |*******                         | 6318k  0:00:42 ETA
[0m[91m-                     26% |********                        | 6889k  0:00:40 ETA
[0m[91m-                     29% |*********                       | 7451k  0:00:39 ETA
[0m[91m-                     31% |*********                       | 7969k  0:00:37 ETA
[0m[91m-                     33% |**********                      | 8536k  0:00:36 ETA
[0m[91m-                     35% |***********                     | 9092k  0:00:34 ETA
[0m[91m-                     37% |************                    | [0m[91m9671k[0m[91m  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:29 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:28 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                    [0m[91m 69% [0m[91m|**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                     99% [0m[91m|******************************* | [0m[91m25.0M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> ae5d264b3c98
Removing intermediate container 6d045e2a1b98
Step 10/13 : WORKDIR /
 ---> b2593191c0f2
Removing intermediate container eafc337e974b
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 0f183bb25eb1
 ---> f5e4da51485d
Removing intermediate container 0f183bb25eb1
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2874a0c6baa8
 ---> ed6479cc7dbf
Removing intermediate container 2874a0c6baa8
Step 13/13 : USER [secure]
 ---> Running in 7fdc276f3b24
 ---> e9632527ff78
Removing intermediate container 7fdc276f3b24
Successfully built e9632527ff78
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c65296c31938f09bcdc7e786618bfb96816d62bf502e46560432dc0890d7c016
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b9581071bafdba447d81f1b9a17aee3ff1a06c6601cba1f1487a6c00cdd4f48b
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
 ```
[Full job log](https://api.travis-ci.org/v3/job/594965004/log.txt)