 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/591102069) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/887c8e1583c8^...46a3f0d5dc83) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     22% |*******                         | 5639k  0:00:46 ETA
[0m[91m-                     24% |*******                         | 6198k  0:00:43 ETA
[0m[91m-                     26% |********                        | 6715k  0:00:42 ETA
[0m[91m-                     28% |*********                       | 7271k  0:00:40 ETA
[0m[91m-                     30% |*********                       | 7842k  0:00:38 ETA
[0m[91m-                     32% |**********                      | 8405k  0:00:36 ETA
[0m[91m-                     34% |***********                     | 8912k  0:00:35 ETA
[0m[91m-                     36% |***********                     | 9478k  0:00:34 ETA
[0m[91m-                     39% |************                    |  9.8M  0:00:32 ETA
[0m[91m-                    [0m[91m 41% |*************                   | 10.3M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:30 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:28 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:27 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.0M  0:00:23 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:18 ETA
[0m[91m-                     67% |*********************           | 16.7M  0:00:17 ETA
[0m[91m-                     69% [0m[91m|**********************          | 17.3M  0:00:16 ETA
[0m[91m-                     71% |**********************          | 17.8M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 18.9M  0:00:12 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.5M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     88% [0m[91m|****************************    | 22.0M  0:00:06 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:05 ETA
[0m[91m-                     92% |*****************************   | 23.0M  0:00:04 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                    [0m[91m 96% [0m[91m|******************************  | 24.1M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    [0m[91m100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 0e6c080d629b
Removing intermediate container 38b87a89d1d0
Step 10/13 : WORKDIR /
 ---> ad6fccbf2e81
Removing intermediate container ff088de3af29
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in dc0c19a0f546
 ---> e49d3eaea7f9
Removing intermediate container dc0c19a0f546
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 270123012c89
 ---> 8095c204fa22
Removing intermediate container 270123012c89
Step 13/13 : USER [secure]
 ---> Running in ea6869bf3e12
 ---> 871ab72ecaae
Removing intermediate container ea6869bf3e12
Successfully built 871ab72ecaae
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1a0c04933b6b2e3ee94062e56f4f3ec75051cdfd9e4225a98902526ee5e64525
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:ed0a09984e7b01b20177ad00cd47d92b36427f3274b6cccd0b6154eae76789d8
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0c0beed8:start=1569766627560657659,finish=1569767046419399421,duration=418858741762,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:17b98720[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/591102084/log.txt)