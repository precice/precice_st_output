## Status: Failure 
Build: [1407](https://travis-ci.org/precice/systemtests/builds/634304738) 

Job: [1407.16](https://travis-ci.org/precice/systemtests/jobs/634304754) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/131) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     22% |*******                         | 5840k  0:00:37 ETA
[0m[91m-                     25% |********                        | 6446k  0:00:35 ETA
[0m[91m-                     27% |********                        | 7033k  0:00:34 ETA
[0m[91m-                     29% |*********                       | 7612k  0:00:33 ETA
[0m[91m-                     32% |**********                      | 8220k  0:00:31 ETA
[0m[91m-                     34% |**********                      | 8798k  0:00:30 ETA
[0m[91m-                     36% |***********                     | 9368k  0:00:29 ETA
[0m[91m-                     38% |************                    | 9986k  0:00:28 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:27 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:25 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:24 ETA
[0m[91m-                     48% |***************                 | 12.0M  0:00:23 ETA
[0m[91m-                     50% |****************                | 12.6M  0:00:22 ETA
[0m[91m-                     52% |****************                | 13.2M  0:00:21 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:20 ETA
[0m[91m-                     57% |******************              | 14.3M  0:00:19 ETA
[0m[91m-                     59% |*******************             | 14.9M  0:00:18 ETA
[0m[91m-                     62% |*******************             | 15.5M  0:00:17 ETA
[0m[91m-                     64% |********************            | 16.1M  0:00:16 ETA
[0m[91m-                     65% |********************            | 16.4M  0:00:15 ETA
[0m[91m-                     66% |*********************           | 16.7M  0:00:15 ETA
[0m[91m-                     68% |*********************           | [0m[91m17.1M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.7M  0:00:13 ETA
[0m[91m-                     73% |***********************         | 18.3M  0:00:12 ETA
[0m[91m-                     75% |************************        | 18.8M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.4M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.0M  0:00:09 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% [0m[91m|***************************     | 21.2M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.7M  0:00:05 ETA
[0m[91m-                     89% |****************************    | 22.3M  0:00:04 ETA
[0m[91m-                     91% |*****************************   | 22.9M  0:00:03 ETA
[0m[91m-                     93% |******************************  | 23.5M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 24.6M  0:00:00 ETA
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
 ---> 3e7ba59e7243
Removing intermediate container bb1afad2465a
Step 11/14 : WORKDIR /
 ---> 547c998bb691
Removing intermediate container d1e8eb2a980f
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in d780a1c8e699
 ---> 4dbcf2ca4e08
Removing intermediate container d780a1c8e699
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fd68cf8e6710
 ---> e8eabc45259f
Removing intermediate container fd68cf8e6710
Step 14/14 : USER [secure]
 ---> Running in 6fbe20934b21
 ---> cb4d440b6dd9
Removing intermediate container 6fbe20934b21
Successfully built cb4d440b6dd9
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e442f33a6f3cab80648fc9ce72f80770ee8c748f2969dc4cd39d3ccd02fd4e5a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e6259893f4093a5cb6bb83bf002935e9a732dd240ea229ed3b845be883daaa5d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
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
travis_time:end:1ebd2fdf:start=1578501093457883577,finish=1578501298033913742,duration=204576030165,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:02ba94a0[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/634304754/log.txt)