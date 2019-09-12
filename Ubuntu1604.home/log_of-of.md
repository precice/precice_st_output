 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584268195) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/69fcf48ce4a0) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
## Last 100 lines of the job log at the moment of push...
```
 travis_time:end:0066d58a:start=1568315252088908210,finish=1568315262266347498,duration=10177439288,event=configure[0Ktravis_time:start:0f393564[0Ktravis_fold:start:services[0Ktravis_time:start:1a37d4a5[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1a37d4a5:start=1568315262293025692,finish=1568315262308233586,duration=15207894,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1a37d4a5:start=1568315262293025692,finish=1568315265313502660,duration=3020476968,event=services[0Ktravis_time:start:08b58036[0Ktravis_time:end:08b58036:start=1568315265318160940,finish=1568315265321336393,duration=3175453,event=fix_ps4[0Ktravis_time:start:030fd380[0K
travis_fold:start:git.checkout[0Ktravis_time:start:16c6edca[0K$ git clone --depth=50 --branch=num_tol https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:16c6edca:start=1568315265330047212,finish=1568315275947076855,duration=10617029643,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 69fcf48ce4a0330d082bf8f5ffc2565d1b4a3e6d
travis_fold:end:git.checkout[0K
travis_time:end:16c6edca:start=1568315265330047212,finish=1568315276845610508,duration=11515563296,event=checkout[0Ktravis_time:start:11fa72e0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:11fa72e0:start=1568315276850834777,finish=1568315276862664716,duration=11829939,event=env[0Ktravis_time:start:13d73b7f[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:13d73b7f:start=1568315276867899075,finish=1568315276874355848,duration=6456773,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:032b8000[0K$ python system_testing.py -s of-of
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:193947ff1e590caf032a10505ac90c1462765a1ecdf4025f9099eb1f318998a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
Traceback (most recent call last):
  File "system_testing.py", line 199, in <module>
    args.force_rebuild, False)
  File "system_testing.py", line 162, in build_run_compare
    run_compose(test, branch, local_[secure], tag, force_rebuild, rm_all)
  File "system_testing.py", line 101, in run_compose
    test_basename in custom_tolerance.keys() else custom_tolerance[test_basename])
AttributeError: 'set' object has no attribute 'keys'
travis_time:end:032b8000:start=1568315277227176526,finish=1568315404517130940,duration=127289954414,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:2adfcf35[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584268209/log.txt)