## Status: Passing 
Build: [1580](https://travis-ci.org/precice/systemtests/builds/645031917) 

Job: [1580.18](https://travis-ci.org/precice/systemtests/jobs/645031935) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
docker start/running, process 3892
travis_fold:end:docker_mtu[0Ktravis_time:end:0f9e7190:start=1580643701430027261,finish=1580643702615315995,duration=1185288734,event=set_docker_mtu[0Ktravis_time:start:2015979a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2015979a:start=1580643702619417711,finish=1580643702679098492,duration=59680781,event=resolvconf[0Ktravis_time:start:200142b8[0Ktravis_time:end:200142b8:start=1580643702683138378,finish=1580643702766695497,duration=83557119,event=maven_central_mirror[0Ktravis_time:start:13b90f78[0Ktravis_time:end:13b90f78:start=1580643702770877609,finish=1580643702836488152,duration=65610543,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:11e57bb4[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:11e57bb4:start=1580643702906162365,finish=1580643703483647416,duration=577485051,event=configure[0Ktravis_time:start:029f0906[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:029f0906:start=1580643703487912445,finish=1580643711582467408,duration=8094554963,event=configure[0Ktravis_time:start:1575abfc[0Ktravis_fold:start:services[0Ktravis_time:start:027f6bfe[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:027f6bfe:start=1580643711605378376,finish=1580643711618520875,duration=13142499,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:027f6bfe:start=1580643711605378376,finish=1580643714622961793,duration=3017583417,event=services[0Ktravis_time:start:12899a10[0Ktravis_time:end:12899a10:start=1580643714626924441,finish=1580643714629679916,duration=2755475,event=fix_ps4[0Ktravis_time:start:1b2a3648[0K
travis_fold:start:git.checkout[0Ktravis_time:start:016c11c2[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:016c11c2:start=1580643714637241716,finish=1580643719919776848,duration=5282535132,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 0b61ba36cce94a5b89e38963d3eebc970dbfd8a0
travis_fold:end:git.checkout[0K
travis_time:end:016c11c2:start=1580643714637241716,finish=1580643720808844447,duration=6171602731,event=checkout[0Ktravis_time:start:01b39858[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01b39858:start=1580643720813647925,finish=1580643720824186149,duration=10538224,event=env[0Ktravis_time:start:0d114059[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0d114059:start=1580643720828687120,finish=1580643720833919226,duration=5232106,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0b002035[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

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
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0f3098a7565f7c13fb013bff8dc52e2c2c3cdd94aca48d41865ca1d71096b7ae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:0b002035:start=1580643721119939978,finish=1580643849211936320,duration=128091996342,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:13bd5208[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645031935/log.txt)