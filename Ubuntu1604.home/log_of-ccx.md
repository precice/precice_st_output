## Status: Failure 
Build: [1402](https://travis-ci.org/precice/systemtests/builds/634229912) 

Job: [1402.16](https://travis-ci.org/precice/systemtests/jobs/634229928) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/129) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     25% |********                        | 6455k  0:00:38 ETA
[0m[91m-                     27% |********                        | 7032k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7650k  0:00:35 ETA
[0m[91m-                     32% |**********                      | 8230k  0:00:33 ETA
[0m[91m-                     34% |**********                      | 8805k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9429k  0:00:30 ETA
[0m[91m-                     38% |************                    | 9995k  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:19 ETA[0m[91m
[0m[91m-                     59% |*******************             | 14.9M  0:00:18 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:05 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                    [0m[91m 89% [0m[91m|****************************    | 22.4M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
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
 ---> d945421d9247
Removing intermediate container f23f5471acfb
Step 11/14 : WORKDIR /
 ---> e7f61eea6c3d
Removing intermediate container 4d8358847273
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 34544681e261
 ---> 88c7c03124f1
Removing intermediate container 34544681e261
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8d8ee79f3cff
 ---> 9f11555c11bd
Removing intermediate container 8d8ee79f3cff
Step 14/14 : USER [secure]
 ---> Running in c905f24e8b97
 ---> 52a610f9b454
Removing intermediate container c905f24e8b97
Successfully built 52a610f9b454
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
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
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
travis_time:end:01d28436:start=1578491616970043026,finish=1578491824398114338,duration=207428071312,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0eac423b[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634229928/log.txt)