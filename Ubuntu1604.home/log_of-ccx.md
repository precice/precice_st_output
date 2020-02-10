## Status: Passing 
Build: [1650](https://travis-ci.org/precice/systemtests/builds/648350351) 

Job: [1650.19](https://travis-ci.org/precice/systemtests/jobs/648350370) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     24% |*******                         | 6215k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6796k  0:00:36 ETA
[0m[91m-                     28% |*********                       | 7359k  0:00:34 ETA
[0m[91m-                     31% |*********                       | 7965k  0:00:33 ETA
[0m[91m-                    [0m[91m 33% |**********                      | 8557k  0:00:31 ETA
[0m[91m-                     35% |***********                     | 9159k  0:00:30 ETA
[0m[91m-                     38% |************                    | 9762k  0:00:29 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:28 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:26 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:25 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:25 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:25 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:24 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.7M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA
[0m[91m-                     59% |*******************             | [0m[91m14.9M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:18 ETA
[0m[91m-                    [0m[91m 64% |********************            | 16.1M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                     68% [0m[91m|**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                    [0m[91m 85% |***************************     | 21.3M  0:00:06 ETA[0m[91m
[0m[91m-                     87% |***************************     | 21.8M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M[0m[91m  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA
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
 ---> 9827bb91c90a
Removing intermediate container a158d34c1ee5
Step 11/14 : WORKDIR /
 ---> edad915a1261
Removing intermediate container ea7786d9a290
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in a11751d05119
 ---> ac2345ef061d
Removing intermediate container a11751d05119
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7939b589f912
 ---> be9478403754
Removing intermediate container 7939b589f912
Step 14/14 : USER [secure]
 ---> Running in ae190adef58e
 ---> 761d29c7d5df
Removing intermediate container ae190adef58e
Successfully built 761d29c7d5df
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f4a35c80e3584b3e11b7da5bf50b88da768fe5fe965b027645946b3c174412f9
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4d3263df1c58bb3dd8415f94b55cfb863c642b1a9d129faf515782cb6ef27d5c
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
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:32a04a5e:start=1581335257958794703,finish=1581335584716627993,duration=326757833290,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0669309e[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0669309e:start=1581335589414040579,finish=1581335590962523100,duration=1548482521,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2574652e[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/648350370/log.txt)