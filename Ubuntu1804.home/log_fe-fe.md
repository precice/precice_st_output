## Status: Failure 
Build: [1398](https://travis-ci.org/precice/systemtests/builds/633704741) 

Job: [1398.21](https://travis-ci.org/precice/systemtests/jobs/633704762) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 4653dc228e02
 ---> f1de5cfd1477
Removing intermediate container 4653dc228e02
Step 3/8 : RUN apk add git
 ---> Running in e6d97181a294
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 5714250c3577
Removing intermediate container e6d97181a294
Step 4/8 : ARG branch=develop
 ---> Running in 0a677d784046
 ---> 1b897f78bafa
Removing intermediate container 0a677d784046
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 8f37011e654f
[91mCloning into 'tutorials'...
[0m ---> 71f40e4c88e3
Removing intermediate container 8f37011e654f
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in fb545399b7e6
 ---> b9e2465feb90
Removing intermediate container fb545399b7e6
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 12688094a16b
 ---> 29c19d6cf52b
Removing intermediate container 12688094a16b
Step 8/8 : USER [secure]
 ---> Running in 503866d48516
 ---> 8e780c98ad09
Removing intermediate container 503866d48516

Successfully built 8e780c98ad09
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:29279725d1b06bc11821c67f792062fee767fb5941162b520668ad211cdfcf2e
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
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['[secure]-HeatDirichlet-iterations.log', '[secure]-HeatNeumann-convergence.log', '[secure]-HeatNeumann-iterations.log']
Files only in output(right)   : []
travis_time:end:0f03fe48:start=1578396968117004872,finish=1578397082378870307,duration=114261865435,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0e4d61de[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/633704762/log.txt)