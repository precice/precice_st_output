## Status: Passing 
Build: [1609](https://travis-ci.org/precice/systemtests/builds/646351628) 

Job: [1609.16](https://travis-ci.org/precice/systemtests/jobs/646351644) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646351628) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     26% |********                        | [0m[91m6889k  0:00:32 ETA
[0m[91m-                     29% |*********                       | 7503k  0:00:31 ETA
[0m[91m-                     31% |**********                      | 8076k  0:00:30 ETA
[0m[91m-                     33% |**********                      | 8646k  0:00:29 ETA
[0m[91m-                     36% |***********                     | 9275k  0:00:28 ETA
[0m[91m-                     38% |************                    | 9856k  0:00:27 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:26 ETA
[0m[91m-                     43% |*************                   | 10.7M  0:00:25 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:24 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:23 ETA
[0m[91m-                     49% |***************                 | 12.5M  0:00:22 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:21 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:21 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:21 ETA
[0m[91m-                     55% |*****************               | 14.0M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.2M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:14 ETA
[0m[91m-                     67% |*********************           | 17.0M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | [0m[91m17.7M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                    [0m[91m 89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:03 ETA
[0m[91m-                     93% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA
written to stdout
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
 ---> e25c7ace91fe
Removing intermediate container 9272e5cb5be7
Step 11/14 : WORKDIR /
 ---> 9cf813db454d
Removing intermediate container 547360eab1af
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in b8bb0112b3a5
 ---> f78ef6ba71b1
Removing intermediate container b8bb0112b3a5
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 6721cc206e38
 ---> 73d769f8e1fb
Removing intermediate container 6721cc206e38
Step 14/14 : USER [secure]
 ---> Running in 6f84aa8253da
 ---> 882d643e9924
Removing intermediate container 6f84aa8253da
Successfully built 882d643e9924
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e412e549a6a376d115044133965ff5c7d7a1fa08e65d438b4f1b92f4c0723a63
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:7ebee716256924987da7d6af552b3f2af3b060dce08cbd8bbfe04d340a88ac75
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:045dcd5b:start=1580904274118215819,finish=1580904600426388308,duration=326308172489,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02040eca[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02040eca:start=1580904605263452446,finish=1580904606834955295,duration=1571502849,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1e8a5f70[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/646351644/log.txt)