## Status: Passing 
Build: [1089](https://travis-ci.org/precice/systemtests/builds/611664101) 

Job: [1089.24](https://travis-ci.org/precice/systemtests/jobs/611664125) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:047264b6:start=1573699861091822220,finish=1573699861159015085,duration=67192865,event=resolvconf[0Ktravis_time:start:32dfc0c3[0Ktravis_time:end:32dfc0c3:start=1573699861164574877,finish=1573699861271027765,duration=106452888,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:01a989f8[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:01a989f8:start=1573699861360752718,finish=1573699861668056468,duration=307303750,event=configure[0Ktravis_time:start:0d42cb24[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d42cb24:start=1573699861673972857,finish=1573699874476975398,duration=12803002541,event=configure[0Ktravis_time:start:029780a6[0Ktravis_fold:start:services[0Ktravis_time:start:06562476[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06562476:start=1573699874505702605,finish=1573699874521315651,duration=15613046,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06562476:start=1573699874505702605,finish=1573699877528543446,duration=3022840841,event=services[0Ktravis_time:start:166311c0[0Ktravis_time:end:166311c0:start=1573699877533947994,finish=1573699877537033571,duration=3085577,event=fix_ps4[0Ktravis_time:start:28eb5b78[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0f5a9990[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0f5a9990:start=1573699877546727951,finish=1573699883777774452,duration=6231046501,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e39228c1c8cf63923ead04a7e05071545b49caa0
travis_fold:end:git.checkout[0K
travis_time:end:0f5a9990:start=1573699877546727951,finish=1573699884525690418,duration=6978962467,event=checkout[0Ktravis_time:start:0324e8bb[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0324e8bb:start=1573699884531291233,finish=1573699884543622273,duration=12331040,event=env[0Ktravis_time:start:0a49c0a0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0a49c0a0:start=1573699884549643596,finish=1573699884556302409,duration=6658813,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:18351c38[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:e38a42902a0744dbd62f72b127d54fbfb9a48dd09f601ebc33441d2daef7ed19
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:18351c38:start=1573699884928881493,finish=1573700005766997148,duration=120838115655,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07f8b505[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07f8b505:start=1573700010417288721,finish=1573700012116510965,duration=1699222244,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1c3948fb[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/611664125/log.txt)