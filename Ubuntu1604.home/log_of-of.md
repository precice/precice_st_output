## Status: Passing 
Build: [1484](https://travis-ci.org/precice/systemtests/builds/641298046) 

Job: [1484.19](https://travis-ci.org/precice/systemtests/jobs/641298076) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4c749ac41fec1ac0cc04f8e71fcd731e33705ab1...e37a006c80df4226e1d22b4d0f731f7780eae018) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:0a1bf73d[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0a1bf73d:start=1579866559137099135,finish=1579866559687069143,duration=549970008,event=configure[0Ktravis_time:start:011f1784[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:011f1784:start=1579866559690606559,finish=1579866568293669424,duration=8603062865,event=configure[0Ktravis_time:start:07f6fb93[0Ktravis_fold:start:services[0Ktravis_time:start:18d72e48[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:18d72e48:start=1579866568319273961,finish=1579866568333189961,duration=13916000,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:18d72e48:start=1579866568319273961,finish=1579866571338714823,duration=3019440862,event=services[0Ktravis_time:start:23a75ac2[0Ktravis_time:end:23a75ac2:start=1579866571342730849,finish=1579866571345117742,duration=2386893,event=fix_ps4[0Ktravis_time:start:00258e5d[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1e3cb070[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1e3cb070:start=1579866571353227164,finish=1579866576852023967,duration=5498796803,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e37a006c80df4226e1d22b4d0f731f7780eae018
travis_fold:end:git.checkout[0K
travis_time:end:1e3cb070:start=1579866571353227164,finish=1579866577614483357,duration=6261256193,event=checkout[0Ktravis_time:start:01e8b7d0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01e8b7d0:start=1579866577618602664,finish=1579866577628625671,duration=10023007,event=env[0Ktravis_time:start:06252066[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:06252066:start=1579866577633027295,finish=1579866577640677656,duration=7650361,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:12377991[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

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
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

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
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
Test succeeded! Differences to referenceOutput within tolerance.
travis_time:end:12377991:start=1579866577931819613,finish=1579866705839532692,duration=127907713079,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1ea36098[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1ea36098:start=1579866710279499882,finish=1579866711687940984,duration=1408441102,event=after_success[0Ktravis_travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/641298076/log.txt)