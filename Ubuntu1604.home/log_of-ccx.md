## Status: Passing 
Build: [1249](https://travis-ci.org/precice/systemtests/builds/620247918) 

Job: [1249.15](https://travis-ci.org/precice/systemtests/jobs/620247944) 

Triggered by: [push](https://github.com/precice/systemtests/compare/96bc06472339...f9c5ac902029) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     46% |**************                  | 11.6M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:21 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:20 ETA[0m[91m
[0m[91m-                     63% |********************            | 15.7M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     78% |************************        | 19.5M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                    [0m[91m 97% |******************************* | 24.4M[0m[91m  0:00:01 ETA[0m[91m
[0m[91m-                    [0m[91m 99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> bae59246656c
Removing intermediate container 0af0b7116249
Step 11/14 : WORKDIR /
 ---> cfa1efd56463
Removing intermediate container c42e95dd121f
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d9b9cb2b4b45
 ---> fd4b16ea25d4
Removing intermediate container d9b9cb2b4b45
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9ae5b1db5edb
 ---> 378b00b6a011
Removing intermediate container 9ae5b1db5edb
Step 14/14 : USER [secure]
 ---> Running in c1e7adbb5f8d
 ---> f6de0111dd19
Removing intermediate container c1e7adbb5f8d
Successfully built f6de0111dd19
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:27f9c92f133bc04da46d7fb6b630ca9dba656907f0728f0a4fd2e27fc75c922f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:18fa09af440dbd2e31b78b43582d34cf4275445875a8c928ee394cd11f2a3976
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
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
travis_time:end:1a438ce6:start=1575402183529460525,finish=1575402529351073342,duration=345821612817,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:224214a0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:224214a0:start=1575402533676169040,finish=1575402535260255367,duration=1584086327,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:12d02718[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/620247944/log.txt)