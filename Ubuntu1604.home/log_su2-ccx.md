## Status: Passing 
Build: [1250](https://travis-ci.org/precice/systemtests/builds/620248621) 

Job: [1250.13](https://travis-ci.org/precice/systemtests/jobs/620248634) 

Triggered by: [push](https://github.com/precice/systemtests/compare/25da98cf068b...23fe0b4a3d6a) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in e7debe98da10
 ---> 631bd24071a8
Removing intermediate container e7debe98da10
Step 3/10 : RUN apk add git bash
 ---> Running in 4d1fde12b1db
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
 ---> e21c45d35d62
Removing intermediate container 4d1fde12b1db
Step 4/10 : ARG branch=develop
 ---> Running in 5c6a44b52434
 ---> 69bfcee4a0b7
Removing intermediate container 5c6a44b52434
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in c972bffeb615
[91mCloning into 'tutorials'...
[0m ---> 3567edce426e
Removing intermediate container c972bffeb615
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 62fcefd96cd0
 ---> 87721baf4eeb
Removing intermediate container 62fcefd96cd0
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 4e3e0694fd6b
 ---> 5f95abf251d5
Removing intermediate container 4e3e0694fd6b
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 75e0bfcfa316
 ---> 0f8e1ab0eaf8
Removing intermediate container 75e0bfcfa316
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ff4aae30ddbe
 ---> 790c1c668592
Removing intermediate container ff4aae30ddbe
Step 10/10 : USER [secure]
 ---> Running in 32fa90f8ceaf
 ---> b459be08ad3b
Removing intermediate container 32fa90f8ceaf
Successfully built b459be08ad3b
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:ee2a634dea63b614f007c4d98377f59b8362d44b71c9bfbb9c775185e2c4c94a
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:3733bb93b3b1f0d8541afc1131db18914615d1eeca4523f077bfecd6b71ca172
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:04ca645f:start=1575403599625749105,finish=1575403888438258900,duration=288812509795,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:32444008[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:32444008:start=1575403893533102600,finish=1575403895222394098,duration=1689291498,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:346169f6[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620248634/log.txt)