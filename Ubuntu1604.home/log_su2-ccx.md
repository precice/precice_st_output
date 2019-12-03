## Status: Passing 
Build: [1243](https://travis-ci.org/precice/systemtests/builds/619873406) 

Job: [1243.13](https://travis-ci.org/precice/systemtests/jobs/619873419) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e4ce4c7c44a4...33d01ce211d8) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in b2e539f6afe6
 ---> 9b1bb6c6e2c5
Removing intermediate container b2e539f6afe6
Step 3/10 : RUN apk add git bash
 ---> Running in 86a9e4dac67a
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
 ---> 06c9d9b296eb
Removing intermediate container 86a9e4dac67a
Step 4/10 : ARG branch=develop
 ---> Running in 80f69a939750
 ---> 989af3cd88fa
Removing intermediate container 80f69a939750
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in f83d4f975fbf
[91mCloning into 'tutorials'...
[0m ---> 0b0ab85e0bfe
Removing intermediate container f83d4f975fbf
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in f61888bef9a5
 ---> 3aaf01233e16
Removing intermediate container f61888bef9a5
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 3609bf34782e
 ---> 064311ff362b
Removing intermediate container 3609bf34782e
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 5500fc1800df
 ---> 2574e0664626
Removing intermediate container 5500fc1800df
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b7d20593f1d2
 ---> 12b9045d3bb1
Removing intermediate container b7d20593f1d2
Step 10/10 : USER [secure]
 ---> Running in c27f4006f2dc
 ---> 8e10e537b3b3
Removing intermediate container c27f4006f2dc
Successfully built 8e10e537b3b3
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6d3b144fba7f852c0ad7843de3be4990e56ece9e8425dacd8392116f41119bf6
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:9d36359d80a50ea5356279b336d42f9531662f8192e58a84fd1367180a79d40c
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
travis_time:end:06628774:start=1575333176028140255,finish=1575333464471816208,duration=288443675953,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:013cd138[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:013cd138:start=1575333469542620815,finish=1575333471197088368,duration=1654467553,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:150544b8[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/619873419/log.txt)