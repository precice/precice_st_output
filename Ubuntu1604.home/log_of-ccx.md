 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/590479609) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/0cb7c0ec452f...92a2d96de651) 
## Last 100 lines of the job log at the moment of push...
```
 [0m[91m-                      5% |*                               | 1429k  0:01:07 ETA
[0m[91m-                      7% |**                              | 2000k  0:00:59 ETA
[0m[91m-                      9% |***                             | 2491k  0:00:55 ETA
[0m[91m-                     11% |***                             | 2883k  0:00:55 ETA
[0m[91m-                     11% |***                             | 3055k  0:00:59 ETA
[0m[91m-                     13% |****                            | 3383k  0:00:59 ETA
[0m[91m-                     15% |****                            | 3883k  0:00:56 ETA
[0m[91m-                     17% |*****                           | 4445k  0:00:52 ETA
[0m[91m-                     19% |******                          | 4950k  0:00:50 ETA
[0m[91m-                     21% |******                          | 5514k  0:00:47 ETA
[0m[91m-                     23% |*******                         | 6082k  0:00:44 ETA
[0m[91m-                     25% |********                        | 6584k  0:00:43 ETA
[0m[91m-                     27% |********                        | 7153k  0:00:41 ETA
[0m[91m-                     30% |*********                       | 7726k  0:00:39 ETA
[0m[91m-                     32% |**********                      | 8297k  0:00:37 ETA
[0m[91m-                     34% |**********                      | 8789k  0:00:36 ETA
[0m[91m-                     36% |***********                     | 9360k  0:00:34 ETA
[0m[91m-                     38% |************                    | 9931k  0:00:33 ETA
[0m[91m-                     40% |*************                   | 10.1M  0:00:31 ETA
[0m[91m-                     42% |*************                   | 10.7M  0:00:30 ETA
[0m[91m-                     45% |**************                  | 11.2M  0:00:29 ETA
[0m[91m-                     47% |***************                 | 11.8M  0:00:27 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:26 ETA
[0m[91m-                     51% |****************                | 12.8M  0:00:25 ETA
[0m[91m-                     53% |*****************               | 13.4M  0:00:24 ETA
[0m[91m-                     55% |*****************               | 13.9M  0:00:23 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:22 ETA
[0m[91m-                     57% [0m[91m|******************              | 14.4M  0:00:22 ETA
[0m[91m-                     59% |******************              | 14.7M  0:00:22 ETA
[0m[91m-                    [0m[91m 61% |*******************             | 15.3M  0:00:20 ETA
[0m[91m-                    [0m[91m 63% |********************            | 15.8M  0:00:19 ETA
[0m[91m-                     65% |********************            | 16.4M  0:00:18 ETA
[0m[91m-                    [0m[91m 67% |*********************           | 16.9M  0:00:17 ETA
[0m[91m-                     69% |**********************          | 17.4M  0:00:15 ETA
[0m[91m-                     72% |***********************         | 18.0M  0:00:14 ETA
[0m[91m-                     73% |***********************         | 18.5M  0:00:13 ETA
[0m[91m-                     76% |************************        | 19.0M  0:00:12 ETA
[0m[91m-                    [0m[91m 78% |*************************       | 19.6M  0:00:11 ETA
[0m[91m-                     80% |*************************       | 20.1M  0:00:10 ETA
[0m[91m-                     82% |**************************      | 20.6M  0:00:09 ETA
[0m[91m-                     84% |***************************     | 21.2M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.7M  0:00:06 ETA
[0m[91m-                     88% |****************************    | 22.2M  0:00:05 ETA
[0m[91m-                     91% |*****************************   | 22.8M  0:00:04 ETA
[0m[91m-                     93% |*****************************   | 23.3M  0:00:03 ETA
[0m[91m-                     95% |******************************  | [0m[91m23.9M  0:00:02 ETA
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
 ---> 9d60aa729a50
Removing intermediate container 405b593ab512
Step 10/13 : WORKDIR /
 ---> 314ffc112a27
Removing intermediate container 0ea05e33c6de
Step 11/13 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in e9d4a6f9a414
 ---> ec132f08d854
Removing intermediate container e9d4a6f9a414
Step 12/13 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 6bc6dbae58e7
 ---> 389430b44956
Removing intermediate container 6bc6dbae58e7
Step 13/13 : USER [secure]
 ---> Running in bfed1265fcc7
 ---> 7e6f6236ebfa
Removing intermediate container bfed1265fcc7
Successfully built 7e6f6236ebfa
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:17f5650d84b1edf1188baa12b43a57878d5324749f7f656f54914c06ff105fb0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:15adf7f16e3c13e87961e833eeae277f031b8fe8de254c27214dbf0bde9c3fc4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-inner ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/590479624/log.txt)