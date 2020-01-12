## Status: Failure 
Build: [1441](https://travis-ci.org/precice/systemtests/builds/635916850) 

Job: [1441.3](https://travis-ci.org/precice/systemtests/jobs/635916853) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/152) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     19% |******                          | 4929k  0:00:37 ETA
[0m[91m-                     21% |******                          | 5551k  0:00:36 ETA[0m[91m
[0m[91m-                     23% |*******                         | 6127k  0:00:35 ETA
[0m[91m-                     26% |********                        | 6686k  0:00:34 ETA
[0m[91m-                     28% |*********                       | 7326k  0:00:32 ETA
[0m[91m-                     30% |*********                       | 7890k  0:00:31 ETA
[0m[91m-                     33% |**********                      | 8513k  0:00:30 ETA
[0m[91m-                     35% |***********                     | 9091k  0:00:29 ETA
[0m[91m-                     37% |************                    | 9647k  0:00:28 ETA
[0m[91m-                    [0m[91m 40% |************                    | 10.0M  0:00:26 ETA
[0m[91m-                     42% |*************                   | 10.5M  0:00:25 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:24 ETA
[0m[91m-                     47% |***************                 | 11.7M  0:00:23 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:22 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:21 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:20 ETA
[0m[91m-                     54% |*****************               | 13.7M  0:00:20 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:20 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:19 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:18 ETA
[0m[91m-                     63% |********************            | 15.7M  0:00:16 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:15 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:14 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:12 ETA
[0m[91m-                     74% [0m[91m|***********************         | 18.6M  0:00:11 ETA
[0m[91m-                     76% |************************        | 19.2M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.7M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:07 ETA
[0m[91m-                     85% |***************************     | 21.5M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |****************************    | 22.6M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 25.0M  0:00:00 ETA
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
 ---> b789cd350fb7
Removing intermediate container 01afc6411bef
Step 11/14 : WORKDIR /
 ---> c899713d16bf
Removing intermediate container 7155dbdf0cbd
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 57d96013c3b3
 ---> c711036aa4f5
Removing intermediate container 57d96013c3b3
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ccd4d013152c
 ---> 2c5aeb3e7828
Removing intermediate container ccd4d013152c
Step 14/14 : USER [secure]
 ---> Running in 4fdb2c18b17d
 ---> e54c123829ec
Removing intermediate container 4fdb2c18b17d
Successfully built e54c123829ec
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:929e20432a5cdeb84eebfe5fee37434ab895549d3aef02d9473f6686f8453835
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:1f607c035c65e2a8c2b8cf400419a2767f97d9cd486d9cea301c1d0f6590834e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner
Creating openfoam-adapter-outer
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Inner-Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput: Outer-Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Inner-Fluid', 'Outer-Fluid']
Files only in output(right)   : []
travis_time:end:0b2376a0:start=1578821841307504215,finish=1578821984479460278,duration=143171956063,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1259b0c0[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635916853/log.txt)