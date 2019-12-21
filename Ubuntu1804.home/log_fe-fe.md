## Status: Failure 
Build: [1356](https://travis-ci.org/precice/systemtests/builds/628061312) 

Job: [1356.20](https://travis-ci.org/precice/systemtests/jobs/628061332) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81) 

---
Last 100 lines of the job log at the moment of push:
```
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - input:/home/[secure]/Data/Input:rw
  fenics-adapter-neumann:
    command: '/bin/bash -c "cd /home/[secure]  && python3 /home/[secure]/Data/Input/heat.py
      -n -i simple && cp *.log /home/[secure]/Data/Output"

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
Step 1/8 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:7c92a2c6bbcb6b6beff92d0a940779769c2477b807c202954c537e2e0deb9bed
Status: Downloaded newer image for alpine:latest
 ---> c85b8f829d1f
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in d67047beea14
 ---> 8b8e7ae1c9b1
Removing intermediate container d67047beea14
Step 3/8 : RUN apk add git
 ---> Running in 4d7fac2ce1e2
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r0)
(5/6) Installing pcre2 (10.34-r0)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 651e93c19dba
Removing intermediate container 4d7fac2ce1e2
Step 4/8 : ARG branch=develop
 ---> Running in e1f01db83c3d
 ---> 884aa66fcfa5
Removing intermediate container e1f01db83c3d
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in fe870ffc8f2f
[91mCloning into 'tutorials'...
[0m ---> 02ce2a0a7c5c
Removing intermediate container fe870ffc8f2f
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in a4bcf824bc5a
 ---> 10023d8ea757
Removing intermediate container a4bcf824bc5a
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 54e5096006ed
 ---> 24da8dccbd4d
Removing intermediate container 54e5096006ed
Step 8/8 : USER [secure]
 ---> Running in 9ef816037514
 ---> b415ce8bc491
Removing intermediate container 9ef816037514

Successfully built b415ce8bc491
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:0c9642262e9b8d4a9eae23fdb42953f063b9f3940d06ea0ee70f21f005dd4a0d
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/628061332/log.txt)