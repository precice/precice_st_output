 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581200523) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/a5fe66e3237c...5b9de68efcd3) 
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
 ---> Running in 01a0d1e093cd
 ---> 8d278892a502
Removing intermediate container 01a0d1e093cd
Step 3/9 : RUN apk add git bash
 ---> Running in 29e13be83ce2
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
(8/11) Installing libcurl (7.65.1-r0)
(9/11) Installing expat (2.2.7-r0)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> c9edb6d64024
Removing intermediate container 29e13be83ce2
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 0d7aa2f75ed0
[91mCloning into 'tutorials'...
[0m ---> 83fc52d2ff81
Removing intermediate container 0d7aa2f75ed0
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 9be98ffe779a
 ---> 7e02cbb0fe4c
Removing intermediate container 9be98ffe779a
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in c30ad05d1dbf
 ---> 91666885d9b3
Removing intermediate container c30ad05d1dbf
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 775b4577784f
 ---> 71d3b4e51c1d
Removing intermediate container 775b4577784f
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e1a134bc0151
 ---> 3d82933ed546
Removing intermediate container e1a134bc0151
Step 9/9 : USER [secure]
 ---> Running in 985ad813fd8e
 ---> c2ab7669da19
Removing intermediate container 985ad813fd8e
Successfully built c2ab7669da19
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:e4ceba9207e6feb6ba7b138c24c9fcf8811fbdf85c4fdb6ce35ca4f26b272e3a
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:f9854f6da6b9f536bf11a93d1d44f7bb40484c87d3c22b2f85b51b1492900385
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
 ```
[Full job log](https://api.travis-ci.org/v3/job/581200535/log.txt)