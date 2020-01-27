## Status: Passing 
Build: [1521](https://travis-ci.org/precice/systemtests/builds/642317432) 

Job: [1521.24](https://travis-ci.org/precice/systemtests/jobs/642317456) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074580 sha256=a2d012e5469e7e0f02f7cc9f55c0b15f17884876ab503fa03b45eda6b6e8dcdd
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> 594341620e06
Removing intermediate container a9b0e9f96160
Step 6/12 : USER [secure]
 ---> Running in 76c595d41f0f
 ---> 74905db886cb
Removing intermediate container 76c595d41f0f
Step 7/12 : ARG branch=develop
 ---> Running in c79f5ed9bbbc
 ---> 2bd2697994a7
Removing intermediate container c79f5ed9bbbc
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in e2e93d72071a
Collecting https://github.com/[secure]/python-bindings/archive/develop.zip
  Downloading https://github.com/[secure]/python-bindings/archive/develop.zip
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
  Created wheel for [secure]: filename=[secure]-2.0.0-cp36-cp36m-linux_x86_64.whl size=676451 sha256=63ec884bc00bf3a5dedbcccf7fe7625f356b869a8ca82e770fcbe1a038632763
  Stored in directory: /tmp/pip-ephem-wheel-cache-8suma0ns/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-2.0.0
 ---> fcd9934baccc
Removing intermediate container e2e93d72071a
Step 9/12 : WORKDIR /home/[secure]/
 ---> 2ba466cbf82e
Removing intermediate container 62369ba9fba5
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in d17a81aa4937
[91mCloning into 'nutils'...
[0mObtaining file:///home/[secure]/nutils
Requirement already satisfied: numpy>=1.12 in /usr/local/lib/python3.6/dist-packages (from nutils==6.0a0) (1.18.1)
Collecting treelog>=1.0b5
  Downloading treelog-1.0b7-py3-none-any.whl (24 kB)
Collecting stickybar
  Downloading stickybar-1.0-py3-none-any.whl (4.3 kB)
Collecting stringly
  Downloading stringly-1.0b1-py3-none-any.whl (9.7 kB)
Collecting typing-extensions
  Downloading typing_extensions-3.7.4.1-py3-none-any.whl (20 kB)
Installing collected packages: typing-extensions, treelog, stickybar, stringly, nutils
  Running setup.py develop for nutils
Successfully installed nutils stickybar-1.0 stringly-1.0b1 treelog-1.0b7 typing-extensions-3.7.4.1
 ---> 5dcdcb553e7f
Removing intermediate container d17a81aa4937
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 0c2656470451
 ---> 83ee84270337
Removing intermediate container 0c2656470451
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> c1a4756bcc5a
Removing intermediate container e787ef9861b0
Successfully built c1a4756bcc5a
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating nutils-adapter
Creating openfoam-adapter-outer
[1A[2KCreating nutils-adapter ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:191e2c22:start=1580125438967014488,finish=1580125707390027935,duration=268423013447,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04660903[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04660903:start=1580125711661433375,finish=1580125713126565775,duration=1465132400,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0dc95216[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/642317456/log.txt)