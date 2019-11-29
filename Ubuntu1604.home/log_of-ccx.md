## Status: Passing 
Build: [1221](https://travis-ci.org/precice/systemtests/builds/618379300) 

Job: [1221.15](https://travis-ci.org/precice/systemtests/jobs/618379315) 

Triggered by: [push](https://github.com/precice/systemtests/compare/fbdb0751795a...d440b60eb25a) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     48% |***************                 | 12.0M  0:00:29 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:27 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:26 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:21 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:21 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:19 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:18 ETA
[0m[91m-                     68% |*********************           | 17.2M  0:00:17 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:14 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:12 ETA
[0m[91m-                     79% |*************************       | [0m[91m19.9M  0:00:11 ETA[0m[91m
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                    [0m[91m 86% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************* | 24.2M  0:00:01 ETA
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
 ---> c8f4ef17c94d
Removing intermediate container f2e6560d98e7
Step 11/14 : WORKDIR /
 ---> f61be534a090
Removing intermediate container f189d7abf733
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 5997f770f2c0
 ---> de6d42c33bae
Removing intermediate container 5997f770f2c0
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ffe8206f37d1
 ---> 0977c129e8e5
Removing intermediate container ffe8206f37d1
Step 14/14 : USER [secure]
 ---> Running in be5aa931a246
 ---> 66ef909ff77d
Removing intermediate container be5aa931a246
Successfully built 66ef909ff77d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:b15181e24da083607c140719641672f98f2b9e7337ef397277aef1817fb5600f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:36ce9964f291eccec7d7495e933ebb092bed002f5b47f6204a0a3b41f300ced9
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
travis_time:end:19ea2550:start=1575014560922684778,finish=1575014923778918376,duration=362856233598,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:068485ce[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:068485ce:start=1575014928326664277,finish=1575014929996573867,duration=1669909590,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:04b0e444[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618379315/log.txt)