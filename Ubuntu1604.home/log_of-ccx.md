## Status: Passing 
Build: [1239](https://travis-ci.org/precice/systemtests/builds/619372101) 

Job: [1239.16](https://travis-ci.org/precice/systemtests/jobs/619372119) 

Triggered by: [push](https://github.com/precice/systemtests/compare/cf8e616f4d09...39aadec5ed5b) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     27% |********                        | 7057k  0:00:36 ETA
[0m[91m-                     29% |*********                       | 7606k  0:00:35 ETA
[0m[91m-                     31% |**********                      | 8137k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8691k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8862k  0:00:34 ETA
[0m[91m-                     35% |***********                     | 9183k  0:00:34 ETA
[0m[91m-                    [0m[91m 37% |***********                     | 9588k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:29 ETA
[0m[91m-                     46% [0m[91m|**************                  | 11.5M  0:00:28 ETA[0m[91m
[0m[91m-                     48% |***************                 | 12.0M  0:00:26 ETA
[0m[91m-                    [0m[91m 50% [0m[91m|****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M[0m[91m  0:00:08 ETA
[0m[91m-                     84% [0m[91m|**************************      | 21.1M  0:00:07 ETA
[0m[91m-                    [0m[91m 86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                    [0m[91m 92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.2M  0:00:01 ETA
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
 ---> 685c1e78fd54
Removing intermediate container afde0219042e
Step 11/14 : WORKDIR /
 ---> 89ff8b2e8f58
Removing intermediate container 43399fd62508
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 16d30561084f
 ---> 2f42f5baf6bf
Removing intermediate container 16d30561084f
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 76c09bc93095
 ---> 4c568c2b3006
Removing intermediate container 76c09bc93095
Step 14/14 : USER [secure]
 ---> Running in b865d3a2e004
 ---> 065b6463edfc
Removing intermediate container b865d3a2e004
Successfully built 065b6463edfc
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:70fe2faa72b2f0b36bebe52feee9ebbc2d8a68c08257a7c3fe32a7a746f8f227
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:cb9e751e559eb7451b60e08bf1b4564e9305cbb017696dc99bdf52617bb290c4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0f9920ae:start=1575245223160646219,finish=1575245566881242185,duration=343720595966,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07634da2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07634da2:start=1575245571508364811,finish=1575245573396459435,duration=1888094624,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1647deb1[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/619372119/log.txt)