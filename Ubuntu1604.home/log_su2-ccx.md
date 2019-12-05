## Status: Passing 
Build: [1268](https://travis-ci.org/precice/systemtests/builds/621181807) 

Job: [1268.13](https://travis-ci.org/precice/systemtests/jobs/621181822) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ff51dfcb2467...d102fedd8227) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/10 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in fc7e40e60e6b
 ---> 27abf2f450d7
Removing intermediate container fc7e40e60e6b
Step 3/10 : RUN apk add git bash
 ---> Running in 34e1b4eb86b1
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
 ---> 1597a8176ca5
Removing intermediate container 34e1b4eb86b1
Step 4/10 : ARG branch=develop
 ---> Running in fa331001d987
 ---> cb44ba458b36
Removing intermediate container fa331001d987
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in e99090cfa87c
[91mCloning into 'tutorials'...
[0m ---> d0288e561ed1
Removing intermediate container e99090cfa87c
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 2f1ac96ceead
 ---> b670c7f1c1bc
Removing intermediate container 2f1ac96ceead
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 353d83d9eebc
 ---> 051f9aa1f49f
Removing intermediate container 353d83d9eebc
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 08818435c14f
 ---> a001e2c5127b
Removing intermediate container 08818435c14f
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8d2045f305a0
 ---> 521d4f8b890f
Removing intermediate container 8d2045f305a0
Step 10/10 : USER [secure]
 ---> Running in c8a7694f244d
 ---> fb76c98d2f5f
Removing intermediate container c8a7694f244d
Successfully built fb76c98d2f5f
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:6637f7ee045d95758de4b8e56b8303623ff0642d9bc57c904e098a34fb548db1
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:5aba1869af452ec46ba4ba2bd7ba5ea7c78339e61b15d837d0256a663dc39cfe
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0dfe25ac:start=1575564888745079987,finish=1575565192515577597,duration=303770497610,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0387d5ba[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/621181822/log.txt)