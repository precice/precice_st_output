## Status: Passing 
Build: [1205](https://travis-ci.org/precice/systemtests/builds/618334138) 

Job: [1205.15](https://travis-ci.org/precice/systemtests/jobs/618334153) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f6ac64c472af...3b2ed1c3a41a) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     32% |**********                      | 8310k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8839k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9404k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9971k  0:00:29 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.7M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 86caf969e82f
Removing intermediate container bb71286af442
Step 11/14 : WORKDIR /
 ---> ab90c91b9c92
Removing intermediate container 5f805d1731e1
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in fd37a23eeedb
 ---> 5322a06c4e0c
Removing intermediate container fd37a23eeedb
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1e701f1fe9fc
 ---> 2de1872e5d52
Removing intermediate container 1e701f1fe9fc
Step 14/14 : USER [secure]
 ---> Running in 4380f46a03fd
 ---> 0ce5641d7b59
Removing intermediate container 4380f46a03fd
Successfully built 0ce5641d7b59
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e64d281cd35453d9fd31b71b7b9bc5d2f481aff68bb487c09f73e28a34da94d1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:99f481053189b36bf738b95c4c9a8a185a160f5007de882ed8f3469596ddb267
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0ced9558:start=1574986890065774911,finish=1574987239020833507,duration=348955058596,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:23226ad0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618334153/log.txt)