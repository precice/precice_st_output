## Status: Passing 
Build: [1580](https://travis-ci.org/precice/systemtests/builds/645031917) 

Job: [1580.19](https://travis-ci.org/precice/systemtests/jobs/645031936) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     47% |***************                 | 11.7M  0:00:24 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:23 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:22 ETA
[0m[91m-                     53% |*****************               | 13.5M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:18 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:09 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 75544c026f5e
Removing intermediate container d2684327ce67
Step 11/14 : WORKDIR /
 ---> 20de61b492f4
Removing intermediate container 6263b512ad24
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 28a0fffa48d4
 ---> 0d3a45309b93
Removing intermediate container 28a0fffa48d4
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 54519e693486
 ---> 392262f43a5f
Removing intermediate container 54519e693486
Step 14/14 : USER [secure]
 ---> Running in 016ab5104b56
 ---> 3baf78d14e65
Removing intermediate container 016ab5104b56
Successfully built 3baf78d14e65
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0f3098a7565f7c13fb013bff8dc52e2c2c3cdd94aca48d41865ca1d71096b7ae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4129efb1c914021feaa3fe1c16f99e06bf7fbb9152c9961d87c77b31652dfeb5
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
travis_time:end:096dfc7e:start=1580643719055689095,finish=1580643988404464633,duration=269348775538,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:040221e0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:040221e0:start=1580643992518795784,finish=1580643993814510552,duration=1295714768,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:025692f0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/645031936/log.txt)