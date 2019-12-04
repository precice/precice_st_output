## Status: Passing 
Build: [1258](https://travis-ci.org/precice/systemtests/builds/620625719) 

Job: [1258.21](https://travis-ci.org/precice/systemtests/jobs/620625740) 

Triggered by: [push](https://github.com/precice/systemtests/compare/23fe0b4a3d6a...ff51dfcb2467) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in b40180bab938
 ---> 0b921346bfa9
Removing intermediate container b40180bab938
Step 3/12 : RUN apk add git bash
 ---> Running in 9f8b048ac41c
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
 ---> 35504e7d4ffd
Removing intermediate container 9f8b048ac41c
Step 4/12 : ARG branch=develop
 ---> Running in 36214239752b
 ---> d21bd3f263a3
Removing intermediate container 36214239752b
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in ac4312fd40f8
[91mCloning into 'tutorials'...
[0m ---> d29aff314413
Removing intermediate container ac4312fd40f8
Step 6/12 : WORKDIR /
 ---> 16bbf94e5910
Removing intermediate container 40293bc9d1de
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> ef896ef23bd4
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in b3fb5ecd24e3
 ---> 1ce0e3cda760
Removing intermediate container b3fb5ecd24e3
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 997af883dc0f
 ---> 65c8f844fb6b
Removing intermediate container 997af883dc0f
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d0c2a2781bda
 ---> e408e7ccdfa3
Removing intermediate container d0c2a2781bda
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in cd4722721526
 ---> b97f35d4e1bf
Removing intermediate container cd4722721526
Step 12/12 : USER [secure]
 ---> Running in 9690be3ed047
 ---> 60c73cdf9eaa
Removing intermediate container 9690be3ed047
Successfully built 60c73cdf9eaa
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:8cd4501581ef6c213ed705adef76ef74c5c514d2ebbda413bcab756637ed995e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:625d14e7ec8201b9f1c193a9957d12272f5c0b750582fb499bf89b522468d693
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
travis_time:end:100de4d0:start=1575471728150706519,finish=1575471874855320361,duration=146704613842,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07f442d0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07f442d0:start=1575471879590613450,finish=1575471881269125488,duration=1678512038,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:11c61d73[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620625740/log.txt)