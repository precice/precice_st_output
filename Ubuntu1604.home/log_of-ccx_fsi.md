## Status: Passing 
Build: [1609](https://travis-ci.org/precice/systemtests/builds/646351628) 

Job: [1609.22](https://travis-ci.org/precice/systemtests/jobs/646351650) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646351628) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in e7ecc251b233
 ---> 69ab3082872b
Removing intermediate container e7ecc251b233
Step 3/12 : RUN apk add git bash
 ---> Running in 285c71cc577c
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
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 31 MiB in 25 packages
 ---> 3178d844637f
Removing intermediate container 285c71cc577c
Step 4/12 : ARG branch=develop
 ---> Running in f6f328a727be
 ---> c833f58efba3
Removing intermediate container f6f328a727be
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d4fbc6fadc32
[91mCloning into 'tutorials'...
[0m ---> 06cd53db3bc6
Removing intermediate container d4fbc6fadc32
Step 6/12 : WORKDIR /
 ---> bf2cedc17886
Removing intermediate container 73d021182bab
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 00f0545756be
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 99c712d03104
 ---> 082efcea23ca
Removing intermediate container 99c712d03104
Step 9/12 : RUN mkdir configs &&      sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Calculix\"|<m2n:sockets from=\"Fluid\" to=\"Calculix\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g'     $tutorial_path/[secure]-config.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in ab0bdbea8150
 ---> bcbecb5c1740
Removing intermediate container ab0bdbea8150
Step 10/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in d289d575adba
 ---> b280cf873449
Removing intermediate container d289d575adba
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c7a74b8f34a8
 ---> 91ce4180dc94
Removing intermediate container c7a74b8f34a8
Step 12/12 : USER [secure]
 ---> Running in 4e5fdfc1d107
 ---> a2ed326a9872
Removing intermediate container 4e5fdfc1d107
Successfully built a2ed326a9872
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:d6bc85fc8d8198ad8e813269a798d9caa247ab3c509403e2d5eb5fb73442bbaf
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:e87c5ca74557826cc4abd8bb72eb9a557078d971453cb1c059dfc71b24783e3f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:036c9129:start=1580904648977705198,finish=1580904788118278044,duration=139140572846,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646351650/log.txt)