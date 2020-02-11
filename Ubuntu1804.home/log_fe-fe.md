## Status: Failure 
Build: [1668](https://travis-ci.org/precice/systemtests/builds/648944980) 

Job: [1668.17](https://travis-ci.org/precice/systemtests/jobs/648944997) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/136) 
Last successful commits 
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/741a9374da6f...6ef13f08e3bc)
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
    networks:
      [secure]comm: null
    volumes:
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
    image: [secure]/fenics-adapter-ubuntu1804.home-i_125:latest
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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in b74c8cfa33bf
 ---> 507f474e462f
Removing intermediate container b74c8cfa33bf
Step 3/8 : RUN apk add git
 ---> Running in 0cf6793c470d
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r1)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r1.trigger
OK: 22 MiB in 20 packages
 ---> 75d5d030fcb5
Removing intermediate container 0cf6793c470d
Step 4/8 : ARG branch=develop
 ---> Running in d2cc8d517ab6
 ---> ddf77b0dd166
Removing intermediate container d2cc8d517ab6
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in da5d7f008e35
[91mCloning into 'tutorials'...
[0m ---> 85f6bbc74937
Removing intermediate container da5d7f008e35
Step 6/8 : RUN mkdir configs && sed -i 's|<m2n:sockets from="HeatDirichlet" to="HeatNeumann"/>|<m2n:sockets from="HeatDirichlet" to="HeatNeumann" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"/>|g' $tutorial_path/[secure]-config.xml
 ---> Running in 76972d8406c7
 ---> 8f62cf3e9d34
Removing intermediate container 76972d8406c7
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 81321ea06d49
 ---> 784fd00e0014
Removing intermediate container 81321ea06d49
Step 8/8 : USER [secure]
 ---> Running in cace71453437
 ---> f602c2438ac4
Removing intermediate container cace71453437

Successfully built f602c2438ac4
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-i_125:latest)...
pull access denied for [secure]/fenics-adapter-ubuntu1804.home-i_125, repository does not exist or may require 'docker login'
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-i_125; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1804.home-i_125; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:1f427948:start=1581436784163153884,finish=1581436794727456803,duration=10564302919,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:13a32254[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648944997/log.txt)