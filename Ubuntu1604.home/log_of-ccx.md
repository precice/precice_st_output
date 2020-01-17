## Status: Failure 
Build: [1468](https://travis-ci.org/precice/systemtests/builds/638588714) 

Job: [1468.16](https://travis-ci.org/precice/systemtests/jobs/638588730) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/128) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     26% |********                        | 6727k  0:00:42 ETA
[0m[91m-                     28% |*********                       | 7292k  0:00:40 ETA
[0m[91m-                     30% |*********                       | 7796k  0:00:38 ETA
[0m[91m-                     32% |**********                      | 8367k  0:00:37 ETA
[0m[91m-                     34% |***********                     | 8929k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9427k  0:00:34 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:32 ETA
[0m[91m-                     40% |*************                   | 10.2M  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:30 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     59% |*******************             | [0m[91m14.9M  0:00:20 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     81% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA[0m[91m
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
 ---> a384da6c3f19
Removing intermediate container 61ef9b96ff3f
Step 11/14 : WORKDIR /
 ---> fa9220cd0a66
Removing intermediate container 80a3555d3b70
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 4e2050771287
 ---> 383a66f37ba6
Removing intermediate container 4e2050771287
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c7bd66418391
 ---> c8c4b0be2e39
Removing intermediate container c7bd66418391
Step 14/14 : USER [secure]
 ---> Running in 3955c6dcb0fe
 ---> 2d0963a253a7
Removing intermediate container 3955c6dcb0fe
Successfully built 2d0963a253a7
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c0ab392f39f60cb340c0bd5ee24119c2aa714c2b6ee94579e6618411be32e2cb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b9897b21c9ee52f7be611723de3cd47f9ec7fe68b59ae3a9d4ac58d5c0031ebd
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
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
travis_time:end:0bbedcb9:start=1579291380190091773,finish=1579291589978339623,duration=209788247850,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0f1bba22[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/638588730/log.txt)