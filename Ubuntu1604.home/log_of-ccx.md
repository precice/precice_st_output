## Status: Failure 
Build: [1356](https://travis-ci.org/precice/systemtests/builds/628061312) 

Job: [1356.19](https://travis-ci.org/precice/systemtests/jobs/628061331) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     31% |*********                       | 7996k  0:00:35 ETA
[0m[91m-                     33% |**********                      | 8566k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8912k  0:00:33 ETA
[0m[91m-                     34% |***********                     | 8912k  0:00:35 ETA
[0m[91m-                     34% |***********                     | 8912k  0:00:37 ETA
[0m[91m-                     35% |***********                     | 9117k  0:00:38 ETA[0m[91m
[0m[91m-                     37% |***********                     | 9605k  0:00:36 ETA
[0m[91m-                    [0m[91m 39% |************                    |  9.9M  0:00:34 ETA
[0m[91m-                     41% |*************                   | 10.4M  0:00:33 ETA
[0m[91m-                     44% |**************                  | 11.0M  0:00:31 ETA
[0m[91m-                     46% |**************                  | 11.5M  0:00:30 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:28 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:27 ETA
[0m[91m-                     52% |****************                | 13.1M  0:00:25 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:24 ETA
[0m[91m-                     56% |******************              | 14.2M  0:00:23 ETA
[0m[91m-                     59% |******************              | 14.7M  0:00:22 ETA
[0m[91m-                     61% |*******************             | 15.3M  0:00:20 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                     65% |*********************           | 16.4M  0:00:18 ETA
[0m[91m-                     67% [0m[91m|*********************           | 16.9M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.5M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.1M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.2M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.7M  0:00:08 ETA
[0m[91m-                     85% |***************************     | 21.3M  0:00:07 ETA
[0m[91m-                    [0m[91m 87% |***************************     | 21.8M  0:00:06 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:04 ETA
[0m[91m-                     93% |******************************  | 23.4M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.9M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.5M  0:00:01 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
[0m[91mwritten to stdout
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
 ---> 12a10823ec97
Removing intermediate container 29311eae5fd3
Step 11/14 : WORKDIR /
 ---> 214646eb629b
Removing intermediate container a9d8e1522591
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in c0b465bb7cce
 ---> c9812a839af1
Removing intermediate container c0b465bb7cce
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 12b1c317ec2b
 ---> 4aebfc918d6f
Removing intermediate container 12b1c317ec2b
Step 14/14 : USER [secure]
 ---> Running in 29c2354e6344
 ---> 0cdec666294b
Removing intermediate container 29c2354e6344
Successfully built 0cdec666294b
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:669d9e0d4323f497483d857574bde38d2e2feb1f672b675d54a49e692b5dbec8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4b94783962b3b9e5538c61e89b8abb1010abd20bdf2ab988b229510f7309ffa8
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Outer-Fluid', 'Inner-Fluid']
Files only in output(right)   : []
travis_time:end:08949710:start=1576927387039564676,finish=1576927599172358093,duration=212132793417,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:332bbe64[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/628061331/log.txt)