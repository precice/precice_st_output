## Status: Failure 
Build: [1438](https://travis-ci.org/precice/systemtests/builds/635907468) 

Job: [1438.1](https://travis-ci.org/precice/systemtests/jobs/635907469) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb) 

---
Last 100 lines of the job log at the moment of push:
```
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - input_solid:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/calculix-adapter/configs:rw
  su2-adapter:
    command: "/bin/bash -c \"ln -sf /home/[secure]/Data/Input Fluid && \n  ln -sf /home/[secure]/su2-adapter/configs/*\
      \ . &&\n  SU2_CFD Fluid/euler_config_coupled.cfg &&\n  cp flow*.vtk *.csv *.dat\
      \ *SU2*.log /home/[secure]/Data/Output/\"\n"
    container_name: su2-adapter
    depends_on:
    - tutorial-data
    image: [secure]/su2-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 8568a62ccf57
 ---> a69e8da288f1
Removing intermediate container 8568a62ccf57
Step 3/10 : RUN apk add git bash
 ---> Running in 8c3b54623103
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
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 31 MiB in 25 packages
 ---> b6f1a2934300
Removing intermediate container 8c3b54623103
Step 4/10 : ARG branch=develop
 ---> Running in 46f423535b4d
 ---> 203a1f3050f8
Removing intermediate container 46f423535b4d
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in af7a6ae84ba5
[91mCloning into 'tutorials'...
[0m ---> 457d21c602ed
Removing intermediate container af7a6ae84ba5
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 9a071e1a7f85
[91msed: tutorials/FSI/flap_perp/SU2-CalculiX/[secure]-config_serial.xml: No such file or directory
[0mService 'tutorial-data' failed to build: The command '/bin/sh -c mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml' returned a non-zero code: 1
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:0780e780:start=1578818331764974447,finish=1578818342189111177,duration=10424136730,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:176660cc[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635907469/log.txt)