 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583929538) 
## Triggered by: [cron](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4) 
## Last 100 lines of the job log at the moment of push...
```
   Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143972 sha256=d5e1517d32d76ae24026bebe7a8252644c3f037538171a10b63c48fca32ef99f
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.2
 ---> e50521da510c
Removing intermediate container ecdfbc7c287c
Step 6/14 : USER [secure]
 ---> Running in fb07decab2e8
 ---> 1abaca7768ed
Removing intermediate container fb07decab2e8
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 41f7d2d5c382
Removing intermediate container 46509b3bfe67
Step 8/14 : RUN pip3 install --user .
 ---> Running in 01d4a10f17ee
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
  Created wheel for [secure]-future: filename=[secure]_future-1.5.2-cp35-cp35m-linux_x86_64.whl size=653539 sha256=fd9f8da819aecd79a3a9532820214bdc335eae1720962d8c0d4918b2a62b4999
  Stored in directory: /tmp/pip-ephem-wheel-cache-a0eazado/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.5.2
 ---> 79cf1b130189
Removing intermediate container 01d4a10f17ee
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> 4b0ee597ed7e
Removing intermediate container 0ca4cfd321fc
Step 10/14 : RUN pip3 install --user .
 ---> Running in 146d01c2d955
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.5.2) (1.5.2)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.5.2-cp35-none-any.whl size=2628 sha256=3317ac17ce56b02eb44d0ce8991510a27667d4b15b93ecd414822bbc83887b9a
  Stored in directory: /tmp/pip-ephem-wheel-cache-kklhw61z/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.5.2
 ---> 57e90c11a695
Removing intermediate container 146d01c2d955
Step 11/14 : WORKDIR /home/[secure]/
 ---> 1002f99b256d
Removing intermediate container 7ba53720c8de
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 7f67ff6e7d91
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
 ---> a54c1300d99c
Removing intermediate container 7f67ff6e7d91
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 3e4cad31aaec
 ---> 5957929b508b
Removing intermediate container 3e4cad31aaec
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> 6fb9adb99b3c
Removing intermediate container 1a42a6b374c4
Successfully built 6fb9adb99b3c
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
All adapters finished!
bash: ../compare_results.sh: No such file or directory
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/Output
travis_time:end:070e5ecc:start=1568254669214623158,finish=1568254972339016804,duration=303124393646,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:2624858d[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583929561/log.txt)