## Status: Passing 
Build: [1326](https://travis-ci.org/precice/systemtests/builds/627156304) 

Job: [1326.19](https://travis-ci.org/precice/systemtests/jobs/627156323) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     41% |*************                   | 10.4M  0:00:27 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:26 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:24 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:24 ETA[0m[91m
[0m[91m-                     53% |*****************               | 13.3M  0:00:22 ETA
[0m[91m-                    [0m[91m 55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA[0m[91m
[0m[91m-                     60% |*******************             | 15.0M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     81% |*************************       | 20.2M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 24b8bd018952
Removing intermediate container e4fc49122325
Step 11/14 : WORKDIR /
 ---> 8eb9eaa4d51a
Removing intermediate container 482e163f4786
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 2293ff945763
 ---> addd4c153c36
Removing intermediate container 2293ff945763
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c696dce2bb76
 ---> 995dc2b79ff1
Removing intermediate container c696dce2bb76
Step 14/14 : USER [secure]
 ---> Running in a3c99009f2d3
 ---> beb3a32dcf4f
Removing intermediate container a3c99009f2d3
Successfully built beb3a32dcf4f
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e170680a0f29ae173193b488e58247c07d9f3cc25078730c65388fd17d91b017
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6669e990cc7c6d0fe03ec19d19e155fee17662af6848869faa071879a02e1be8
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1b2b22c4:start=1576754642795842847,finish=1576754907726888099,duration=264931045252,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1659c401[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1659c401:start=1576754911904915247,finish=1576754913237602242,duration=1332686995,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:168f91f0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/627156323/log.txt)