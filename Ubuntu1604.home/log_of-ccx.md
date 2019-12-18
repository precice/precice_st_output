## Status: Passing 
Build: [1324](https://travis-ci.org/precice/systemtests/builds/626625324) 

Job: [1324.19](https://travis-ci.org/precice/systemtests/jobs/626625351) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     35% |***********                     | 9181k  0:00:35 ETA
[0m[91m-                     38% |************                    | 9753k  0:00:34 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:32 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:32 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:32 ETA
[0m[91m-                     45% |**************                  | 11.2M  0:00:31 ETA
[0m[91m-                    [0m[91m 47% |***************                 | 11.8M  0:00:30 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:28 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:27 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:25 ETA
[0m[91m-                    [0m[91m 55% [0m[91m|*****************               | 13.9M  0:00:24 ETA
[0m[91m-                    [0m[91m 57% |******************              | 14.4M  0:00:23 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:20 ETA
[0m[91m-                    [0m[91m 64% |********************            | 16.0M  0:00:19 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:18 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:17 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:11 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% [0m[91m|****************************    | 21.9M  0:00:06 ETA
[0m[91m-                    [0m[91m 89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M[0m[91m  0:00:04 ETA[0m[91m
[0m[91m-                     93% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
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
 ---> fec54908c501
Removing intermediate container e95cbb7ff936
Step 11/14 : WORKDIR /
 ---> 569d506c0b31
Removing intermediate container 7b57b03bf64f
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in ea72163539bc
 ---> 59dee89bf87c
Removing intermediate container ea72163539bc
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7c6bc4b1d270
 ---> 79995c32cc35
Removing intermediate container 7c6bc4b1d270
Step 14/14 : USER [secure]
 ---> Running in ba7f4aa5dd8c
 ---> 94ec1e9aa194
Removing intermediate container ba7f4aa5dd8c
Successfully built 94ec1e9aa194
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c3a9c88d2a644a109c91ceb8b95f57d3e2389d374e84bdd06d85311542068410
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:32481bd8f4d56c2359e6d26a2bb8723fde0eac8d6c861c2444fe6dc1e299ec46
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1065b4dc:start=1576670226345150525,finish=1576670687188686645,duration=460843536120,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:00d42691[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
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
Full job log](https://api.travis-ci.org/v3/job/626625351/log.txt)