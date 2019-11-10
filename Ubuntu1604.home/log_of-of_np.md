## Status: Passing 
Build: [1071](https://travis-ci.org/precice/systemtests/builds/610072373) 

Job: [1071.20](https://travis-ci.org/precice/systemtests/jobs/610072397) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ffab6e4cf6eb...2e77de77c876) 

---
Last 100 lines of the job log at the moment of push:
```
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0bb59f3f[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0bb59f3f:start=1573425601760330257,finish=1573425602079445272,duration=319115015,event=configure[0Ktravis_time:start:239cdaa0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:239cdaa0:start=1573425602085816641,finish=1573425614509397678,duration=12423581037,event=configure[0Ktravis_time:start:2e973ac3[0Ktravis_fold:start:services[0Ktravis_time:start:011d7300[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:011d7300:start=1573425614536255782,finish=1573425614552601500,duration=16345718,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:011d7300:start=1573425614536255782,finish=1573425617558842581,duration=3022586799,event=services[0Ktravis_time:start:00109946[0Ktravis_time:end:00109946:start=1573425617564471119,finish=1573425617567519326,duration=3048207,event=fix_ps4[0Ktravis_time:start:1a067aec[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00c8aeb2[0K$ git clone --depth=50 --branch=EderK-mpich_deploy https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00c8aeb2:start=1573425617577179795,finish=1573425623873128846,duration=6295949051,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2e77de77c876e38e0322a21c82436af686fbdc3b
travis_fold:end:git.checkout[0K
travis_time:end:00c8aeb2:start=1573425617577179795,finish=1573425624724077544,duration=7146897749,event=checkout[0Ktravis_time:start:1743d34a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1743d34a:start=1573425624729367465,finish=1573425624742514507,duration=13147042,event=env[0Ktravis_time:start:0060828e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0060828e:start=1573425624748669839,finish=1573425624756062354,duration=7392515,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1f5e41f5[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:98e7b7fde8bd6b618c7ffe6b7ed9cd847d62e94c024d4c0ecdbd1eb70a3db786
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1f5e41f5:start=1573425625144911448,finish=1573425746304715527,duration=121159804079,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01afad2c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01afad2c:start=1573425751145106253,finish=1573425752869585715,duration=1724479462,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0f7962ca[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/610072397/log.txt)