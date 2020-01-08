## Status: Failure 
Build: [1408](https://travis-ci.org/precice/systemtests/builds/634323804) 

Job: [1408.16](https://travis-ci.org/precice/systemtests/jobs/634323829) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/131) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     46% |**************                  | 11.5M  0:00:31 ETA
[0m[91m-                     47% |***************                 | 11.7M  0:00:31 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:31 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:31 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:31 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:30 ETA
[0m[91m-                     53% |*****************               | 13.2M  0:00:29 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:27 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:25 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:23 ETA
[0m[91m-                     61% |*******************             | 15.2M  0:00:23 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:23 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:22 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:20 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:20 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:19 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:17 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:16 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:14 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:13 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:13 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:12 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:11 ETA
[0m[91m-                     83% |**************************      | 20.7M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:09 ETA
[0m[91m-                     85% |***************************     | 21.2M  0:00:09 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:08 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:07 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     96% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
[0m[91mwritten to stdout
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
 ---> f0afff0af603
Removing intermediate container 547bf82e5057
Step 11/14 : WORKDIR /
 ---> 28d9bac477f3
Removing intermediate container 50bf22d96238
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in f5970e7cd278
 ---> d6fbb73bdd49
Removing intermediate container f5970e7cd278
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in abe6d704c219
 ---> e6d760fab3f4
Removing intermediate container abe6d704c219
Step 14/14 : USER [secure]
 ---> Running in 97685c582b29
 ---> 63b5b11e5ed8
Removing intermediate container 97685c582b29
Successfully built 63b5b11e5ed8
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e442f33a6f3cab80648fc9ce72f80770ee8c748f2969dc4cd39d3ccd02fd4e5a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e6259893f4093a5cb6bb83bf002935e9a732dd240ea229ed3b845be883daaa5d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Outer-Fluid', 'Inner-Fluid']
Files only in output(right)   : []
travis_time:end:08084028:start=1578503867956138831,finish=1578504085904632646,duration=217948493815,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:04ede5a0[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634323829/log.txt)