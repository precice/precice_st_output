## Status: Passing 
Build: [1172](https://travis-ci.org/precice/systemtests/builds/618111185) 

Job: [1172.21](https://travis-ci.org/precice/systemtests/jobs/618111206) 

Triggered by: [push](https://github.com/precice/systemtests/compare/i_16) 

---
Last 100 lines of the job log at the moment of push:
```
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 4b2c9dffb5ac
 ---> 313e33b9582d
Removing intermediate container 4b2c9dffb5ac
Step 3/12 : RUN apk add git bash
 ---> Running in 4938e32c2898
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
 ---> 667a6ed7855b
Removing intermediate container 4938e32c2898
Step 4/12 : ARG branch=develop
 ---> Running in 1a53d9396349
 ---> dfa038d2d1e3
Removing intermediate container 1a53d9396349
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1865be15e009
[91mCloning into 'tutorials'...
[0m ---> ed81a81485e2
Removing intermediate container 1865be15e009
Step 6/12 : WORKDIR /
 ---> 78ecb11f7cf5
Removing intermediate container c0743b30d657
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 8dd74a4be57d
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 59a20c838b34
 ---> b96b149d4c9b
Removing intermediate container 59a20c838b34
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 1fbd991442f1
 ---> bc36d487f8b5
Removing intermediate container 1fbd991442f1
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d899e569591f
 ---> b4db704d85a0
Removing intermediate container d899e569591f
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0fe34d3e4c08
 ---> 5c74627086ad
Removing intermediate container 0fe34d3e4c08
Step 12/12 : USER [secure]
 ---> Running in d2f9f51019fa
 ---> cd6042ed694f
Removing intermediate container d2f9f51019fa
Successfully built cd6042ed694f
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:ea604014f6bb910761e6983010e0d9e02e71e9854fef369f3c1354ba16f5fce8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:134708cc63997c531a4e5f119a0c9bb938c16b9045dc7296178ec7d874afa5de
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
travis_time:end:04dfce01:start=1574938895794776364,finish=1574939042962745010,duration=147167968646,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0dc69332[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0dc69332:start=1574939047323685201,finish=1574939048858753846,duration=1535068645,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:060fce10[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618111206/log.txt)