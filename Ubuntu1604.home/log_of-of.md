## Status: Passing 
Build: [1085](https://travis-ci.org/precice/systemtests/builds/611163313) 

Job: [1085.18](https://travis-ci.org/precice/systemtests/jobs/611163331) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/be03fa4f457521db4ca77bac58da891a5245c954...e39228c1c8cf63923ead04a7e05071545b49caa0) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00a802a0[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00a802a0:start=1573613440971478477,finish=1573613441400801273,duration=429322796,event=configure[0Ktravis_time:start:193a0e2e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:193a0e2e:start=1573613441407923711,finish=1573613452853914377,duration=11445990666,event=configure[0Ktravis_time:start:317ea8a7[0Ktravis_fold:start:services[0Ktravis_time:start:198eb9ac[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:198eb9ac:start=1573613452880548980,finish=1573613452896573729,duration=16024749,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:198eb9ac:start=1573613452880548980,finish=1573613455902198708,duration=3021649728,event=services[0Ktravis_time:start:077dd106[0Ktravis_time:end:077dd106:start=1573613455907300760,finish=1573613455910246456,duration=2945696,event=fix_ps4[0Ktravis_time:start:0509ff26[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08fa7df2[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08fa7df2:start=1573613455920331266,finish=1573613462240418077,duration=6320086811,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e39228c1c8cf63923ead04a7e05071545b49caa0
travis_fold:end:git.checkout[0K
travis_time:end:08fa7df2:start=1573613455920331266,finish=1573613462449911051,duration=6529579785,event=checkout[0Ktravis_time:start:0235ef78[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0235ef78:start=1573613462454901277,finish=1573613462470917254,duration=16015977,event=env[0Ktravis_time:start:1c83108c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1c83108c:start=1573613462476706717,finish=1573613462482892487,duration=6185770,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0cbdda14[0K$ python system_testing.py -s of-of
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
Digest: sha256:eaa389694a370d827f8d13708456ce515f27efde4eb0b77abb736faddffc304d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0cbdda14:start=1573613462845843063,finish=1573613585624265472,duration=122778422409,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04cdbf08[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04cdbf08:start=1573613590466208444,finish=1573613592318859672,duration=1852651228,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2678816d[0KCloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/611163331/log.txt)