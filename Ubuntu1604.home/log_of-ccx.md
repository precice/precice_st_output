 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/597589850) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3ebec4464c61...546279f1ebbf) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     17% |*****                           | 4457k  0:00:42 ETA
[0m[91m-                     19% |******                          | [0m[91m5028k  0:00:40 ETA
[0m[91m-                     21% |******                          | 5583k  0:00:39 ETA
[0m[91m-                     23% |*******                         | 6151k  0:00:38 ETA
[0m[91m-                    [0m[91m 25% |********                        | 6660k  0:00:37 ETA
[0m[91m-                     28% |*********                       | 7231k  0:00:35 ETA
[0m[91m-                     30% |*********                       | 7785k  0:00:34 ETA
[0m[91m-                     32% |**********                      | 8299k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8880k  0:00:32 ETA
[0m[91m-                     36% |***********                     | 9422k  0:00:30 ETA
[0m[91m-                     39% |************                    | 9997k  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.2M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:23 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:24 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 17.0M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% [0m[91m|***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% [0m[91m|****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     95% [0m[91m|******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:00 ETA
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
 ---> b9723121561e
Removing intermediate container 039600cf9a9d
Step 10/13 : WORKDIR /
 ---> 9462223c15b4
Removing intermediate container e0a8b693883f
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e9ef4bc7adb6
 ---> 1ff657df2734
Removing intermediate container e9ef4bc7adb6
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e52d3c776876
 ---> 10f34e453a69
Removing intermediate container e52d3c776876
Step 13/13 : USER [secure]
 ---> Running in 47ebf44d4284
 ---> 503f0d21db29
Removing intermediate container 47ebf44d4284
Successfully built 503f0d21db29
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:b9dd57649ccc64d335d03e613e3bbcd00960ff161c4c695cdce852282e836357
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:ebe45d1696d2bacf02a07a1bc88acc42111f5ef6028e90be3f2be31e1f01afe8
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0868a3fa:start=1571056068544515411,finish=1571056480290318469,duration=411745803058,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:028b70f5[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/597589867/log.txt)