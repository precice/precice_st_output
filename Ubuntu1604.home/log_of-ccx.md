 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586647457) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/cd89b1900540...aac1a14c474b) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     14% |****                            | 3826k  0:00:45 ETA
[0m[91m-                     17% |*****                           | 4396k  0:00:43 ETA
[0m[91m-                     19% |******                          | 4935k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5500k  0:00:40 ETA
[0m[91m-                     23% |*******                         | 6029k  0:00:39 ETA[0m[91m
[0m[91m-                     25% |********                        | 6601k  0:00:37 ETA
[0m[91m-                     27% |********                        | 7171k  0:00:36 ETA
[0m[91m-                     30% |*********                       | 7706k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8278k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8813k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9374k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9928k  0:00:30 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA[0m[91m
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.5M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                    [0m[91m 85% [0m[91m|***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
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
 ---> 2fa613c4ba70
Removing intermediate container 331e54add7ac
Step 10/13 : WORKDIR /
 ---> d985f5f21c3e
Removing intermediate container 3bd067538e50
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e4afa6568902
 ---> 96c5c8b7b32d
Removing intermediate container e4afa6568902
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5ff65b1c873b
 ---> 53a7e5a375c4
Removing intermediate container 5ff65b1c873b
Step 13/13 : USER [secure]
 ---> Running in 773f8c57ef34
 ---> 90de121adf87
Removing intermediate container 773f8c57ef34
Successfully built 90de121adf87
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:853d85c34dd7c47fbda46df356c3c2eb58f3f1f322a907dbd536bdd378963dcc
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:84976e75900bfcba1bbee046757ac75d8e4d3dd7f1bf22b52c24a52ad68087a6
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:054dd22f:start=1568830853285446115,finish=1568831202283565216,duration=348998119101,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:06b452e0[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586647472/log.txt)