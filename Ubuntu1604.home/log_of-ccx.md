## Status: Passing 
Build: [1089](https://travis-ci.org/precice/systemtests/builds/611664101) 

Job: [1089.19](https://travis-ci.org/precice/systemtests/jobs/611664120) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     22% |*******                         | 5664k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6238k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6801k  0:00:35 ETA
[0m[91m-                     28% |*********                       | 7337k  0:00:34 ETA
[0m[91m-                     30% |*********                       | 7909k  0:00:33 ETA
[0m[91m-                    [0m[91m 32% |**********                      | 8448k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 9018k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9559k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:28 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.5M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% [0m[91m|******************************* | 24.9M  0:00:00 ETA
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
 ---> 69f1b33d904c
Removing intermediate container 12fd6cbe42dd
Step 10/13 : WORKDIR /
 ---> 8b8340fbb5c4
Removing intermediate container a3a7edaf9dd4
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 3eaee787ba1e
 ---> 2555b41a2eb6
Removing intermediate container 3eaee787ba1e
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 300e76bff701
 ---> 84bb38c43521
Removing intermediate container 300e76bff701
Step 13/13 : USER [secure]
 ---> Running in 9f5aa976205b
 ---> 02317a484013
Removing intermediate container 9f5aa976205b
Successfully built 02317a484013
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e38a42902a0744dbd62f72b127d54fbfb9a48dd09f601ebc33441d2daef7ed19
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:a68c26f5c60cab67469ba7827a6b2134a8baf0122ffbd76689eb5c132ab988f2
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:02a9d182:start=1573699618475205146,finish=1573699963722471871,duration=345247266725,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:08d5faa9:start=1573699968302207348,finish=1573699969839147655,duration=1536940307,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1d36bd1e[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/611664120/log.txt)