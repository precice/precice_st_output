## Status: Passing 
Build: [1064](https://travis-ci.org/precice/systemtests/builds/609194596) 

Job: [1064.15](https://travis-ci.org/precice/systemtests/jobs/609194611) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e3f7960c948e...be03fa4f4575) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     48% |***************                 | 12.0M  0:00:32 ETA
[0m[91m-                     50% [0m[91m|****************                | 12.5M  0:00:30 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:28 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:27 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:26 ETA
[0m[91m-                     58% [0m[91m|******************              | 14.7M  0:00:24 ETA
[0m[91m-                     61% |*******************             | 15.2M  0:00:22 ETA
[0m[91m-                     63% |********************            | 15.7M  0:00:21 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:20 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:18 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:17 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:16 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:14 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:13 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:12 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:11 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     90% |*****************************   | 22.6M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% [0m[91m|******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
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
 ---> 054159260250
Removing intermediate container dc47662644be
Step 10/13 : WORKDIR /
 ---> 8496f1025ece
Removing intermediate container be7255ea004e
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 9ab04b8ea789
 ---> 1ab7a70b5ef4
Removing intermediate container 9ab04b8ea789
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b6919897159f
 ---> e331656905b0
Removing intermediate container b6919897159f
Step 13/13 : USER [secure]
 ---> Running in ffbe57c359d2
 ---> d7922be138ee
Removing intermediate container ffbe57c359d2
Successfully built d7922be138ee
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e6cca2c606740a71adfe247662765329b4e2fa8282df5c61b4295aa4a293bc1b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:33fa9bc4762cebcd6e86234e6ccdf9f4cc2817ea949f83fc6934b3aab9d78d40
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
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
travis_time:end:19b3dcc9:start=1573218281178386800,finish=1573218640747353686,duration=359568966886,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2b931836[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2b931836:start=1573218645467657535,finish=1573218647190166892,duration=1722509357,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:14a377ec[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/609194611/log.txt)