## Status: Passing 
Build: [1219](https://travis-ci.org/precice/systemtests/builds/618379002) 

Job: [1219.18](https://travis-ci.org/precice/systemtests/jobs/618379020) 

Triggered by: [push](https://github.com/precice/systemtests/compare/7189d2841f25...dca772ad009c) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 208124d36f95
 ---> 7730c924f47e
Removing intermediate container 208124d36f95
Step 3/12 : RUN apk add git
 ---> Running in a4d20a965ac2
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
 ---> e00a39a5688f
Removing intermediate container a4d20a965ac2
Step 4/12 : ARG branch=develop
 ---> Running in 3b952ab13714
 ---> dcd2afb500a4
Removing intermediate container 3b952ab13714
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 2e54005b60b7
[91mCloning into 'tutorials'...
[0m ---> 94c0a3e0dbe4
Removing intermediate container 2e54005b60b7
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 3747a8a711ba
 ---> 62c2719430c8
Removing intermediate container 3747a8a711ba
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 1db768160016
 ---> 74639b2504a5
Removing intermediate container 1db768160016
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 462f11d9a454
 ---> 90366da97d37
Removing intermediate container 462f11d9a454
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 0466fece4c86
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 9a1f829e0f65
Removing intermediate container 0466fece4c86
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 8d5f73717838
 ---> 565eb36744b6
Removing intermediate container 8d5f73717838
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1b6aa3783589
 ---> 5ec502ae1cf1
Removing intermediate container 1b6aa3783589
Step 12/12 : USER [secure]
 ---> Running in b7a5e1c8fb4d
 ---> afda4f1d637c
Removing intermediate container b7a5e1c8fb4d
Successfully built afda4f1d637c
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:00845e1ffe0b07f596edaae901de7b42ce3f89a08f557de115aa9e47ae051d3f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:b424e6fae6a59b99146108171b7f637ba70410a584627c9a5c1a65cc6dde17d2
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
travis_time:end:117e16d2:start=1575009538106829454,finish=1575009802272751683,duration=264165922229,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:35cc6f3d[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:35cc6f3d:start=1575009807196651502,finish=1575009808951034535,duration=1754383033,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:27a27029[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618379020/log.txt)