## Status: Passing 
Build: [1320](https://travis-ci.org/precice/systemtests/builds/626119890) 

Job: [1320.19](https://travis-ci.org/precice/systemtests/jobs/626119913) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     45% |**************                  | 11.4M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.2M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.7M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> fa5a21f0d11f
Removing intermediate container 4a3338985eb8
Step 11/14 : WORKDIR /
 ---> 0a614b7ae992
Removing intermediate container 267ba48bc2f2
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 83af8b3fa818
 ---> eab036613d09
Removing intermediate container 83af8b3fa818
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 858bb1e9d111
 ---> 6db21921e452
Removing intermediate container 858bb1e9d111
Step 14/14 : USER [secure]
 ---> Running in fd00fa6d5a0a
 ---> aa3522eeeeb1
Removing intermediate container fd00fa6d5a0a
Successfully built aa3522eeeeb1
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8740f6fb490f48da9260ac8159c7db6ee4b4dfe6bb39f6e2ae0d4f57421d92cc
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:07ac69e544e44fe9581482b360fa014436640ccd6994b79a44c72200de464f87
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:01e4c080:start=1576582150899247157,finish=1576582542397745583,duration=391498498426,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0c8f8dd6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0c8f8dd6:start=1576582547232327239,finish=1576582548862606557,duration=1630279318,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:10020b5a[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/626119913/log.txt)