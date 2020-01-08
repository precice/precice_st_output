## Status: Failure 
Build: [1403](https://travis-ci.org/precice/systemtests/builds/634235375) 

Job: [1403.16](https://travis-ci.org/precice/systemtests/jobs/634235399) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/143) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     24% |*******                         | 6265k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6899k  0:00:35 ETA
[0m[91m-                     29% |*********                       | 7471k  0:00:34 ETA
[0m[91m-                     31% |**********                      | 8025k  0:00:32 ETA
[0m[91m-                     33% |**********                      | 8657k  0:00:31 ETA
[0m[91m-                     35% |***********                     | [0m[91m9225k  0:00:30 ETA
[0m[91m-                     38% |************                    | 9801k  0:00:29 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:27 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:25 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:24 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:21 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:20 ETA
[0m[91m-                     56% [0m[91m|******************              | 14.2M  0:00:19 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:18 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:17 ETA
[0m[91m-                     63% |********************            | 15.9M[0m[91m  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:15 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:09 ETA
[0m[91m-                    [0m[91m 79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.8M[0m[91m  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> f898885854db
Removing intermediate container ce76611c12c2
Step 11/14 : WORKDIR /
 ---> f142a9b27e76
Removing intermediate container a56064002f87
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 3e70aaf6998a
 ---> c324da6131f3
Removing intermediate container 3e70aaf6998a
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9a0974a9f7d2
 ---> cf4ecff2fa5b
Removing intermediate container 9a0974a9f7d2
Step 14/14 : USER [secure]
 ---> Running in 0dd25bf4a459
 ---> 03407fb78a19
Removing intermediate container 0dd25bf4a459
Successfully built 03407fb78a19
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
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
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
travis_time:end:249c7d2e:start=1578493188023547692,finish=1578493393930112594,duration=205906564902,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:14c7020d[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634235399/log.txt)