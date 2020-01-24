## Status: Passing 
Build: [1484](https://travis-ci.org/precice/systemtests/builds/641298046) 

Job: [1484.25](https://travis-ci.org/precice/systemtests/jobs/641298093) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4c749ac41fec1ac0cc04f8e71fcd731e33705ab1...e37a006c80df4226e1d22b4d0f731f7780eae018) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:05a090c6[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:05a090c6:start=1579866770916773654,finish=1579866772574673323,duration=1657899669,event=configure[0Ktravis_time:start:18d33340[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:18d33340:start=1579866772579663318,finish=1579866781266742327,duration=8687079009,event=configure[0Ktravis_time:start:0ff2599e[0Ktravis_fold:start:services[0Ktravis_time:start:02e7b50e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:02e7b50e:start=1579866781289200140,finish=1579866781301632244,duration=12432104,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:02e7b50e:start=1579866781289200140,finish=1579866784307441117,duration=3018240977,event=services[0Ktravis_time:start:0537e90a[0Ktravis_time:end:0537e90a:start=1579866784311730833,finish=1579866784314279386,duration=2548553,event=fix_ps4[0Ktravis_time:start:078c820c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:02843f07[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:02843f07:start=1579866784322544847,finish=1579866789728175829,duration=5405630982,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e37a006c80df4226e1d22b4d0f731f7780eae018
travis_fold:end:git.checkout[0K
travis_time:end:02843f07:start=1579866784322544847,finish=1579866790390914555,duration=6068369708,event=checkout[0Ktravis_time:start:01eaa244[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01eaa244:start=1579866790395353569,finish=1579866790403336046,duration=7982477,event=env[0Ktravis_time:start:206c25b8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:206c25b8:start=1579866790407131909,finish=1579866790412504249,duration=5372340,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1c48b296[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
Test succeeded! Differences to referenceOutput within tolerance.
travis_time:end:1c48b296:start=1579866790708766762,finish=1579866918853351245,duration=128144584483,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:06b92ad2[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:06b92ad2:start=1579866922934654775,finish=1579866924275064311,duration=1340409536,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:128c3151[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/641298093/log.txt)