## Status: Passing 
Build: [1248](https://travis-ci.org/precice/systemtests/builds/620247509) 

Job: [1248.21](https://travis-ci.org/precice/systemtests/jobs/620247530) 

Triggered by: [push](https://github.com/precice/systemtests/commit/25da98cf068b) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 53f6d52bf48c
 ---> be70fe710b04
Removing intermediate container 53f6d52bf48c
Step 3/12 : RUN apk add git bash
 ---> Running in 7168150078e6
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
 ---> a2a3cb8f01f3
Removing intermediate container 7168150078e6
Step 4/12 : ARG branch=develop
 ---> Running in 168baf2c6e91
 ---> 2bd73e16b3ac
Removing intermediate container 168baf2c6e91
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in fc7ece64ea19
[91mCloning into 'tutorials'...
[0m ---> f3576b123983
Removing intermediate container fc7ece64ea19
Step 6/12 : WORKDIR /
 ---> d3e741292827
Removing intermediate container 89b3e979aaaf
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> b9aeb43ae88f
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in d44827bf956c
 ---> a0d217e33f76
Removing intermediate container d44827bf956c
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in e60e766c1fe3
 ---> 19d67138e2d3
Removing intermediate container e60e766c1fe3
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 4903ce89a22d
 ---> ac1320e2b886
Removing intermediate container 4903ce89a22d
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ee667db7fed4
 ---> 54dd74100823
Removing intermediate container ee667db7fed4
Step 12/12 : USER [secure]
 ---> Running in bb0a67a932c8
 ---> e470dbd74487
Removing intermediate container bb0a67a932c8
Successfully built e470dbd74487
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:69caf46ee718ee3f9af247de069f7057a5834fe8d16b163d02573e2bb7b6eb84
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:c92152f42dcc9fbbe796699e87875640f2245e90f4db0fc9eba51175bd40cdd8
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:13ef60b0:start=1575400665345598212,finish=1575400811789137656,duration=146443539444,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0ed6dd73[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0ed6dd73:start=1575400816977351531,finish=1575400818938533492,duration=1961181961,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:11d29a22[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620247530/log.txt)