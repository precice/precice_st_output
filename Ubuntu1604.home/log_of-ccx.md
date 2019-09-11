 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583691853) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3530c57a8cfa) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     14% |****                            | 3829k  0:00:51 ETA
[0m[91m-                     17% |*****                           | 4400k  0:00:48 ETA
[0m[91m-                     19% |******                          | 4973k  0:00:45 ETA
[0m[91m-                     21% |******                          | 5532k[0m[91m  0:00:43 ETA
[0m[91m-                     23% [0m[91m|*******                         | 6040k  0:00:42 ETA
[0m[91m-                     25% |********                        | 6610k  0:00:40 ETA
[0m[91m-                     27% |********                        | 7170k  0:00:38 ETA
[0m[91m-                     30% |*********                       | 7736k  0:00:37 ETA
[0m[91m-                    [0m[91m 32% [0m[91m|**********                      | 8241k  0:00:35 ETA
[0m[91m-                     34% |**********                      | 8807k  0:00:34 ETA
[0m[91m-                     36% |***********                     | 9376k  0:00:32 ETA[0m[91m
[0m[91m-                     38% |************                    | 9945k  0:00:31 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:30 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:29 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:23 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | [0m[91m15.0M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA[0m[91m
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.7M  0:00:00 ETA
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
 ---> d5543dc3d68b
Removing intermediate container b24386654d5a
Step 10/13 : WORKDIR /
 ---> 782508b18842
Removing intermediate container 0225ecb2a914
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 60c3a009484c
 ---> a1da483a46bb
Removing intermediate container 60c3a009484c
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in cd34a16b9ba6
 ---> ccc0c3356f11
Removing intermediate container cd34a16b9ba6
Step 13/13 : USER [secure]
 ---> Running in 89a87140803d
 ---> 04e062e8ce62
Removing intermediate container 89a87140803d
Successfully built 04e062e8ce62
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2647945be3e201da067863b8afffa94cebdbad120ca5cfcf06fdfc56d034eee4
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:1e4a0aaa02ee26d9e50c2b1bc520178d58b16b1cf18bb1d744d33a1d7f3d8c97
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1e0c6e36:start=1568218630674998006,finish=1568218975766524622,duration=345091526616,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:022a9474[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583691868/log.txt)