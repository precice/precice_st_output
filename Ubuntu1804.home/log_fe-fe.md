## Status: Passing 
Build: [1603](https://travis-ci.org/precice/systemtests/builds/646122956) 

Job: [1603.17](https://travis-ci.org/precice/systemtests/jobs/646122973) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646122956) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 19aa1c5ab2dd
 ---> 87e0e203c3b6
Removing intermediate container 19aa1c5ab2dd
Step 3/8 : RUN apk add git
 ---> Running in 0679d6d8391a
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 332da5408338
Removing intermediate container 0679d6d8391a
Step 4/8 : ARG branch=develop
 ---> Running in 9a096f3bf285
 ---> 9451159e0080
Removing intermediate container 9a096f3bf285
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 37d2233f9550
[91mCloning into 'tutorials'...
[0m ---> 6a1e6e26c4df
Removing intermediate container 37d2233f9550
Step 6/8 : RUN mkdir configs && sed -i 's|<m2n:sockets from="HeatDirichlet" to="HeatNeumann"/>|<m2n:sockets from="HeatDirichlet" to="HeatNeumann" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"/>|g' $tutorial_path/[secure]-config.xml
 ---> Running in a3cbb14089af
 ---> aabf13f9c5ad
Removing intermediate container a3cbb14089af
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b8cd5266f06e
 ---> 3f5545c278b0
Removing intermediate container b8cd5266f06e
Step 8/8 : USER [secure]
 ---> Running in 304680bc8633
 ---> c34f955a57d0
Removing intermediate container 304680bc8633

Successfully built c34f955a57d0
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:d46eb8a14c3b38f0f154e983f3683e3eadba355db5d9e9152992ccb1f04237cf
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-neumann
Creating fenics-adapter-dirichlet
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:1181a2a9:start=1580851263386942612,finish=1580851380273285747,duration=116886343135,event=script[0K[32;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0771f820[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0771f820:start=1580851384547993407,finish=1580851386014471380,duration=1466477973,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:043f6c14[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/646122973/log.txt)