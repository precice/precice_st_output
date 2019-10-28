## Status: Passing 
Build: [1044](https://travis-ci.org/precice/systemtests/builds/603937404) 

Job: [1044.15](https://travis-ci.org/precice/systemtests/jobs/603937420) 

Triggered by: [push](https://github.com/precice/systemtests/compare/81ea09464169...4d5c1a1b3cfb) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     54% |*****************               | 13.6M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.2M  0:00:21 ETA
[0m[91m-                     63% |********************            | 15.7M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:14 ETA[0m[91m
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% [0m[91m|*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
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
 ---> 5755b3083df3
Removing intermediate container 9084f8e6f090
Step 10/13 : WORKDIR /
 ---> 5ca40f438cee
Removing intermediate container 6e9afdcbc654
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 83e4a1894810
 ---> 5e4f4e8e1d4a
Removing intermediate container 83e4a1894810
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9933fcc1f41b
 ---> 51ffacf93003
Removing intermediate container 9933fcc1f41b
Step 13/13 : USER [secure]
 ---> Running in 2b736f4d2a57
 ---> 613b1601d829
Removing intermediate container 2b736f4d2a57
Successfully built 613b1601d829
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:fbf7e03e88b589e5eecfdb836fb724bfb62537ee7ba51b3a30ccd8a75852d23f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:1d91c2519eb907bc34323f65542ace4ef96c4df6e00e7df1a80b399fb9922048
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:30797454:start=1572275867617929772,finish=1572276221411889950,duration=353793960178,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0055b3d8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0055b3d8:start=1572276225941189669,finish=1572276227563848103,duration=1622658434,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0fe4f3c6[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/603937420/log.txt)