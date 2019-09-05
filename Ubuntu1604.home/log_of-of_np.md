 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581200523) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/a5fe66e3237c...5b9de68efcd3) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/ebff6c50c3f73041f2c55084665fd592a8641f61...d36bb995194a3f0a3fb55ab93560cf230f23bc1c)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
## Last 100 lines of the job log at the moment of push...
```
 travis_time:start:0cdf2b80[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0cdf2b80:start=1567689974804048684,finish=1567689975373705061,duration=569656377,event=configure[0Ktravis_time:start:0a622460[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a622460:start=1567689975379189941,finish=1567689986987345827,duration=11608155886,event=configure[0Ktravis_time:start:1cb0a23b[0Ktravis_fold:start:services[0Ktravis_time:start:0d400115[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0d400115:start=1567689987017538724,finish=1567689987034997053,duration=17458329,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0d400115:start=1567689987017538724,finish=1567689990040829582,duration=3023290858,event=services[0Ktravis_time:start:2503bcf7[0Ktravis_time:end:2503bcf7:start=1567689990045649384,finish=1567689990048777993,duration=3128609,event=fix_ps4[0Ktravis_time:start:27a2b085[0K
travis_fold:start:git.checkout[0Ktravis_time:start:13244f51[0K$ git clone --depth=50 --branch=job_info https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:13244f51:start=1567689990059643911,finish=1567689996230964817,duration=6171320906,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 5b9de68efcd3863839a081e03ba04969b43ad7c5
travis_fold:end:git.checkout[0K
travis_time:end:13244f51:start=1567689990059643911,finish=1567689996425756161,duration=6366112250,event=checkout[0Ktravis_time:start:2b9d7de0[0K
[33;1mSetting environment variables from repository settings[0m
$ export GH_TOKEN=[secure]
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]

travis_time:end:2b9d7de0:start=1567689996431467760,finish=1567689996445251897,duration=13784137,event=env[0Ktravis_time:start:03e3b6c2[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03e3b6c2:start=1567689996451908924,finish=1567689996463263018,duration=11354094,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:003caa1f[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
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
travis_time:end:003caa1f:start=1567689996881248836,finish=1567690119689355716,duration=122808106880,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:19bd753c[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581200542/log.txt)