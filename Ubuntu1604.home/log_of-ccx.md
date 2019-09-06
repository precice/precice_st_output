 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581674746) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/e95758ebfe65...18b4f9274e2d) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     19% |******                          | 4916k  0:00:42 ETA
[0m[91m-                     21% |******                          | 5417k  0:00:41 ETA
[0m[91m-                     23% |*******                         | 5988k  0:00:39 ETA
[0m[91m-                     25% |********                        | 6487k  0:00:38 ETA
[0m[91m-                     27% |********                        | 7026k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7567k  0:00:35 ETA
[0m[91m-                     31% |**********                      | 8092k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8632k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9143k  0:00:32 ETA
[0m[91m-                     37% |************                    | 9699k  0:00:31 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:30 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:29 ETA
[0m[91m-                     43% |**************                  | 11.0M  0:00:28 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:25 ETA[0m[91m
[0m[91m-                     50% |****************                | 12.5M  0:00:24 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:22 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:19 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:16 ETA
[0m[91m-                     68% |**********************          | 17.2M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.7M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 7ea5697927a8
Removing intermediate container 54d3c7f33e6a
Step 10/13 : WORKDIR /
 ---> 0102a2d712a4
Removing intermediate container 8592f54de7d0
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e10a45bb61ca
 ---> bd7b9a0e3803
Removing intermediate container e10a45bb61ca
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 42c41c9ec063
 ---> 24402610355a
Removing intermediate container 42c41c9ec063
Step 13/13 : USER [secure]
 ---> Running in b9a66fa82226
 ---> 70b925477326
Removing intermediate container b9a66fa82226
Successfully built 70b925477326
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
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:020beea2:start=1567777008084687313,finish=1567777413978693001,duration=405894005688,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1cab1d9d[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581674758/log.txt)