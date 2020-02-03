## Status: Passing 
Build: [1587](https://travis-ci.org/precice/systemtests/builds/645394789) 

Job: [1587.19](https://travis-ci.org/precice/systemtests/jobs/645394817) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:18 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:15 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     78% |************************        | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:07 ETA
[0m[91m-                     84% |**************************      | 21.1M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 22.9M[0m[91m  0:00:03 ETA
[0m[91m-                    [0m[91m 93% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                    [0m[91m 96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
[0m[91mwritten to stdout
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
 ---> ac082b6a9118
Removing intermediate container e3cf78efd635
Step 11/14 : WORKDIR /
 ---> 1bb9e2f8ff86
Removing intermediate container 42e9a3ebc7e7
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 4ad258bcb02d
 ---> 7175f1b83069
Removing intermediate container 4ad258bcb02d
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in a2de1b0a82cf
 ---> 88f058ef486a
Removing intermediate container a2de1b0a82cf
Step 14/14 : USER [secure]
 ---> Running in 44be40d23e0c
 ---> 551d951d05e1
Removing intermediate container 44be40d23e0c
Successfully built 551d951d05e1
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1bf7bfebac3582204fa43ff8841c901bd107b21d514963b85f521a8d27991f7b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:cae278f74b44afbe0e419f212e668f19fd36fcfd3a0ba016973d42b07076f28e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:1ff7429c:start=1580730176963930338,finish=1580730442901924694,duration=265937994356,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:033e8b8c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:033e8b8c:start=1580730447028015408,finish=1580730448402174638,duration=1374159230,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:16bd1ee3[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/645394817/log.txt)