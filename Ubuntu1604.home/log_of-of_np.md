## Status: Passing 
Build: [1124](https://travis-ci.org/precice/systemtests/builds/614316725) 

Job: [1124.24](https://travis-ci.org/precice/systemtests/jobs/614316759) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:017f13ec[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:017f13ec:start=1574218583888330157,finish=1574218584140298589,duration=251968432,event=configure[0Ktravis_time:start:24cc4368[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:24cc4368:start=1574218584146283068,finish=1574218597926840099,duration=13780557031,event=configure[0Ktravis_time:start:0ecc84fa[0Ktravis_fold:start:services[0Ktravis_time:start:1631c796[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1631c796:start=1574218597957306802,finish=1574218597974559953,duration=17253151,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1631c796:start=1574218597957306802,finish=1574218600982119099,duration=3024812297,event=services[0Ktravis_time:start:08610bd6[0Ktravis_time:end:08610bd6:start=1574218600988339148,finish=1574218600992964477,duration=4625329,event=fix_ps4[0Ktravis_time:start:1518ad30[0K
travis_fold:start:git.checkout[0Ktravis_time:start:120c25b8[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:120c25b8:start=1574218601005393881,finish=1574218607665728084,duration=6660334203,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:120c25b8:start=1574218601005393881,finish=1574218608210051989,duration=7204658108,event=checkout[0Ktravis_time:start:1cf96f2d[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1cf96f2d:start=1574218608216416762,finish=1574218608237176774,duration=20760012,event=env[0Ktravis_time:start:00985a58[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00985a58:start=1574218608243442904,finish=1574218608251386658,duration=7943754,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2fbedad0[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:55b877d050d3079ce1d91749c20487d3ba43580cf274dfd15feb866543dd2a4e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2fbedad0:start=1574218608646744001,finish=1574218729894939921,duration=121248195920,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07fdac3b[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07fdac3b:start=1574218734965942878,finish=1574218736665405483,duration=1699462605,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0bc0e43a[0KCloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/614316759/log.txt)