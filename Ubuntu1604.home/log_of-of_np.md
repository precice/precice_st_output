## Status: Passing 
Build: [1268](https://travis-ci.org/precice/systemtests/builds/621181807) 

Job: [1268.20](https://travis-ci.org/precice/systemtests/jobs/621181829) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ff51dfcb2467...d102fedd8227) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:03eeb1cf:start=1575565361523585245,finish=1575565361596413663,duration=72828418,event=resolvconf[0Ktravis_time:start:0a8f0201[0Ktravis_time:end:0a8f0201:start=1575565361601494481,finish=1575565361700650731,duration=99156250,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0baaaf86[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0baaaf86:start=1575565361788396794,finish=1575565363454001677,duration=1665604883,event=configure[0Ktravis_time:start:14d64d04[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:14d64d04:start=1575565363460267689,finish=1575565373460929589,duration=10000661900,event=configure[0Ktravis_time:start:1dd01228[0Ktravis_fold:start:services[0Ktravis_time:start:1203e988[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1203e988:start=1575565373488400984,finish=1575565373502561166,duration=14160182,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1203e988:start=1575565373488400984,finish=1575565376509819557,duration=3021418573,event=services[0Ktravis_time:start:0252fc14[0Ktravis_time:end:0252fc14:start=1575565376514309054,finish=1575565376517563829,duration=3254775,event=fix_ps4[0Ktravis_time:start:19c6721d[0K
travis_fold:start:git.checkout[0Ktravis_time:start:008dbd78[0K$ git clone --depth=50 --branch=update_to_python_bindings_repo https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:008dbd78:start=1575565376527462405,finish=1575565382728177343,duration=6200714938,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf d102fedd82279f59627da0720ee5b9054a018fdd
travis_fold:end:git.checkout[0K
travis_time:end:008dbd78:start=1575565376527462405,finish=1575565383402198236,duration=6874735831,event=checkout[0Ktravis_time:start:0f5bba1b[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0f5bba1b:start=1575565383408669650,finish=1575565383421700662,duration=13031012,event=env[0Ktravis_time:start:13cfd083[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:13cfd083:start=1575565383427412754,finish=1575565383434122808,duration=6710054,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:010b3866[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:509928ef47f3e2b800f11b0e404af7166a82ae4a4bbbda84fd9701c8da64dadb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:010b3866:start=1575565383786604420,finish=1575565505523856365,duration=121737251945,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04883300[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04883300:start=1575565510083851430,finish=1575565511722498897,duration=1638647467,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:162b5780[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/621181829/log.txt)