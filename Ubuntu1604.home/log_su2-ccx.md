## Status: Passing 
Build: [1006](https://travis-ci.org/precice/systemtests/builds/602019179) 

Job: [1006.13](https://travis-ci.org/precice/systemtests/jobs/602019192) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4ea43c307afb...2f3949cca1ae) 

---
Last 100 lines of the job log at the moment of push:
```
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  input_fluid: {}
  input_solid: {}
  output: {}

Creating network "testcomposesu2ccx_default" with the default driver
Creating network "testcomposesu2ccx_[secure]comm" with the default driver
Creating volume "testcomposesu2ccx_output" with default driver
Creating volume "testcomposesu2ccx_configs" with default driver
Creating volume "testcomposesu2ccx_input_solid" with default driver
Creating volume "testcomposesu2ccx_input_fluid" with default driver
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/9 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 2c8adb18da76
 ---> f93582a33663
Removing intermediate container 2c8adb18da76
Step 3/9 : RUN apk add git bash
 ---> Running in 4affba5c191d
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
 ---> aaaee766dc08
Removing intermediate container 4affba5c191d
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 010becc877e4
[91mCloning into 'tutorials'...
[0m ---> 7a968adb116a
Removing intermediate container 010becc877e4
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 07c06918b2a4
 ---> cd79ab9858d1
Removing intermediate container 07c06918b2a4
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a45e95590917
 ---> f0781efb0967
Removing intermediate container a45e95590917
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 665367b5b560
 ---> 2dd24ebc777c
Removing intermediate container 665367b5b560
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9f6746335b14
 ---> 510d53e773ec
Removing intermediate container 9f6746335b14
Step 9/9 : USER [secure]
 ---> Running in ba206667a6d8
 ---> dc779fd52288
Removing intermediate container ba206667a6d8
Successfully built dc779fd52288
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b3f73dc0fa9a4fa00f021a626671657638f1048b19834dcc5e3a8456ee7dcbc7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:0703693dd6c7f0d0e6770ad56eaab4bce471559052aab78f32cd94f78cfd1041
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0158171b:start=1571867772668217303,finish=1571868061305794323,duration=288637577020,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1d007a9b[0K$ python push.py -s -t su2-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602019192/log.txt)