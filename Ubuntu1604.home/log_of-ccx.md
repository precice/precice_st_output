## Status: Passing 
Build: [1177](https://travis-ci.org/precice/systemtests/builds/618293063) 

Job: [1177.15](https://travis-ci.org/precice/systemtests/jobs/618293080) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f42978edba8f...f6ac64c472af) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     45% |**************                  | 11.4M[0m[91m  0:00:33 ETA
[0m[91m-                     47% |***************                 | 11.9M[0m[91m  0:00:31 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:30 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:28 ETA
[0m[91m-                     53% |*****************               | 13.5M[0m[91m  0:00:27 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:25 ETA
[0m[91m-                    [0m[91m 58% |******************              | 14.5M  0:00:24 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:22 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:21 ETA
[0m[91m-                    [0m[91m 64% |********************            | 16.1M  0:00:20 ETA
[0m[91m-                    [0m[91m 66% |*********************           | 16.7M  0:00:18 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:17 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:16 ETA
[0m[91m-                    [0m[91m 73% |***********************         | 18.3M  0:00:15 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:13 ETA
[0m[91m-                    [0m[91m 77% [0m[91m|************************        | 19.3M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% [0m[91m|***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                    [0m[91m 98% |******************************* | 24.6M  0:00:00 ETA
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
 ---> f67060dfc199
Removing intermediate container 10a19ca249d1
Step 10/13 : WORKDIR /
 ---> 6b4fc64a25dd
Removing intermediate container b5891116a548
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7bce67cf84b5
 ---> a3c8cc6b8196
Removing intermediate container 7bce67cf84b5
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 33abaab8ce13
 ---> c121e32560ef
Removing intermediate container 33abaab8ce13
Step 13/13 : USER [secure]
 ---> Running in ac523d7a4413
 ---> 5cc5e9c9f0f0
Removing intermediate container ac523d7a4413
Successfully built 5cc5e9c9f0f0
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:3320cb415223ff3ee8fefb382544a974c922bd4a4bb2ef99bca16abea6b6983e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:8ccdf5bb06cfb219e490784aacab984a83dd722cde9136c6bdc2a651e1876924
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:04dccf16:start=1574965887017614614,finish=1574966239570621901,duration=352553007287,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2b9a1948[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2b9a1948:start=1574966244385523740,finish=1574966246192441471,duration=1806917731,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:01ff5abf[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618293080/log.txt)