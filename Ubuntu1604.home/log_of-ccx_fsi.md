## Status: Failure 
Build: [1516](https://travis-ci.org/precice/systemtests/builds/641834656) 

Job: [1516.22](https://travis-ci.org/precice/systemtests/jobs/641834678) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/131) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/6e941caa282e...b01641e40c11)
* [systemtests](https://github.com/precice/systemtests/pull/157) 

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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path /tutorials/FSI/flap_perp/OpenFOAM-CalculiX
 ---> Running in 85ec8fa48bd6
 ---> b55e21306004
Removing intermediate container 85ec8fa48bd6
Step 3/12 : RUN apk add git bash
 ---> Running in d1c965110da1
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
 ---> 507eee10652e
Removing intermediate container d1c965110da1
Step 4/12 : ARG branch=develop
 ---> Running in b1c4b9aba664
 ---> d838923cc9c0
Removing intermediate container b1c4b9aba664
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d23542a45856
[91mCloning into 'tutorials'...
[0m ---> 81024f3509a9
Removing intermediate container d23542a45856
Step 6/12 : WORKDIR /
 ---> a695b263bb31
Removing intermediate container 8049055327c6
Step 7/12 : COPY interface_beam.nam fix1_beam.nam all.msh $tutorial_path/Solid/
 ---> b288833d109c
Step 8/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 514be5e59aa5
 ---> 618e807dab24
Removing intermediate container 514be5e59aa5
Step 9/12 : RUN mkdir configs &&      sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Calculix\"|<m2n:sockets from=\"Fluid\" to=\"Calculix\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g'     $tutorial_path/[secure]-config.xml > configs/[secure]-config.xml && cp $tutorial_path/config.yml configs/
 ---> Running in d42614770ddc
 ---> f11311833a46
Removing intermediate container d42614770ddc
Step 10/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in c735bb520c83
 ---> 3074573e461e
Removing intermediate container c735bb520c83
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in bd1af8373f06
 ---> 2e249781e693
Removing intermediate container bd1af8373f06
Step 12/12 : USER [secure]
 ---> Running in df7b10ef8f53
 ---> 5bbbc07bd8cb
Removing intermediate container df7b10ef8f53
Successfully built 5bbbc07bd8cb
Successfully tagged testcomposeofccxfsiubuntu1604homepetsc_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:dd67d0c943bbfec92cf3e03849f208bd44b15e6bdb8e8f136f53cc8b8b360197
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home.petsc-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home.petsc-develop
Digest: sha256:e88684eca52b307048fd62b9caceedb75d9e8fa223e3d77d9944c5c7d822944f
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home.petsc-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-fluid ... 
Creating calculix-adapter-solid ... 
Creating calculix-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home.petsc-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx_fsi.Ubuntu1604.home.PETSc/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:020cbbc3:start=1579989743647946141,finish=1579989817592669145,duration=73944723004,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx_fsi --base Ubuntu1604.home.PETSc" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0eaad854[0K$ python push.py -t of-ccx_fsi
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/641834678/log.txt)