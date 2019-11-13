## Status: Passing 
Build: [1085](https://travis-ci.org/precice/systemtests/builds/611163313) 

Job: [1085.19](https://travis-ci.org/precice/systemtests/jobs/611163332) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                    [0m[91m 17% [0m[91m|*****                           | 4551k  0:00:41 ETA
[0m[91m-                     19% |******                          | 5108k  0:00:40 ETA
[0m[91m-                     21% |*******                         | 5617k  0:00:39 ETA
[0m[91m-                     24% |*******                         | 6183k  0:00:37 ETA
[0m[91m-                     25% |********                        | 6515k  0:00:38 ETA
[0m[91m-                    [0m[91m 25% |********                        | 6656k  0:00:39 ETA
[0m[91m-                     27% |********                        | 7038k  0:00:39 ETA
[0m[91m-                     29% |*********                       | 7554k  0:00:38 ETA
[0m[91m-                    [0m[91m 31% |**********                      | 8047k  0:00:37 ETA
[0m[91m-                     33% |**********                      | 8624k  0:00:35 ETA
[0m[91m-                     35% |***********                     | 9184k  0:00:34 ETA
[0m[91m-                     37% |************                    | 9695k  0:00:32 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:29 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:18 ETA
[0m[91m-                    [0m[91m 67% |*********************           | 16.8M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     78% |************************        | 19.5M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M[0m[91m  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA[0m[91m
[0m[91m-                     95% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 883977268130
Removing intermediate container 4529cebaa677
Step 10/13 : WORKDIR /
 ---> 58a9865b400d
Removing intermediate container 8b1409b5edfc
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in ca195ae065e3
 ---> f644acccedbe
Removing intermediate container ca195ae065e3
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 6f3641df2679
 ---> 6a62597b1d3c
Removing intermediate container 6f3641df2679
Step 13/13 : USER [secure]
 ---> Running in aa4048f5fa13
 ---> 288353f80071
Removing intermediate container aa4048f5fa13
Successfully built 288353f80071
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:eaa389694a370d827f8d13708456ce515f27efde4eb0b77abb736faddffc304d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6d5fdaca8a951aa66a57d9809b26a3bcd4fd62ca8b33754144f0d1f63be1f242
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
travis_time:end:00a61940:start=1573613461243832885,finish=1573613817720078021,duration=356476245136,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Knd:0978068c:start=1573613822600475119,finish=1573613824392484443,duration=1792009324,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:19a2a04e[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/611163332/log.txt)