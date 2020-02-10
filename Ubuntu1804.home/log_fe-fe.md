## Status: Passing 
Build: [1650](https://travis-ci.org/precice/systemtests/builds/648350351) 

Job: [1650.20](https://travis-ci.org/precice/systemtests/jobs/648350371) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in d1c625b5a4e1
 ---> c1e34dcd1f44
Removing intermediate container d1c625b5a4e1
Step 3/8 : RUN apk add git
 ---> Running in dbcfb593418d
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
 ---> c17af82ae698
Removing intermediate container dbcfb593418d
Step 4/8 : ARG branch=develop
 ---> Running in 27de1838df77
 ---> d5c03da2afe8
Removing intermediate container 27de1838df77
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in b848abe3bda4
[91mCloning into 'tutorials'...
[0m ---> 3be898d6b876
Removing intermediate container b848abe3bda4
Step 6/8 : RUN mkdir configs && sed -i 's|<m2n:sockets from="HeatDirichlet" to="HeatNeumann"/>|<m2n:sockets from="HeatDirichlet" to="HeatNeumann" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"/>|g' $tutorial_path/[secure]-config.xml
 ---> Running in 211f073b2ead
 ---> bd91341667b3
Removing intermediate container 211f073b2ead
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8961f8032daf
 ---> c91c974a73a9
Removing intermediate container 8961f8032daf
Step 8/8 : USER [secure]
 ---> Running in 106e694d3ad3
 ---> aae253d4290a
Removing intermediate container 106e694d3ad3

Successfully built aae253d4290a
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:9265811329342630e75a43916554f7f0fa30955c0bc1039764329d480bdd4fd1
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann
Creating fenics-adapter-dirichlet
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:265e6516:start=1581335255794814439,finish=1581335371401234290,duration=115606419851,event=script[0K[32;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02c5f0e6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02c5f0e6:start=1581335375798600359,finish=1581335377217204410,duration=1418604051,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1ac7c2b6[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648350371/log.txt)