## Status: Failure 
Build: [1473](https://travis-ci.org/precice/systemtests/builds/639882085) 

Job: [1473.20](https://travis-ci.org/precice/systemtests/jobs/639882107) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     24% |*******                         | 6170k  0:00:34 ETA
[0m[91m-                     26% |********                        | 6758k  0:00:33 ETA
[0m[91m-                     28% |*********                       | 7363k  0:00:32 ETA
[0m[91m-                     30% |*********                       | 7941k  0:00:31 ETA
[0m[91m-                     32% |**********                      | 8311k  0:00:31 ETA
[0m[91m-                     33% |**********                      | 8527k  0:00:32 ETA
[0m[91m-                     34% |***********                     | 8943k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9537k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:26 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:20 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:11 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:09 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
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
 ---> 3d8bb20cb243
Removing intermediate container 5d44fbe06329
Step 11/14 : WORKDIR /
 ---> aa6d6ae09c29
Removing intermediate container 14dc7e5254bb
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in f6ec13a3cb1e
 ---> f2bc3f6556dc
Removing intermediate container f6ec13a3cb1e
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ab22508a9679
 ---> 7851eb3585eb
Removing intermediate container ab22508a9679
Step 14/14 : USER [secure]
 ---> Running in e304580723f7
 ---> 64682c8239e7
Removing intermediate container e304580723f7
Successfully built 64682c8239e7
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c9b1ac4c62dcfdcdaec91308e9dd1f3744c533cd952757de7a30543d9bf4c96b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:ff6794dd1ce3de5ca8d7135faac789b2b02dbeb529bf1375093e04af45e243f4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
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
travis_time:end:06999d3b:start=1579606915234564845,finish=1579607120045386192,duration=204810821347,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:21d67e98[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/639882107/log.txt)