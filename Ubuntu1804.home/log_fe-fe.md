## Status: Failure 
Build: [1157](https://travis-ci.org/precice/systemtests/builds/617667611) 

Job: [1157.16](https://travis-ci.org/precice/systemtests/jobs/617667627) 

Triggered by: [push](https://github.com/precice/systemtests/compare/develop) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/8efd2703b5a5...62ae8185f089) 

---
Last 100 lines of the job log at the moment of push:
```
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
Step 1/7 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/7 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 6e943c8dfa1d
 ---> ea8a15338e49
Removing intermediate container 6e943c8dfa1d
Step 3/7 : RUN apk add git
 ---> Running in ad8c5e414979
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.66.0-r0)
(4/6) Installing expat (2.2.8-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> 877bf55b47cf
Removing intermediate container ad8c5e414979
Step 4/7 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 827f6465ef96
[91mCloning into 'tutorials'...
[0m ---> 060439f20574
Removing intermediate container 827f6465ef96
Step 5/7 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in 51c16b24535e
 ---> 7b24170bf4c6
Removing intermediate container 51c16b24535e
Step 6/7 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fcee1a813fe2
 ---> 494e3383eb88
Removing intermediate container fcee1a813fe2
Step 7/7 : USER [secure]
 ---> Running in 39140c9d0b2e
 ---> 934454c8a177
Removing intermediate container 39140c9d0b2e

Successfully built 934454c8a177
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:9b7538862adc38a9f3b30acf24f160b30042c81dcdedbb653dd4f19a8259c97e
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
fenics-adapter-neumann failed! Find the logs below
Attaching to fenics-adapter-neumann
[36mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m This is preCICE version 1.6.1
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Revision info: v1.6.1-124-ged8e871c
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Configuring preCICE with configuration: "/home/[secure]/Data/Input/[secure]-config.xml"
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Run in coupling mode
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Setting up master communication to coupling partner/s
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Masters are connected
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Gather mesh NeumannNodes
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Send global mesh NeumannNodes
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Compute partition for mesh NeumannNodes
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Setting up slaves communication to coupling partner/s
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m Slaves are connected
[36mfenics-adapter-neumann      |[0m ---[[secure]] [0m it 1 of 100 | dt# 1 | t 0 of 1 | dt 0.1 | max dt 0.1 | ongoing yes | dt complete no | write-initial-data | write-iteration-checkpoint | 
[36mfenics-adapter-neumann      |[0m Traceback (most recent call last):
[36mfenics-adapter-neumann      |[0m   File "/home/[secure]/Data/Input/heat.py", line 139, in <module>
[36mfenics-adapter-neumann      |[0m     F += [secure].create_coupling_neumann_boundary_condition(v, V_g)
[36mfenics-adapter-neumann      |[0m   File "/home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py", line 537, in create_coupling_neumann_boundary_condition
[36mfenics-adapter-neumann      |[0m     n = FacetNormal(self._mesh_fenics)
[36mfenics-adapter-neumann      |[0m NameError: name 'FacetNormal' is not defined
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:03f8b415:start=1574856374377784856,finish=1574856501266982055,duration=126889197199,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:192ffdeb[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/617667627/log.txt)