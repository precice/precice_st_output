## Status: Passing 
Build: [1219](https://travis-ci.org/precice/systemtests/builds/618379002) 

Job: [1219.21](https://travis-ci.org/precice/systemtests/jobs/618379023) 

Triggered by: [push](https://github.com/precice/systemtests/compare/7189d2841f25...dca772ad009c) 

---
Last 100 lines of the job log at the moment of push:
```
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in c4a8ecdea724
 ---> 082c5cd38e82
Removing intermediate container c4a8ecdea724
Step 3/12 : RUN apk add git bash
 ---> Running in 4af3453fed43
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
 ---> afc710f6346b
Removing intermediate container 4af3453fed43
Step 4/12 : ARG branch=develop
 ---> Running in fbfab48f00d2
 ---> 8d4b4dafca77
Removing intermediate container fbfab48f00d2
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 486b581aee7e
[91mCloning into 'tutorials'...
[0m ---> 2678feb1bde8
Removing intermediate container 486b581aee7e
Step 6/12 : WORKDIR /
 ---> a6ddb5fd85e0
Removing intermediate container e041675b8fc3
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 81769603407e
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 23cc23fa062f
 ---> b5d8fdcde5bd
Removing intermediate container 23cc23fa062f
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 71c06628cc02
 ---> e38808808f51
Removing intermediate container 71c06628cc02
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 118b2f71033d
 ---> 9c9d4633e1cf
Removing intermediate container 118b2f71033d
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 22fbed9bd8b8
 ---> 36438508e51c
Removing intermediate container 22fbed9bd8b8
Step 12/12 : USER [secure]
 ---> Running in a5ee1939febe
 ---> 4b7734bc7105
Removing intermediate container a5ee1939febe
Successfully built 4b7734bc7105
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:4c4259e5249ac06ef8c8c580592bd139d3d529832f00912835afed895f505ef0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:cc5c9d32e3eaace0365bcf35d2b6872f2ef5adde992c2cab73f91d06e57996e7
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:19c350ea:start=1575009636555164978,finish=1575009785099037736,duration=148543872758,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04b0f550[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04b0f550:start=1575009790030370242,finish=1575009791784168002,duration=1753797760,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0b25d02a[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618379023/log.txt)