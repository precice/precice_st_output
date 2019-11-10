## Status: Passing 
Build: [1068](https://travis-ci.org/precice/systemtests/builds/609999431) 

Job: [1068.14](https://travis-ci.org/precice/systemtests/jobs/609999445) 

Triggered by: [push](https://github.com/precice/systemtests/commit/5cfc071ae529) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:38dffff8[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:38dffff8:start=1573408321581458674,finish=1573408321886778352,duration=305319678,event=configure[0Ktravis_time:start:17860d58[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:17860d58:start=1573408321892952464,finish=1573408332526940848,duration=10633988384,event=configure[0Ktravis_time:start:1113dc34[0Ktravis_fold:start:services[0Ktravis_time:start:0892cc38[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0892cc38:start=1573408332554522452,finish=1573408332570344086,duration=15821634,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0892cc38:start=1573408332554522452,finish=1573408335578185972,duration=3023663520,event=services[0Ktravis_time:start:0fe7b57c[0Ktravis_time:end:0fe7b57c:start=1573408335584244071,finish=1573408335587540562,duration=3296491,event=fix_ps4[0Ktravis_time:start:004c6f44[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0ef7c8ea[0K$ git clone --depth=50 --branch=EderK-mpich_deploy https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0ef7c8ea:start=1573408335597851787,finish=1573408342071315712,duration=6473463925,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 5cfc071ae5291a49fcb583309c6169eb56dd805b
travis_fold:end:git.checkout[0K
travis_time:end:0ef7c8ea:start=1573408335597851787,finish=1573408342140877922,duration=6543026135,event=checkout[0Ktravis_time:start:166aec83[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:166aec83:start=1573408342146939128,finish=1573408342158045974,duration=11106846,event=env[0Ktravis_time:start:02c53c7a[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:02c53c7a:start=1573408342164096285,finish=1573408342171181855,duration=7085570,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:06b3e8b2[0K$ python system_testing.py -s of-of
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
Digest: sha256:44c638fda07529b4fa826c3e2802921e4745184ba890cdda8eff73606f82ea90
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:06b3e8b2:start=1573408342567130930,finish=1573408463817055977,duration=121249925047,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04b7190a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04b7190a:start=1573408468920357532,finish=1573408470690447167,duration=1770089635,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1cba7ca6[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/609999445/log.txt)