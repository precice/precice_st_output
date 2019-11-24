## Status: Passing 
Build: [1132](https://travis-ci.org/precice/systemtests/builds/616148321) 

Job: [1132.25](https://travis-ci.org/precice/systemtests/jobs/616148348) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 8012c3698997
 ---> 0c96234a3ac1
Removing intermediate container 8012c3698997
Step 3/11 : RUN apk add git bash
 ---> Running in a377da09a7a6
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
 ---> 995c49561384
Removing intermediate container a377da09a7a6
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in c31c08309e94
[91mCloning into 'tutorials'...
[0m ---> 60cf53630f76
Removing intermediate container c31c08309e94
Step 5/11 : WORKDIR /
 ---> 4e2c4c6b016c
Removing intermediate container d49dfc5ab2e2
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 3fc9d9bc0aa6
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 9ecf2766f436
 ---> 65201083ebf4
Removing intermediate container 9ecf2766f436
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 9ffcf9e27b93
 ---> 500c09c70685
Removing intermediate container 9ffcf9e27b93
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in c968f3cd1955
 ---> 0899e94f9282
Removing intermediate container c968f3cd1955
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in a2f516dc1bdf
 ---> 5b9e92e174b1
Removing intermediate container a2f516dc1bdf
Step 11/11 : USER [secure]
 ---> Running in c6b9e49ffebc
 ---> 61ae407dc257
Removing intermediate container c6b9e49ffebc
Successfully built 61ae407dc257
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:fa2d44cbce45fa098edf7936806221c62d7795390f2a8fccccb6627f5a3dfbb2
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:ff36b14e0114960f8a3d857c9c0366e32bc05a4eea40fedbe4901c8a66f4fd2e
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
travis_time:end:0a417b3e:start=1574564318967849919,finish=1574564466562952671,duration=147595102752,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02ac6ee0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02ac6ee0:start=1574564471247093146,finish=1574564472914048203,duration=1666955057,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1c13dcc0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/616148348/log.txt)