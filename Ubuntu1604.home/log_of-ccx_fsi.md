## Status: Passing 
Build: [1365](https://travis-ci.org/precice/systemtests/builds/629956799) 

Job: [1365.24](https://travis-ci.org/precice/systemtests/jobs/629956823) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_fluid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_solid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_configs" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 1cab23d170aa
 ---> f8775f43d530
Removing intermediate container 1cab23d170aa
Step 3/12 : RUN apk add git bash
 ---> Running in d355b8dbc61b
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
 ---> 287bf2fcd60d
Removing intermediate container d355b8dbc61b
Step 4/12 : ARG branch=develop
 ---> Running in 33656211877e
 ---> a51f313f9c5b
Removing intermediate container 33656211877e
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 227b70a6e6ba
[91mCloning into 'tutorials'...
[0m ---> 97cb26c23ab8
Removing intermediate container 227b70a6e6ba
Step 6/12 : WORKDIR /
 ---> 9e3638478746
Removing intermediate container f7ae91036173
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> f7cbf78b0f7d
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in fc97ff5d9633
 ---> 5f40f10dc655
Removing intermediate container fc97ff5d9633
Step 9/12 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in c2715ba6e440
 ---> 954ce19f97ca
Removing intermediate container c2715ba6e440
Step 10/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 1fa4aab15612
 ---> 0c22115360d1
Removing intermediate container 1fa4aab15612
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5d82d7a1411f
 ---> 2f4528442d40
Removing intermediate container 5d82d7a1411f
Step 12/12 : USER [secure]
 ---> Running in 198f42e96a15
 ---> 29829d7d6bab
Removing intermediate container 198f42e96a15
Successfully built 29829d7d6bab
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:3a12ddbdf4ff5758237c6a7fdd2e42c964fc2fe65161a4afab6394edaebebb71
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:ecf02576da803067934e616022c8cf9764f8cdd3e6bc471a644e0d7176d3ae5a
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
travis_time:end:1084ac76:start=1577446145929353706,finish=1577446283741552722,duration=137812199016,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2ca62e54[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2ca62e54:start=1577446287750114805,finish=1577446289114431600,duration=1364316795,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1e5c6797[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/629956823/log.txt)