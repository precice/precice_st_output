## Status: Failure 
Build: [1384](https://travis-ci.org/precice/systemtests/builds/631624532) 

Job: [1384.16](https://travis-ci.org/precice/systemtests/jobs/631624548) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/131) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
Downloading and extracting the Outer-Fluid mesh...
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      0% |                                | 53991  0:08:07 ETA
[0m[91m-                      2% |                                |  527k  0:01:35 ETA
[0m[91m-                      4% |*                               | 1126k  0:01:05 ETA
[0m[91m-                      6% |**                              | 1681k  0:00:56 ETA
[0m[91m-                      8% |**                              | 2295k  0:00:50 ETA
[0m[91m-                     11% |***                             | 2891k  0:00:47 ETA
[0m[91m-                     13% |****                            | 3493k  0:00:44 ETA
[0m[91m-                     15% |*****                           | 4079k  0:00:42 ETA
[0m[91m-                     18% |*****                           | 4657k  0:00:40 ETA
[0m[91m-                     20% |******                          | 5251k  0:00:38 ETA
[0m[91m-                     22% |*******                         | 5847k  0:00:37 ETA
[0m[91m-                     25% |********                        | 6422k  0:00:35 ETA
[0m[91m-                     27% |********                        | 7046k  0:00:34 ETA
[0m[91m-                     29% |*********                       | 7615k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8222k  0:00:31 ETA
[0m[91m-                     34% |***********                     | 8813k  0:00:30 ETA
[0m[91m-                     36% |***********                     | 9383k  0:00:29 ETA
[0m[91m-                     38% |************                    | 9991k  0:00:28 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:26 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:25 ETA
[0m[91m-                     45% |**************                  | 11.5M  0:00:24 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:23 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:22 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:21 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:20 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:19 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:18 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:13 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:12 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:11 ETA
[0m[91m-                     75% |************************        | 19.0M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:09 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:08 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> 2d2d5d726f6c
Removing intermediate container acc4a07a1821
Step 11/14 : WORKDIR /
 ---> e99c2b6e4aa7
Removing intermediate container 33881804b695
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d83592ceaec3
 ---> 84a201be4f28
Removing intermediate container d83592ceaec3
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c87d219b0d47
 ---> 94d86e24b21e
Removing intermediate container c87d219b0d47
Step 14/14 : USER [secure]
 ---> Running in 89483f214987
 ---> db354a52e075
Removing intermediate container 89483f214987
Successfully built db354a52e075
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2eadc3a0c70c4b90e6aa86c93f35b0b1f6d1f10272fd491ce30485450f51e8ca
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:d5d71a6e16a8462bf733bdc4cfcb900614336848d9e9d2a3359da5ec84ccb745
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!

```
[
Full job log](https://api.travis-ci.org/v3/job/631624548/log.txt)