## Status: Passing 
Build: [1256](https://travis-ci.org/precice/systemtests/builds/620607294) 

Job: [1256.22](https://travis-ci.org/precice/systemtests/jobs/620607327) 

Triggered by: [push](https://github.com/precice/systemtests/compare/db99b1df1818...f0c87c5da690) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 9a8b38670106
 ---> 293a0677ec2c
Removing intermediate container 9a8b38670106
Step 3/12 : RUN apk add git bash
 ---> Running in 0f60c13c56e8
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
 ---> a69979a77003
Removing intermediate container 0f60c13c56e8
Step 4/12 : ARG branch=develop
 ---> Running in 9a91fcd51c35
 ---> f075f4a587a9
Removing intermediate container 9a91fcd51c35
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in c2493c0439df
[91mCloning into 'tutorials'...
[0m ---> 0515cc9c129b
Removing intermediate container c2493c0439df
Step 6/12 : WORKDIR /
 ---> 9e443bb447f3
Removing intermediate container 1097bdfb2b10
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 0ebd427caf86
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in f64a99ad474e
 ---> d6eff4353ac6
Removing intermediate container f64a99ad474e
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 67191a10017e
 ---> 2672221048ac
Removing intermediate container 67191a10017e
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in bea3d04e474d
 ---> 94e5909724d3
Removing intermediate container bea3d04e474d
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 3ff87670a8f9
 ---> 256e9dbd2a0c
Removing intermediate container 3ff87670a8f9
Step 12/12 : USER [secure]
 ---> Running in d6138f85fd5d
 ---> d1e26449b29c
Removing intermediate container d6138f85fd5d
Successfully built d1e26449b29c
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:7d851bd6cde8ddfede9a5df6d87062d648c3ca575fc889f5ae3bf03689afd0f1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:90f7ce1c027fc121f396f61f32504330701c0016146827e99737489bad562514
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
travis_time:end:0b19ae0c:start=1575467973492946271,finish=1575468111365891646,duration=137872945375,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:09c38d26[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:09c38d26:start=1575468115230308972,finish=1575468116618088222,duration=1387779250,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:11c2e1c0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620607327/log.txt)