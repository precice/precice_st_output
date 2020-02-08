## Status: Passing 
Build: [1614](https://travis-ci.org/precice/systemtests/builds/647676484) 

Job: [1614.23](https://travis-ci.org/precice/systemtests/jobs/647676507) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
  Stored in directory: /root/.cache/pip/wheels/d6/73/83/ad9dd3ebae512829ab3f21657f76403dc4aa6649e1118c9369
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy
Successfully installed Cython-0.29.14 mpi4py-3.0.3 numpy-1.18.1
 ---> 5692c34150c1
Removing intermediate container 875d152eb19b
Step 6/12 : USER [secure]
 ---> Running in 18f882ad7b7e
 ---> e84217586de6
Removing intermediate container 18f882ad7b7e
Step 7/12 : ARG branch=develop
 ---> Running in 47f91597d402
 ---> cfc39df22c4f
Removing intermediate container 47f91597d402
Step 8/12 : RUN pip3 install --user https://github.com/[secure]/python-bindings/archive/$branch.zip
 ---> Running in b154fc9be4ff
Collecting https://github.com/[secure]/python-bindings/archive/develop.zip
  Downloading https://github.com/[secure]/python-bindings/archive/develop.zip
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from py[secure]==2.0.0a1) (1.18.1)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.6/dist-packages (from py[secure]==2.0.0a1) (3.0.3)
Building wheels for collected packages: py[secure]
  Building wheel for py[secure] (PEP 517): started
  Building wheel for py[secure] (PEP 517): finished with status 'done'
  Created wheel for py[secure]: filename=py[secure]-2.0.0a1-cp36-cp36m-linux_x86_64.whl size=713560 sha256=423e7c58ccab9908209110297de7371cca2e4afb515434295f5e4c3ebf30cc66
  Stored in directory: /tmp/pip-ephem-wheel-cache-91hdk75m/wheels/8d/4d/18/308222d4aaadc3616c73ac4d4563793feb863232b1b31836e3
Successfully built py[secure]
Installing collected packages: py[secure]
Successfully installed py[secure]-2.0.0a1
 ---> 2f50e834547b
Removing intermediate container b154fc9be4ff
Step 9/12 : WORKDIR /home/[secure]/
 ---> 70d11d57abde
Removing intermediate container 54c6c65e3a3b
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 02628ce2ffd2
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
 ---> 837956304833
Removing intermediate container 02628ce2ffd2
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 8f0f1dfbbb0a
 ---> fa8b0d0686f7
Removing intermediate container 8f0f1dfbbb0a
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> 5fea9366a60d
Removing intermediate container 109355cb68bb
Successfully built 5fea9366a60d
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
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:00764f82:start=1581163766707846083,finish=1581164037754436001,duration=271046589918,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0ba294e8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0ba294e8:start=1581164042168341658,finish=1581164043683575854,duration=1515234196,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:000dde3c[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/647676507/log.txt)