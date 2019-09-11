 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583654671) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/318f6af1f707...32fdbbbc7d35) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                     18% |*****                           | 4727k  0:00:44 ETA
[0m[91m-                     20% |******                          | 5298k  0:00:42 ETA
[0m[91m-                     22% |*******                         | 5869k  0:00:40 ETA
[0m[91m-                     24% |*******                         | 6377k  0:00:39 ETA
[0m[91m-                     27% |********                        | 6934k  0:00:37 ETA
[0m[91m-                     29% |*********                       | 7498k  0:00:36 ETA
[0m[91m-                     31% [0m[91m|**********                      | 8077k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8620k  0:00:33 ETA
[0m[91m-                    [0m[91m 35% |***********                     | 9139k  0:00:32 ETA
[0m[91m-                     37% |************                    | 9716k  0:00:31 ETA
[0m[91m-                     38% |************                    | 9908k  0:00:31 ETA
[0m[91m-                    [0m[91m 40% [0m[91m|************                    | 10.0M  0:00:31 ETA
[0m[91m-                    [0m[91m 42% [0m[91m|*************                   | 10.5M  0:00:30 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:28 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:26 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.8M[0m[91m  0:00:22 ETA[0m[91m
[0m[91m-                     57% |******************              | 14.3M  0:00:21 ETA
[0m[91m-                     59% |******************              | 14.8M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:18 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% [0m[91m|******************************* | 24.3M  0:00:01 ETA
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
 ---> 1b4aa9d2c39a
Removing intermediate container d73138cb6c2c
Step 10/13 : WORKDIR /
 ---> c6c6b716f1aa
Removing intermediate container 8e58c52b3176
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 6f9a437e1c67
 ---> f77843890d06
Removing intermediate container 6f9a437e1c67
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 22bf3beed363
 ---> b6a966e8dfc6
Removing intermediate container 22bf3beed363
Step 13/13 : USER [secure]
 ---> Running in 200290c89e5d
 ---> 231ff11e169e
Removing intermediate container 200290c89e5d
Successfully built 231ff11e169e
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:895d26be6ec8aaef205e1ff89d7c86bd53b0def33da41d40b1175595d4cf74af
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:ccceae89533ea70c80a0e87297ae7cc3dd4b38c88fb53d4e67cb41b4675b2390
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:048468f0:start=1568210308994932697,finish=1568210656863325469,duration=347868392772,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:06fc07f0[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583654686/log.txt)