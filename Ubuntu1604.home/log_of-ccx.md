## Status: Passing 
Build: [1161](https://travis-ci.org/precice/systemtests/builds/617683464) 

Job: [1161.15](https://travis-ci.org/precice/systemtests/jobs/617683480) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ec4ef9d4aedd...6a636c04a7f9) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     45% |**************                  | 11.3M  0:00:26 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:25 ETA
[0m[91m-                     49% [0m[91m|***************                 | 12.4M  0:00:24 ETA
[0m[91m-                    [0m[91m 51% |****************                | 12.9M  0:00:23 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:22 ETA
[0m[91m-                    [0m[91m 56% |*****************               | 14.0M  0:00:21 ETA
[0m[91m-                     58% [0m[91m|******************              | 14.5M  0:00:20 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     62% |*******************             | 15.6M[0m[91m  0:00:18 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     69% |**********************          | 17.2M  0:00:14 ETA
[0m[91m-                     71% |**********************          | 17.7M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA[0m[91m
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.9M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     84% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | [0m[91m21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
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
 ---> bee13616947a
Removing intermediate container 2b6a131939d2
Step 11/14 : WORKDIR /
 ---> 22841efaac5f
Removing intermediate container 63a39c8cfadd
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 9b9557491f75
 ---> f18c65060b3a
Removing intermediate container 9b9557491f75
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in f5fee6c9571c
 ---> 048ba4f93ef0
Removing intermediate container f5fee6c9571c
Step 14/14 : USER [secure]
 ---> Running in dd5941c18375
 ---> d2232ac6a9c8
Removing intermediate container dd5941c18375
Successfully built d2232ac6a9c8
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d1e3cf9fc21d38b0bd5071fdc517a74de9ad989536e3e0e143422b194b9b30a7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0a00f5ee096947d16d6bfb876909901d1081ec0034c65fbcef93f25e76f36a93
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
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
travis_time:end:15bdbaa6:start=1574861361513838610,finish=1574861705271249056,duration=343757410446,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0d99545a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0d99545a:start=1574861709845922649,finish=1574861711580223972,duration=1734301323,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:15ec682c[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/617683480/log.txt)