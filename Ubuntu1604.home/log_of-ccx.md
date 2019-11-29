## Status: Passing 
Build: [1219](https://travis-ci.org/precice/systemtests/builds/618379002) 

Job: [1219.15](https://travis-ci.org/precice/systemtests/jobs/618379017) 

Triggered by: [push](https://github.com/precice/systemtests/compare/7189d2841f25...dca772ad009c) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     26% |********                        | 6791k  0:00:36 ETA
[0m[91m-                     28% |*********                       | 7371k  0:00:34 ETA
[0m[91m-                     30% |*********                       | 7902k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8436k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 9004k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9578k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                    [0m[91m 41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:27 ETA
[0m[91m-                    [0m[91m 45% |**************                  | 11.5M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                    [0m[91m 60% [0m[91m|*******************             | [0m[91m15.0M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:18 ETA[0m[91m
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% [0m[91m|****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
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
 ---> 4d764c8f6ea6
Removing intermediate container 81771dd79129
Step 11/14 : WORKDIR /
 ---> 3c80044280b3
Removing intermediate container 669e44142b88
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7991c6e82f65
 ---> 2cda98081897
Removing intermediate container 7991c6e82f65
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in afc21bedf3d9
 ---> db8c71732d9a
Removing intermediate container afc21bedf3d9
Step 14/14 : USER [secure]
 ---> Running in cf64d5732009
 ---> 6512f4903b2e
Removing intermediate container cf64d5732009
Successfully built 6512f4903b2e
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:00845e1ffe0b07f596edaae901de7b42ce3f89a08f557de115aa9e47ae051d3f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:21848c502571634f6b20f866324b3462d276726e4722cf39ae98ffce207baab0
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:04a2126a:start=1575008879758801210,finish=1575009287882701819,duration=408123900609,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:05e144bf[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:05e144bf:start=1575009293208997418,finish=1575009295227018897,duration=2018021479,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:000236ab[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/618379017/log.txt)