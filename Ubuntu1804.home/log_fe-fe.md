## Status: Failure 
Build: [1471](https://travis-ci.org/precice/systemtests/builds/639080221) 

Job: [1471.21](https://travis-ci.org/precice/systemtests/jobs/639080242) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in 405567b5fd49
 ---> 8dea0b9b04dc
Removing intermediate container 405567b5fd49
Step 3/8 : RUN apk add git
 ---> Running in 8609be7aef75
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
 ---> e2b7a775ac64
Removing intermediate container 8609be7aef75
Step 4/8 : ARG branch=develop
 ---> Running in 97bb132bbcae
 ---> d1b0655eeac7
Removing intermediate container 97bb132bbcae
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 75aca748c2b3
[91mCloning into 'tutorials'...
[0m ---> 38b67c34a80c
Removing intermediate container 75aca748c2b3
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in f33434c28421
 ---> 5537bab075c7
Removing intermediate container f33434c28421
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 262a256fb1e2
 ---> 315359cb2444
Removing intermediate container 262a256fb1e2
Step 8/8 : USER [secure]
 ---> Running in d278e8325db5
 ---> bfad651dd875
Removing intermediate container d278e8325db5

Successfully built bfad651dd875
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:5ab03bb45c652b6140f8225101f2e97829590691ba118a69912ebd22978e3aa6
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-neumann
Creating fenics-adapter-dirichlet
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BRunning the simulation...Be patient
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

```
[
Full job log](https://api.travis-ci.org/v3/job/639080242/log.txt)