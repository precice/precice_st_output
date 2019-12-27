## Status: Failure 
Build: [1365](https://travis-ci.org/precice/systemtests/builds/629956799) 

Job: [1365.23](https://travis-ci.org/precice/systemtests/jobs/629956822) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:0040849a:start=1577446122210952268,finish=1577446122917738122,duration=706785854,event=configure[0Ktravis_time:start:1f46db06[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1f46db06:start=1577446122924922232,finish=1577446130765180754,duration=7840258522,event=configure[0Ktravis_time:start:0d2e87e2[0Ktravis_fold:start:services[0Ktravis_time:start:0fea655e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0fea655e:start=1577446130788222983,finish=1577446130801335462,duration=13112479,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0fea655e:start=1577446130788222983,finish=1577446133807160334,duration=3018937351,event=services[0Ktravis_time:start:323d4480[0Ktravis_time:end:323d4480:start=1577446133810588110,finish=1577446133812841387,duration=2253277,event=fix_ps4[0Ktravis_time:start:1819f5c0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1c7bafec[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1c7bafec:start=1577446133819253727,finish=1577446139096972033,duration=5277718306,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 968fe698268820917cf52199d2d3dcbaaf61fbaf
travis_fold:end:git.checkout[0K
travis_time:end:1c7bafec:start=1577446133819253727,finish=1577446139178132087,duration=5358878360,event=checkout[0Ktravis_time:start:0abfb800[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0abfb800:start=1577446139181617375,finish=1577446139188588562,duration=6971187,event=env[0Ktravis_time:start:2425a37c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2425a37c:start=1577446139193420903,finish=1577446139198940479,duration=5519576,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:041a348d[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:3c6e3ba82fe5460988633d4112cd6d2708134239b7ab0401cc4137b49011923f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:041a348d:start=1577446139469697630,finish=1577446266357597944,duration=126887900314,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:058b6bd6[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/629956822/log.txt)