## Status: Passing 
Build: [1170](https://travis-ci.org/precice/systemtests/builds/617994421) 

Job: [1170.19](https://travis-ci.org/precice/systemtests/jobs/617994440) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                    [0m[91m 45% [0m[91m|**************                  | 11.3M  0:00:30 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:26 ETA
[0m[91m-                     53% |*****************               | 13.5M  0:00:24 ETA
[0m[91m-                     56% |*****************               | 14.0M[0m[91m  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     68% |**********************          | [0m[91m17.2M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                    [0m[91m 77% [0m[91m|************************        | 19.4M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | [0m[91m22.1M  0:00:05 ETA
[0m[91m-                    [0m[91m 90% [0m[91m|*****************************   | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% [0m[91m|******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 347d6c7f410c
Removing intermediate container f17d6f4c9abd
Step 10/13 : WORKDIR /
 ---> 85a678385a4c
Removing intermediate container 601ef945ef97
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d2a6b0d92420
 ---> ad3eb2d1a660
Removing intermediate container d2a6b0d92420
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c9f2c0cdc651
 ---> bfcbc2d52093
Removing intermediate container c9f2c0cdc651
Step 13/13 : USER [secure]
 ---> Running in b2ead6ca6bb6
 ---> 575bf4387f9a
Removing intermediate container b2ead6ca6bb6
Successfully built 575bf4387f9a
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:b4cd2d454d68843068cbd63106533105383ce6a650bf581e97e0a0196527023a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e592aba03c4e1f91e695bae05d662f4a322675fddbc582a2e480e3e5e84782b4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:20b3aa06:start=1574909501897217346,finish=1574909850011699250,duration=348114481904,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1a87c8ce[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1a87c8ce:start=1574909854471517436,finish=1574909856108640839,duration=1637123403,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1de24f08[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/617994440/log.txt)