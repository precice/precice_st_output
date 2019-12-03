## Status: Passing 
Build: [1253](https://travis-ci.org/precice/systemtests/builds/620270666) 

Job: [1253.14](https://travis-ci.org/precice/systemtests/jobs/620270680) 

Triggered by: [push](https://github.com/precice/systemtests/compare/d9baae2f9648...db99b1df1818) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 99a7b7bbd5d7
 ---> 6284a8adcb38
Removing intermediate container 99a7b7bbd5d7
Step 3/10 : RUN apk add git bash
 ---> Running in 3a7bf8830a72
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
 ---> 14804b5fe4c5
Removing intermediate container 3a7bf8830a72
Step 4/10 : ARG branch=develop
 ---> Running in 504d88995990
 ---> 731259449a21
Removing intermediate container 504d88995990
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 870043115ab3
[91mCloning into 'tutorials'...
[0m ---> 04753e42b478
Removing intermediate container 870043115ab3
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 0507df664c2e
 ---> af0e836b9352
Removing intermediate container 0507df664c2e
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 74336e610985
 ---> fac3ca11afd9
Removing intermediate container 74336e610985
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 239e41a08015
 ---> 476ae6bf129b
Removing intermediate container 239e41a08015
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 45d212d7669b
 ---> 59d00f1d81e9
Removing intermediate container 45d212d7669b
Step 10/10 : USER [secure]
 ---> Running in 941c1d165ec5
 ---> 5b9450121875
Removing intermediate container 941c1d165ec5
Successfully built 5b9450121875
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:8d775e4b2e0eb21cc17426a22d12509b6c9f140c0af1bb4071068d94949df68b
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:6c2cf03337d5f71f0266632ffd5b472e9e10104b4c677998f6752eed590a84a1
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
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
travis_time:end:01084b33:start=1575408680103448573,finish=1575409028127560652,duration=348024112079,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:3d5c27b0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:3d5c27b0:start=1575409033208103763,finish=1575409034968374521,duration=1760270758,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0820368e[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620270680/log.txt)