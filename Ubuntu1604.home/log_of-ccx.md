## Status: Passing 
Build: [1122](https://travis-ci.org/precice/systemtests/builds/613794885) 

Job: [1122.19](https://travis-ci.org/precice/systemtests/jobs/613794904) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     27% |********                        | 7019k  0:00:47 ETA
[0m[91m-                     29% |*********                       | 7583k  0:00:45 ETA
[0m[91m-                     31% |**********                      | 8082k  0:00:43 ETA
[0m[91m-                     33% |**********                      | 8643k  0:00:41 ETA
[0m[91m-                     35% |***********                     | 9213k  0:00:39 ETA
[0m[91m-                     38% [0m[91m|************                    | 9779k  0:00:37 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:35 ETA
[0m[91m-                     42% [0m[91m|*************                   | 10.6M  0:00:33 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:32 ETA
[0m[91m-                    [0m[91m 46% |**************                  | 11.7M  0:00:30 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:29 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:27 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:26 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:24 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:23 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:21 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:19 ETA
[0m[91m-                    [0m[91m 66% |*********************           | 16.5M  0:00:18 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:17 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.2M  0:00:12 ETA
[0m[91m-                    [0m[91m 79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA[0m[91m
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% [0m[91m|****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                    [0m[91m 95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
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
 ---> 87c62883d8ca
Removing intermediate container 22b0f0923399
Step 10/13 : WORKDIR /
 ---> 833d21182694
Removing intermediate container 123d13e46b8e
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in f2a65ffe57f0
 ---> e7273e1e535b
Removing intermediate container f2a65ffe57f0
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in a5e4e94b5d92
 ---> 80f83f057e63
Removing intermediate container a5e4e94b5d92
Step 13/13 : USER [secure]
 ---> Running in a5acc622a8ce
 ---> 86689e7de8a5
Removing intermediate container a5acc622a8ce
Successfully built 86689e7de8a5
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:844e14e1d93b14d3bb4ad6659f7796969c12548b32aeb379689f4a726d61cf48
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e5b5465467953818d261bae21695334c0e64c42bab9651ed231a5e8566bafea4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
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
travis_time:end:0d55f218:start=1574131894369560001,finish=1574132246696951284,duration=352327391283,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0131b2c2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0131b2c2:start=1574132251467459811,finish=1574132253236310928,duration=1768851117,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2ce144a4[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/613794904/log.txt)