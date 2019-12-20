## Status: Passing 
Build: [1354](https://travis-ci.org/precice/systemtests/builds/627653298) 

Job: [1354.19](https://travis-ci.org/precice/systemtests/jobs/627653317) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     44% |**************                  | 11.1M  0:00:26 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:24 ETA
[0m[91m-                     49% |***************                 | [0m[91m12.3M  0:00:23 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:22 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:21 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:20 ETA
[0m[91m-                     58% [0m[91m|******************              | 14.6M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:15 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:14 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:11 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:09 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:09 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
written to stdout
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
 ---> e81bba11197c
Removing intermediate container a0eadf9e67f0
Step 11/14 : WORKDIR /
 ---> 8e614989e2c3
Removing intermediate container 84a11da0ec08
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in b0d468d981f0
 ---> 4540059b853c
Removing intermediate container b0d468d981f0
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 936a5e37a6ec
 ---> f62ce5ac1b05
Removing intermediate container 936a5e37a6ec
Step 14/14 : USER [secure]
 ---> Running in 6832b12492af
 ---> f3770875e8a5
Removing intermediate container 6832b12492af
Successfully built f3770875e8a5
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8ae4b42ea38e04ba17c36bf6dcaac763642483e46c306707438eff2f15b15bb5
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6f6a979fe8752119572b83c5a6aae17fcf8a4cadd0ee2052088f47fea8e87894
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:28f9c5bd:start=1576841111697680062,finish=1576841375947074408,duration=264249394346,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0abf64d6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0abf64d6:start=1576841379967937610,finish=1576841381338461069,duration=1370523459,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:00aa151a[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/627653317/log.txt)