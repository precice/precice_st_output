## Status: Failure 
Build: [1575](https://travis-ci.org/precice/systemtests/builds/644736951) 

Job: [1575.16](https://travis-ci.org/precice/systemtests/jobs/644736967) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/167) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     23% |*******                         | 6079k  0:00:38 ETA
[0m[91m-                     25% |********                        | 6617k  0:00:37 ETA
[0m[91m-                     28% |********                        | 7181k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7740k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8320k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8845k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9384k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9954k  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.2M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.5M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
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
 ---> 7b4e0a506400
Removing intermediate container 6008d61d09d3
Step 11/14 : WORKDIR /
 ---> fa10c192be6a
Removing intermediate container 715426d4435e
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 759b1f97d038
 ---> 8b22e195e3b9
Removing intermediate container 759b1f97d038
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 4a6d6301e050
 ---> 40cd438bd40a
Removing intermediate container 4a6d6301e050
Step 14/14 : USER [secure]
 ---> Running in 53734329e15e
 ---> c7e44f07c3eb
Removing intermediate container 53734329e15e
Successfully built c7e44f07c3eb
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f0f925358b4c286a42eda5797d10433dd43d09bca66de4c5787bf3ea780166bd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:27094d5caf272586659f8cb1ea41a684f49f31b67652274c39be8c8576ecc01f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:050a3c2f:start=1580563551468877118,finish=1580563757233853590,duration=205764976472,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:23ac5838[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/644736967/log.txt)