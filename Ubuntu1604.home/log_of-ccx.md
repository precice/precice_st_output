## Status: Passing 
Build: [1256](https://travis-ci.org/precice/systemtests/builds/620607294) 

Job: [1256.16](https://travis-ci.org/precice/systemtests/jobs/620607318) 

Triggered by: [push](https://github.com/precice/systemtests/compare/db99b1df1818...f0c87c5da690) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     87% |****************************    | 21.9M  0:00:18 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:18 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:17 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:16 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:15 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:14 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:13 ETA
[0m[91m-                     91% |*****************************   | 22.7M  0:00:13 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:12 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:11 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:11 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:10 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:10 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:09 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:08 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:08 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:07 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:06 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:06 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:06 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:05 ETA
[0m[91m-                     96% |******************************* | 24.2M  0:00:04 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:03 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:03 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:02 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 96f121980e49
Removing intermediate container 0a75b77790f8
Step 11/14 : WORKDIR /
 ---> d847cad6629d
Removing intermediate container b4782778b594
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in b620ca7b73f4
 ---> 436ba86f032f
Removing intermediate container b620ca7b73f4
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2f5c72e35209
 ---> 6932b1e490d0
Removing intermediate container 2f5c72e35209
Step 14/14 : USER [secure]
 ---> Running in e4d824f7e581
 ---> 3070d442f1d9
Removing intermediate container e4d824f7e581
Successfully built 3070d442f1d9
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:715bdb658ce28c87b1344b87e535852cd579de49e1cc517a990ba19387287544
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:86c6e9db47764d2a510483b4e76acdef741f1ec728d8d7efb0e9387ed0eaec96
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:04ca5630:start=1575467285712100807,finish=1575467741769850159,duration=456057749352,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:00ea6f24[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:00ea6f24:start=1575467745884179076,finish=1575467747361352871,duration=1477173795,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2a852f0f[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620607318/log.txt)