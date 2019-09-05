 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581212684) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.13 enum34-1.1.6 mpi4py-3.0.2 numpy-1.17.1
 ---> aadf90d856c1
Removing intermediate container eb884cc7dd66
Step 6/14 : USER [secure]
 ---> Running in d613e0143dde
 ---> 6a7f4dcd00fc
Removing intermediate container d613e0143dde
Step 7/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 1d5261ea9a30
Removing intermediate container a56d7298732a
Step 8/14 : RUN pip3 install --user .
 ---> Running in 5a3d8e161618
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
  Created wheel for [secure]-future: filename=[secure]_future-1.5.2-cp35-cp35m-linux_x86_64.whl size=413550 sha256=d22de44fb944828dea56150821973d73637c99a60f51342a671e986634bd7f15
  Stored in directory: /tmp/pip-ephem-wheel-cache-e3_3qfo9/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.5.2
 ---> b136970bf36f
Removing intermediate container 5a3d8e161618
Step 9/14 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> fd85d5b54a38
Removing intermediate container c88c437cb599
Step 10/14 : RUN pip3 install --user .
 ---> Running in 5e3a855e8026
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /home/[secure]/.local/lib/python3.5/site-packages (from [secure]==1.5.2) (1.5.2)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.5.2) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.5.2-cp35-none-any.whl size=2575 sha256=6ad1c18fa62e704abefdabb0952ea110dff0084351497dfc9025c212d59c9e32
  Stored in directory: /tmp/pip-ephem-wheel-cache-l0a19p9e/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.5.2
 ---> bbc7ec92d9ea
Removing intermediate container 5e3a855e8026
Step 11/14 : WORKDIR /home/[secure]/
 ---> 36899d1b2855
Removing intermediate container 00a6a5670424
Step 12/14 : RUN git clone https://github.com/nutils/nutils.git &&     python3 -m pip install --user --editable nutils
 ---> Running in 696ba26adac8
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
 ---> 953da1b8fc17
Removing intermediate container 696ba26adac8
Step 13/14 : RUN mkdir -p Data/Input Data/Output Data/Exchange
 ---> Running in 87cfd1da7703
 ---> 0c6d698d42fe
Removing intermediate container 87cfd1da7703
Step 14/14 : WORKDIR /home/[secure]/nutils
 ---> e98c5b380060
Removing intermediate container 4c54a4295837
Successfully built e98c5b380060
Successfully tagged testcomposenutilsof_nutils-adapter:latest
Image for service nutils-adapter was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:be8e37fe141c3aebfdaea18d27b3ffa9ef98fadcfc17a3167f5925fc0e3dc0ea
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating nutils-adapter ... 
Creating openfoam-adapter-outer
Creating nutils-adapter
[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating nutils-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/TestCompose_nutils-of/referenceOutput /home/travis/build/[secure]/systemtests/TestCompose_nutils-of/Output
travis_time:end:030f20b8:start=1567693899276821276,finish=1567694298988613057,duration=399711791781,event=script[0K[32;1mThe command "python system_testing.py -s nutils-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:20fe0eb4[0K$ python push.py -s -t nutils-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581212700/log.txt)