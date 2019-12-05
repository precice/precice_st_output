## Status: Passing 
Build: [1266](https://travis-ci.org/precice/systemtests/builds/621095475) 

Job: [1266.14](https://travis-ci.org/precice/systemtests/jobs/621095489) 

Triggered by: [push](https://github.com/precice/systemtests/compare/13952c2945a9...25edd038370a) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in f7c38be5134c
 ---> f85fb26810e2
Removing intermediate container f7c38be5134c
Step 3/10 : RUN apk add git bash
 ---> Running in 728a9ac6b3cc
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
 ---> 773ca24ba731
Removing intermediate container 728a9ac6b3cc
Step 4/10 : ARG branch=develop
 ---> Running in 3d02d366d2db
 ---> 992fb7957da7
Removing intermediate container 3d02d366d2db
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in a776d1a9d94c
[91mCloning into 'tutorials'...
[0m ---> 51c898cbd80b
Removing intermediate container a776d1a9d94c
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 1599c115e484
 ---> 63e309c4773c
Removing intermediate container 1599c115e484
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a85421f65edc
 ---> 3ad0dc6d30ee
Removing intermediate container a85421f65edc
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 0ea2847fd5a4
 ---> d0c7c672fc11
Removing intermediate container 0ea2847fd5a4
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 33e1f8f3ea52
 ---> 79e8e5bebd76
Removing intermediate container 33e1f8f3ea52
Step 10/10 : USER [secure]
 ---> Running in f1416ce07de6
 ---> 4352b844bd1b
Removing intermediate container f1416ce07de6
Successfully built 4352b844bd1b
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:f054fbf78aa64191b8b965c31b3bd39d364ee39bf12a2a152b43b73605d98db3
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:d92130800908c3537ada06be3afe834984152d2e3b0dd68a90f5dddd1d606e06
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1a589b1f:start=1575552263344594971,finish=1575552532345697148,duration=269001102177,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0ca86f6c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0ca86f6c:start=1575552536656469543,finish=1575552538018185915,duration=1361716372,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1f2ee7e2[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/621095489/log.txt)