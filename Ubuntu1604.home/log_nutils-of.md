 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583691853) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3530c57a8cfa) 
## Last 100 lines of the job log at the moment of push...
```
   Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143978 sha256=9f4e52aa0ee8896afec1ca208fa34787de04f7b142c11a6dd2217652edd61e18
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.2
 ---> ae36f77b1196
Removing intermediate container 60705c89e97e
Step 6/14 : USER [secure]
 ---> Running in ff47dabe84e0
 ---> f58b22c24697
Removing intermediate container ff47dabe84e0
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 65d38040da00
Removing intermediate container a732d232c567
Step 8/14 : RUN pip3 install --user .
 ---> Running in 07efad4a6ade
Processing /home/[secure]/[secure]/src/[secure]/bindings/python_future
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.5.2) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.5.2) (0.29.13)
Building wheels for collected packages: [secure]-future
  Building wheel for [secure]-future (PEP 517): started
  Building wheel for [secure]-future (PEP 517): finished with status 'done'
  Created wheel for [secure]-future: filename=[secure]_future-1.5.2-cp35-cp35m-linux_x86_64.whl size=653556 sha256=e35987dceeb9201bd0fdb11a9764f1651a2d5a202d4ebf9fd4a44dae08699578
  Stored in directory: /tmp/pip-ephem-wheel-cache-irm3tcvg/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.5.2
 ---> fab6edc2e387
Removing intermediate container 07efad4a6ade
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> bdbf71d9e5e3
Removing intermediate container e0e8e6ae90a1
Step 10/14 : RUN pip3 install --user .
 ---> Running in 3d30fcb11be5
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.5.2) (1.5.2)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.5.2-cp35-none-any.whl size=2628 sha256=f5801e6b5801480032e56b826c5a71aa7105590a625d1e921091c8a1f40fb843
  Stored in directory: /tmp/pip-ephem-wheel-cache-kf_htyt4/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.5.2
 ---> 944dca6cbd70
Removing intermediate container 3d30fcb11be5
Step 11/14 : WORKDIR /home/[secure]/
 ---> 3a72e37846fb
Removing intermediate container 18ebb069e847
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 5f1bfd517430
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
 ---> 9ca9dd83e00c
Removing intermediate container 5f1bfd517430
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in b1b7e8066a7b
 ---> 62ac5d75dea8
Removing intermediate container b1b7e8066a7b
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> 4e00b4545beb
Removing intermediate container 750c62204799
Successfully built 4e00b4545beb
Successfully tagged testcomposenutilsof_nutils-adapter:latest
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
bash: ../compare_results.sh: No such file or directory
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/Output
travis_time:end:13f5efc9:start=1568219068519614111,finish=1568219366138042179,duration=297618428068,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:05740644[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583691872/log.txt)