## Status: Passing 
Build: [978](https://travis-ci.org/precice/systemtests/builds/599812617) 

Job: [978.20](https://travis-ci.org/precice/systemtests/jobs/599812637) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 

---
Last 100 lines of the job log at the moment of push:
```
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:22c9dfd0:start=1571439142454926697,finish=1571439142527045285,duration=72118588,event=resolvconf[0Ktravis_time:start:1ceb69c6[0Ktravis_time:end:1ceb69c6:start=1571439142532822890,finish=1571439142649005615,duration=116182725,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:15e44557[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:15e44557:start=1571439142747134598,finish=1571439143297918395,duration=550783797,event=configure[0Ktravis_time:start:03b58940[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:03b58940:start=1571439143305368382,finish=1571439154322907474,duration=11017539092,event=configure[0Ktravis_time:start:1337b6eb[0Ktravis_fold:start:services[0Ktravis_time:start:0a351ef4[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0a351ef4:start=1571439154350289890,finish=1571439154365053955,duration=14764065,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0a351ef4:start=1571439154350289890,finish=1571439157370713714,duration=3020423824,event=services[0Ktravis_time:start:0262cbf0[0Ktravis_time:end:0262cbf0:start=1571439157375955953,finish=1571439157379400289,duration=3444336,event=fix_ps4[0Ktravis_time:start:00a4bb64[0K
travis_fold:start:git.checkout[0Ktravis_time:start:213985a8[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:213985a8:start=1571439157389604393,finish=1571439164017063560,duration=6627459167,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:05baa2d4[0K$ git fetch origin +refs/pull/111/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/111/merge -> FETCH_HEAD
travis_time:end:05baa2d4:start=1571439164022421243,finish=1571439164453774228,duration=431352985,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:05baa2d4:start=1571439164022421243,finish=1571439164478117391,duration=455696148,event=checkout[0Ktravis_time:start:0c068040[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0c068040:start=1571439164483318351,finish=1571439164496230719,duration=12912368,event=env[0Ktravis_time:start:09144ec4[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:09144ec4:start=1571439164501233812,finish=1571439164508046276,duration=6812464,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1377357c[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:abc28e71defd133daf727eb6220447d4b2e15733a7d410a36239238646b31351
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1377357c:start=1571439164905182299,finish=1571439289736150584,duration=124830968285,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00af60b8[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/599812637/log.txt)