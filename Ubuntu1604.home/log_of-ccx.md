 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581674796) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/88) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                    [0m[91m 19% [0m[91m|******                          | 5065k  0:00:40 ETA
[0m[91m-                     21% |*******                         | 5621k  0:00:39 ETA
[0m[91m-                     24% |*******                         | 6184k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6705k  0:00:36 ETA
[0m[91m-                     28% |*********                       | 7280k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7823k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8398k  0:00:32 ETA
[0m[91m-                     34% |***********                     | 8909k  0:00:31 ETA
[0m[91m-                     36% |***********                     | 9481k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.5M  0:00:24 ETA
[0m[91m-                     51% |****************                | 13.0M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% [0m[91m|***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                    [0m[91m 87% [0m[91m|****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     96% [0m[91m|******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     97% |******************************* | [0m[91m24.5M  0:00:01 ETA
[0m[91m-                     99% [0m[91m|******************************* | 25.0M  0:00:00 ETA
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
 ---> 27c5c50d0a23
Removing intermediate container 55e16a090428
Step 10/13 : WORKDIR /
 ---> 4f7e1549d282
Removing intermediate container 598d5ef20b90
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 1c4ed02ef35b
 ---> 13ad3b8a25ef
Removing intermediate container 1c4ed02ef35b
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 3b586137f351
 ---> 305610b9ecbc
Removing intermediate container 3b586137f351
Step 13/13 : USER [secure]
 ---> Running in d36b557b9094
 ---> 7ad6252f23fa
Removing intermediate container d36b557b9094
Successfully built 7ad6252f23fa
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:be8e37fe141c3aebfdaea18d27b3ffa9ef98fadcfc17a3167f5925fc0e3dc0ea
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b97f3bf0742fa58bb2a132c5952c83d04958654227347d4ec3581e12ca675459
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:011be468:start=1567776800639347353,finish=1567777147806788984,duration=347167441631,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:045192f9[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581674808/log.txt)