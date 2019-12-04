## Status: Passing 
Build: [1261](https://travis-ci.org/precice/systemtests/builds/620720012) 

Job: [1261.15](https://travis-ci.org/precice/systemtests/jobs/620720027) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f0c87c5da690...4b1d49be8e29) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:12fd56e7:start=1575481565858987003,finish=1575481565910231033,duration=51244030,event=resolvconf[0Ktravis_time:start:0476acf6[0Ktravis_time:end:0476acf6:start=1575481565913932794,finish=1575481565991130974,duration=77198180,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:166c29b8[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:166c29b8:start=1575481566057103023,finish=1575481566538896105,duration=481793082,event=configure[0Ktravis_time:start:01070c7f[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:01070c7f:start=1575481566543450689,finish=1575481574327105078,duration=7783654389,event=configure[0Ktravis_time:start:1506e6ec[0Ktravis_fold:start:services[0Ktravis_time:start:06851e90[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06851e90:start=1575481574348911542,finish=1575481574360693036,duration=11781494,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06851e90:start=1575481574348911542,finish=1575481577365990018,duration=3017078476,event=services[0Ktravis_time:start:17d69137[0Ktravis_time:end:17d69137:start=1575481577370196569,finish=1575481577372511539,duration=2314970,event=fix_ps4[0Ktravis_time:start:13ca3d4c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:15fb46ba[0K$ git clone --depth=50 --branch=nutils-of_ubuntu1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:15fb46ba:start=1575481577379365487,finish=1575481583274243617,duration=5894878130,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4b1d49be8e29960e88a16c23724e94cf14a442db
travis_fold:end:git.checkout[0K
travis_time:end:15fb46ba:start=1575481577379365487,finish=1575481583500370461,duration=6121004974,event=checkout[0Ktravis_time:start:0c3ec1f8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0c3ec1f8:start=1575481583504488909,finish=1575481583517415866,duration=12926957,event=env[0Ktravis_time:start:08f50ef3[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:08f50ef3:start=1575481583521796150,finish=1575481583527015510,duration=5219360,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1f13427c[0K$ python system_testing.py -s of-of
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
Digest: sha256:adb0bdf9d85c4e2e5a8575830f7c1ee523d8d89a96ef8f07ecee9346af7b4ee6
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1f13427c:start=1575481583793144376,finish=1575481708175338498,duration=124382194122,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:038fd406[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:038fd406:start=1575481711708012899,finish=1575481712984041631,duration=1276028732,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:2402ebee[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/620720027/log.txt)