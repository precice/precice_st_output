## Status: Passing 
Build: [1215](https://travis-ci.org/precice/systemtests/builds/618378110) 

Job: [1215.13](https://travis-ci.org/precice/systemtests/jobs/618378123) 

Triggered by: [push](https://github.com/precice/systemtests/compare/95fbdb5c2d24...03b1aca5c88d) 

---
Last 100 lines of the job log at the moment of push:
```
Creating network "testcomposesu2ccx_[secure]comm" with the default driver
Creating volume "testcomposesu2ccx_output" with default driver
Creating volume "testcomposesu2ccx_configs" with default driver
Creating volume "testcomposesu2ccx_input_solid" with default driver
Creating volume "testcomposesu2ccx_input_fluid" with default driver
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/10 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 9de07e0a7409
 ---> 2547e4d2a6bf
Removing intermediate container 9de07e0a7409
Step 3/10 : RUN apk add git bash
 ---> Running in cf4db6917921
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
 ---> 389109cc23d4
Removing intermediate container cf4db6917921
Step 4/10 : ARG branch=develop
 ---> Running in 5d6e1148b883
 ---> 59307f72b315
Removing intermediate container 5d6e1148b883
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d4c958cc89f4
[91mCloning into 'tutorials'...
[0m ---> 92192c66a39c
Removing intermediate container d4c958cc89f4
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in c1aebda0fb73
 ---> 92909354f569
Removing intermediate container c1aebda0fb73
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in b0f797135c44
 ---> 197c23d9c693
Removing intermediate container b0f797135c44
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 1cd4f5083a38
 ---> 473ef834c7cc
Removing intermediate container 1cd4f5083a38
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8735ea75434f
 ---> 1908ad20aad5
Removing intermediate container 8735ea75434f
Step 10/10 : USER [secure]
 ---> Running in c2dd65782383
 ---> c98667cd76e5
Removing intermediate container c2dd65782383
Successfully built c98667cd76e5
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:f03bc14ebf254a2ca23c889b94de17fddd2c30af520067fb4b39363719505637
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:f30973aa6c05ec57516d73291a8d9142d3d762e09414db388341b9ca0d3f1a31
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:028a6ab7:start=1575000996335981021,finish=1575001284927567958,duration=288591586937,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01197c78[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01197c78:start=1575001289449244125,finish=1575001291102564281,duration=1653320156,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:01d69722[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618378123/log.txt)