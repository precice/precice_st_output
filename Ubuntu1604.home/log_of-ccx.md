## Status: Failure 
Build: [1388](https://travis-ci.org/precice/systemtests/builds/632603195) 

Job: [1388.20](https://travis-ci.org/precice/systemtests/jobs/632603215) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0mpolyMesh.org/boundary
[91m-                      1% |                                |  369k  0:02:16 ETA
[0m[91m-                      3% |*                               |  984k  0:01:15 ETA
[0m[91m-                      5% |*                               | 1343k  0:01:12 ETA
[0m[91m-                      5% |*                               | 1529k  0:01:18 ETA
[0m[91m-                      7% |**                              | 1981k  0:01:11 ETA
[0m[91m-                      9% |***                             | 2520k[0m[91m  0:01:04 ETA
[0m[91m-                     12% |***                             | 3154k  0:00:57 ETA
[0m[91m-                     14% |****                            | 3722k  0:00:52 ETA
[0m[91m-                     16% |*****                           | 4293k  0:00:49 ETA
[0m[91m-                     19% |******                          | 4911k  0:00:46 ETA
[0m[91m-                     21% |******                          | 5482k  0:00:44 ETA
[0m[91m-                     23% |*******                         | 6116k  0:00:41 ETA
[0m[91m-                     26% |********                        | 6679k  0:00:39 ETA
[0m[91m-                     28% |*********                       | 7253k  0:00:38 ETA
[0m[91m-                     30% |*********                       | 7888k  0:00:35 ETA
[0m[91m-                     33% |**********                      | 8460k  0:00:34 ETA
[0m[91m-                     34% |***********                     | 8834k  0:00:34 ETA
[0m[91m-                     35% |***********                     | 9081k  0:00:34 ETA
[0m[91m-                     37% |***********                     | 9490k  0:00:34 ETA
[0m[91m-                     39% [0m[91m|************                    |  9.8M  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:29 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:22 ETA
[0m[91m-                     59% |*******************             | 14.8M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.6M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
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
 ---> 34024bf473e5
Removing intermediate container f9fbd47c4331
Step 11/14 : WORKDIR /
 ---> d14ca835721a
Removing intermediate container 3f2cd827d80c
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in dc2f0a0c9a0f
 ---> 453d849ca07a
Removing intermediate container dc2f0a0c9a0f
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c6b236fd6cd4
 ---> 79e7c0f25290
Removing intermediate container c6b236fd6cd4
Step 14/14 : USER [secure]
 ---> Running in 61972c1041a3
 ---> 035c81e3372d
Removing intermediate container 61972c1041a3
Successfully built 035c81e3372d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0a70c4bda4b8a4b21007a5392fa06b986eb68a743e629af06920da7302579693
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:561dff9af197262423d8a518869723f810d0fc5bdba33a093fb43316d1dfd72d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/632603215/log.txt)