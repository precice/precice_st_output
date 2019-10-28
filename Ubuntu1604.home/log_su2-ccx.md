## Status: Passing 
Build: [1044](https://travis-ci.org/precice/systemtests/builds/603937404) 

Job: [1044.13](https://travis-ci.org/precice/systemtests/jobs/603937417) 

Triggered by: [push](https://github.com/precice/systemtests/compare/81ea09464169...4d5c1a1b3cfb) 

---
Last 100 lines of the job log at the moment of push:
```
Building tutorial-data
Step 1/9 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 7f1838d13ae8
 ---> 4f6398d4ed0e
Removing intermediate container 7f1838d13ae8
Step 3/9 : RUN apk add git bash
 ---> Running in 10a3b33ff11a
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
 ---> a5853f892450
Removing intermediate container 10a3b33ff11a
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 4ce9ad9f260a
[91mCloning into 'tutorials'...
[0m ---> 76b80e61fec0
Removing intermediate container 4ce9ad9f260a
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in b290502b89e6
 ---> 2900676a5849
Removing intermediate container b290502b89e6
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 6f9a50aad890
 ---> 1f22da5b759d
Removing intermediate container 6f9a50aad890
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in d6b91f941855
 ---> a9713a3635af
Removing intermediate container d6b91f941855
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9c2c24872ce7
 ---> 37024aeccca2
Removing intermediate container 9c2c24872ce7
Step 9/9 : USER [secure]
 ---> Running in 9d2099ab0c0a
 ---> 68c97d9c8368
Removing intermediate container 9d2099ab0c0a
Successfully built 68c97d9c8368
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:1d91c2519eb907bc34323f65542ace4ef96c4df6e00e7df1a80b399fb9922048
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:cb5fb1780684201e30842e79b6e2899b38394f54d8c0c9198b27daed96c1d367
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
travis_time:end:02cfd5b2:start=1572275795177534010,finish=1572276084906300280,duration=289728766270,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1f7c8df4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1f7c8df4:start=1572276089634536758,finish=1572276091301874483,duration=1667337725,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1f04b4eb[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/603937417/log.txt)