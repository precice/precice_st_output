## Status: Passing 
Build: [1258](https://travis-ci.org/precice/systemtests/builds/620625719) 

Job: [1258.13](https://travis-ci.org/precice/systemtests/jobs/620625732) 

Triggered by: [push](https://github.com/precice/systemtests/compare/23fe0b4a3d6a...ff51dfcb2467) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 92fd08fb844a
 ---> 778bbd86516a
Removing intermediate container 92fd08fb844a
Step 3/10 : RUN apk add git bash
 ---> Running in c5586484b48e
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
 ---> a34297527f6f
Removing intermediate container c5586484b48e
Step 4/10 : ARG branch=develop
 ---> Running in f9c921c22380
 ---> 408063f61f2b
Removing intermediate container f9c921c22380
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1c548533ec48
[91mCloning into 'tutorials'...
[0m ---> 425b9d58e5ac
Removing intermediate container 1c548533ec48
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 2eecc07951ea
 ---> e30ea9942d77
Removing intermediate container 2eecc07951ea
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in f8e4f043fce7
 ---> e17693ea39cb
Removing intermediate container f8e4f043fce7
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 1cf2464cc1c6
 ---> de88b616f209
Removing intermediate container 1cf2464cc1c6
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8fb201121576
 ---> 3bbd484ab2e4
Removing intermediate container 8fb201121576
Step 10/10 : USER [secure]
 ---> Running in 68c7b1d2a0fb
 ---> f33f77d0e35b
Removing intermediate container 68c7b1d2a0fb
Successfully built f33f77d0e35b
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:deb01da54c83d99ec7925731ac5a5d39cb86258ae7e3101b96d25fa39a3edb32
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:7fdb83c9fec0c86c144967ee5861f2783959ea9c5fd8c06c38b5c4d9fdd29038
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0078a1d7:start=1575470726627595878,finish=1575471015054128751,duration=288426532873,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:285d37b2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:285d37b2:start=1575471019626495494,finish=1575471021220847921,duration=1594352427,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0335103a[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620625732/log.txt)