## Status: Passing 
Build: [1264](https://travis-ci.org/precice/systemtests/builds/621025152) 

Job: [1264.16](https://travis-ci.org/precice/systemtests/jobs/621025168) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4b1d49be8e29...13952c2945a9) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     85% |***************************     | 21.3M  0:00:27 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:26 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:24 ETA
[0m[91m-                     87% |****************************    | 22.0M  0:00:22 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:20 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:18 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:16 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:16 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:15 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:15 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:14 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:13 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:12 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:11 ETA
[0m[91m-                     93% |******************************  | 23.5M  0:00:11 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:10 ETA
[0m[91m-                     95% |******************************  | 23.7M  0:00:09 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:08 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:07 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:07 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:06 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:04 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:02 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> 4ac4fd9388bc
Removing intermediate container 1ecc32658e2e
Step 11/14 : WORKDIR /
 ---> 9fd4f6da5fd6
Removing intermediate container e142ebc93748
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 3ecc066fc6b1
 ---> dc25a72596d1
Removing intermediate container 3ecc066fc6b1
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ee2d7d16342d
 ---> 0bc01ab7587a
Removing intermediate container ee2d7d16342d
Step 14/14 : USER [secure]
 ---> Running in 9c7bc4d4f059
 ---> 8df0df1e4542
Removing intermediate container 9c7bc4d4f059
Successfully built 8df0df1e4542
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:64bb4629f0595f8e57a085825919ea335ffcf293a1cbd4b373ac03ea321a9673
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:94bccbf197944151cf9088a2906872adce0681169d1a6cefbd61b59b84e33d84
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
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
travis_time:end:14759932:start=1575540417765429958,finish=1575540901591853952,duration=483826423994,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04162c5c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04162c5c:start=1575540905539506488,finish=1575540907030920094,duration=1491413606,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1d002654[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/621025168/log.txt)