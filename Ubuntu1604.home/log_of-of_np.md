## Status: Failure 
Build: [1397](https://travis-ci.org/precice/systemtests/builds/633228536) 

Job: [1397.25](https://travis-ci.org/precice/systemtests/jobs/633228561) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:start:0cd3bd0e[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0cd3bd0e:start=1578310389925588618,finish=1578310390279771288,duration=354182670,event=configure[0Ktravis_time:start:01dba1b4[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:01dba1b4:start=1578310390284432691,finish=1578310398471534543,duration=8187101852,event=configure[0Ktravis_time:start:19d517e2[0Ktravis_fold:start:services[0Ktravis_time:start:093e55b8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:093e55b8:start=1578310398497274757,finish=1578310398509192614,duration=11917857,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:093e55b8:start=1578310398497274757,finish=1578310401514538745,duration=3017263988,event=services[0Ktravis_time:start:03f346b6[0Ktravis_time:end:03f346b6:start=1578310401518626619,finish=1578310401521490230,duration=2863611,event=fix_ps4[0Ktravis_time:start:152e0c74[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0049f900[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0049f900:start=1578310401528300869,finish=1578310406848133576,duration=5319832707,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:0049f900:start=1578310401528300869,finish=1578310407601141596,duration=6072840727,event=checkout[0Ktravis_time:start:0c7f1007[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0c7f1007:start=1578310407605675006,finish=1578310407614626547,duration=8951541,event=env[0Ktravis_time:start:01e4838e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01e4838e:start=1578310407619241470,finish=1578310407624661555,duration=5420085,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0234c648[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0553b4dbaaf216bec05bfdfc2c695b344d3c95e49c15ab1baa33c7fe8ebdc93f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []
travis_time:end:0234c648:start=1578310407899351062,finish=1578310472703011893,duration=64803660831,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:09c016fe[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/633228561/log.txt)