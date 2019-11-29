## Status: Passing 
Build: [1219](https://travis-ci.org/precice/systemtests/builds/618379002) 

Job: [1219.14](https://travis-ci.org/precice/systemtests/jobs/618379016) 

Triggered by: [push](https://github.com/precice/systemtests/compare/7189d2841f25...dca772ad009c) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:309dd508:start=1575008621510600654,finish=1575008621583888662,duration=73288008,event=resolvconf[0Ktravis_time:start:08adb5f3[0Ktravis_time:end:08adb5f3:start=1575008621589569692,finish=1575008621698185665,duration=108615973,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:03684647[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:03684647:start=1575008621789745084,finish=1575008622119258370,duration=329513286,event=configure[0Ktravis_time:start:1852fecb[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1852fecb:start=1575008622125013140,finish=1575008638592329422,duration=16467316282,event=configure[0Ktravis_time:start:117c7094[0Ktravis_fold:start:services[0Ktravis_time:start:14fb340c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:14fb340c:start=1575008638622264452,finish=1575008638639184784,duration=16920332,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:14fb340c:start=1575008638622264452,finish=1575008641646386941,duration=3024122489,event=services[0Ktravis_time:start:1b51c770[0Ktravis_time:end:1b51c770:start=1575008641651447981,finish=1575008641654819388,duration=3371407,event=fix_ps4[0Ktravis_time:start:08fc7986[0K
travis_fold:start:git.checkout[0Ktravis_time:start:061da600[0K$ git clone --depth=50 --branch=improve_python_bindings_dependencies https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:061da600:start=1575008641664549093,finish=1575008648300871039,duration=6636321946,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf dca772ad009ca1028472bdd5db7cb9b148ba7d64
travis_fold:end:git.checkout[0K
travis_time:end:061da600:start=1575008641664549093,finish=1575008648550862634,duration=6886313541,event=checkout[0Ktravis_time:start:00b0f950[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00b0f950:start=1575008648557066624,finish=1575008648569650474,duration=12583850,event=env[0Ktravis_time:start:00fdbdc0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00fdbdc0:start=1575008648576403015,finish=1575008648584043314,duration=7640299,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:133d95b4[0K$ python system_testing.py -s of-of
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
Digest: sha256:00845e1ffe0b07f596edaae901de7b42ce3f89a08f557de115aa9e47ae051d3f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[1A[2KCreating tutorial-data ... [32mdone[0m[1B[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:133d95b4:start=1575008649015063793,finish=1575008777003713958,duration=127988650165,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1c98116a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1c98116a:start=1575008782090934366,finish=1575008783879766695,duration=1788832329,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:031736c4[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/618379016/log.txt)