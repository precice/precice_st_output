## Status: Passing 
Build: [1603](https://travis-ci.org/precice/systemtests/builds/646122956) 

Job: [1603.14](https://travis-ci.org/precice/systemtests/jobs/646122970) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646122956) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 74592de937e8
 ---> 3191a37d681f
Removing intermediate container 74592de937e8
Step 3/10 : RUN apk add git bash
 ---> Running in c82c200bef7f
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/11) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/11) Installing ncurses-libs (6.1_p20191130-r0)
(4/11) Installing readline (8.0.1-r0)
(5/11) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/11) Installing ca-certificates (20191127-r0)
(7/11) Installing nghttp2-libs (1.40.0-r0)
(8/11) Installing libcurl (7.67.0-r0)
(9/11) Installing expat (2.2.9-r1)
(10/11) Installing pcre2 (10.34-r1)
(11/11) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 31 MiB in 25 packages
 ---> 7325112f65dd
Removing intermediate container c82c200bef7f
Step 4/10 : ARG branch=develop
 ---> Running in a9b53d4fc656
 ---> 22edd7d004bd
Removing intermediate container a9b53d4fc656
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in cf53ab4880c6
[91mCloning into 'tutorials'...
[0m ---> 91c58f95f977
Removing intermediate container cf53ab4880c6
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in be91fc6bf052
 ---> 788943821dce
Removing intermediate container be91fc6bf052
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in ab55b2c3f9e2
 ---> e2621c259875
Removing intermediate container ab55b2c3f9e2
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 766eea235d53
 ---> a6f239bd1b6b
Removing intermediate container 766eea235d53
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in d43707d101e2
 ---> f393a1ab5034
Removing intermediate container d43707d101e2
Step 10/10 : USER [secure]
 ---> Running in 9a805d2ddf29
 ---> bb25629242eb
Removing intermediate container 9a805d2ddf29
Successfully built bb25629242eb
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:50013b7e1814a9420fbde5bcdbf460f447110b29ea921e0e99f45dcf2cec30a7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:ca57e3ac53b5a70b44c0b3939188028ca7616f2711ae8f054accaff34837824f
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:0b165bd2:start=1580851263607574966,finish=1580851555002884217,duration=291395309251,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2dd2fe78[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2dd2fe78:start=1580851559381698712,finish=1580851560839529281,duration=1457830569,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:03ae8bb0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646122970/log.txt)