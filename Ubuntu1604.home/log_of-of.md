## Status: Passing 
Build: [1100](https://travis-ci.org/precice/systemtests/builds/612774159) 

Job: [1100.14](https://travis-ci.org/precice/systemtests/jobs/612774173) 

Triggered by: [push](https://github.com/precice/systemtests/compare/772d64248024...9566b8a963d8) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:03e44ccb:start=1573907979833877205,finish=1573907990084642474,duration=10250765269,event=configure[0Ktravis_time:start:090b8a03[0Ktravis_fold:start:services[0Ktravis_time:start:07a63a90[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:07a63a90:start=1573907990112591584,finish=1573907990128705710,duration=16114126,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:07a63a90:start=1573907990112591584,finish=1573907993134378723,duration=3021787139,event=services[0Ktravis_time:start:0853bef4[0Ktravis_time:end:0853bef4:start=1573907993138882621,finish=1573907993141644015,duration=2761394,event=fix_ps4[0Ktravis_time:start:147b7550[0K
travis_fold:start:git.checkout[0Ktravis_time:start:071fd5a7[0K$ git clone --depth=50 --branch=EderK-iss118 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:071fd5a7:start=1573907993150704661,finish=1573907999323281185,duration=6172576524,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 9566b8a963d82b008bbbd4c9812f70c6878c97a9
travis_fold:end:git.checkout[0K
travis_time:end:071fd5a7:start=1573907993150704661,finish=1573907999602101714,duration=6451397053,event=checkout[0Ktravis_time:start:02cc2464[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:02cc2464:start=1573907999607688558,finish=1573907999621075843,duration=13387285,event=env[0Ktravis_time:start:0029a2ac[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0029a2ac:start=1573907999626087263,finish=1573907999632127473,duration=6040210,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:21464778[0K$ python system_testing.py -s of-of
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
Digest: sha256:716de21b0369d6022c063dd3d1be49cb1424694a2ef78c353e3a2532fd4077da
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:21464778:start=1573907999985367544,finish=1573908120999624397,duration=121014256853,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:157f7832[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/612774173/log.txt)