## Status: Passing 
Build: [1598](https://travis-ci.org/precice/systemtests/builds/645892844) 

Job: [1598.23](https://travis-ci.org/precice/systemtests/jobs/645892873) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/07c487419fcd18bdb04b9d9fef13c8b1318f3bef...6213c52a25101c0051df0fbc215ba9f941209daa) 

---
Last 100 lines of the job log at the moment of push:
```
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
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074604 sha256=006c65b7f15312f6bfd7c2c29993dd8728a237c2e0d790049915f45cd46899dc
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> f0906e0aaab3
Removing intermediate container e752d8466d5d
Step 6/12 : USER [secure]
 ---> Running in 3ece18086e1d
 ---> 10500787bb37
Removing intermediate container 3ece18086e1d
Step 7/12 : ARG branch=develop
 ---> Running in 91a8b897cad8
 ---> 1bc64b12088f
Removing intermediate container 91a8b897cad8
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in a95c78edad20
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
  Created wheel for py[secure]: filename=py[secure]-0.1.0-cp36-cp36m-linux_x86_64.whl size=703149 sha256=6d2146b58acba6db2f52199afaa9e4f15ff76b597f3dc29664878f267e3e2d8a
  Stored in directory: /tmp/pip-ephem-wheel-cache-m6zavio1/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built py[secure]
Installing collected packages: py[secure]
Successfully installed py[secure]-0.1.0
 ---> a3ae9b844af0
Removing intermediate container a95c78edad20
Step 9/12 : WORKDIR /home/[secure]/
 ---> 81811144e5e1
Removing intermediate container ac761bae57a7
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 86eddfb28f93
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
 ---> 951cff5a5336
Removing intermediate container 86eddfb28f93
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in d37208f7072d
 ---> 36f8a82768a1
Removing intermediate container d37208f7072d
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> af60c8857803
Removing intermediate container 99d353d26dd8
Successfully built af60c8857803
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
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:000568e6:start=1580818087436047018,finish=1580818362057645371,duration=274621598353,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04641e4c:start=1580818366536232401,finish=1580818368046945950,duration=1510713549,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1eb490f0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645892873/log.txt)