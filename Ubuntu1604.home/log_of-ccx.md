## Status: Passing 
Build: [1134](https://travis-ci.org/precice/systemtests/builds/616642276) 

Job: [1134.15](https://travis-ci.org/precice/systemtests/jobs/616642291) 

Triggered by: [push](https://github.com/precice/systemtests/commit/0d3b5a2c0bbe) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     44% [0m[91m|**************                  | 11.0M  0:00:32 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:31 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:29 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:28 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:26 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:25 ETA
[0m[91m-                    [0m[91m 56% |******************              | 14.2M  0:00:24 ETA
[0m[91m-                     59% [0m[91m|******************              | 14.8M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:21 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.4M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.5M  0:00:16 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:14 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                    [0m[91m 78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:08 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:01 ETA
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
 ---> bb8a11224bff
Removing intermediate container 6bc1ebbb7421
Step 10/13 : WORKDIR /
 ---> 94094419e252
Removing intermediate container 84ba67da41cb
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 00f3c8d1c6b1
 ---> 98398fc83e4a
Removing intermediate container 00f3c8d1c6b1
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2857fbea63f3
 ---> 9306216afdd0
Removing intermediate container 2857fbea63f3
Step 13/13 : USER [secure]
 ---> Running in 2ac9cd8c1ccf
 ---> 044f0119422b
Removing intermediate container 2ac9cd8c1ccf
Successfully built 044f0119422b
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:841fbebfd0e95b69b4a71598fc5834714c1fe03a0af429fbffb0119c530d48ec
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0662464aa216afb229ee0f28dcf699e638117125e116527d57c65add6618ef2c
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:08726b5f:start=1574687239545031787,finish=1574687615327110371,duration=375782078584,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:009db775[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:009db775:start=1574687619892326937,finish=1574687621593486287,duration=1701159350,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:20f6ad14[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/616642291/log.txt)