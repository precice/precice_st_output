 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593438448) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/46a3f0d5dc83...a992016cf5d2) 
## Last 100 lines of the job log at the moment of push...
```
   Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143965 sha256=f441100206427f005cbed6aec24c323ca10ff0bf0620c428b96d5ca9c0caf6ec
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.2
 ---> 4e7a109a431c
Removing intermediate container 81b2083c5060
Step 6/14 : USER [secure]
 ---> Running in 9a0a69d06539
 ---> 14f43add9b9a
Removing intermediate container 9a0a69d06539
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 0049e8c37ad7
Removing intermediate container 7e24f39aaee7
Step 8/14 : RUN pip3 install --user .
 ---> Running in 56ee6ecc300a
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
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653589 sha256=4cbb1b221274bb23f34d78608a25b6c1835a0991dba1651ce736ad16dd7e7932
  Stored in directory: /tmp/pip-ephem-wheel-cache-mv2fnvk5/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> c01e507b90ba
Removing intermediate container 56ee6ecc300a
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> bb8f09cd0557
Removing intermediate container 247c4c16ce0d
Step 10/14 : RUN pip3 install --user .
 ---> Running in c88ba243c30d
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=aa4455fb4f84e4c5e86a7bc23830dfb9a442676bbdf2e0e68b50c4828d5f0bbe
  Stored in directory: /tmp/pip-ephem-wheel-cache-ucwpmy42/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> ce501502eaa7
Removing intermediate container c88ba243c30d
Step 11/14 : WORKDIR /home/[secure]/
 ---> 98ac7874d5e7
Removing intermediate container 7b26aba809eb
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in c33151520cda
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
 ---> 2c47f44e65c5
Removing intermediate container c33151520cda
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 9f6c6079f7b1
 ---> 8a228a44e92d
Removing intermediate container 9f6c6079f7b1
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> aa8ca2a0b2c3
Removing intermediate container d86988a3e728
Successfully built aa8ca2a0b2c3
Successfully tagged testcomposenutilsof_nutils-adapter:latest
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/Output
travis_time:end:057ef7b8:start=1570181700548294141,finish=1570181992982012033,duration=292433717892,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1f46629e[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593438475/log.txt)