## Status: Passing 
Build: [1053](https://travis-ci.org/precice/systemtests/builds/606180964) 

Job: [1053.15](https://travis-ci.org/precice/systemtests/jobs/606180979) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4d5c1a1b3cfb...f02cef114a79) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA[0m[91m
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:15 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:14 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:13 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:12 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:11 ETA
[0m[91m-                     81% [0m[91m|*************************       | 20.3M  0:00:11 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:09 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:08 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:07 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 616f9b96e91b
Removing intermediate container d927a27536f3
Step 10/13 : WORKDIR /
 ---> 7559aefd6580
Removing intermediate container 6b5853cfba2c
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in fa9b7acf0091
 ---> 96e6b5471851
Removing intermediate container fa9b7acf0091
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e9d015b2ca52
 ---> 651594d6a7b3
Removing intermediate container e9d015b2ca52
Step 13/13 : USER [secure]
 ---> Running in 5cb31ebe98a7
 ---> ca8cd680b997
Removing intermediate container 5cb31ebe98a7
Successfully built ca8cd680b997
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:914638c131614e647c0780f831aae7d3efcff62515e7d50251f431eac2f2ec92
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0afac72e64c0f7687f1d81215b477395fe403f76e3be43129de86004b60a57e2
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
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1b6857cb:start=1572641880092883001,finish=1572642298951672346,duration=418858789345,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:03f23e55[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:03f23e55:start=1572642304175344410,finish=1572642305964498400,duration=1789153990,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0a95b1e2[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/606180979/log.txt)