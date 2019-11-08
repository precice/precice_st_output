## Status: Passing 
Build: [1061](https://travis-ci.org/precice/systemtests/builds/609034257) 

Job: [1061.19](https://travis-ci.org/precice/systemtests/jobs/609034276) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     27% |********                        | 7124k  0:00:36 ETA
[0m[91m-                     29% |*********                       | 7632k  0:00:35 ETA
[0m[91m-                     32% |**********                      | 8203k  0:00:33 ETA
[0m[91m-                     33% |**********                      | 8468k  0:00:34 ETA
[0m[91m-                     33% |**********                      | 8683k  0:00:35 ETA
[0m[91m-                    [0m[91m 35% |***********                     | 9007k  0:00:35 ETA
[0m[91m-                     37% |***********                     | 9508k  0:00:33 ETA
[0m[91m-                     37% |************                    | 9695k  0:00:34 ETA
[0m[91m-                     38% |************                    | 9988k  0:00:34 ETA
[0m[91m-                     40% |************                    | 10.1M  0:00:33 ETA
[0m[91m-                    [0m[91m 42% |*************                   | 10.6M  0:00:32 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:30 ETA[0m[91m
[0m[91m-                     47% |***************                 | 11.7M  0:00:29 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:28 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:26 ETA
[0m[91m-                     53% [0m[91m|*****************               | 13.3M  0:00:25 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:22 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:21 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:20 ETA
[0m[91m-                     64% [0m[91m|********************            | 16.0M  0:00:19 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:17 ETA[0m[91m
[0m[91m-                     68% |*********************           | 17.1M  0:00:16 ETA
[0m[91m-                    [0m[91m 70% |**********************          | 17.7M  0:00:15 ETA[0m[91m
[0m[91m-                     72% |***********************         | 18.1M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:13 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:11 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                    [0m[91m 93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.5M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
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
 ---> 762b3e98d68b
Removing intermediate container f01a3a71e77b
Step 10/13 : WORKDIR /
 ---> 796b3a6695d1
Removing intermediate container 3bb0de750e31
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 17eec11e5e01
 ---> 87880853a085
Removing intermediate container 17eec11e5e01
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fc16b57e6c2d
 ---> f354b064c9a0
Removing intermediate container fc16b57e6c2d
Step 13/13 : USER [secure]
 ---> Running in 052455a87dd6
 ---> 68bcb20d16ff
Removing intermediate container 052455a87dd6
Successfully built 68bcb20d16ff
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0df5ddcdd2fbe3eb36701daa030517b98e10ce7531c23f062b5175b29302c75e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:84c63b8f2c83b99dac5bb0e0182a115eec821f5402aef7019bcc6b768a26fd90
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0bdce9ce:start=1573181014048172909,finish=1573181427333920277,duration=413285747368,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1b502330[0K$ python push.py -s -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/609034276/log.txt)