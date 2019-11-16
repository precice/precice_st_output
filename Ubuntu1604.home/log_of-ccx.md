## Status: Passing 
Build: [1099](https://travis-ci.org/precice/systemtests/builds/612668494) 

Job: [1099.19](https://travis-ci.org/precice/systemtests/jobs/612668513) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     14% |****                            | 3632k  0:00:48 ETA
[0m[91m-                     16% |*****                           | 4192k  0:00:46 ETA
[0m[91m-                     18% |*****                           | 4741k  0:00:44 ETA
[0m[91m-                     20% |******                          | 5273k  0:00:42 ETA
[0m[91m-                     22% |*******                         | 5835k  0:00:40 ETA
[0m[91m-                     24% |*******                         | 6259k  0:00:40 ETA
[0m[91m-                     24% |*******                         | 6398k  0:00:42 ETA
[0m[91m-                     26% |********                        | 6718k  0:00:42 ETA
[0m[91m-                     27% |********                        | 7161k  0:00:41 ETA
[0m[91m-                     30% |*********                       | [0m[91m7739k  0:00:39 ETA
[0m[91m-                     32% |**********                      | 8241k  0:00:37 ETA
[0m[91m-                    [0m[91m 34% |**********                      | 8804k  0:00:36 ETA
[0m[91m-                     36% |***********                     | 9374k  0:00:34 ETA
[0m[91m-                     38% |************                    | [0m[91m9942k  0:00:33 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:32 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:30 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:22 ETA[0m[91m
[0m[91m-                     57% |******************              | 14.5M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:20 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                    [0m[91m 85% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
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
 ---> e9baea1beb9b
Removing intermediate container ea7d55a841ef
Step 10/13 : WORKDIR /
 ---> 067c8d5ef0cb
Removing intermediate container 9b744e253c21
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in b123d0a57de5
 ---> cea73166a649
Removing intermediate container b123d0a57de5
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 99ea49cabc26
 ---> 5b613e2a395c
Removing intermediate container 99ea49cabc26
Step 13/13 : USER [secure]
 ---> Running in 4516a52c0266
 ---> d95531ff19fe
Removing intermediate container 4516a52c0266
Successfully built d95531ff19fe
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0d2215f836abbd7f38af6d037a5900a7c2f12c29425b5756f3eaeb2b1d5cdf99
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:d9b5ded71ccd60f87472e38bc5b287946a37f29faea841f6a0145adfd107100a
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1bdebeec:start=1573872537144657507,finish=1573872893054656190,duration=355909998683,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04f11e30[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl

```
[
Full job log](https://api.travis-ci.org/v3/job/612668513/log.txt)