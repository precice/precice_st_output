## Status: Passing 
Build: [1580](https://travis-ci.org/precice/systemtests/builds/645031917) 

Job: [1580.23](https://travis-ci.org/precice/systemtests/jobs/645031940) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

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
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074602 sha256=92fe37017be252c9261da64a09cae6d936e0034da920fb9192727011845780ed
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> b2ffdf5d0178
Removing intermediate container a6865c0c2daf
Step 6/12 : USER [secure]
 ---> Running in c22562d33e8a
 ---> bf1db286ee09
Removing intermediate container c22562d33e8a
Step 7/12 : ARG branch=develop
 ---> Running in 797f26ce7333
 ---> 2930bcf0c57f
Removing intermediate container 797f26ce7333
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in c91635b3bf44
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
  Created wheel for py[secure]: filename=py[secure]-0.1.0-cp36-cp36m-linux_x86_64.whl size=703105 sha256=400330542a52f0b18b4cb281f6666a6fb61331f0ba785797d9f5d42849d7ae8a
  Stored in directory: /tmp/pip-ephem-wheel-cache-o5egh6_0/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built py[secure]
Installing collected packages: py[secure]
Successfully installed py[secure]-0.1.0
 ---> d19b7acea4be
Removing intermediate container c91635b3bf44
Step 9/12 : WORKDIR /home/[secure]/
 ---> 7c9b89ddef1a
Removing intermediate container 74fb424b8e12
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 2a342caca87d
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
 ---> 8514181789fe
Removing intermediate container 2a342caca87d
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 955f27ac4af8
 ---> 3a1acb4aa853
Removing intermediate container 955f27ac4af8
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 86f81bf02518
Removing intermediate container 8ce0cd82a976
Successfully built 86f81bf02518
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating nutils-adapter
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:03922a82:start=1580643918452986047,finish=1580644190947823930,duration=272494837883,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1edbd220[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645031940/log.txt)