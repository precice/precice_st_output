## Status: Passing 
Build: [1372](https://travis-ci.org/precice/systemtests/builds/630890411) 

Job: [1372.24](https://travis-ci.org/precice/systemtests/jobs/630890445) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 3ec7e3fbab39
 ---> 6a4ea89fb78d
Removing intermediate container 3ec7e3fbab39
Step 3/12 : RUN apk add git bash
 ---> Running in e6ab08968010
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
 ---> 045e6972dbab
Removing intermediate container e6ab08968010
Step 4/12 : ARG branch=develop
 ---> Running in 120b942cc32b
 ---> 9c74f67c0271
Removing intermediate container 120b942cc32b
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in a70c2665dfb9
[91mCloning into 'tutorials'...
[0m ---> 4f55d915af44
Removing intermediate container a70c2665dfb9
Step 6/12 : WORKDIR /
 ---> 25448ece11cd
Removing intermediate container 1382fac57e4e
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 3143461a4863
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 4f748c8f4efa
 ---> 5db3d7eef28a
Removing intermediate container 4f748c8f4efa
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 1aafd2ecd954
 ---> 89e066d17ff1
Removing intermediate container 1aafd2ecd954
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 0fe81fe424f1
 ---> f2a0c6b7fd60
Removing intermediate container 0fe81fe424f1
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b243d6ef9b94
 ---> 4207fd03865f
Removing intermediate container b243d6ef9b94
Step 12/12 : USER [secure]
 ---> Running in ab54d9663189
 ---> 70c4d8f39e07
Removing intermediate container ab54d9663189
Successfully built 70c4d8f39e07
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:74a0f2c6753e144934dcbacbf629e7dd5f7c037b79ac3f747a5260e73c7a64ea
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:f2a0ad816a742c5da0282d69e58aa120181f5085d7837e3157bc71dbedc8d201
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:18fe6d59:start=1577705376227800242,finish=1577705513247327309,duration=137019527067,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0227a2f4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0227a2f4:start=1577705517338507696,finish=1577705518731446078,duration=1392938382,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:116186f7[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/630890445/log.txt)