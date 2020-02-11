## Status: Failure 
Build: [1668](https://travis-ci.org/precice/systemtests/builds/648944980) 

Job: [1668.14](https://travis-ci.org/precice/systemtests/jobs/648944994) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/136) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb) 

---
Last 100 lines of the job log at the moment of push:
```
    - output:/home/[secure]/Data/Output:rw
    - input_fluid:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/su2-adapter/configs:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_su2-ccx
      dockerfile: Dockerfile.tutorial_data
    container_name: tutorial-data
    volumes:
    - input_solid:/tutorials/FSI/flap_perp/SU2-CalculiX/Solid:rw
    - input_fluid:/tutorials/FSI/flap_perp/SU2-CalculiX/Fluid:rw
    - configs:/configs:rw
    - output:/Output:rw
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  input_fluid: {}
  input_solid: {}
  output: {}

Creating network "testcomposesu2ccx_default" with the default driver
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
 ---> Running in d7b004c0e115
 ---> 67e5dbb472b9
Removing intermediate container d7b004c0e115
Step 3/10 : RUN apk add git bash
 ---> Running in 8e8f7a05e442
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/11) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/11) Installing ncurses-libs (6.1_p20191130-r0)
(4/11) Installing readline (8.0.1-r0)
(5/11) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/11) Installing ca-certificates (20191127-r1)
(7/11) Installing nghttp2-libs (1.40.0-r0)
(8/11) Installing libcurl (7.67.0-r0)
(9/11) Installing expat (2.2.9-r1)
(10/11) Installing pcre2 (10.34-r1)
(11/11) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r1.trigger
OK: 31 MiB in 25 packages
 ---> 30a4d339f937
Removing intermediate container 8e8f7a05e442
Step 4/10 : ARG branch=develop
 ---> Running in d5a3fac32dfa
 ---> f7db2b2b0424
Removing intermediate container d5a3fac32dfa
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 7efe29a19f60
[91mCloning into 'tutorials'...
[0m ---> 7aba1beb2115
Removing intermediate container 7efe29a19f60
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in 9470830e92e4
 ---> b968a31c44ff
Removing intermediate container 9470830e92e4
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in b6b1e0e937d9
 ---> 1bd66a6c42f2
Removing intermediate container b6b1e0e937d9
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 7a86ad0c7d89
 ---> 6057f2c2d681
Removing intermediate container 7a86ad0c7d89
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in d85affd1d916
 ---> 1348ec506773
Removing intermediate container d85affd1d916
Step 10/10 : USER [secure]
 ---> Running in 64dd6530a2cd
 ---> 029e7ef9a649
Removing intermediate container 64dd6530a2cd
Successfully built 029e7ef9a649
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-i_125:latest)...
pull access denied for [secure]/calculix-adapter-ubuntu1604.home-i_125, repository does not exist or may require 'docker login'
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-i_125; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-i_125; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:1358dbee:start=1581436687518376441,finish=1581436701370421266,duration=13852044825,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:05971f4a[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648944994/log.txt)