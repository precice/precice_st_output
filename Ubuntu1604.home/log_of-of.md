## Status: Passing 
Build: [1055](https://travis-ci.org/precice/systemtests/builds/606615476) 

Job: [1055.18](https://travis-ci.org/precice/systemtests/jobs/606615494) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:0f5c8c50:start=1572748831775367629,finish=1572748831785179251,duration=9811622,event=show_system_info[0Ktravis_time:start:11b811ca[0Ktravis_time:end:11b811ca:start=1572748831789711904,finish=1572748831821874038,duration=32162134,event=rm_riak_source[0Ktravis_time:start:2ee547e2[0Ktravis_time:end:2ee547e2:start=1572748831826076458,finish=1572748831834479609,duration=8403151,event=fix_rwky_redis[0Ktravis_time:start:1c55a204[0Ktravis_time:end:1c55a204:start=1572748831838938049,finish=1572748832200313410,duration=361375361,event=wait_for_network[0Ktravis_time:start:02be9987[0Ktravis_time:end:02be9987:start=1572748832207305670,finish=1572748833844995525,duration=1637689855,event=update_apt_keys[0Ktravis_time:start:07f2cb6c[0Ktravis_time:end:07f2cb6c:start=1572748833851971270,finish=1572748834979585100,duration=1127613830,event=fix_hhvm_source[0Ktravis_time:start:0c3448ef[0Ktravis_time:end:0c3448ef:start=1572748834986154261,finish=1572748834999157392,duration=13003131,event=update_mongo_arch[0Ktravis_time:start:2029b231[0Ktravis_time:end:2029b231:start=1572748835004883932,finish=1572748835056926510,duration=52042578,event=fix_sudo_enabled_trusty[0Ktravis_time:start:000b539e[0Ktravis_time:end:000b539e:start=1572748835062529304,finish=1572748835066973846,duration=4444542,event=update_glibc[0Ktravis_time:start:0482497b[0Ktravis_time:end:0482497b:start=1572748835072508201,finish=1572748835084568584,duration=12060383,event=clean_up_path[0Ktravis_time:start:08831807[0Ktravis_time:end:08831807:start=1572748835090665888,finish=1572748835102135602,duration=11469714,event=fix_resolv_conf[0Ktravis_time:start:03591d0a[0Ktravis_time:end:03591d0a:start=1572748835110787803,finish=1572748835123893502,duration=13105699,event=fix_etc_hosts[0Ktravis_time:start:1434048b[0Ktravis_time:end:1434048b:start=1572748835129593798,finish=1572748835142195960,duration=12602162,event=fix_mvn_settings_xml[0Ktravis_time:start:087ca98c[0Ktravis_time:end:087ca98c:start=1572748835147261997,finish=1572748835162053226,duration=14791229,event=no_ipv6_localhost[0Ktravis_time:start:0974d562[0Ktravis_time:end:0974d562:start=1572748835167694164,finish=1572748835171617326,duration=3923162,event=fix_etc_mavenrc[0Ktravis_time:start:00e757d8[0Ktravis_time:end:00e757d8:start=1572748835178294232,finish=1572748835183126438,duration=4832206,event=fix_wwdr_certificate[0Ktravis_time:start:0cc7edcb[0Ktravis_time:end:0cc7edcb:start=1572748835188124126,finish=1572748835224582832,duration=36458706,event=put_localhost_first[0Ktravis_time:start:1217e35c[0Ktravis_time:end:1217e35c:start=1572748835230814844,finish=1572748835237085449,duration=6270605,event=home_paths[0Ktravis_time:start:015231c0[0Ktravis_time:end:015231c0:start=1572748835242534163,finish=1572748835260648572,duration=18114409,event=disable_initramfs[0Ktravis_time:start:08158a2b[0Ktravis_time:end:08158a2b:start=1572748835266798664,finish=1572748835636763551,duration=369964887,event=disable_ssh_roaming[0Ktravis_time:start:000e5a2e[0Ktravis_time:end:000e5a2e:start=1572748835641221714,finish=1572748835644544080,duration=3322366,event=debug_tools[0Ktravis_time:start:094a3744[0Ktravis_time:end:094a3744:start=1572748835648929818,finish=1572748835653252253,duration=4322435,event=uninstall_oclint[0Ktravis_time:start:1b5fd9f0[0Ktravis_time:end:1b5fd9f0:start=1572748835659799746,finish=1572748835664181619,duration=4381873,event=rvm_use[0Ktravis_time:start:10ec0b19[0Ktravis_time:end:10ec0b19:start=1572748835668655362,finish=1572748835682599848,duration=13944486,event=rm_etc_boto_cfg[0Ktravis_time:start:110b5f8a[0Ktravis_time:end:110b5f8a:start=1572748835687710838,finish=1572748835691309250,duration=3598412,event=rm_oraclejdk8_symlink[0Ktravis_time:start:018ffdf0[0Ktravis_time:end:018ffdf0:start=1572748835695949524,finish=1572748835763002435,duration=67052911,event=enable_i386[0Ktravis_time:start:014bedb7[0Ktravis_time:end:014bedb7:start=1572748835768969660,finish=1572748835775352842,duration=6383182,event=update_rubygems[0Ktravis_time:start:0b9991b3[0Ktravis_time:end:0b9991b3:start=1572748835779873082,finish=1572748836966334154,duration=1186461072,event=ensure_path_components[0Ktravis_time:start:2d6c4572[0Ktravis_time:end:2d6c4572:start=1572748836971947926,finish=1572748836975439069,duration=3491143,event=redefine_curl[0Ktravis_time:start:0037d263[0Ktravis_time:end:0037d263:start=1572748836980542688,finish=1572748837037973165,duration=57430477,event=nonblock_pipe[0Ktravis_time:start:01660c61[0Ktravis_time:end:01660c61:start=1572748837043917300,finish=1572748840124283104,duration=3080365804,event=apt_get_update[0Ktravis_time:start:08c0eb00[0Ktravis_time:end:08c0eb00:start=1572748840130620318,finish=1572748840135838304,duration=5217986,event=deprecate_xcode_64[0Ktravis_time:start:16957a94[0Ktravis_time:end:16957a94:start=1572748840141101157,finish=1572748845194987254,duration=5053886097,event=update_heroku[0Ktravis_time:start:345533d4[0Ktravis_time:end:345533d4:start=1572748845201261439,finish=1572748845206576711,duration=5315272,event=shell_session_update[0Ktravis_time:start:00bd01ff[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3856
travis_fold:end:docker_mtu[0Ktravis_time:end:00bd01ff:start=1572748845211682968,finish=1572748846425996094,duration=1214313126,event=set_docker_mtu[0Ktravis_time:start:379d9838[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:379d9838:start=1572748846431361277,finish=1572748846519008383,duration=87647106,event=resolvconf[0Ktravis_time:start:16ec89a0[0Ktravis_time:end:16ec89a0:start=1572748846525412557,finish=1572748846647648110,duration=122235553,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:026fb149[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:026fb149:start=1572748846745415527,finish=1572748847009419763,duration=264004236,event=configure[0Ktravis_time:start:16e5045c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:16e5045c:start=1572748847016233410,finish=1572748862475445759,duration=15459212349,event=configure[0Ktravis_time:start:1428a177[0Ktravis_fold:start:services[0Ktravis_time:start:00330fea[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:00330fea:start=1572748862503411317,finish=1572748862521147510,duration=17736193,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:00330fea:start=1572748862503411317,finish=1572748865527211418,duration=3023800101,event=services[0Ktravis_time:start:17976fb2[0Ktravis_time:end:17976fb2:start=1572748865532844628,finish=1572748865537731440,duration=4886812,event=fix_ps4[0Ktravis_time:start:00f7721d[0K
travis_fold:start:git.checkout[0Ktravis_time:start:09ca3a13[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:09ca3a13:start=1572748865547740315,finish=1572748871955367023,duration=6407626708,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:09ca3a13:start=1572748865547740315,finish=1572748872807105801,duration=7259365486,event=checkout[0Ktravis_time:start:0434f178[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0434f178:start=1572748872813620785,finish=1572748872826761302,duration=13140517,event=env[0Ktravis_time:start:00ccd77d[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00ccd77d:start=1572748872832716615,finish=1572748872843336720,duration=10620105,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:37388616[0K$ python system_testing.py -s of-of
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e1ede29dae04cac520d17c81301087123c03455b9bb7251d4b5da0388fc8b489
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!

```
[
Full job log](https://api.travis-ci.org/v3/job/606615494/log.txt)