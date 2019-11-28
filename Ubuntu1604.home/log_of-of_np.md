## Status: Passing 
Build: [1170](https://travis-ci.org/precice/systemtests/builds/617994421) 

Job: [1170.24](https://travis-ci.org/precice/systemtests/jobs/617994445) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:3918e706:start=1574909712608657392,finish=1574909712691224127,duration=82566735,event=resolvconf[0Ktravis_time:start:12874d85[0Ktravis_time:end:12874d85:start=1574909712696848908,finish=1574909712820820594,duration=123971686,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:04fd45fc[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:04fd45fc:start=1574909712910566330,finish=1574909713165481560,duration=254915230,event=configure[0Ktravis_time:start:08a793a1[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:08a793a1:start=1574909713172433295,finish=1574909724112940538,duration=10940507243,event=configure[0Ktravis_time:start:0478ec00[0Ktravis_fold:start:services[0Ktravis_time:start:0ca77b28[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0ca77b28:start=1574909724141599410,finish=1574909724156814677,duration=15215267,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0ca77b28:start=1574909724141599410,finish=1574909727162743322,duration=3021143912,event=services[0Ktravis_time:start:0f1b584a[0Ktravis_time:end:0f1b584a:start=1574909727167121444,finish=1574909727170393371,duration=3271927,event=fix_ps4[0Ktravis_time:start:19b493e0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:10a0f17a[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:10a0f17a:start=1574909727179769005,finish=1574909733541621000,duration=6361851995,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:10a0f17a:start=1574909727179769005,finish=1574909734011814330,duration=6832045325,event=checkout[0Ktravis_time:start:0bb9a02e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0bb9a02e:start=1574909734016795177,finish=1574909734028428812,duration=11633635,event=env[0Ktravis_time:start:1aced91b[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1aced91b:start=1574909734033245367,finish=1574909734040070431,duration=6825064,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:011f3e74[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:b4cd2d454d68843068cbd63106533105383ce6a650bf581e97e0a0196527023a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:011f3e74:start=1574909734420682655,finish=1574909855499218335,duration=121078535680,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04cbca2c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04cbca2c:start=1574909860788281200,finish=1574909862505843746,duration=1717562546,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:00bc4a2c[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/617994445/log.txt)