## Status: Passing 
Build: [1613](https://travis-ci.org/precice/systemtests/builds/647273995) 

Job: [1613.18](https://travis-ci.org/precice/systemtests/jobs/647274013) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:12957978:start=1581077975209073585,finish=1581077982677920052,duration=7468846467,event=checkout[0Ktravis_time:start:13031388[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:13031388:start=1581077982684160911,finish=1581077982695093137,duration=10932226,event=env[0Ktravis_time:start:0121ed69[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0121ed69:start=1581077982699054208,finish=1581077982709004035,duration=9949827,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:11eb70c4[0K$ python system_testing.py -s of-of
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
Digest: sha256:b1617965f93659491aadc821ca91d521d2ba707714389c1cc7ddab49496a39bd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:11eb70c4:start=1581077982995472045,finish=1581078109854683052,duration=126859211007,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0155b302[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0155b302:start=1581078114105500348,finish=1581078115578844750,duration=1473344402,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1749da8e[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/647274013/log.txt)