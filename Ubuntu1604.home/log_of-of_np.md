## Status: Passing 
Build: [1326](https://travis-ci.org/precice/systemtests/builds/627156304) 

Job: [1326.23](https://travis-ci.org/precice/systemtests/jobs/627156327) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:resolvconf[0Ktravis_time:end:002e8dcb:start=1576754825977276517,finish=1576754826033395338,duration=56118821,event=resolvconf[0Ktravis_time:start:17c21049[0Ktravis_time:end:17c21049:start=1576754826038140931,finish=1576754826124509918,duration=86368987,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:08dff2ca[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:08dff2ca:start=1576754826197404645,finish=1576754826609914413,duration=412509768,event=configure[0Ktravis_time:start:03ee85ba[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:03ee85ba:start=1576754826613281812,finish=1576754835410401165,duration=8797119353,event=configure[0Ktravis_time:start:0570f660[0Ktravis_fold:start:services[0Ktravis_time:start:151aaf08[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:151aaf08:start=1576754835432716232,finish=1576754835445822229,duration=13105997,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:151aaf08:start=1576754835432716232,finish=1576754838452036794,duration=3019320562,event=services[0Ktravis_time:start:0292bff4[0Ktravis_time:end:0292bff4:start=1576754838456185157,finish=1576754838459124954,duration=2939797,event=fix_ps4[0Ktravis_time:start:019ce009[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08c86c72[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08c86c72:start=1576754838467590289,finish=1576754843606290961,duration=5138700672,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ff457bed2521c9ab78f7f6e490c7785219151c1e
travis_fold:end:git.checkout[0K
travis_time:end:08c86c72:start=1576754838467590289,finish=1576754844126284315,duration=5658694026,event=checkout[0Ktravis_time:start:109b93c0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:109b93c0:start=1576754844130483776,finish=1576754844139819814,duration=9336038,event=env[0Ktravis_time:start:0e041ba4[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0e041ba4:start=1576754844143538280,finish=1576754844152743796,duration=9205516,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09cc4b40[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:e170680a0f29ae173193b488e58247c07d9f3cc25078730c65388fd17d91b017
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:09cc4b40:start=1576754844434425225,finish=1576754963040241431,duration=118605816206,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:161848a1[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:161848a1:start=1576754967048591759,finish=1576754968463341994,duration=1414750235,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1509eea4[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/627156327/log.txt)