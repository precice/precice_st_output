## Status: Passing 
Build: [1062](https://travis-ci.org/precice/systemtests/builds/609194087) 

Job: [1062.13](https://travis-ci.org/precice/systemtests/jobs/609194102) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f02cef114a79...c96d99257303) 

---
Last 100 lines of the job log at the moment of push:
```
  input_solid: {}
  output: {}

Creating network "testcomposesu2ccx_default" with the default driver
Creating network "testcomposesu2ccx_[secure]comm" with the default driver
Creating volume "testcomposesu2ccx_output" with default driver
Creating volume "testcomposesu2ccx_configs" with default driver
Creating volume "testcomposesu2ccx_input_solid" with default driver
Creating volume "testcomposesu2ccx_input_fluid" with default driver
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/9 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 5da2a4e2fd4d
 ---> ed7b340a8a17
Removing intermediate container 5da2a4e2fd4d
Step 3/9 : RUN apk add git bash
 ---> Running in 3d04c8b8ded5
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
(8/11) Installing libcurl (7.66.0-r0)
(9/11) Installing expat (2.2.8-r0)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> 88e79c0e143c
Removing intermediate container 3d04c8b8ded5
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in a5ba4392fbe3
[91mCloning into 'tutorials'...
[0m ---> fed4fb3c0881
Removing intermediate container a5ba4392fbe3
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in da5b6fa5220c
 ---> 4a7fdffcfde6
Removing intermediate container da5b6fa5220c
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 618756782af4
 ---> e3846ba95f28
Removing intermediate container 618756782af4
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in ca1ab9212de8
 ---> 6af54c9ec1ea
Removing intermediate container ca1ab9212de8
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ebcac40a9e61
 ---> dc1789bebbe5
Removing intermediate container ebcac40a9e61
Step 9/9 : USER [secure]
 ---> Running in 26dd4eb457fe
 ---> 95615a59bfda
Removing intermediate container 26dd4eb457fe
Successfully built 95615a59bfda
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:87855d0dd45e69c0f2d705a60aa523a06ac3ac2021da68f5876a8ff785277ea1
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:660ae90c03873463decfe2db7570871aa430eb8ef8d02ff3b1648b1cbd6117d2
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1ad24fda:start=1573216504062863387,finish=1573216793128086015,duration=289065222628,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02b4b2fd[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02b4b2fd:start=1573216797734996665,finish=1573216799402117967,duration=1667121302,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2336a500[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/609194102/log.txt)