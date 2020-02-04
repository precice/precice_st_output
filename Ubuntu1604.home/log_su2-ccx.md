## Status: Passing 
Build: [1600](https://travis-ci.org/precice/systemtests/builds/645903423) 

Job: [1600.1](https://travis-ci.org/precice/systemtests/jobs/645903424) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/645903423) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 3274d10e0afd
 ---> 86ff0a12abd1
Removing intermediate container 3274d10e0afd
Step 3/10 : RUN apk add git bash
 ---> Running in 52b22285189b
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
 ---> 7fb5dca33467
Removing intermediate container 52b22285189b
Step 4/10 : ARG branch=develop
 ---> Running in c93e3d8ea257
 ---> 35da68e7dd23
Removing intermediate container c93e3d8ea257
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in fe8c58db92d6
[91mCloning into 'tutorials'...
[0m ---> 8ccd39654820
Removing intermediate container fe8c58db92d6
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in ffcb0c17dc66
 ---> ffebfcf7c41f
Removing intermediate container ffcb0c17dc66
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in cbd762639be0
 ---> fc60fb9e121d
Removing intermediate container cbd762639be0
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 603b4581a077
 ---> 8ea4a1deb8dd
Removing intermediate container 603b4581a077
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in a383dfe5c0bb
 ---> 6258109e7f68
Removing intermediate container a383dfe5c0bb
Step 10/10 : USER [secure]
 ---> Running in f077b5807494
 ---> 335974bdcb7c
Removing intermediate container f077b5807494
Successfully built 335974bdcb7c
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:27abdedf761cf5fb2ee1c39ccfc5da48e1de5bf25fd2c14ffce433615a00ab3d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:9a340a7411ac5d49aadb43351b66deae69a52b37d6df461fd97058404589e36c
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:02e32910:start=1580815592130494535,finish=1580815887413357716,duration=295282863181,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0464df0d[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0464df0d:start=1580815892297193098,finish=1580815893878817752,duration=1581624654,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:01a716dd[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/645903424/log.txt)