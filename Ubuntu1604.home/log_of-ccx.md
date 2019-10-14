 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/597566138) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/01ea67b040c1...3ebec4464c61) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     16% |*****                           | 4264k  0:00:45 ETA
[0m[91m-                     18% |******                          | 4840k  0:00:42 ETA
[0m[91m-                     21% |******                          | 5402k  0:00:41 ETA
[0m[91m-                     23% |*******                         | 5951k  0:00:39 ETA
[0m[91m-                     23% |*******                         | 6026k  0:00:42 ETA
[0m[91m-                     25% |********                        | 6524k  0:00:40 ETA
[0m[91m-                     26% |********                        | 6693k  0:00:42 ETA
[0m[91m-                     27% |********                        | 7103k  0:00:41 ETA
[0m[91m-                     29% |*********                       | 7639k  0:00:40 ETA
[0m[91m-                     32% |**********                      | 8203k  0:00:38 ETA
[0m[91m-                     33% |**********                      | 8714k  0:00:36 ETA
[0m[91m-                     36% |***********                     | 9280k  0:00:35 ETA
[0m[91m-                     38% |************                    | 9849k  0:00:33 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:32 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.7M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:24 ETA
[0m[91m-                    [0m[91m 55% |*****************               | 13.9M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:20 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:17 ETA
[0m[91m-                     68% [0m[91m|*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.2M  0:00:13 ETA
[0m[91m-                    [0m[91m 75% |************************        | 18.7M  0:00:12 ETA[0m[91m
[0m[91m-                    [0m[91m 77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                    [0m[91m 88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                    [0m[91m 90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% [0m[91m|*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.7M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 73500bf5dd8a
Removing intermediate container 14bf34cfdcda
Step 10/13 : WORKDIR /
 ---> 7b9d1638b286
Removing intermediate container bb3449027c75
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 4dc8c2d5c3da
 ---> 94ed55dadf6a
Removing intermediate container 4dc8c2d5c3da
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 08a08de1d9d6
 ---> 4d246aa68f7f
Removing intermediate container 08a08de1d9d6
Step 13/13 : USER [secure]
 ---> Running in b7faf5e73956
 ---> 87ba82421cde
Removing intermediate container b7faf5e73956
Successfully built 87ba82421cde
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:cd80f1c307ee01d96ec423b7d65149139c623a220434f8605da3b9ac0c7122fe
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:5bc4bd19b2c588f1393af183d4baad9c44b6aef928f645cfbabd3170525b8c7e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:134534c3:start=1571052008706447053,finish=1571052357844909044,duration=349138461991,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0979989c[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/597566153/log.txt)