## Status: Passing 
Build: [1264](https://travis-ci.org/precice/systemtests/builds/621025152) 

Job: [1264.17](https://travis-ci.org/precice/systemtests/jobs/621025169) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4b1d49be8e29...13952c2945a9) 

---
Last 100 lines of the job log at the moment of push:
```
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
Step 1/8 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 34326b0362cc
 ---> ce7f0fdbe1bf
Removing intermediate container 34326b0362cc
Step 3/8 : RUN apk add git
 ---> Running in 654fb19ca671
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
 ---> 5a5b904e16a6
Removing intermediate container 654fb19ca671
Step 4/8 : ARG branch=develop
 ---> Running in b1dff2e390a9
 ---> aa62986f8b6e
Removing intermediate container b1dff2e390a9
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 26dcacd63109
[91mCloning into 'tutorials'...
[0m ---> a1981085181c
Removing intermediate container 26dcacd63109
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in be626b1ac6b2
 ---> 10448254ef3f
Removing intermediate container be626b1ac6b2
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1fab5fb8bfe6
 ---> e3af80557835
Removing intermediate container 1fab5fb8bfe6
Step 8/8 : USER [secure]
 ---> Running in f392096cbfc0
 ---> 202d888e2533
Removing intermediate container f392096cbfc0

Successfully built 202d888e2533
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:4d6e15479ba5c0ec5f56d1e59854fd09e412f35a1ca1ac59cd5d82024a3bb321
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:071184fc:start=1575540468436762251,finish=1575540596766520304,duration=128329758053,event=script[0K[32;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04c646ee[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/621025169/log.txt)