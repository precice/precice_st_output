## Status: Passing 
Build: [1520](https://travis-ci.org/precice/systemtests/builds/641980444) 

Job: [1520.20](https://travis-ci.org/precice/systemtests/jobs/641980464) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     42% |*************                   | 10.5M  0:00:25 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:24 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:23 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:22 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:21 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:20 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:19 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:18 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:17 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:16 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:15 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:11 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M[0m[91m  0:00:08 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
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
 ---> 16da907a2727
Removing intermediate container 4a07809f966a
Step 11/14 : WORKDIR /
 ---> 55419f471acd
Removing intermediate container 8105d3bad643
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d77e9b25c02e
 ---> 3a435299c8ea
Removing intermediate container d77e9b25c02e
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ed37422cafc0
 ---> 2365039e1caa
Removing intermediate container ed37422cafc0
Step 14/14 : USER [secure]
 ---> Running in e7ea235b531f
 ---> a171817ea47d
Removing intermediate container e7ea235b531f
Successfully built a171817ea47d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:a75d4bfff6af02cc2b843e66159d1d66a2273e84224bce5a82273feb54bfeca0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4631907828a700b11554568e7a59c3d1b25032657373a9801cffe18ff92c7e6e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:06bd52cc:start=1580039815065790137,finish=1580040080774795726,duration=265709005589,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0e7d899a:start=1580040084724403067,finish=1580040086041524984,duration=1317121917,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:240632d9[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/641980464/log.txt)