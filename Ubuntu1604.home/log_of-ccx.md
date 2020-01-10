## Status: Failure 
Build: [1419](https://travis-ci.org/precice/systemtests/builds/635195369) 

Job: [1419.20](https://travis-ci.org/precice/systemtests/jobs/635195389) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     37% |***********                     | 9562k  0:00:31 ETA
[0m[91m-                     37% |************                    | 9731k  0:00:32 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:29 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:22 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:21 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:20 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                    [0m[91m 77% |************************        | 19.5M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | [0m[91m23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 91f527312c58
Removing intermediate container 2bf05e7f462e
Step 11/14 : WORKDIR /
 ---> 115a8feca63b
Removing intermediate container 1de8cc8f55dd
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7879b3c80607
 ---> fc35472af719
Removing intermediate container 7879b3c80607
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 34eb08dca754
 ---> 7cea3b922b31
Removing intermediate container 34eb08dca754
Step 14/14 : USER [secure]
 ---> Running in f8a6d832dde3
 ---> 4f9e9f8471fa
Removing intermediate container f8a6d832dde3
Successfully built 4f9e9f8471fa
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7725613ed53c7e7b1edf84a4611ef5f930acdd6f0dd8a6170c571c8bd2d47979
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:919abe00fab4dea098262e90f9d73b47a8dc22029d1db3cdb3e34be3d8d45719
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
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
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:055bdd0c:start=1578655963796656443,finish=1578656179821207329,duration=216024550886,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:03d15c38[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635195389/log.txt)