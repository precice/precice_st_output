 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598441565) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/478596e1ce45) 
## Last 100 lines of the job log at the moment of push...
```
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
 ---> Running in db9c23cca122
 ---> 6a407f62c35b
Removing intermediate container db9c23cca122
Step 3/11 : RUN apk add git bash
 ---> Running in a3c440d2c204
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
 ---> e08f725d7ebb
Removing intermediate container a3c440d2c204
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 807794618d2e
[91mCloning into 'tutorials'...
[0m ---> 262775b87592
Removing intermediate container 807794618d2e
Step 5/11 : WORKDIR /
 ---> b2eb858bae41
Removing intermediate container 847c01ea5376
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 895d83f71edf
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 219f88a7ecd2
 ---> fe6fc0b92a68
Removing intermediate container 219f88a7ecd2
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 3fe63b775345
 ---> da2c2e6c2ae9
Removing intermediate container 3fe63b775345
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in eebc1202683e
 ---> 7e356cbcaa52
Removing intermediate container eebc1202683e
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5532793be952
 ---> bedfe9fb815c
Removing intermediate container 5532793be952
Step 11/11 : USER [secure]
 ---> Running in 4f4fcdd9e31c
 ---> 578de2d57c07
Removing intermediate container 4f4fcdd9e31c
Successfully built 578de2d57c07
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:6f82eff2c03c3589d5dacba71c4e401ea85e319874629c6bdd02f8f725cade4b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:53f88c325add084de02fc5fd13147ca979a6d61f3679c884a4819944d7bd1e23
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
travis_time:start:0ce7d640[0K$ python push.py -s -t of-ccx_fsi
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598441593/log.txt)