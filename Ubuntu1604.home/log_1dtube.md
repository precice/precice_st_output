 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/591102069) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/887c8e1583c8^...46a3f0d5dc83) 
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
  Created wheel for mpi4py: filename=mpi4py-3.0.2-cp35-cp35m-linux_x86_64.whl size=2143984 sha256=156c246764d50dfe116fca48d4d24da55fdaffded0206e83c0bd63f79b470902
  Stored in directory: /root/.cache/pip/wheels/a7/12/be/11b9ba83d337f1647a0fdea73fbe28a58b0593e64723233d64
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34, pyparsing, six, python-dateutil, kiwisolver, cycler, matplotlib, vtk
Successfully installed Cython-0.29.13 cycler-0.10.0 enum34-1.1.6 kiwisolver-1.1.0 matplotlib-3.0.3 mpi4py-3.0.2 numpy-1.17.2 pyparsing-2.4.2 python-dateutil-2.8.0 six-1.12.0 vtk-8.1.2
 ---> 820bc27ce82f
Removing intermediate container b25be430490b
Step 6/16 : ARG CACHEBUST
 ---> Running in bb14e8e09826
 ---> 543b0bec7c85
Removing intermediate container bb14e8e09826
Step 7/16 : RUN mkdir /Output
 ---> Running in 3e971f023f81
 ---> ad9784d05918
Removing intermediate container 3e971f023f81
Step 8/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python_future
 ---> c30c79b8d48b
Removing intermediate container 8c8644176f8f
Step 9/16 : RUN pip3 install --user .
 ---> Running in af1d696c15c6
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
  Created wheel for [secure]-future: filename=[secure]_future-1.6.1-cp35-cp35m-linux_x86_64.whl size=653577 sha256=dd5fb74b3b1dd0a925c988640f156410ac84303235b8470aa407355f4385c884
  Stored in directory: /tmp/pip-ephem-wheel-cache-79pwfv1_/wheels/2f/02/43/5cdf49c8639dfe9bda6c53aefb6cc3ac7647ed99b1f83af0ba
Successfully built [secure]-future
Installing collected packages: [secure]-future
Successfully installed [secure]-future-1.6.1
 ---> 73b159e5f781
Removing intermediate container af1d696c15c6
Step 10/16 : WORKDIR $PRECICE_ROOT/src/[secure]/bindings/python
 ---> c63b848355dc
Removing intermediate container c3964d1d625b
Step 11/16 : RUN pip3 install --user .
 ---> Running in e01f897dea5f
Processing /home/[secure]/[secure]/src/[secure]/bindings/python
Requirement already satisfied: [secure]_future in /root/.local/lib/python3.5/site-packages (from [secure]==1.6.1) (1.6.1)
Requirement already satisfied: cython in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (0.29.13)
Requirement already satisfied: mpi4py in /usr/local/lib/python3.5/dist-packages (from [secure]_future->[secure]==1.6.1) (3.0.2)
Building wheels for collected packages: [secure]
  Building wheel for [secure] (setup.py): started
  Building wheel for [secure] (setup.py): finished with status 'done'
  Created wheel for [secure]: filename=[secure]-1.6.1-cp35-none-any.whl size=2625 sha256=1d12c37d28a1f094ab6b5a3a6c7da93c93b4a5e7d8db2db767267c27d1052349
  Stored in directory: /tmp/pip-ephem-wheel-cache-3a148sct/wheels/e7/1f/7e/67833b7ad05611ebf90b18bfed2767db6e6c0fbf13bd500e29
Successfully built [secure]
Installing collected packages: [secure]
Successfully installed [secure]-1.6.1
 ---> 60eb49d6e9f9
Removing intermediate container e01f897dea5f
Step 12/16 : WORKDIR /home/[secure]/
 ---> 9e0526aa53d7
Removing intermediate container de1f6cb6f309
Step 13/16 : RUN git clone https://github.com/Eder-K/elastictube1d.git
 ---> Running in c37feb016a90
[91mCloning into 'elastictube1d'...
[0m ---> 7499120d3295
Removing intermediate container c37feb016a90
Step 14/16 : WORKDIR /home/[secure]/elastictube1d
 ---> 5cec6295a97b
Removing intermediate container 5d42bf44f0c1
Step 15/16 : RUN ./Allrun
 ---> Running in 077a9345388d
Starting Fluid participant...
Starting Structure participant...

Waiting for participants to finish...
(you may run 'tail -f Fluid.log' in another terminal to check the progress)
 ---> a3c821ac9e17
Removing intermediate container 7220cdd491d6
Successfully built a3c821ac9e17
Successfully tagged st_1dtube-ubuntu1604.home-develop:latest
d6dd7d22501cbe4f37b7cacab5e10515a6a7dc2092d6f6dfb84acf785e010af9
EXECUTING: docker build --network=host --file Dockerfile --tag st_1dtube-ubuntu1604.home-develop --build-arg from=[secure]/[secure]-ubuntu1604.home-develop:latest .
EXECUTING: docker run -it -d --name st_1dtube-ubuntu1604.home-develop st_1dtube-ubuntu1604.home-develop
EXECUTING: docker cp st_1dtube-ubuntu1604.home-develop:Output . 
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/Test_1dtube/referenceOutput /home/travis/build/[secure]/systemtests/tests/Test_1dtube/Output
travis_time:end:1e957f8c:start=1569767036835353111,finish=1569767208734754170,duration=171899401059,event=script[0K[32;1mThe command "python system_testing.py -s 1dtube" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:047f7ac5[0K$ python push.py -s -t 1dtube
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/591102091/log.txt)