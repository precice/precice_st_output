## Status: Passing 
Build: [1268](https://travis-ci.org/precice/systemtests/builds/621181807) 

Job: [1268.18](https://travis-ci.org/precice/systemtests/jobs/621181827) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ff51dfcb2467...d102fedd8227) 

---
Last 100 lines of the job log at the moment of push:
```
Removing intermediate container 6df260f2973d
Step 3/12 : RUN apk add git
 ---> Running in 906135f5ac79
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
 ---> 551bd22c857c
Removing intermediate container 906135f5ac79
Step 4/12 : ARG branch=develop
 ---> Running in 03818e2571a3
 ---> df4dca7f0005
Removing intermediate container 03818e2571a3
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 6a61189c22b0
[91mCloning into 'tutorials'...
[0m ---> b853276e0546
Removing intermediate container 6a61189c22b0
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 0c954cb6ef0b
 ---> 42722f992b3b
Removing intermediate container 0c954cb6ef0b
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 46cc3a5f3f77
 ---> 641f7f89d4b3
Removing intermediate container 46cc3a5f3f77
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in cfac18e3246f
 ---> 7a53ea6f5e6e
Removing intermediate container cfac18e3246f
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in db661af95949
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 4b6a390006be
Removing intermediate container db661af95949
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in bc9da9ec6e9c
 ---> eed520e1cfba
Removing intermediate container bc9da9ec6e9c
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 49f8a95f2bff
 ---> 911e4a535ca0
Removing intermediate container 49f8a95f2bff
Step 12/12 : USER [secure]
 ---> Running in 06f4f6def28b
 ---> 5c3d8022e6b4
Removing intermediate container 06f4f6def28b
Successfully built 5c3d8022e6b4
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:509928ef47f3e2b800f11b0e404af7166a82ae4a4bbbda84fd9701c8da64dadb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:f3794d5781c02908071460a6a2f91d302c070ccb4f79cc8d4f7c9fd400ca8553
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:12a0ef19:start=1575565273361030077,finish=1575565472393032178,duration=199032002101,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2b833dde:start=1575565476159276639,finish=1575565477521187663,duration=1361911024,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0f6a2cd1[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/621181827/log.txt)