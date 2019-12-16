## Status: Passing 
Build: [1319](https://travis-ci.org/precice/systemtests/builds/625610178) 

Job: [1319.19](https://travis-ci.org/precice/systemtests/jobs/625610197) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     53% |*****************               | 13.3M  0:00:25 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:24 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:23 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:22 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:21 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:20 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:18 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:17 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:16 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:14 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:11 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:09 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:08 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:07 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:01 ETA
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
 ---> 8e99398b01ca
Removing intermediate container 7a1cf3679b8a
Step 11/14 : WORKDIR /
 ---> 7bdc6953f794
Removing intermediate container 67e5eae038e1
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in a60450663b87
 ---> abb2c09d38b4
Removing intermediate container a60450663b87
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8ded6809652e
 ---> 5edea9074727
Removing intermediate container 8ded6809652e
Step 14/14 : USER [secure]
 ---> Running in 7cd064143fa4
 ---> f3b8bcf21feb
Removing intermediate container 7cd064143fa4
Successfully built f3b8bcf21feb
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1ba6b0e960501300870aabf7bfa64d904caeff59808132a5da9e69953621da51
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:f68ccbe67292cb54b4dc86ba23cdbb3583deb31addad1abbc223cfcb2b94e808
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0f2af32a:start=1576495609999347969,finish=1576495945323148675,duration=335323800706,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0f0dedf2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0f0dedf2:start=1576495949277146762,finish=1576495950613736490,duration=1336589728,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:153a5e67[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/625610197/log.txt)