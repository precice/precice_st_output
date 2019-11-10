## Status: Passing 
Build: [1068](https://travis-ci.org/precice/systemtests/builds/609999431) 

Job: [1068.18](https://travis-ci.org/precice/systemtests/jobs/609999449) 

Triggered by: [push](https://github.com/precice/systemtests/commit/5cfc071ae529) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_input_dealii" with default driver
Creating volume "testcomposedealiiof_input_of" with default driver
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in e95e7e3837c2
 ---> 979bfe4ffe3e
Removing intermediate container e95e7e3837c2
Step 3/11 : RUN apk add git
 ---> Running in f760e2bf1e3e
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.66.0-r0)
(4/6) Installing expat (2.2.8-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> e1403b3fd2b8
Removing intermediate container f760e2bf1e3e
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 99af1d69f1fb
[91mCloning into 'tutorials'...
[0m ---> 24685e850481
Removing intermediate container 99af1d69f1fb
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 8ca4e399ce75
 ---> 97e70e64dec4
Removing intermediate container 8ca4e399ce75
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in c991840b0f19
 ---> ef3c60f26853
Removing intermediate container c991840b0f19
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in e07a3c179f6a
 ---> 09b5b0ca4f56
Removing intermediate container e07a3c179f6a
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in cadacc74dc29
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> c27cc46bdd7d
Removing intermediate container cadacc74dc29
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 4023707bc31b
 ---> 7f33b2a916e2
Removing intermediate container 4023707bc31b
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1ce0858f7d0e
 ---> 95cc3237c245
Removing intermediate container 1ce0858f7d0e
Step 11/11 : USER [secure]
 ---> Running in fe6c8d78a444
 ---> e1ba9fa5b6f2
Removing intermediate container fe6c8d78a444
Successfully built e1ba9fa5b6f2
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:44c638fda07529b4fa826c3e2802921e4745184ba890cdda8eff73606f82ea90
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:b02ff328d010e68f8067656c8e46e789ee1096a3ec96336d4dda5f854bb824bc
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:01e96860:start=1573408547849683405,finish=1573408818936126191,duration=271086442786,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1e7fa6c8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1e7fa6c8:start=1573408823323496758,finish=1573408824869118265,duration=1545621507,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:01f76ecb[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/609999449/log.txt)