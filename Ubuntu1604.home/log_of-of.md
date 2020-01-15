## Status: Failure 
Build: [1458](https://travis-ci.org/precice/systemtests/builds/637381788) 

Job: [1458.15](https://travis-ci.org/precice/systemtests/jobs/637381803) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/128) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
start: Job is already running: docker
travis_time:end:03d0aa5e:start=1579091517033872013,finish=1579091517048224996,duration=14352983,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03d0aa5e:start=1579091517033872013,finish=1579091520053561131,duration=3019689118,event=services[0Ktravis_time:start:073d5f3c[0Ktravis_time:end:073d5f3c:start=1579091520057859492,finish=1579091520060510858,duration=2651366,event=fix_ps4[0Ktravis_time:start:00607a86[0K
travis_fold:start:git.checkout[0Ktravis_time:start:154c2b14[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:154c2b14:start=1579091520068408929,finish=1579091525632309060,duration=5563900131,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:1d9fe298[0K$ git fetch origin +refs/pull/128/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/128/merge -> FETCH_HEAD
travis_time:end:1d9fe298:start=1579091525637052041,finish=1579091526123380796,duration=486328755,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:1d9fe298:start=1579091525637052041,finish=1579091526677587368,duration=1040535327,event=checkout[0Ktravis_time:start:3993afd7[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:3993afd7:start=1579091526682689860,finish=1579091526693342637,duration=10652777,event=env[0Ktravis_time:start:33aae7a8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:33aae7a8:start=1579091526700704364,finish=1579091526706706092,duration=6001728,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2f362ad9[0K$ python system_testing.py -s of-of
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e6bac11a4a05f0568bb262f30003dda508046e3d50a0c699bbf3c472a41668e6
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:2f362ad9:start=1579091527011664413,finish=1579091592202098196,duration=65190433783,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:06e4ec94[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637381803/log.txt)