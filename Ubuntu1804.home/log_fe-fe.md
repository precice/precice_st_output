 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599531436) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3f2f194851e3...aeaaaab693ed) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/3211dcc17558...521ff68ed5cc)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/a7cddc93a407...ce8a62f20104) 
## Last 100 lines of the job log at the moment of push...
```
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/7 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 038b2f6ce88e
 ---> 100dfd68d2f6
Removing intermediate container 038b2f6ce88e
Step 3/7 : RUN apk add git
 ---> Running in e1478a055b2c
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
 ---> 7f572d085264
Removing intermediate container e1478a055b2c
Step 4/7 : RUN git clone https://github.com/IshaanDesai/tutorials.git -b complexDomain_HT_fenics-fenics
 ---> Running in 06a53bc0f100
[91mCloning into 'tutorials'...
[0m ---> a2f98f80131a
Removing intermediate container 06a53bc0f100
Step 5/7 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in 4da8b19be9d5
 ---> 56774b979cee
Removing intermediate container 4da8b19be9d5
Step 6/7 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9d9966dd1a2a
 ---> dd5790a773ce
Removing intermediate container 9d9966dd1a2a
Step 7/7 : USER [secure]
 ---> Running in 76eb6b254ff3
 ---> 7fffa9bd4994
Removing intermediate container 76eb6b254ff3

Successfully built 7fffa9bd4994
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:53aa9dcdb3c9e41676701779f74003101d4674eb29b58823b79832943f2ade82
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-neumann
Creating fenics-adapter-dirichlet
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
fenics-adapter-neumann failed! Find the logs below
Attaching to fenics-adapter-neumann
[36mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:107 in configure: [0mThis is preCICE version 1.6.1
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:108 in configure: [0mRevision info: v1.6.1-101-gd48b59c1
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:109 in configure: [0mConfiguring preCICE with configuration: "/home/[secure]/Data/Input/[secure]-config.xml"
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:152 in configure: [0mRun in coupling mode
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:221 in initialize: [0mSetting up master communication to coupling partner/s
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:229 in initialize: [0mMasters are connected
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [partition::ProvidedPartition]:36 in communicate: [0mGather mesh NeumannNodes
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [partition::ProvidedPartition]:62 in communicate: [0mSend global mesh NeumannNodes
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [partition::ProvidedPartition]:79 in compute: [0mCompute partition for mesh NeumannNodes
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:233 in initialize: [0mSetting up slaves communication to coupling partner/s
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:241 in initialize: [0mSlaves are connected
[36mfenics-adapter-neumann      |[0m (0) 09:57:19 [impl::SolverInterfaceImpl]:269 in initialize: [0mit 1 of 100 | dt# 1 | t 0 of 1 | dt 0.1 | max dt 0.1 | ongoing yes | dt complete no | write-initial-data | write-iteration-checkpoint | 
[36mfenics-adapter-neumann      |[0m /home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py:16: Warning: This version of the [secure] bindings is deprecated and will be removed in preCICE version 2.0.0. You may import the updated python module using "import [secure]_future as [secure]" instead. Refer to the changelog for more information.
[36mfenics-adapter-neumann      |[0m   import [secure]
[36mfenics-adapter-neumann      |[0m Traceback (most recent call last):
[36mfenics-adapter-neumann      |[0m   File "/home/[secure]/Data/Input/heat.py", line 139, in <module>
[36mfenics-adapter-neumann      |[0m     F += [secure].create_coupling_neumann_boundary_condition(v, V_g)
[36mfenics-adapter-neumann      |[0m   File "/home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py", line 528, in create_coupling_neumann_boundary_condition
[36mfenics-adapter-neumann      |[0m     raise Exception("Boundary markers are not implemented yet")
[36mfenics-adapter-neumann      |[0m Exception: Boundary markers are not implemented yet
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:24597a50:start=1571392563109125601,finish=1571392691831510983,duration=128722385382,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:2607a0c4[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599531452/log.txt)