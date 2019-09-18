 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586647457) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/cd89b1900540...aac1a14c474b) 
## Last 100 lines of the job log at the moment of push...
```
   Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.2
 ---> a68cde82e9a6
Removing intermediate container be0cfe44122f
Step 6/14 : USER [secure]
 ---> Running in d4e6bd069561
 ---> 6e89bafbfbea
Removing intermediate container d4e6bd069561
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> b100087a3c5e
Removing intermediate container 3d090d87afcc
Step 8/14 : RUN pip3 install --user .
 ---> Running in c03c081c8c87
Processing /home/[secure]/[secure]/src/[secure]/bindings/python_future
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.6.1) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.6.1) (0.29.13)
Building wheels for collected packages: [secure]-future
  Building wheel for [secure]-future (PEP 517): started
  Building wheel for [secure]-future (PEP 517): finished with status 'done'
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653541 sha256=f9a444c0f5e33c9770f3d8d6310ef0fb48872027408d192c67b145044359506f
  Stored in directory: /tmp/pip-ephem-wheel-cache-r_9vlb9u/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> 2af6efd973d8
Removing intermediate container c03c081c8c87
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> fc7433e023ee
Removing intermediate container c9496ff3f17c
Step 10/14 : RUN pip3 install --user .
 ---> Running in 66ab9355c907
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=015921f310fc5ba063de73b08384fd2a6ea7f18c7b0952f839266169b94ac39b
  Stored in directory: /tmp/pip-ephem-wheel-cache-y8a3pnn3/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> 2dcbfa2fa548
Removing intermediate container 66ab9355c907
Step 11/14 : WORKDIR /home/[secure]/
 ---> c8d6e9d0ab25
Removing intermediate container 9cbae9717454
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in a9b49e46f10b
[91mCloning into 'nutils'...
[0mObtaining file:///home/[secure]/nutils
Requirement already satisfied: numpy>=1.12 in /usr/local/lib/python3.5/dist-packages (from nutils==6.0a0) (1.17.2)
Collecting treelog>=1.0b5 (from nutils==6.0a0)
  Downloading https://files.pythonhosted.org/packages/92/7e/373175f7e8399e956eb191f066f89c0fa955be307463c9e73f3f0f382d3e/treelog-1.0b5-py3-none-any.whl
Collecting stickybar (from nutils==6.0a0)
  Downloading https://files.pythonhosted.org/packages/15/0f/5745e5f091d78b15afd580a76d712bea7076e1f0e9cedbe1932397cb3ea4/stickybar-1.0b2-py3-none-any.whl
Installing collected packages: treelog, stickybar, nutils
  Running setup.py develop for nutils
Successfully installed nutils stickybar-1.0b2 treelog-1.0b5
 ---> 3bbb152e4faf
Removing intermediate container a9b49e46f10b
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 3862de82e030
 ---> e30ba32003a9
Removing intermediate container 3862de82e030
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> f7a82d2e9721
Removing intermediate container 49adaa55578e
Successfully built f7a82d2e9721
Successfully tagged testcomposenutilsof_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating nutils-adapter ... 
Creating openfoam-adapter-outer ... 
Creating nutils-adapter
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
bash: ../compare_results.sh: No such file or directory
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/Output
travis_time:end:049b2faa:start=1568831138078194459,finish=1568831510432000765,duration=372353806306,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1e530002[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586647476/log.txt)