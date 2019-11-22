## Status: Passing 
Build: [1130](https://travis-ci.org/precice/systemtests/builds/615348483) 

Job: [1130.25](https://travis-ci.org/precice/systemtests/jobs/615348508) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```

Creating network "testcomposeofccxfsiubuntu1604homepetsc_default" with the default driver
Creating network "testcomposeofccxfsiubuntu1604homepetsc_[secure]comm" with the default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_output" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_fluid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_solid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_configs" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_exchange" with default driver
Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in e247c2ef2611
 ---> d7cabdb1a859
Removing intermediate container e247c2ef2611
Step 3/11 : RUN apk add git bash
 ---> Running in bbd9c633ad97
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
 ---> f4555d67ab2b
Removing intermediate container bbd9c633ad97
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in c0257f2e90f5
[91mCloning into 'tutorials'...
[0m ---> aa2e9ba69ce0
Removing intermediate container c0257f2e90f5
Step 5/11 : WORKDIR /
 ---> cf87dcf1d65a
Removing intermediate container 68e963ab40ee
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 9f2e58857e5e
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 0309e8ea3334
 ---> 5f0044a5e77c
Removing intermediate container 0309e8ea3334
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 335f4bdcb164
 ---> 99e366d1d886
Removing intermediate container 335f4bdcb164
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in cd95b57d7ad8
 ---> d2ee4dfba2bf
Removing intermediate container cd95b57d7ad8
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7905bb9f6914
 ---> ce4e27f081dc
Removing intermediate container 7905bb9f6914
Step 11/11 : USER [secure]
 ---> Running in 8e405a8ae8ae
 ---> 2e212eef51f1
Removing intermediate container 8e405a8ae8ae
Successfully built 2e212eef51f1
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:e6071743807a975d13a109c77a2a7e4f861a98abeb69825ddad7ebb1d971c54f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:32569dacf619440d9699ad2dd884acc84bcccb76e735cce0b32b123dcff9cb5b
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:12b4f5dc:start=1574391526887272016,finish=1574391678083575747,duration=151196303731,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02748a3a:start=1574391683561293720,finish=1574391685672826719,duration=2111532999,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:00b17e40[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/615348508/log.txt)