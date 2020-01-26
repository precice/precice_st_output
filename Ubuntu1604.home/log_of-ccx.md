## Status: Failure 
Build: [1519](https://travis-ci.org/precice/systemtests/builds/641972691) 

Job: [1519.16](https://travis-ci.org/precice/systemtests/jobs/641972707) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/161) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/pull/157) 

---
Last 100 lines of the job log at the moment of push:
```
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      1% |                                |  269k  0:01:34 ETA
[0m[91m-                      3% |*                               |  840k  0:00:59 ETA
[0m[91m-                      5% |*                               | 1447k  0:00:50 ETA
[0m[91m-                      7% |**                              | 2039k  0:00:46 ETA
[0m[91m-                     10% |***                             | 2650k  0:00:43 ETA
[0m[91m-                     12% |****                            | 3230k  0:00:41 ETA
[0m[91m-                     14% |****                            | 3805k  0:00:40 ETA
[0m[91m-                     17% |*****                           | 4415k  0:00:38 ETA
[0m[91m-                     19% |******                          | 5006k  0:00:37 ETA
[0m[91m-                     21% |******                          | 5572k  0:00:35 ETA
[0m[91m-                     24% |*******                         | 6179k  0:00:34 ETA
[0m[91m-                     26% |********                        | 6781k  0:00:33 ETA
[0m[91m-                     28% |*********                       | 7391k  0:00:32 ETA
[0m[91m-                     31% |*********                       | 7959k  0:00:31 ETA
[0m[91m-                     33% |**********                      | 8535k  0:00:30 ETA
[0m[91m-                     35% |***********                     | 9152k  0:00:28 ETA
[0m[91m-                     37% |************                    | 9736k  0:00:27 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:26 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:26 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:27 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:26 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:22 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:22 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:20 ETA
[0m[91m-                     59% |******************              | 14.7M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     66% |*********************           | [0m[91m16.5M[0m[91m  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
[0m[91mwritten to stdout
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
 ---> 6e5904461281
Removing intermediate container b55f935bb326
Step 11/14 : WORKDIR /
 ---> f7fe4524d1cf
Removing intermediate container 815afddff342
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 4263617c14c2
 ---> 8192c7332608
Removing intermediate container 4263617c14c2
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b66e0953188e
 ---> 63b1a69e97b9
Removing intermediate container b66e0953188e
Step 14/14 : USER [secure]
 ---> Running in d76958afd66e
 ---> d3a927d59b63
Removing intermediate container d76958afd66e
Successfully built d3a927d59b63
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ab232f3ec4153d1e6e56dc63acc9ebce94d07174940d32a6b37e4e1c545878e8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:dc9a96815bd271e83d220b6f7fb4a42fc4f9057c333c5f6264b05d8ba55e2928
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/641972707/log.txt)