## Status: Passing 
Build: [1100](https://travis-ci.org/precice/systemtests/builds/612774159) 

Job: [1100.15](https://travis-ci.org/precice/systemtests/jobs/612774174) 

Triggered by: [push](https://github.com/precice/systemtests/compare/772d64248024...9566b8a963d8) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     29% |*********                       | 7619k[0m[91m  0:00:37 ETA
[0m[91m-                     31% |**********                      | 8180k  0:00:36 ETA
[0m[91m-                     33% |**********                      | 8684k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9247k  0:00:33 ETA
[0m[91m-                     38% |************                    | 9817k  0:00:32 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:30 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:31 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:30 ETA
[0m[91m-                     45% [0m[91m|**************                  | 11.3M  0:00:30 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:25 ETA
[0m[91m-                    [0m[91m 54% |*****************               | 13.5M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                    [0m[91m 96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                     99% |******************************* | 25.0M  0:00:00 ETA
-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> d65404a4692c
Removing intermediate container 13ce5ec39cc4
Step 10/13 : WORKDIR /
 ---> e3ec1f41decf
Removing intermediate container 59b2a8b21a0f
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d06a10bd8990
 ---> 40e6a0dee3cb
Removing intermediate container d06a10bd8990
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 46bc3b93068e
 ---> 4f2ccefe2431
Removing intermediate container 46bc3b93068e
Step 13/13 : USER [secure]
 ---> Running in 102a4798422d
 ---> 571d24185f24
Removing intermediate container 102a4798422d
Successfully built 571d24185f24
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:716de21b0369d6022c063dd3d1be49cb1424694a2ef78c353e3a2532fd4077da
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:9599864e0fd75ad936a502ea9d7634eb9059ad0f98056f5cccbc1b80bf83199c
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:065ac075:start=1573908018286552074,finish=1573908387186206642,duration=368899654568,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07a60d10[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07a60d10:start=1573908391880061109,finish=1573908393735560077,duration=1855498968,event=after_success[
```
[
Full job log](https://api.travis-ci.org/v3/job/612774174/log.txt)