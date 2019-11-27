## Status: Passing 
Build: [1158](https://travis-ci.org/precice/systemtests/builds/617673343) 

Job: [1158.13](https://travis-ci.org/precice/systemtests/jobs/617673356) 

Triggered by: [push](https://github.com/precice/systemtests/commit/d97574ad98bc) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in b2f6af232777
 ---> 87d18d298bcb
Removing intermediate container b2f6af232777
Step 3/10 : RUN apk add git bash
 ---> Running in 6df1cc0c6002
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
 ---> 0f477bea4fbe
Removing intermediate container 6df1cc0c6002
Step 4/10 : ARG branch=develop
 ---> Running in 86b8ff5a0c6f
 ---> ca9abf34aeae
Removing intermediate container 86b8ff5a0c6f
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in fb0fd819c2ef
[91mCloning into 'tutorials'...
[0m ---> 63faf4769bbc
Removing intermediate container fb0fd819c2ef
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 2aca8b587996
 ---> 8f7102b6d653
Removing intermediate container 2aca8b587996
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in e593bd7235f2
 ---> 3b45453ca617
Removing intermediate container e593bd7235f2
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in e4a7de810c46
 ---> b3ddb22d964b
Removing intermediate container e4a7de810c46
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0e408d66bf63
 ---> 8b21f52c19a6
Removing intermediate container 0e408d66bf63
Step 10/10 : USER [secure]
 ---> Running in 4b8d0e1c210d
 ---> b437401c40e5
Removing intermediate container 4b8d0e1c210d
Successfully built b437401c40e5
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e785e647d755d552f4259758cd76c1effc7f8449dc68c30cd11ffa75d15fbe5f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:69208a8d06293e08cfbd888dc4de2c2ae4412b9cf61ad36c384abdbbc47ee8d7
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
travis_time:end:00ad9908:start=1574857725632040705,finish=1574858014451441718,duration=288819401013,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0197fec0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0197fec0:start=1574858019416534254,finish=1574858021133371542,duration=1716837288,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:23a572f1[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/617673356/log.txt)