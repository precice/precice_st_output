## Status: Failure 
Build: [1360](https://travis-ci.org/precice/systemtests/builds/629054356) 

Job: [1360.19](https://travis-ci.org/precice/systemtests/jobs/629054381) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      1% |                                |  510k  0:00:49 ETA
[0m[91m-                      4% |*                               | 1076k  0:00:45 ETA
[0m[91m-                      6% |**                              | 1713k  0:00:41 ETA
[0m[91m-                      8% |**                              | 2276k  0:00:41 ETA
[0m[91m-                     11% |***                             | 2841k  0:00:40 ETA
[0m[91m-                     13% |****                            | 3474k  0:00:38 ETA
[0m[91m-                     15% |*****                           | 4046k  0:00:37 ETA
[0m[91m-                     18% |*****                           | 4673k  0:00:35 ETA
[0m[91m-                     20% |******                          | 5234k  0:00:35 ETA[0m[91m
[0m[91m-                     22% |*******                         | 5810k  0:00:34 ETA
[0m[91m-                     25% |********                        | 6428k  0:00:32 ETA
[0m[91m-                     26% |********                        | 6834k  0:00:33 ETA
[0m[91m-                     27% |********                        | 7007k  0:00:34 ETA
[0m[91m-                     29% |*********                       | 7459k  0:00:34 ETA
[0m[91m-                     31% |*********                       | 7980k  0:00:33 ETA
[0m[91m-                     33% |**********                      | 8616k  0:00:31 ETA
[0m[91m-                     35% |***********                     | 9183k  0:00:30 ETA
[0m[91m-                     38% |************                    | 9753k  0:00:29 ETA
[0m[91m-                     40% |************                    | 10.1M[0m[91m  0:00:27 ETA[0m[91m
[0m[91m-                     42% |*************                   | 10.6M  0:00:26 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:25 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:24 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:18 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:17 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:16 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:15 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:11 ETA
[0m[91m-                     77% |************************        | [0m[91m19.3M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:09 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> 9ce601bbfc46
Removing intermediate container e705e4f0ca0a
Step 11/14 : WORKDIR /
 ---> 4b361db10bd2
Removing intermediate container 5f18810c7c45
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in a387dc2638d7
 ---> 0dbe433ed508
Removing intermediate container a387dc2638d7
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 99eb0920a445
 ---> ba43a3578223
Removing intermediate container 99eb0920a445
Step 14/14 : USER [secure]
 ---> Running in 0b0c7e5cb819
 ---> d1cc60bee45b
Removing intermediate container 0b0c7e5cb819
Successfully built d1cc60bee45b
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:164e164435f8b470b0a42c8de4ccf6a8a760373ebebaf061ccea3235cb13a096
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:45ef4180455b2b27234da48207efbd85830b43aaeec8429c2c8b4534d2639a03
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/629054381/log.txt)