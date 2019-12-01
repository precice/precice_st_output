## Status: Passing 
Build: [1237](https://travis-ci.org/precice/systemtests/builds/619351844) 

Job: [1237.14](https://travis-ci.org/precice/systemtests/jobs/619351858) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5cd65d21e48f...60b68152f174) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0ca087fb[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0ca087fb:start=1575240933324836837,finish=1575240933823516469,duration=498679632,event=configure[0Ktravis_time:start:082aa930[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:082aa930:start=1575240933830839585,finish=1575240947532333665,duration=13701494080,event=configure[0Ktravis_time:start:1f19e666[0Ktravis_fold:start:services[0Ktravis_time:start:0087e5f8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0087e5f8:start=1575240947560208029,finish=1575240947575998764,duration=15790735,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0087e5f8:start=1575240947560208029,finish=1575240950583665969,duration=3023457940,event=services[0Ktravis_time:start:18814928[0Ktravis_time:end:18814928:start=1575240950588172472,finish=1575240950591276297,duration=3103825,event=fix_ps4[0Ktravis_time:start:003b895c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:018ae120[0K$ git clone --depth=50 --branch=nutils-of_ubuntu1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:018ae120:start=1575240950600394657,finish=1575240956895208160,duration=6294813503,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 60b68152f174e23f2e1ccc72a51e24312ef04254
travis_fold:end:git.checkout[0K
travis_time:end:018ae120:start=1575240950600394657,finish=1575240957735197426,duration=7134802769,event=checkout[0Ktravis_time:start:14bbb4f0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:14bbb4f0:start=1575240957740895446,finish=1575240957754253057,duration=13357611,event=env[0Ktravis_time:start:059cb2b2[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:059cb2b2:start=1575240957760185647,finish=1575240957768466782,duration=8281135,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2eed1eb6[0K$ python system_testing.py -s of-of
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
Digest: sha256:17df4e0778368c5680a67d4fbd568496224f149d9b071688dad9e92221715498
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
travis_time:end:2eed1eb6:start=1575240958165342639,finish=1575241079383481933,duration=121218139294,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:06b7b5b1[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:06b7b5b1:start=1575241084300095713,finish=1575241086089927801,duration=1789832088,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:06542030[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/619351858/log.txt)