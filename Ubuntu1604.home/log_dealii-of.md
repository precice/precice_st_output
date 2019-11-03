## Status: Passing 
Build: [1055](https://travis-ci.org/precice/systemtests/builds/606615476) 

Job: [1055.22](https://travis-ci.org/precice/systemtests/jobs/606615498) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
    - output:/Output:rw
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
 ---> Running in b641a413c828
 ---> afec21129e4d
Removing intermediate container b641a413c828
Step 3/11 : RUN apk add git
 ---> Running in 7de1287e4f1d
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
 ---> d3cae6143fc5
Removing intermediate container 7de1287e4f1d
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in ca6343c7428f
[91mCloning into 'tutorials'...
[0m ---> 036711650e79
Removing intermediate container ca6343c7428f
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 24aeba559d4c
 ---> b9d9885d59f1
Removing intermediate container 24aeba559d4c
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in fada451926ce
 ---> f6143de25d72
Removing intermediate container fada451926ce
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 6504a14150e5
 ---> 91b39d2d6e57
Removing intermediate container 6504a14150e5
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in c5dc2acf2f07
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> eaa0c869b400
Removing intermediate container c5dc2acf2f07
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 7962d9617bfa
 ---> 6b3126bb79d6
Removing intermediate container 7962d9617bfa
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5a9b563ec4c1
 ---> 1d3cbfb69ba1
Removing intermediate container 5a9b563ec4c1
Step 11/11 : USER [secure]
 ---> Running in f5ff48575816
 ---> f9c7f7797d56
Removing intermediate container f5ff48575816
Successfully built f9c7f7797d56
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e1ede29dae04cac520d17c81301087123c03455b9bb7251d4b5da0388fc8b489
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:840511d29bc0942e72232283b54378e32ba0a53bf0836e5bce08525e0c8a3e5a
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

```
[
Full job log](https://api.travis-ci.org/v3/job/606615498/log.txt)