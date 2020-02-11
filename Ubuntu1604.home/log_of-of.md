## Status: Failure 
Build: [1666](https://travis-ci.org/precice/systemtests/builds/648938191) 

Job: [1666.10](https://travis-ci.org/precice/systemtests/jobs/648938201) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/174) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:start:git.checkout[0Ktravis_time:start:0034cd72[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0034cd72:start=1581432857933364842,finish=1581432864512356343,duration=6578991501,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:07feec39[0K$ git fetch origin +refs/pull/174/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/174/merge -> FETCH_HEAD
travis_time:end:07feec39:start=1581432864517397425,finish=1581432865056142115,duration=538744690,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:07feec39:start=1581432864517397425,finish=1581432865470028237,duration=952630812,event=checkout[0Ktravis_time:start:0ee56cd1[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0ee56cd1:start=1581432865474147791,finish=1581432865483353321,duration=9205530,event=env[0Ktravis_time:start:00f43e50[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00f43e50:start=1581432865488685345,finish=1581432865493613408,duration=4928063,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1c4b7000[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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

Creating network "testcomposeofof_default" with the default driver
Creating network "testcomposeofof_[secure]comm" with the default driver
Creating volume "testcomposeofof_output" with default driver
Creating volume "testcomposeofof_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f4a35c80e3584b3e11b7da5bf50b88da768fe5fe965b027645946b3c174412f9
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output/Fluid: [secure]-adapter-config.yml
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput/Fluid/system: [secure]Dict
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output/Solid: [secure]-adapter-config.yml
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput/Solid/system: [secure]Dict
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : ['U', 'T', 'phi', 'U', 'T', 'phi', 'U', 'T', 'phi', 'U', 'T', 'phi', 'U', 'T', 'phi', 'gradTy', 'gradTx', 'gradTy', 'gradTx', 'gradTy', 'gradTx', 'T', 'gradTy', 'gradTx', 'gradTy', 'gradTx']
Files only in reference (left): ['[secure]Dict', '[secure]Dict']
Files only in output(right)   : ['[secure]-adapter-config.yml', '[secure]-adapter-config.yml']
travis_time:end:1c4b7000:start=1581432865773795935,finish=1581432995498014881,duration=129724218946,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:216dc398[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648938201/log.txt)