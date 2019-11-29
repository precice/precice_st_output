## Status: Passing 
Build: [1215](https://travis-ci.org/precice/systemtests/builds/618378110) 

Job: [1215.15](https://travis-ci.org/precice/systemtests/jobs/618378125) 

Triggered by: [push](https://github.com/precice/systemtests/compare/95fbdb5c2d24...03b1aca5c88d) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     28% |*********                       | 7341k  0:00:34 ETA
[0m[91m-                     30% |*********                       | 7886k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8445k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 9007k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9552k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:25 ETA
[0m[91m-                     47% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:22 ETA
[0m[91m-                     52% [0m[91m|****************                | 13.2M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:21 ETA
[0m[91m-                    [0m[91m 58% [0m[91m|******************              | 14.6M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                    [0m[91m 62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:17 ETA
[0m[91m-                    [0m[91m 66% [0m[91m|*********************           | 16.7M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA[0m[91m
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
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
 ---> 9ac260861577
Removing intermediate container c1c9542bec5b
Step 11/14 : WORKDIR /
 ---> 774aaef4a63e
Removing intermediate container 15ace9a97ab7
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in a97c6ccd25b5
 ---> 551ff1a9305c
Removing intermediate container a97c6ccd25b5
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7593efa3c43c
 ---> 0653d33056fd
Removing intermediate container 7593efa3c43c
Step 14/14 : USER [secure]
 ---> Running in 6e78761d58df
 ---> fb6b31036388
Removing intermediate container 6e78761d58df
Successfully built fb6b31036388
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e53292d98713aaab24a43c37f3df5ae3008cfab8a4d0c68d0a4db65ec1e3cad7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:f03bc14ebf254a2ca23c889b94de17fddd2c30af520067fb4b39363719505637
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2ac451a7:start=1575001575728165331,finish=1575001932526211671,duration=356798046340,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:26270070[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:26270070:start=1575001937149097520,finish=1575001938820000318,duration=1670902798,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:001741a7[0KCloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618378125/log.txt)