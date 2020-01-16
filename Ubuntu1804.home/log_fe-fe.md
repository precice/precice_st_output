## Status: Failure 
Build: [1461](https://travis-ci.org/precice/systemtests/builds/637943411) 

Job: [1461.4](https://travis-ci.org/precice/systemtests/jobs/637943415) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [fenics-adapter](https://github.com/precice/fenics-adapter/compare/150697fca846...bd6a64d89c81) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 00b6650b7dda
 ---> 858ffcf92edb
Removing intermediate container 00b6650b7dda
Step 3/8 : RUN apk add git
 ---> Running in 285e16b44afd
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
 ---> ce88e3741988
Removing intermediate container 285e16b44afd
Step 4/8 : ARG branch=develop
 ---> Running in 02839e9c0b8f
 ---> 50fa4b13167b
Removing intermediate container 02839e9c0b8f
Step 5/8 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1ea8df8f7480
[91mCloning into 'tutorials'...
[0m ---> abdd7393a843
Removing intermediate container 1ea8df8f7480
Step 6/8 : RUN mkdir configs && sed -i 's|<m2n:sockets from="HeatDirichlet" to="HeatNeumann"/>|<m2n:sockets from="HeatDirichlet" to="HeatNeumann" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"/>|g' $tutorial_path/[secure]-config.xml
 ---> Running in 5e65f25bd2a8
 ---> 8e256e050120
Removing intermediate container 5e65f25bd2a8
Step 7/8 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in df4ac9b96b4b
 ---> b5a1d356c240
Removing intermediate container df4ac9b96b4b
Step 8/8 : USER [secure]
 ---> Running in 6e72ab8a9bb7
 ---> 9bcdacd52e4d
Removing intermediate container 6e72ab8a9bb7

Successfully built 9bcdacd52e4d
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
[1A[2KCreating fenics-adapter-neumann ... [32mdone[0m[1B[1A[2KCreating fenics-adapter-dirichlet ... [32mdone[0m[1BAttaching to tutorial-data, fenics-adapter-neumann, fenics-adapter-dirichlet
[36mtutorial-data exited with code 0
[0m[33mfenics-adapter-neumann      |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[33mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m Default domain partitioning for simple interface is used: Left part of domain is a Dirichlet-type problem; right part is a Neumann-type problem
[32mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[33mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[32mfenics-adapter-dirichlet    |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[33mfenics-adapter-neumann      |[0m Calling FFC just-in-time (JIT) compiler, this may take some time.
[33mfenics-adapter-neumann      |[0m /usr/lib/python3.6/importlib/_bootstrap.py:219: UserWarning: Please don't import mpi4py before importing [secure], since this may lead to errors. If you need to import mpi4py, you can do so after importing [secure].
[33mfenics-adapter-neumann      |[0m   return f(*args, **kwds)
[32mfenics-adapter-dirichlet    |[0m /usr/lib/python3.6/importlib/_bootstrap.py:219: UserWarning: Please don't import mpi4py before importing [secure], since this may lead to errors. If you need to import mpi4py, you can do so after importing [secure].
[32mfenics-adapter-dirichlet    |[0m   return f(*args, **kwds)
[32mfenics-adapter-dirichlet    |[0m Traceback (most recent call last):
[32mfenics-adapter-dirichlet    |[0m   File "/home/[secure]/Data/Input/heat.py", line 116, in <module>
[32mfenics-adapter-dirichlet    |[0m     [secure] = Adapter(adapter_config_filename, interpolation_strategy=interpolation_strategy)
[32mfenics-adapter-dirichlet    |[0m   File "/home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py", line 259, in __init__
[32mfenics-adapter-dirichlet    |[0m     self._interface = [secure].Interface(self._solver_name, 0, 1)
[32mfenics-adapter-dirichlet    |[0m   File "[secure].pyx", line 35, in [secure].Interface.__cinit__
[32mfenics-adapter-dirichlet    |[0m TypeError: __cinit__() takes exactly 4 positional arguments (3 given)
[33mfenics-adapter-neumann      |[0m Traceback (most recent call last):
[33mfenics-adapter-neumann      |[0m   File "/home/[secure]/Data/Input/heat.py", line 116, in <module>
[33mfenics-adapter-neumann      |[0m     [secure] = Adapter(adapter_config_filename, interpolation_strategy=interpolation_strategy)
[33mfenics-adapter-neumann      |[0m   File "/home/[secure]/.local/lib/python3.6/site-packages/fenicsadapter/fenicsadapter.py", line 259, in __init__
[33mfenics-adapter-neumann      |[0m     self._interface = [secure].Interface(self._solver_name, 0, 1)
[33mfenics-adapter-neumann      |[0m   File "[secure].pyx", line 35, in [secure].Interface.__cinit__
[33mfenics-adapter-neumann      |[0m TypeError: __cinit__() takes exactly 4 positional arguments (3 given)
[32mfenics-adapter-dirichlet exited with code 1
[0m[33mfenics-adapter-neumann exited with code 1
[0mOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: .gitkeep
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatDirichlet-iterations.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-convergence.log
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput: [secure]-HeatNeumann-iterations.log
EXECUTING: export PRECICE_BASE=-ubuntu1804.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_fe-fe.Ubuntu1804.home/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['[secure]-HeatNeumann-iterations.log', '[secure]-HeatDirichlet-iterations.log', '[secure]-HeatNeumann-convergence.log']
Files only in output(right)   : []
travis_time:end:2382eb27:start=1579180289020862903,finish=1579180355615910603,duration=66595047700,event=script[0K[31;1mThe command "python system_testing.py -s fe-fe --base Ubuntu1804.home" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:052aa494[0K$ python push.py -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637943415/log.txt)