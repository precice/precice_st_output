## Status: Passing 
Build: [1064](https://travis-ci.org/precice/systemtests/builds/609194596) 

Job: [1064.21](https://travis-ci.org/precice/systemtests/jobs/609194617) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e3f7960c948e...be03fa4f4575) 

---
Last 100 lines of the job log at the moment of push:
```
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 6363686662f4
 ---> c609a7a890f2
Removing intermediate container 6363686662f4
Step 3/11 : RUN apk add git bash
 ---> Running in 7bdeccadcb22
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
 ---> 684a9c840f66
Removing intermediate container 7bdeccadcb22
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 1425b68a4582
[91mCloning into 'tutorials'...
[0m ---> cc479ad1ca4d
Removing intermediate container 1425b68a4582
Step 5/11 : WORKDIR /
 ---> 9134af7b83b8
Removing intermediate container f3dec684c3b0
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 2d08677fd955
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 1bd6d3756301
 ---> 0914a7d0bc66
Removing intermediate container 1bd6d3756301
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in c0871a5b4c6a
 ---> 928b6da3b921
Removing intermediate container c0871a5b4c6a
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 5f9f4fa169b5
 ---> 0b4fd834bfa6
Removing intermediate container 5f9f4fa169b5
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0e2da5cd7344
 ---> 2e6a44dad613
Removing intermediate container 0e2da5cd7344
Step 11/11 : USER [secure]
 ---> Running in 694d35f6622f
 ---> 99bf1d0f9c2e
Removing intermediate container 694d35f6622f
Successfully built 99bf1d0f9c2e
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:db02b3c0446a6d00253caaef9225a0efb1006e1666f2f6e885771b8784c2dc22
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:deabf18e2f2c68fdcf0398d3a3bc52a570d361a4a575d2ac36fd4b9a09927988
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
travis_time:end:0ed2880f:start=1573218655070026286,finish=1573218803088192074,duration=148018165788,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:015baf9e[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:015baf9e:start=1573218807809337729,finish=1573218809549198437,duration=1739860708,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0144d1a6[0KSuccessfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/609194617/log.txt)