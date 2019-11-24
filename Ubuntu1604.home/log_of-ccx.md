## Status: Passing 
Build: [1132](https://travis-ci.org/precice/systemtests/builds/616148321) 

Job: [1132.19](https://travis-ci.org/precice/systemtests/jobs/616148342) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.0M[0m[91m  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.5M[0m[91m  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:17 ETA
[0m[91m-                    [0m[91m 66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.7M[0m[91m  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                    [0m[91m 83% |**************************      | 20.8M  0:00:08 ETA[0m[91m
[0m[91m-                    [0m[91m 85% [0m[91m|***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% [0m[91m|*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.0M[0m[91m  0:00:01 ETA
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
 ---> 95f373fee57e
Removing intermediate container bf104afc7d9c
Step 10/13 : WORKDIR /
 ---> 4efd1ab76b5e
Removing intermediate container 0dce12747eec
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in c52e3b7525ca
 ---> 4896636b776b
Removing intermediate container c52e3b7525ca
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 176b75e80da9
 ---> 0a046d117efa
Removing intermediate container 176b75e80da9
Step 13/13 : USER [secure]
 ---> Running in c07912c64ee1
 ---> 588e9d111729
Removing intermediate container c07912c64ee1
Successfully built 588e9d111729
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:037a6917e7d1072f5578a2bdad297d1509ff41df3d51aee9c218c5281d7411ed
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:7927be5dfc7e68bb915ac8ea5e85837aa1ea893ecb059927e42ca53cdfe46d33
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
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
travis_time:end:022b8b7a:start=1574563942952601803,finish=1574564288686822990,duration=345734221187,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:053838a8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:053838a8:start=1574564293335250899,finish=1574564295117776354,duration=1782525455,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2bc960d7[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/616148342/log.txt)