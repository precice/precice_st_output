## Status: Passing 
Build: [1085](https://travis-ci.org/precice/systemtests/builds/611163313) 

Job: [1085.25](https://travis-ci.org/precice/systemtests/jobs/611163338) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 828a5f641c63
 ---> 2c11370b5d95
Removing intermediate container 828a5f641c63
Step 3/11 : RUN apk add git bash
 ---> Running in bba76152af1c
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
 ---> a102745f746e
Removing intermediate container bba76152af1c
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 8bbf301abe60
[91mCloning into 'tutorials'...
[0m ---> baf336c15ea2
Removing intermediate container 8bbf301abe60
Step 5/11 : WORKDIR /
 ---> 8ab31e32ae0d
Removing intermediate container b80171dcd739
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 4a0591ab49b4
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 4a11c6bdfbdb
 ---> 5f1815baa5ba
Removing intermediate container 4a11c6bdfbdb
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 32ffab59201a
 ---> 43f00c5ca71c
Removing intermediate container 32ffab59201a
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 9c0bc6d2a817
 ---> 883cfc40d924
Removing intermediate container 9c0bc6d2a817
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ec5f8a0d4680
 ---> e7b21aba9058
Removing intermediate container ec5f8a0d4680
Step 11/11 : USER [secure]
 ---> Running in 2b9168d6b015
 ---> debb57938505
Removing intermediate container 2b9168d6b015
Successfully built debb57938505
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:81beed55a2cafd61db44e141353255fec3dbf12b52e4193ee814d60b79425526
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:c48e8a9763e28af4d4e88988fb3b8030bbfd5f26759a35199cf1f59557cca478
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:02edd948:start=1573613838137589985,finish=1573613985721474935,duration=147583884950,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0ff1f66c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0ff1f66c:start=1573613990578523019,finish=1573613992325316381,duration=1746793362,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0803f180[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/611163338/log.txt)