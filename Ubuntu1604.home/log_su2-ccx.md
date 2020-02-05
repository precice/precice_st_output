## Status: Passing 
Build: [1609](https://travis-ci.org/precice/systemtests/builds/646351628) 

Job: [1609.14](https://travis-ci.org/precice/systemtests/jobs/646351642) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646351628) 

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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 78dd77936149
 ---> 8663acb54b88
Removing intermediate container 78dd77936149
Step 3/10 : RUN apk add git bash
 ---> Running in b9a92fe30b9c
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
 ---> 25e7bb4d6b16
Removing intermediate container b9a92fe30b9c
Step 4/10 : ARG branch=develop
 ---> Running in 99fe35999739
 ---> 8536af596516
Removing intermediate container 99fe35999739
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in f38377d3b85c
[91mCloning into 'tutorials'...
[0m ---> 53297c1eb34e
Removing intermediate container f38377d3b85c
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in 7327193bd006
 ---> 66cef07780aa
Removing intermediate container 7327193bd006
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 760ec609d550
 ---> 7521ee5fb0f6
Removing intermediate container 760ec609d550
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 1f96ae5752af
 ---> 5050c4286f0e
Removing intermediate container 1f96ae5752af
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fbd67b1e002a
 ---> 1d8d89d536a9
Removing intermediate container fbd67b1e002a
Step 10/10 : USER [secure]
 ---> Running in cab4fefb94be
 ---> 05b6a7a63e44
Removing intermediate container cab4fefb94be
Successfully built 05b6a7a63e44
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0fca47ac514dc9fb24d0bf5cab33643511c6695bf6ac37e5be93e5858054bf4b
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:98130325f1211feb90f4744756c68d715b14f5995682c1869d2b4138a39fe0de
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:1f0340ed:start=1580903942766066221,finish=1580904233446313324,duration=290680247103,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:08fbd87a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:08fbd87a:start=1580904237940621374,finish=1580904239385702221,duration=1445080847,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:091fe65a[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/646351642/log.txt)