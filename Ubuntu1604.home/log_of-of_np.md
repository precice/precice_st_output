## Status: Passing 
Build: [1227](https://travis-ci.org/precice/systemtests/builds/618560778) 

Job: [1227.20](https://travis-ci.org/precice/systemtests/jobs/618560800) 

Triggered by: [push](https://github.com/precice/systemtests/compare/d440b60eb25a...e486b1f8560f) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:0c018117:start=1575030957209622241,finish=1575030957282274529,duration=72652288,event=resolvconf[0Ktravis_time:start:3598b405[0Ktravis_time:end:3598b405:start=1575030957288137052,finish=1575030957397143472,duration=109006420,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:09c3efa8[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:09c3efa8:start=1575030957485421921,finish=1575030957924417406,duration=438995485,event=configure[0Ktravis_time:start:06c68c68[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:06c68c68:start=1575030957930163133,finish=1575030970671283574,duration=12741120441,event=configure[0Ktravis_time:start:2100d5e4[0Ktravis_fold:start:services[0Ktravis_time:start:0030ac42[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0030ac42:start=1575030970698316508,finish=1575030970712813611,duration=14497103,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0030ac42:start=1575030970698316508,finish=1575030973719966875,duration=3021650367,event=services[0Ktravis_time:start:02976354[0Ktravis_time:end:02976354:start=1575030973725799472,finish=1575030973729352306,duration=3552834,event=fix_ps4[0Ktravis_time:start:009e1108[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1d4c78f0[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-fixpip1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1d4c78f0:start=1575030973740653535,finish=1575030980089244726,duration=6348591191,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e486b1f8560f13987c1ba6b812e649d8e1cf4c0c
travis_fold:end:git.checkout[0K
travis_time:end:1d4c78f0:start=1575030973740653535,finish=1575030980197802707,duration=6457149172,event=checkout[0Ktravis_time:start:151f39c6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:151f39c6:start=1575030980203634425,finish=1575030980216193219,duration=12558794,event=env[0Ktravis_time:start:0850d220[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0850d220:start=1575030980222862740,finish=1575030980231736767,duration=8874027,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0482cfc0[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
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

Creating network "testcomposeofofnp_default" with the default driver
Creating network "testcomposeofofnp_[secure]comm" with the default driver
Creating volume "testcomposeofofnp_output" with default driver
Creating volume "testcomposeofofnp_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f0b435d58bc6bf4fb69c4f19af360da26c7b396f81e4bf8d437d7314c7188d74
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0482cfc0:start=1575030980608404690,finish=1575031101526277360,duration=120917872670,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1b554a9a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem itravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618560800/log.txt)