 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599803615) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     10% |***                             | 2705k  0:00:50 ETA
[0m[91m-                    [0m[91m 12% [0m[91m|****                            | 3265k  0:00:47 ETA
[0m[91m-                     14% |****                            | 3838k  0:00:45 ETA
[0m[91m-                     17% |*****                           | 4400k  0:00:43 ETA
[0m[91m-                     19% |******                          | 4963k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5478k[0m[91m  0:00:40 ETA
[0m[91m-                    [0m[91m 23% |*******                         | 6037k  0:00:38 ETA
[0m[91m-                     25% |********                        | 6598k  0:00:37 ETA
[0m[91m-                     27% |********                        | 7167k  0:00:36 ETA
[0m[91m-                     29% |*********                       | 7682k  0:00:35 ETA
[0m[91m-                     32% |**********                      | 8238k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8814k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9377k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9876k  0:00:30 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:29 ETA
[0m[91m-                     42% [0m[91m|*************                   | 10.7M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:24 ETA
[0m[91m-                    [0m[91m 51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% [0m[91m|*******************             | 15.0M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                    [0m[91m 66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                    [0m[91m 81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% [0m[91m|******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 6323aa47d18c
Removing intermediate container 68d93763261a
Step 10/13 : WORKDIR /
 ---> 4338941d0704
Removing intermediate container 7434e409340a
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7aa169aef5fb
 ---> 5a1303b19a7d
Removing intermediate container 7aa169aef5fb
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2c25c8cb34a7
 ---> 60d386eac2e7
Removing intermediate container 2c25c8cb34a7
Step 13/13 : USER [secure]
 ---> Running in 599acfdabb7d
 ---> ab9fb7b92c38
Removing intermediate container 599acfdabb7d
Successfully built ab9fb7b92c38
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d99ac418afb23059999d46ddcd0bebcb574e2f5230b1652b211366449195c777
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6182e7738253ce1f482de27b0de616c0c20f0885dfcff0c7f2eb9d008d54bc8d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1caa7c26:start=1571430443955999599,finish=1571430795530620066,duration=351574620467,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:02455d0c[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599803630/log.txt)