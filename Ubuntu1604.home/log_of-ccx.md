## Status: Failure 
Build: [1382](https://travis-ci.org/precice/systemtests/builds/631528701) 

Job: [1382.20](https://travis-ci.org/precice/systemtests/jobs/631528721) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     36% |***********                     | 9233k  0:00:37 ETA
[0m[91m-                     37% |***********                     | 9530k  0:00:37 ETA
[0m[91m-                     37% |************                    | 9736k  0:00:37 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:37 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:38 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:38 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:37 ETA
[0m[91m-                     43% [0m[91m|*************                   | 10.9M  0:00:36 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:34 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:32 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:30 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:29 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:29 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:28 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:27 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:25 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:24 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:22 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:21 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:19 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:18 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:16 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:15 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:14 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:12 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:11 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:10 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:05 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                    [0m[91m 97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> 25c2e8496459
Removing intermediate container 7e3c404c3051
Step 11/14 : WORKDIR /
 ---> 89da37cc2ee8
Removing intermediate container c9fb6888c43c
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d09450f08ebc
 ---> c752bae41a5c
Removing intermediate container d09450f08ebc
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 07d7cbf19cd5
 ---> 836367ee1598
Removing intermediate container 07d7cbf19cd5
Step 14/14 : USER [secure]
 ---> Running in e247242b9485
 ---> 4611486b06e4
Removing intermediate container e247242b9485
Successfully built 4611486b06e4
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2eadc3a0c70c4b90e6aa86c93f35b0b1f6d1f10272fd491ce30485450f51e8ca
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:d5d71a6e16a8462bf733bdc4cfcb900614336848d9e9d2a3359da5ec84ccb745
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
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
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:039d1589:start=1577879549170364260,finish=1577879762804225240,duration=213633860980,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:37ddac0d[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/631528721/log.txt)