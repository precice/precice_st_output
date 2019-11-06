## Status: Passing 
Build: [1058](https://travis-ci.org/precice/systemtests/builds/607962841) 

Job: [1058.19](https://travis-ci.org/precice/systemtests/jobs/607962862) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     19% |******                          | 5068k  0:00:48 ETA
[0m[91m-                     21% |*******                         | 5624k  0:00:46 ETA
[0m[91m-                     23% |*******                         | 6130k  0:00:44 ETA
[0m[91m-                     24% |*******                         | 6335k  0:00:45 ETA
[0m[91m-                     26% [0m[91m|********                        | 6677k  0:00:45 ETA
[0m[91m-                     27% |********                        | 7156k  0:00:43 ETA
[0m[91m-                     29% |*********                       | 7665k  0:00:42 ETA
[0m[91m-                     32% |**********                      | 8218k  0:00:40 ETA
[0m[91m-                     34% |**********                      | 8796k  0:00:38 ETA
[0m[91m-                     36% [0m[91m|***********                     | 9353k  0:00:36 ETA
[0m[91m-                     38% |************                    | 9929k  0:00:34 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:33 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:31 ETA
[0m[91m-                     45% |**************                  | 11.2M  0:00:30 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:26 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:25 ETA
[0m[91m-                     55% |*****************               | 14.0M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:22 ETA[0m[91m
[0m[91m-                     60% |*******************             | 15.0M  0:00:21 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:15 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                    [0m[91m 75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                    [0m[91m 78% |*************************       | 19.5M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                    [0m[91m 88% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.2M  0:00:01 ETA
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
 ---> 4c7024daa870
Removing intermediate container fb2890e8a396
Step 10/13 : WORKDIR /
 ---> b0f927c41747
Removing intermediate container 9ccb6ab7b582
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in bc432fbc2b6d
 ---> 7f84eb8eb96f
Removing intermediate container bc432fbc2b6d
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1f91aa9ac8c4
 ---> 0d2c91d106a1
Removing intermediate container 1f91aa9ac8c4
Step 13/13 : USER [secure]
 ---> Running in 620e4a1af264
 ---> 411563c9f796
Removing intermediate container 620e4a1af264
Successfully built 411563c9f796
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1f11411670b7e8e03ddcfb87356be9d1396f52a11746c00e8586258ce97e581e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:96a2c55bcb7826f63e5afd772789b10c02b7cad4256ef6882852a866375f87ef
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:35578b08:start=1573008730794940578,finish=1573009144883163892,duration=414088223314,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:07a3067c[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/607962862/log.txt)