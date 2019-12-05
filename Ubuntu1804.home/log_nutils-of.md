## Status: Passing 
Build: [1264](https://travis-ci.org/precice/systemtests/builds/621025152) 

Job: [1264.20](https://travis-ci.org/precice/systemtests/jobs/621025172) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4b1d49be8e29...13952c2945a9) 

---
Last 100 lines of the job log at the moment of push:
```
Requirement already satisfied: cython in /usr/local/lib/python3.6/dist-packages (from [secure]==2.0.0) (0.29.14)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (PEP 517): started
  Building wheel for [secure] (PEP 517): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-2.0.0-cp36-cp36m-linux_x86_64.whl size=675885 sha256=163ad5e8d69ddffde5e3e05aa9c1f0e04110073a2c7ee5ba5977683347267a75
  Stored in directory: /tmp/pip-ephem-wheel-cache-eg4q3abs/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-2.0.0
 ---> ef5c5a7db683
Removing intermediate container 09d3fe6abe80
Step 9/12 : WORKDIR /home/[secure]/
 ---> 1d2b81e918ec
Removing intermediate container 225b913a029d
Step 10/12 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 9e5c771025e7
[91mCloning into 'nutils'...
[0mObtaining file:///home/[secure]/nutils
Requirement already satisfied: numpy>=1.12 in /usr/local/lib/python3.6/dist-packages (from nutils==6.0a0) (1.17.4)
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
 ---> 0c9eb79490e4
Removing intermediate container 9e5c771025e7
Step 11/12 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in d48431b71b09
 ---> 17506fb45e50
Removing intermediate container d48431b71b09
Step 12/12 : WORKDIR /home/[secure]/nutils
 ---> d198a5f0a1fa
Removing intermediate container 742a1ac518a6
Successfully built d198a5f0a1fa
Successfully tagged testcomposenutilsofubuntu1804_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating openfoam-adapter-outer
Creating nutils-adapter
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
awk: cmd. line:6: (FILENAME=- FNR=1) fatal: division by zero attempted
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of.Ubuntu1804/Output
travis_time:end:0ba72cb2:start=1575540603517639027,finish=1575540879997898573,duration=276480259546,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of --base Ubuntu1804.home" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0f0cb4cf[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0f0cb4cf:start=1575540884650372217,finish=1575540886289926854,duration=1639554637,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0ff24bc4[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/621025172/log.txt)