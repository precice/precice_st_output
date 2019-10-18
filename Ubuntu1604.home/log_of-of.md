 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599803615) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 
## Last 100 lines of the job log at the moment of push...
```
 travis_fold:end:docker_mtu[0Ktravis_time:end:0c0efdda:start=1571430353227297215,finish=1571430354424210021,duration=1196912806,event=set_docker_mtu[0Ktravis_time:start:06ac0440[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:06ac0440:start=1571430354429236517,finish=1571430354496997222,duration=67760705,event=resolvconf[0Ktravis_time:start:2a9f1360[0Ktravis_time:end:2a9f1360:start=1571430354501313272,finish=1571430354610328468,duration=109015196,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0adf6c0d[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0adf6c0d:start=1571430354694890309,finish=1571430355214476391,duration=519586082,event=configure[0Ktravis_time:start:040708e6[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:040708e6:start=1571430355220192562,finish=1571430365149065693,duration=9928873131,event=configure[0Ktravis_time:start:09b9cd51[0Ktravis_fold:start:services[0Ktravis_time:start:0a200d0a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0a200d0a:start=1571430365174988000,finish=1571430365189687651,duration=14699651,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0a200d0a:start=1571430365174988000,finish=1571430368194850690,duration=3019862690,event=services[0Ktravis_time:start:046972c0[0Ktravis_time:end:046972c0:start=1571430368199926472,finish=1571430368203202596,duration=3276124,event=fix_ps4[0Ktravis_time:start:0b52bf38[0K
travis_fold:start:git.checkout[0Ktravis_time:start:130ff68c[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:130ff68c:start=1571430368214118859,finish=1571430374502373861,duration=6288255002,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:140ae83e[0K$ git fetch origin +refs/pull/111/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/111/merge -> FETCH_HEAD
travis_time:end:140ae83e:start=1571430374506917489,finish=1571430374943726180,duration=436808691,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:140ae83e:start=1571430374506917489,finish=1571430375358865927,duration=851948438,event=checkout[0Ktravis_time:start:08791ba0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:08791ba0:start=1571430375363567696,finish=1571430375374579634,duration=11011938,event=env[0Ktravis_time:start:0c4cdfca[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0c4cdfca:start=1571430375379570133,finish=1571430375385572647,duration=6002514,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0f20be80[0K$ python system_testing.py -s of-of
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
Digest: sha256:d99ac418afb23059999d46ddcd0bebcb574e2f5230b1652b211366449195c777
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0f20be80:start=1571430375732950114,finish=1571430506276428460,duration=130543478346,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0340b0de[0K$ python push.py -s -t of-of
 ```
[Full job log](https://api.travis-ci.org/v3/job/599803629/log.txt)