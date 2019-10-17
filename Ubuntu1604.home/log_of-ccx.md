 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599241988) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/58fea094b8a4...67d504057297) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     15% |****                            | 3901k  0:00:50 ETA
[0m[91m-                     17% |*****                           | 4471k  0:00:47 ETA
[0m[91m-                     19% |******                          | 5044k  0:00:44 ETA
[0m[91m-                     21% |*******                         | 5612k  0:00:42 ETA
[0m[91m-                     24% |*******                         | 6173k  0:00:40 ETA
[0m[91m-                     26% |********                        | 6686k  0:00:39 ETA
[0m[91m-                     28% |*********                       | 7248k  0:00:38 ETA[0m[91m
[0m[91m-                     30% |*********                       | 7822k  0:00:36 ETA
[0m[91m-                     32% |**********                      | 8380k  0:00:34 ETA
[0m[91m-                     34% |***********                     | 8889k  0:00:33 ETA
[0m[91m-                     36% |***********                     | 9459k  0:00:32 ETA
[0m[91m-                    [0m[91m 39% [0m[91m|************                    |  9.7M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:29 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:28 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.5M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.5M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> ef9cd2db3480
Removing intermediate container 1c6146719c7c
Step 10/13 : WORKDIR /
 ---> a160a38d16d4
Removing intermediate container b7317f555d73
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 75a3de467338
 ---> 24e0c14014b8
Removing intermediate container 75a3de467338
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 490daf5e9e8c
 ---> 568ce76f8855
Removing intermediate container 490daf5e9e8c
Step 13/13 : USER [secure]
 ---> Running in 79283f22d2e8
 ---> b159c16d26f6
Removing intermediate container 79283f22d2e8
Successfully built b159c16d26f6
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9d0c3e1b98eaa8f1a730eb5f148bb2285fb17194b6695041112ff9c6279b21ed
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0108e1c578385621dd5c254ef7f0d4eceeb631d159af25d772e9d9acca0860bd
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
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
travis_time:end:12d8630c:start=1571334622794537344,finish=1571334969986073799,duration=347191536455,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00074530[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599242003/log.txt)