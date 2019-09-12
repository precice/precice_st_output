 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584268195) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/69fcf48ce4a0) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [systemtests](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4) 
## Last 100 lines of the job log at the moment of push...
```
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
 ---> Running in 20af749ef338
 ---> 265541eed08b
Removing intermediate container 20af749ef338
Step 3/11 : RUN apk add git bash
 ---> Running in 97f31896d723
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
(9/11) Installing expat (2.2.7-r0)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> 2c8f38069975
Removing intermediate container 97f31896d723
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 0cd7e610b0c5
[91mCloning into 'tutorials'...
[0m ---> 0380d3749ddf
Removing intermediate container 0cd7e610b0c5
Step 5/11 : WORKDIR /
 ---> 813bac992fde
Removing intermediate container 0b33b0b40405
Step 6/11 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 7c3a68cf04a2
Step 7/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in fcc97b2bff54
 ---> 2e1cbb793dcb
Removing intermediate container fcc97b2bff54
Step 8/11 : RUN mkdir configs &&      sed 's|distribution-type="gather-scatter"|distribution-type="gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in 869fda01a5b9
 ---> e933ea649491
Removing intermediate container 869fda01a5b9
Step 9/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a3af0b1378f3
 ---> 268fc0b4e29c
Removing intermediate container a3af0b1378f3
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5c9d1edef4e4
 ---> a0a0a7dd06e4
Removing intermediate container 5c9d1edef4e4
Step 11/11 : USER [secure]
 ---> Running in 6f24a0514d28
 ---> 95e377f24a80
Removing intermediate container 6f24a0514d28
Successfully built 95e377f24a80
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:5ad442a34e1569ff88047904947efeff61e0864db31b06e717aab97e4403787f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:bc032843da2f7e6ac233e5b2c7a2ff02d646a8b63d546e880af30d08e398a010
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
Traceback (most recent call last):
  File "system_testing.py", line 199, in <module>
    args.force_rebuild, False)
  File "system_testing.py", line 162, in build_run_compare
    run_compose(test, branch, local_[secure], tag, force_rebuild, rm_all)
  File "system_testing.py", line 101, in run_compose
    test_basename in custom_tolerance.keys() else custom_tolerance[test_basename])
AttributeError: 'set' object has no attribute 'keys'
travis_time:end:07c94fb2:start=1568315780126311572,finish=1568315928981480847,duration=148855169275,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:17fa4b27[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584268216/log.txt)