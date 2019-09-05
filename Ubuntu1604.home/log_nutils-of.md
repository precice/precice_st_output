 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581134218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.1
 ---> e7f255569a0b
Removing intermediate container 7aafdc388e6b
Step 6/14 : USER [secure]
 ---> Running in e2e0bf6c3965
 ---> a221e521119b
Removing intermediate container e2e0bf6c3965
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 3171f59a34d5
Removing intermediate container 091d3c4f5bb0
Step 8/14 : RUN pip3 install --user .
 ---> Running in 79818a040193
Processing /home/[secure]/[secure]/src/[secure]/bindings/python_future
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.5.2) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.5.2) (3.0.2)
Building wheels for collected packages: [secure]-future
  Building wheel for [secure]-future (PEP 517): started
  Building wheel for [secure]-future (PEP 517): finished with status 'done'
  Created wheel for [secure]-future: filename=[secure]_future-1.5.2-cp35-cp35m-linux_x86_64.whl size=413527 sha256=24120ed345f512b4dd605c0d659eee2a2d0bd125cde10ab00889e754b1912dbd
  Stored in directory: /tmp/pip-ephem-wheel-cache-9l0sttm5/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.5.2
 ---> de6193cef74e
Removing intermediate container 79818a040193
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> 972212b024f4
Removing intermediate container 75fe7ed9a146
Step 10/14 : RUN pip3 install --user .
 ---> Running in dd1979add5d6
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.5.2) (1.5.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (3.0.2)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.5.2-cp35-none-any.whl size=2575 sha256=0c3a2617088850f71bf44b13ac2f02cb87b2caf13c386ab4a095c7f1ceb266e8
  Stored in directory: /tmp/pip-ephem-wheel-cache-_i9i2lbg/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.5.2
 ---> 360794104112
Removing intermediate container dd1979add5d6
Step 11/14 : WORKDIR /home/[secure]/
 ---> ad6dc1c8829e
Removing intermediate container 06f593bdc23a
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 94684091fb3e
[91mCloning into 'nutils'...
[0mObtaining file:///home/[secure]/nutils
Requirement already satisfied: numpy>=1.12 in /usr/local/lib/python3.5/dist-packages (from nutils==6.0a0) (1.17.1)
Collecting treelog>=1.0b5 (from nutils==6.0a0)
  Downloading https://files.pythonhosted.org/packages/92/7e/373175f7e8399e956eb191f066f89c0fa955be307463c9e73f3f0f382d3e/treelog-1.0b5-py3-none-any.whl
Collecting stickybar (from nutils==6.0a0)
  Downloading https://files.pythonhosted.org/packages/15/0f/5745e5f091d78b15afd580a76d712bea7076e1f0e9cedbe1932397cb3ea4/stickybar-1.0b2-py3-none-any.whl
Installing collected packages: treelog, stickybar, nutils
  Running setup.py develop for nutils
Successfully installed nutils stickybar-1.0b2 treelog-1.0b5
 ---> d122ba741e2e
Removing intermediate container 94684091fb3e
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in abbfdb247bb9
 ---> 8d92be222966
Removing intermediate container abbfdb247bb9
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> fcd496b99742
Removing intermediate container 7cc3c585333d
Successfully built fcd496b99742
Successfully tagged testcomposenutilsof_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating nutils-adapter
Creating openfoam-adapter-outer
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/TestCompose_nutils-of/Output
travis_time:end:01891c7c:start=1567679514571960519,finish=1567679826184345913,duration=311612385394,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1642a0ac[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581134236/log.txt)