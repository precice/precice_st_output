## Status: Passing 
Build: [1239](https://travis-ci.org/precice/systemtests/builds/619372101) 

Job: [1239.19](https://travis-ci.org/precice/systemtests/jobs/619372122) 

Triggered by: [push](https://github.com/precice/systemtests/compare/cf8e616f4d09...39aadec5ed5b) 

---
Last 100 lines of the job log at the moment of push:
```
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in fb53d16bdbd8
 ---> 2798ea64aecf
Removing intermediate container fb53d16bdbd8
Step 3/12 : RUN apk add git
 ---> Running in 0ab49dac353c
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.66.0-r0)
(4/6) Installing expat (2.2.8-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> 3d8bed55ce9c
Removing intermediate container 0ab49dac353c
Step 4/12 : ARG branch=develop
 ---> Running in 0ce4ca589012
 ---> baeb707377bf
Removing intermediate container 0ce4ca589012
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in a541a957aab3
[91mCloning into 'tutorials'...
[0m ---> aae4e116d1f6
Removing intermediate container a541a957aab3
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 114155ae6ab5
 ---> 07d6ea1d5c7d
Removing intermediate container 114155ae6ab5
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in a8c6023c9d0f
 ---> 91495fdda51b
Removing intermediate container a8c6023c9d0f
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 34d02ce58890
 ---> 955e9f3a0c39
Removing intermediate container 34d02ce58890
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in f1a5fd3d7449
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 9bf000814af1
Removing intermediate container f1a5fd3d7449
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in bc77eac8f30d
 ---> 1baec74d7d89
Removing intermediate container bc77eac8f30d
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c78496276682
 ---> b35f74b231fe
Removing intermediate container c78496276682
Step 12/12 : USER [secure]
 ---> Running in 81cc2601b6b8
 ---> e4360223f682
Removing intermediate container 81cc2601b6b8
Successfully built e4360223f682
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:70fe2faa72b2f0b36bebe52feee9ebbc2d8a68c08257a7c3fe32a7a746f8f227
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:e504dcc9c33e2c87a295bfe90904234693b550d3d9c846db0977fe36e9420ba9
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03867534:start=1575245531449715625,finish=1575245798107212199,duration=266657496574,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:152a759c:start=1575245802967240521,finish=1575245804679817450,duration=1712576929,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:17745540[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/619372122/log.txt)