## Status: Passing 
Build: [1045](https://travis-ci.org/precice/systemtests/builds/604222443) 

Job: [1045.19](https://travis-ci.org/precice/systemtests/jobs/604222464) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     10% |***                             | 2815k  0:00:48 ETA
[0m[91m-                     13% |****                            | 3392k  0:00:45 ETA
[0m[91m-                    [0m[91m 15% |****                            | 3950k  0:00:43 ETA
[0m[91m-                     17% |*****                           | 4497k  0:00:42 ETA
[0m[91m-                     19% |******                          | 5036k  0:00:40 ETA
[0m[91m-                     21% [0m[91m|******                          | 5593k  0:00:39 ETA
[0m[91m-                     24% |*******                         | 6165k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6715k  0:00:36 ETA
[0m[91m-                     28% |*********                       | 7229k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7812k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8372k  0:00:32 ETA
[0m[91m-                     34% |***********                     | 8921k  0:00:31 ETA
[0m[91m-                     36% |***********                     | 9446k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | [0m[91m18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> 0620576fa07a
Removing intermediate container 2856867c2657
Step 10/13 : WORKDIR /
 ---> 44c840986e77
Removing intermediate container 01cd698404c2
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 09adefd64ba6
 ---> ec389f6ccec6
Removing intermediate container 09adefd64ba6
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 06ce83d4e3ff
 ---> f18fae75db1a
Removing intermediate container 06ce83d4e3ff
Step 13/13 : USER [secure]
 ---> Running in 87393cee79ea
 ---> b6e1891ca87b
Removing intermediate container 87393cee79ea
Successfully built b6e1891ca87b
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:edfe062e8b0068c848afcd6ba420e0377dd633d043a2a3c41f75a315b9d7b1b6
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:2c3fdf2511eb544ed15c4d1b5ecc0fb49035c6e599c1525efc98d678b29983b1
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:196765c7:start=1572316904338251812,finish=1572317261537462515,duration=357199210703,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0113c51d[0K$ python push.py -s -t of-ccx

```
[
Full job log](https://api.travis-ci.org/v3/job/604222464/log.txt)