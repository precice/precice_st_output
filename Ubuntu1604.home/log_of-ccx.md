 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598541158) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/478596e1ce45...2f42d88d1871) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                      2% |                                |  618k  0:01:20 ETA
[0m[91m-                      3% |*                               |  801k  0:01:32 ETA
[0m[91m-                      4% |*                               | 1227k  0:01:19 ETA
[0m[91m-                    [0m[91m  6% |**                              | 1699k  0:01:10 ETA
[0m[91m-                      8% [0m[91m|**                              | 2271k  0:01:01 ETA
[0m[91m-                     11% |***                             | 2839k  0:00:56 ETA
[0m[91m-                     13% |****                            | 3404k  0:00:52 ETA
[0m[91m-                     15% |****                            | 3899k  0:00:50 ETA
[0m[91m-                     17% |*****                           | 4478k  0:00:47 ETA
[0m[91m-                     19% |******                          | 5036k  0:00:44 ETA
[0m[91m-                     21% |*******                         | 5614k  0:00:42 ETA
[0m[91m-                     23% |*******                         | 6120k  0:00:41 ETA
[0m[91m-                     26% |********                        | 6685k  0:00:39 ETA
[0m[91m-                     28% |*********                       | 7248k  0:00:38 ETA
[0m[91m-                     30% |*********                       | 7810k  0:00:36 ETA
[0m[91m-                     32% |**********                      | 8325k  0:00:35 ETA
[0m[91m-                     34% |***********                     | 8896k  0:00:33 ETA
[0m[91m-                     36% |***********                     | 9456k  0:00:32 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:31 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:29 ETA
[0m[91m-                     46% [0m[91m|***************                 | 11.7M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:20 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M[0m[91m  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
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
 ---> 7b66128f0865
Removing intermediate container 98ad6f6665a0
Step 10/13 : WORKDIR /
 ---> d4b48d2dc98b
Removing intermediate container ffe833aef7a9
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 6191dd48bfa9
 ---> d209681f79aa
Removing intermediate container 6191dd48bfa9
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0c18522e2e1b
 ---> 48e876bc7d4e
Removing intermediate container 0c18522e2e1b
Step 13/13 : USER [secure]
 ---> Running in 28231d8a9fd4
 ---> 972027569874
Removing intermediate container 28231d8a9fd4
Successfully built 972027569874
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7d002fc20b8a936e9af3f431707439657c2fb037fc483b62dc29cc6c0384e923
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:d029a5bd86e16a33d7767d620899712b687885ed281c63bcb4110aa9320adf97
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/598541173/log.txt)