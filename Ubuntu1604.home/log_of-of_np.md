 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598783692) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/108) 
## Last 100 lines of the job log at the moment of push...
```
 resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:043f7c40:start=1571253059751081546,finish=1571253059824881141,duration=73799595,event=resolvconf[0Ktravis_time:start:221d3270[0Ktravis_time:end:221d3270:start=1571253059830557846,finish=1571253059950569126,duration=120011280,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:01ec9ebe[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:01ec9ebe:start=1571253060040167101,finish=1571253060431310342,duration=391143241,event=configure[0Ktravis_time:start:011eb95a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:011eb95a:start=1571253060438395401,finish=1571253072748191166,duration=12309795765,event=configure[0Ktravis_time:start:04fb9e34[0Ktravis_fold:start:services[0Ktravis_time:start:35a6a058[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:35a6a058:start=1571253072774457283,finish=1571253072789436343,duration=14979060,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:35a6a058:start=1571253072774457283,finish=1571253075795025768,duration=3020568485,event=services[0Ktravis_time:start:0080ac87[0Ktravis_time:end:0080ac87:start=1571253075800382468,finish=1571253075803524578,duration=3142110,event=fix_ps4[0Ktravis_time:start:0f4f7e72[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1b651669[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1b651669:start=1571253075813009033,finish=1571253082151930152,duration=6338921119,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:00021588[0K$ git fetch origin +refs/pull/108/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/108/merge -> FETCH_HEAD
travis_time:end:00021588:start=1571253082157069625,finish=1571253082603214693,duration=446145068,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:00021588:start=1571253082157069625,finish=1571253082713405420,duration=556335795,event=checkout[0Ktravis_time:start:32f7cc6d[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:32f7cc6d:start=1571253082718603762,finish=1571253082731359276,duration=12755514,event=env[0Ktravis_time:start:34dc7965[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:34dc7965:start=1571253082739315629,finish=1571253082746258816,duration=6943187,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0ee3e000[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:14c454f027edb7ee09d95f55057266e2975bf722f078ec6dd2abb625be3db80e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0ee3e000:start=1571253083115846720,finish=1571253204774938435,duration=121659091715,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:014efc80[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598783712/log.txt)