## Status: Passing 
Build: [1250](https://travis-ci.org/precice/systemtests/builds/620248621) 

Job: [1250.21](https://travis-ci.org/precice/systemtests/jobs/620248642) 

Triggered by: [push](https://github.com/precice/systemtests/compare/25da98cf068b...23fe0b4a3d6a) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 844dcae984be
 ---> e313788ca535
Removing intermediate container 844dcae984be
Step 3/12 : RUN apk add git bash
 ---> Running in 7fd18b928383
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
 ---> 1754b9703d85
Removing intermediate container 7fd18b928383
Step 4/12 : ARG branch=develop
 ---> Running in a46cce8711e1
 ---> 679bb6b345db
Removing intermediate container a46cce8711e1
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in c0bcd2ffa5f7
[91mCloning into 'tutorials'...
[0m ---> 6d2ac4a401d7
Removing intermediate container c0bcd2ffa5f7
Step 6/12 : WORKDIR /
 ---> 787ec55c48a8
Removing intermediate container 295628c97525
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 601dece1ebb7
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 9f57e57a09e6
 ---> 23c975177dff
Removing intermediate container 9f57e57a09e6
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in d16a2cd573b9
 ---> 13b98238efed
Removing intermediate container d16a2cd573b9
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in afbe763efdb3
 ---> 0f8c20a42121
Removing intermediate container afbe763efdb3
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 91a126ba67ff
 ---> 5dbe950306ef
Removing intermediate container 91a126ba67ff
Step 12/12 : USER [secure]
 ---> Running in aba5c7127e47
 ---> 77a89d077286
Removing intermediate container aba5c7127e47
Successfully built 77a89d077286
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:dfb01ef9415e2092539e0033ee5700745d61616df1ebb7d2eecd3fcc0d540113
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:f6f454b722c11b3d218d9547105e22d1189805da867fe8efbce49d7f0fa676a7
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
travis_time:end:1bc94200:start=1575404819514008301,finish=1575404956783932504,duration=137269924203,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:176db84a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:176db84a:start=1575404960864161112,finish=1575404962287350365,duration=1423189253,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1252c6f2[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620248642/log.txt)