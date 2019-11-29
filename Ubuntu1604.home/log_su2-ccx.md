## Status: Passing 
Build: [1205](https://travis-ci.org/precice/systemtests/builds/618334138) 

Job: [1205.13](https://travis-ci.org/precice/systemtests/jobs/618334151) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f6ac64c472af...3b2ed1c3a41a) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 9aabc37132b2
 ---> d17d62d72726
Removing intermediate container 9aabc37132b2
Step 3/10 : RUN apk add git bash
 ---> Running in 7b92d5387937
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
 ---> ee577552c420
Removing intermediate container 7b92d5387937
Step 4/10 : ARG branch=develop
 ---> Running in 123791b8bab3
 ---> d21d4fb1f8dd
Removing intermediate container 123791b8bab3
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 082c618aca01
[91mCloning into 'tutorials'...
[0m ---> eff059db5f7e
Removing intermediate container 082c618aca01
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in ab61404fc0b9
 ---> 3674a6c52659
Removing intermediate container ab61404fc0b9
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a629018bc4c3
 ---> c84fac910183
Removing intermediate container a629018bc4c3
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in f57ecd69ad87
 ---> 38dbbed8fed1
Removing intermediate container f57ecd69ad87
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2bc10a34ac00
 ---> 01f5402a9a2f
Removing intermediate container 2bc10a34ac00
Step 10/10 : USER [secure]
 ---> Running in dde05e351d69
 ---> 9d5d56ca82c7
Removing intermediate container dde05e351d69
Successfully built 9d5d56ca82c7
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4174e4b498a6d21c3425f9480b871a5c0cacbf300264230688b561c96dd6641b
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:dad04c7db82a975ed9176b64cc2158e80750462f283b29d293b5c20288a3a032
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
travis_time:end:114ecff7:start=1575051705306935304,finish=1575051993818601051,duration=288511665747,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:296a01c0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:296a01c0:start=1575051998296574834,finish=1575051999926081837,duration=1629507003,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:141b7fb0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618334151/log.txt)