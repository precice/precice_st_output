## Status: Passing 
Build: [1520](https://travis-ci.org/precice/systemtests/builds/641980444) 

Job: [1520.19](https://travis-ci.org/precice/systemtests/jobs/641980463) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:154be670[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:154be670:start=1580039800557224670,finish=1580039801633618255,duration=1076393585,event=configure[0Ktravis_time:start:28921ba5[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:28921ba5:start=1580039801637962620,finish=1580039809841298519,duration=8203335899,event=configure[0Ktravis_time:start:151a1534[0Ktravis_fold:start:services[0Ktravis_time:start:08d0b8bf[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08d0b8bf:start=1580039809863718230,finish=1580039809877126886,duration=13408656,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08d0b8bf:start=1580039809863718230,finish=1580039812883633231,duration=3019915001,event=services[0Ktravis_time:start:0572ce4c[0Ktravis_time:end:0572ce4c:start=1580039812888193932,finish=1580039812890829637,duration=2635705,event=fix_ps4[0Ktravis_time:start:39869e02[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0b4e57c0[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0b4e57c0:start=1580039812899814347,finish=1580039818310215374,duration=5410401027,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf feb7379d4291423a8ea6ec40728f855e8268130b
travis_fold:end:git.checkout[0K
travis_time:end:0b4e57c0:start=1580039812899814347,finish=1580039818561869276,duration=5662054929,event=checkout[0Ktravis_time:start:226fd808[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:226fd808:start=1580039818566011641,finish=1580039818575781887,duration=9770246,event=env[0Ktravis_time:start:249d3138[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:249d3138:start=1580039818580128413,finish=1580039818594071899,duration=13943486,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1d4c6b86[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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

Creating network "testcomposeofof_default" with the default driver
Creating network "testcomposeofof_[secure]comm" with the default driver
Creating volume "testcomposeofof_output" with default driver
Creating volume "testcomposeofof_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:a75d4bfff6af02cc2b843e66159d1d66a2273e84224bce5a82273feb54bfeca0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:1d4c6b86:start=1580039818859662632,finish=1580039948767050161,duration=129907387529,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:09cdacc5[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:09cdacc5:start=1580039952817466035,finish=1580039954140473974,duration=1323007939,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:07312491[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/641980463/log.txt)