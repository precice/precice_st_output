## Status: Passing 
Build: [978](https://travis-ci.org/precice/systemtests/builds/599812617) 

Job: [978.15](https://travis-ci.org/precice/systemtests/jobs/599812632) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     17% |*****                           | 4588k  0:00:45 ETA
[0m[91m-                     18% |******                          | 4809k  0:00:47 ETA
[0m[91m-                     20% |******                          | 5170k  0:00:47 ETA
[0m[91m-                     22% |*******                         | 5686k  0:00:45 ETA
[0m[91m-                     24% |*******                         | 6244k  0:00:43 ETA
[0m[91m-                     26% |********                        | 6828k  0:00:41 ETA
[0m[91m-                     28% |*********                       | [0m[91m7384k  0:00:39 ETA
[0m[91m-                     30% |*********                       | 7897k  0:00:38 ETA
[0m[91m-                     33% |**********                      | 8458k  0:00:36 ETA
[0m[91m-                     35% [0m[91m|***********                     | 9037k  0:00:34 ETA
[0m[91m-                    [0m[91m 37% [0m[91m|***********                     | 9596k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     43% [0m[91m|**************                  | 10.9M  0:00:29 ETA
[0m[91m-                    [0m[91m 46% [0m[91m|**************                  | 11.5M  0:00:28 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:26 ETA
[0m[91m-                     50% [0m[91m|****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:24 ETA
[0m[91m-                    [0m[91m 54% |*****************               | 13.6M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     59% |******************              | [0m[91m14.7M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M[0m[91m  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     88% [0m[91m|****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> bcebef17597f
Removing intermediate container 66a2ac73d7dc
Step 10/13 : WORKDIR /
 ---> 6428dc7f7c9a
Removing intermediate container 305c96306734
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in f2beaa8f4023
 ---> 36bf0f743e73
Removing intermediate container f2beaa8f4023
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c060e8084bb7
 ---> d5a71bb1e348
Removing intermediate container c060e8084bb7
Step 13/13 : USER [secure]
 ---> Running in 5bfc24bae726
 ---> 3cd01efb22c4
Removing intermediate container 5bfc24bae726
Successfully built 3cd01efb22c4
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:abc28e71defd133daf727eb6220447d4b2e15733a7d410a36239238646b31351
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:99d2f22fa80feda97102b66d730297da7669422086fab3867902a7c7ef4617ec
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1337ab1e:start=1571438572374497549,finish=1571438919687386423,duration=347312888874,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00d41f64[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/599812632/log.txt)