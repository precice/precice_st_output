## Status: Passing 
Build: [1130](https://travis-ci.org/precice/systemtests/builds/615348483) 

Job: [1130.19](https://travis-ci.org/precice/systemtests/jobs/615348502) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     47% |***************                 | 11.9M  0:00:25 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:18 ETA
[0m[91m-                     64% [0m[91m|********************            | 16.1M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                    [0m[91m 68% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:11 ETA
[0m[91m-                     79% |*************************       | [0m[91m19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA[0m[91m
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% [0m[91m|******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> f90a4db88c5d
Removing intermediate container 831ddb994cbf
Step 10/13 : WORKDIR /
 ---> e97c8dd48cc1
Removing intermediate container 533dda368af1
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 2efd566b2ef6
 ---> cd8451fb6e31
Removing intermediate container 2efd566b2ef6
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in f24d367be8bc
 ---> 798d8445b115
Removing intermediate container f24d367be8bc
Step 13/13 : USER [secure]
 ---> Running in f44e6d50d951
 ---> 9b84b2451d80
Removing intermediate container f44e6d50d951
Successfully built 9b84b2451d80
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:bfa8012e320fec45d2ce7b5aea06f822117b8991efe51f62b48bf1a68007f789
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:c4d25dea016758e78dc973fe9e77a686f36a9122c375aba31724c5a1b2f68426
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0a68eb0c:start=1574391151926266405,finish=1574391498247821642,duration=346321555237,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01b6e84a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01b6e84a:start=1574391503600047024,finish=1574391505293531795,duration=1693484771,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:09f56628[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/615348502/log.txt)