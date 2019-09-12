 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584268195) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/69fcf48ce4a0) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/32fdbbbc7d35f2395ee394dc8113d538b3dd86a1...04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
## Last 100 lines of the job log at the moment of push...
```
 travis_time:end:040455c9:start=1568315685046226842,finish=1568315696506732971,duration=11460506129,event=configure[0Ktravis_time:start:0408ad40[0Ktravis_fold:start:services[0Ktravis_time:start:173f247f[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:173f247f:start=1568315696551390944,finish=1568315696566998190,duration=15607246,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:173f247f:start=1568315696551390944,finish=1568315699575478264,duration=3024087320,event=services[0Ktravis_time:start:22e7b678[0Ktravis_time:end:22e7b678:start=1568315699579758639,finish=1568315699582876023,duration=3117384,event=fix_ps4[0Ktravis_time:start:358bb60c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1a8a4c36[0K$ git clone --depth=50 --branch=num_tol https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1a8a4c36:start=1568315699604530731,finish=1568315710084239396,duration=10479708665,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 69fcf48ce4a0330d082bf8f5ffc2565d1b4a3e6d
travis_fold:end:git.checkout[0K
travis_time:end:1a8a4c36:start=1568315699604530731,finish=1568315710152137109,duration=10547606378,event=checkout[0Ktravis_time:start:03713303[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:03713303:start=1568315710161567604,finish=1568315710173739017,duration=12171413,event=env[0Ktravis_time:start:0a26690c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0a26690c:start=1568315710186486015,finish=1568315710192411774,duration=5925759,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0911f04a[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:193947ff1e590caf032a10505ac90c1462765a1ecdf4025f9099eb1f318998a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
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
travis_time:end:0911f04a:start=1568315710607275802,finish=1568315837840751214,duration=127233475412,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:037fa294[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584268215/log.txt)