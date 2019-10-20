## Status: Passing 
Build: [990](https://travis-ci.org/precice/systemtests/builds/600304885) 

Job: [990.15](https://travis-ci.org/precice/systemtests/jobs/600304900) 

Triggered by: [push](https://github.com/precice/systemtests/compare/26213e77ad5d...a84a139c2665) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     15% |*****                           | 4010k  0:00:53 ETA
[0m[91m-                     17% |*****                           | 4504k  0:00:51 ETA
[0m[91m-                    [0m[91m 19% |******                          | 5074k  0:00:48 ETA
[0m[91m-                     21% |******                          | 5581k  0:00:46 ETA
[0m[91m-                     23% |*******                         | 6086k  0:00:44 ETA
[0m[91m-                     25% |********                        | 6660k  0:00:42 ETA
[0m[91m-                     27% |********                        | 7160k  0:00:41 ETA
[0m[91m-                     29% |*********                       | 7672k  0:00:39 ETA
[0m[91m-                     32% |**********                      | 8237k  0:00:38 ETA
[0m[91m-                    [0m[91m 34% |**********                      | 8735k  0:00:36 ETA
[0m[91m-                     36% |***********                     | 9307k  0:00:35 ETA
[0m[91m-                     38% |************                    | 9808k  0:00:33 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:32 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:31 ETA[0m[91m
[0m[91m-                     44% |**************                  | 11.1M  0:00:30 ETA
[0m[91m-                    [0m[91m 46% |**************                  | 11.6M  0:00:28 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:27 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:20 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                    [0m[91m 91% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 125fffd99e40
Removing intermediate container 6e7b83f46681
Step 10/13 : WORKDIR /
 ---> ae7cda9298bd
Removing intermediate container 01ceddc67385
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 4f5cfbc954ee
 ---> 6f1a5c8e427e
Removing intermediate container 4f5cfbc954ee
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in f9d8838e355c
 ---> 89d843248826
Removing intermediate container f9d8838e355c
Step 13/13 : USER [secure]
 ---> Running in 3590dd151b5f
 ---> a1b34da6e9e7
Removing intermediate container 3590dd151b5f
Successfully built a1b34da6e9e7
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9a6ec2cc70ceed2d43eb990b726e61e5e7a3b457101d40bf784f81c204130d95
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:aef390d122189670da8733e21efe952a14e5013b791248306db94c4bb1ffe20c
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1573d6ca:start=1571576283070883958,finish=1571576696589195136,duration=413518311178,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:02412cbe[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/600304900/log.txt)