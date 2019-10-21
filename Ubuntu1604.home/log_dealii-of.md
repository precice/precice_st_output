## Status: Passing 
Build: [993](https://travis-ci.org/precice/systemtests/builds/600693901) 

Job: [993.18](https://travis-ci.org/precice/systemtests/jobs/600693920) 

Triggered by: [push](https://github.com/precice/systemtests/compare/a84a139c2665...500cfbb53a97) 

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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 6069ce0b2aa9
 ---> 32eb551e443c
Removing intermediate container 6069ce0b2aa9
Step 3/11 : RUN apk add git
 ---> Running in e4ce263f343a
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
 ---> ec215ee2adb8
Removing intermediate container e4ce263f343a
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 9dfc99b67929
[91mCloning into 'tutorials'...
[0m ---> 9761754ac398
Removing intermediate container 9dfc99b67929
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 5cd6bf954088
 ---> 9075987dd11c
Removing intermediate container 5cd6bf954088
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 867fc2e2dff4
 ---> 014011b3b1d9
Removing intermediate container 867fc2e2dff4
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in c84e541c0291
 ---> 399ef8f4df62
Removing intermediate container c84e541c0291
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in eeac63a7fa67
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 8eaee9cdbb9b
Removing intermediate container eeac63a7fa67
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in a86f11e1a60e
 ---> 7c96d556e955
Removing intermediate container a86f11e1a60e
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 58e2686308e4
 ---> a3c922c96908
Removing intermediate container 58e2686308e4
Step 11/11 : USER [secure]
 ---> Running in 08b92f33ccc1
 ---> 424aefbb2b2f
Removing intermediate container 08b92f33ccc1
Successfully built 424aefbb2b2f
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:04602e91508ea2c3b26d367af5b44dc79b28546a9dc09a0543218d00fc13e338
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:dbea6698711bfdd233ac9b3f7e2dfc6f50561cb4b94ee32f6143d69ef684890e
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

```
[
Full job log](https://api.travis-ci.org/v3/job/600693920/log.txt)