 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598777025) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/521ff68ed5cc...3211dcc17558) 
## Last 100 lines of the job log at the moment of push...
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/11 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in b4effd298edc
 ---> aab63ec4acae
Removing intermediate container b4effd298edc
Step 3/11 : RUN apk add git bash
 ---> Running in 387ab82d4549
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
 ---> ce21f6c158f3
Removing intermediate container 387ab82d4549
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 79cb3fec504e
[91mCloning into 'tutorials'...
[0m ---> 850462aca872
Removing intermediate container 79cb3fec504e
Step 5/11 : WORKDIR /
 ---> 3fbb7a01805a
Removing intermediate container 47e8fde16412
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> fd11447f9ef8
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 18154d7e0046
 ---> ae7256a0cea9
Removing intermediate container 18154d7e0046
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 55d20ad47995
 ---> 4ae0cbb100e6
Removing intermediate container 55d20ad47995
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 95bc6974e2df
 ---> 6f4e3f32d407
Removing intermediate container 95bc6974e2df
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9296683e95ff
 ---> e0f4f417d4e1
Removing intermediate container 9296683e95ff
Step 11/11 : USER [secure]
 ---> Running in 9873d13bce15
 ---> c3431c330698
Removing intermediate container 9873d13bce15
Successfully built c3431c330698
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:adaf3ab1e6f03f7f4573e33eef67301479eeabf43508a5628c1d22da13620c6c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:08a31e541a52a252167608168a0a564f2c57742e1d02e911a1b8cd9f9a5b2d5b
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
travis_time:end:015b1b55:start=1571251446449772463,finish=1571251598449263253,duration=151999490790,event=script[0K[32;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:03147780[0K$ python push.py -s -t of-ccx_fsi
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598777046/log.txt)