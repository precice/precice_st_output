## Status: Passing 
Build: [1048](https://travis-ci.org/precice/systemtests/builds/605292585) 

Job: [1048.17](https://travis-ci.org/precice/systemtests/jobs/605292602) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
      dockerfile: Dockerfile.tutorial_data
    container_name: tutorial-data
    volumes:
    - input_solid:/tutorials/FSI/flap_perp/SU2-CalculiX/Solid:rw
    - input_fluid:/tutorials/FSI/flap_perp/SU2-CalculiX/Fluid:rw
    - configs:/configs:rw
    - output:/Output:rw
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in afe1aa01860c
 ---> f510d45c3dcd
Removing intermediate container afe1aa01860c
Step 3/9 : RUN apk add git bash
 ---> Running in ff22c60399e9
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
 ---> 0ac9f0b6ad7c
Removing intermediate container ff22c60399e9
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 2c3e2c9e6d65
[91mCloning into 'tutorials'...
[0m ---> 0507d45a736d
Removing intermediate container 2c3e2c9e6d65
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 05a4b5659971
 ---> 9d4cbaccb8a1
Removing intermediate container 05a4b5659971
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 8e78bfe021d0
 ---> 2d1270020245
Removing intermediate container 8e78bfe021d0
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 5faa39e7b72d
 ---> 611e8d3ab7fe
Removing intermediate container 5faa39e7b72d
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 5adf8cdbc816
 ---> db72bbc4afe1
Removing intermediate container 5adf8cdbc816
Step 9/9 : USER [secure]
 ---> Running in 207d951885c4
 ---> 80e7aab8ec1f
Removing intermediate container 207d951885c4
Successfully built 80e7aab8ec1f
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:711f476fc18badf51c238a19f23c63991b879e7c29d89d5a56418d0becaab9f5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:0948627adee6ad3f68befb6de347b788135ff920b2c984c9da5c3ad58404201b
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

```
[
Full job log](https://api.travis-ci.org/v3/job/605292602/log.txt)