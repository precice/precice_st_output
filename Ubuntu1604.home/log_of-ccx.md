## Status: Passing 
Build: [1118](https://travis-ci.org/precice/systemtests/builds/612976109) 

Job: [1118.19](https://travis-ci.org/precice/systemtests/jobs/612976128) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     65% |*********************           | 16.4M  0:00:26 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:25 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:24 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:23 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:23 ETA
[0m[91m-                    [0m[91m 70% |**********************          | 17.7M  0:00:23 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:22 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:21 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:21 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:21 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:20 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:19 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:18 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:16 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:15 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:15 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:15 ETA
[0m[91m-                     83% |**************************      | 20.7M  0:00:13 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:12 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:10 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:10 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:08 ETA
[0m[91m-                    [0m[91m 91% |*****************************   | 22.7M  0:00:07 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:05 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:03 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:02 ETA
[0m[91m-                    [0m[91m 99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    [0m[91m100% [0m[91m|********************************| 25.0M[0m[91m  0:00:00 ETA[0m[91m
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
 ---> 59b8f2ae8eaa
Removing intermediate container b873dbd369e0
Step 10/13 : WORKDIR /
 ---> bbaef520dd2a
Removing intermediate container b35410c55039
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 3c77d04b41b5
 ---> f1e12db5d715
Removing intermediate container 3c77d04b41b5
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 049e9337ac6a
 ---> 24a7b3b8b9b5
Removing intermediate container 049e9337ac6a
Step 13/13 : USER [secure]
 ---> Running in 4849b1006995
 ---> 7f0191b22932
Removing intermediate container 4849b1006995
Successfully built 7f0191b22932
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:b6387388dca0eed8725e4578b7aa575f82ac415c2ccf5823e677ff66c08229d9
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:2d312a88b64b94f813141b50d916eccb97d24ed5c2affaa051e2fe768ac9c311
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1344e42a:start=1573959072294718016,finish=1573959446435465532,duration=374140747516,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2a38e38e[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2a38e38e:start=1573959451295766709,finish=1573959452962343890,duration=1666577181,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0084df3c[0KSuccessfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/612976128/log.txt)