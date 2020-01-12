## Status: Failure 
Build: [1443](https://travis-ci.org/precice/systemtests/builds/635921671) 

Job: [1443.9](https://travis-ci.org/precice/systemtests/jobs/635921680) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/152) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  ln -sf configs/*
      . && cp -r /home/[secure]/Data/Input/0.orig /home/[secure]/Data/Input/0 && blockMesh
      -case /home/[secure]/Data/Input && pimpleDyMFoam -case /home/[secure]/Data/Input
      && cp -r /home/[secure]/Data/Input/. /home/[secure]/Data/Output/Fluid"

      '
    container_name: openfoam-adapter-fluid
    depends_on:
    - tutorial-data
    image: [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - fluid_input:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/openfoam-adapter/configs:rw
    - output:/home/[secure]/Data/Output:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc
      dockerfile: Dockerfile.tutorial_data
    container_name: tutorial-data
    volumes:
    - fluid_input:/tutorials/FSI/flap_perp/OpenFOAM-CalculiX/Fluid:rw
    - solid_input:/tutorials/FSI/flap_perp/OpenFOAM-CalculiX/Solid:rw
    - configs:/configs:rw
    - output:/Output:rw
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  fluid_input: {}
  output: {}
  solid_input: {}

Creating network "testcomposeofccxfsiubuntu1604homepetsc_default" with the default driver
Creating network "testcomposeofccxfsiubuntu1604homepetsc_[secure]comm" with the default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_output" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_fluid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_solid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_configs" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 55a03de3dd1f
 ---> e0a3c7398404
Removing intermediate container 55a03de3dd1f
Step 3/12 : RUN apk add git bash
 ---> Running in a3d4b295b09c
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
 ---> 1a5c2b0906b9
Removing intermediate container a3d4b295b09c
Step 4/12 : ARG branch=develop
 ---> Running in c48ceec372c8
 ---> 668cfecf80d0
Removing intermediate container c48ceec372c8
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 9f98b49cbbc9
[91mCloning into 'tutorials'...
[0m ---> 5de2357c2b6c
Removing intermediate container 9f98b49cbbc9
Step 6/12 : WORKDIR /
 ---> 8e175d5fae17
Removing intermediate container 6aed251866f1
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> c71e8ee584ad
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 66824b86abe7
Service 'tutorial-data' failed to build: The command '/bin/sh -c mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/' returned a non-zero code: 1
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:1d29a394:start=1578823993918078163,finish=1578824005178984427,duration=11260906264,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:009cc3f0[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635921680/log.txt)