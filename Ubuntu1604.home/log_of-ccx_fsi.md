## Status: Passing 
Build: [1027](https://travis-ci.org/precice/systemtests/builds/603099773) 

Job: [1027.25](https://travis-ci.org/precice/systemtests/jobs/603099800) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

---
Last 100 lines of the job log at the moment of push:
```
  exchange: {}
  fluid_input: {}
  output: {}
  solid_input: {}

Creating network "testcomposeofccxfsiubuntu1604homepetsc_default" with the default driver
Creating network "testcomposeofccxfsiubuntu1604homepetsc_[secure]comm" with the default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_output" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_fluid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_solid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_configs" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_exchange" with default driver
Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 9a56d1846490
 ---> c20ee6607427
Removing intermediate container 9a56d1846490
Step 3/11 : RUN apk add git bash
 ---> Running in f597559d19fb
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
 ---> 38f6c00e108c
Removing intermediate container f597559d19fb
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 51e675670837
[91mCloning into 'tutorials'...
[0m ---> eca2901962d8
Removing intermediate container 51e675670837
Step 5/11 : WORKDIR /
 ---> 298cda2b8747
Removing intermediate container 8194ec0d1766
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 6f7d092a2fa9
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in af2bf0aefcc9
 ---> dec718aae0e9
Removing intermediate container af2bf0aefcc9
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in c13d5ac3d1ee
 ---> 23902fd3bc72
Removing intermediate container c13d5ac3d1ee
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in f4b9aaef0b0f
 ---> 6a1922ba8337
Removing intermediate container f4b9aaef0b0f
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in dc6e835aa03b
 ---> de4a3a306d3a
Removing intermediate container dc6e835aa03b
Step 11/11 : USER [secure]
 ---> Running in 6b5c28fbf050
 ---> f15ec557fd7e
Removing intermediate container 6b5c28fbf050
Successfully built f15ec557fd7e
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:ebfe001ae34f3c2bdc9eb45464ed079e59a42024120e0d0cf57c416554ad671a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:998fc60f3017143e0e2a3af66efbfa7373a08c06b424ef677c6acd044748489d
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0719ce20:start=1572057866736606146,finish=1572058016759661637,duration=150023055491,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1976cfa0[0K$ python push.py -s -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/603099800/log.txt)