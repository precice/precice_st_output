## Status: Passing 
Build: [1006](https://travis-ci.org/precice/systemtests/builds/602019179) 

Job: [1006.15](https://travis-ci.org/precice/systemtests/jobs/602019194) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4ea43c307afb...2f3949cca1ae) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     14% |****                            | 3763k  0:00:52 ETA
[0m[91m-                     16% |*****                           | 4333k  0:00:49 ETA
[0m[91m-                     19% |******                          | 4901k  0:00:46 ETA
[0m[91m-                     21% |******                          | 5413k  0:00:44 ETA
[0m[91m-                     23% |*******                         | 5982k  0:00:42 ETA
[0m[91m-                     25% [0m[91m|********                        | 6552k  0:00:40 ETA
[0m[91m-                     27% |********                        | 7112k  0:00:39 ETA
[0m[91m-                     29% |*********                       | 7682k  0:00:37 ETA
[0m[91m-                    [0m[91m 31% [0m[91m|**********                      | 8194k  0:00:36 ETA
[0m[91m-                     34% [0m[91m|**********                      | 8746k  0:00:34 ETA
[0m[91m-                     36% |***********                     | 9314k  0:00:33 ETA[0m[91m
[0m[91m-                     38% |************                    | 9882k  0:00:31 ETA
[0m[91m-                    [0m[91m 40% |*************                   | 10.2M  0:00:30 ETA
[0m[91m-                    [0m[91m 42% |*************                   | 10.7M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:28 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:25 ETA
[0m[91m-                     51% [0m[91m|****************                | 12.9M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.9M[0m[91m  0:00:22 ETA
[0m[91m-                    [0m[91m 57% [0m[91m|******************              | 14.5M  0:00:21 ETA
[0m[91m-                    [0m[91m 58% |******************              | 14.6M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:20 ETA
[0m[91m-                    [0m[91m 61% |*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     63% |********************            | 16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                    [0m[91m 81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                    [0m[91m 83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA[0m[91m
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
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
 ---> 26d9f4ca0ad8
Removing intermediate container 9afffe53b5b2
Step 10/13 : WORKDIR /
 ---> 35cef623c61e
Removing intermediate container 1ea369f8daee
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 33432656eaff
 ---> ef5bcbaf5e8a
Removing intermediate container 33432656eaff
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 43efeb1dfe7e
 ---> 80a9ef22a4cb
Removing intermediate container 43efeb1dfe7e
Step 13/13 : USER [secure]
 ---> Running in efea3ab9810e
 ---> e3e92ecf7db0
Removing intermediate container efea3ab9810e
Successfully built e3e92ecf7db0
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:71e59392c3eda1815295b9b43606e5b8ae997da323ad190311b227bd2bde769e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b3f73dc0fa9a4fa00f021a626671657638f1048b19834dcc5e3a8456ee7dcbc7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:009ad5d7:start=1571867773671919401,finish=1571868132421938376,duration=358750018975,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:039a5b10[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602019194/log.txt)