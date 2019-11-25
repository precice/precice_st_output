## Status: Passing 
Build: [1133](https://travis-ci.org/precice/systemtests/builds/616444566) 

Job: [1133.19](https://travis-ci.org/precice/systemtests/jobs/616444590) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     33% |**********                      | 8637k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9206k  0:00:32 ETA
[0m[91m-                     38% |************                    | 9771k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |**************                  | 11.7M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.7M  0:00:24 ETA
[0m[91m-                     53% [0m[91m|*****************               | 13.3M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M[0m[91m  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% [0m[91m|****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 8adcd7576e75
Removing intermediate container 87da8d709e99
Step 10/13 : WORKDIR /
 ---> 31222144f8c4
Removing intermediate container 525d55b74f13
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in f5e4c253ea10
 ---> 1ef5dd8a5466
Removing intermediate container f5e4c253ea10
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in a2734105c954
 ---> 0c497b6464dc
Removing intermediate container a2734105c954
Step 13/13 : USER [secure]
 ---> Running in 989e603a9f98
 ---> 6d0792e39cf2
Removing intermediate container 989e603a9f98
Successfully built 6d0792e39cf2
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8c87ca91a9ec4828f4c741ce69267ed62fa37009baa759554a9de4867241fc1e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:bd8aecc291ec219738802ec09516bf2497ccfc13076cfa870f2be7441f02fce7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
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
travis_time:end:0982ecc0:start=1574650549520251979,finish=1574650928589801850,duration=379069549871,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:08e536ea[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/616444590/log.txt)