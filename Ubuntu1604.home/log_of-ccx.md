## Status: Passing 
Build: [1162](https://travis-ci.org/precice/systemtests/builds/617695037) 

Job: [1162.15](https://travis-ci.org/precice/systemtests/jobs/617695052) 

Triggered by: [push](https://github.com/precice/systemtests/commit/e19c9061ae73) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     44% |**************                  | 11.1M  0:00:27 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:26 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:24 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:22 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:21 ETA
[0m[91m-                     57% |******************              | 14.4M  0:00:20 ETA
[0m[91m-                     59% |*******************             | 15.0M  0:00:19 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:18 ETA
[0m[91m-                    [0m[91m 64% |********************            | 16.1M  0:00:17 ETA
[0m[91m-                     66% |*********************           | 16.6M  0:00:16 ETA
[0m[91m-                     68% |*********************           | 17.1M  0:00:15 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:14 ETA
[0m[91m-                     72% |***********************         | 18.2M  0:00:12 ETA
[0m[91m-                     75% [0m[91m|************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.3M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA[0m[91m
[0m[91m-                     83% |**************************      | 20.9M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.0M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M[0m[91m  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.6M  0:00:02 ETA
[0m[91m-                     96% [0m[91m|******************************  | 24.2M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.7M  0:00:00 ETA
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
 ---> d898842a94da
Removing intermediate container d316bc5cb62e
Step 11/14 : WORKDIR /
 ---> dc0c69440c1b
Removing intermediate container 5fe6e6e5f266
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 995db0c1c9da
 ---> ca325d97807a
Removing intermediate container 995db0c1c9da
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c049c95409ca
 ---> 6ff8e1b08796
Removing intermediate container c049c95409ca
Step 14/14 : USER [secure]
 ---> Running in c386a737585d
 ---> f575eee4e160
Removing intermediate container c386a737585d
Successfully built f575eee4e160
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:10d928c972f1e351417920df1a616eacec15d7e8cec24bec4cfc967efc3374f5
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:68fc44da63ef258f07b87a257fa01baaa5f488d5c5030214a78bd6713e180ded
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03193415:start=1574867952717112425,finish=1574868296206440195,duration=343489327770,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:030228a2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:030228a2:start=1574868300941016938,finish=1574868302664572607,duration=1723555669,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:02101bfa[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/617695052/log.txt)