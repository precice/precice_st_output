## Status: Passing 
Build: [1580](https://travis-ci.org/precice/systemtests/builds/645031917) 

Job: [1580.24](https://travis-ci.org/precice/systemtests/jobs/645031941) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:158f6c1c[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:158f6c1c:start=1580643911694064246,finish=1580643912131206506,duration=437142260,event=configure[0Ktravis_time:start:1cdd3218[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1cdd3218:start=1580643912136163290,finish=1580643920254583169,duration=8118419879,event=configure[0Ktravis_time:start:1510bc1e[0Ktravis_fold:start:services[0Ktravis_time:start:0b799f68[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0b799f68:start=1580643920281239471,finish=1580643920294344905,duration=13105434,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0b799f68:start=1580643920281239471,finish=1580643923298611498,duration=3017372027,event=services[0Ktravis_time:start:10345408[0Ktravis_time:end:10345408:start=1580643923302586634,finish=1580643923305276332,duration=2689698,event=fix_ps4[0Ktravis_time:start:06d13a91[0K
travis_fold:start:git.checkout[0Ktravis_time:start:151fadd0[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:151fadd0:start=1580643923313533774,finish=1580643928785477094,duration=5471943320,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 0b61ba36cce94a5b89e38963d3eebc970dbfd8a0
travis_fold:end:git.checkout[0K
travis_time:end:151fadd0:start=1580643923313533774,finish=1580643929496643067,duration=6183109293,event=checkout[0Ktravis_time:start:1cd7fd14[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1cd7fd14:start=1580643929501142833,finish=1580643929512696587,duration=11553754,event=env[0Ktravis_time:start:012794ed[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:012794ed:start=1580643929517362341,finish=1580643929523301383,duration=5939042,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09cb1bfe[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

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
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0f3098a7565f7c13fb013bff8dc52e2c2c3cdd94aca48d41865ca1d71096b7ae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:09cb1bfe:start=1580643929806825822,finish=1580644057676912863,duration=127870087041,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0585e2b3[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0585e2b3:start=1580644061799385466,finish=1580644063210847627,duration=1411462161,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:010a7b88[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645031941/log.txt)