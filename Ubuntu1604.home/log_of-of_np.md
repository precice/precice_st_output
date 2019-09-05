 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581225637) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/1ae3635d9a98...bde2eea33c21) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/ebff6c50c3f73041f2c55084665fd592a8641f61...d36bb995194a3f0a3fb55ab93560cf230f23bc1c)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
## Last 100 lines of the job log at the moment of push...
```
 travis_time:end:0a613c4c:start=1567693473546762302,finish=1567693474216546300,duration=669783998,event=configure[0Ktravis_time:start:0168936c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0168936c:start=1567693474222246258,finish=1567693483434458781,duration=9212212523,event=configure[0Ktravis_time:start:07a3cf4c[0Ktravis_fold:start:services[0Ktravis_time:start:010f78b3[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:010f78b3:start=1567693483459787483,finish=1567693483473456709,duration=13669226,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:010f78b3:start=1567693483459787483,finish=1567693486478129195,duration=3018341712,event=services[0Ktravis_time:start:0f7611b4[0Ktravis_time:end:0f7611b4:start=1567693486482507645,finish=1567693486485007917,duration=2500272,event=fix_ps4[0Ktravis_time:start:233c9400[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00f705cc[0K$ git clone --depth=50 --branch=job_info https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00f705cc:start=1567693486493775969,finish=1567693492042809287,duration=5549033318,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf bde2eea33c21d9d713711ee25d7ca4173fdaa604
travis_fold:end:git.checkout[0K
travis_time:end:00f705cc:start=1567693486493775969,finish=1567693492083158812,duration=5589382843,event=checkout[0Ktravis_time:start:0be6c2e4[0K
[33;1mSetting environment variables from repository settings[0m
$ export GH_TOKEN=[secure]
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]

travis_time:end:0be6c2e4:start=1567693492087780123,finish=1567693492100255074,duration=12474951,event=env[0Ktravis_time:start:01d9ea70[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01d9ea70:start=1567693492104852467,finish=1567693492110521405,duration=5668938,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0ef222be[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:be8e37fe141c3aebfdaea18d27b3ffa9ef98fadcfc17a3167f5925fc0e3dc0ea
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid', 'Solid']
Files only in output(right)   : []
travis_time:end:0ef222be:start=1567693492440147211,finish=1567693613109327369,duration=120669180158,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:2c9ee234[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581225654/log.txt)