## Status: Passing 
Build: [1064](https://travis-ci.org/precice/systemtests/builds/609194596) 

Job: [1064.16](https://travis-ci.org/precice/systemtests/jobs/609194612) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e3f7960c948e...be03fa4f4575) 

---
Last 100 lines of the job log at the moment of push:
```
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/7 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 6203f33c3f0a
 ---> 3edc23262d95
Removing intermediate container 6203f33c3f0a
Step 3/7 : RUN apk add git
 ---> Running in e359c225fe3a
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
 ---> ea12523a95aa
Removing intermediate container e359c225fe3a
Step 4/7 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 346f56dd2c74
[91mCloning into 'tutorials'...
[0m ---> 813948a1edcb
Removing intermediate container 346f56dd2c74
Step 5/7 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in ce6f5fd5b2bd
 ---> 11edf550f2ec
Removing intermediate container ce6f5fd5b2bd
Step 6/7 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 279488ad658b
 ---> 0a94f737bd3f
Removing intermediate container 279488ad658b
Step 7/7 : USER [secure]
 ---> Running in 021d8c5822b7
 ---> ad5cad6350ff
Removing intermediate container 021d8c5822b7

Successfully built ad5cad6350ff
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:274a0a37698d462d410c5912be5b58d5be7542315f33c8016a33630b7c7d6deb
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1112a000:start=1573218280714983389,finish=1573218409740641258,duration=129025657869,event=script[0K[32;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2675b9a4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2675b9a4:start=1573218414461630002,finish=1573218416129166871,duration=1667536869,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:017f6cce[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/609194612/log.txt)