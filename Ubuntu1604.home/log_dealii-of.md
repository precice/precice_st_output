## Status: Failure 
Build: [1668](https://travis-ci.org/precice/systemtests/builds/648944980) 

Job: [1668.19](https://travis-ci.org/precice/systemtests/jobs/648944999) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/136) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
    container_name: tutorial-data
    volumes:
    - input_of:/tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid:rw
    - input_dealii:/tutorials/FSI/flap_perp/OpenFOAM-deal.II/Solid:rw
    - configs:/configs:rw
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
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 0a4fbce80942
 ---> aff0543e9115
Removing intermediate container 0a4fbce80942
Step 3/12 : RUN apk add git
 ---> Running in cfa2bd5c1282
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r1)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r1.trigger
OK: 22 MiB in 20 packages
 ---> 262914f1ab21
Removing intermediate container cfa2bd5c1282
Step 4/12 : ARG branch=develop
 ---> Running in 268719be1fd6
 ---> 5df393fb6ca1
Removing intermediate container 268719be1fd6
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 79c3756444e5
[91mCloning into 'tutorials'...
[0m ---> b647596d5a74
Removing intermediate container 79c3756444e5
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in 5411dafc643a
 ---> 3c20ceb23276
Removing intermediate container 5411dafc643a
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in a42b37edd9c9
 ---> 2c045b766139
Removing intermediate container a42b37edd9c9
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 01635b6d3efd
 ---> 8aa7a77d9d54
Removing intermediate container 01635b6d3efd
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 89c006d63480
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> f59a3cdc6915
Removing intermediate container 89c006d63480
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 16ddacfc5e23
 ---> feceefd20e57
Removing intermediate container 16ddacfc5e23
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 264059b54042
 ---> adf240b6d06b
Removing intermediate container 264059b54042
Step 12/12 : USER [secure]
 ---> Running in 55dc68f4ef8c
 ---> e1cf6e4c508b
Removing intermediate container 55dc68f4ef8c
Successfully built e1cf6e4c508b
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-i_125:latest)...
pull access denied for [secure]/openfoam-adapter-ubuntu1604.home-i_125, repository does not exist or may require 'docker login'
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-i_125; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-i_125; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:24f11d26:start=1581436877077379854,finish=1581436891366433376,duration=14289053522,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0112a39e[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648944999/log.txt)