## Status: Passing 
Build: [1598](https://travis-ci.org/precice/systemtests/builds/645892844) 

Job: [1598.17](https://travis-ci.org/precice/systemtests/jobs/645892867) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/07c487419fcd18bdb04b9d9fef13c8b1318f3bef...6213c52a25101c0051df0fbc215ba9f941209daa) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 9b79063937ea
 ---> 581d15d2faad
Removing intermediate container 9b79063937ea
Step 3/10 : RUN apk add git bash
 ---> Running in cb21cefb5896
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
 ---> cb9154557c67
Removing intermediate container cb21cefb5896
Step 4/10 : ARG branch=develop
 ---> Running in 9a2be63e8985
 ---> c27ae77aae17
Removing intermediate container 9a2be63e8985
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 606945d51d6e
[91mCloning into 'tutorials'...
[0m ---> e5aac56bcd5b
Removing intermediate container 606945d51d6e
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in cb4f48a958da
 ---> e6dae482791d
Removing intermediate container cb4f48a958da
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in d79e8209499f
 ---> 2191f8cfeb59
Removing intermediate container d79e8209499f
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 095c5eff9a19
 ---> fa59bf93daa8
Removing intermediate container 095c5eff9a19
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9d6732e169ee
 ---> e1aee6dd26c3
Removing intermediate container 9d6732e169ee
Step 10/10 : USER [secure]
 ---> Running in 71e50275d110
 ---> 724bc5a30109
Removing intermediate container 71e50275d110
Successfully built 724bc5a30109
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:cbfc53d937fb813ced19c90ccce35b11a7c01c370364d8469f6fbe0565151b7f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:b77bf9a070fb3c6850bd3d99120fb46e8d0a6147df633e5e266fcc1950af0f41
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_su2-ccx/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_su2-ccx/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:157cfad0:start=1580817525924698601,finish=1580817832463325645,duration=306538627044,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:175543a8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:175543a8:start=1580817836473207725,finish=1580817837818444200,duration=1345236475,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0b2cf028[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645892867/log.txt)