 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593511816) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/ac9e17230162...f01784f81bb4) 
## Last 100 lines of the job log at the moment of push...
```
   Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143965 sha256=98d93c366c1b67253b196a442686b5051804ce7974e1d05ee0825013553e6531
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34, kiwisolver, six, python-dateutil, pyparsing, cycler, matplotlib, vtk
Successfully installed Cython-0.29.13 cycler-0.10.0 enum34-1.1.6 kiwisolver-1.1.0 matplotlib-3.0.3 mpi4py-3.0.2 numpy-1.17.2 pyparsing-2.4.2 python-dateutil-2.8.0 six-1.12.0 vtk-8.1.2
 ---> 696e25e0f71a
Removing intermediate container d080a16bd485
Step 6/16 : ARG CACHEBUST
 ---> Running in 0400efeca6e6
 ---> 0bb5985225ce
Removing intermediate container 0400efeca6e6
Step 7/16 : RUN mkdir /Output
 ---> Running in 66434cda6077
 ---> 7749f4f541b4
Removing intermediate container 66434cda6077
Step 8/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> 6f0394af2cfd
Removing intermediate container 68644e5c3d54
Step 9/16 : RUN pip3 install --user .
 ---> Running in 8fa03c05404f
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
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653558 sha256=ddb009d2faadfdb98c37a39cfe869f7c47cf809c93026d67f28d13d56ce62129
  Stored in directory: /tmp/pip-ephem-wheel-cache-j03fiesc/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> 0a5728320dc4
Removing intermediate container 8fa03c05404f
Step 10/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> 746ce978b578
Removing intermediate container d62e3fecbeca
Step 11/16 : RUN pip3 install --user .
 ---> Running in 434fbfc35176
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /root/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=094b1f7276e4bbcba1041c4d70855e7a5dcf9208ee88d4bdbd9e7d00119b645f
  Stored in directory: /tmp/pip-ephem-wheel-cache-lqyv1tza/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> f2d8c049845b
Removing intermediate container 434fbfc35176
Step 12/16 : WORKDIR /home/[secure]/
 ---> 4cb85723c4ec
Removing intermediate container e2dd2f7818c1
Step 13/16 : RUN git clone https://github.com/Eder-K/elastictube1d.git
 ---> Running in b318e0226b0a
[91mCloning into 'elastictube1d'...
[0m ---> 726f9d3bd52a
Removing intermediate container b318e0226b0a
Step 14/16 : WORKDIR /home/[secure]/elastictube1d
 ---> 9d6880a8a5c8
Removing intermediate container 8e785442d049
Step 15/16 : RUN ./Allrun
 ---> Running in cfa25cdb4dbe
Starting Fluid participant...
Starting Structure participant...

Waiting for participants to finish...
(you may run 'tail -f Fluid.log' in another terminal to check the progress)
Fluid participant finished. Waiting for Structure participant...
Structure participant finished.

Simulation completed successfully! Output files of the simulation were written to 'VTK/fluid.*.vtk'.
 ---> 24014f518642
Removing intermediate container cfa25cdb4dbe
Step 16/16 : RUN cp -r VTK /Output/
 ---> Running in 836dfbd1a1bc
 ---> c1d479624955
Removing intermediate container 836dfbd1a1bc
Successfully built c1d479624955
Successfully tagged st_1dtube_py-ubuntu1604.home-develop:latest
20abd4f7efe57c4cc0e6cb6ec617bdd65dca660ce981e9a4b899830a2bc655a0
EXECUTING: docker build --network=host --file Dockerfile --tag st_1dtube_py-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_1dtube_py-ubuntu1604.home-develop st_1dtube_py-ubuntu1604.home-develop
EXECUTING: docker cp st_1dtube_py-ubuntu1604.home-develop:Output . 
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/Test_1dtube_py/referenceOutput /home/travis/build/[secure]/systemtests/tests/Test_1dtube_py/Output
travis_time:end:084ea688:start=1570190934066443897,finish=1570191107531509319,duration=173465065422,event=script[0K[32;1mThe command "python system_testing.py -s 1dtube_py" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0b9a00ff[0K$ python push.py -s -t 1dtube_py
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593511841/log.txt)