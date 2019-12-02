## Status: Passing 
Build: [1239](https://travis-ci.org/precice/systemtests/builds/619372101) 

Job: [1239.21](https://travis-ci.org/precice/systemtests/jobs/619372124) 

Triggered by: [push](https://github.com/precice/systemtests/compare/cf8e616f4d09...39aadec5ed5b) 

---
Last 100 lines of the job log at the moment of push:
```
start: Job is already running: docker
travis_time:end:2cc764b8:start=1575245600656070232,finish=1575245600671258345,duration=15188113,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2cc764b8:start=1575245600656070232,finish=1575245603677649277,duration=3021579045,event=services[0Ktravis_time:start:17ca77bd[0Ktravis_time:end:17ca77bd:start=1575245603681999471,finish=1575245603685364426,duration=3364955,event=fix_ps4[0Ktravis_time:start:2f76862b[0K
travis_fold:start:git.checkout[0Ktravis_time:start:12727566[0K$ git clone --depth=50 --branch=nutils-of_ubuntu1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:12727566:start=1575245603693868998,finish=1575245609977005026,duration=6283136028,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 39aadec5ed5bb49c22278968a5e50399f98ce8d3
travis_fold:end:git.checkout[0K
travis_time:end:12727566:start=1575245603693868998,finish=1575245610950294977,duration=7256425979,event=checkout[0Ktravis_time:start:0394cc44[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0394cc44:start=1575245610955237761,finish=1575245610967484787,duration=12247026,event=env[0Ktravis_time:start:0eda8790[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0eda8790:start=1575245610973003436,finish=1575245610980062394,duration=7058958,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:055f431b[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:70fe2faa72b2f0b36bebe52feee9ebbc2d8a68c08257a7c3fe32a7a746f8f227
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:055f431b:start=1575245611362863886,finish=1575245732564064506,duration=121201200620,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0379446a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/619372124/log.txt)