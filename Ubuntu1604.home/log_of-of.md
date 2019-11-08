## Status: Passing 
Build: [1062](https://travis-ci.org/precice/systemtests/builds/609194087) 

Job: [1062.14](https://travis-ci.org/precice/systemtests/jobs/609194103) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f02cef114a79...c96d99257303) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:0faa8db8:start=1573216483049162069,finish=1573216483116734749,duration=67572680,event=resolvconf[0Ktravis_time:start:0c03d993[0Ktravis_time:end:0c03d993:start=1573216483120712694,finish=1573216483224030054,duration=103317360,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0090e3d0[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0090e3d0:start=1573216483308863345,finish=1573216483717402124,duration=408538779,event=configure[0Ktravis_time:start:1b4828ec[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1b4828ec:start=1573216483722741437,finish=1573216493965838561,duration=10243097124,event=configure[0Ktravis_time:start:00301e94[0Ktravis_fold:start:services[0Ktravis_time:start:11822d08[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:11822d08:start=1573216493992886264,finish=1573216494008056128,duration=15169864,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:11822d08:start=1573216493992886264,finish=1573216497014369306,duration=3021483042,event=services[0Ktravis_time:start:06fb9846[0Ktravis_time:end:06fb9846:start=1573216497019276548,finish=1573216497022556971,duration=3280423,event=fix_ps4[0Ktravis_time:start:07216bb2[0K
travis_fold:start:git.checkout[0Ktravis_time:start:284c65be[0K$ git clone --depth=50 --branch=EderK-fix-after_success https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:284c65be:start=1573216497031416826,finish=1573216503237903694,duration=6206486868,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf c96d992573036eb70390aaa4136d2494a6aaa9b6
travis_fold:end:git.checkout[0K
travis_time:end:284c65be:start=1573216497031416826,finish=1573216503447039154,duration=6415622328,event=checkout[0Ktravis_time:start:0ae7a3b0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0ae7a3b0:start=1573216503452413344,finish=1573216503464342684,duration=11929340,event=env[0Ktravis_time:start:33cf9b29[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:33cf9b29:start=1573216503468911804,finish=1573216503474812060,duration=5900256,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00471f0e[0K$ python system_testing.py -s of-of
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
Digest: sha256:378ef6ba2ce11e83a8e56ce1b601e6708559dc7791caea54395add87de1e187d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:00471f0e:start=1573216503819051418,finish=1573216624659360511,duration=120840309093,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0818de3d[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0818de3d:start=1573216629231688224,finish=1573216630879903762,duration=1648215538,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:116f72ec[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/609194103/log.txt)