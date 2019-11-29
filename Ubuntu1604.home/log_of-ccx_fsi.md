## Status: Passing 
Build: [1231](https://travis-ci.org/precice/systemtests/builds/618755773) 

Job: [1231.21](https://travis-ci.org/precice/systemtests/jobs/618755794) 

Triggered by: [push](https://github.com/precice/systemtests/compare/3b2ed1c3a41a...be71f6e722f0) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 6d7b67c5ceb6
 ---> 30cbaef8d659
Removing intermediate container 6d7b67c5ceb6
Step 3/12 : RUN apk add git bash
 ---> Running in dd619eb63d42
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
 ---> f04f4775c5e8
Removing intermediate container dd619eb63d42
Step 4/12 : ARG branch=develop
 ---> Running in d53194d5ec49
 ---> 2b2152195934
Removing intermediate container d53194d5ec49
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 5390e9e7470b
[91mCloning into 'tutorials'...
[0m ---> cee04a538cf0
Removing intermediate container 5390e9e7470b
Step 6/12 : WORKDIR /
 ---> c980bfd8783f
Removing intermediate container a8a8c06b9972
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 9f104d56d0ec
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 56f8c46ae199
 ---> aaba9b20994e
Removing intermediate container 56f8c46ae199
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 861350fe653a
 ---> 0ec1c1fef184
Removing intermediate container 861350fe653a
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 012b3160144c
 ---> 182bd92ef55b
Removing intermediate container 012b3160144c
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 796b9efc0a41
 ---> 43163f6930fa
Removing intermediate container 796b9efc0a41
Step 12/12 : USER [secure]
 ---> Running in 7d3d4b96c22a
 ---> 9d0933a9cdf3
Removing intermediate container 7d3d4b96c22a
Successfully built 9d0933a9cdf3
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:f1dc45766e798ea1f3bc7529acb94e9d4e6a502749bfa4413cf79dafa124994d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:5c4959661c4e472ea514bc9f34e046c70e97c2791e15a8eab70d45c48228a8b4
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
travis_time:end:25fa58a0:start=1575066124442820877,finish=1575066271921081339,duration=147478260462,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02ee3cc8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02ee3cc8:start=1575066276410521656,finish=1575066278004377603,duration=1593855947,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0502887f[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/618755794/log.txt)