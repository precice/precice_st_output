## Status: Failure 
Build: [1472](https://travis-ci.org/precice/systemtests/builds/639426908) 

Job: [1472.25](https://travis-ci.org/precice/systemtests/jobs/639426933) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:1a1de5a6[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1a1de5a6:start=1579520581675997620,finish=1579520582221301853,duration=545304233,event=configure[0Ktravis_time:start:0371e6b4[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0371e6b4:start=1579520582225548083,finish=1579520590668405320,duration=8442857237,event=configure[0Ktravis_time:start:0994e75c[0Ktravis_fold:start:services[0Ktravis_time:start:10e10e1f[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:10e10e1f:start=1579520590692818592,finish=1579520590707089531,duration=14270939,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:10e10e1f:start=1579520590692818592,finish=1579520593715458258,duration=3022639666,event=services[0Ktravis_time:start:04470f9b[0Ktravis_time:end:04470f9b:start=1579520593719224877,finish=1579520593721861426,duration=2636549,event=fix_ps4[0Ktravis_time:start:1239d1f6[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0db560fa[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0db560fa:start=1579520593729530385,finish=1579520598992943443,duration=5263413058,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:0db560fa:start=1579520593729530385,finish=1579520599937729365,duration=6208198980,event=checkout[0Ktravis_time:start:0412e84c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0412e84c:start=1579520599942559418,finish=1579520599953584194,duration=11024776,event=env[0Ktravis_time:start:0502c4ac[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0502c4ac:start=1579520599958095707,finish=1579520599964423612,duration=6327905,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00c50f76[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8fa319a89b61bdcbfa28f2f53f935b0401e4112ad1e8c65b0ca09ded9c3b179c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:00c50f76:start=1579520600259596656,finish=1579520655059241469,duration=54799644813,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0f4ab3c6[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/639426933/log.txt)