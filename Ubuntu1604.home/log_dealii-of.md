 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583929538) 
## Triggered by: [cron](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4) 
## Last 100 lines of the job log at the moment of push...
```
 
Creating network "testcomposedealiiof_default" with the default driver
Creating network "testcomposedealiiof_[secure]comm" with the default driver
Creating volume "testcomposedealiiof_output" with default driver
Creating volume "testcomposedealiiof_configs" with default driver
Creating volume "testcomposedealiiof_input_dealii" with default driver
Creating volume "testcomposedealiiof_input_of" with default driver
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 9f2da7b7c49e
 ---> 74cf1ed2c8a6
Removing intermediate container 9f2da7b7c49e
Step 3/11 : RUN apk add git
 ---> Running in f813b5d22a7c
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.65.1-r0)
(4/6) Installing expat (2.2.7-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> 4abd303fec8f
Removing intermediate container f813b5d22a7c
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 25c7a4ae0679
[91mCloning into 'tutorials'...
[0m ---> f77b2d629ed1
Removing intermediate container 25c7a4ae0679
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 31d86837b72b
 ---> 1b74e20d7c72
Removing intermediate container 31d86837b72b
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 95c22731aab9
 ---> 4074824a29ed
Removing intermediate container 95c22731aab9
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 49bba32eb718
 ---> 6a4845352b9f
Removing intermediate container 49bba32eb718
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in aebf54ed6678
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> e1e47ab2c8e9
Removing intermediate container aebf54ed6678
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in c4817a14e662
 ---> d4b620f71f57
Removing intermediate container c4817a14e662
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c6d4d6caa82d
 ---> 8aaf29435a06
Removing intermediate container c6d4d6caa82d
Step 11/11 : USER [secure]
 ---> Running in 151704cb0643
 ---> 108c099f8e0d
Removing intermediate container 151704cb0643
Successfully built 108c099f8e0d
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:193947ff1e590caf032a10505ac90c1462765a1ecdf4025f9099eb1f318998a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:1b75e825f5a3a41af29f0024e9bfb467d45705de8a0e646efc0566256f2ffd0a
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
travis_time:end:03580a10:start=1568254648009252018,finish=1568254913904604287,duration=265895352269,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:18424c6e[0K$ python push.py -s -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583929560/log.txt)