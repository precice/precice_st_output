 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581646369) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/bde2eea33c21...5cd0caba623e) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/22c7a2563db646c589aa4b12b230bdf3564ccc67...3d2a931687e7c7c6c60f2b7fc8f2e6272fed4eb0)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
## Last 100 lines of the job log at the moment of push...
```
 travis_time:start:0892ed75[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0892ed75:start=1567774062996343626,finish=1567774063843934283,duration=847590657,event=configure[0Ktravis_time:start:03f8c3b1[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:03f8c3b1:start=1567774063848292067,finish=1567774076782202538,duration=12933910471,event=configure[0Ktravis_time:start:0d150f83[0Ktravis_fold:start:services[0Ktravis_time:start:03bd5eb7[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:03bd5eb7:start=1567774076810917812,finish=1567774076827216213,duration=16298401,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03bd5eb7:start=1567774076810917812,finish=1567774079833494967,duration=3022577155,event=services[0Ktravis_time:start:060c1c6c[0Ktravis_time:end:060c1c6c:start=1567774079837689473,finish=1567774079840141240,duration=2451767,event=fix_ps4[0Ktravis_time:start:2b15ab00[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1ff154d6[0K$ git clone --depth=50 --branch=job_info https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1ff154d6:start=1567774079847871673,finish=1567774086887336978,duration=7039465305,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 5cd0caba623e27b53a7ab528109efc0b427a8603
travis_fold:end:git.checkout[0K
travis_time:end:1ff154d6:start=1567774079847871673,finish=1567774087677470188,duration=7829598515,event=checkout[0Ktravis_time:start:01ec3768[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01ec3768:start=1567774087683056691,finish=1567774087694910016,duration=11853325,event=env[0Ktravis_time:start:167e7188[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:167e7188:start=1567774087701524456,finish=1567774087708107405,duration=6582949,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0136a0e7[0K$ python system_testing.py -s of-of_np
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
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:0136a0e7:start=1567774088120164274,finish=1567774149886913334,duration=61766749060,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:022d4702[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581646386/log.txt)