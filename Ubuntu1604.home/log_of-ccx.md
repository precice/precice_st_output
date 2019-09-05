 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581225637) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/1ae3635d9a98...bde2eea33c21) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     21% |******                          | 5385k  0:00:41 ETA
[0m[91m-                     23% |*******                         | 5896k  0:00:40 ETA
[0m[91m-                     25% |********                        | 6473k  0:00:38 ETA
[0m[91m-                     27% |********                        | 7030k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7532k  0:00:36 ETA
[0m[91m-                     30% |*********                       | 7871k  0:00:36 ETA
[0m[91m-                     31% |**********                      | 8011k  0:00:37 ETA
[0m[91m-                     32% |**********                      | 8379k  0:00:37 ETA
[0m[91m-                     34% |**********                      | 8788k  0:00:36 ETA
[0m[91m-                     36% |***********                     | 9351k  0:00:34 ETA
[0m[91m-                     38% |************                    | [0m[91m9861k  0:00:33 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:32 ETA
[0m[91m-                    [0m[91m 42% |*************                   | [0m[91m10.6M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.7M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:27 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:25 ETA[0m[91m
[0m[91m-                     53% |*****************               | 13.3M  0:00:24 ETA
[0m[91m-                     55% [0m[91m|*****************               | 13.8M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.3M[0m[91m  0:00:22 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     65% |*********************           | 16.5M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 17.0M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:13 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                    [0m[91m 82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                    [0m[91m 86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                    [0m[91m 96% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 4d90f1e9a86e
Removing intermediate container d18b289e1ab8
Step 10/13 : WORKDIR /
 ---> a3605a93f79f
Removing intermediate container d454ffd4f7ba
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e60ac0ead868
 ---> ab29db59bf0a
Removing intermediate container e60ac0ead868
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in cd4587ed1537
 ---> 425b2d0a2b6f
Removing intermediate container cd4587ed1537
Step 13/13 : USER [secure]
 ---> Running in 3469c74c03f0
 ---> 74811adfd704
Removing intermediate container 3469c74c03f0
Successfully built 74811adfd704
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b97f3bf0742fa58bb2a132c5952c83d04958654227347d4ec3581e12ca675459
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03c92e1d:start=1567693014344631053,finish=1567693408940831161,duration=394596200108,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:19150670[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581225649/log.txt)