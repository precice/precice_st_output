## Status: Passing 
Build: [1261](https://travis-ci.org/precice/systemtests/builds/620720012) 

Job: [1261.20](https://travis-ci.org/precice/systemtests/jobs/620720032) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f0c87c5da690...4b1d49be8e29) 

---
Last 100 lines of the job log at the moment of push:
```
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: cython in /usr/local/lib/python3.6/dist-packages (from [secure]==2.0.0) (0.29.14)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.6/dist-packages (from [secure]==2.0.0) (3.0.3)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (PEP 517): started
  Building wheel for [secure] (PEP 517): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-2.0.0-cp36-cp36m-linux_x86_64.whl size=675872 sha256=9c05bd2986489dc6e851766ec277791409ef4c39b6162f78d25478a050ced61a
  Stored in directory: /tmp/pip-ephem-wheel-cache-f66bcyk2/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-2.0.0
 ---> 37209b37a54e
Removing intermediate container c3c567cbc283
Step 11/13 : WORKDIR /home/[secure]/
 ---> 7fa77bb36cab
Removing intermediate container 362c1f286cd2
Step 12/13 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 199fd65808aa
 ---> 96c47821c428
Removing intermediate container 199fd65808aa
Step 13/13 : WORKDIR /home/[secure]/nutils
 ---> 3e4af77885f3
Removing intermediate container 26c93e593645
Successfully built 3e4af77885f3
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating nutils-adapter ... 
Creating openfoam-adapter-outer ... 
Creating nutils-adapter
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
travis_time:end:190c7abf:start=1575482084408705438,finish=1575482346537986358,duration=262129280920,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:13b87c75[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:13b87c75:start=1575482350103776653,finish=1575482351526650960,duration=1422874307,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0ecb61a8[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/620720032/log.txt)