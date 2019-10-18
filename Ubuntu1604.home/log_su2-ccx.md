## Status: Passing 
Build: [982](https://travis-ci.org/precice/systemtests/builds/599837428) 

Job: [982.13](https://travis-ci.org/precice/systemtests/jobs/599837441) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5939c36bf85d...26213e77ad5d) 

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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 3f5464c6100e
 ---> 43ba06c00b61
Removing intermediate container 3f5464c6100e
Step 3/9 : RUN apk add git bash
 ---> Running in 52160ad89b76
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
 ---> aec6b0275ff2
Removing intermediate container 52160ad89b76
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 63bb64dde036
[91mCloning into 'tutorials'...
[0m ---> 12e2f5ece1d0
Removing intermediate container 63bb64dde036
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 4c4bd073b27e
 ---> c941d6df8f3d
Removing intermediate container 4c4bd073b27e
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 75209da0dec3
 ---> 44ffadfc7ca1
Removing intermediate container 75209da0dec3
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in d49ab9504f23
 ---> 21c6395383eb
Removing intermediate container d49ab9504f23
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 6e613aad54ff
 ---> 281134489728
Removing intermediate container 6e613aad54ff
Step 9/9 : USER [secure]
 ---> Running in 4ad0bf22e04e
 ---> 35eba48e999e
Removing intermediate container 4ad0bf22e04e
Successfully built 35eba48e999e
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:8246c1ff2f01eefd1acaf3f7b0fade601ff2599563c308fbcc1c7bdda7fa57d1
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:614c7e78b1e731a03d733c80faf60846c9dfed5c0554c6cb31a18954587a0c29
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/599837441/log.txt)