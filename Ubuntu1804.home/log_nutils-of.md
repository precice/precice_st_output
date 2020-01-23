## Status: Passing 
Build: [1476](https://travis-ci.org/precice/systemtests/builds/640842744) 

Job: [1476.24](https://travis-ci.org/precice/systemtests/jobs/640842768) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 

---
Last 100 lines of the job log at the moment of push:
```
Successfully installed pip-20.0.1 setuptools-45.1.0 wheel-0.33.6
Collecting Cython
  Downloading Cython-0.29.14-cp36-cp36m-manylinux1_x86_64.whl (2.1 MB)
Collecting mpi4py
  Downloading mpi4py-3.0.3.tar.gz (1.4 MB)
Collecting numpy
  Downloading numpy-1.18.1-cp36-cp36m-manylinux1_x86_64.whl (20.1 MB)
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074583 sha256=3bf6886df63aa25a8be8ed8bf2d8e87c05eb47eda23d073a4a5ad07fe360cfbf
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> 8ef28dbd5f6b
Removing intermediate container e66d065c0153
Step 6/12 : USER [secure]
 ---> Running in b4f512e32edd
 ---> a053c25d51a7
Removing intermediate container b4f512e32edd
Step 7/12 : ARG branch=develop
 ---> Running in 9fbd624f58fd
 ---> fbb1d1405a8b
Removing intermediate container 9fbd624f58fd
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in 59790843b908
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
  Created wheel for [secure]: filename=[secure]-2.0.0-cp36-cp36m-linux_x86_64.whl size=676428 sha256=5db46b63ba0843d9174be6720b1d04467bc6c4bd47dc69f2b5a91a3b501a2ba1
  Stored in directory: /tmp/pip-ephem-wheel-cache-5i01s5t_/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-2.0.0
 ---> a0ae4a0bd70a
Removing intermediate container 59790843b908
Step 9/12 : WORKDIR /home/[secure]/
 ---> 838bff371ec1
Removing intermediate container d4700ce198e3
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 91fccbba3931
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
 ---> 6ff687ccc23f
Removing intermediate container 91fccbba3931
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 6a29f82b56f3
 ---> b087379b5e36
Removing intermediate container 6a29f82b56f3
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 91a4fa2c7fb7
Removing intermediate container a08cc0f01af6
Successfully built 91a4fa2c7fb7
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
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0fa1c4ce:start=1579779942783953037,finish=1579780213003095889,duration=270219142852,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:03709ae2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:03709ae2:start=1579780217150532826,finish=1579780218517163187,duration=1366630361,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:036ab816[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/640842768/log.txt)