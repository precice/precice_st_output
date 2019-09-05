 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581134218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 travis_fold:end:docker_mtu[0Ktravis_time:end:0393d833:start=1567678937626603862,finish=1567678938827926823,duration=1201322961,event=set_docker_mtu[0Ktravis_time:start:03805802[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03805802:start=1567678938833840382,finish=1567678938906348483,duration=72508101,event=resolvconf[0Ktravis_time:start:08c2b531[0Ktravis_time:end:08c2b531:start=1567678938912230891,finish=1567678939024084341,duration=111853450,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02f508c0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02f508c0:start=1567678939110208311,finish=1567678939850966615,duration=740758304,event=configure[0Ktravis_time:start:043ed018[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:043ed018:start=1567678939856199540,finish=1567678950472168155,duration=10615968615,event=configure[0Ktravis_time:start:131cc7d7[0Ktravis_fold:start:services[0Ktravis_time:start:0371690d[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0371690d:start=1567678950497463214,finish=1567678950511773724,duration=14310510,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0371690d:start=1567678950497463214,finish=1567678953516696828,duration=3019233614,event=services[0Ktravis_time:start:1ee1695d[0Ktravis_time:end:1ee1695d:start=1567678953520777226,finish=1567678953523517640,duration=2740414,event=fix_ps4[0Ktravis_time:start:00e7c66a[0K
travis_fold:start:git.checkout[0Ktravis_time:start:03e111a9[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:03e111a9:start=1567678953531329741,finish=1567678959047736990,duration=5516407249,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0b80a8d1[0K$ git fetch origin +refs/pull/91/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/91/merge -> FETCH_HEAD
travis_time:end:0b80a8d1:start=1567678959053197678,finish=1567678959476623055,duration=423425377,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0b80a8d1:start=1567678959053197678,finish=1567678959525385303,duration=472187625,event=checkout[0Ktravis_time:start:042ab558[0K
[33;1mSetting environment variables from repository settings[0m
$ export GH_TOKEN=[secure]
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]

travis_time:end:042ab558:start=1567678959530282275,finish=1567678959541980032,duration=11697757,event=env[0Ktravis_time:start:0b715545[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0b715545:start=1567678959547403277,finish=1567678959553727385,duration=6324108,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1b6d7fe8[0K$ python system_testing.py -s of-of
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1b6d7fe8:start=1567678959915188733,finish=1567679081195324544,duration=121280135811,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:032a37b4[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581134231/log.txt)