 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584619352) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3433ca666766...b4f731a5d60e) 
## Last 100 lines of the job log at the moment of push...
```
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
 ---> Running in bff923d3e210
 ---> f523935d84f3
Removing intermediate container bff923d3e210
Step 3/11 : RUN apk add git bash
 ---> Running in 8d99a26679e7
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
(8/11) Installing libcurl (7.65.1-r0)
(9/11) Installing expat (2.2.7-r1)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> 9684227cb3a4
Removing intermediate container 8d99a26679e7
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in b1d7eaabdca6
[91mCloning into 'tutorials'...
[0m ---> 90abe9e48377
Removing intermediate container b1d7eaabdca6
Step 5/11 : WORKDIR /
 ---> 7153a48d2384
Removing intermediate container d95003822f3c
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 867dd344f5fe
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 39283b7da801
 ---> 3cbc2e0be3f3
Removing intermediate container 39283b7da801
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 5f2f4c93e958
 ---> 0cf206c7f000
Removing intermediate container 5f2f4c93e958
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in beef6eb54f57
 ---> 522f51499246
Removing intermediate container beef6eb54f57
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b14e61db67a8
 ---> 1b8c0aa806bc
Removing intermediate container b14e61db67a8
Step 11/11 : USER [secure]
 ---> Running in 58cedc89eb7e
 ---> 01ba6d98ce18
Removing intermediate container 58cedc89eb7e
Successfully built 01ba6d98ce18
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:a7cd0c31b119471e11898c43f90e360bfe044f9e59fd7d921faaeba06347d5d8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:6bcbb24a5d5f0a1f56ca05604b342f27e7e0c180eca35b63e2fa9995426b5c12
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/584619373/log.txt)