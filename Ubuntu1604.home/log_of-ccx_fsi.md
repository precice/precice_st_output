## Status: Passing 
Build: [1227](https://travis-ci.org/precice/systemtests/builds/618560778) 

Job: [1227.21](https://travis-ci.org/precice/systemtests/jobs/618560801) 

Triggered by: [push](https://github.com/precice/systemtests/compare/d440b60eb25a...e486b1f8560f) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in eae29f5401e8
 ---> 7479ce2917d0
Removing intermediate container eae29f5401e8
Step 3/12 : RUN apk add git bash
 ---> Running in 1ebb641815d1
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
 ---> 4f1208964c34
Removing intermediate container 1ebb641815d1
Step 4/12 : ARG branch=develop
 ---> Running in a31184928c69
 ---> 930eec6c59d4
Removing intermediate container a31184928c69
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in b6d76c7733b6
[91mCloning into 'tutorials'...
[0m ---> 6724c289757f
Removing intermediate container b6d76c7733b6
Step 6/12 : WORKDIR /
 ---> d150d7d6a045
Removing intermediate container 331cd527b164
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 88841271aa28
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 5b8a5e90c194
 ---> 1fb4624c99c1
Removing intermediate container 5b8a5e90c194
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 522421399cec
 ---> db463f860c6c
Removing intermediate container 522421399cec
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in fe2f2adbe946
 ---> c97265f1f3d4
Removing intermediate container fe2f2adbe946
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 225159f19d79
 ---> 1e7a8aa76a9d
Removing intermediate container 225159f19d79
Step 12/12 : USER [secure]
 ---> Running in 365e837d4e6a
 ---> 4620ab0c6436
Removing intermediate container 365e837d4e6a
Successfully built 4620ab0c6436
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:205ed71c700d347f8b4f84a61e45c5947a57258cf43020d81f61569713929870
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:132022f19caafe60e93849f71f0e5b23df9043567d2006c52f29d71778aaab22
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
travis_time:end:132d491c:start=1575030992628459912,finish=1575031140286268653,duration=147657808741,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0038acc3[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0038acc3:start=1575031145145973058,finish=1575031146778160875,duration=1632187817,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:06ab9d94[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618560801/log.txt)