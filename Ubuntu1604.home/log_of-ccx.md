## Status: Failure 
Build: [1363](https://travis-ci.org/precice/systemtests/builds/629608911) 

Job: [1363.19](https://travis-ci.org/precice/systemtests/jobs/629608933) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      0% |                                |  120k  0:03:32 ETA
[0m[91m-                      2% |                                |  724k  0:01:08 ETA
[0m[91m-                      5% |*                               | 1310k  0:00:55 ETA
[0m[91m-                      7% |**                              | 1881k  0:00:50 ETA
[0m[91m-                      9% |***                             | 2488k  0:00:46 ETA
[0m[91m-                     12% |***                             | 3083k  0:00:43 ETA
[0m[91m-                     14% |****                            | 3646k  0:00:42 ETA
[0m[91m-                     16% |*****                           | 4260k  0:00:40 ETA
[0m[91m-                     18% [0m[91m|******                          | 4845k  0:00:38 ETA
[0m[91m-                     21% |******                          | 5412k  0:00:37 ETA
[0m[91m-                     23% |*******                         | 6045k  0:00:35 ETA
[0m[91m-                     25% |********                        | 6612k[0m[91m  0:00:34 ETA
[0m[91m-                     28% |*********                       | 7224k  0:00:33 ETA
[0m[91m-                     30% |*********                       | 7801k  0:00:31 ETA
[0m[91m-                     32% |**********                      | 8372k  0:00:30 ETA
[0m[91m-                     35% |***********                     | 8982k  0:00:29 ETA
[0m[91m-                     37% |***********                     | 9576k  0:00:28 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:27 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:26 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:25 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:24 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:22 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:21 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:20 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:19 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:18 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:17 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:16 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:16 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:15 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:13 ETA
[0m[91m-                     71% |***********************         | 17.9M  0:00:12 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     75% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
written to stdout
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
 ---> 87e226408401
Removing intermediate container 165a58ee9bc4
Step 11/14 : WORKDIR /
 ---> 3bdfc7de95e4
Removing intermediate container a1b18e2676f3
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in c17c5e198cd3
 ---> d721e3373123
Removing intermediate container c17c5e198cd3
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 02024d0ef856
 ---> a0097521b8cc
Removing intermediate container 02024d0ef856
Step 14/14 : USER [secure]
 ---> Running in 1bddd3028d52
 ---> 01eaeadc9c86
Removing intermediate container 1bddd3028d52
Successfully built 01eaeadc9c86
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:a1a5baab556ea2d8fd2fc85bff2e47acd84b39d85aa1e9494077bb4dbf2697d4
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:5696faaaccaa01084435e9c36b6bdba0954cd61b3d4b84990e1849d9717f7c78
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
All adapters finished!

```
[
Full job log](https://api.travis-ci.org/v3/job/629608933/log.txt)