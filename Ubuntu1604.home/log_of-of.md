## Status: Passing 
Build: [1266](https://travis-ci.org/precice/systemtests/builds/621095475) 

Job: [1266.15](https://travis-ci.org/precice/systemtests/jobs/621095490) 

Triggered by: [push](https://github.com/precice/systemtests/compare/13952c2945a9...25edd038370a) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:16e9f072[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:16e9f072:start=1575552252027599831,finish=1575552252259250589,duration=231650758,event=configure[0Ktravis_time:start:0199fa79[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0199fa79:start=1575552252264860995,finish=1575552262001652319,duration=9736791324,event=configure[0Ktravis_time:start:0d889c6a[0Ktravis_fold:start:services[0Ktravis_time:start:1462437e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1462437e:start=1575552262029126068,finish=1575552262044734425,duration=15608357,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1462437e:start=1575552262029126068,finish=1575552265051410626,duration=3022284558,event=services[0Ktravis_time:start:03852e2a[0Ktravis_time:end:03852e2a:start=1575552265056230486,finish=1575552265059467088,duration=3236602,event=fix_ps4[0Ktravis_time:start:039c7c86[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1275a0b0[0K$ git clone --depth=50 --branch=nutils-of_ubuntu1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1275a0b0:start=1575552265070368466,finish=1575552271986231119,duration=6915862653,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 25edd038370ae003d7f13dcdc0ab2f33bd024c4e
travis_fold:end:git.checkout[0K
travis_time:end:1275a0b0:start=1575552265070368466,finish=1575552272964540225,duration=7894171759,event=checkout[0Ktravis_time:start:0da99150[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0da99150:start=1575552272970389249,finish=1575552272983677344,duration=13288095,event=env[0Ktravis_time:start:1c1ce6bc[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1c1ce6bc:start=1575552272989611082,finish=1575552272996514240,duration=6903158,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:08089569[0K$ python system_testing.py -s of-of
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
Digest: sha256:76b87c8ea50a9e57b02181433e4edd807832e07ab450ec96b52da3ed35004282
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:08089569:start=1575552273352029861,finish=1575552393988540385,duration=120636510524,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:33e37ca8[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:33e37ca8:start=1575552398475893641,finish=1575552400091093677,duration=1615200036,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:009c40df[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/621095490/log.txt)