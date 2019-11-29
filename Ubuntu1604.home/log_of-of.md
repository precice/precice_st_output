## Status: Passing 
Build: [1205](https://travis-ci.org/precice/systemtests/builds/618334138) 

Job: [1205.14](https://travis-ci.org/precice/systemtests/jobs/618334152) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f6ac64c472af...3b2ed1c3a41a) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:0bfce5f3:start=1575052051576327739,finish=1575052051645066750,duration=68739011,event=resolvconf[0Ktravis_time:start:2706fbd1[0Ktravis_time:end:2706fbd1:start=1575052051650104851,finish=1575052051765315138,duration=115210287,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:26e26712[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:26e26712:start=1575052051849688680,finish=1575052053065703886,duration=1216015206,event=configure[0Ktravis_time:start:001d1d10[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:001d1d10:start=1575052053071103127,finish=1575052063693142013,duration=10622038886,event=configure[0Ktravis_time:start:02857e30[0Ktravis_fold:start:services[0Ktravis_time:start:044f916b[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:044f916b:start=1575052063724090680,finish=1575052063740536456,duration=16445776,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:044f916b:start=1575052063724090680,finish=1575052066747378177,duration=3023287497,event=services[0Ktravis_time:start:0e0dc6b0[0Ktravis_time:end:0e0dc6b0:start=1575052066752280235,finish=1575052066755280652,duration=3000417,event=fix_ps4[0Ktravis_time:start:01479f00[0K
travis_fold:start:git.checkout[0Ktravis_time:start:132d2f12[0K$ git clone --depth=50 --branch=compatibility_PR_576_on_[secure]_core https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:132d2f12:start=1575052066764618375,finish=1575052073320389026,duration=6555770651,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3b2ed1c3a41a6dfa009f9cc83cedd5535382de8c
travis_fold:end:git.checkout[0K
travis_time:end:132d2f12:start=1575052066764618375,finish=1575052073593818120,duration=6829199745,event=checkout[0Ktravis_time:start:080b3d22[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:080b3d22:start=1575052073598939675,finish=1575052073608879633,duration=9939958,event=env[0Ktravis_time:start:034ee433[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:034ee433:start=1575052073614731041,finish=1575052073621672542,duration=6941501,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:13fc0f4c[0K$ python system_testing.py -s of-of
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
Digest: sha256:ce171974344908d9cd30d6b96441d1073584c84ad0e4bd47423ae72c52217f81
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:13fc0f4c:start=1575052073979191987,finish=1575052195108195306,duration=121129003319,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2b81da00[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2b81da00:start=1575052199848123544,finish=1575052201539846912,duration=1691723368,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0ae5ad24[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/618334152/log.txt)