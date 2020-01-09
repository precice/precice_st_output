## Status: Failure 
Build: [1413](https://travis-ci.org/precice/systemtests/builds/634661128) 

Job: [1413.3](https://travis-ci.org/precice/systemtests/jobs/634661131) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     28% |********                        | 7179k  0:00:38 ETA
[0m[91m-                     30% |*********                       | 7701k  0:00:37 ETA
[0m[91m-                     32% |**********                      | 8279k  0:00:35 ETA
[0m[91m-                     34% |***********                     | 8836k  0:00:34 ETA
[0m[91m-                     36% |***********                     | 9350k  0:00:33 ETA
[0m[91m-                     38% |************                    | 9916k  0:00:31 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:30 ETA
[0m[91m-                     43% |*************                   | 10.7M  0:00:29 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% [0m[91m|***************                 | 12.3M[0m[91m  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.5M  0:00:23 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:16 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M[0m[91m  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                    [0m[91m 81% [0m[91m|**************************      | 20.4M  0:00:08 ETA
[0m[91m-                    [0m[91m 82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                    [0m[91m 99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 40ab3b26f2e2
Removing intermediate container c88cf70da1b2
Step 11/14 : WORKDIR /
 ---> 9c3d74fbc73f
Removing intermediate container d04b49e962aa
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 13e5d4aedb33
 ---> 4f6c6f19319e
Removing intermediate container 13e5d4aedb33
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 25c3e69f768b
 ---> 47dac50ad9a6
Removing intermediate container 25c3e69f768b
Step 14/14 : USER [secure]
 ---> Running in f21cd001404f
 ---> cef1a456c689
Removing intermediate container f21cd001404f
Successfully built cef1a456c689
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
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Outer-Fluid', 'Inner-Fluid']
Files only in output(right)   : []
travis_time:end:16947a59:start=1578563593645551389,finish=1578563744126993674,duration=150481442285,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0c852d96[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634661131/log.txt)