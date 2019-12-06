## Status: Passing 
Build: [1274](https://travis-ci.org/precice/systemtests/builds/621545880) 

Job: [1274.13](https://travis-ci.org/precice/systemtests/jobs/621545893) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f9c5ac902029...10d407970668) 

---
Last 100 lines of the job log at the moment of push:
```
Creating network "testcomposesu2ccx_[secure]comm" with the default driver
Creating volume "testcomposesu2ccx_output" with default driver
Creating volume "testcomposesu2ccx_configs" with default driver
Creating volume "testcomposesu2ccx_input_solid" with default driver
Creating volume "testcomposesu2ccx_input_fluid" with default driver
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/10 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 78660a305d73
 ---> 82ea11dbb800
Removing intermediate container 78660a305d73
Step 3/10 : RUN apk add git bash
 ---> Running in 36db8aff3567
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
 ---> 59e19cc748a2
Removing intermediate container 36db8aff3567
Step 4/10 : ARG branch=develop
 ---> Running in cc3ff198c035
 ---> 274d0b93868e
Removing intermediate container cc3ff198c035
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1d90d6cb2dde
[91mCloning into 'tutorials'...
[0m ---> 157197b328d1
Removing intermediate container 1d90d6cb2dde
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 19e83da5e594
 ---> 4fce295eb05a
Removing intermediate container 19e83da5e594
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 43ad7555d812
 ---> 3e71dd4d5a01
Removing intermediate container 43ad7555d812
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 11ea51316af6
 ---> 642f9c1c9ab1
Removing intermediate container 11ea51316af6
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b80c375df900
 ---> e4273e6fbfa0
Removing intermediate container b80c375df900
Step 10/10 : USER [secure]
 ---> Running in 81eac2525bbc
 ---> 43335e07328a
Removing intermediate container 81eac2525bbc
Successfully built 43335e07328a
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:75bfbfa0de7a0980b9fb8b41af07d140b6c711ded78025113c55a2bd36c8254c
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:e861ee14a87063fd2af66dfa7f46d5879d7b82425cfad9b4c7dad5c84c957d0d
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
travis_time:end:000fc41c:start=1575636462489709260,finish=1575636731932993288,duration=269443284028,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02574474[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02574474:start=1575636735716264748,finish=1575636737081178907,duration=1364914159,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1fd69f89[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/621545893/log.txt)