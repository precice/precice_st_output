## Status: Passing 
Build: [1094](https://travis-ci.org/precice/systemtests/builds/612166197) 

Job: [1094.24](https://travis-ci.org/precice/systemtests/jobs/612166221) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:0371c967:start=1573786344878445307,finish=1573786344960765422,duration=82320115,event=resolvconf[0Ktravis_time:start:129eac33[0Ktravis_time:end:129eac33:start=1573786344965624941,finish=1573786345089587344,duration=123962403,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:15201274[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:15201274:start=1573786345180238804,finish=1573786345504164495,duration=323925691,event=configure[0Ktravis_time:start:182e1f4b[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:182e1f4b:start=1573786345510668286,finish=1573786358532189375,duration=13021521089,event=configure[0Ktravis_time:start:036f7c84[0Ktravis_fold:start:services[0Ktravis_time:start:022f501f[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:022f501f:start=1573786358559608685,finish=1573786358574742794,duration=15134109,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:022f501f:start=1573786358559608685,finish=1573786361581600276,duration=3021991591,event=services[0Ktravis_time:start:00ba6de0[0Ktravis_time:end:00ba6de0:start=1573786361586909706,finish=1573786361590308692,duration=3398986,event=fix_ps4[0Ktravis_time:start:06da3dc4[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0e82ee5d[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0e82ee5d:start=1573786361599845957,finish=1573786367979220477,duration=6379374520,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e39228c1c8cf63923ead04a7e05071545b49caa0
travis_fold:end:git.checkout[0K
travis_time:end:0e82ee5d:start=1573786361599845957,finish=1573786368943589319,duration=7343743362,event=checkout[0Ktravis_time:start:00b685dc[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00b685dc:start=1573786368948957267,finish=1573786368959638796,duration=10681529,event=env[0Ktravis_time:start:0311cd3c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0311cd3c:start=1573786368964870102,finish=1573786368972196874,duration=7326772,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:05814a5c[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:0ae867a0bf4596155dec39c40214ef0bdc2941a0552d3578d83e96ddc5041ef4
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:05814a5c:start=1573786369354361089,finish=1573786490401301980,duration=121046940891,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:08cd3abe[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:08cd3abe:start=1573786495112564521,finish=1573786496915254762,duration=1802690241,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1f828ae2[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/612166221/log.txt)