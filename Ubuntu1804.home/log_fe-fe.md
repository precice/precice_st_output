## Status: Failure 
Build: [1458](https://travis-ci.org/precice/systemtests/builds/637381788) 

Job: [1458.17](https://travis-ci.org/precice/systemtests/jobs/637381805) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/128) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/8 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in abe9b1b0a469
 ---> 2bfc3b62c2eb
Removing intermediate container abe9b1b0a469
Step 3/8 : RUN apk add git
 ---> Running in 7da84235daac
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
 ---> 3fc4c170bb18
Removing intermediate container 7da84235daac
Step 4/8 : ARG branch=develop
 ---> Running in 0f841340438b
 ---> 79d6046381b3
Removing intermediate container 0f841340438b
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 6c0b8f5ee95d
[91mCloning into 'tutorials'...
[0m ---> ef166b8c2668
Removing intermediate container 6c0b8f5ee95d
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in a682ec829924
 ---> f3566752442b
Removing intermediate container a682ec829924
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1bd973c8110e
 ---> 9460fd24a045
Removing intermediate container 1bd973c8110e
Step 8/8 : USER [secure]
 ---> Running in 4965febe5c83
 ---> bc9f7695e8aa
Removing intermediate container 4965febe5c83

Successfully built bc9f7695e8aa
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:5322e3e3a9825d6d9bf8c1d70248a19b2e306f0904f10f48b10d3c906f6e4fa5
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-neumann
Creating fenics-adapter-dirichlet
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
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m Revision info: v1.6.1-208-g625be7cb
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m Configuring preCICE with configuration: "/home/[secure]/Data/Input/[secure]-config.xml"
[36mfenics-adapter-dirichlet    |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping fenics-adapter-dirichlet ... 
[1A[2KStopping fenics-adapter-dirichlet ... [32mdone[0m[1BAttaching to fenics-adapter-neumann
[36mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m This is preCICE version 1.6.1
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Revision info: v1.6.1-208-g625be7cb
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Configuring preCICE with configuration: "/home/[secure]/Data/Input/[secure]-config.xml"
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
Stopping fenics-adapter-neumann ... 
[1A[2KStopping fenics-adapter-neumann ... [32mdone[0m[1BEXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:0055047e:start=1579091525310275097,finish=1579092202965485120,duration=677655210023,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:06d71abc[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637381805/log.txt)