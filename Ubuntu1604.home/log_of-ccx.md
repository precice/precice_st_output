## Status: Failure 
Build: [1378](https://travis-ci.org/precice/systemtests/builds/631253529) 

Job: [1378.20](https://travis-ci.org/precice/systemtests/jobs/631253549) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     30% |*********                       | 7853k  0:00:38 ETA
[0m[91m-                     33% |**********                      | 8478k  0:00:36 ETA
[0m[91m-                     35% |***********                     | 9049k  0:00:34 ETA
[0m[91m-                     37% |***********                     | 9609k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.2M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:31 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:28 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:22 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     63% |********************            | 16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                    [0m[91m 73% |***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M[0m[91m  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     92% [0m[91m|*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 2e328f1920dd
Removing intermediate container 21a331efb31f
Step 11/14 : WORKDIR /
 ---> 439c71903749
Removing intermediate container b7a3218a2d58
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 511361b4e03f
 ---> e09aa92d2952
Removing intermediate container 511361b4e03f
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 4685500f5ec8
 ---> 9aff73cd9060
Removing intermediate container 4685500f5ec8
Step 14/14 : USER [secure]
 ---> Running in ae362cd322cc
 ---> 5c85c609968e
Removing intermediate container ae362cd322cc
Successfully built 5c85c609968e
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:fc34d09e5533265453e6fd1359326aa5c430eea19ed47fcd8e60325f28e2b011
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:07084e33f4f130b9cd6ff5986f296cf71fbdadac604bd75534ced976275e8738
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
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
Files only in reference (left): ['Outer-Fluid', 'Inner-Fluid']
Files only in output(right)   : []
travis_time:end:04c736ca:start=1577791619361547150,finish=1577791832330941622,duration=212969394472,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0fd59567[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/631253549/log.txt)