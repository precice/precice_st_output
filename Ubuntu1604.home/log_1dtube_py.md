 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593438448) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/46a3f0d5dc83...a992016cf5d2) 
## Last 100 lines of the job log at the moment of push...
```
   Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143968 sha256=7040c02ca03cbb82126193374e51b660d0282c60885cb30020a99bceb54f4291
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34, six, python-dateutil, cycler, kiwisolver, pyparsing, matplotlib, vtk
Successfully installed Cython-0.29.13 cycler-0.10.0 enum34-1.1.6 kiwisolver-1.1.0 matplotlib-3.0.3 mpi4py-3.0.2 numpy-1.17.2 pyparsing-2.4.2 python-dateutil-2.8.0 six-1.12.0 vtk-8.1.2
 ---> 6216333b2b94
Removing intermediate container 720f9468b597
Step 6/16 : ARG CACHEBUST
 ---> Running in 215a07ffe782
 ---> 71abfc65e112
Removing intermediate container 215a07ffe782
Step 7/16 : RUN mkdir /Output
 ---> Running in 28356386ba1d
 ---> a6c090c94e4d
Removing intermediate container 28356386ba1d
Step 8/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 1933e44af304
Removing intermediate container 9d32b48323b1
Step 9/16 : RUN pip3 install --user .
 ---> Running in 9ba89128a6db
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
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653577 sha256=9d670fe22f37d175a95385ad20d5d276dbf20045cdf347b7b47b1cc5fc1d0aff
  Stored in directory: /tmp/pip-ephem-wheel-cache-bmvi47dn/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> a44a1ad20d8d
Removing intermediate container 9ba89128a6db
Step 10/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> b12a2d0e8969
Removing intermediate container 46034117df44
Step 11/16 : RUN pip3 install --user .
 ---> Running in 4f993f26b5a8
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /root/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=0af7d1bc97f7949bc8855b7b135fa6bc3b4ed16356e3835d3b4b83fcc3aaf281
  Stored in directory: /tmp/pip-ephem-wheel-cache-k4bozfcy/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> 05051644684f
Removing intermediate container 4f993f26b5a8
Step 12/16 : WORKDIR /home/[secure]/
 ---> 219d9f8ce297
Removing intermediate container a6c13ec43ee6
Step 13/16 : RUN git clone https://github.com/Eder-K/elastictube1d.git
 ---> Running in f54d1f5a38b8
[91mCloning into 'elastictube1d'...
[0m ---> 866e91531a5a
Removing intermediate container f54d1f5a38b8
Step 14/16 : WORKDIR /home/[secure]/elastictube1d
 ---> e305cd470802
Removing intermediate container 5f3be81a642d
Step 15/16 : RUN ./Allrun
 ---> Running in 77053d215722
Starting Fluid participant...
Starting Structure participant...

Waiting for participants to finish...
(you may run 'tail -f Fluid.log' in another terminal to check the progress)
Fluid participant finished. Waiting for Structure participant...
Structure participant finished.

Simulation completed successfully! Output files of the simulation were written to 'VTK/fluid.*.vtk'.
 ---> a7714b792484
Removing intermediate container 77053d215722
Step 16/16 : RUN cp -r VTK /Output/
 ---> Running in 1ef3f9ef555b
 ---> b4c9d2f75f8e
Removing intermediate container 1ef3f9ef555b
Successfully built b4c9d2f75f8e
Successfully tagged st_1dtube_py-ubuntu1604.home-develop:latest
6b7f6c474cb4d77fb0a544f19511ca78b70b3cab4f06ebf816ab0669b117fe74
EXECUTING: docker build --network=host --file Dockerfile --tag st_1dtube_py-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_1dtube_py-ubuntu1604.home-develop st_1dtube_py-ubuntu1604.home-develop
EXECUTING: docker cp st_1dtube_py-ubuntu1604.home-develop:Output . 
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/Test_1dtube_py/referenceOutput /home/travis/build/[secure]/systemtests/tests/Test_1dtube_py/Output
travis_time:end:058b85b0:start=1570181920046002489,finish=1570182096805725185,duration=176759722696,event=script[0K[32;1mThe command "python system_testing.py -s 1dtube_py" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:252267ea[0K$ python push.py -s -t 1dtube_py
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593438478/log.txt)