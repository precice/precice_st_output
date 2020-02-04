## Status: Passing 
Build: [1600](https://travis-ci.org/precice/systemtests/builds/645903423) 

Job: [1600.3](https://travis-ci.org/precice/systemtests/jobs/645903426) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/645903423) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     18% |******                          | 4838k  0:00:38 ETA
[0m[91m-                     21% |******                          | 5416k  0:00:37 ETA
[0m[91m-                     23% |*******                         | 6013k  0:00:35 ETA
[0m[91m-                     25% |********                        | 6608k  0:00:34 ETA
[0m[91m-                    [0m[91m 28% [0m[91m|********                        | 7183k  0:00:33 ETA
[0m[91m-                     30% |*********                       | 7791k  0:00:32 ETA
[0m[91m-                     32% |**********                      | 8377k  0:00:30 ETA
[0m[91m-                     34% |***********                     | 8948k  0:00:29 ETA
[0m[91m-                     37% |***********                     | 9547k  0:00:28 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:27 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:26 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:25 ETA
[0m[91m-                     46% |**************                  | 11.6M  0:00:24 ETA
[0m[91m-                     48% |***************                 | 12.1M  0:00:23 ETA
[0m[91m-                     51% |****************                | 12.7M  0:00:22 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:20 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:19 ETA
[0m[91m-                    [0m[91m 58% |******************              | 14.5M  0:00:18 ETA
[0m[91m-                     60% |*******************             | 15.0M  0:00:17 ETA
[0m[91m-                     62% |********************            | 15.6M  0:00:16 ETA
[0m[91m-                     64% |********************            | 16.2M  0:00:15 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:14 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:13 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.5M  0:00:11 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:10 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:09 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:06 ETA
[0m[91m-                    [0m[91m 87% |****************************    | 21.9M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% |********************************| [0m[91m25.0M  0:00:00 ETA
written to stdout
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
 ---> 58238bcb37d3
Removing intermediate container 9f61aecefc60
Step 11/14 : WORKDIR /
 ---> 848f0ac7d692
Removing intermediate container 7e96634c699f
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 5a4b3cf50c42
 ---> feb2bed1cf25
Removing intermediate container 5a4b3cf50c42
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 3602a36862ad
 ---> b8216ebcd14d
Removing intermediate container 3602a36862ad
Step 14/14 : USER [secure]
 ---> Running in 8656f9407eec
 ---> 3fdc3dad043d
Removing intermediate container 8656f9407eec
Successfully built 3fdc3dad043d
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1bf7bfebac3582204fa43ff8841c901bd107b21d514963b85f521a8d27991f7b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:27abdedf761cf5fb2ee1c39ccfc5da48e1de5bf25fd2c14ffce433615a00ab3d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:05666f98:start=1580815948971162209,finish=1580816317535097450,duration=368563935241,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:048203bc[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:048203bc:start=1580816321835108666,finish=1580816323308572960,duration=1473464294,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0550ad70[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/645903426/log.txt)