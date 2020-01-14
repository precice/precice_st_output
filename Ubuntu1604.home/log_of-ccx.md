## Status: Failure 
Build: [1454](https://travis-ci.org/precice/systemtests/builds/636821308) 

Job: [1454.20](https://travis-ci.org/precice/systemtests/jobs/636821328) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     20% |******                          | 5139k  0:00:39 ETA
[0m[91m-                     22% |*******                         | 5708k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6267k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6899k  0:00:35 ETA
[0m[91m-                     29% |*********                       | 7473k  0:00:34 ETA
[0m[91m-                     31% |**********                      | 8045k  0:00:32 ETA
[0m[91m-                     33% |**********                      | 8662k  0:00:31 ETA
[0m[91m-                     36% |***********                     | 9235k  0:00:30 ETA
[0m[91m-                     38% |************                    | 9806k  0:00:29 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:27 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:25 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:24 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:21 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:20 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:19 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:18 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:17 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:15 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:06 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:05 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:03 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:02 ETA
[0m[91m-                     95% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> fc569fdefec4
Removing intermediate container b1f3fc2fc73e
Step 11/14 : WORKDIR /
 ---> 94d4dd09780a
Removing intermediate container 8467bb587b21
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 9bdabf7a9e3b
 ---> c7b280e4a650
Removing intermediate container 9bdabf7a9e3b
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 43f63079f729
 ---> d20143c153da
Removing intermediate container 43f63079f729
Step 14/14 : USER [secure]
 ---> Running in 0edeb5ff1f63
 ---> b628b28f4315
Removing intermediate container 0edeb5ff1f63
Successfully built b628b28f4315
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7f404ee162f678abc384ee6f4bcfd7b81bb96c62c2146ea43bff1252aeba2caa
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0d7a2fc29952047bd268fbe8e17040d6780397999981f13626163bc17ad02455
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
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
travis_time:end:12bb0821:start=1579001607742989865,finish=1579001815639773656,duration=207896783791,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:14b83223[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/636821328/log.txt)