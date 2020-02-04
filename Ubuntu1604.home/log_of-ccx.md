## Status: Passing 
Build: [1598](https://travis-ci.org/precice/systemtests/builds/645892844) 

Job: [1598.19](https://travis-ci.org/precice/systemtests/jobs/645892869) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/07c487419fcd18bdb04b9d9fef13c8b1318f3bef...6213c52a25101c0051df0fbc215ba9f941209daa) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     25% |********                        | 6476k  0:00:41 ETA
[0m[91m-                     27% |********                        | 7046k  0:00:39 ETA
[0m[91m-                     29% |*********                       | 7546k  0:00:38 ETA
[0m[91m-                     31% |**********                      | 8120k  0:00:36 ETA
[0m[91m-                     33% |**********                      | 8687k  0:00:35 ETA[0m[91m
[0m[91m-                     36% |***********                     | 9248k  0:00:33 ETA
[0m[91m-                     38% |************                    | 9808k  0:00:32 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:29 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:28 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:27 ETA
[0m[91m-                     48% |***************                 | 12.2M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.7M  0:00:24 ETA
[0m[91m-                    [0m[91m 53% |*****************               | 13.3M  0:00:23 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:22 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:21 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:20 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:19 ETA
[0m[91m-                     64% |********************            | 16.0M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:14 ETA
[0m[91m-                    [0m[91m 72% |***********************         | 18.1M  0:00:13 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:12 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:11 ETA[0m[91m
[0m[91m-                     79% |*************************       | 19.7M  0:00:10 ETA
[0m[91m-                     81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.8M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.4M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     87% |****************************    | 21.9M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.4M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 24.0M[0m[91m  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:01 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> 62364d2d2ad6
Removing intermediate container 1fb5a92ba883
Step 11/14 : WORKDIR /
 ---> 98cd4ea02dc4
Removing intermediate container 107545d215b4
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in b0b2ef502d25
 ---> bd36f2efeccf
Removing intermediate container b0b2ef502d25
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 74e9da400430
 ---> ab1054489139
Removing intermediate container 74e9da400430
Step 14/14 : USER [secure]
 ---> Running in 4ceaf2515dee
 ---> c5ad5faa2294
Removing intermediate container 4ceaf2515dee
Successfully built c5ad5faa2294
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ea8abdbefd367fb0c30630136b061c6189bb5ad3767d77bfd08372119fb5af39
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:cbfc53d937fb813ced19c90ccce35b11a7c01c370364d8469f6fbe0565151b7f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:02ee0514:start=1580817880255657946,finish=1580818149256202681,duration=269000544735,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:00603094[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:00603094:start=1580818153298487496,finish=1580818154700228529,duration=1401741033,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:07d44d1c[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645892869/log.txt)