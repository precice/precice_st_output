## Status: Passing 
Build: [1054](https://travis-ci.org/precice/systemtests/builds/606282132) 

Job: [1054.19](https://travis-ci.org/precice/systemtests/jobs/606282157) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     10% |***                             | 2688k  0:00:42 ETA
[0m[91m-                     12% |****                            | 3254k  0:00:41 ETA
[0m[91m-                     14% |****                            | 3822k  0:00:39 ETA
[0m[91m-                     16% [0m[91m|*****                           | 4326k  0:00:39 ETA
[0m[91m-                     19% |******                          | 4901k  0:00:38 ETA
[0m[91m-                     21% |******                          | 5470k  0:00:36 ETA
[0m[91m-                     23% |*******                         | 6027k  0:00:35 ETA
[0m[91m-                     25% |********                        | 6597k  0:00:34 ETA
[0m[91m-                     27% [0m[91m|********                        | 7102k  0:00:33 ETA[0m[91m
[0m[91m-                     29% |*********                       | 7667k  0:00:32 ETA
[0m[91m-                     32% |**********                      | 8238k  0:00:31 ETA
[0m[91m-                     34% |**********                      | 8806k  0:00:30 ETA
[0m[91m-                     36% |***********                     | 9378k  0:00:29 ETA
[0m[91m-                     38% |************                    | 9871k  0:00:28 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:27 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:25 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:24 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:23 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:22 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:21 ETA
[0m[91m-                     55% |*****************               | 14.0M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% [0m[91m|***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA[0m[91m
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA[0m[91m
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
 ---> fb75ff684453
Removing intermediate container 39d23a00f1e0
Step 10/13 : WORKDIR /
 ---> 215ccc3c701e
Removing intermediate container 413841e3c26b
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d8505f50b579
 ---> af1bed19e0e2
Removing intermediate container d8505f50b579
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in cd2e9675abf1
 ---> 2e276c96abf7
Removing intermediate container cd2e9675abf1
Step 13/13 : USER [secure]
 ---> Running in 1286600062a0
 ---> f6010fef5b5e
Removing intermediate container 1286600062a0
Successfully built f6010fef5b5e
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7b35f009c5169ca242753a754e0675197b77bde0b0ee3330c95449a33e668f39
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:35243c562b58ff22497bd23b9ca1f14d538c7a84396d7f226f791fcbe7a66d81
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
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
travis_time:end:055eacb4:start=1572662619936728048,finish=1572662963243101397,duration=343306373349,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0ce49ffc[0K$ python push.py -s -t of-ccx

```
[
Full job log](https://api.travis-ci.org/v3/job/606282157/log.txt)