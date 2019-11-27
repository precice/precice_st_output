## Status: Passing 
Build: [1161](https://travis-ci.org/precice/systemtests/builds/617683464) 

Job: [1161.13](https://travis-ci.org/precice/systemtests/jobs/617683478) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ec4ef9d4aedd...6a636c04a7f9) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 72bb462aded2
 ---> ddecbfcfebd2
Removing intermediate container 72bb462aded2
Step 3/10 : RUN apk add git bash
 ---> Running in 28165ba1b537
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
 ---> 70247c1b97f3
Removing intermediate container 28165ba1b537
Step 4/10 : ARG branch=develop
 ---> Running in 49d550cc2bd3
 ---> 4929e835e64d
Removing intermediate container 49d550cc2bd3
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 746b5bdf0b69
[91mCloning into 'tutorials'...
[0m ---> de75bec8a1c1
Removing intermediate container 746b5bdf0b69
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 119d169b672d
 ---> 24c9a78b3f8d
Removing intermediate container 119d169b672d
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in db6f378df3bf
 ---> 1ba8bbd60dfb
Removing intermediate container db6f378df3bf
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 61678229d459
 ---> 713044aba0e2
Removing intermediate container 61678229d459
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 65cf20909a49
 ---> e95e502a8685
Removing intermediate container 65cf20909a49
Step 10/10 : USER [secure]
 ---> Running in 813e2ad3e662
 ---> 3e002cf1b197
Removing intermediate container 813e2ad3e662
Successfully built 3e002cf1b197
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0a00f5ee096947d16d6bfb876909901d1081ec0034c65fbcef93f25e76f36a93
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:41af0c9d3942fc7d9daf45688c8935c8b765bcff3a74dba72db716e6953508e4
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
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0128f03c:start=1574861297542451996,finish=1574861647246091581,duration=349703639585,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0775ad4b[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0775ad4b:start=1574861652757482250,finish=1574861654755232794,duration=1997750544,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:035f2120[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/617683478/log.txt)