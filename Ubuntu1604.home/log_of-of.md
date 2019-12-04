## Status: Passing 
Build: [1256](https://travis-ci.org/precice/systemtests/builds/620607294) 

Job: [1256.15](https://travis-ci.org/precice/systemtests/jobs/620607316) 

Triggered by: [push](https://github.com/precice/systemtests/compare/db99b1df1818...f0c87c5da690) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02a6b1f0[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02a6b1f0:start=1575467056363637568,finish=1575467056796055448,duration=432417880,event=configure[0Ktravis_time:start:0b7e1fff[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0b7e1fff:start=1575467056800687782,finish=1575467066244598357,duration=9443910575,event=configure[0Ktravis_time:start:0c41e456[0Ktravis_fold:start:services[0Ktravis_time:start:114c287a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:114c287a:start=1575467066267870457,finish=1575467066280820240,duration=12949783,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:114c287a:start=1575467066267870457,finish=1575467069287302519,duration=3019432062,event=services[0Ktravis_time:start:0038f394[0Ktravis_time:end:0038f394:start=1575467069291431893,finish=1575467069294164504,duration=2732611,event=fix_ps4[0Ktravis_time:start:1eb98dd5[0K
travis_fold:start:git.checkout[0Ktravis_time:start:010a1c66[0K$ git clone --depth=50 --branch=nutils-of_ubuntu1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:010a1c66:start=1575467069302574195,finish=1575467074694467943,duration=5391893748,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf f0c87c5da6902d0ded043df8875d19222a1c2dbb
travis_fold:end:git.checkout[0K
travis_time:end:010a1c66:start=1575467069302574195,finish=1575467075306257933,duration=6003683738,event=checkout[0Ktravis_time:start:0402144c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0402144c:start=1575467075311116635,finish=1575467075321270475,duration=10153840,event=env[0Ktravis_time:start:05fa5e98[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:05fa5e98:start=1575467075325755147,finish=1575467075331428452,duration=5673305,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:03d473da[0K$ python system_testing.py -s of-of
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
Digest: sha256:715bdb658ce28c87b1344b87e535852cd579de49e1cc517a990ba19387287544
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03d473da:start=1575467075633270305,finish=1575467202260822792,duration=126627552487,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:056f0a39[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:056f0a39:start=1575467206099807707,finish=1575467207485445731,duration=1385638024,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:364dc2c0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/620607316/log.txt)