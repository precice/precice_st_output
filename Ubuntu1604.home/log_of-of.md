## Status: Passing 
Build: [1124](https://travis-ci.org/precice/systemtests/builds/614316725) 

Job: [1124.18](https://travis-ci.org/precice/systemtests/jobs/614316750) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:0a8e269e:start=1574218341369610538,finish=1574218341434934143,duration=65323605,event=resolvconf[0Ktravis_time:start:35fd1c28[0Ktravis_time:end:35fd1c28:start=1574218341439670821,finish=1574218341539160244,duration=99489423,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:16e4ffb0[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:16e4ffb0:start=1574218341621453472,finish=1574218341954864330,duration=333410858,event=configure[0Ktravis_time:start:015a5009[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:015a5009:start=1574218341961184233,finish=1574218352691417226,duration=10730232993,event=configure[0Ktravis_time:start:2c7ebe7b[0Ktravis_fold:start:services[0Ktravis_time:start:1f4e712c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1f4e712c:start=1574218352722630464,finish=1574218352739359501,duration=16729037,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1f4e712c:start=1574218352722630464,finish=1574218355746279801,duration=3023649337,event=services[0Ktravis_time:start:315cbc08[0Ktravis_time:end:315cbc08:start=1574218355750863652,finish=1574218355753996089,duration=3132437,event=fix_ps4[0Ktravis_time:start:1652ad08[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0921bcd0[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0921bcd0:start=1574218355763235114,finish=1574218362342533249,duration=6579298135,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:0921bcd0:start=1574218355763235114,finish=1574218362630110318,duration=6866875204,event=checkout[0Ktravis_time:start:08df15b3[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:08df15b3:start=1574218362635266969,finish=1574218362647455649,duration=12188680,event=env[0Ktravis_time:start:086447b2[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:086447b2:start=1574218362655766769,finish=1574218362664007895,duration=8241126,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:112e4ced[0K$ python system_testing.py -s of-of
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
Digest: sha256:55b877d050d3079ce1d91749c20487d3ba43580cf274dfd15feb866543dd2a4e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:112e4ced:start=1574218363057465985,finish=1574218484437596340,duration=121380130355,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:06874e38[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:06874e38:start=1574218489502896870,finish=1574218491391239043
```
[
Full job log](https://api.travis-ci.org/v3/job/614316750/log.txt)