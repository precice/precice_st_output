## Status: Failure 
Build: [1366](https://travis-ci.org/precice/systemtests/builds/630280475) 

Job: [1366.19](https://travis-ci.org/precice/systemtests/jobs/630280495) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     26% |********                        | 6834k  0:00:49 ETA
[0m[91m-                     28% |*********                       | 7397k  0:00:46 ETA
[0m[91m-                     31% |**********                      | 8022k  0:00:43 ETA
[0m[91m-                     33% |**********                      | 8594k  0:00:41 ETA
[0m[91m-                     35% |***********                     | 9166k  0:00:39 ETA
[0m[91m-                     36% |***********                     | 9287k  0:00:40 ETA
[0m[91m-                     37% |************                    | 9689k  0:00:39 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:37 ETA
[0m[91m-                     42% [0m[91m|*************                   | 10.5M  0:00:35 ETA
[0m[91m-                     44% |**************                  | 11.1M  0:00:33 ETA
[0m[91m-                     46% |***************                 | 11.7M  0:00:31 ETA
[0m[91m-                     49% |***************                 | 12.2M  0:00:30 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:28 ETA
[0m[91m-                    [0m[91m 53% |*****************               | 13.4M  0:00:26 ETA
[0m[91m-                     56% |*****************               | 14.0M  0:00:25 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:23 ETA
[0m[91m-                     60% |*******************             | 15.1M  0:00:21 ETA
[0m[91m-                     62% |********************            | 15.7M  0:00:20 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:19 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:17 ETA[0m[91m
[0m[91m-                     70% |**********************          | 17.5M  0:00:16 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     74% |***********************         | 18.6M  0:00:13 ETA
[0m[91m-                    [0m[91m 76% |************************        | 19.2M  0:00:12 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:11 ETA
[0m[91m-                    [0m[91m 81% |**************************      | 20.3M  0:00:09 ETA
[0m[91m-                     83% |**************************      | 20.9M  0:00:08 ETA
[0m[91m-                     86% |***************************     | 21.5M  0:00:07 ETA
[0m[91m-                     88% |****************************    | 22.1M  0:00:05 ETA
[0m[91m-                     90% |*****************************   | 22.7M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | [0m[91m23.2M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     96% |******************************  | 24.0M  0:00:01 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA[0m[91m
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
 ---> 490e78425efb
Removing intermediate container 4126d03f9b55
Step 11/14 : WORKDIR /
 ---> 07f089208944
Removing intermediate container d07b2a335166
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in 3eddcd1a5cc6
 ---> 4921221e1642
Removing intermediate container 3eddcd1a5cc6
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in aa589a1fd041
 ---> bbdb0a5b536d
Removing intermediate container aa589a1fd041
Step 14/14 : USER [secure]
 ---> Running in e8e46d2ee5dc
 ---> c761b814ae07
Removing intermediate container e8e46d2ee5dc
Successfully built c761b814ae07
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9024986cf3d867f75dc706a8ccb49bb4481849776cc904724de2d76405d11b2c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:623ab068cff8f3dfcac4a74805d3fd47bca3fb14f53283b20cc7348800681673
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
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
travis_time:end:14ba22b6:start=1577532333712117425,finish=1577532548384966979,duration=214672849554,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:006eb226[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/630280495/log.txt)