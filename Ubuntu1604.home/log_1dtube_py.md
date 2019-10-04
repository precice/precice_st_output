 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593458246) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/a992016cf5d2...efd4521f157f) 
## Last 100 lines of the job log at the moment of push...
```
 Collecting kiwisolver>=1.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/ee/18/4cd2e84c6aff0c6a50479118083d20b9e676e5175a913c0ea76d700fc244/kiwisolver-1.1.0-cp35-cp35m-manylinux1_x86_64.whl (90kB)
Collecting cycler>=0.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting six>=1.5 (from python-dateutil>=2.1->matplotlib)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools in /usr/local/lib/python3.5/dist-packages (from kiwisolver>=1.0.1->matplotlib) (41.2.0)
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143967 sha256=8d507123e745ecd1c465f85b6f419ca94cdda68767df61505e8c0f2df8854860
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34, six, python-dateutil, pyparsing, kiwisolver, cycler, matplotlib, vtk
Successfully installed Cython-0.29.13 cycler-0.10.0 enum34-1.1.6 kiwisolver-1.1.0 matplotlib-3.0.3 mpi4py-3.0.2 numpy-1.17.2 pyparsing-2.4.2 python-dateutil-2.8.0 six-1.12.0 vtk-8.1.2
 ---> f80f7cdf4c7c
Removing intermediate container cf05e1288be8
Step 6/16 : ARG CACHEBUST
 ---> Running in 8e9d63d484f0
 ---> 2deb46b7d094
Removing intermediate container 8e9d63d484f0
Step 7/16 : RUN mkdir /Output
 ---> Running in 7669082e5fc7
 ---> 2bb2e5e20694
Removing intermediate container 7669082e5fc7
Step 8/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> e5454ec94734
Removing intermediate container c8914a90e0a6
Step 9/16 : RUN pip3 install --user .
 ---> Running in caecc193407e
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
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653613 sha256=9dcd59feb1b5333cf49e3c66f3acc2dff43f9152b388c70b05f91e3d1c0d3668
  Stored in directory: /tmp/pip-ephem-wheel-cache-3ro6p1ia/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> 101ea719bcf8
Removing intermediate container caecc193407e
Step 10/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> 3511d0e553ae
Removing intermediate container cc0d7fa958ec
Step 11/16 : RUN pip3 install --user .
 ---> Running in 588e82a77645
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /root/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=c9240294b0c164423aa446233e1e4c0b1ace11be7c42f6b7e7cbfd003c9a2cba
  Stored in directory: /tmp/pip-ephem-wheel-cache-m6_2xvjo/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> a2304d9c22de
Removing intermediate container 588e82a77645
Step 12/16 : WORKDIR /home/[secure]/
 ---> 426d6ca196e7
Removing intermediate container 9e9db39d5df3
Step 13/16 : RUN git clone https://github.com/Eder-K/elastictube1d.git
 ---> Running in 409731c8e0b2
[91mCloning into 'elastictube1d'...
[0m ---> 8cba57a836c6
Removing intermediate container 409731c8e0b2
Step 14/16 : WORKDIR /home/[secure]/elastictube1d
 ---> 605dc3fd78d3
Removing intermediate container 842ab3d48639
Step 15/16 : RUN ./Allrun
 ---> Running in d14693e59c4b
Starting Fluid participant...
Starting Structure participant...

Waiting for participants to finish...
(you may run 'tail -f Fluid.log' in another terminal to check the progress)
Fluid participant finished. Waiting for Structure participant...
Structure participant finished.

Simulation completed successfully! Output files of the simulation were written to 'VTK/fluid.*.vtk'.
 ---> c85e97fe62e9
Removing intermediate container d14693e59c4b
Step 16/16 : RUN cp -r VTK /Output/
 ---> Running in 6706a31c1ac2
 ---> c33de2d4d407
Removing intermediate container 6706a31c1ac2
Successfully built c33de2d4d407
Successfully tagged st_1dtube_py-ubuntu1604.home-develop:latest
841aa42d01943841278bfe999113c6cd35ceab5e7c3ae97bc2f16089452cbb0f
 ```
[Full job log](https://api.travis-ci.org/v3/job/593458268/log.txt)