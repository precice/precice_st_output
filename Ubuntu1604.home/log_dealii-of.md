## Status: Passing 
Build: [1133](https://travis-ci.org/precice/systemtests/builds/616444566) 

Job: [1133.22](https://travis-ci.org/precice/systemtests/jobs/616444594) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_configs" with default driver
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
 ---> Running in 1149f3cfb2cd
 ---> 1100377695f3
Removing intermediate container 1149f3cfb2cd
Step 3/11 : RUN apk add git
 ---> Running in 44e6b39fc107
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
 ---> 43d52c0e9f2f
Removing intermediate container 44e6b39fc107
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 4935111eec5e
[91mCloning into 'tutorials'...
[0m ---> 710e1b88730f
Removing intermediate container 4935111eec5e
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in fcda29f756fe
 ---> 5374b1cf6a73
Removing intermediate container fcda29f756fe
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in d4bc04a325a3
 ---> 24fa41b9c3c2
Removing intermediate container d4bc04a325a3
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 53715ada4562
 ---> 2880fb19f8f4
Removing intermediate container 53715ada4562
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in bc2eb69680c3
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 1a7bfc3e9900
Removing intermediate container bc2eb69680c3
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in d91571b290dc
 ---> fe801d790393
Removing intermediate container d91571b290dc
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e1b13168d899
 ---> 3189fbcf75b4
Removing intermediate container e1b13168d899
Step 11/11 : USER [secure]
 ---> Running in f1f1110ab1a2
 ---> 5093b37b1117
Removing intermediate container f1f1110ab1a2
Successfully built 5093b37b1117
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8c87ca91a9ec4828f4c741ce69267ed62fa37009baa759554a9de4867241fc1e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:72a382b7e8d84f7a2ed52f38b7558810f90dca0887172cea8b5b11b98be3262a
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
travis_time:end:10de4b56:start=1574650756950266274,finish=1574651023450027510,duration=266499761236,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01047ec2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01047ec2:start=1574651028549045206,finish=1574651030323020310,duration=1773975104,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0bd7820e[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/616444594/log.txt)