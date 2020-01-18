## Status: Failure 
Build: [1470](https://travis-ci.org/precice/systemtests/builds/638788530) 

Job: [1470.21](https://travis-ci.org/precice/systemtests/jobs/638788554) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/8 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 439e63c3f638
 ---> 50870146b563
Removing intermediate container 439e63c3f638
Step 3/8 : RUN apk add git
 ---> Running in ba1389b345b0
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
 ---> 1aa13673c6aa
Removing intermediate container ba1389b345b0
Step 4/8 : ARG branch=develop
 ---> Running in 596f10b72584
 ---> ce8ca681f6bc
Removing intermediate container 596f10b72584
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in b2086ec7a052
[91mCloning into 'tutorials'...
[0m ---> a11f3a075cd4
Removing intermediate container b2086ec7a052
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in b5ddff1a70cb
 ---> ed32115d10bf
Removing intermediate container b5ddff1a70cb
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 26227fd00eb8
 ---> fb1fb7cfda5d
Removing intermediate container 26227fd00eb8
Step 8/8 : USER [secure]
 ---> Running in 00c99bddc55f
 ---> 2a21a4cdd7cb
Removing intermediate container 00c99bddc55f

Successfully built 2a21a4cdd7cb
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:d5c57d7f12c2a0ae0f855c2adb78e7e8894c53de99cf056cf790307036e2d00c
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Timeout!
Printing logs for services:
Attaching to fenics-adapter-dirichlet
[36mfenics-adapter-dirichlet    |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m This is preCICE version 1.6.1
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m Revision info: v1.6.1-213-g9f778290
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m Configuring preCICE with configuration: "/home/[secure]/Data/Input/[secure]-config.xml"
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping fenics-adapter-dirichlet ... 
[1A[2KStopping fenics-adapter-dirichlet ... [32mdone[0m[1BAttaching to fenics-adapter-neumann
[36mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m This is preCICE version 1.6.1
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Revision info: v1.6.1-213-g9f778290
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Configuring preCICE with configuration: "/home/[secure]/Data/Input/[secure]-config.xml"
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping fenics-adapter-neumann ... 
[1A[2KStopping fenics-adapter-neumann ... [32mdone[0m[1BEXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:0431be6d:start=1579347385479346570,finish=1579348064526297353,duration=679046950783,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:06f26c40[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/638788554/log.txt)