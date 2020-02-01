## Status: Failure 
Build: [1574](https://travis-ci.org/precice/systemtests/builds/644725337) 

Job: [1574.19](https://travis-ci.org/precice/systemtests/jobs/644725356) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4999f333493e1d71bc360afa644a77d2630ce82e...b42adf2e689a763071326fd2ccb4fad54589f1aa) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     25% |********                        | 6551k  0:00:37 ETA
[0m[91m-                     27% |********                        | 7080k  0:00:36 ETA
[0m[91m-                     29% |*********                       | 7614k  0:00:35 ETA
[0m[91m-                     31% |**********                      | 8146k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8709k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9220k  0:00:32 ETA
[0m[91m-                     38% |************                    | 9792k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:24 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:20 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     71% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% [0m[91m|*****************************   | 22.7M  0:00:04 ETA
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
 ---> 940072dcadaf
Removing intermediate container ddf7a2f10916
Step 11/14 : WORKDIR /
 ---> 62ce9467825a
Removing intermediate container 9450d4d22ecf
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 9445f91d9aca
 ---> 9cc562d29d10
Removing intermediate container 9445f91d9aca
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 421dbbb58225
 ---> 829dedda8ef3
Removing intermediate container 421dbbb58225
Step 14/14 : USER [secure]
 ---> Running in 032f0190c295
 ---> eccd08c461f1
Removing intermediate container 032f0190c295
Successfully built eccd08c461f1
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
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
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
travis_time:end:0232aeb8:start=1580557690261405150,finish=1580557896847808847,duration=206586403697,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0530a80a[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/644725356/log.txt)