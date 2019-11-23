## Status: Passing 
Build: [1131](https://travis-ci.org/precice/systemtests/builds/615847024) 

Job: [1131.19](https://travis-ci.org/precice/systemtests/jobs/615847043) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     29% |*********                       | 7484k  0:00:43 ETA
[0m[91m-                    [0m[91m 31% |**********                      | 8062k  0:00:41 ETA
[0m[91m-                     33% |**********                      | [0m[91m8625k  0:00:39 ETA
[0m[91m-                    [0m[91m 35% [0m[91m|***********                     | 9131k  0:00:37 ETA
[0m[91m-                     37% |************                    | [0m[91m9687k  0:00:36 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:34 ETA
[0m[91m-                     42% |*************                   | 10.5M[0m[91m  0:00:32 ETA
[0m[91m-                    [0m[91m 44% |**************                  | 11.1M  0:00:31 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:30 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:28 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:27 ETA
[0m[91m-                    [0m[91m 53% |****************                | 13.2M  0:00:25 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:24 ETA
[0m[91m-                     57% [0m[91m|******************              | 14.3M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:22 ETA
[0m[91m-                    [0m[91m 59% |*******************             | 14.8M  0:00:22 ETA[0m[91m
[0m[91m-                     61% [0m[91m|*******************             | 15.2M  0:00:21 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:20 ETA
[0m[91m-                     65% |********************            | [0m[91m16.2M[0m[91m  0:00:19 ETA
[0m[91m-                    [0m[91m 67% |*********************           | 16.8M  0:00:17 ETA
[0m[91m-                    [0m[91m 69% [0m[91m|**********************          | 17.4M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:14 ETA
[0m[91m-                    [0m[91m 75% [0m[91m|************************        | 18.9M  0:00:13 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                    [0m[91m 82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:07 ETA[0m[91m
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                    [0m[91m 90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | [0m[91m23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
-                    [0m[91m100% |********************************| 25.0M[0m[91m  0:00:00 ETA[0m[91m
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
 ---> 484f7adf3b95
Removing intermediate container 77915465b23a
Step 10/13 : WORKDIR /
 ---> dab6326ef4d6
Removing intermediate container 98b0e13c0fe9
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 800a491e1bfa
 ---> d7632a200d1e
Removing intermediate container 800a491e1bfa
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8f7daea12ba6
 ---> c9a7dd9b676a
Removing intermediate container 8f7daea12ba6
Step 13/13 : USER [secure]
 ---> Running in 90f4568175c6
 ---> 56ae7aac0aa7
Removing intermediate container 90f4568175c6
Successfully built 56ae7aac0aa7
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:434364091ca51fc8b71e13677c447ae4b75692f28a8629fbc2e4cdaa18040de8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:fed39dd6704645fb9e4cb5f14d0b9c20dab9ae49506883769ed1cef2d90cbfeb
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
travis_time:end:007ebad9:start=1574477592609975871,finish=1574477942975477789,duration=350365501918,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:025997a6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:025997a6:start=1574477947475532566,finish=1574477949098417374,duration=1622884808,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:11627c10[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/615847043/log.txt)