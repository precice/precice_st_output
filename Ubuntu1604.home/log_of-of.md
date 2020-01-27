## Status: Passing 
Build: [1521](https://travis-ci.org/precice/systemtests/builds/642317432) 

Job: [1521.19](https://travis-ci.org/precice/systemtests/jobs/642317451) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:19943fc1[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:19943fc1:start=1580125216189910423,finish=1580125216709790424,duration=519880001,event=configure[0Ktravis_time:start:06b2f470[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:06b2f470:start=1580125216713932256,finish=1580125225427846777,duration=8713914521,event=configure[0Ktravis_time:start:2bd4fa62[0Ktravis_fold:start:services[0Ktravis_time:start:05dd289a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:05dd289a:start=1580125225450083482,finish=1580125225462649529,duration=12566047,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:05dd289a:start=1580125225450083482,finish=1580125228467492253,duration=3017408771,event=services[0Ktravis_time:start:16553e60[0Ktravis_time:end:16553e60:start=1580125228472136414,finish=1580125228474623328,duration=2486914,event=fix_ps4[0Ktravis_time:start:204b5716[0K
travis_fold:start:git.checkout[0Ktravis_time:start:121ae79a[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:121ae79a:start=1580125228483450058,finish=1580125233737322691,duration=5253872633,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf feb7379d4291423a8ea6ec40728f855e8268130b
travis_fold:end:git.checkout[0K
travis_time:end:121ae79a:start=1580125228483450058,finish=1580125234392088131,duration=5908638073,event=checkout[0Ktravis_time:start:15bfea04[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:15bfea04:start=1580125234396653240,finish=1580125234407335933,duration=10682693,event=env[0Ktravis_time:start:150c7b90[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:150c7b90:start=1580125234412262384,finish=1580125234417847782,duration=5585398,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:08804b92[0K$ python system_testing.py -s of-of
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
Digest: sha256:9c34ba59ce7def418b30f072762f1af26bfd19cd52917002802465bb132e1e52
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:08804b92:start=1580125234707554807,finish=1580125359981138096,duration=125273583289,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:05db9683[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:05db9683:start=1580125364049720503,finish=1580125365471201494,duration=1421480991,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2caf4e6c[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/642317451/log.txt)