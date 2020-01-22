## Status: Failure 
Build: [1475](https://travis-ci.org/precice/systemtests/builds/640388632) 

Job: [1475.20](https://travis-ci.org/precice/systemtests/jobs/640388652) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     31% |*********                       | 7994k  0:00:37 ETA
[0m[91m-                     33% |**********                      | 8540k  0:00:36 ETA
[0m[91m-                     35% |***********                     | 9061k  0:00:34 ETA[0m[91m
[0m[91m-                     37% |************                    | 9630k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:30 ETA
[0m[91m-                     43% |**************                  | 11.0M  0:00:29 ETA
[0m[91m-                    [0m[91m 46% |**************                  | 11.5M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:26 ETA
[0m[91m-                    [0m[91m 50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                    [0m[91m 61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA[0m[91m
[0m[91m-                     81% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                    [0m[91m 88% |****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| [0m[91m25.0M  0:00:00 ETA[0m[91m
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
 ---> 0ed095385032
Removing intermediate container f918c10d95c7
Step 11/14 : WORKDIR /
 ---> 6d9cfa2faece
Removing intermediate container 70d6dfed92d0
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in a1069140a5af
 ---> 30095abacbeb
Removing intermediate container a1069140a5af
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2237ef928f68
 ---> 97b82f088ebe
Removing intermediate container 2237ef928f68
Step 14/14 : USER [secure]
 ---> Running in 3e940d9ef66e
 ---> 0bdfa8230a85
Removing intermediate container 3e940d9ef66e
Successfully built 0bdfa8230a85
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f45929668d4ff51c7a03ead8d8c33b26222d106b708047ec43214a00ae3dd34e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:f278cbb3c5ccb2957f49b337969e93f49d11fefda8e191274274174561fb2fa7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
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
travis_time:end:0e170e4a:start=1579694298188960969,finish=1579694509141196682,duration=210952235713,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0d1e1a73[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/640388652/log.txt)