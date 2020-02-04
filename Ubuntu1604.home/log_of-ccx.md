## Status: Passing 
Build: [1603](https://travis-ci.org/precice/systemtests/builds/646122956) 

Job: [1603.16](https://travis-ci.org/precice/systemtests/jobs/646122972) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646122956) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     48% |***************                 | 12.0M  0:00:28 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:20 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     71% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     81% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
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
 ---> db2ead9e1f55
Removing intermediate container 437572ed6502
Step 11/14 : WORKDIR /
 ---> 45b960e00435
Removing intermediate container 12116b494b0c
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 0cc3a704b411
 ---> 0da69fe1de16
Removing intermediate container 0cc3a704b411
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 10b6bcdaf791
 ---> 79ef377fcad0
Removing intermediate container 10b6bcdaf791
Step 14/14 : USER [secure]
 ---> Running in 16b60bac486b
 ---> d60ccfb13e19
Removing intermediate container 16b60bac486b
Successfully built d60ccfb13e19
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:72b3e3bb4c1db43896d6ca7bd81587cfce50fc735ba4f20791092f003beab7cb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:50013b7e1814a9420fbde5bcdbf460f447110b29ea921e0e99f45dcf2cec30a7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:2284efb3:start=1580851261348114028,finish=1580851533851573321,duration=272503459293,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0702b1d8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0702b1d8:start=1580851538032093497,finish=1580851539420394298,duration=1388300801,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:04b6577f[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646122972/log.txt)