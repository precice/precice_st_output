## Status: Passing 
Build: [1243](https://travis-ci.org/precice/systemtests/builds/619873406) 

Job: [1243.16](https://travis-ci.org/precice/systemtests/jobs/619873422) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e4ce4c7c44a4...33d01ce211d8) 

---
Last 100 lines of the job log at the moment of push:
```
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
Step 1/8 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 7f901d0d9922
 ---> eab23d6e6493
Removing intermediate container 7f901d0d9922
Step 3/8 : RUN apk add git
 ---> Running in 0b34e69da9f6
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
 ---> e857a334adde
Removing intermediate container 0b34e69da9f6
Step 4/8 : ARG branch=develop
 ---> Running in ae98e22bbc59
 ---> 83a3b5a39821
Removing intermediate container ae98e22bbc59
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 21f1f6c3d21a
[91mCloning into 'tutorials'...
[0m ---> 4c542ddc36e4
Removing intermediate container 21f1f6c3d21a
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in 17de683522a3
 ---> 43c70ebaaa0b
Removing intermediate container 17de683522a3
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 77af2da15612
 ---> 9ad57965be54
Removing intermediate container 77af2da15612
Step 8/8 : USER [secure]
 ---> Running in 43888d501520
 ---> dc00ab5b9d5a
Removing intermediate container 43888d501520

Successfully built dc00ab5b9d5a
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:863c8714e5b47c56975b98fa46657f070598f48c15b78479b94462ea9fcc9f85
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0592c538:start=1575333243355695541,finish=1575333371085310695,duration=127729615154,event=script[0K[32;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1a144d1b[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1a144d1b:start=1575333375528013722,finish=1575333377140620395,duration=1612606673,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0c973968[0Kt
```
[
Full job log](https://api.travis-ci.org/v3/job/619873422/log.txt)