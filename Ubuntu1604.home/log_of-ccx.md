 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583929538) 
## Triggered by: [cron](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     11% |***                             | 2827k  0:00:48 ETA
[0m[91m-                     13% |****                            | 3405k  0:00:45 ETA
[0m[91m-                    [0m[91m 15% |****                            | 3973k  0:00:43 ETA
[0m[91m-                     17% |*****                           | 4527k  0:00:41 ETA
[0m[91m-                     19% |******                          | 5091k  0:00:40 ETA
[0m[91m-                     21% |*******                         | 5615k  0:00:39 ETA
[0m[91m-                     24% |*******                         | 6176k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6744k  0:00:36 ETA
[0m[91m-                     28% |*********                       | 7299k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7810k  0:00:34 ETA
[0m[91m-                     32% [0m[91m|**********                      | 8381k  0:00:32 ETA
[0m[91m-                     34% |***********                     | 8959k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9526k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                    [0m[91m 41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:21 ETA
[0m[91m-                    [0m[91m 56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> 883a5c9be99c
Removing intermediate container 2d51ce1ebd54
Step 10/13 : WORKDIR /
 ---> 17fb2bda79d5
Removing intermediate container 9d882fd3b180
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d84f209e698f
 ---> 83e0e7a278f0
Removing intermediate container d84f209e698f
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 80edddecbeee
 ---> 33f7d1f60c83
Removing intermediate container 80edddecbeee
Step 13/13 : USER [secure]
 ---> Running in ec6fc79abb13
 ---> 2e74ad8a670d
Removing intermediate container ec6fc79abb13
Successfully built 2e74ad8a670d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:193947ff1e590caf032a10505ac90c1462765a1ecdf4025f9099eb1f318998a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:c14a14703d914f641d31bdacb87f51fdde55eb506bf0053f2ff3b3bc77b415c9
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1b3f39d2:start=1568254469772669889,finish=1568254815297079550,duration=345524409661,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:29ae9718[0K$ python push.py -s -t of-ccx
 ```
[Full job log](https://api.travis-ci.org/v3/job/583929557/log.txt)