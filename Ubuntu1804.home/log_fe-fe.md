## Status: Failure 
Build: [1360](https://travis-ci.org/precice/systemtests/builds/629054356) 

Job: [1360.20](https://travis-ci.org/precice/systemtests/jobs/629054382) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 92c50ad5b58e
 ---> 4fea73272b86
Removing intermediate container 92c50ad5b58e
Step 3/8 : RUN apk add git
 ---> Running in e8a440a576c6
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r0)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 02f329a59070
Removing intermediate container e8a440a576c6
Step 4/8 : ARG branch=develop
 ---> Running in a32793ba8497
 ---> 67826472ec04
Removing intermediate container a32793ba8497
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d0adfccb7fa1
[91mCloning into 'tutorials'...
[0m ---> 1c438e4e0899
Removing intermediate container d0adfccb7fa1
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in c6501ba642c0
 ---> 1f24cbc92b59
Removing intermediate container c6501ba642c0
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 684d33fc8814
 ---> d9c806139a00
Removing intermediate container 684d33fc8814
Step 8/8 : USER [secure]
 ---> Running in b8b718267646
 ---> 532c8dc28c4e
Removing intermediate container b8b718267646

Successfully built 532c8dc28c4e
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:6e1997efd1437e4b30847706ba82be0762994bc1106d7ada6411e9cdb27b893e
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: .gitkeep
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatDirichlet-iterations.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-convergence.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-iterations.log
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['[secure]-HeatNeumann-convergence.log', '[secure]-HeatNeumann-iterations.log', '[secure]-HeatDirichlet-iterations.log']
Files only in output(right)   : []
travis_time:end:08e65e3c:start=1577186633671596981,finish=1577186749742185254,duration=116070588273,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:3983d308[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/629054382/log.txt)