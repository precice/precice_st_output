 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581225671) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/91) 
## Last 100 lines of the job log at the moment of push...
```
 resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:311e3da0:start=1567692495055847221,finish=1567692495121138444,duration=65291223,event=resolvconf[0Ktravis_time:start:0482081c[0Ktravis_time:end:0482081c:start=1567692495125119620,finish=1567692495226256425,duration=101136805,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:183584fa[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:183584fa:start=1567692495310251445,finish=1567692495645617666,duration=335366221,event=configure[0Ktravis_time:start:1df0a244[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1df0a244:start=1567692495650507194,finish=1567692505914302548,duration=10263795354,event=configure[0Ktravis_time:start:07017f00[0Ktravis_fold:start:services[0Ktravis_time:start:03bc5420[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:03bc5420:start=1567692505939842182,finish=1567692505954095308,duration=14253126,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03bc5420:start=1567692505939842182,finish=1567692508960918697,duration=3021076515,event=services[0Ktravis_time:start:0d221c00[0Ktravis_time:end:0d221c00:start=1567692508967501729,finish=1567692508971526488,duration=4024759,event=fix_ps4[0Ktravis_time:start:01147f94[0K
travis_fold:start:git.checkout[0Ktravis_time:start:02e5b7d8[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:02e5b7d8:start=1567692508985958310,finish=1567692515040901663,duration=6054943353,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:1508f001[0K$ git fetch origin +refs/pull/91/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/91/merge -> FETCH_HEAD
travis_time:end:1508f001:start=1567692515046592213,finish=1567692515477400271,duration=430808058,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:1508f001:start=1567692515046592213,finish=1567692515513376269,duration=466784056,event=checkout[0Ktravis_time:start:03e3b0e0[0K
[33;1mSetting environment variables from repository settings[0m
$ export GH_TOKEN=[secure]
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]

travis_time:end:03e3b0e0:start=1567692515517541434,finish=1567692515528201588,duration=10660154,event=env[0Ktravis_time:start:07f0f28e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:07f0f28e:start=1567692515532662709,finish=1567692515538708106,duration=6045397,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:014a5c40[0K$ python system_testing.py -s of-of
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
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:014a5c40:start=1567692515881549840,finish=1567692637144927632,duration=121263377792,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:059cb9fc[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581225682/log.txt)