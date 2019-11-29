## Status: Passing 
Build: [1214](https://travis-ci.org/precice/systemtests/builds/618377761) 

Job: [1214.19](https://travis-ci.org/precice/systemtests/jobs/618377780) 

Triggered by: [push](https://github.com/precice/systemtests/compare/c0803d891710...b25e633a777f) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> aa75fd8d5297
Removing intermediate container 78eef8a08642
Step 3/12 : RUN apk add git
 ---> Running in c40d32d3f8f3
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
 ---> b3e328c8cf16
Removing intermediate container c40d32d3f8f3
Step 4/12 : ARG branch=develop
 ---> Running in 9b435d6a1410
 ---> 043e60ffb731
Removing intermediate container 9b435d6a1410
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in e60a136af70e
[91mCloning into 'tutorials'...
[0m ---> 04fa543ccf18
Removing intermediate container e60a136af70e
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in e6770e0c48df
 ---> f0e0b85e4ec6
Removing intermediate container e6770e0c48df
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 79fbf986af81
 ---> ee95f6d92c3a
Removing intermediate container 79fbf986af81
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 8c80bbe6a351
 ---> 0ff1c240a271
Removing intermediate container 8c80bbe6a351
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 54eb85fb6fb6
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 7fbe8a553021
Removing intermediate container 54eb85fb6fb6
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 1d98c979b175
 ---> 6bc8d51ac101
Removing intermediate container 1d98c979b175
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in d0306175732d
 ---> 562c11e970cc
Removing intermediate container d0306175732d
Step 12/12 : USER [secure]
 ---> Running in 90708c8ec71d
 ---> 8ea60e54b6c4
Removing intermediate container 90708c8ec71d
Successfully built 8ea60e54b6c4
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:73462a7c759aad84b1e13bb3b5719e6857c653a5eca6b4fc1b537b0eb9582dbe
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:d59720c169bc5ce25e7fa2064af67784140b1230a46c07756cf1c6780f2ba98d
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
travis_time:end:1ae6decc:start=1574999922482880746,finish=1575000193436562961,duration=270953682215,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07fe7194[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07fe7194:start=1575000198509398177,finish=1575000200375722891,duration=1866324714,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0e996dfc[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis
```
[
Full job log](https://api.travis-ci.org/v3/job/618377780/log.txt)