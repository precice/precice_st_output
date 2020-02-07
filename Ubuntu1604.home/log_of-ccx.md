## Status: Passing 
Build: [1613](https://travis-ci.org/precice/systemtests/builds/647273995) 

Job: [1613.19](https://travis-ci.org/precice/systemtests/jobs/647274014) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     29% |*********                       | 7491k  0:00:36 ETA
[0m[91m-                     31% |**********                      | 8017k  0:00:35 ETA
[0m[91m-                     33% |**********                      | 8556k  0:00:33 ETA
[0m[91m-                     35% |***********                     | 9111k  0:00:32 ETA
[0m[91m-                     37% |************                    | 9658k  0:00:31 ETA
[0m[91m-                     39% |************                    |  9.9M  0:00:30 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:29 ETA
[0m[91m-                     43% |**************                  | 11.0M  0:00:28 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:27 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:27 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:27 ETA
[0m[91m-                    [0m[91m 49% |***************                 | 12.2M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:23 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:22 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:18 ETA
[0m[91m-                     66% |*********************           | 16.5M  0:00:17 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:16 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:11 ETA
[0m[91m-                     78% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M[0m[91m  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
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
 ---> 6872cf22d481
Removing intermediate container 4e19bcb709e7
Step 11/14 : WORKDIR /
 ---> 0386aa5b946d
Removing intermediate container d98e64300224
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 5d4209776cee
 ---> 899f46602eed
Removing intermediate container 5d4209776cee
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 737c74655bf1
 ---> 93c88280abd4
Removing intermediate container 737c74655bf1
Step 14/14 : USER [secure]
 ---> Running in 5b8445397a54
 ---> bc058197ef0b
Removing intermediate container 5b8445397a54
Successfully built bc058197ef0b
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:b1617965f93659491aadc821ca91d521d2ba707714389c1cc7ddab49496a39bd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:fa1617bd2c3be7af0a6ef3b306317aa1c7ac1798c6c8cdbfa68598ecd501e323
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:06d36d30:start=1581077983911673113,finish=1581078312791551389,duration=328879878276,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:005c51ac[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:005c51ac:start=1581078317003835286,finish=1581078318446988328,duration=1443153042,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1ddad988[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/647274014/log.txt)