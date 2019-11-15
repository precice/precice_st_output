## Status: Passing 
Build: [1094](https://travis-ci.org/precice/systemtests/builds/612166197) 

Job: [1094.19](https://travis-ci.org/precice/systemtests/jobs/612166216) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                    [0m[91m 50% |****************                | 12.6M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:26 ETA
[0m[91m-                    [0m[91m 53% [0m[91m|*****************               | 13.3M  0:00:25 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:23 ETA[0m[91m
[0m[91m-                     57% |******************              | 14.4M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:20 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA[0m[91m
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
 ---> 05670fc21ae3
Removing intermediate container da2dd45f7301
Step 10/13 : WORKDIR /
 ---> e839ec447f62
Removing intermediate container aa6088e299d5
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7ec46f93861a
 ---> 98e2dfec1247
Removing intermediate container 7ec46f93861a
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7d6c22619c79
 ---> 94364c6bdb62
Removing intermediate container 7d6c22619c79
Step 13/13 : USER [secure]
 ---> Running in 016ddd4743a4
 ---> e6cb9a6168db
Removing intermediate container 016ddd4743a4
Successfully built e6cb9a6168db
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0ae867a0bf4596155dec39c40214ef0bdc2941a0552d3578d83e96ddc5041ef4
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:63be63b649a3670644f55b0dc84382cad84bb44cb0619575fd2ef4e10381da5c
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2590486e:start=1573786124957767612,finish=1573786478454284685,duration=353496517073,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0eaf2a48[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0eaf2a48:start=1573786482858480936,finish=1573786484440486559,duration=1582005623,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2f20a796[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/612166216/log.txt)