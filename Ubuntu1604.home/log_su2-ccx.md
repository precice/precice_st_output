## Status: Passing 
Build: [1070](https://travis-ci.org/precice/systemtests/builds/610065106) 

Job: [1070.2](https://travis-ci.org/precice/systemtests/jobs/610065108) 

Triggered by: [push](https://github.com/precice/systemtests/compare/63342ccc971a...ffab6e4cf6eb) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 1799d4704fe6
 ---> d280c4faf797
Removing intermediate container 1799d4704fe6
Step 3/9 : RUN apk add git bash
 ---> Running in 0259d6b649b9
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
 ---> 864707753369
Removing intermediate container 0259d6b649b9
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in dff420d93f02
[91mCloning into 'tutorials'...
[0m ---> 34bcd48d6d57
Removing intermediate container dff420d93f02
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 0f7aa79ea629
 ---> be8a1c9ff1db
Removing intermediate container 0f7aa79ea629
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 6c04f9155c82
 ---> 122d40f27357
Removing intermediate container 6c04f9155c82
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in c28b0309916f
 ---> 9b395f90c877
Removing intermediate container c28b0309916f
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 18928da524a6
 ---> 681772d1cb80
Removing intermediate container 18928da524a6
Step 9/9 : USER [secure]
 ---> Running in b3d8effb97c8
 ---> f10c14afb98d
Removing intermediate container b3d8effb97c8
Successfully built f10c14afb98d
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:7f338c300576d32654a57b0af045919cf2238c8ee743b6ff562cadd232e770e5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:74bad8f70ea22d6671ae756a3d3fc8302444755e5cb6b98282e7ef71a9a3ddf3
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2d785118:start=1573422052274631841,finish=1573422340748328590,duration=288473696749,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:03b63cfa[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:03b63cfa:start=1573422345345435587,finish=1573422347010771228,duration=1665335641,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0284a1a2[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/610065108/log.txt)