## Status: Passing 
Build: [1520](https://travis-ci.org/precice/systemtests/builds/641980444) 

Job: [1520.24](https://travis-ci.org/precice/systemtests/jobs/641980468) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
  Created wheel for mpi4py: filename=mpi4py-3.0.3-cp36-cp36m-linux_x86_64.whl size=2074587 sha256=7ecb2104bd62caf64ada4502805b25bee407a5a306a20c5d2396005564d27732
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> b9cdf2302f6f
Removing intermediate container 4d605992743f
Step 6/12 : USER [secure]
 ---> Running in a18cbaca8fc3
 ---> b3403be56c1f
Removing intermediate container a18cbaca8fc3
Step 7/12 : ARG branch=develop
 ---> Running in b479b523163c
 ---> 7eac0f0b4cbe
Removing intermediate container b479b523163c
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in 2b71be893c81
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
  Created wheel for [secure]: filename=[secure]-2.0.0-cp36-cp36m-linux_x86_64.whl size=676422 sha256=1de7f19cb29974f6f54805e7634c7f640dcf2b4c7497d380d232ea9420ba0512
  Stored in directory: /tmp/pip-ephem-wheel-cache-og7zct9t/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-2.0.0
 ---> b2e590ea26c9
Removing intermediate container 2b71be893c81
Step 9/12 : WORKDIR /home/[secure]/
 ---> 60dbdb69480e
Removing intermediate container 0df513101bf0
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in b747fc8e2bc0
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
 ---> 4eb364513ba0
Removing intermediate container b747fc8e2bc0
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 035dcbfd7787
 ---> b07bb9f61729
Removing intermediate container 035dcbfd7787
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 12581d24e59c
Removing intermediate container a07ebfa112f1
Successfully built 12581d24e59c
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
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:051b344f:start=1580040016956834262,finish=1580040290908916815,duration=273952082553,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:16233915[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:16233915:start=1580040295051086232,finish=1580040296473676696,duration=1422590464,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:265a6f88[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/641980468/log.txt)