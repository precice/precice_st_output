## Status: Passing 
Build: [1155](https://travis-ci.org/precice/systemtests/builds/617504380) 

Job: [1155.22](https://travis-ci.org/precice/systemtests/jobs/617504402) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

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
 ---> Running in eb9a124c934c
 ---> 91df5e5b5d00
Removing intermediate container eb9a124c934c
Step 3/11 : RUN apk add git
 ---> Running in 51ecc1638093
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
 ---> 6bd820e176aa
Removing intermediate container 51ecc1638093
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 09ea1329aeb1
[91mCloning into 'tutorials'...
[0m ---> a22866ded062
Removing intermediate container 09ea1329aeb1
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in d9aee80eef2f
 ---> 7b1c077ccc4c
Removing intermediate container d9aee80eef2f
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 7fe4f05f11a6
 ---> 87187698d75e
Removing intermediate container 7fe4f05f11a6
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in bd335efc33ad
 ---> 3eec346e8d21
Removing intermediate container bd335efc33ad
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 8ab989995c09
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> c0549b883dfc
Removing intermediate container 8ab989995c09
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in afeed03b6307
 ---> 1d03aaf7726a
Removing intermediate container afeed03b6307
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 572f5853787c
 ---> b995bb9f539a
Removing intermediate container 572f5853787c
Step 11/11 : USER [secure]
 ---> Running in 80e78c1731c9
 ---> 2d669e9c16ad
Removing intermediate container 80e78c1731c9
Successfully built 2d669e9c16ad
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c1b04241d5b9c1e4102b8bd1110c756b0acb05912f874531f62de82e70763643
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:654aa53f9ec05af54889632238d5b7b5fcec0825a2a3f28ec81a224c3b8c629f
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
travis_time:end:04d80e58:start=1574823404927773587,finish=1574823674321061234,duration=269393287647,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02ec5208[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02ec5208:start=1574823678705520186,finish=1574823680322993849,duration=1617473663,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:03276d86[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/617504402/log.txt)