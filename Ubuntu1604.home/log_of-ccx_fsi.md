## Status: Passing 
Build: [1396](https://travis-ci.org/precice/systemtests/builds/632899723) 

Job: [1396.26](https://travis-ci.org/precice/systemtests/jobs/632899749) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> cc0abc535e36
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 2a35fc153e19
 ---> 60e6459ae481
Removing intermediate container 2a35fc153e19
Step 3/12 : RUN apk add git bash
 ---> Running in 90b491f6bec0
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
 ---> f7cd5bc1972b
Removing intermediate container 90b491f6bec0
Step 4/12 : ARG branch=develop
 ---> Running in 56c4cb2e50ac
 ---> bc591d2e18aa
Removing intermediate container 56c4cb2e50ac
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d3f203417228
[91mCloning into 'tutorials'...
[0m ---> 5996314ace7f
Removing intermediate container d3f203417228
Step 6/12 : WORKDIR /
 ---> 3dd946cfc04a
Removing intermediate container 58c56ba6a00a
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 8e3daa68ea4c
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 219af98b0193
 ---> 4c3b50343305
Removing intermediate container 219af98b0193
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 9fe2590e2b13
 ---> d6f6dcf29d4d
Removing intermediate container 9fe2590e2b13
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a254fb7caa53
 ---> 3b52da833798
Removing intermediate container a254fb7caa53
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8fa4bd0c66ea
 ---> 4924ffb37539
Removing intermediate container 8fa4bd0c66ea
Step 12/12 : USER [secure]
 ---> Running in ed5f498d7a69
 ---> 920dbe79cf60
Removing intermediate container ed5f498d7a69
Successfully built 920dbe79cf60
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:77b1c899015546c33d9068c40ed4be8ce50e85b0a2a43849e1cfee59b649214d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:92984f531c6dc143f2edde6eb5b78538b8c666c38e06c9b814f5aea9bd3bd431
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2dc1c63e:start=1578223972930292955,finish=1578224110734387184,duration=137804094229,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:073d89b4:start=1578224114868477014,finish=1578224116187857918,duration=1319380904,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:208cccd4[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/632899749/log.txt)