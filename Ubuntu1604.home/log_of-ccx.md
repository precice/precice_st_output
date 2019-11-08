## Status: Passing 
Build: [1062](https://travis-ci.org/precice/systemtests/builds/609194087) 

Job: [1062.15](https://travis-ci.org/precice/systemtests/jobs/609194104) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f02cef114a79...c96d99257303) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     47% |***************                 | 11.8M  0:00:30 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:29 ETA
[0m[91m-                     51% [0m[91m|****************                | 12.7M  0:00:27 ETA
[0m[91m-                     53% |*****************               | 13.3M  0:00:26 ETA
[0m[91m-                     55% |*****************               | 13.8M  0:00:24 ETA
[0m[91m-                    [0m[91m 57% |******************              | [0m[91m14.3M  0:00:23 ETA
[0m[91m-                     59% |*******************             | 14.8M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.4M  0:00:21 ETA
[0m[91m-                     63% |********************            | 15.9M  0:00:20 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:18 ETA
[0m[91m-                     68% |*********************           | 17.0M  0:00:17 ETA
[0m[91m-                     70% |**********************          | 17.6M  0:00:16 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.7M[0m[91m  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:10 ETA
[0m[91m-                     83% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                     86% [0m[91m|***************************     | 21.7M  0:00:07 ETA
[0m[91m-                     88% |****************************    | [0m[91m22.2M  0:00:06 ETA
[0m[91m-                     91% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M[0m[91m  0:00:00 ETA
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
 ---> 6ead0cafce75
Removing intermediate container 42a1b6eff543
Step 10/13 : WORKDIR /
 ---> f78af12780ca
Removing intermediate container 245b1e83df7d
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 7d15a1024ba7
 ---> eac10358445e
Removing intermediate container 7d15a1024ba7
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 65efd742d992
 ---> d353e881944a
Removing intermediate container 65efd742d992
Step 13/13 : USER [secure]
 ---> Running in 1103ff5d9452
 ---> ceb201ad0563
Removing intermediate container 1103ff5d9452
Successfully built ceb201ad0563
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:378ef6ba2ce11e83a8e56ce1b601e6708559dc7791caea54395add87de1e187d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:87855d0dd45e69c0f2d705a60aa523a06ac3ac2021da68f5876a8ff785277ea1
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1536f9c0:start=1573216502578188083,finish=1573216857757741500,duration=355179553417,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01f514f4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01f514f4:start=1573216862237547312,finish=1573216864062859978,duration=1825312666,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:130cc827[0KSuccessfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/609194104/log.txt)