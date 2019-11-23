## Status: Passing 
Build: [1131](https://travis-ci.org/precice/systemtests/builds/615847024) 

Job: [1131.18](https://travis-ci.org/precice/systemtests/jobs/615847042) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:15eea4d8[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:15eea4d8:start=1574477570136473303,finish=1574477570705743430,duration=569270127,event=configure[0Ktravis_time:start:046da48f[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:046da48f:start=1574477570710570723,finish=1574477581484173871,duration=10773603148,event=configure[0Ktravis_time:start:03c69b62[0Ktravis_fold:start:services[0Ktravis_time:start:112cc6c0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:112cc6c0:start=1574477581512650391,finish=1574477581527961097,duration=15310706,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:112cc6c0:start=1574477581512650391,finish=1574477584534541047,duration=3021890656,event=services[0Ktravis_time:start:13667858[0Ktravis_time:end:13667858:start=1574477584540397887,finish=1574477584543700996,duration=3303109,event=fix_ps4[0Ktravis_time:start:146850d8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0c818c5e[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0c818c5e:start=1574477584553420852,finish=1574477590854352778,duration=6300931926,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:0c818c5e:start=1574477584553420852,finish=1574477591680245379,duration=7126824527,event=checkout[0Ktravis_time:start:18d4923f[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:18d4923f:start=1574477591684804515,finish=1574477591696008133,duration=11203618,event=env[0Ktravis_time:start:0a0f9020[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0a0f9020:start=1574477591701370891,finish=1574477591708323937,duration=6953046,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:012b59f7[0K$ python system_testing.py -s of-of
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
Digest: sha256:434364091ca51fc8b71e13677c447ae4b75692f28a8629fbc2e4cdaa18040de8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:012b59f7:start=1574477592067853199,finish=1574477712927658566,duration=120859805367,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:280578a0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:280578a0:start=1574477717654510021,finish=1574477719342925543,duration=1688415522,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:06f698ce[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/615847042/log.txt)