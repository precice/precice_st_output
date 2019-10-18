 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599812595) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/efe9b440d9b6...4b854cdf2c7b) 
## Last 100 lines of the job log at the moment of push...
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 1945d4bfea53
 ---> 83f51c56a7c1
Removing intermediate container 1945d4bfea53
Step 3/9 : RUN apk add git bash
 ---> Running in 27a2cff75c8c
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
 ---> 8bdea86ed4c0
Removing intermediate container 27a2cff75c8c
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 614be7e5dac8
[91mCloning into 'tutorials'...
[0m ---> ededb345449c
Removing intermediate container 614be7e5dac8
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 6c9176679e3f
 ---> 656c9b6466fb
Removing intermediate container 6c9176679e3f
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 2604b25a4410
 ---> dc2cae0612b3
Removing intermediate container 2604b25a4410
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in a3c12b0032e2
 ---> 999f0b78db7f
Removing intermediate container a3c12b0032e2
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 17bd64c4611d
 ---> ef907ba7a35c
Removing intermediate container 17bd64c4611d
Step 9/9 : USER [secure]
 ---> Running in 73c2c422d69b
 ---> 54ca21fcf05a
Removing intermediate container 73c2c422d69b
Successfully built 54ca21fcf05a
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:5c5893cdeddb7a611d3ca8329ad0c3427690f896db9cb513cb99d67f8837d36e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:1d51cfbe007f6b5a53feb7ed48e611146fa3a9275dfea3e0988ea7a670359436
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/599812608/log.txt)