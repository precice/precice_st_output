 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593438448) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/46a3f0d5dc83...a992016cf5d2) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     13% |****                            | 3376k  0:00:52 ETA
[0m[91m-                     15% |****                            | 3916k  0:00:49 ETA
[0m[91m-                     17% |*****                           | 4467k  0:00:47 ETA
[0m[91m-                     19% |******                          | 5045k  0:00:44 ETA
[0m[91m-                     21% |******                          | 5586k  0:00:43 ETA
[0m[91m-                     23% |*******                         | 6126k  0:00:41 ETA
[0m[91m-                     26% |********                        | 6686k  0:00:39 ETA
[0m[91m-                     28% |*********                       | 7250k  0:00:38 ETA
[0m[91m-                     30% |*********                       | 7783k  0:00:36 ETA
[0m[91m-                     32% |**********                      | 8337k  0:00:35 ETA
[0m[91m-                     34% |***********                     | 8892k  0:00:33 ETA
[0m[91m-                     36% |***********                     | 9431k  0:00:32 ETA
[0m[91m-                     39% |************                    | 9999k  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:30 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:28 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:22 ETA
[0m[91m-                    [0m[91m 56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M[0m[91m  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA
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
 ---> c378eb7e7b9b
Removing intermediate container db4873934cd9
Step 10/13 : WORKDIR /
 ---> 683bd9e4db39
Removing intermediate container 7fa2b1df7da4
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 8f0f93b8b27b
 ---> 9fb1d03faee1
Removing intermediate container 8f0f93b8b27b
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 96c0f26bbaa9
 ---> 682fcdfb6bd4
Removing intermediate container 96c0f26bbaa9
Step 13/13 : USER [secure]
 ---> Running in d5cb3005c47a
 ---> 877b6495e6ba
Removing intermediate container d5cb3005c47a
Successfully built 877b6495e6ba
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:aa92deb706c423affecf0ab585f41e6d8fd965503ebcd5fae2671f58ae9ea6a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:c6e3a1abc24e4282b8dde3a9e6413b75ac189beff8c003f16172b01dec2792f4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03a84710:start=1570181492587022355,finish=1570181837456308665,duration=344869286310,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1a623e18[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593438471/log.txt)