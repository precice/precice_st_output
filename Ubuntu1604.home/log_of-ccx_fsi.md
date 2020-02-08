## Status: Passing 
Build: [1614](https://travis-ci.org/precice/systemtests/builds/647676484) 

Job: [1614.25](https://travis-ci.org/precice/systemtests/jobs/647676509) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_solid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_configs" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in e4b81dbcfdc1
 ---> 8988e4d194bf
Removing intermediate container e4b81dbcfdc1
Step 3/12 : RUN apk add git bash
 ---> Running in 3bb32e8af89d
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/11) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/11) Installing ncurses-libs (6.1_p20191130-r0)
(4/11) Installing readline (8.0.1-r0)
(5/11) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/11) Installing ca-certificates (20191127-r1)
(7/11) Installing nghttp2-libs (1.40.0-r0)
(8/11) Installing libcurl (7.67.0-r0)
(9/11) Installing expat (2.2.9-r1)
(10/11) Installing pcre2 (10.34-r1)
(11/11) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r1.trigger
OK: 31 MiB in 25 packages
 ---> ecc35c74ccbf
Removing intermediate container 3bb32e8af89d
Step 4/12 : ARG branch=develop
 ---> Running in 1f5d9d83a7ed
 ---> b5127951e331
Removing intermediate container 1f5d9d83a7ed
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 027bfd125099
[91mCloning into 'tutorials'...
[0m ---> d50b2b4c9481
Removing intermediate container 027bfd125099
Step 6/12 : WORKDIR /
 ---> 8e528ae49a87
Removing intermediate container afb801795591
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 6efd37d91e15
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 108d171c8c93
 ---> fca1cd61ac6f
Removing intermediate container 108d171c8c93
Step 9/12 : RUN mkdir configs &&      sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Calculix\"|<m2n:sockets from=\"Fluid\" to=\"Calculix\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g'     $tutorial_path/[secure]-config.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 07d37018723a
 ---> 675e355c11c8
Removing intermediate container 07d37018723a
Step 10/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 34f8dc5f1ef1
 ---> a3970323984f
Removing intermediate container 34f8dc5f1ef1
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 404441c2583e
 ---> 986071341164
Removing intermediate container 404441c2583e
Step 12/12 : USER [secure]
 ---> Running in 7cfa483040d8
 ---> 83bf30f896ae
Removing intermediate container 7cfa483040d8
Successfully built 83bf30f896ae
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:990e2eb0496da344fc5f991a9a51a5eb22e4ea39de089d506ac166935c723ffc
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:d3d394002d24c8821f5cf241dca4e780697aff40b6ca4142846e14cd57eb1e25
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:0102a1dc:start=1581164117454952162,finish=1581164253917403804,duration=136462451642,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:09572616[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:09572616:start=1581164258113800166,finish=1581164259521217984,duration=1407417818,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:060cd2b7[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/647676509/log.txt)