## Status: Failure 
Build: [1574](https://travis-ci.org/precice/systemtests/builds/644725337) 

Job: [1574.20](https://travis-ci.org/precice/systemtests/jobs/644725357) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4999f333493e1d71bc360afa644a77d2630ce82e...b42adf2e689a763071326fd2ccb4fad54589f1aa) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/741a9374da6f...6ef13f08e3bc) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 3fc7379ac9f8
 ---> dc73c017ef1f
Removing intermediate container 3fc7379ac9f8
Step 3/8 : RUN apk add git
 ---> Running in 8edfe0666616
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
 ---> 472214a0e6a1
Removing intermediate container 8edfe0666616
Step 4/8 : ARG branch=develop
 ---> Running in 4f8b07277739
 ---> a3d08847a01b
Removing intermediate container 4f8b07277739
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 3f636f63638c
[91mCloning into 'tutorials'...
[0m ---> 98fa36da480e
Removing intermediate container 3f636f63638c
Step 6/8 : RUN mkdir configs && sed -i 's|<m2n:sockets from="HeatDirichlet" to="HeatNeumann"/>|<m2n:sockets from="HeatDirichlet" to="HeatNeumann" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"/>|g' $tutorial_path/[secure]-config.xml
 ---> Running in 1f20f67aa847
 ---> 251326001803
Removing intermediate container 1f20f67aa847
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7d60cf365986
 ---> 3f6f5fdc94d1
Removing intermediate container 7d60cf365986
Step 8/8 : USER [secure]
 ---> Running in 3cbbc5b5a737
 ---> 06744b6c4c66
Removing intermediate container 3cbbc5b5a737

Successfully built 06744b6c4c66
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:0e1bdce31436db0885ca600968cf1f0375ea614fe6caaf19a8800d3de972784a
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: .gitkeep
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatDirichlet-iterations.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-convergence.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-iterations.log
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['[secure]-HeatNeumann-iterations.log', '[secure]-HeatDirichlet-iterations.log', '[secure]-HeatNeumann-convergence.log']
Files only in output(right)   : []
travis_time:end:09706b8e:start=1580557638646847890,finish=1580557755160336282,duration=116513488392,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:00583ab2[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/644725357/log.txt)