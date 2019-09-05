 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581212664) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/b9bb696f2d2c...1ae3635d9a98) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     18% |*****                           | 4666k  0:00:40 ETA
[0m[91m-                     20% |******                          | 5176k  0:00:39 ETA
[0m[91m-                     22% |*******                         | 5736k  0:00:38 ETA
[0m[91m-                     24% |*******                         | 6246k  0:00:37 ETA
[0m[91m-                     26% |********                        | 6830k  0:00:35 ETA
[0m[91m-                     28% |*********                       | 7334k  0:00:34 ETA
[0m[91m-                    [0m[91m 30% [0m[91m|*********                       | 7893k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8407k  0:00:32 ETA
[0m[91m-                     35% |***********                     | 8971k  0:00:31 ETA
[0m[91m-                     37% |***********                     | 9522k  0:00:30 ETA
[0m[91m-                     39% [0m[91m|************                    |  9.8M  0:00:29 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:28 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:27 ETA
[0m[91m-                     45% [0m[91m|**************                  | 11.4M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:24 ETA[0m[91m
[0m[91m-                     51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% [0m[91m|*****************               | 13.5M  0:00:22 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:21 ETA[0m[91m
[0m[91m-                     57% |******************              | 14.2M  0:00:21 ETA
[0m[91m-                     58% |******************              | 14.5M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                    [0m[91m 61% [0m[91m|*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     63% |********************            | [0m[91m16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:16 ETA[0m[91m
[0m[91m-                     68% |*********************           | 17.0M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:14 ETA
[0m[91m-                     72% [0m[91m|***********************         | 18.0M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA[0m[91m
[0m[91m-                     87% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> 6629cd1af4ce
Removing intermediate container 697b24652794
Step 10/13 : WORKDIR /
 ---> c19877723106
Removing intermediate container d4beac2c5f19
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d4f64c43ecd1
 ---> 617fbd4c8e04
Removing intermediate container d4f64c43ecd1
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b114e14be31b
 ---> f06b305d0396
Removing intermediate container b114e14be31b
Step 13/13 : USER [secure]
 ---> Running in f5503e2c8630
 ---> 2fc7770d03ca
Removing intermediate container f5503e2c8630
Successfully built 2fc7770d03ca
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e4ceba9207e6feb6ba7b138c24c9fcf8811fbdf85c4fdb6ce35ca4f26b272e3a
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:01ec7dc4:start=1567691602910223293,finish=1567691995623297026,duration=392713073733,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00dd6160[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581212676/log.txt)