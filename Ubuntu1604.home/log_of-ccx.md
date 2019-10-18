 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599531436) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3f2f194851e3...aeaaaab693ed) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     19% |******                          | 5049k  0:00:57 ETA
[0m[91m-                     21% |*******                         | 5621k  0:00:53 ETA
[0m[91m-                     24% |*******                         | 6187k  0:00:50 ETA
[0m[91m-                     26% [0m[91m|********                        | 6698k  0:00:48 ETA
[0m[91m-                     28% |*********                       | 7258k  0:00:45 ETA
[0m[91m-                     30% |*********                       | 7823k  0:00:43 ETA
[0m[91m-                     32% |**********                      | 8387k  0:00:41 ETA
[0m[91m-                    [0m[91m 34% [0m[91m|***********                     | 8890k  0:00:39 ETA
[0m[91m-                     36% |***********                     | 9455k  0:00:37 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:35 ETA
[0m[91m-                     41% |*************                   | [0m[91m10.3M  0:00:34 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:32 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:31 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:29 ETA
[0m[91m-                     49% |***************                 | 12.5M  0:00:28 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:27 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:26 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:25 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:24 ETA
[0m[91m-                    [0m[91m 59% |*******************             | 14.9M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:21 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:20 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:18 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:17 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:16 ETA
[0m[91m-                     72% |***********************         | [0m[91m18.2M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:13 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.2M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M[0m[91m  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                    [0m[91m 99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> cf927df5c983
Removing intermediate container 7b83ef8fe5db
Step 10/13 : WORKDIR /
 ---> e2c4a2f36f7e
Removing intermediate container d45cd294eab4
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in df372f36dbbb
 ---> cfd2c09ae84c
Removing intermediate container df372f36dbbb
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in bc0467ed6bfc
 ---> 8f079b167ec7
Removing intermediate container bc0467ed6bfc
Step 13/13 : USER [secure]
 ---> Running in 33b5ca47b6cd
 ---> bb5b1a1c4421
Removing intermediate container 33b5ca47b6cd
Successfully built bb5b1a1c4421
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ad692be02c5fed5891c3c0ecac2c2952067014e26d8596600ed9bd76fc76529f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:c075bea598796a084f35c73d0d563564a568ed706c5a0d4c2abd9525244da98a
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:081213cc:start=1571392497396162262,finish=1571392849717094334,duration=352320932072,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:02ea3614[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599531451/log.txt)