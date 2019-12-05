## Status: Passing 
Build: [1264](https://travis-ci.org/precice/systemtests/builds/621025152) 

Job: [1264.22](https://travis-ci.org/precice/systemtests/jobs/621025174) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4b1d49be8e29...13952c2945a9) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in dcff49312655
 ---> 03d906de9b99
Removing intermediate container dcff49312655
Step 3/12 : RUN apk add git bash
 ---> Running in 949188d6da48
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
 ---> c4c1372bd11d
Removing intermediate container 949188d6da48
Step 4/12 : ARG branch=develop
 ---> Running in 5683321da344
 ---> 958e7f122870
Removing intermediate container 5683321da344
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in b126e9b42f44
[91mCloning into 'tutorials'...
[0m ---> cbedc06f79fe
Removing intermediate container b126e9b42f44
Step 6/12 : WORKDIR /
 ---> 897ce64927ea
Removing intermediate container db3622b4a5bc
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> f88edff3c9f6
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in cd89a2ed6216
 ---> d3ffc195ead1
Removing intermediate container cd89a2ed6216
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in f6a1e1ee2315
 ---> a4a880a67508
Removing intermediate container f6a1e1ee2315
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 3f133c8e5bd6
 ---> 89c351ab4fc7
Removing intermediate container 3f133c8e5bd6
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fa1c8f40c40a
 ---> 9b8161a0b23f
Removing intermediate container fa1c8f40c40a
Step 12/12 : USER [secure]
 ---> Running in 1d06a3440c00
 ---> ad439498d356
Removing intermediate container 1d06a3440c00
Successfully built ad439498d356
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:cd55e994451fa11c513ea705c8a89f756a6f33fe79ed075a2aec40d5f635110e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:7e6e2b092d7decaf8b69a4d13a064f3ba0279986903eaef1d8f3da45847a5968
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
travis_time:end:234d0309:start=1575540696387667307,finish=1575540851695034640,duration=155307367333,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:148dff12[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:148dff12:start=1575540856218673399,finish=1575540857844511464,duration=1625838065,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:026ed924[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/621025174/log.txt)