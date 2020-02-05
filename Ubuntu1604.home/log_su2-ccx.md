## Status: Passing 
Build: [1610](https://travis-ci.org/precice/systemtests/builds/646351873) 

Job: [1610.17](https://travis-ci.org/precice/systemtests/jobs/646351891) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 5d697ddc2243
 ---> e2a9b68db39a
Removing intermediate container 5d697ddc2243
Step 3/10 : RUN apk add git bash
 ---> Running in 3f367014326e
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
 ---> dfa8f83d6159
Removing intermediate container 3f367014326e
Step 4/10 : ARG branch=develop
 ---> Running in dd8d7780eaad
 ---> 52b3f5743e0c
Removing intermediate container dd8d7780eaad
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in fdf9db662833
[91mCloning into 'tutorials'...
[0m ---> 66d23c340fae
Removing intermediate container fdf9db662833
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in 7a4203dc07e7
 ---> 202676099c2a
Removing intermediate container 7a4203dc07e7
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 488e1a624a96
 ---> 6cee76a5df3e
Removing intermediate container 488e1a624a96
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 7b6660d100ac
 ---> 3d09e1a7e023
Removing intermediate container 7b6660d100ac
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 107c2923d437
 ---> 17e0b3f39330
Removing intermediate container 107c2923d437
Step 10/10 : USER [secure]
 ---> Running in 9825d92524b5
 ---> 8a135ddd17c7
Removing intermediate container 9825d92524b5
Successfully built 8a135ddd17c7
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:7ebee716256924987da7d6af552b3f2af3b060dce08cbd8bbfe04d340a88ac75
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:643abf74076cdf538e9b11c0663abf86d69ac163a1a497a4ffe024ca763b2424
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
travis_time:end:11e03499:start=1580905287111125696,finish=1580905593484387472,duration=306373261776,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:041bac34[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:041bac34:start=1580905597625440293,finish=1580905599045004711,duration=1419564418,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0bdca9c8[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646351891/log.txt)