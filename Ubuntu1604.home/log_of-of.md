## Status: Failure 
Build: [1475](https://travis-ci.org/precice/systemtests/builds/640388632) 

Job: [1475.19](https://travis-ci.org/precice/systemtests/jobs/640388651) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:03b38acf[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:03b38acf:start=1579694274206945157,finish=1579694275189092406,duration=982147249,event=configure[0Ktravis_time:start:0629d630[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0629d630:start=1579694275193334800,finish=1579694283073503912,duration=7880169112,event=configure[0Ktravis_time:start:072c10f8[0Ktravis_fold:start:services[0Ktravis_time:start:1de9cae8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1de9cae8:start=1579694283094766430,finish=1579694283107324226,duration=12557796,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1de9cae8:start=1579694283094766430,finish=1579694286113122413,duration=3018355983,event=services[0Ktravis_time:start:014e6a2e[0Ktravis_time:end:014e6a2e:start=1579694286117037938,finish=1579694286119597644,duration=2559706,event=fix_ps4[0Ktravis_time:start:1eddf466[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0185aff4[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0185aff4:start=1579694286127198978,finish=1579694291326707627,duration=5199508649,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:0185aff4:start=1579694286127198978,finish=1579694291592277644,duration=5465078666,event=checkout[0Ktravis_time:start:0b6e8c4f[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0b6e8c4f:start=1579694291596466820,finish=1579694291607403640,duration=10936820,event=env[0Ktravis_time:start:0a8e4f3b[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0a8e4f3b:start=1579694291612047680,finish=1579694291621343877,duration=9296197,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00320cb2[0K$ python system_testing.py -s of-of
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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f45929668d4ff51c7a03ead8d8c33b26222d106b708047ec43214a00ae3dd34e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
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
travis_time:end:00320cb2:start=1579694291891623714,finish=1579694351397262090,duration=59505638376,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:24aff428[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/640388651/log.txt)