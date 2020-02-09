## Status: Passing 
Build: [1623](https://travis-ci.org/precice/systemtests/builds/647989489) 

Job: [1623.23](https://travis-ci.org/precice/systemtests/jobs/647989512) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
Successfully installed pip-20.0.2 setuptools-45.2.0 wheel-0.34.2
Collecting Cython
  Downloading Cython-0.29.14-cp36-cp36m-manylinux1_x86_64.whl (2.1 MB)
Collecting mpi4py
  Downloading mpi4py-3.0.3.tar.gz (1.4 MB)
Collecting numpy
  Downloading numpy-1.18.1-cp36-cp36m-manylinux1_x86_64.whl (20.1 MB)
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074585 sha256=4f352de5453bd00f70f2e4cb876aa0cd5371cba2d564d4b7ee047ee254061913
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> 56c2ef4af30a
Removing intermediate container b922671c4d51
Step 6/12 : USER [secure]
 ---> Running in bda142f4f226
 ---> 54697c5a5452
Removing intermediate container bda142f4f226
Step 7/12 : ARG branch=develop
 ---> Running in 0b3a0e2ad4f0
 ---> ac92243a5fa9
Removing intermediate container 0b3a0e2ad4f0
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in c328cafeb9b0
Collecting https://github.com/[secure]/python-bindings/archive/develop.zip
  Downloading https://github.com/[secure]/python-bindings/archive/develop.zip
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: mpi4py in /usr/local/lib/python3.6/dist-packages (from py[secure]==2.0.0a1) (3.0.3)
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from py[secure]==2.0.0a1) (1.18.1)
Building wheels for collected packages: py[secure]
  Building wheel for py[secure] (PEP 517): started
  Building wheel for py[secure] (PEP 517): finished with status 'done'
  Created wheel for py[secure]: filename=py[secure]-2.0.0a1-cp36-cp36m-linux_x86_64.whl size=713564 sha256=c41605a2c38caef9fec287bc1cca115d6521443d5db73c24f606e12de9889c30
  Stored in directory: /tmp/pip-ephem-wheel-cache-grhc9evm/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built py[secure]
Installing collected packages: py[secure]
Successfully installed py[secure]-2.0.0a1
 ---> 8801f032bee7
Removing intermediate container c328cafeb9b0
Step 9/12 : WORKDIR /home/[secure]/
 ---> fec713ffd597
Removing intermediate container fef913aa48bc
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 196a8fa5ee28
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
 ---> a2e19da181a2
Removing intermediate container 196a8fa5ee28
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 6e9cc2083677
 ---> b07b185812e4
Removing intermediate container 6e9cc2083677
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> e093868ba102
Removing intermediate container 75625572eb85
Successfully built e093868ba102
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
travis_time:end:00743ca5:start=1581249069475248655,finish=1581249344228684667,duration=274753436012,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2bf961e6:start=1581249348541654126,finish=1581249350002872660,duration=1461218534,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:068cc700[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/647989512/log.txt)