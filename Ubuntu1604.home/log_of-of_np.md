## Status: Failure 
Build: [1441](https://travis-ci.org/precice/systemtests/builds/635916850) 

Job: [1441.8](https://travis-ci.org/precice/systemtests/jobs/635916858) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/152) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:1c993b84:start=1578822060677732094,finish=1578822069897744928,duration=9220012834,event=configure[0Ktravis_time:start:09a7464a[0Ktravis_fold:start:services[0Ktravis_time:start:17af399c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:17af399c:start=1578822069922918652,finish=1578822069936540425,duration=13621773,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:17af399c:start=1578822069922918652,finish=1578822072942547345,duration=3019628693,event=services[0Ktravis_time:start:23745920[0Ktravis_time:end:23745920:start=1578822072946649574,finish=1578822072949594644,duration=2945070,event=fix_ps4[0Ktravis_time:start:03e676e6[0K
travis_fold:start:git.checkout[0Ktravis_time:start:136fa7de[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:136fa7de:start=1578822072957357982,finish=1578822078370507346,duration=5413149364,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0a279e8d[0K$ git fetch origin +refs/pull/152/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/152/merge -> FETCH_HEAD
travis_time:end:0a279e8d:start=1578822078375492959,finish=1578822078799013125,duration=423520166,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0a279e8d:start=1578822078375492959,finish=1578822079103475325,duration=727982366,event=checkout[0Ktravis_time:start:0af1fde4[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0af1fde4:start=1578822079108228703,finish=1578822079119410925,duration=11182222,event=env[0Ktravis_time:start:23b378a6[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:23b378a6:start=1578822079124828383,finish=1578822079134662894,duration=9834511,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:312a37c8[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

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
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:929e20432a5cdeb84eebfe5fee37434ab895549d3aef02d9473f6686f8453835
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BOnly in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid', 'Solid']
Files only in output(right)   : []
travis_time:end:312a37c8:start=1578822079434170624,finish=1578822145521609576,duration=66087438952,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:23ed1b68[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/635916858/log.txt)