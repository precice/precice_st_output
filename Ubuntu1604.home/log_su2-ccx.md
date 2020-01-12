## Status: Failure 
Build: [1448](https://travis-ci.org/precice/systemtests/builds/635927597) 

Job: [1448.18](https://travis-ci.org/precice/systemtests/jobs/635927615) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:1d0205d8[0K$ python system_testing.py -s su2-ccx
networks:
  [secure]comm: {}
services:
  calculix-adapter:
    command: '/bin/bash -c "ln -sf /home/[secure]/Data/Input Solid;  ln -sf /home/[secure]/calculix-adapter/configs/*
      . && ccx_preCICE -i Solid/flap -[secure]-participant Calculix && cp   Solid/*.dat  Solid/*.cvg
      Solid/*.sta *.log *.out /home/[secure]/Data/Output/"

      '
    container_name: calculix-adapter
    depends_on:
    - tutorial-data
    image: [secure]/calculix-adapter-ubuntu1604.home-develop:latest
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
 ---> Running in db401e834d4c
 ---> 8925ea44c544
Removing intermediate container db401e834d4c
Step 3/10 : RUN apk add git bash
 ---> Running in 0436b0901d2b
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
 ---> 098df974597f
Removing intermediate container 0436b0901d2b
Step 4/10 : ARG branch=develop
 ---> Running in 36016e96d80f
 ---> 531d6dca86f1
Removing intermediate container 36016e96d80f
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in c21d2567e862
[91mCloning into 'tutorials'...
[0m
```
[
Full job log](https://api.travis-ci.org/v3/job/635927615/log.txt)