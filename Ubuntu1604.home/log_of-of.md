 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598783692) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/108) 
## Last 100 lines of the job log at the moment of push...
```
 resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0c494a96:start=1571252831104483505,finish=1571252831176337369,duration=71853864,event=resolvconf[0Ktravis_time:start:2eba56ef[0Ktravis_time:end:2eba56ef:start=1571252831181416978,finish=1571252831288017102,duration=106600124,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:15aeff30[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:15aeff30:start=1571252831377367673,finish=1571252832012440444,duration=635072771,event=configure[0Ktravis_time:start:0b353efc[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0b353efc:start=1571252832019244270,finish=1571252841772166857,duration=9752922587,event=configure[0Ktravis_time:start:00eb3506[0Ktravis_fold:start:services[0Ktravis_time:start:0649b930[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0649b930:start=1571252841799762739,finish=1571252841815417521,duration=15654782,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0649b930:start=1571252841799762739,finish=1571252844820939407,duration=3021176668,event=services[0Ktravis_time:start:082417f3[0Ktravis_time:end:082417f3:start=1571252844825255089,finish=1571252844828084839,duration=2829750,event=fix_ps4[0Ktravis_time:start:02bd3ed4[0K
travis_fold:start:git.checkout[0Ktravis_time:start:041d0f0c[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:041d0f0c:start=1571252844836342825,finish=1571252851152649827,duration=6316307002,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:03fee744[0K$ git fetch origin +refs/pull/108/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/108/merge -> FETCH_HEAD
travis_time:end:03fee744:start=1571252851157501672,finish=1571252851599194534,duration=441692862,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:03fee744:start=1571252851157501672,finish=1571252851706710122,duration=549208450,event=checkout[0Ktravis_time:start:1b57cb02[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1b57cb02:start=1571252851711459735,finish=1571252851722810592,duration=11350857,event=env[0Ktravis_time:start:03ec49ee[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03ec49ee:start=1571252851727087835,finish=1571252851740659479,duration=13571644,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:22a8a311[0K$ python system_testing.py -s of-of
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
Digest: sha256:14c454f027edb7ee09d95f55057266e2975bf722f078ec6dd2abb625be3db80e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:22a8a311:start=1571252852073181423,finish=1571252974473104055,duration=122399922632,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1d3ef978[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598783706/log.txt)