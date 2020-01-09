## Status: Failure 
Build: [1415](https://travis-ci.org/precice/systemtests/builds/634678414) 

Job: [1415.20](https://travis-ci.org/precice/systemtests/jobs/634678436) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     33% |**********                      | 8702k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9286k  0:00:33 ETA
[0m[91m-                     38% |************                    | 9866k  0:00:31 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:30 ETA
[0m[91m-                     43% |*************                   | 10.7M  0:00:29 ETA
[0m[91m-                    [0m[91m 45% |**************                  | 11.3M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.5M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.2M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% [0m[91m|********************            | [0m[91m16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                    [0m[91m 71% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.5M[0m[91m  0:00:07 ETA
[0m[91m-                     87% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 24550f419789
Removing intermediate container 313f7cb11a6c
Step 11/14 : WORKDIR /
 ---> b0d9bf28b1b7
Removing intermediate container ef73eaa77a79
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 65b120afc825
 ---> ebd5cb4707df
Removing intermediate container 65b120afc825
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 619c12c39e2e
 ---> 59edabdff313
Removing intermediate container 619c12c39e2e
Step 14/14 : USER [secure]
 ---> Running in ba9236ff6c6f
 ---> efd8d5655bb9
Removing intermediate container ba9236ff6c6f
Successfully built efd8d5655bb9
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8469fc15e29f7e13ef656170fc50b2543001183fb3f84c25ed30090dae8831c6
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6acdaee81c5fc807c10ed0eef15f00dce1b1f6043e1856b45079c267afa17651
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
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
travis_time:end:33caf149:start=1578569450228811900,finish=1578569668313605424,duration=218084793524,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:3634b2b8[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634678436/log.txt)