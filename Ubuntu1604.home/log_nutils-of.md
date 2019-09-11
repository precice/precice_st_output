 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/583654671) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/318f6af1f707...32fdbbbc7d35) 
## Last 100 lines of the job log at the moment of push...
```
   Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143947 sha256=7b3289846c435a088cbc2c0efc753dd2d288e33e6a1dc1f79eae3bdd6ef8ce5d
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.2
 ---> d6b689dd4622
Removing intermediate container c1fee066b046
Step 6/14 : USER [secure]
 ---> Running in 1da0a18fb786
 ---> 169b17750071
Removing intermediate container 1da0a18fb786
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> c70090936ded
Removing intermediate container 982fa0ee0e38
Step 8/14 : RUN pip3 install --user .
 ---> Running in ad4a6423948c
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
  Created wheel for [secure]-future: filename=[secure]_future-1.5.2-cp35-cp35m-linux_x86_64.whl size=653562 sha256=666e807b0fd1f59b54f68af1bbc2ddc87d570e1486384e6b5b6c35e9eaef5088
  Stored in directory: /tmp/pip-ephem-wheel-cache-i95w32fs/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.5.2
 ---> 3b556b04122a
Removing intermediate container ad4a6423948c
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> 28b284d8df8c
Removing intermediate container 498d33be1ae2
Step 10/14 : RUN pip3 install --user .
 ---> Running in 0586198c3045
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.5.2) (1.5.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (3.0.2)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.5.2-cp35-none-any.whl size=2628 sha256=740666c97a18650962e4b8f14ae3f2e51c1d5e1e301e91d39af6d13e1016de73
  Stored in directory: /tmp/pip-ephem-wheel-cache-isznkwdp/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.5.2
 ---> 5ed4c64a55cc
Removing intermediate container 0586198c3045
Step 11/14 : WORKDIR /home/[secure]/
 ---> 6844c6f5ca50
Removing intermediate container 2b024ba916cd
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 109fb0624272
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
 ---> 897a74fdd27a
Removing intermediate container 109fb0624272
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 4bf58140ec15
 ---> b213b4df8ef9
Removing intermediate container 4bf58140ec15
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> b08dcf958356
Removing intermediate container 48a71440eb0c
Successfully built b08dcf958356
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
travis_time:end:026ea82b:start=1568210508061729415,finish=1568210797030395568,duration=288968666153,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0e916b76[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/583654690/log.txt)