 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599812595) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/efe9b440d9b6...4b854cdf2c7b) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     15% |*****                           | 4022k  0:00:42 ETA
[0m[91m-                     17% |*****                           | 4592k  0:00:41 ETA
[0m[91m-                     20% |******                          | 5130k  0:00:39 ETA
[0m[91m-                     22% |*******                         | 5692k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6225k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6800k  0:00:35 ETA
[0m[91m-                     28% |*********                       | 7364k  0:00:34 ETA
[0m[91m-                     30% |*********                       | 7900k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8435k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 9007k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9569k  0:00:30 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:28 ETA
[0m[91m-                     43% |**************                  | 10.9M  0:00:26 ETA
[0m[91m-                     45% |**************                  | 11.5M  0:00:25 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:24 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:23 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:22 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:21 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.7M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:17 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:16 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 25.0M  0:00:00 ETA
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
 ---> 74b3db8123a2
Removing intermediate container 65fbaf22d7fd
Step 10/13 : WORKDIR /
 ---> a0145a209c2d
Removing intermediate container 5757d32c7247
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in df72f9cc974d
 ---> 99cec3ee9dad
Removing intermediate container df72f9cc974d
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 153e92756fd3
 ---> 384c2b63b3cb
Removing intermediate container 153e92756fd3
Step 13/13 : USER [secure]
 ---> Running in 4f67cf7c0e02
 ---> 555d45650e4d
Removing intermediate container 4f67cf7c0e02
Successfully built 555d45650e4d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:638bd8696638781aae21b0324d5a14efc491bdf6c87e6a10c25cbaa293bf9a92
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:5c5893cdeddb7a611d3ca8329ad0c3427690f896db9cb513cb99d67f8837d36e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0d07ae1f:start=1571436113127732454,finish=1571436516468924836,duration=403341192382,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:01bf831c[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599812610/log.txt)