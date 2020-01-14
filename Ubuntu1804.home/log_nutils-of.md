## Status: Passing 
Build: [1454](https://travis-ci.org/precice/systemtests/builds/636821308) 

Job: [1454.24](https://travis-ci.org/precice/systemtests/jobs/636821332) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074604 sha256=dcf259aa4514b8970beaaee08e76601f02512da611b471a7e3edf5737e04e661
  Stored in directory: /root/.cache/pip/wheels/18/e0/86/2b713dd512199096012ceca61429e12b960888de59818871d6
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> 99f5e23f293e
Removing intermediate container d78150a46b12
Step 6/12 : USER [secure]
 ---> Running in 12f6e0e83727
 ---> 65766e416620
Removing intermediate container 12f6e0e83727
Step 7/12 : ARG branch=develop
 ---> Running in 2e6197458ffb
 ---> 4512f8f60bc0
Removing intermediate container 2e6197458ffb
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in fd90aad8249c
Collecting https://github.com/[secure]/python-bindings/archive/develop.zip
  Downloading https://github.com/[secure]/python-bindings/archive/develop.zip
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: mpi4py in /usr/local/lib/python3.6/dist-packages (from [secure]==2.0.0) (3.0.3)
Requirement already satisfied: cython in /usr/local/lib/python3.6/dist-packages (from [secure]==2.0.0) (0.29.14)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (PEP 517): started
  Building wheel for [secure] (PEP 517): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-2.0.0-cp36-cp36m-linux_x86_64.whl size=678381 sha256=6c744a6a956e66cdef0ab0666962646c38eb998a49ede0ba1a2b4d0a73ed6b17
  Stored in directory: /tmp/pip-ephem-wheel-cache-pn6a0czv/wheels/45/d3/8f/2f8233d1d2214382b9535b84f8c3189221e554cacb2af9e937
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-2.0.0
 ---> 17e8ab71aa58
Removing intermediate container fd90aad8249c
Step 9/12 : WORKDIR /home/[secure]/
 ---> 291b41015356
Removing intermediate container c5c37e22cc35
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in f8ada56dd447
[91mCloning into 'nutils'...
[0mObtaining file:///home/[secure]/nutils
Requirement already satisfied: numpy>=1.12 in /usr/local/lib/python3.6/dist-packages (from nutils==6.0a0) (1.18.1)
Collecting treelog>=1.0b5
  Downloading https://files.pythonhosted.org/packages/a4/4a/adf25d9ddd8a39847a93ff162f7766a61ac7b9e6b6ce82eecc8bc1df0c39/treelog-1.0b7-py3-none-any.whl
Collecting stickybar
  Downloading https://files.pythonhosted.org/packages/2a/e5/592d1dd8212cd70e3a74752c7cd6d4c3a4d5b725ad39b2e3ed609a6e38d3/stickybar-1.0-py3-none-any.whl
Collecting stringly
  Downloading https://files.pythonhosted.org/packages/8e/3c/0a50a63f6949f980c148ffcfc2511556ed5910df1a07aaa16a7b75851985/stringly-1.0b1-py3-none-any.whl
Collecting typing-extensions
  Downloading https://files.pythonhosted.org/packages/03/92/705fe8aca27678e01bbdd7738173b8e7df0088a2202c80352f664630d638/typing_extensions-3.7.4.1-py3-none-any.whl
Installing collected packages: typing-extensions, treelog, stickybar, stringly, nutils
  Running setup.py develop for nutils
Successfully installed nutils stickybar-1.0 stringly-1.0b1 treelog-1.0b7 typing-extensions-3.7.4.1
 ---> 81c03d6a242e
Removing intermediate container f8ada56dd447
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in a24d0c7b05f1
 ---> a834df45c7bd
Removing intermediate container a24d0c7b05f1
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 3d1e96973d6c
Removing intermediate container 89b757f20efc
Successfully built 3d1e96973d6c
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating openfoam-adapter-outer
Creating nutils-adapter
[1A[2KCreating nutils-adapter ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:010a73c0:start=1579001751848013453,finish=1579002019331584541,duration=267483571088,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0211f005[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0211f005:start=1579002023441066169,finish=1579002024833131188,duration=1392065019,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:04a4bfe2[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/636821332/log.txt)