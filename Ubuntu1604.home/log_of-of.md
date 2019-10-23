## Status: Passing 
Build: [1006](https://travis-ci.org/precice/systemtests/builds/602019179) 

Job: [1006.14](https://travis-ci.org/precice/systemtests/jobs/602019193) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4ea43c307afb...2f3949cca1ae) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:2e35927c:start=1571867734865162780,finish=1571867734871469915,duration=6307135,event=show_system_info[0Ktravis_time:start:13425220[0Ktravis_time:end:13425220:start=1571867734874769720,finish=1571867734899745051,duration=24975331,event=rm_riak_source[0Ktravis_time:start:18c9801f[0Ktravis_time:end:18c9801f:start=1571867734903161455,finish=1571867734913162509,duration=10001054,event=fix_rwky_redis[0Ktravis_time:start:2f1516be[0Ktravis_time:end:2f1516be:start=1571867734916826431,finish=1571867735353114309,duration=436287878,event=wait_for_network[0Ktravis_time:start:10ac58b8[0Ktravis_time:end:10ac58b8:start=1571867735358445042,finish=1571867736320829468,duration=962384426,event=update_apt_keys[0Ktravis_time:start:024ad781[0Ktravis_time:end:024ad781:start=1571867736325895699,finish=1571867737429323193,duration=1103427494,event=fix_hhvm_source[0Ktravis_time:start:01b34767[0Ktravis_time:end:01b34767:start=1571867737434078670,finish=1571867737445035750,duration=10957080,event=update_mongo_arch[0Ktravis_time:start:025c7b94[0Ktravis_time:end:025c7b94:start=1571867737450051022,finish=1571867737493783212,duration=43732190,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1a153546[0Ktravis_time:end:1a153546:start=1571867737498537190,finish=1571867737501376468,duration=2839278,event=update_glibc[0Ktravis_time:start:0b523549[0Ktravis_time:end:0b523549:start=1571867737505864652,finish=1571867737516365019,duration=10500367,event=clean_up_path[0Ktravis_time:start:2bf53477[0Ktravis_time:end:2bf53477:start=1571867737521089140,finish=1571867737531312900,duration=10223760,event=fix_resolv_conf[0Ktravis_time:start:046963d4[0Ktravis_time:end:046963d4:start=1571867737535580011,finish=1571867737547052799,duration=11472788,event=fix_etc_hosts[0Ktravis_time:start:00a85ac6[0Ktravis_time:end:00a85ac6:start=1571867737553191751,finish=1571867737562927439,duration=9735688,event=fix_mvn_settings_xml[0Ktravis_time:start:12f87ea0[0Ktravis_time:end:12f87ea0:start=1571867737567485137,finish=1571867737578625890,duration=11140753,event=no_ipv6_localhost[0Ktravis_time:start:168d5df2[0Ktravis_time:end:168d5df2:start=1571867737583735416,finish=1571867737586541523,duration=2806107,event=fix_etc_mavenrc[0Ktravis_time:start:079b79a4[0Ktravis_time:end:079b79a4:start=1571867737591026018,finish=1571867737595316282,duration=4290264,event=fix_wwdr_certificate[0Ktravis_time:start:052f551c[0Ktravis_time:end:052f551c:start=1571867737599663887,finish=1571867737630476890,duration=30813003,event=put_localhost_first[0Ktravis_time:start:00bed331[0Ktravis_time:end:00bed331:start=1571867737636339059,finish=1571867737640936884,duration=4597825,event=home_paths[0Ktravis_time:start:02047368[0Ktravis_time:end:02047368:start=1571867737646029168,finish=1571867737659439326,duration=13410158,event=disable_initramfs[0Ktravis_time:start:1c301c51[0Ktravis_time:end:1c301c51:start=1571867737664912664,finish=1571867737990837626,duration=325924962,event=disable_ssh_roaming[0Ktravis_time:start:2a7df187[0Ktravis_time:end:2a7df187:start=1571867737996142611,finish=1571867738000368790,duration=4226179,event=debug_tools[0Ktravis_time:start:123f52b6[0Ktravis_time:end:123f52b6:start=1571867738005878590,finish=1571867738011132288,duration=5253698,event=uninstall_oclint[0Ktravis_time:start:023f05e6[0Ktravis_time:end:023f05e6:start=1571867738016256336,finish=1571867738020415742,duration=4159406,event=rvm_use[0Ktravis_time:start:06b5736a[0Ktravis_time:end:06b5736a:start=1571867738027470803,finish=1571867738037416945,duration=9946142,event=rm_etc_boto_cfg[0Ktravis_time:start:360ef012[0Ktravis_time:end:360ef012:start=1571867738044003639,finish=1571867738047830855,duration=3827216,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0a42f0aa[0Ktravis_time:end:0a42f0aa:start=1571867738053365426,finish=1571867738112290378,duration=58924952,event=enable_i386[0Ktravis_time:start:005b29e4[0Ktravis_time:end:005b29e4:start=1571867738118721053,finish=1571867738124108020,duration=5386967,event=update_rubygems[0Ktravis_time:start:146252d3[0Ktravis_time:end:146252d3:start=1571867738129084014,finish=1571867739180499956,duration=1051415942,event=ensure_path_components[0Ktravis_time:start:2efbaa30[0Ktravis_time:end:2efbaa30:start=1571867739185595170,finish=1571867739188566484,duration=2971314,event=redefine_curl[0Ktravis_time:start:1907f454[0Ktravis_time:end:1907f454:start=1571867739192550179,finish=1571867739246332439,duration=53782260,event=nonblock_pipe[0Ktravis_time:start:322835e8[0Ktravis_time:end:322835e8:start=1571867739251529039,finish=1571867742298328725,duration=3046799686,event=apt_get_update[0Ktravis_time:start:34b44a95[0Ktravis_time:end:34b44a95:start=1571867742304048943,finish=1571867742307334599,duration=3285656,event=deprecate_xcode_64[0Ktravis_time:start:30c218c0[0Ktravis_time:end:30c218c0:start=1571867742311716072,finish=1571867747157727266,duration=4846011194,event=update_heroku[0Ktravis_time:start:2cffd71d[0Ktravis_time:end:2cffd71d:start=1571867747163321222,finish=1571867747166404703,duration=3083481,event=shell_session_update[0Ktravis_time:start:0e728430[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3964
travis_fold:end:docker_mtu[0Ktravis_time:end:0e728430:start=1571867747170782193,finish=1571867748375066538,duration=1204284345,event=set_docker_mtu[0Ktravis_time:start:0dd6bb24[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0dd6bb24:start=1571867748380604348,finish=1571867748451128503,duration=70524155,event=resolvconf[0Ktravis_time:start:0df41390[0Ktravis_time:end:0df41390:start=1571867748456144743,finish=1571867748565400735,duration=109255992,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:207269cc[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:207269cc:start=1571867748654386292,finish=1571867749004381976,duration=349995684,event=configure[0Ktravis_time:start:175b7ae0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:175b7ae0:start=1571867749009641498,finish=1571867762142095021,duration=13132453523,event=configure[0Ktravis_time:start:0f5522e8[0Ktravis_fold:start:services[0Ktravis_time:start:128fabdb[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:128fabdb:start=1571867762168908924,finish=1571867762183712140,duration=14803216,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:128fabdb:start=1571867762168908924,finish=1571867765189904150,duration=3020995226,event=services[0Ktravis_time:start:28d5fb3c[0Ktravis_time:end:28d5fb3c:start=1571867765194987264,finish=1571867765198152315,duration=3165051,event=fix_ps4[0Ktravis_time:start:04d9b008[0K
travis_fold:start:git.checkout[0Ktravis_time:start:22cdfec0[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:22cdfec0:start=1571867765208037452,finish=1571867771473733881,duration=6265696429,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2f3949cca1ae3a51d8f298d1e4286edbe06c066c
travis_fold:end:git.checkout[0K
travis_time:end:22cdfec0:start=1571867765208037452,finish=1571867771866728796,duration=6658691344,event=checkout[0Ktravis_time:start:03ec3c64[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:03ec3c64:start=1571867771873387205,finish=1571867771886715438,duration=13328233,event=env[0Ktravis_time:start:28a2c8a8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:28a2c8a8:start=1571867771894993541,finish=1571867771902486842,duration=7493301,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:026e84f5[0K$ python system_testing.py -s of-of
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
Digest: sha256:71e59392c3eda1815295b9b43606e5b8ae997da323ad190311b227bd2bde769e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:026e84f5:start=1571867772275921725,finish=1571867893754808632,duration=121478886907,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:226ebd8f[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602019193/log.txt)