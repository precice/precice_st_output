## Status: Failure 
Build: [1357](https://travis-ci.org/precice/systemtests/builds/628327379) 

Job: [1357.19](https://travis-ci.org/precice/systemtests/jobs/628327398) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     26% |********                        | 6736k  0:00:42 ETA
[0m[91m-                     28% |*********                       | 7252k  0:00:40 ETA
[0m[91m-                     30% |*********                       | 7806k  0:00:38 ETA
[0m[91m-                     32% |**********                      | 8370k  0:00:37 ETA
[0m[91m-                     34% |***********                     | 8947k  0:00:35 ETA
[0m[91m-                    [0m[91m 37% |***********                     | 9510k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.7M  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.8M  0:00:29 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:28 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.4M  0:00:26 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:20 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.3M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.4M  0:00:13 ETA
[0m[91m-                     75% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.1M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
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
 ---> 5c0455fbd12d
Removing intermediate container 56878d498a78
Step 11/14 : WORKDIR /
 ---> 937953bfedab
Removing intermediate container 412a678dca81
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in ca0001e81bcb
 ---> 4b7e2ec0370a
Removing intermediate container ca0001e81bcb
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 83428b6033d7
 ---> bd66cc0b6cd6
Removing intermediate container 83428b6033d7
Step 14/14 : USER [secure]
 ---> Running in a5f2f3b037b1
 ---> c64b2e7dc192
Removing intermediate container a5f2f3b037b1
Successfully built c64b2e7dc192
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8d4a806cc71cc7bf0b40fe6b7ed9fecfad916807f641126c158b5dd753384d46
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4053ac29425a73e4a8962f8b9997ce90853b9c21f158e27fc92f6eab626a14db
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
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
travis_time:end:0fb6762a:start=1577013886055067370,finish=1577014091999645218,duration=205944577848,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:04e5acf4[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/628327398/log.txt)