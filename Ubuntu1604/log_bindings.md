System testing at Sun May  5 12:21:38 2019
 # Status : Failing
 # [Job url](https://travis-ci.org/shkodm/systemtests/builds/528423596)
## Triggered by: [push](https://github.com/shkodm/systemtests/compare/b16a26eb6775...fb2d43b9934d)
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/57b164a8d4112c5e57a4eef1f636d3c109524d69...269012c2748bf5513bc244ad9f50d886de05a18b)
## Last 100 lines of the job log at the moment of push...
```
Setting up libpython3.5-stdlib:amd64 (3.5.2-2ubuntu0~16.04.5) ...
Setting up python3.5 (3.5.2-2ubuntu0~16.04.5) ...
Setting up libpython3-stdlib:amd64 (3.5.1-3) ...
Setting up libpython3.5:amd64 (3.5.2-2ubuntu0~16.04.5) ...
Setting up libpython3.5-dev:amd64 (3.5.2-2ubuntu0~16.04.5) ...
Setting up libpython3-dev:amd64 (3.5.1-3) ...
Setting up python3.5-dev (3.5.2-2ubuntu0~16.04.5) ...
Setting up dh-python (2.20151103ubuntu1.1) ...
Setting up python3 (3.5.1-3) ...
running python rtupdate hooks for python3.5...
running python post-rtupdate hooks for python3.5...
Setting up python3-dev (3.5.1-3) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
 ---> 25b474963bab
Removing intermediate container 72a2875dc10a
Step 6/21 : RUN wget -q https://bootstrap.pypa.io/get-pip.py -O get-pip.py &&     python3 get-pip.py &&     python2 get-pip.py &&     pip2 install Cython mpi4py enum34 &&     pip3 install Cython mpi4py numpy enum34
 ---> Running in 618a99e3cd64
Collecting pip
  Downloading https://files.pythonhosted.org/packages/f9/fb/863012b13912709c13cf5cfdbfb304fa6c727659d6290438e1a88df9d848/pip-19.1-py2.py3-none-any.whl (1.4MB)
Collecting setuptools
  Downloading https://files.pythonhosted.org/packages/ec/51/f45cea425fd5cb0b0380f5b0f048ebc1da5b417e48d304838c02d6288a1e/setuptools-41.0.1-py2.py3-none-any.whl (575kB)
Collecting wheel
  Downloading https://files.pythonhosted.org/packages/96/ba/a4702cbb6a3a485239fbe9525443446203f00771af9ac000fa3ef2788201/wheel-0.33.1-py2.py3-none-any.whl
Installing collected packages: pip, setuptools, wheel
Successfully installed pip-19.1 setuptools-41.0.1 wheel-0.33.1
[91mDEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
[0mCollecting pip
  Using cached https://files.pythonhosted.org/packages/f9/fb/863012b13912709c13cf5cfdbfb304fa6c727659d6290438e1a88df9d848/pip-19.1-py2.py3-none-any.whl
Collecting setuptools
  Using cached https://files.pythonhosted.org/packages/ec/51/f45cea425fd5cb0b0380f5b0f048ebc1da5b417e48d304838c02d6288a1e/setuptools-41.0.1-py2.py3-none-any.whl
Collecting wheel
  Using cached https://files.pythonhosted.org/packages/96/ba/a4702cbb6a3a485239fbe9525443446203f00771af9ac000fa3ef2788201/wheel-0.33.1-py2.py3-none-any.whl
Installing collected packages: pip, setuptools, wheel
Successfully installed pip-19.1 setuptools-41.0.1 wheel-0.33.1
[91mDEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
[0mCollecting Cython
  Downloading https://files.pythonhosted.org/packages/16/7d/30ab222995d7dd551dee875c9f8fecf94b3c16a24f1c34d9a93031b19209/Cython-0.29.7-cp27-cp27mu-manylinux1_x86_64.whl (2.0MB)
Collecting mpi4py
  Downloading https://files.pythonhosted.org/packages/55/a2/c827b196070e161357b49287fa46d69f25641930fd5f854722319d431843/mpi4py-3.0.1.tar.gz (1.4MB)
Collecting enum34
  Downloading https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/58/43/98/b31d9ba388287a8523b04034f4306d83bb2be0492e2514f0be
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, enum34
Successfully installed Cython-0.29.7 enum34-1.1.6 mpi4py-3.0.1
Collecting Cython
  Downloading https://files.pythonhosted.org/packages/e7/bd/59054534d09830394470c14e4dd4a2e8fa64ac14559095a044208bf34c18/Cython-0.29.7-cp35-cp35m-manylinux1_x86_64.whl (2.0MB)
Collecting mpi4py
  Using cached https://files.pythonhosted.org/packages/55/a2/c827b196070e161357b49287fa46d69f25641930fd5f854722319d431843/mpi4py-3.0.1.tar.gz
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/f6/f3/cc6c6745347c1e997cc3e58390584a250b8e22b6dfc45414a7d69a3df016/numpy-1.16.3-cp35-cp35m-manylinux1_x86_64.whl (17.2MB)
Collecting enum34
  Downloading https://files.pythonhosted.org/packages/af/42/cb9355df32c69b553e72a2e28daee25d1611d2c0d9c272aa1d34204205b2/enum34-1.1.6-py3-none-any.whl
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/58/43/98/b31d9ba388287a8523b04034f4306d83bb2be0492e2514f0be
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.7 enum34-1.1.6 mpi4py-3.0.1 numpy-1.16.3
 ---> 42c8d0cd887c
Removing intermediate container 618a99e3cd64
Step 7/21 : WORKDIR $PRECICE_ROOT/src/precice/bindings/python
[91m/usr/local/lib/python2.7/dist-packages/Cython/Compiler/Main.py:367: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /precice/src/precice/bindings/python/precice.pyx
  tree = Parsing.p_module(s, pxd, full_module_name)
[0m#####
calling my_build_ext
using --mpicompiler=mpic++
#####
Compiling /precice/src/precice/bindings/python/precice.pyx because it changed.
[1/1] Cythonizing /precice/src/precice/bindings/python/precice.pyx
building 'precice' extension
creating build
creating build/temp.linux-x86_64-2.7
creating build/temp.linux-x86_64-2.7/precice
creating build/temp.linux-x86_64-2.7/precice/src
creating build/temp.linux-x86_64-2.7/precice/src/precice
creating build/temp.linux-x86_64-2.7/precice/src/precice/bindings
creating build/temp.linux-x86_64-2.7/precice/src/precice/bindings/python
x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/usr/include/python2.7 -c /precice/src/precice/bindings/python/precice.cpp -o build/temp.linux-x86_64-2.7/precice/src/precice/bindings/python/precice.o -Wall -std=c++11 -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent/include -I/usr/lib/openmpi/include -I/usr/lib/openmpi/include/openmpi -pthread
[91mcc1plus: warning: command line option '-Wstrict-prototypes' is valid for C/ObjC but not for C++
[0mcreating build/lib.linux-x86_64-2.7
c++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -Wdate-time -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wl,-Bsymbolic-functions -Wl,-z,relro -Wdate-time -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format-security build/temp.linux-x86_64-2.7/precice/src/precice/bindings/python/precice.o -o build/lib.linux-x86_64-2.7/precice.so -lprecice -pthread -Wl,-rpath -Wl,/usr/lib/openmpi/lib -Wl,--enable-new-dtags -L/usr/lib/openmpi/lib -lmpi_cxx -lmpi
running install_lib
copying build/lib.linux-x86_64-2.7/precice.so -> /usr/local/lib/python2.7/dist-packages
running install_egg_info
running egg_info
creating precice.egg-info
writing requirements to precice.egg-info/requires.txt
writing precice.egg-info/PKG-INFO
writing top-level names to precice.egg-info/top_level.txt
writing dependency_links to precice.egg-info/dependency_links.txt
writing manifest file 'precice.egg-info/SOURCES.txt'
reading manifest file 'precice.egg-info/SOURCES.txt'
writing manifest file 'precice.egg-info/SOURCES.txt'
Copying precice.egg-info to /usr/local/lib/python2.7/dist-packages/precice-1.4-py2.7.egg-info
```
[Full job log](https://api.travis-ci.org/v3/job/528423603/log.txt)