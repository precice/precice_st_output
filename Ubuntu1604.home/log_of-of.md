## Status: Passing 
Build: [1170](https://travis-ci.org/precice/systemtests/builds/617994421) 

Job: [1170.18](https://travis-ci.org/precice/systemtests/jobs/617994439) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0e8f2ab0:start=1574909479149095468,finish=1574909479212150345,duration=63054877,event=resolvconf[0Ktravis_time:start:13b5d438[0Ktravis_time:end:13b5d438:start=1574909479218117289,finish=1574909479323508509,duration=105391220,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:28443bee[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:28443bee:start=1574909479404449320,finish=1574909479764079515,duration=359630195,event=configure[0Ktravis_time:start:0193ef6f[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0193ef6f:start=1574909479769279837,finish=1574909488834477186,duration=9065197349,event=configure[0Ktravis_time:start:12d96c4d[0Ktravis_fold:start:services[0Ktravis_time:start:1abc0645[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1abc0645:start=1574909488861172062,finish=1574909488876047010,duration=14874948,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1abc0645:start=1574909488861172062,finish=1574909491881912704,duration=3020740642,event=services[0Ktravis_time:start:02825c5e[0Ktravis_time:end:02825c5e:start=1574909491887654686,finish=1574909491891850063,duration=4195377,event=fix_ps4[0Ktravis_time:start:00b0cd1e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:109d0340[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:109d0340:start=1574909491903003665,finish=1574909498063968949,duration=6160965284,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:109d0340:start=1574909491903003665,finish=1574909498170870128,duration=6267866463,event=checkout[0Ktravis_time:start:006dd8a5[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:006dd8a5:start=1574909498174593361,finish=1574909498186927910,duration=12334549,event=env[0Ktravis_time:start:1817ca54[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1817ca54:start=1574909498192334784,finish=1574909498199796219,duration=7461435,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:006e326c[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
      && sed -i ''s|gather-scatter\"|gather-scatter\" exchange-directory=\"/home/[secure]/Data/Exchange/\"
      network=\"eth0\"|g'' [secure]-config_serial.xml && ./runFluid && cp -r Fluid/
      /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-fluid
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  openfoam-adapter-solid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
      && sed -i ''s|gather-scatter\"|gather-scatter\" exchange-directory=\"/home/[secure]/Data/Exchange/\"
      network=\"eth0\"|g'' [secure]-config_serial.xml && ./runSolid && cp -r Solid/
      /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-solid
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  tutorial-data:
    container_name: tutorial-data
    image: alpine
    volumes:
    - output:/Output:rw
version: '3.0'
volumes:
  exchange: {}
  output: {}

Creating network "testcomposeofof_default" with the default driver
Creating network "testcomposeofof_[secure]comm" with the default driver
Creating volume "testcomposeofof_output" with default driver
Creating volume "testcomposeofof_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:b4cd2d454d68843068cbd63106533105383ce6a650bf581e97e0a0196527023a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:006e326c:start=1574909498537868166,finish=1574909619239720863,duration=120701852697,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:274f33fa:start=1574909623507141400,finish=1574909625080048224,duration=1572906824,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1052377a[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/617994439/log.txt)