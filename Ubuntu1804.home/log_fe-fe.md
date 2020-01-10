## Status: Failure 
Build: [1423](https://travis-ci.org/precice/systemtests/builds/635300170) 

Job: [1423.4](https://travis-ci.org/precice/systemtests/jobs/635300174) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in d281e28022de
 ---> 58108a4a1342
Removing intermediate container d281e28022de
Step 3/8 : RUN apk add git
 ---> Running in f3f1d2654a1c
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
 ---> 0a30d70e50a1
Removing intermediate container f3f1d2654a1c
Step 4/8 : ARG branch=develop
 ---> Running in 15775eeaf64b
 ---> b875f3c245d4
Removing intermediate container 15775eeaf64b
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 4493075574a0
[91mCloning into 'tutorials'...
[0m ---> 415a4b1df124
Removing intermediate container 4493075574a0
Step 6/8 : RUN mkdir configs && sed -i 's|<m2n:sockets from="HeatDirichlet" to="HeatNeumann"/>|<m2n:sockets from="HeatDirichlet" to="HeatNeumann" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"/>|g' $tutorial_path/[secure]-config.xml
 ---> Running in f090251c28ad
 ---> 050715d8345f
Removing intermediate container f090251c28ad
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9e54b8eb3857
 ---> b0aa75037e0f
Removing intermediate container 9e54b8eb3857
Step 8/8 : USER [secure]
 ---> Running in 8a8cf9fccdfd
 ---> 13455dfa5856
Removing intermediate container 8a8cf9fccdfd

Successfully built 13455dfa5856
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:538ff1de547ce17a17e91385353432864beca1bf9133cb071870b3f78acd0621
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BAttaching to tutorial-data, fenics-adapter-neumann, fenics-adapter-dirichlet
[36mtutorial-data exited with code 0
[0m[33mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[33mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[32mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[33mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[33mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[33mfenics-adapter-neumann      |[0m ---[[secure]] [31mERROR: [0m Wrong attribute "distribution-type"
[33mfenics-adapter-neumann exited with code 255
[0m[32mfenics-adapter-dirichlet exited with code 255
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: .gitkeep
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatDirichlet-iterations.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-convergence.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-iterations.log
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['[secure]-HeatDirichlet-iterations.log', '[secure]-HeatNeumann-iterations.log', '[secure]-HeatNeumann-convergence.log']
Files only in output(right)   : []
travis_time:end:114f93b4:start=1578668168169785581,finish=1578668235067085159,duration=66897299578,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:074c92fe[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635300174/log.txt)