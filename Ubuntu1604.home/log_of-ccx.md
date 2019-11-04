## Status: Passing 
Build: [1056](https://travis-ci.org/precice/systemtests/builds/606935491) 

Job: [1056.19](https://travis-ci.org/precice/systemtests/jobs/606935513) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     11% |***                             | 2928k  0:00:54 ETA
[0m[91m-                     13% |****                            | 3406k  0:00:52 ETA
[0m[91m-                     15% |****                            | 3904k[0m[91m  0:00:50 ETA
[0m[91m-                     17% |*****                           | 4409k  0:00:48 ETA
[0m[91m-                     19% |******                          | 4928k  0:00:46 ETA
[0m[91m-                     20% |******                          | 5381k  0:00:45 ETA
[0m[91m-                     22% |*******                         | 5877k  0:00:43 ETA
[0m[91m-                     24% |*******                         | 6389k  0:00:42 ETA
[0m[91m-                     26% |********                        | [0m[91m6892k  0:00:40 ETA
[0m[91m-                     28% |*********                       | 7396k  0:00:39 ETA
[0m[91m-                     30% |*********                       | 7900k  0:00:38 ETA
[0m[91m-                     32% |**********                      | 8397k  0:00:36 ETA
[0m[91m-                     34% |***********                     | 8893k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9403k  0:00:34 ETA
[0m[91m-                     38% |************                    | 9896k  0:00:33 ETA
[0m[91m-                     40% |************                    | [0m[91m10.1M  0:00:32 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:31 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:30 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:28 ETA
[0m[91m-                    [0m[91m 48% |***************                 | 12.0M  0:00:27 ETA
[0m[91m-                     50% [0m[91m|****************                | 12.5M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:24 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:20 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:19 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                    [0m[91m 85% [0m[91m|***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.6M  0:00:05 ETA
[0m[91m-                    [0m[91m 92% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:01 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> 3b2b6e5cfcba
Removing intermediate container 41f55403ad0c
Step 10/13 : WORKDIR /
 ---> f992617404be
Removing intermediate container 7614a446a96d
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 6fa4fef63e87
 ---> dd517f1627b7
Removing intermediate container 6fa4fef63e87
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 932d4153ec9d
 ---> 8fb998549e91
Removing intermediate container 932d4153ec9d
Step 13/13 : USER [secure]
 ---> Running in b4b8642d6f9d
 ---> 04c75d51ffdf
Removing intermediate container b4b8642d6f9d
Successfully built 04c75d51ffdf
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:61bc80da6f66c50f0becba80f8502ed08e6c12ff77e5f6f4d4e1419680c98209
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:cb32df1239cc3abc23006ad245f4a7b46255d1860e4cbf3f1dc77af2af863fb5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/606935513/log.txt)