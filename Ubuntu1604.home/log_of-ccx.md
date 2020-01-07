## Status: Failure 
Build: [1398](https://travis-ci.org/precice/systemtests/builds/633704741) 

Job: [1398.20](https://travis-ci.org/precice/systemtests/jobs/633704761) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     19% |******                          | 5011k  0:00:45 ETA
[0m[91m-                     21% |******                          | 5581k  0:00:43 ETA
[0m[91m-                     24% |*******                         | 6207k  0:00:40 ETA
[0m[91m-                     26% |********                        | 6786k  0:00:38 ETA
[0m[91m-                     27% |********                        | 7128k  0:00:38 ETA
[0m[91m-                     28% |*********                       | 7430k  0:00:39 ETA
[0m[91m-                     30% |*********                       | 7894k  0:00:38 ETA
[0m[91m-                     33% |**********                      | 8458k  0:00:36 ETA
[0m[91m-                     35% |***********                     | 9090k  0:00:34 ETA
[0m[91m-                     37% |************                    | 9653k  0:00:33 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:28 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:23 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M[0m[91m  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M[0m[91m  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
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
 ---> 98154457756f
Removing intermediate container e5d47bfac8b8
Step 11/14 : WORKDIR /
 ---> dd5b5aa2a8c7
Removing intermediate container 139549fed97c
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 74a63ca2c32c
 ---> a7324c89891c
Removing intermediate container 74a63ca2c32c
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in af02be5b2e93
 ---> 5e44a68791d2
Removing intermediate container af02be5b2e93
Step 14/14 : USER [secure]
 ---> Running in 86b9eb798430
 ---> bc5f705e8458
Removing intermediate container 86b9eb798430
Successfully built bc5f705e8458
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d90f6de2b144d3d3cc1da4103640c3b0e9783b5d23c505e6ff7d36dd3150c640
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:3673422f6b1f22cd6604758f62b83a72aa7edffcd277292560a518fe315b820e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
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

```
[
Full job log](https://api.travis-ci.org/v3/job/633704761/log.txt)