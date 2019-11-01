## Status: Passing 
Build: [1052](https://travis-ci.org/precice/systemtests/builds/605812235) 

Job: [1052.22](https://travis-ci.org/precice/systemtests/jobs/605812257) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  input_dealii: {}
  input_of: {}
  output: {}

Creating network "testcomposedealiiof_default" with the default driver
Creating network "testcomposedealiiof_[secure]comm" with the default driver
Creating volume "testcomposedealiiof_output" with default driver
Creating volume "testcomposedealiiof_configs" with default driver
Creating volume "testcomposedealiiof_input_dealii" with default driver
Creating volume "testcomposedealiiof_input_of" with default driver
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in e41f38c5bc1a
 ---> abd996603fc6
Removing intermediate container e41f38c5bc1a
Step 3/11 : RUN apk add git
 ---> Running in c56bb74fdad9
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
 ---> afb19a74d8aa
Removing intermediate container c56bb74fdad9
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 528fcfd87b80
[91mCloning into 'tutorials'...
[0m ---> 7feed333534a
Removing intermediate container 528fcfd87b80
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 8ec9dffc9d94
 ---> ce6a98b90cfe
Removing intermediate container 8ec9dffc9d94
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in b217a66eb416
 ---> 6e658fb4ec8f
Removing intermediate container b217a66eb416
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 761ef163edad
 ---> 1b8cc101b99d
Removing intermediate container 761ef163edad
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 4a0e1cea4601
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 073dd200df87
Removing intermediate container 4a0e1cea4601
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 207ac3d1cccb
 ---> 93628749efec
Removing intermediate container 207ac3d1cccb
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c91ab271d951
 ---> ec1d3455d7c0
Removing intermediate container c91ab271d951
Step 11/11 : USER [secure]
 ---> Running in 884f8e72768e
 ---> 485b4b597af4
Removing intermediate container 884f8e72768e
Successfully built 485b4b597af4
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:5f4cf9654d3e8ad6e24ca09f06617acede4a15c96234e007a7edfec2b73ce6cd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:0d1f928230287e5656d5ff151f19e03c3a8a814e0a141402dea66f1e7f4cfa76
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
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/605812257/log.txt)