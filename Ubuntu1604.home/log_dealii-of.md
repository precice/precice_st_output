## Status: Passing 
Build: [1030](https://travis-ci.org/precice/systemtests/builds/603395419) 

Job: [1030.22](https://travis-ci.org/precice/systemtests/jobs/603395441) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

---
Last 100 lines of the job log at the moment of push:
```

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
 ---> Running in 9942ac2b580c
 ---> 93ad4a04e696
Removing intermediate container 9942ac2b580c
Step 3/11 : RUN apk add git
 ---> Running in 7eae4e70fa0c
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
 ---> a39e5917d641
Removing intermediate container 7eae4e70fa0c
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in d48eb06cdcec
[91mCloning into 'tutorials'...
[0m ---> b9c9a50585d4
Removing intermediate container d48eb06cdcec
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in add44e9dc447
 ---> e8a10a046212
Removing intermediate container add44e9dc447
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 11adcca02eb3
 ---> edc543cd6027
Removing intermediate container 11adcca02eb3
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a0c0770638d5
 ---> 17fca47b922e
Removing intermediate container a0c0770638d5
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 87eee6cb0b45
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 13b36123d222
Removing intermediate container 87eee6cb0b45
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in e5ee22b8a187
 ---> e60af584188d
Removing intermediate container e5ee22b8a187
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 05a40b73f860
 ---> 5985e011a45a
Removing intermediate container 05a40b73f860
Step 11/11 : USER [secure]
 ---> Running in 91711415a562
 ---> 393598b85346
Removing intermediate container 91711415a562
Successfully built 393598b85346
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d8a5bfbc8deb1b0507d1dc8aa3f8ccef96ebe5eb58582e4d759442585182293c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:0589896e8286cd73747714512eef2d8aed275415e9dc502603b4ac2130aa257e
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
travis_time:end:02e9300e:start=1572143959285662899,finish=1572144230935203227,duration=271649540328,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:19d3b950[0K$ python push.py -s -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/603395441/log.txt)