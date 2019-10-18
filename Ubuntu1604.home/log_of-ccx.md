 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599535277) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aeaaaab693ed...bc601c6301d2) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     14% |****                            | 3840k  0:00:45 ETA
[0m[91m-                     17% |*****                           | 4423k  0:00:43 ETA
[0m[91m-                     19% |******                          | 4990k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5492k  0:00:40 ETA
[0m[91m-                    [0m[91m 23% |*******                         | 6052k  0:00:38 ETA
[0m[91m-                     25% |********                        | 6631k  0:00:37 ETA
[0m[91m-                     28% |********                        | 7194k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7698k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8272k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8827k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9403k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9965k  0:00:29 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:28 ETA
[0m[91m-                     46% |**************                  | 11.7M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:24 ETA
[0m[91m-                    [0m[91m 53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                    [0m[91m 55% |*****************               | 13.8M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                    [0m[91m 96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 23db47d302f2
Removing intermediate container abc5929ed8fc
Step 10/13 : WORKDIR /
 ---> 4edc178764e9
Removing intermediate container b7683719adc5
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 77d467285a02
 ---> 432022775c71
Removing intermediate container 77d467285a02
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 13c981128186
 ---> 47bb3f53b89d
Removing intermediate container 13c981128186
Step 13/13 : USER [secure]
 ---> Running in cfb4a0766b95
 ---> 2fd4fc024f95
Removing intermediate container cfb4a0766b95
Successfully built 2fd4fc024f95
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9235d23d74933ab1c4a88a461f57e661efb920ded7187cf11181a207f0c7ea38
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:2904abd42ec49f1b40a8a9e548dc00258b05bc93aa103bfbb5b1049d8024a722
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:01016028:start=1571394143414480702,finish=1571394489543232113,duration=346128751411,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:29c8d98e[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599535301/log.txt)