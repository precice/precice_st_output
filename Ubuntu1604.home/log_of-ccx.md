## Status: Passing 
Build: [1023](https://travis-ci.org/precice/systemtests/builds/602890333) 

Job: [1023.15](https://travis-ci.org/precice/systemtests/jobs/602890348) 

Triggered by: [push](https://github.com/precice/systemtests/compare/14ba7f611330...9921a3e9e3f7) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     19% |******                          | 5076k  0:00:40 ETA
[0m[91m-                     22% |*******                         | 5653k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6202k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6716k  0:00:36 ETA
[0m[91m-                     28% |*********                       | 7280k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7840k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8398k  0:00:32 ETA
[0m[91m-                     34% |***********                     | 8929k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9488k  0:00:30 ETA
[0m[91m-                     38% |************                    | 9950k  0:00:29 ETA
[0m[91m-                     38% |************                    | 9950k  0:00:31 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:32 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:33 ETA[0m[91m
[0m[91m-                     42% |*************                   | 10.5M  0:00:31 ETA
[0m[91m-                     43% |**************                  | 11.0M  0:00:30 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:29 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:27 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:25 ETA
[0m[91m-                     54% [0m[91m|*****************               | 13.7M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.2M  0:00:22 ETA
[0m[91m-                     59% |******************              | 14.7M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:20 ETA[0m[91m
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                    [0m[91m 65% |********************            | 16.3M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M[0m[91m  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA
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
 ---> 8a1a458bc3a6
Removing intermediate container 528f8a5b44bd
Step 10/13 : WORKDIR /
 ---> 842274fde428
Removing intermediate container f298e42b722b
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e5a6d754bd88
 ---> 0b727edc273a
Removing intermediate container e5a6d754bd88
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1d1b1dce02d4
 ---> 296781bbd3a0
Removing intermediate container 1d1b1dce02d4
Step 13/13 : USER [secure]
 ---> Running in f58066791e41
 ---> 077fc6d263a6
Removing intermediate container f58066791e41
Successfully built 077fc6d263a6
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d1528af363df954e5a3be334a2d22d5061e1360a624636367fe2b227c6d1addd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:9dc5aa22cefe6b088e81e26c17c7597af611d0bc49e3cceab954e9cf63095372
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:14fc6198:start=1572021738636914543,finish=1572022088951941136,duration=350315026593,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:06b96880[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602890348/log.txt)