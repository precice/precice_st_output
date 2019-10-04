 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593511816) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/ac9e17230162...f01784f81bb4) 
## Last 100 lines of the job log at the moment of push...
```
   Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143956 sha256=6a3f3d0e950f1e1dcc3c2a9b0c36f368203004a1218fa1bc61fcaf010e495a3a
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34, six, cycler, pyparsing, kiwisolver, python-dateutil, matplotlib, vtk
Successfully installed Cython-0.29.13 cycler-0.10.0 enum34-1.1.6 kiwisolver-1.1.0 matplotlib-3.0.3 mpi4py-3.0.2 numpy-1.17.2 pyparsing-2.4.2 python-dateutil-2.8.0 six-1.12.0 vtk-8.1.2
 ---> 4e63d18b51ad
Removing intermediate container d810f9a6dac2
Step 6/16 : ARG CACHEBUST
 ---> Running in 5f4ee7e6dcd7
 ---> b23cebc87fda
Removing intermediate container 5f4ee7e6dcd7
Step 7/16 : RUN mkdir /Output
 ---> Running in 404ebfab7618
 ---> 443d28e1baff
Removing intermediate container 404ebfab7618
Step 8/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> c0df77b0ab63
Removing intermediate container 82535b79af26
Step 9/16 : RUN pip3 install --user .
 ---> Running in 0cf257caa67c
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
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653556 sha256=2177a76242290e169869cb93313a7674d87568b4abaa0544bfd08b3c7fdbf475
  Stored in directory: /tmp/pip-ephem-wheel-cache-g92d9aa_/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> e998f4a49a53
Removing intermediate container 0cf257caa67c
Step 10/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> f893364840ad
Removing intermediate container cd8e626f9635
Step 11/16 : RUN pip3 install --user .
 ---> Running in 43950222fcb8
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /root/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=8d5707d1cc44576e4d32256ae43952468802439661956cc7853fce8b7ac01491
  Stored in directory: /tmp/pip-ephem-wheel-cache-r98zwmdp/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> f66decbb43ec
Removing intermediate container 43950222fcb8
Step 12/16 : WORKDIR /home/[secure]/
 ---> 3e0c51301d1a
Removing intermediate container 34f70a757ea0
Step 13/16 : RUN git clone https://github.com/Eder-K/elastictube1d.git
 ---> Running in 815c9fcb1f50
[91mCloning into 'elastictube1d'...
[0m ---> fb2e816385bb
Removing intermediate container 815c9fcb1f50
Step 14/16 : WORKDIR /home/[secure]/elastictube1d
 ---> 117a39603415
Removing intermediate container a9c913acde18
Step 15/16 : RUN ./Allrun
 ---> Running in f6668c1646e8
Starting Fluid participant...
Starting Structure participant...

Waiting for participants to finish...
(you may run 'tail -f Fluid.log' in another terminal to check the progress)
Fluid participant finished. Waiting for Structure participant...
Structure participant finished.

Simulation completed successfully! Output files of the simulation were written to 'VTK/fluid.*.vtk'.
 ---> 5b5c63ce231f
Removing intermediate container f6668c1646e8
Step 16/16 : RUN cp -r VTK /Output/
 ---> Running in 30ca933ba672
 ---> 9afc0bb5479c
Removing intermediate container 30ca933ba672
Successfully built 9afc0bb5479c
Successfully tagged st_1dtube_py-ubuntu1604.home-develop:latest
5e4679f1f0c734ba78273cd44861b305dad4b8f96744a3eea7359785d02855a1
EXECUTING: docker build --network=host --file Dockerfile --tag st_1dtube_py-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_1dtube_py-ubuntu1604.home-develop st_1dtube_py-ubuntu1604.home-develop
EXECUTING: docker cp st_1dtube_py-ubuntu1604.home-develop:Output . 
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/Test_1dtube_py/referenceOutput /home/travis/build/[secure]/systemtests/tests/Test_1dtube_py/Output
travis_time:end:2d9aba5b:start=1570204791710587025,finish=1570204966545840326,duration=174835253301,event=script[0K[32;1mThe command "python system_testing.py -s 1dtube_py" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0cd9a145[0K$ python push.py -s -t 1dtube_py
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/593511841/log.txt)