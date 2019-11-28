## Status: Passing 
Build: [1172](https://travis-ci.org/precice/systemtests/builds/618111185) 

Job: [1172.15](https://travis-ci.org/precice/systemtests/jobs/618111200) 

Triggered by: [push](https://github.com/precice/systemtests/compare/i_16) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     60% |*******************             | 15.0M  0:00:23 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:21 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:20 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:19 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:17 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:16 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:15 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:10 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
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
 ---> c92a9cff4a05
Removing intermediate container 5afd43f313e3
Step 11/14 : WORKDIR /
 ---> 61d13fec9782
Removing intermediate container 14b33a6c454b
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in c2577c36642a
 ---> 9ca7528e912f
Removing intermediate container c2577c36642a
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 26eb5599b62a
 ---> c8258e939bfe
Removing intermediate container 26eb5599b62a
Step 14/14 : USER [secure]
 ---> Running in 218d80abdef3
 ---> e7d0db4d02bc
Removing intermediate container 218d80abdef3
Successfully built e7d0db4d02bc
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:4491787de2d4fac20f1d9f1e5c5b3c0381e57cd6347953bbc802fe433075bcb0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:62c6bf0e000fc53a5a523d5051d0f63530a64f21a716336632b47d6cb2ec3e35
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2c799e4a:start=1574938522916921589,finish=1574938953898596125,duration=430981674536,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:051c078d[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:051c078d:start=1574938959104966740,finish=1574938960939172264,duration=1834205524,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:298d1f90[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618111200/log.txt)