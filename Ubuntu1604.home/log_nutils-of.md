 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/590477881) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aac1a14c474b...0cb7c0ec452f) 
## Last 100 lines of the job log at the moment of push...
```
   Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143977 sha256=692901cfda2a05697ef446d2e34985be32fe9468a3ce9e179182d78d22b36cde
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.2
 ---> 90f620ccf722
Removing intermediate container 6036c2330fe8
Step 6/14 : USER [secure]
 ---> Running in 8d2d43fd84f1
 ---> 22fc0da3daf5
Removing intermediate container 8d2d43fd84f1
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 077a490f5740
Removing intermediate container 4ab0c371c223
Step 8/14 : RUN pip3 install --user .
 ---> Running in fb3db910e874
Processing /home/[secure]/[secure]/src/[secure]/bindings/python_future
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.6.1) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]-future==1.6.1) (3.0.2)
Building wheels for collected packages: [secure]-future
  Building wheel for [secure]-future (PEP 517): started
  Building wheel for [secure]-future (PEP 517): finished with status 'done'
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653587 sha256=b54999926ae9b51875f91dc0383c54320342dc3ee32fcdaeaf2d51d62d416e7f
  Stored in directory: /tmp/pip-ephem-wheel-cache-369pcsab/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> 9101326f6da7
Removing intermediate container fb3db910e874
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> e50dfc537fda
Removing intermediate container e58a7200967e
Step 10/14 : RUN pip3 install --user .
 ---> Running in 90f730c894f5
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=8a10b8cfe246e1a807919619ac80a6aa883f808090ef48d75b79a0a101d2df10
  Stored in directory: /tmp/pip-ephem-wheel-cache-97oaspmg/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> e5b3c1104436
Removing intermediate container 90f730c894f5
Step 11/14 : WORKDIR /home/[secure]/
 ---> c672bedd864c
Removing intermediate container b05c44be2ec7
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in cc77c5d0e685
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
 ---> 550dea20193e
Removing intermediate container cc77c5d0e685
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 835fe428adfb
 ---> f98e650800ca
Removing intermediate container 835fe428adfb
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> b27315e4eebc
Removing intermediate container 2b8105b35e8f
Successfully built b27315e4eebc
Successfully tagged testcomposenutilsof_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating nutils-adapter
Creating openfoam-adapter-outer
[1A[2KCreating nutils-adapter ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
bash: ../compare_results.sh: No such file or directory
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_nutils-of/Output
travis_time:end:072e242b:start=1569602361762946783,finish=1569602699715708809,duration=337952762026,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:02c76e94[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/590477900/log.txt)