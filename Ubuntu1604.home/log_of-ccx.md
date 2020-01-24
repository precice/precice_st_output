## Status: Passing 
Build: [1484](https://travis-ci.org/precice/systemtests/builds/641298046) 

Job: [1484.20](https://travis-ci.org/precice/systemtests/jobs/641298078) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4c749ac41fec1ac0cc04f8e71fcd731e33705ab1...e37a006c80df4226e1d22b4d0f731f7780eae018) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     23% |*******                         | 5979k  0:00:46 ETA
[0m[91m-                     25% |********                        | 6597k[0m[91m  0:00:43 ETA[0m[91m
[0m[91m-                     27% |********                        | 7169k  0:00:41 ETA
[0m[91m-                     30% |*********                       | 7736k  0:00:39 ETA
[0m[91m-                     32% |**********                      | 8364k  0:00:37 ETA
[0m[91m-                     34% |***********                     | 8931k[0m[91m  0:00:35 ETA
[0m[91m-                     37% |***********                     | 9489k  0:00:34 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:29 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.7M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.6M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.1M[0m[91m  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M[0m[91m  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% [0m[91m|******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> b72e4afc8a73
Removing intermediate container fa92a02695a3
Step 11/14 : WORKDIR /
 ---> 50952b706035
Removing intermediate container f38d438691e1
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d717431f14f4
 ---> 42b226d9501d
Removing intermediate container d717431f14f4
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5414ac943992
 ---> 01eeed506db8
Removing intermediate container 5414ac943992
Step 14/14 : USER [secure]
 ---> Running in 0b361d740e85
 ---> dbc9589d383d
Removing intermediate container 0b361d740e85
Successfully built dbc9589d383d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:eed3979fbded39e8a23ede0f432ef6f195727d13ee124bb42462ecca63a1b1fe
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
Test succeeded! No difference to referenceOutput found.
travis_time:end:08cf138a:start=1579866574088534166,finish=1579866900124722662,duration=326036188496,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:11e84a81[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:11e84a81:start=1579866904254001720,finish=1579866905688760419,duration=1434758699,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:08d7f6a0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/641298078/log.txt)