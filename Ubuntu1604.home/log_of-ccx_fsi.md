## Status: Failure 
Build: [1582](https://travis-ci.org/precice/systemtests/builds/645122283) 

Job: [1582.22](https://travis-ci.org/precice/systemtests/jobs/645122305) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/168) 
Last successful commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```

Creating network "testcomposeofccxfsiubuntu1604homepetsc_default" with the default driver
Creating network "testcomposeofccxfsiubuntu1604homepetsc_[secure]comm" with the default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_output" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_fluid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_solid_input" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_configs" with default driver
Creating volume "testcomposeofccxfsiubuntu1604homepetsc_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 6f6ce3337abc
 ---> 2f45959c107a
Removing intermediate container 6f6ce3337abc
Step 3/12 : RUN apk add git bash
 ---> Running in fd315e3b0c2e
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
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 31 MiB in 25 packages
 ---> 38b56a844c5f
Removing intermediate container fd315e3b0c2e
Step 4/12 : ARG branch=develop
 ---> Running in 7403092c529b
 ---> 7d95adf5dd22
Removing intermediate container 7403092c529b
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 8f07829c6b2d
[91mCloning into 'tutorials'...
[0m ---> 18395ac85d36
Removing intermediate container 8f07829c6b2d
Step 6/12 : WORKDIR /
 ---> 24b04a75bbf5
Removing intermediate container 3c51f2cdf455
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> 78976e07e7b5
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 2f14db7c4722
 ---> d072d280b459
Removing intermediate container 2f14db7c4722
Step 9/12 : RUN mkdir configs &&      sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Calculix\"|<m2n:sockets from=\"Fluid\" to=\"Calculix\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g'     $tutorial_path/[secure]-config.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in d4f89955588f
 ---> 32b590c86de4
Removing intermediate container d4f89955588f
Step 10/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 5b7652a4813a
 ---> aa650bbcbb37
Removing intermediate container 5b7652a4813a
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 13649e804a4b
 ---> 204140f31f63
Removing intermediate container 13649e804a4b
Step 12/12 : USER [secure]
 ---> Running in b50fa82dfbb9
 ---> 2b5d2b7e5307
Removing intermediate container b50fa82dfbb9
Successfully built 2b5d2b7e5307
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:9a83191571c17d4ca1de3d6d1c5325ec44bb7d4412dff2d3524176f8a2a56452
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:f0d3230a746a245d299b4c5d478356198010d869c76d5561e3b5f44b5f3efdbb
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating calculix-adapter-solid
[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1Bx_fsi.Ubuntu1604.home.PETSc/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:0258c855:start=1580667223158689126,finish=1580667298700564102,duration=75541874976,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:001a5f9a[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/645122305/log.txt)