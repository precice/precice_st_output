## Status: Passing 
Build: [1000](https://travis-ci.org/precice/systemtests/builds/601988696) 

Job: [1000.15](https://travis-ci.org/precice/systemtests/jobs/601988711) 

Triggered by: [push](https://github.com/precice/systemtests/compare/500cfbb53a97...73300f5bea0c) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     17% |*****                           | 4600k  0:00:41 ETA
[0m[91m-                     20% |******                          | 5170k  0:00:39 ETA
[0m[91m-                     22% |*******                         | 5716k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6268k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6810k  0:00:35 ETA
[0m[91m-                     28% |*********                       | 7377k  0:00:34 ETA
[0m[91m-                     31% |*********                       | 7948k  0:00:33 ETA
[0m[91m-                     33% |**********                      | 8483k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 9055k  0:00:31 ETA
[0m[91m-                     36% |***********                     | 9404k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9576k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9910k  0:00:31 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:30 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:30 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:30 ETA
[0m[91m-                     45% |**************                  | 11.5M  0:00:29 ETA
[0m[91m-                     48% [0m[91m|***************                 | 12.0M  0:00:27 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:25 ETA
[0m[91m-                     54% [0m[91m|*****************               | 13.7M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:22 ETA
[0m[91m-                     59% |******************              | 14.7M  0:00:21 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:20 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                    [0m[91m 65% |*********************           | 16.4M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                    [0m[91m 93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 24.0M  0:00:02 ETA
[0m[91m-                     98% |******************************* | 24.5M  0:00:00 ETA
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
 ---> bdd8d86c7ae8
Removing intermediate container e9cb46933aac
Step 10/13 : WORKDIR /
 ---> fe018d889028
Removing intermediate container 058da2c267e5
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in a3c84a181acf
 ---> fc29c67178d9
Removing intermediate container a3c84a181acf
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7c4f69da6bb0
 ---> 43482d34228f
Removing intermediate container 7c4f69da6bb0
Step 13/13 : USER [secure]
 ---> Running in 6017210a7d30
 ---> 1bdbe2e79749
Removing intermediate container 6017210a7d30
Successfully built 1bdbe2e79749
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:800ef878bf82edef081068e05b4fbe89b92f4870c31a470ddb56147df1cb0d1d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e8fbb15f8b75071b703c355651cfa9df534583d456769e02fb938e433f92abb9
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0dcc91d0:start=1571863178835017780,finish=1571863532324937813,duration=353489920033,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1c3148a0[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/601988711/log.txt)