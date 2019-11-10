## Status: Passing 
Build: [1068](https://travis-ci.org/precice/systemtests/builds/609999431) 

Job: [1068.15](https://travis-ci.org/precice/systemtests/jobs/609999446) 

Triggered by: [push](https://github.com/precice/systemtests/commit/5cfc071ae529) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     10% |***                             | 2692k  0:00:59 ETA
[0m[91m-                     12% |****                            | 3252k  0:00:55 ETA
[0m[91m-                     14% |****                            | 3756k  0:00:52 ETA
[0m[91m-                     16% |*****                           | 4310k  0:00:49 ETA
[0m[91m-                     19% |******                          | 4878k  0:00:46 ETA
[0m[91m-                     21% |******                          | 5444k  0:00:44 ETA
[0m[91m-                     23% |*******                         | 5940k  0:00:43 ETA
[0m[91m-                     25% |********                        | 6516k  0:00:41 ETA
[0m[91m-                     27% |********                        | 7074k  0:00:39 ETA
[0m[91m-                     29% |*********                       | 7654k  0:00:37 ETA
[0m[91m-                     31% |**********                      | 8154k  0:00:36 ETA
[0m[91m-                     34% |**********                      | 8717k  0:00:34 ETA
[0m[91m-                     36% |***********                     | 9279k  0:00:33 ETA
[0m[91m-                     38% |************                    | 9842k  0:00:32 ETA
[0m[91m-                    [0m[91m 40% [0m[91m|************                    | 10.1M  0:00:30 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:28 ETA
[0m[91m-                    [0m[91m 47% |***************                 | 11.7M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:25 ETA
[0m[91m-                     51% [0m[91m|****************                | 12.8M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:23 ETA[0m[91m
[0m[91m-                     55% |*****************               | 13.9M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA[0m[91m
[0m[91m-                     66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M[0m[91m  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
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
 ---> 2e3908fdad99
Removing intermediate container bfa9ff932ef8
Step 10/13 : WORKDIR /
 ---> c25df406780d
Removing intermediate container f0e64b68cfb3
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d2cff101ca29
 ---> 5f4fb1a50434
Removing intermediate container d2cff101ca29
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in a79ac778589a
 ---> b31572dad6ce
Removing intermediate container a79ac778589a
Step 13/13 : USER [secure]
 ---> Running in ba5bfbfb80a6
 ---> 0b60b3e3fd25
Removing intermediate container ba5bfbfb80a6
Successfully built 0b60b3e3fd25
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:44c638fda07529b4fa826c3e2802921e4745184ba890cdda8eff73606f82ea90
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:7f338c300576d32654a57b0af045919cf2238c8ee743b6ff562cadd232e770e5
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
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0c44a944:start=1573408343355343402,finish=1573408694691718460,duration=351336375058,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:023dc608[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl

```
[
Full job log](https://api.travis-ci.org/v3/job/609999446/log.txt)