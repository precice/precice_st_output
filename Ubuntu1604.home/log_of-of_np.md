## Status: Passing 
Build: [1155](https://travis-ci.org/precice/systemtests/builds/617504380) 

Job: [1155.24](https://travis-ci.org/precice/systemtests/jobs/617504404) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:060f5dcd[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:060f5dcd:start=1574823390069016477,finish=1574823391396424513,duration=1327408036,event=configure[0Ktravis_time:start:1b904087[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1b904087:start=1574823391401517443,finish=1574823400526272863,duration=9124755420,event=configure[0Ktravis_time:start:1749ba44[0Ktravis_fold:start:services[0Ktravis_time:start:23e40f8e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:23e40f8e:start=1574823400553245151,finish=1574823400567753555,duration=14508404,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:23e40f8e:start=1574823400553245151,finish=1574823403573000579,duration=3019755428,event=services[0Ktravis_time:start:068333e8[0Ktravis_time:end:068333e8:start=1574823403577915339,finish=1574823403580916477,duration=3001138,event=fix_ps4[0Ktravis_time:start:324c8e38[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0651b7c0[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0651b7c0:start=1574823403590311694,finish=1574823409735295277,duration=6144983583,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:0651b7c0:start=1574823403590311694,finish=1574823410422556410,duration=6832244716,event=checkout[0Ktravis_time:start:0855af1e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0855af1e:start=1574823410428160577,finish=1574823410437221403,duration=9060826,event=env[0Ktravis_time:start:01e97d40[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01e97d40:start=1574823410441680845,finish=1574823410447814308,duration=6133463,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:14205f6c[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:c1b04241d5b9c1e4102b8bd1110c756b0acb05912f874531f62de82e70763643
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:14205f6c:start=1574823410789256477,finish=1574823531364132815,duration=120574876338,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:034213d4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:034213d4:start=1574823535794146168,finish=1574823537404575112,duration=1610428944,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:040dbe30[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/617504404/log.txt)