 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598783692) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/108) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     23% |*******                         | 6037k  0:00:38 ETA
[0m[91m-                    [0m[91m 25% |********                        | 6599k  0:00:37 ETA
[0m[91m-                     27% |********                        | 7147k  0:00:36 ETA
[0m[91m-                     29% |*********                       | 7678k  0:00:35 ETA
[0m[91m-                     32% |**********                      | 8240k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8818k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9386k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9923k  0:00:30 ETA
[0m[91m-                     40% [0m[91m|*************                   | 10.2M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA[0m[91m
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     87% [0m[91m|***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:05 ETA
[0m[91m-                     92% [0m[91m|*****************************   | 23.1M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA
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
 ---> ac7b7301b442
Removing intermediate container 91741d7e0a35
Step 10/13 : WORKDIR /
 ---> db87b18540cb
Removing intermediate container 13746a6ef456
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 381eac7bfe27
 ---> d96c213f4836
Removing intermediate container 381eac7bfe27
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ff8c3f4c58ee
 ---> 3017828ae5f6
Removing intermediate container ff8c3f4c58ee
Step 13/13 : USER [secure]
 ---> Running in 7ae206c57b96
 ---> e5e9a9dc2873
Removing intermediate container 7ae206c57b96
Successfully built e5e9a9dc2873
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:14c454f027edb7ee09d95f55057266e2975bf722f078ec6dd2abb625be3db80e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:8b59c9ea454a4530b88813d1be1739d3cd2f0a75b2b013904ef38ef948e2d887
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:052ebb38:start=1571252852969937821,finish=1571253249369342897,duration=396399405076,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:21166464[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598783707/log.txt)