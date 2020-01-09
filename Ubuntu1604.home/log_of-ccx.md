## Status: Failure 
Build: [1412](https://travis-ci.org/precice/systemtests/builds/634659751) 

Job: [1412.3](https://travis-ci.org/precice/systemtests/jobs/634659754) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     34% |***********                     | 8888k  0:00:30 ETA
[0m[91m-                     36% |***********                     | 9447k  0:00:29 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:27 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:27 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:25 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:22 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:16 ETA
[0m[91m-                    [0m[91m 71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.7M[0m[91m  0:00:08 ETA[0m[91m
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M[0m[91m  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA
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
 ---> 9f1f471f4e8f
Removing intermediate container 92d8d96b81f8
Step 11/14 : WORKDIR /
 ---> 2e869780b455
Removing intermediate container 996496227fec
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 9f5b7e1e1d67
 ---> ea529349921a
Removing intermediate container 9f5b7e1e1d67
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fc9f2f1b3bdd
 ---> 15baa2c7d7b2
Removing intermediate container fc9f2f1b3bdd
Step 14/14 : USER [secure]
 ---> Running in 8871a2b90ccf
 ---> 537488e2db85
Removing intermediate container 8871a2b90ccf
Successfully built 537488e2db85
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
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:0ccf6a68:start=1578563244968624087,finish=1578563455381553317,duration=210412929230,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0dfb4a4e[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634659754/log.txt)