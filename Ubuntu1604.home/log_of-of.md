 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581212684) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:019b17cb:start=1567693548112056081,finish=1567693548178139003,duration=66082922,event=resolvconf[0Ktravis_time:start:076c066d[0Ktravis_time:end:076c066d:start=1567693548183103483,finish=1567693548282250193,duration=99146710,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2199f450[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2199f450:start=1567693548366530942,finish=1567693549859189148,duration=1492658206,event=configure[0Ktravis_time:start:22576a18[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:22576a18:start=1567693549864359653,finish=1567693559305582042,duration=9441222389,event=configure[0Ktravis_time:start:04a35fa4[0Ktravis_fold:start:services[0Ktravis_time:start:02080aa0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:02080aa0:start=1567693559330333926,finish=1567693559343697073,duration=13363147,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:02080aa0:start=1567693559330333926,finish=1567693562349539452,duration=3019205526,event=services[0Ktravis_time:start:056b60c2[0Ktravis_time:end:056b60c2:start=1567693562354453886,finish=1567693562357050238,duration=2596352,event=fix_ps4[0Ktravis_time:start:3389a0de[0K
travis_fold:start:git.checkout[0Ktravis_time:start:065417cd[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:065417cd:start=1567693562366010685,finish=1567693568430030358,duration=6064019673,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0f6a1351[0K$ git fetch origin +refs/pull/91/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/91/merge -> FETCH_HEAD
travis_time:end:0f6a1351:start=1567693568435590034,finish=1567693568871293142,duration=435703108,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0f6a1351:start=1567693568435590034,finish=1567693569249357689,duration=813767655,event=checkout[0Ktravis_time:start:00581178[0K
[33;1mSetting environment variables from repository settings[0m
$ export GH_TOKEN=[secure]
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]

travis_time:end:00581178:start=1567693569253856636,finish=1567693569268005667,duration=14149031,event=env[0Ktravis_time:start:0b4cf0ba[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0b4cf0ba:start=1567693569273052658,finish=1567693569278888730,duration=5836072,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2d1a63a5[0K$ python system_testing.py -s of-of
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
Digest: sha256:be8e37fe141c3aebfdaea18d27b3ffa9ef98fadcfc17a3167f5925fc0e3dc0ea
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2d1a63a5:start=1567693569631757757,finish=1567693691409773521,duration=121778015764,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:01390d90[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581212695/log.txt)