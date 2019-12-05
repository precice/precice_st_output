## Status: Passing 
Build: [1268](https://travis-ci.org/precice/systemtests/builds/621181807) 

Job: [1268.15](https://travis-ci.org/precice/systemtests/jobs/621181824) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ff51dfcb2467...d102fedd8227) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     51% |****************                | 12.8M  0:00:26 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:25 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:23 ETA[0m[91m
[0m[91m-                     57% |******************              | 14.4M  0:00:22 ETA
[0m[91m-                     59% |*******************             | 14.9M[0m[91m  0:00:21 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:20 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:14 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:04 ETA[0m[91m
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
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
 ---> c5c9b26ce4db
Removing intermediate container 4cfa4ec9d064
Step 11/14 : WORKDIR /
 ---> 2328875837ee
Removing intermediate container a25799e109d7
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d43492b10df4
 ---> 0dd5bbc5764b
Removing intermediate container d43492b10df4
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 47f61870a0f3
 ---> d07b6b221250
Removing intermediate container 47f61870a0f3
Step 14/14 : USER [secure]
 ---> Running in 26816b3fb638
 ---> 7886fdcda5ac
Removing intermediate container 26816b3fb638
Successfully built 7886fdcda5ac
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:509928ef47f3e2b800f11b0e404af7166a82ae4a4bbbda84fd9701c8da64dadb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6637f7ee045d95758de4b8e56b8303623ff0642d9bc57c904e098a34fb548db1
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
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
travis_time:end:1e625584:start=1575565057666783239,finish=1575565409715112834,duration=352048329595,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:15ef1a38[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:15ef1a38:start=1575565414279716576,finish=1575565415910642980,duration=1630926404,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:28a4a290[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/621181824/log.txt)