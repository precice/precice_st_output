## Status: Passing 
Build: [1248](https://travis-ci.org/precice/systemtests/builds/620247509) 

Job: [1248.15](https://travis-ci.org/precice/systemtests/jobs/620247524) 

Triggered by: [push](https://github.com/precice/systemtests/commit/25da98cf068b) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     52% |****************                | 13.0M  0:00:23 ETA
[0m[91m-                    [0m[91m 54% |*****************               | 13.6M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                    [0m[91m 80% |*************************       | 20.2M[0m[91m  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M[0m[91m  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     95% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| [0m[91m25.0M[0m[91m  0:00:00 ETA
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
 ---> c9a8d5cd55f4
Removing intermediate container 3f357cdd82d4
Step 11/14 : WORKDIR /
 ---> fff3a21a46b9
Removing intermediate container ef93095a3507
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d39032af13ae
 ---> db3a62072594
Removing intermediate container d39032af13ae
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 10ad908bb022
 ---> 2d58e0f38ddd
Removing intermediate container 10ad908bb022
Step 14/14 : USER [secure]
 ---> Running in d654e374997e
 ---> e1aac4cf4467
Removing intermediate container d654e374997e
Successfully built e1aac4cf4467
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c6392f8479b0628d5026f531530b3fa6ba5a7f27506f57712b6f098558a846c7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b4c7818bd0a230a8636f7cdbfa8ca911d10becc540f4f4f8cd6e9e95dde365f4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0a9375c2:start=1575399900713084663,finish=1575400340131433765,duration=439418349102,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02a39814[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02a39814:start=1575400344712056838,finish=1575400346348017170,duration=1635960332,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:13cef627[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620247524/log.txt)