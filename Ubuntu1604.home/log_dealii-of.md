## Status: Failure 
Build: [1454](https://travis-ci.org/precice/systemtests/builds/636821308) 

Job: [1454.23](https://travis-ci.org/precice/systemtests/jobs/636821331) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

---
Last 100 lines of the job log at the moment of push:
```
    - openfoam-adapter
    - tutorial-data
    image: [secure]/dealii-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - input_dealii:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/dealii-adapter/configs:rw
    - output:/home/[secure]/Data/Output:rw
  openfoam-adapter:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  ln -sf configs/*
      . && blockMesh -case /home/[secure]/Data/Input && checkMesh -case /home/[secure]/Data/Input
      && pimpleDyMFoam -case /home/[secure]/Data/Input && cp -r /home/[secure]/Data/Input/.
      /home/[secure]/Data/Output/Fluid"

      '
    container_name: openfoam-adapter
    depends_on:
    - tutorial-data
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - input_of:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/openfoam-adapter/configs:rw
    - output:/home/[secure]/Data/Output:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of
      dockerfile: Dockerfile.tutorial_data
    container_name: tutorial-data
    volumes:
    - input_of:/tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid:rw
    - input_dealii:/tutorials/FSI/flap_perp/OpenFOAM-deal.II/Solid:rw
    - configs:/configs:rw
    - output:/Output:rw
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  input_dealii: {}
  input_of: {}
  output: {}

Creating network "testcomposedealiiof_default" with the default driver
Creating network "testcomposedealiiof_[secure]comm" with the default driver
Creating volume "testcomposedealiiof_output" with default driver
Creating volume "testcomposedealiiof_configs" with default driver
Creating volume "testcomposedealiiof_input_dealii" with default driver
Creating volume "testcomposedealiiof_input_of" with default driver
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in d77d9af7856f
 ---> c9b04768f99a
Removing intermediate container d77d9af7856f
Step 3/12 : RUN apk add git
 ---> Running in 3508521ccffa
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> e03b764af546
Removing intermediate container 3508521ccffa
Step 4/12 : ARG branch=develop
 ---> Running in cd0a6312773e
 ---> 43c6c0f3b827
Removing intermediate container cd0a6312773e
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1250f414e011
[91mCloning into 'tutorials'...
[0m ---> 5a6364d6e57c
Removing intermediate container 1250f414e011
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 6b31fbf51527
[91msed: tutorials/FSI/flap_perp/OpenFOAM-deal.II/[secure]-config_serial.xml: No such file or directory
[0mService 'tutorial-data' failed to build: The command '/bin/sh -c mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml' returned a non-zero code: 1
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:03f1e54c:start=1579001697205729917,finish=1579001707284848850,duration=10079118933,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:002d8328[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/636821331/log.txt)