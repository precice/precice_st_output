## Status: Failure 
Build: [1385](https://travis-ci.org/precice/systemtests/builds/631818063) 

Job: [1385.19](https://travis-ci.org/precice/systemtests/jobs/631818084) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:0588866d[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0588866d:start=1577964489642857261,finish=1577964490315295433,duration=672438172,event=configure[0Ktravis_time:start:06aba7bc[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:06aba7bc:start=1577964490324322323,finish=1577964499109588724,duration=8785266401,event=configure[0Ktravis_time:start:14a08682[0Ktravis_fold:start:services[0Ktravis_time:start:15e4601c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:15e4601c:start=1577964499132789655,finish=1577964499146223093,duration=13433438,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:15e4601c:start=1577964499132789655,finish=1577964502151742162,duration=3018952507,event=services[0Ktravis_time:start:044085cc[0Ktravis_time:end:044085cc:start=1577964502155002048,finish=1577964502157497316,duration=2495268,event=fix_ps4[0Ktravis_time:start:0277ff18[0K
travis_fold:start:git.checkout[0Ktravis_time:start:056c881b[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:056c881b:start=1577964502164516223,finish=1577964507550232328,duration=5385716105,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:056c881b:start=1577964502164516223,finish=1577964508021075756,duration=5856559533,event=checkout[0Ktravis_time:start:138a1890[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:138a1890:start=1577964508025554821,finish=1577964508035692873,duration=10138052,event=env[0Ktravis_time:start:1035ed24[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1035ed24:start=1577964508040668319,finish=1577964508046033445,duration=5365126,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:324b4096[0K$ python system_testing.py -s of-of
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
Digest: sha256:21f8da290e7a6a6a227e00d549b69b19410de111f78d6d5f9b6e6844dd506776
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid', 'Solid']
Files only in output(right)   : []
travis_time:end:324b4096:start=1577964508336391048,finish=1577964575959806941,duration=67623415893,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:00edad24[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/631818084/log.txt)