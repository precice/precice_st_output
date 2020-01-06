## Status: Failure 
Build: [1397](https://travis-ci.org/precice/systemtests/builds/633228536) 

Job: [1397.20](https://travis-ci.org/precice/systemtests/jobs/633228556) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     25% |********                        | 6431k  0:00:38 ETA
[0m[91m-                     27% |********                        | 6989k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7527k  0:00:36 ETA
[0m[91m-                     31% |**********                      | 8068k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8639k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9208k  0:00:32 ETA
[0m[91m-                     38% |************                    | 9742k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.7M  0:00:24 ETA
[0m[91m-                     53% |****************                | 13.2M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA
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
 ---> ef4d38fce04e
Removing intermediate container 4af459abfbec
Step 11/14 : WORKDIR /
 ---> 22c19c866e78
Removing intermediate container 2c6244571e55
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 3e30abeb0c3a
 ---> b12792d7c160
Removing intermediate container 3e30abeb0c3a
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0d45c2debfa5
 ---> 0e006769ddd3
Removing intermediate container 0d45c2debfa5
Step 14/14 : USER [secure]
 ---> Running in 4f696361152b
 ---> 9e08fd5dea98
Removing intermediate container 4f696361152b
Successfully built 9e08fd5dea98
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0553b4dbaaf216bec05bfdfc2c695b344d3c95e49c15ab1baa33c7fe8ebdc93f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:af37c082c1f91ebc7c02ce104fbdce63be888243364264b44e562458c4fb60f6
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
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
travis_time:end:2151ce50:start=1578310220199574693,finish=1578310426525407224,duration=206325832531,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:01597fbe[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/633228556/log.txt)