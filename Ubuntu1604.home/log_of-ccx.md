## Status: Passing 
Build: [1205](https://travis-ci.org/precice/systemtests/builds/618334138) 

Job: [1205.15](https://travis-ci.org/precice/systemtests/jobs/618334153) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f6ac64c472af...3b2ed1c3a41a) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     29% |*********                       | 7607k  0:00:37 ETA
[0m[91m-                    [0m[91m 31% [0m[91m|**********                      | 8172k  0:00:36 ETA
[0m[91m-                     33% |**********                      | 8678k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9253k  0:00:33 ETA
[0m[91m-                     38% |************                    | 9817k  0:00:32 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:30 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:28 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:24 ETA
[0m[91m-                    [0m[91m 55% |*****************               | 13.7M  0:00:23 ETA
[0m[91m-                    [0m[91m 56% [0m[91m|******************              | 14.2M  0:00:22 ETA
[0m[91m-                    [0m[91m 58% |******************              | 14.6M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:20 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                    [0m[91m 71% [0m[91m|**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                    [0m[91m 84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     87% |***************************     | [0m[91m21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | [0m[91m22.8M  0:00:04 ETA
[0m[91m-                    [0m[91m 93% [0m[91m|*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% [0m[91m|******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA
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
 ---> 5bb1beb95ae7
Removing intermediate container 5880bbdb8c0e
Step 11/14 : WORKDIR /
 ---> 5fb4bbf50f90
Removing intermediate container 77ab013168ad
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 1dc40ef96427
 ---> 00b708caa741
Removing intermediate container 1dc40ef96427
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b093b07adb80
 ---> d5889a1b9aa6
Removing intermediate container b093b07adb80
Step 14/14 : USER [secure]
 ---> Running in 52abb9c2f187
 ---> e4b98f7967af
Removing intermediate container 52abb9c2f187
Successfully built e4b98f7967af
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ce171974344908d9cd30d6b96441d1073584c84ad0e4bd47423ae72c52217f81
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4174e4b498a6d21c3425f9480b871a5c0cacbf300264230688b561c96dd6641b
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:01f25104:start=1575052073884698622,finish=1575052473684128140,duration=399799429518,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0f7f96aa[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0f7f96aa:start=1575052478268034633,finish=1575052479975699296,duration=1707664663,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:186c88fc[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618334153/log.txt)