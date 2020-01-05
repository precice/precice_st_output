## Status: Failure 
Build: [1396](https://travis-ci.org/precice/systemtests/builds/632899723) 

Job: [1396.20](https://travis-ci.org/precice/systemtests/jobs/632899743) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      0% |                                | 85136  0:05:07 ETA
[0m[91m-                      2% |                                |  574k  0:01:27 ETA
[0m[91m-                      4% |*                               | 1114k  0:01:06 ETA
[0m[91m-                      6% |**                              | 1685k  0:00:56 ETA
[0m[91m-                      8% |**                              | 2215k  0:00:52 ETA
[0m[91m-                     10% |***                             | 2778k  0:00:49 ETA
[0m[91m-                     13% |****                            | 3350k  0:00:46 ETA
[0m[91m-                     15% |****                            | 3896k  0:00:44 ETA
[0m[91m-                     17% |*****                           | 4415k  0:00:43 ETA
[0m[91m-                     19% |******                          | 4989k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5555k  0:00:39 ETA
[0m[91m-                     23% |*******                         | 6104k  0:00:38 ETA
[0m[91m-                     25% |********                        | 6631k  0:00:37 ETA
[0m[91m-                     28% |********                        | 7187k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7752k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8292k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8864k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9395k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9967k  0:00:29 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> cd4c6580087a
Removing intermediate container 953dd3a48f9d
Step 11/14 : WORKDIR /
 ---> ac18e8251003
Removing intermediate container a4044f879073
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 98dabc5ad904
 ---> a8bd07086d90
Removing intermediate container 98dabc5ad904
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 58349ceafbe3
 ---> 78d9e3c03fa1
Removing intermediate container 58349ceafbe3
Step 14/14 : USER [secure]
 ---> Running in 6aa0395d9c3d
 ---> 797e8af7e26a
Removing intermediate container 6aa0395d9c3d
Successfully built 797e8af7e26a
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:3ab18c507e8bd47b0be2b872093edcab70bf5a758a63df93a1878c720f6aeddb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0c60e597e82754c3a015c905809dbe6569cb63f53f1c07055973e1becae0426b
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

```
[
Full job log](https://api.travis-ci.org/v3/job/632899743/log.txt)