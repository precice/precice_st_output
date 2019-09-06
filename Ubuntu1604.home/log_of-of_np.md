 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581674746) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/e95758ebfe65...18b4f9274e2d) 
## Last 100 lines of the job log at the moment of push...
```
 travis_fold:end:docker_mtu[0Ktravis_time:end:003e3714:start=1567777212134553125,finish=1567777213361616805,duration=1227063680,event=set_docker_mtu[0Ktravis_time:start:102b2eaa[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:102b2eaa:start=1567777213368294850,finish=1567777213450507586,duration=82212736,event=resolvconf[0Ktravis_time:start:0b9bedde[0Ktravis_time:end:0b9bedde:start=1567777213455586243,finish=1567777213589844350,duration=134258107,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:166dcb3c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:166dcb3c:start=1567777213692922502,finish=1567777214150164823,duration=457242321,event=configure[0Ktravis_time:start:0bfc6d60[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0bfc6d60:start=1567777214157777037,finish=1567777229259182945,duration=15101405908,event=configure[0Ktravis_time:start:02c5ab34[0Ktravis_fold:start:services[0Ktravis_time:start:112e7026[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:112e7026:start=1567777229291346143,finish=1567777229309677359,duration=18331216,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:112e7026:start=1567777229291346143,finish=1567777232316466213,duration=3025120070,event=services[0Ktravis_time:start:18438e58[0Ktravis_time:end:18438e58:start=1567777232322652865,finish=1567777232326534602,duration=3881737,event=fix_ps4[0Ktravis_time:start:09a7deec[0K
travis_fold:start:git.checkout[0Ktravis_time:start:23fc618f[0K$ git clone --depth=50 --branch=restructure https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:23fc618f:start=1567777232337802569,finish=1567777238451197134,duration=6113394565,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 18b4f9274e2d110abc8f28a90be8aaaf79c9bbf2
travis_fold:end:git.checkout[0K
travis_time:end:23fc618f:start=1567777232337802569,finish=1567777238828212409,duration=6490409840,event=checkout[0Ktravis_time:start:171d5c24[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:171d5c24:start=1567777238834253548,finish=1567777238846865444,duration=12611896,event=env[0Ktravis_time:start:01fc7fe1[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01fc7fe1:start=1567777238852207288,finish=1567777238859081903,duration=6874615,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:05c87e8d[0K$ python system_testing.py -s of-of_np
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
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
bash: ../compare_results.sh: No such file or directory
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
travis_time:end:05c87e8d:start=1567777239313496749,finish=1567777361118088565,duration=121804591816,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:006dc74f[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581674762/log.txt)