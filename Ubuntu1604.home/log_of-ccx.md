## Status: Failure 
Build: [1459](https://travis-ci.org/precice/systemtests/builds/637887909) 

Job: [1459.20](https://travis-ci.org/precice/systemtests/jobs/637887951) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     24% |*******                         | 6268k  0:00:43 ETA
[0m[91m-                     26% [0m[91m|********                        | 6788k  0:00:41 ETA
[0m[91m-                     28% |*********                       | 7358k  0:00:39 ETA
[0m[91m-                     31% |*********                       | 7982k  0:00:37 ETA
[0m[91m-                     33% |**********                      | 8549k  0:00:35 ETA
[0m[91m-                     35% |***********                     | 9186k  0:00:34 ETA[0m[91m
[0m[91m-                     38% |************                    | 9755k  0:00:32 ETA
[0m[91m-                     40% [0m[91m|************                    | 10.0M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:28 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:17 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
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
 ---> 3d5a014ea837
Removing intermediate container 076ea3f9f7d2
Step 11/14 : WORKDIR /
 ---> 7ada8ae9340c
Removing intermediate container fdfe3d88055d
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e045ff5e5db5
 ---> 942224c457b9
Removing intermediate container e045ff5e5db5
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ed40dde77220
 ---> da5182961038
Removing intermediate container ed40dde77220
Step 14/14 : USER [secure]
 ---> Running in a2407e8a3484
 ---> 2fa9cee8c48b
Removing intermediate container a2407e8a3484
Successfully built 2fa9cee8c48b
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e0ba286116ffd00b3284eb80c068a679ca2a6207dd63adce1caa59512fd9b920
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:70d6ac343f54ab83e728847a11c4c78a1548644af0b7fa5e12cc7386fa3de2e9
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
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
travis_time:end:2acbb5cf:start=1579174748364736692,finish=1579174953972396675,duration=205607659983,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0230df78[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637887951/log.txt)