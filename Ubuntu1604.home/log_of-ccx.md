## Status: Passing 
Build: [1071](https://travis-ci.org/precice/systemtests/builds/610072373) 

Job: [1071.15](https://travis-ci.org/precice/systemtests/jobs/610072390) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ffab6e4cf6eb...2e77de77c876) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     10% |***                             | 2599k  0:01:02 ETA
[0m[91m-                     11% |***                             | 3013k  0:01:00 ETA
[0m[91m-                     13% |****                            | 3553k  0:00:55 ETA
[0m[91m-                     16% |*****                           | 4124k  0:00:52 ETA
[0m[91m-                     18% |*****                           | 4631k  0:00:49 ETA
[0m[91m-                    [0m[91m 20% [0m[91m|******                          | 5196k  0:00:47 ETA
[0m[91m-                     22% |*******                         | 5763k  0:00:44 ETA
[0m[91m-                     24% |*******                         | 6332k  0:00:42 ETA
[0m[91m-                     26% |********                        | 6900k  0:00:40 ETA
[0m[91m-                     28% |*********                       | 7408k  0:00:39 ETA
[0m[91m-                     31% |*********                       | 7980k  0:00:37 ETA
[0m[91m-                     33% [0m[91m|**********                      | 8549k  0:00:35 ETA
[0m[91m-                     35% |***********                     | 9107k  0:00:34 ETA
[0m[91m-                     37% |************                    | 9620k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:31 ETA
[0m[91m-                     41% [0m[91m|*************                   | 10.5M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:29 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:28 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:26 ETA
[0m[91m-                    [0m[91m 50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                    [0m[91m 59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.4M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M[0m[91m  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.5M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M[0m[91m  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% [0m[91m|***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% [0m[91m|****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 86d6d8af551b
Removing intermediate container 4e8b459df331
Step 10/13 : WORKDIR /
 ---> 50ba31d925e4
Removing intermediate container 42f3c78fed60
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d915a9a762d7
 ---> f90dbca0cc72
Removing intermediate container d915a9a762d7
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 63e4746ee686
 ---> ba8b1c16cc24
Removing intermediate container 63e4746ee686
Step 13/13 : USER [secure]
 ---> Running in 5a8d127e934d
 ---> ffeb7757d6b8
Removing intermediate container 5a8d127e934d
Successfully built ffeb7757d6b8
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:98e7b7fde8bd6b618c7ffe6b7ed9cd847d62e94c024d4c0ecdbd1eb70a3db786
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:150441b2553ec18c0e0243cef43db9f7fa116d3c9fcb49bfdd3d0022e39f5911
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0754ca34:start=1573425383102447841,finish=1573425730773146473,duration=347670698632,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:06192114[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl

```
[
Full job log](https://api.travis-ci.org/v3/job/610072390/log.txt)