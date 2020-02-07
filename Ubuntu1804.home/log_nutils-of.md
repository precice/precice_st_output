## Status: Passing 
Build: [1613](https://travis-ci.org/precice/systemtests/builds/647273995) 

Job: [1613.23](https://travis-ci.org/precice/systemtests/jobs/647274018) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
  Downloading setuptools-45.1.0-py3-none-any.whl (583 kB)
Collecting wheel
  Downloading wheel-0.34.2-py2.py3-none-any.whl (26 kB)
Installing collected packages: pip, setuptools, wheel
Successfully installed pip-20.0.2 setuptools-45.1.0 wheel-0.34.2
Collecting Cython
  Downloading Cython-0.29.14-cp36-cp36m-manylinux1_x86_64.whl (2.1 MB)
Collecting mpi4py
  Downloading mpi4py-3.0.3.tar.gz (1.4 MB)
Collecting numpy
  Downloading numpy-1.18.1-cp36-cp36m-manylinux1_x86_64.whl (20.1 MB)
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074586 sha256=48925c1d526b0dcbf84a3d833ba70a7f0f28fe8a7c7a00b4c12ae98066c2e15c
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> 1260b67e4b70
Removing intermediate container 7b816fae14a8
Step 6/12 : USER [secure]
 ---> Running in 11ceba7ed4e0
 ---> e84b3a6874c4
Removing intermediate container 11ceba7ed4e0
Step 7/12 : ARG branch=develop
 ---> Running in 775f53689ec5
 ---> 30757aa8fafe
Removing intermediate container 775f53689ec5
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in 140641d714df
Collecting https://github.com/[secure]/python-bindings/archive/develop.zip
  Downloading https://github.com/[secure]/python-bindings/archive/develop.zip
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: mpi4py in /usr/local/lib/python3.6/dist-packages (from py[secure]==0.1.0) (3.0.3)
Requirement already satisfied: cython in /usr/local/lib/python3.6/dist-packages (from py[secure]==0.1.0) (0.29.14)
Building wheels for collected packages: py[secure]
  Building wheel for py[secure] (PEP 517): started
  Building wheel for py[secure] (PEP 517): finished with status 'done'
  Created wheel for py[secure]: filename=py[secure]-0.1.0-cp36-cp36m-linux_x86_64.whl size=703112 sha256=f5d6f635b6cac8025b2fe0d7caa0d417d2e62f54afffa38b9fe687bed8a811c0
  Stored in directory: /tmp/pip-ephem-wheel-cache-e5mx0szg/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built py[secure]
Installing collected packages: py[secure]
Successfully installed py[secure]-0.1.0
 ---> 30bff8720f91
Removing intermediate container 140641d714df
Step 9/12 : WORKDIR /home/[secure]/
 ---> c9afedd38460
Removing intermediate container 409d7b2e83fa
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 37822fc67311
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
 ---> 6d10694936df
Removing intermediate container 37822fc67311
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 862e5444ad66
 ---> 89fafc3a5a47
Removing intermediate container 862e5444ad66
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 1ac7b61c0b80
Removing intermediate container 7cb2624cd0de
Successfully built 1ac7b61c0b80
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating nutils-adapter ... 
Creating openfoam-adapter-outer ... 
Creating openfoam-adapter-outer
Creating nutils-adapter
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:017e9d01:start=1581078192577910695,finish=1581078462094705438,duration=269516794743,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:03bb0e30[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/647274018/log.txt)