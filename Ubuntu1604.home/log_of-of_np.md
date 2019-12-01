## Status: Passing 
Build: [1237](https://travis-ci.org/precice/systemtests/builds/619351844) 

Job: [1237.20](https://travis-ci.org/precice/systemtests/jobs/619351864) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5cd65d21e48f...60b68152f174) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:07a8e768[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:07a8e768:start=1575240637420818922,finish=1575240637967007994,duration=546189072,event=configure[0Ktravis_time:start:15f2a368[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:15f2a368:start=1575240637972654018,finish=1575240647498855449,duration=9526201431,event=configure[0Ktravis_time:start:01e1df08[0Ktravis_fold:start:services[0Ktravis_time:start:27abc9c9[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:27abc9c9:start=1575240647525951904,finish=1575240647540660222,duration=14708318,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:27abc9c9:start=1575240647525951904,finish=1575240650546915418,duration=3020963514,event=services[0Ktravis_time:start:20a4a770[0Ktravis_time:end:20a4a770:start=1575240650552548505,finish=1575240650555611982,duration=3063477,event=fix_ps4[0Ktravis_time:start:1510226d[0K
travis_fold:start:git.checkout[0Ktravis_time:start:2af2f8d8[0K$ git clone --depth=50 --branch=nutils-of_ubuntu1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:2af2f8d8:start=1575240650565523317,finish=1575240656841917879,duration=6276394562,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 60b68152f174e23f2e1ccc72a51e24312ef04254
travis_fold:end:git.checkout[0K
travis_time:end:2af2f8d8:start=1575240650565523317,finish=1575240657665157189,duration=7099633872,event=checkout[0Ktravis_time:start:0dd075d0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0dd075d0:start=1575240657670899868,finish=1575240657682837822,duration=11937954,event=env[0Ktravis_time:start:158283a4[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:158283a4:start=1575240657687294644,finish=1575240657693434663,duration=6140019,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:11237baf[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:17df4e0778368c5680a67d4fbd568496224f149d9b071688dad9e92221715498
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:11237baf:start=1575240658032836751,finish=1575240779241177036,duration=121208340285,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:190f55d6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:190f55d6:start=1575240784137432358,finish=1575240785832637504,duration=1695205146,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0f21af48[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/619351864/log.txt)