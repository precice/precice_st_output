 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584299312) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/95) 
## Last 100 lines of the job log at the moment of push...
```
     command: '/bin/bash -c "python3 /home/[secure]/Data/Input/heat.py -n && cp *.log
      /home/[secure]/Data/Output"

      '
    container_name: fenics-adapter-neumann
    depends_on:
    - tutorial-data
    image: [secure]/fenics-adapter-ubuntu1804.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - input:/home/[secure]/Data/Input:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home
      dockerfile: Dockerfile.tutorial_data
      network: host
    container_name: tutorial-data
    volumes:
    - output:/Output:rw
    - input:/tutorials/HT/partitioned-heat/fenics-fenics:rw
version: '3.4'
volumes:
  exchange: {}
  input: {}
  output: {}

Creating network "testcomposefefeubuntu1804home_default" with the default driver
Creating network "testcomposefefeubuntu1804home_[secure]comm" with the default driver
Creating volume "testcomposefefeubuntu1804home_output" with default driver
Creating volume "testcomposefefeubuntu1804home_input" with default driver
Creating volume "testcomposefefeubuntu1804home_exchange" with default driver
Building tutorial-data
Step 1/7 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/7 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 88b97ceed5de
 ---> 74dd2c611266
Removing intermediate container 88b97ceed5de
Step 3/7 : RUN apk add git
 ---> Running in 97272b6e3e9e
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
 ---> 08f60854d9cf
Removing intermediate container 97272b6e3e9e
Step 4/7 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in d42c5e416a48
[91mCloning into 'tutorials'...
[0m ---> 1e76de6ff326
Removing intermediate container d42c5e416a48
Step 5/7 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in 16c320b634f5
 ---> 740c03a9592c
Removing intermediate container 16c320b634f5
Step 6/7 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in d3a56de43554
 ---> 66a62c5d4ffe
Removing intermediate container d3a56de43554
Step 7/7 : USER [secure]
 ---> Running in fc0086078574
 ---> da1b9ffdb13c
Removing intermediate container fc0086078574

Successfully built da1b9ffdb13c
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:cddbf8bc8981f084f197b0e7f4d0fb01d39b360c58d0377a01e97f73fbfe0503
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-neumann
Creating fenics-adapter-dirichlet
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:142afbee:start=1568328095535772777,finish=1568328222623479109,duration=127087706332,event=script[0K[32;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:27439bb8[0K$ python push.py -s -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584299328/log.txt)