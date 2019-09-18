 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586647457) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/cd89b1900540...aac1a14c474b) 
## Last 100 lines of the job log at the moment of push...
```
 version: '3.0'
volumes:
  configs: {}
  exchange: {}
  input_fluid: {}
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 21ae3912ac9e
 ---> a16e04139c79
Removing intermediate container 21ae3912ac9e
Step 3/9 : RUN apk add git bash
 ---> Running in 26c8bd25412e
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
(9/11) Installing expat (2.2.7-r1)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> f7d7311539f6
Removing intermediate container 26c8bd25412e
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in adcd3da048d7
[91mCloning into 'tutorials'...
[0m ---> 7bba99ebae6e
Removing intermediate container adcd3da048d7
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 488edb649388
 ---> 60781933f77f
Removing intermediate container 488edb649388
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in c1b65dd931e2
 ---> 321cdbb3d651
Removing intermediate container c1b65dd931e2
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in f5c9bd05332f
 ---> 74669e7f1540
Removing intermediate container f5c9bd05332f
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 67a4b2ae0dd0
 ---> 1a0e728c82b0
Removing intermediate container 67a4b2ae0dd0
Step 9/9 : USER [secure]
 ---> Running in 799186ad7497
 ---> 925e510f8990
Removing intermediate container 799186ad7497
Successfully built 925e510f8990
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:84976e75900bfcba1bbee046757ac75d8e4d3dd7f1bf22b52c24a52ad68087a6
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:90a3064b2cdc165630d5db8bf3c7947116ee2b3fbcc5ab6f93c5b97a34cb5e95
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:00236265:start=1568830894359321547,finish=1568831183050530300,duration=288691208753,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:03a1d9f8[0K$ python push.py -s -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586647470/log.txt)