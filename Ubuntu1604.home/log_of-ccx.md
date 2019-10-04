 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593511816) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/ac9e17230162...f01784f81bb4) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     19% |******                          | 4894k  0:00:42 ETA
[0m[91m-                     20% |******                          | 5338k  0:00:41 ETA
[0m[91m-                     21% |******                          | 5497k  0:00:43 ETA
[0m[91m-                     22% |*******                         | 5840k  0:00:44 ETA
[0m[91m-                    [0m[91m 24% [0m[91m|*******                         | 6348k  0:00:42 ETA
[0m[91m-                     27% |********                        | 6925k  0:00:40 ETA
[0m[91m-                     29% |*********                       | 7481k  0:00:38 ETA
[0m[91m-                    [0m[91m 31% [0m[91m|*********                       | [0m[91m7991k  0:00:37 ETA
[0m[91m-                    [0m[91m 33% |**********                      | 8550k  0:00:35 ETA
[0m[91m-                     35% |***********                     | 9126k  0:00:34 ETA
[0m[91m-                    [0m[91m 37% [0m[91m|************                    | 9692k  0:00:32 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.2M  0:00:31 ETA
[0m[91m-                     41% |*************                   | 10.4M[0m[91m  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:31 ETA
[0m[91m-                    [0m[91m 45% |**************                  | 11.3M  0:00:30 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:22 ETA
[0m[91m-                     60% |*******************             | 15.1M[0m[91m  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:19 ETA[0m[91m
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% [0m[91m|***********************         | 18.3M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:11 ETA[0m[91m
[0m[91m-                     79% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     84% |**************************      | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M[0m[91m  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% [0m[91m|********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 7db85d69ba67
Removing intermediate container edca53c4b684
Step 10/13 : WORKDIR /
 ---> 80286f7194c4
Removing intermediate container 766f6f642e8d
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 00d4307a66f6
 ---> 7f47c3a2d474
Removing intermediate container 00d4307a66f6
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c673b51e68dd
 ---> dd22576d44ef
Removing intermediate container c673b51e68dd
Step 13/13 : USER [secure]
 ---> Running in 06fc014cddce
 ---> 92b1c505b258
Removing intermediate container 06fc014cddce
Successfully built 92b1c505b258
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:71cf2104d8b90a360452bb8556fdfe9f26c55b8d7e439f142a34ae66d2e35bf7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:31a20adeb285aade96cee5f364662fd988f81ade309a561d0a0e83d076e58cd7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:26ef9de0:start=1570204148968412333,finish=1570204499985842633,duration=351017430300,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:04b9da92[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593511834/log.txt)