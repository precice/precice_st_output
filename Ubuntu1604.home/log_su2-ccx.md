## Status: Passing 
Build: [1227](https://travis-ci.org/precice/systemtests/builds/618560778) 

Job: [1227.13](https://travis-ci.org/precice/systemtests/jobs/618560793) 

Triggered by: [push](https://github.com/precice/systemtests/compare/d440b60eb25a...e486b1f8560f) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 579679b309e8
 ---> 868af23916c3
Removing intermediate container 579679b309e8
Step 3/10 : RUN apk add git bash
 ---> Running in 8c4b2c057893
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20190518-r0)
(2/11) Installing ncurses-terminfo (6.1_p20190518-r0)
(3/11) Installing ncurses-libs (6.1_p20190518-r0)
(4/11) Installing readline (8.0.0-r0)
(5/11) Installing bash (5.0.0-r0)
Executing bash-5.0.0-r0.post-install
(6/11) Installing ca-certificates (20190108-r0)
(7/11) Installing nghttp2-libs (1.39.2-r0)
(8/11) Installing libcurl (7.66.0-r0)
(9/11) Installing expat (2.2.8-r0)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> dbf91d710d4e
Removing intermediate container 8c4b2c057893
Step 4/10 : ARG branch=develop
 ---> Running in 1e7584986a1b
 ---> d93eeb596f99
Removing intermediate container 1e7584986a1b
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 3fab648d531d
[91mCloning into 'tutorials'...
[0m ---> 0bb991ca85bc
Removing intermediate container 3fab648d531d
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 4644feb9280d
 ---> 625ebc9cfcb7
Removing intermediate container 4644feb9280d
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d5f632185f26
 ---> bdb589a35b81
Removing intermediate container d5f632185f26
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 0bd3ed9611ac
 ---> 30c946adf8b3
Removing intermediate container 0bd3ed9611ac
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 047020337b3f
 ---> 261676db42d4
Removing intermediate container 047020337b3f
Step 10/10 : USER [secure]
 ---> Running in dec1ea27583e
 ---> 5690b5ef5226
Removing intermediate container dec1ea27583e
Successfully built 5690b5ef5226
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:1816597e56233bf073df0f07c6697126b6edaecbb0ef01a761e52cb6fd17a8dc
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:30ff6f2d96538f561a5878a7f0a706973e9452a7b8291d8bde557a7a51dd26ae
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0ea17f6c:start=1575030554750193457,finish=1575030843378459833,duration=288628266376,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:253e10b9[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:253e10b9:start=1575030847960942188,finish=1575030849567707303,duration=1606765115,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:14821a34[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618560793/log.txt)