System testing at Sat Mar 30 18:42:07 2019
 # Status :  Passing 
 # [Job url](https://travis-ci.org/shkodm/systemtests/builds/513524773)
## Triggered by: [push](https://github.com/shkodm/systemtests/compare/2218cb89898b^...77160b8c85dc)
## Last 100 lines of the job log...
```
  Downloading https://files.pythonhosted.org/packages/c2/34/99ced126b3f41a908d8883570a67fbf900f10eea3cfdd11e388eb8ae9aac/Cython-0.29.6-cp35-cp35m-manylinux1_x86_64.whl (2.0MB)
Collecting mpi4py
  Using cached https://files.pythonhosted.org/packages/55/a2/c827b196070e161357b49287fa46d69f25641930fd5f854722319d431843/mpi4py-3.0.1.tar.gz
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/e3/18/4f013c3c3051f4e0ffbaa4bf247050d6d5e527fe9cb1907f5975b172f23f/numpy-1.16.2-cp35-cp35m-manylinux1_x86_64.whl (17.2MB)
Collecting enum34
  Downloading https://files.pythonhosted.org/packages/af/42/cb9355df32c69b553e72a2e28daee25d1611d2c0d9c272aa1d34204205b2/enum34-1.1.6-py3-none-any.whl
Building wheels for collected packages: mpi4py
  Building wheel for mpi4py (setup.py): started
  Building wheel for mpi4py (setup.py): finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/58/43/98/b31d9ba388287a8523b04034f4306d83bb2be0492e2514f0be
Successfully built mpi4py
Installing collected packages: Cython, mpi4py, numpy, enum34
Successfully installed Cython-0.29.6 enum34-1.1.6 mpi4py-3.0.1 numpy-1.16.2
 ---> 84e380d43ed1
Removing intermediate container 45488ae63392
Step 7/21 : WORKDIR $PRECICE_ROOT/src/precice/bindings/python
 ---> 539550750ff3
Removing intermediate container 5574874c6d2c
Step 8/21 : RUN python2 setup.py install
 ---> Running in 0b66d8428e9f
running install
#####
calling my_build
using --mpicompiler=mpic++
adding extension
#####
running build
running build_ext
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
 ---> f26d53fc4906
Removing intermediate container 0b66d8428e9f
Step 9/21 : WORKDIR $PRECICE_ROOT/src/precice/bindings/python
 ---> 642e1274626d
Removing intermediate container 0f7e509fab71
Step 10/21 : RUN python3 setup.py install
 ---> Running in f61832d0fcc3
running install
#####
calling my_build
using --mpicompiler=mpic++
adding extension
#####
running build
running build_ext
#####
calling my_build_ext
using --mpicompiler=mpic++
#####
building 'precice' extension
creating build/temp.linux-x86_64-3.5
creating build/temp.linux-x86_64-3.5/precice
creating build/temp.linux-x86_64-3.5/precice/src
creating build/temp.linux-x86_64-3.5/precice/src/precice
creating build/temp.linux-x86_64-3.5/precice/src/precice/bindings
creating build/temp.linux-x86_64-3.5/precice/src/precice/bindings/python
x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/usr/include/python3.5m -c /precice/src/precice/bindings/python/precice.cpp -o build/temp.linux-x86_64-3.5/precice/src/precice/bindings/python/precice.o -Wall -std=c++11 -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent/include -I/usr/lib/openmpi/include -I/usr/lib/openmpi/include/openmpi -pthread
[91mcc1plus: warning: command line option '-Wstrict-prototypes' is valid for C/ObjC but not for C++
[0m ---> f7011c719711
Removing intermediate container f61832d0fcc3
Step 11/21 : WORKDIR $PRECICE_ROOT/tools/solverdummies/python
 ---> 97ac973ad834
Removing intermediate container c89bbd9b1a40
Step 12/21 : RUN python2 solverdummy.py precice-config.xml SolverOne MeshOne & python solverdummy.py precice-config.xml SolverTwo MeshTwo
 ---> Running in 1853cbf0d719
[91mUnexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/LYNKI4MHG5IIWBG5XIWOYWJ5ZS:/var/lib/docker/overlay2/l/S4OWCICVGU4W673EGMK7LWLKWH:/var/lib/docker/overlay2/l/IN2ARQRUJPHJPXYBY572LYVSPZ:/var/lib/docker/overlay2/l/R26AV6JLUF65RVQPKBLCFXKJXM:/var/lib/docker/overlay2/l/5DEMJP3QD62DANK42BW2BOEL3V:/var/lib/docker/overlay2/l/SFJEQG2QUANAGM52LOCDCA6GMP:/var/lib/docker/overlay2/l/JV4W7ZXPQIBDSXVCBHVEIN3H2G:/var/lib/docker/overlay2/l/VAV4VQPBKHYCDGRJLOSQXQL6QP:/var/lib/docker/overlay2/l/5A7N6AMU6SLOM'
Unexpected end of /proc/mounts line `overlay / overlay rw,relatime,lowerdir=/var/lib/docker/overlay2/l/LYNKI4MHG5IIWBG5XIWOYWJ5ZS:/var/lib/docker/overlay2/l/S4OWCICVGU4W673EGMK7LWLKWH:/var/lib/docker/overlay2/l/IN2ARQRUJPHJPXYBY572LYVSPZ:/var/lib/docker/overlay2/l/R26AV6JLUF65RVQPKBLCFXKJXM:/var/lib/docker/overlay2/l/5DEMJP3QD62DANK42BW2BOEL3V:/var/lib/docker/overlay2/l/SFJEQG2QUANAGM52LOCDCA6GMP:/var/lib/docker/overlay2/l/JV4W7ZXPQIBDSXVCBHVEIN3H2G:/var/lib/docker/overlay2/l/VAV4VQPBKHYCDGRJLOSQXQL6QP:/var/lib/docker/overlay2/l/5A7N6AMU6SLOM'
Unexpected end of /proc/mounts line `WI2NNOV32OAL3:/var/lib/docker/overlay2/l/XLQ5ZF5TQLRC5H22XYVWPO4E4P:/var/lib/docker/overlay2/l/RE7JUBQCFHKXNVVYMHGSQWF4BI:/var/lib/docker/overlay2/l/237NAVZHGXUQRAEAEGMOS46UZG:/var/lib/docker/overlay2/l/YPMNCFEGBTID6DSBQIB3Q5FIVM:/var/lib/docker/overlay2/l/VFIGN5LFGGHAFRJAJTCOFSLRRB:/var/lib/docker/overlay2/l/XTAYZGRWJDQA45BJCHLWPN22Q6,upperdir=/var/lib/docker/overlay2/52f50b9b2cc1952acbe0867cf6457bdd83f27a80cfb805e7654267ea0a9e335e/diff,workdir=/var/lib/docker/overlay2/52f50b9b2cc1952acbe0867cf6457bdd83```
