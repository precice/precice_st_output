## Status: Passing 
Build: [1610](https://travis-ci.org/precice/systemtests/builds/646351873) 

Job: [1610.23](https://travis-ci.org/precice/systemtests/jobs/646351897) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
Collecting Cython
  Downloading Cython-0.29.14-cp36-cp36m-manylinux1_x86_64.whl (2.1 MB)
Collecting mpi4py
  Downloading mpi4py-3.0.3.tar.gz (1.4 MB)
Collecting numpy
  Downloading numpy-1.18.1-cp36-cp36m-manylinux1_x86_64.whl (20.1 MB)
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074595 sha256=583b79f8431b324fc17484803221d3b6d93d5d992ad1c3cba72a69f3916a3aec
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> fc6e944b5c1c
Removing intermediate container 5b1d42467734
Step 6/12 : USER [secure]
 ---> Running in 8a6cede720f0
 ---> a397fd1d4729
Removing intermediate container 8a6cede720f0
Step 7/12 : ARG branch=develop
 ---> Running in 1c6ec7cfcffa
 ---> e12e913d6a6e
Removing intermediate container 1c6ec7cfcffa
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in debd2daef9cc
Collecting https://github.com/[secure]/python-bindings/archive/develop.zip
  Downloading https://github.com/[secure]/python-bindings/archive/develop.zip
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: cython in /usr/local/lib/python3.6/dist-packages (from py[secure]==0.1.0) (0.29.14)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.6/dist-packages (from py[secure]==0.1.0) (3.0.3)
Building wheels for collected packages: py[secure]
  Building wheel for py[secure] (PEP 517): started
  Building wheel for py[secure] (PEP 517): finished with status 'done'
  Created wheel for py[secure]: filename=py[secure]-0.1.0-cp36-cp36m-linux_x86_64.whl size=703124 sha256=d2f2122f4c5be5e77bd98d28589d6bea1fe2b2d3dc9cab08e234d848a4870b0d
  Stored in directory: /tmp/pip-ephem-wheel-cache-xz6vgzd_/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built py[secure]
Installing collected packages: py[secure]
Successfully installed py[secure]-0.1.0
 ---> 00d89b455942
Removing intermediate container debd2daef9cc
Step 9/12 : WORKDIR /home/[secure]/
 ---> 14a9cf21e70c
Removing intermediate container e15de6f6cc7a
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in f175bc273f8a
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
 ---> 0c4663f7dc01
Removing intermediate container f175bc273f8a
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 381e20f74b64
 ---> f31dbc55b70e
Removing intermediate container 381e20f74b64
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 2914f80b7b86
Removing intermediate container 420c4a207123
Successfully built 2914f80b7b86
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating nutils-adapter ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating nutils-adapter
[1A[2KCreating nutils-adapter ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:303360ea:start=1580905801548303128,finish=1580906073200048864,duration=271651745736,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:260eb888[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:260eb888:start=1580906077301849205,finish=1580906078711391662,duration=1409542457,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1b22ac25[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/646351897/log.txt)