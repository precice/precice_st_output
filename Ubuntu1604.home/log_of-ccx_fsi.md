## Status: Passing 
Build: [990](https://travis-ci.org/precice/systemtests/builds/600304885) 

Job: [990.21](https://travis-ci.org/precice/systemtests/jobs/600304906) 

Triggered by: [push](https://github.com/precice/systemtests/compare/26213e77ad5d...a84a139c2665) 

---
Last 100 lines of the job log at the moment of push:
```
    volumes:
    - fluid_input:/tutorials/FSI/flap_perp/OpenFOAM-CalculiX/Fluid:rw
    - solid_input:/tutorials/FSI/flap_perp/OpenFOAM-CalculiX/Solid:rw
    - configs:/configs:rw
    - output:/Output:rw
version: '3.0'
volumes:
  configs: {}
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 6ceca2c08bd6
 ---> 996bef153d47
Removing intermediate container 6ceca2c08bd6
Step 3/11 : RUN apk add git bash
 ---> Running in ab349b2fb621
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
 ---> d2efa87dc3bf
Removing intermediate container ab349b2fb621
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 02bc22d01ae7
[91mCloning into 'tutorials'...
[0m ---> 75c57ffaec91
Removing intermediate container 02bc22d01ae7
Step 5/11 : WORKDIR /
 ---> e0ec7d24ad19
Removing intermediate container a276d20cec6e
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 3887ce1161f6
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 7acc9425b8de
 ---> 93e6d9953847
Removing intermediate container 7acc9425b8de
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in d5d1c2349623
 ---> ffbaacf2470d
Removing intermediate container d5d1c2349623
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in b48b7b1d5c2c
 ---> 22fd85807c14
Removing intermediate container b48b7b1d5c2c
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 96ba22ef92ff
 ---> 74831bd71333
Removing intermediate container 96ba22ef92ff
Step 11/11 : USER [secure]
 ---> Running in 77fff6d601fa
 ---> a7b273c896da
Removing intermediate container 77fff6d601fa
Successfully built a7b273c896da
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:fea0f5704f3a0b092665f820b4454a61853613b6d9cc23f83bd54cb30fe9d10f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:9736ceec92568330cea8c349a6d55d56d9200492f992e764e4bd64a6603ba2a5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/600304906/log.txt)