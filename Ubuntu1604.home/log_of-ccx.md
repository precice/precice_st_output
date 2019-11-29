## Status: Passing 
Build: [1211](https://travis-ci.org/precice/systemtests/builds/618376977) 

Job: [1211.15](https://travis-ci.org/precice/systemtests/jobs/618376998) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f1e6a1b68d13...e4ce4c7c44a4) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     80% |*************************       | 20.0M  0:00:19 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:19 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:19 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:19 ETA
[0m[91m-                     81% |*************************       | 20.2M  0:00:19 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:18 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:18 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:17 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:17 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:16 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:15 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:15 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:14 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:14 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:13 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:13 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:12 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:11 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:09 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:09 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:08 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:06 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:06 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:05 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:03 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:01 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> 9a20b1700530
Removing intermediate container 8b7d56dbeac6
Step 11/14 : WORKDIR /
 ---> 0b64568019f0
Removing intermediate container e6c39d0d256d
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 858a54e642ed
 ---> 776d00980dcc
Removing intermediate container 858a54e642ed
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ade12c261875
 ---> 86a699f02e71
Removing intermediate container ade12c261875
Step 14/14 : USER [secure]
 ---> Running in 424cdc79b119
 ---> 4c7e1c547bd8
Removing intermediate container 424cdc79b119
Successfully built 4c7e1c547bd8
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:621857c5b2f5d84275e432a812ae4700a596751767623e580112a305388d6eaa
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:efbb1212cd625cf951d8671884048990e484873996abf99eeee2cb420afc91cd
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:013002fc:start=1574991415184824365,finish=1574991818067961037,duration=402883136672,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:18d52220[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:18d52220:start=1574991822625823655,finish=1574991824184661867,duration=1558838212,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:063ed7f4[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618376998/log.txt)