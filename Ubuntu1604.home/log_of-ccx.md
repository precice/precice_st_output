## Status: Passing 
Build: [1623](https://travis-ci.org/precice/systemtests/builds/647989489) 

Job: [1623.19](https://travis-ci.org/precice/systemtests/jobs/647989508) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     17% |*****                           | 4431k  0:00:47 ETA
[0m[91m-                     19% |******                          | 5047k  0:00:44 ETA
[0m[91m-                     21% |*******                         | 5619k  0:00:42 ETA
[0m[91m-                     24% |*******                         | 6193k  0:00:40 ETA
[0m[91m-                     26% |********                        | 6814k  0:00:38 ETA
[0m[91m-                     28% |*********                       | 7384k  0:00:37 ETA
[0m[91m-                     31% |*********                       | 7946k  0:00:35 ETA
[0m[91m-                     33% |**********                      | 8580k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9150k  0:00:32 ETA
[0m[91m-                    [0m[91m 38% |************                    | 9780k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:28 ETA
[0m[91m-                     45% |**************                  | 11.2M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:24 ETA
[0m[91m-                    [0m[91m 51% |****************                | [0m[91m13.0M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA[0m[91m
[0m[91m-                     58% |******************              | 14.7M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:18 ETA[0m[91m
[0m[91m-                     63% |********************            | 15.8M  0:00:17 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:11 ETA[0m[91m
[0m[91m-                     77% |************************        | 19.3M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.8M[0m[91m  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                    [0m[91m 93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:00 ETA
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
 ---> 9e6c4a5147bb
Removing intermediate container 40c263c65e5f
Step 11/14 : WORKDIR /
 ---> 691ddd75c09d
Removing intermediate container aeb756338e03
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7bce7625ec49
 ---> 165563b3c892
Removing intermediate container 7bce7625ec49
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0809e8f20fa8
 ---> fc2a13816c25
Removing intermediate container 0809e8f20fa8
Step 14/14 : USER [secure]
 ---> Running in 1bea672a8c92
 ---> e117cec11e40
Removing intermediate container 1bea672a8c92
Successfully built e117cec11e40
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:78f3861a694fedc4f3d0974b44ef5e5edf890039de3b77f73db8e8d2c6a261fd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:9f49fe73c80921ef7a8e5769d1c5988bebe037131b3bb0ed10756d087601a406
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
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
travis_time:end:04a7eb59:start=1581248868537478428,finish=1581249192072091698,duration=323534613270,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0a3fc650[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0a3fc650:start=1581249196663383690,finish=1581249198193241918,duration=1529858228,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:210edd28[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/647989508/log.txt)