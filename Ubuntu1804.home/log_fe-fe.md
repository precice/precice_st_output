## Status: Failure 
Build: [1459](https://travis-ci.org/precice/systemtests/builds/637887909) 

Job: [1459.21](https://travis-ci.org/precice/systemtests/jobs/637887952) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/8 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/8 : ENV tutorial_path tutorials/HT/partitioned-heat/fenics-fenics
 ---> Running in 4aa35591556f
 ---> c46b6fb3e6f7
Removing intermediate container 4aa35591556f
Step 3/8 : RUN apk add git
 ---> Running in f39a9903bf43
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 65cfbc010074
Removing intermediate container f39a9903bf43
Step 4/8 : ARG branch=develop
 ---> Running in 00653ed96894
 ---> a0f413d658f2
Removing intermediate container 00653ed96894
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in f4c56f1894b0
[91mCloning into 'tutorials'...
[0m ---> 36c45ba02322
Removing intermediate container f4c56f1894b0
Step 6/8 : RUN mkdir configs && sed -i 's|network="lo"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config.xml
 ---> Running in d5170529a1ff
 ---> c93f28c015bd
Removing intermediate container d5170529a1ff
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in b8de4c88b89c
 ---> 48b04797372f
Removing intermediate container b8de4c88b89c
Step 8/8 : USER [secure]
 ---> Running in dfeabf6403df
 ---> c0ab6e43392a
Removing intermediate container dfeabf6403df

Successfully built c0ab6e43392a
Successfully tagged testcomposefefeubuntu1804home_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling fenics-adapter-dirichlet ([secure]/fenics-adapter-ubuntu1804.home-develop:latest)...
latest: Pulling from [secure]/fenics-adapter-ubuntu1804.home-develop
Digest: sha256:d3429ded2785adb523431333a97efb44bcb7c5a7efadbc694b7b52343e33f910
Status: Downloaded newer image for [secure]/fenics-adapter-ubuntu1804.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating fenics-adapter-dirichlet ... 
Creating fenics-adapter-neumann ... 
Creating fenics-adapter-dirichlet
Creating fenics-adapter-neumann
[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1BRunning the simulation...Be patient
fenics-adapter-dirichlet failed! Find the logs below
Attaching to fenics-adapter-dirichlet
[36mfenics-adapter-dirichlet    |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-dirichlet    |[0m /usr/lib/python3.6/importlib/_bootstrap.py:219: UserWarning: Please don't import mpi4py before importing [secure], since this may lead to errors. If you need to import mpi4py, you can do so after importing [secure].
[36mfenics-adapter-dirichlet    |[0m   return f(*args, **kwds)
[36mfenics-adapter-dirichlet    |[0m Traceback (most recent call last):
[36mfenics-adapter-dirichlet    |[0m   File "/home/[secure]/Data/Input/heat.py", line 116, in <module>
[36mfenics-adapter-dirichlet    |[0m     [secure] = Adapter(adapter_config_filename, interpolation_strategy=interpolation_strategy)
[36mfenics-adapter-dirichlet    |[0m   File "/home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py", line 259, in __init__
[36mfenics-adapter-dirichlet    |[0m     self._interface = [secure].Interface(self._solver_name, 0, 1)
[36mfenics-adapter-dirichlet    |[0m   File "[secure].pyx", line 35, in [secure].Interface.__cinit__
[36mfenics-adapter-dirichlet    |[0m TypeError: __cinit__() takes exactly 4 positional arguments (3 given)
fenics-adapter-neumann failed! Find the logs below
Attaching to fenics-adapter-neumann
[36mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[36mfenics-adapter-neumann      |[0m /usr/lib/python3.6/importlib/_bootstrap.py:219: UserWarning: Please don't import mpi4py before importing [secure], since this may lead to errors. If you need to import mpi4py, you can do so after importing [secure].
[36mfenics-adapter-neumann      |[0m   return f(*args, **kwds)
[36mfenics-adapter-neumann      |[0m Traceback (most recent call last):
[36mfenics-adapter-neumann      |[0m   File "/home/[secure]/Data/Input/heat.py", line 116, in <module>
[36mfenics-adapter-neumann      |[0m     [secure] = Adapter(adapter_config_filename, interpolation_strategy=interpolation_strategy)
[36mfenics-adapter-neumann      |[0m   File "/home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py", line 259, in __init__
[36mfenics-adapter-neumann      |[0m     self._interface = [secure].Interface(self._solver_name, 0, 1)
[36mfenics-adapter-neumann      |[0m   File "[secure].pyx", line 35, in [secure].Interface.__cinit__
[36mfenics-adapter-neumann      |[0m TypeError: __cinit__() takes exactly 4 positional arguments (3 given)
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh' returned non-zero exit status 1
travis_time:end:06cbbcb2:start=1579174747536375076,finish=1579174862249239179,duration=114712864103,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:04a3af6c[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637887952/log.txt)