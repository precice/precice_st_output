## Status: Passing 
Build: [1214](https://travis-ci.org/precice/systemtests/builds/618377761) 

Job: [1214.13](https://travis-ci.org/precice/systemtests/jobs/618377774) 

Triggered by: [push](https://github.com/precice/systemtests/compare/c0803d891710...b25e633a777f) 

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
 ---> Running in 6648ed65c101
 ---> 896a81303cda
Removing intermediate container 6648ed65c101
Step 3/10 : RUN apk add git bash
 ---> Running in adeaad8e9120
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
 ---> aa27402789e3
Removing intermediate container adeaad8e9120
Step 4/10 : ARG branch=develop
 ---> Running in 98b3612726d0
 ---> 1093cd75edac
Removing intermediate container 98b3612726d0
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in f5a0186c4b6e
[91mCloning into 'tutorials'...
[0m ---> 5a6d16bf7815
Removing intermediate container f5a0186c4b6e
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in bf410aa82b17
 ---> 228a1439639a
Removing intermediate container bf410aa82b17
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 5897ca3c0558
 ---> 04302c8d75aa
Removing intermediate container 5897ca3c0558
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 53affeccf60f
 ---> 0d9ff6925e03
Removing intermediate container 53affeccf60f
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c633f260f089
 ---> 22968c4ceee7
Removing intermediate container c633f260f089
Step 10/10 : USER [secure]
 ---> Running in ba62b51d8ba7
 ---> 33ce86f63fb9
Removing intermediate container ba62b51d8ba7
Successfully built 33ce86f63fb9
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:3ee428e2b4f6ca221070db366fc7e5321b9b07c20eb0569a82705ecd33a58afd
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:4981a2f9f0c169267090420e3b6f953c53b23a66e1e65ac9b46955babfcaf0b8
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
travis_time:end:05f26086:start=1574998730100854198,finish=1574999060617891749,duration=330517037551,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:16708026[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:16708026:start=1574999064899973531,finish=1574999066366690625,duration=1466717094,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:115546cd[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618377774/log.txt)