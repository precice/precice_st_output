## Status: Passing 
Build: [1324](https://travis-ci.org/precice/systemtests/builds/626625324) 

Job: [1324.18](https://travis-ci.org/precice/systemtests/jobs/626625348) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:0872fc7c:start=1576670205430696093,finish=1576670205488755110,duration=58059017,event=resolvconf[0Ktravis_time:start:0ca2691b[0Ktravis_time:end:0ca2691b:start=1576670205493435329,finish=1576670205568629031,duration=75193702,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1a417cee[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1a417cee:start=1576670205642983639,finish=1576670207201225871,duration=1558242232,event=configure[0Ktravis_time:start:011ba9c4[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:011ba9c4:start=1576670207206001327,finish=1576670216432194007,duration=9226192680,event=configure[0Ktravis_time:start:0cf1c858[0Ktravis_fold:start:services[0Ktravis_time:start:063f263a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:063f263a:start=1576670216456232985,finish=1576670216470245177,duration=14012192,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:063f263a:start=1576670216456232985,finish=1576670219476433604,duration=3020200619,event=services[0Ktravis_time:start:0450eb10[0Ktravis_time:end:0450eb10:start=1576670219481645533,finish=1576670219484773392,duration=3127859,event=fix_ps4[0Ktravis_time:start:00db16b8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:105b7308[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:105b7308:start=1576670219494716687,finish=1576670224842130362,duration=5347413675,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ff457bed2521c9ab78f7f6e490c7785219151c1e
travis_fold:end:git.checkout[0K
travis_time:end:105b7308:start=1576670219494716687,finish=1576670225604061731,duration=6109345044,event=checkout[0Ktravis_time:start:269bc442[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:269bc442:start=1576670225608384441,finish=1576670225619011898,duration=10627457,event=env[0Ktravis_time:start:12c2f0c3[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:12c2f0c3:start=1576670225623437252,finish=1576670225628731559,duration=5294307,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:23f997ac[0K$ python system_testing.py -s of-of
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
Digest: sha256:c3a9c88d2a644a109c91ceb8b95f57d3e2389d374e84bdd06d85311542068410
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:23f997ac:start=1576670225918610353,finish=1576670339686969650,duration=113768359297,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:05aeffc6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:05aeffc6:start=1576670343771834102,finish=1576670345167667977,duration=1395833875,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:00244c9e[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/626625348/log.txt)