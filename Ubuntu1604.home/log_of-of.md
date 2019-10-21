## Status: Passing 
Build: [993](https://travis-ci.org/precice/systemtests/builds/600693901) 

Job: [993.14](https://travis-ci.org/precice/systemtests/jobs/600693916) 

Triggered by: [push](https://github.com/precice/systemtests/compare/a84a139c2665...500cfbb53a97) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:036a2400:start=1571660696681206854,finish=1571660696687557152,duration=6350298,event=show_system_info[0Ktravis_time:start:0cc9b604[0Ktravis_time:end:0cc9b604:start=1571660696692750474,finish=1571660696720693785,duration=27943311,event=rm_riak_source[0Ktravis_time:start:0c399600[0Ktravis_time:end:0c399600:start=1571660696725157940,finish=1571660696731989107,duration=6831167,event=fix_rwky_redis[0Ktravis_time:start:04875de0[0Ktravis_time:end:04875de0:start=1571660696735848501,finish=1571660697173772544,duration=437924043,event=wait_for_network[0Ktravis_time:start:21835fd2[0Ktravis_time:end:21835fd2:start=1571660697178816283,finish=1571660698725261868,duration=1546445585,event=update_apt_keys[0Ktravis_time:start:184acb50[0Ktravis_time:end:184acb50:start=1571660698730686112,finish=1571660699741046280,duration=1010360168,event=fix_hhvm_source[0Ktravis_time:start:06ce8a79[0Ktravis_time:end:06ce8a79:start=1571660699746044316,finish=1571660699756043553,duration=9999237,event=update_mongo_arch[0Ktravis_time:start:12b20b80[0Ktravis_time:end:12b20b80:start=1571660699762179041,finish=1571660699803151701,duration=40972660,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0d92e5af[0Ktravis_time:end:0d92e5af:start=1571660699807689908,finish=1571660699810793038,duration=3103130,event=update_glibc[0Ktravis_time:start:04d52006[0Ktravis_time:end:04d52006:start=1571660699814516502,finish=1571660699825350428,duration=10833926,event=clean_up_path[0Ktravis_time:start:24aecace[0Ktravis_time:end:24aecace:start=1571660699829094057,finish=1571660699838940513,duration=9846456,event=fix_resolv_conf[0Ktravis_time:start:1da28320[0Ktravis_time:end:1da28320:start=1571660699842774414,finish=1571660699854155607,duration=11381193,event=fix_etc_hosts[0Ktravis_time:start:2295ba41[0Ktravis_time:end:2295ba41:start=1571660699858006437,finish=1571660699869750880,duration=11744443,event=fix_mvn_settings_xml[0Ktravis_time:start:0b2820e8[0Ktravis_time:end:0b2820e8:start=1571660699874172446,finish=1571660699884637593,duration=10465147,event=no_ipv6_localhost[0Ktravis_time:start:351568ed[0Ktravis_time:end:351568ed:start=1571660699889897179,finish=1571660699893298272,duration=3401093,event=fix_etc_mavenrc[0Ktravis_time:start:00dda26b[0Ktravis_time:end:00dda26b:start=1571660699898862510,finish=1571660699903751976,duration=4889466,event=fix_wwdr_certificate[0Ktravis_time:start:1ed36290[0Ktravis_time:end:1ed36290:start=1571660699907615753,finish=1571660699936308201,duration=28692448,event=put_localhost_first[0Ktravis_time:start:0c8b82ae[0Ktravis_time:end:0c8b82ae:start=1571660699940666041,finish=1571660699944232724,duration=3566683,event=home_paths[0Ktravis_time:start:00633a36[0Ktravis_time:end:00633a36:start=1571660699948094186,finish=1571660699962089773,duration=13995587,event=disable_initramfs[0Ktravis_time:start:110693dc[0Ktravis_time:end:110693dc:start=1571660699965811205,finish=1571660700276519710,duration=310708505,event=disable_ssh_roaming[0Ktravis_time:start:06a635cc[0Ktravis_time:end:06a635cc:start=1571660700281214185,finish=1571660700283989272,duration=2775087,event=debug_tools[0Ktravis_time:start:0106efb8[0Ktravis_time:end:0106efb8:start=1571660700290825432,finish=1571660700294788925,duration=3963493,event=uninstall_oclint[0Ktravis_time:start:29b700fd[0Ktravis_time:end:29b700fd:start=1571660700300373510,finish=1571660700304075073,duration=3701563,event=rvm_use[0Ktravis_time:start:096859cb[0Ktravis_time:end:096859cb:start=1571660700309117890,finish=1571660700321007179,duration=11889289,event=rm_etc_boto_cfg[0Ktravis_time:start:171fb1cc[0Ktravis_time:end:171fb1cc:start=1571660700324990510,finish=1571660700327885663,duration=2895153,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0139117b[0Ktravis_time:end:0139117b:start=1571660700331935828,finish=1571660700389168688,duration=57232860,event=enable_i386[0Ktravis_time:start:29da8246[0Ktravis_time:end:29da8246:start=1571660700394798156,finish=1571660700400365674,duration=5567518,event=update_rubygems[0Ktravis_time:start:157075e6[0Ktravis_time:end:157075e6:start=1571660700405612485,finish=1571660701428485375,duration=1022872890,event=ensure_path_components[0Ktravis_time:start:08805d80[0Ktravis_time:end:08805d80:start=1571660701433105428,finish=1571660701436918033,duration=3812605,event=redefine_curl[0Ktravis_time:start:0ebd0d9c[0Ktravis_time:end:0ebd0d9c:start=1571660701440688591,finish=1571660701492513477,duration=51824886,event=nonblock_pipe[0Ktravis_time:start:17083524[0Ktravis_time:end:17083524:start=1571660701497285687,finish=1571660704568478169,duration=3071192482,event=apt_get_update[0Ktravis_time:start:2e6b76b4[0Ktravis_time:end:2e6b76b4:start=1571660704573213940,finish=1571660704576163145,duration=2949205,event=deprecate_xcode_64[0Ktravis_time:start:05e75bc0[0Ktravis_time:end:05e75bc0:start=1571660704580821783,finish=1571660709099084015,duration=4518262232,event=update_heroku[0Ktravis_time:start:21e40687[0Ktravis_time:end:21e40687:start=1571660709104465254,finish=1571660709107416725,duration=2951471,event=shell_session_update[0Ktravis_time:start:1e517452[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3967
travis_fold:end:docker_mtu[0Ktravis_time:end:1e517452:start=1571660709112155363,finish=1571660710309507451,duration=1197352088,event=set_docker_mtu[0Ktravis_time:start:1a185bb4[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1a185bb4:start=1571660710313540012,finish=1571660710382209275,duration=68669263,event=resolvconf[0Ktravis_time:start:27542430[0Ktravis_time:end:27542430:start=1571660710387196147,finish=1571660710480278131,duration=93081984,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02458605[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02458605:start=1571660710562018146,finish=1571660711303491823,duration=741473677,event=configure[0Ktravis_time:start:33963042[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:33963042:start=1571660711318705492,finish=1571660721122752584,duration=9804047092,event=configure[0Ktravis_time:start:0d25e7d6[0Ktravis_fold:start:services[0Ktravis_time:start:0b503bf0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0b503bf0:start=1571660721149923994,finish=1571660721165095311,duration=15171317,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0b503bf0:start=1571660721149923994,finish=1571660724170843657,duration=3020919663,event=services[0Ktravis_time:start:016b4990[0Ktravis_time:end:016b4990:start=1571660724175510618,finish=1571660724178425350,duration=2914732,event=fix_ps4[0Ktravis_time:start:012a2426[0K
travis_fold:start:git.checkout[0Ktravis_time:start:12e79e26[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:12e79e26:start=1571660724187970923,finish=1571660730379629525,duration=6191658602,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 500cfbb53a97da6082e1935375882c5b85bda017
travis_fold:end:git.checkout[0K
travis_time:end:12e79e26:start=1571660724187970923,finish=1571660730692693632,duration=6504722709,event=checkout[0Ktravis_time:start:226038e4[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:226038e4:start=1571660730697589598,finish=1571660730707447437,duration=9857839,event=env[0Ktravis_time:start:0493b8e2[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0493b8e2:start=1571660730716227352,finish=1571660730722693414,duration=6466062,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0cf07b6e[0K$ python system_testing.py -s of-of
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
Digest: sha256:04602e91508ea2c3b26d367af5b44dc79b28546a9dc09a0543218d00fc13e338
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0cf07b6e:start=1571660731064642999,finish=1571660852363592203,duration=121298949204,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:03be46cc[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/600693916/log.txt)