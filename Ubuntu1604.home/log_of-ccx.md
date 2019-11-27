## Status: Passing 
Build: [1155](https://travis-ci.org/precice/systemtests/builds/617504380) 

Job: [1155.19](https://travis-ci.org/precice/systemtests/jobs/617504399) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[0m[91m-                     24% |*******                         | 6210k  0:00:43 ETA
[0m[91m-                     26% |********                        | 6777k  0:00:41 ETA
[0m[91m-                     28% |*********                       | 7301k  0:00:40 ETA
[0m[91m-                    [0m[91m 30% |*********                       | 7863k  0:00:38 ETA
[0m[91m-                     32% |**********                      | 8421k  0:00:36 ETA
[0m[91m-                     35% |***********                     | 8973k  0:00:35 ETA
[0m[91m-                     37% |***********                     | 9496k  0:00:33 ETA
[0m[91m-                     39% |************                    |  9.8M[0m[91m  0:00:32 ETA
[0m[91m-                     41% |*************                   | 10.3M  0:00:31 ETA
[0m[91m-                     43% |*************                   | 10.9M  0:00:29 ETA
[0m[91m-                     45% |**************                  | 11.4M  0:00:28 ETA
[0m[91m-                     47% |***************                 | 11.9M  0:00:27 ETA
[0m[91m-                     50% |****************                | 12.5M  0:00:25 ETA
[0m[91m-                     52% |****************                | 13.0M  0:00:24 ETA
[0m[91m-                     54% |*****************               | 13.6M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:22 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:21 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:19 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:18 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:17 ETA
[0m[91m-                     67% |*********************           | 16.8M  0:00:16 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     71% |**********************          | 17.9M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                     75% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                     78% |*************************       | 19.5M  0:00:10 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:09 ETA[0m[91m
[0m[91m-                     82% |**************************      | 20.6M  0:00:08 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | 23.8M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.4M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.9M  0:00:00 ETA
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
 ---> dddbc7618097
Removing intermediate container 630f23466705
Step 10/13 : WORKDIR /
 ---> 70f3fbda6cce
Removing intermediate container c03d0167a100
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in f4c0550f4fd3
 ---> 6c645fa82cfd
Removing intermediate container f4c0550f4fd3
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in f888ca22bd01
 ---> 375f829252ad
Removing intermediate container f888ca22bd01
Step 13/13 : USER [secure]
 ---> Running in 4ea63fb72dbb
 ---> e262e4c9eac8
Removing intermediate container 4ea63fb72dbb
Successfully built e262e4c9eac8
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c1b04241d5b9c1e4102b8bd1110c756b0acb05912f874531f62de82e70763643
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:2fa75ecb93c0710efb66171c159f7a535147d776ade95383d556993f77b749aa
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0ff0701b:start=1574823187515422423,finish=1574823533944199669,duration=346428777246,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0e007c78[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0e007c78:start=1574823538734228782,finish=1574823540396574130,duration=1662345348,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:30a83ea3[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/617504399/log.txt)