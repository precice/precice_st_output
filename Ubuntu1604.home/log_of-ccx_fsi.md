## Status: Passing 
Build: [1268](https://travis-ci.org/precice/systemtests/builds/621181807) 

Job: [1268.21](https://travis-ci.org/precice/systemtests/jobs/621181830) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ff51dfcb2467...d102fedd8227) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 4496cf42acac
 ---> 9e57657f63b0
Removing intermediate container 4496cf42acac
Step 3/12 : RUN apk add git bash
 ---> Running in 5721cb4583b8
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
 ---> 448ef63770a0
Removing intermediate container 5721cb4583b8
Step 4/12 : ARG branch=develop
 ---> Running in 598fc3d7eea8
 ---> 93490e2207db
Removing intermediate container 598fc3d7eea8
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 87e0b34706a4
[91mCloning into 'tutorials'...
[0m ---> cf7c2a9d779b
Removing intermediate container 87e0b34706a4
Step 6/12 : WORKDIR /
 ---> e93f21e9826e
Removing intermediate container 87f37a5a354a
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> d9330b11e17c
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 1ffe6521f433
 ---> 32d4c13e5a7d
Removing intermediate container 1ffe6521f433
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in fe92def5fe41
 ---> 626ba03663b9
Removing intermediate container fe92def5fe41
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d3691ebda302
 ---> 8917bedbe445
Removing intermediate container d3691ebda302
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 94fe000564d6
 ---> 8bd7a4515791
Removing intermediate container 94fe000564d6
Step 12/12 : USER [secure]
 ---> Running in 6efc623c1c28
 ---> 0bf3da0e8c8c
Removing intermediate container 6efc623c1c28
Successfully built 0bf3da0e8c8c
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:d8bfbff16851c80326d5971d73869e66631931416ce0104862fb057357abfbb0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:86046cc9d14dc8d08c9359269dd5d9077c09c76ea494be01a000db4e3408c1f5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:00646020:start=1575565428337346790,finish=1575565566219433871,duration=137882087081,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:12e72699[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:12e72699:start=1575565570011876663,finish=1575565571363973713,duration=1352097050,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:01437cd8[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/621181830/log.txt)