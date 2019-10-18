## Status: Passing 
Build: [978](https://travis-ci.org/precice/systemtests/builds/599812617) 

Job: [978.14](https://travis-ci.org/precice/systemtests/jobs/599812631) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 

---
Last 100 lines of the job log at the moment of push:
```
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:15230bbc:start=1571438361658895253,finish=1571438361726393334,duration=67498081,event=resolvconf[0Ktravis_time:start:2a9f53af[0Ktravis_time:end:2a9f53af:start=1571438361731137826,finish=1571438361836609931,duration=105472105,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:025ffec7[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:025ffec7:start=1571438361921711591,finish=1571438362401354287,duration=479642696,event=configure[0Ktravis_time:start:0b28848c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0b28848c:start=1571438362407297935,finish=1571438372053263939,duration=9645966004,event=configure[0Ktravis_time:start:1a4ce7c0[0Ktravis_fold:start:services[0Ktravis_time:start:221aa3f2[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:221aa3f2:start=1571438372078039338,finish=1571438372091688514,duration=13649176,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:221aa3f2:start=1571438372078039338,finish=1571438375097422356,duration=3019383018,event=services[0Ktravis_time:start:060da69d[0Ktravis_time:end:060da69d:start=1571438375102204198,finish=1571438375105242251,duration=3038053,event=fix_ps4[0Ktravis_time:start:00f88fae[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0d7a6b01[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0d7a6b01:start=1571438375114693591,finish=1571438381352840229,duration=6238146638,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0e0783bc[0K$ git fetch origin +refs/pull/111/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/111/merge -> FETCH_HEAD
travis_time:end:0e0783bc:start=1571438381357519348,finish=1571438381802586289,duration=445066941,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0e0783bc:start=1571438381357519348,finish=1571438382085350469,duration=727831121,event=checkout[0Ktravis_time:start:08974660[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:08974660:start=1571438382090349515,finish=1571438382103718973,duration=13369458,event=env[0Ktravis_time:start:1efd7712[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1efd7712:start=1571438382109248980,finish=1571438382115047780,duration=5798800,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2f681436[0K$ python system_testing.py -s of-of
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:abc28e71defd133daf727eb6220447d4b2e15733a7d410a36239238646b31351
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2f681436:start=1571438382465902356,finish=1571438505017020613,duration=122551118257,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:189c0668[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/599812631/log.txt)