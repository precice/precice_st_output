## Status: Failure 
Build: [1668](https://travis-ci.org/precice/systemtests/builds/648944980) 

Job: [1668.22](https://travis-ci.org/precice/systemtests/jobs/648945002) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/136) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11) 

---
Last 100 lines of the job log at the moment of push:
```
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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 4da19bcfdbd0
 ---> b024fe6d4782
Removing intermediate container 4da19bcfdbd0
Step 3/12 : RUN apk add git bash
 ---> Running in 1dfa14375829
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
 ---> 319f7e20b0f5
Removing intermediate container 1dfa14375829
Step 4/12 : ARG branch=develop
 ---> Running in 19b287fdcabc
 ---> 7b9c899cf7ed
Removing intermediate container 19b287fdcabc
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 82681f57d176
[91mCloning into 'tutorials'...
[0m ---> 2c2ec83f27f7
Removing intermediate container 82681f57d176
Step 6/12 : WORKDIR /
 ---> f51deb49d2a8
Removing intermediate container eb30be17cf6e
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 25a6344a35fe
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in fda872631e42
 ---> 26d74f164a58
Removing intermediate container fda872631e42
Step 9/12 : RUN mkdir configs &&      sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Calculix\"|<m2n:sockets from=\"Fluid\" to=\"Calculix\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g'     $tutorial_path/[secure]-config.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in e4258ad5de50
 ---> 61c04ea4f89d
Removing intermediate container e4258ad5de50
Step 10/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 78cbd363660e
 ---> 02070dcc9f97
Removing intermediate container 78cbd363660e
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 48bbfc77f8f8
 ---> fb574025812d
Removing intermediate container 48bbfc77f8f8
Step 12/12 : USER [secure]
 ---> Running in f49680632c31
 ---> b12effb1881e
Removing intermediate container f49680632c31
Successfully built b12effb1881e
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-i_125:latest)...
pull access denied for [secure]/openfoam-adapter-ubuntu1604.home.petsc-i_125, repository does not exist or may require 'docker login'
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-i_125; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home.petsc-i_125; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:26c8f7d2:start=1581436971311549298,finish=1581436985626551763,duration=14315002465,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1078e398[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648945002/log.txt)