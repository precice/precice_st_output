## Status: Passing 
Build: [1253](https://travis-ci.org/precice/systemtests/builds/620270666) 

Job: [1253.22](https://travis-ci.org/precice/systemtests/jobs/620270688) 

Triggered by: [push](https://github.com/precice/systemtests/compare/d9baae2f9648...db99b1df1818) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 8ca7314bdadf
 ---> f8e7367a5620
Removing intermediate container 8ca7314bdadf
Step 3/12 : RUN apk add git bash
 ---> Running in 4acd26d23011
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
 ---> 82bc9e7a2d9b
Removing intermediate container 4acd26d23011
Step 4/12 : ARG branch=develop
 ---> Running in 277a45318999
 ---> f5f54abf248d
Removing intermediate container 277a45318999
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in dab388fb8fa3
[91mCloning into 'tutorials'...
[0m ---> 9470a2978641
Removing intermediate container dab388fb8fa3
Step 6/12 : WORKDIR /
 ---> 4963e06d8f27
Removing intermediate container 580b1f715f5c
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> eb7d904f9ac2
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in f0b691e3cfb0
 ---> 5b5f1095884b
Removing intermediate container f0b691e3cfb0
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 3396a16159cf
 ---> c7c536a3828d
Removing intermediate container 3396a16159cf
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 602bcaa7b909
 ---> 5aadebe0218a
Removing intermediate container 602bcaa7b909
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ad701bc4d0e4
 ---> 66cc70a15b37
Removing intermediate container ad701bc4d0e4
Step 12/12 : USER [secure]
 ---> Running in dff8ad2ba16e
 ---> 60a02986b90f
Removing intermediate container dff8ad2ba16e
Successfully built 60a02986b90f
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:da1cbc580b85f0b80e7e258be311e3e32966eb1c35a4c455f7b53d3a0b6e5c48
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:6e797acdebdd4b380c14a89c51594830f9ad538551322f056c9f3dafbbb17d1e
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
travis_time:end:011201db:start=1575409320286368961,finish=1575409459776249934,duration=139489880973,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1acd65c4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1acd65c4:start=1575409463592196952,finish=1575409464927128859,duration=1334931907,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0b7d0a00[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620270688/log.txt)