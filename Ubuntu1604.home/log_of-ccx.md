 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599707111) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/677b242d01cf...3df000d61aa4) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     18% |*****                           | 4756k  0:00:43 ETA
[0m[91m-                     20% |******                          | 5316k  0:00:42 ETA
[0m[91m-                     22% |*******                         | 5853k  0:00:40 ETA
[0m[91m-                     25% |********                        | 6427k  0:00:38 ETA
[0m[91m-                     27% |********                        | 6956k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7529k  0:00:36 ETA
[0m[91m-                     31% |**********                      | 8060k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8639k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9192k  0:00:32 ETA[0m[91m
[0m[91m-                     38% |************                    | 9740k  0:00:30 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:29 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:28 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:26 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:25 ETA
[0m[91m-                     51% |****************                | 12.7M  0:00:24 ETA
[0m[91m-                     53% |****************                | 13.2M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.8M  0:00:19 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M[0m[91m  0:00:12 ETA[0m[91m
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     81% |*************************       | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 23.0M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     96% |******************************  | 24.2M  0:00:01 ETA
[0m[91m-                    [0m[91m 97% [0m[91m|******************************* | 24.5M  0:00:00 ETA[0m[91m
[0m[91m-                     99% |******************************* | [0m[91m24.9M  0:00:00 ETA
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
 ---> 8b1d52e6aa93
Removing intermediate container 10fa5b565099
Step 10/13 : WORKDIR /
 ---> 9c690a86f04a
Removing intermediate container 6e26fe64c911
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 5ba781968522
 ---> c252b49dcf32
Removing intermediate container 5ba781968522
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 56e81dab549e
 ---> 24db312263ae
Removing intermediate container 56e81dab549e
Step 13/13 : USER [secure]
 ---> Running in 7e6add553941
 ---> a184c0d50cd0
Removing intermediate container 7e6add553941
Successfully built a184c0d50cd0
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:4261dc44e3bc0dd4adc2106659a59ee75ed8b466e28a745e1d0278ff73773f96
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:086c760992a034ec05167871d818a4724f12564e43453b7eee24b0b92e3ff1dd
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0056c098:start=1571417401068697449,finish=1571417808151469161,duration=407082771712,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1406d260[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599707126/log.txt)