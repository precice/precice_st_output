 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581212684) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                      8% |**                              | 2139k  0:00:54 ETA
[0m[91m-                     10% |***                             | 2677k  0:00:51 ETA
[0m[91m-                     12% |****                            | 3211k  0:00:48 ETA
[0m[91m-                     14% |****                            | 3781k  0:00:46 ETA
[0m[91m-                     16% |*****                           | 4311k  0:00:44 ETA
[0m[91m-                     18% |******                          | 4851k  0:00:42 ETA
[0m[91m-                     21% |******                          | 5415k  0:00:41 ETA
[0m[91m-                     23% |*******                         | 5984k  0:00:39 ETA
[0m[91m-                     25% |********                        | 6486k  0:00:38 ETA
[0m[91m-                     27% |********                        | 7050k  0:00:36 ETA
[0m[91m-                     29% |*********                       | 7618k  0:00:35 ETA
[0m[91m-                     31% |**********                      | 8164k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8697k  0:00:33 ETA
[0m[91m-                     36% |***********                     | 9256k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9811k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                    [0m[91m 42% [0m[91m|*************                   | 10.6M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.7M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:18 ETA
[0m[91m-                     63% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:08 ETA[0m[91m
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     96% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
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
 ---> 114bd642e15c
Removing intermediate container 96225a8aae19
Step 10/13 : WORKDIR /
 ---> 04027e4a143b
Removing intermediate container 703eea163860
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 1f6c46d15c2d
 ---> ec9f60662d83
Removing intermediate container 1f6c46d15c2d
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 80017460e2cd
 ---> a1834a89526c
Removing intermediate container 80017460e2cd
Step 13/13 : USER [secure]
 ---> Running in 1c226b79c114
 ---> c79594c1fcf0
Removing intermediate container 1c226b79c114
Successfully built c79594c1fcf0
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:be8e37fe141c3aebfdaea18d27b3ffa9ef98fadcfc17a3167f5925fc0e3dc0ea
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b97f3bf0742fa58bb2a132c5952c83d04958654227347d4ec3581e12ca675459
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/581212696/log.txt)