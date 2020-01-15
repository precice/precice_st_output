## Status: Failure 
Build: [1457](https://travis-ci.org/precice/systemtests/builds/637357729) 

Job: [1457.19](https://travis-ci.org/precice/systemtests/jobs/637357750) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:184b7414[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:184b7414:start=1579089925050479129,finish=1579089925499008241,duration=448529112,event=configure[0Ktravis_time:start:1016c4dc[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1016c4dc:start=1579089925503821166,finish=1579089933647990431,duration=8144169265,event=configure[0Ktravis_time:start:0ea44c53[0Ktravis_fold:start:services[0Ktravis_time:start:1830c1c8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1830c1c8:start=1579089933669959481,finish=1579089933682661445,duration=12701964,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1830c1c8:start=1579089933669959481,finish=1579089936688529658,duration=3018570177,event=services[0Ktravis_time:start:05612f34[0Ktravis_time:end:05612f34:start=1579089936692662475,finish=1579089936695111374,duration=2448899,event=fix_ps4[0Ktravis_time:start:1a314b06[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1f4af1e0[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1f4af1e0:start=1579089936703191502,finish=1579089941939645438,duration=5236453936,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:1f4af1e0:start=1579089936703191502,finish=1579089942837872780,duration=6134681278,event=checkout[0Ktravis_time:start:18f664f3[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:18f664f3:start=1579089942842373368,finish=1579089942851360616,duration=8987248,event=env[0Ktravis_time:start:0c2a66e0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0c2a66e0:start=1579089942855089413,finish=1579089942860272602,duration=5183189,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:05ef9026[0K$ python system_testing.py -s of-of
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
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BAll adapters finished!
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
travis_time:end:05ef9026:start=1579089943137595378,finish=1579090008064681589,duration=64927086211,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:00d01670[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/637357750/log.txt)