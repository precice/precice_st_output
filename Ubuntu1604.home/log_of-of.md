## Status: Passing 
Build: [1042](https://travis-ci.org/precice/systemtests/builds/603824297) 

Job: [1042.14](https://travis-ci.org/precice/systemtests/jobs/603824311) 

Triggered by: [push](https://github.com/precice/systemtests/compare/9921a3e9e3f7...e3f7960c948e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:system_info[0K
travis_time:end:22e1a988:start=1572260469211736801,finish=1572260469217826728,duration=6089927,event=show_system_info[0Ktravis_time:start:0e856ba0[0Ktravis_time:end:0e856ba0:start=1572260469220904071,finish=1572260469244742233,duration=23838162,event=rm_riak_source[0Ktravis_time:start:1f2e89b0[0Ktravis_time:end:1f2e89b0:start=1572260469248374167,finish=1572260469255833602,duration=7459435,event=fix_rwky_redis[0Ktravis_time:start:0b7b2104[0Ktravis_time:end:0b7b2104:start=1572260469260412413,finish=1572260469687994225,duration=427581812,event=wait_for_network[0Ktravis_time:start:03507f2a[0Ktravis_time:end:03507f2a:start=1572260469694882403,finish=1572260471283382645,duration=1588500242,event=update_apt_keys[0Ktravis_time:start:35049e8c[0Ktravis_time:end:35049e8c:start=1572260471287900497,finish=1572260472339533887,duration=1051633390,event=fix_hhvm_source[0Ktravis_time:start:2a8be965[0Ktravis_time:end:2a8be965:start=1572260472345244777,finish=1572260472355626305,duration=10381528,event=update_mongo_arch[0Ktravis_time:start:1b074d4e[0Ktravis_time:end:1b074d4e:start=1572260472360221158,finish=1572260472403269148,duration=43047990,event=fix_sudo_enabled_trusty[0Ktravis_time:start:39ad7b7c[0Ktravis_time:end:39ad7b7c:start=1572260472407987562,finish=1572260472410961246,duration=2973684,event=update_glibc[0Ktravis_time:start:027a5128[0Ktravis_time:end:027a5128:start=1572260472416314464,finish=1572260472425363656,duration=9049192,event=clean_up_path[0Ktravis_time:start:0e9230a7[0Ktravis_time:end:0e9230a7:start=1572260472431918340,finish=1572260472440700671,duration=8782331,event=fix_resolv_conf[0Ktravis_time:start:080038ec[0Ktravis_time:end:080038ec:start=1572260472445319482,finish=1572260472457765388,duration=12445906,event=fix_etc_hosts[0Ktravis_time:start:034c4b52[0Ktravis_time:end:034c4b52:start=1572260472462518040,finish=1572260472473200967,duration=10682927,event=fix_mvn_settings_xml[0Ktravis_time:start:0b960860[0Ktravis_time:end:0b960860:start=1572260472479271098,finish=1572260472490398105,duration=11127007,event=no_ipv6_localhost[0Ktravis_time:start:07ea1454[0Ktravis_time:end:07ea1454:start=1572260472496770610,finish=1572260472500805906,duration=4035296,event=fix_etc_mavenrc[0Ktravis_time:start:22894d7c[0Ktravis_time:end:22894d7c:start=1572260472506075904,finish=1572260472510159194,duration=4083290,event=fix_wwdr_certificate[0Ktravis_time:start:10de0d7c[0Ktravis_time:end:10de0d7c:start=1572260472515387532,finish=1572260472545270816,duration=29883284,event=put_localhost_first[0Ktravis_time:start:07181193[0Ktravis_time:end:07181193:start=1572260472551087172,finish=1572260472555477658,duration=4390486,event=home_paths[0Ktravis_time:start:0b95e8a0[0Ktravis_time:end:0b95e8a0:start=1572260472560133192,finish=1572260472575617825,duration=15484633,event=disable_initramfs[0Ktravis_time:start:0783135c[0Ktravis_time:end:0783135c:start=1572260472580631583,finish=1572260472879588073,duration=298956490,event=disable_ssh_roaming[0Ktravis_time:start:37345ef0[0Ktravis_time:end:37345ef0:start=1572260472884297847,finish=1572260472887240424,duration=2942577,event=debug_tools[0Ktravis_time:start:28fdf688[0Ktravis_time:end:28fdf688:start=1572260472891713530,finish=1572260472895330004,duration=3616474,event=uninstall_oclint[0Ktravis_time:start:0e430279[0Ktravis_time:end:0e430279:start=1572260472900572160,finish=1572260472904295130,duration=3722970,event=rvm_use[0Ktravis_time:start:003ab3cc[0Ktravis_time:end:003ab3cc:start=1572260472908674715,finish=1572260472917429715,duration=8755000,event=rm_etc_boto_cfg[0Ktravis_time:start:06329dfc[0Ktravis_time:end:06329dfc:start=1572260472923796976,finish=1572260472926953490,duration=3156514,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0578c994[0Ktravis_time:end:0578c994:start=1572260472932318337,finish=1572260472991367256,duration=59048919,event=enable_i386[0Ktravis_time:start:10a60a3c[0Ktravis_time:end:10a60a3c:start=1572260472995992455,finish=1572260473001189919,duration=5197464,event=update_rubygems[0Ktravis_time:start:292b4e42[0Ktravis_time:end:292b4e42:start=1572260473007806831,finish=1572260474057807018,duration=1050000187,event=ensure_path_components[0Ktravis_time:start:09588b9a[0Ktravis_time:end:09588b9a:start=1572260474063516335,finish=1572260474066784709,duration=3268374,event=redefine_curl[0Ktravis_time:start:0bb62d69[0Ktravis_time:end:0bb62d69:start=1572260474071898539,finish=1572260474126394474,duration=54495935,event=nonblock_pipe[0Ktravis_time:start:0581a75d[0Ktravis_time:end:0581a75d:start=1572260474131876751,finish=1572260477180142024,duration=3048265273,event=apt_get_update[0Ktravis_time:start:0d9f62c0[0Ktravis_time:end:0d9f62c0:start=1572260477184802096,finish=1572260477187605402,duration=2803306,event=deprecate_xcode_64[0Ktravis_time:start:196b602a[0Ktravis_time:end:196b602a:start=1572260477191556320,finish=1572260482018948043,duration=4827391723,event=update_heroku[0Ktravis_time:start:05963025[0Ktravis_time:end:05963025:start=1572260482024476734,finish=1572260482027662309,duration=3185575,event=shell_session_update[0Ktravis_time:start:1406d66c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3889
travis_fold:end:docker_mtu[0Ktravis_time:end:1406d66c:start=1572260482032990564,finish=1572260483234451887,duration=1201461323,event=set_docker_mtu[0Ktravis_time:start:04bc6a02[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:04bc6a02:start=1572260483238598074,finish=1572260483308712882,duration=70114808,event=resolvconf[0Ktravis_time:start:1c18a5f5[0Ktravis_time:end:1c18a5f5:start=1572260483312864527,finish=1572260483412962229,duration=100097702,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:03cbf280[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:03cbf280:start=1572260483496921986,finish=1572260484307823024,duration=810901038,event=configure[0Ktravis_time:start:077c7390[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:077c7390:start=1572260484313165866,finish=1572260494509144349,duration=10195978483,event=configure[0Ktravis_time:start:188b423c[0Ktravis_fold:start:services[0Ktravis_time:start:06c3f090[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06c3f090:start=1572260494535129764,finish=1572260494549730907,duration=14601143,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06c3f090:start=1572260494535129764,finish=1572260497554997579,duration=3019867815,event=services[0Ktravis_time:start:1093a430[0Ktravis_time:end:1093a430:start=1572260497559012033,finish=1572260497561833518,duration=2821485,event=fix_ps4[0Ktravis_time:start:0a2102b8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0470b9d6[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0470b9d6:start=1572260497570094717,finish=1572260503840998936,duration=6270904219,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0470b9d6:start=1572260497570094717,finish=1572260504612646930,duration=7042552213,event=checkout[0Ktravis_time:start:00966f34[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00966f34:start=1572260504617553416,finish=1572260504630250851,duration=12697435,event=env[0Ktravis_time:start:01b121f8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01b121f8:start=1572260504635564813,finish=1572260504647811487,duration=12246674,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09532b0a[0K$ python system_testing.py -s of-of
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
Digest: sha256:684f2ebeff45e7dab02a0e37e1963e46f66ae2fb29f2d90334d515b440fbcb54
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:09532b0a:start=1572260505003060802,finish=1572260626021098008,duration=121018037206,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:02d0f7c8[0K$ python push.py -s -t of-of

```
[
Full job log](https://api.travis-ci.org/v3/job/603824311/log.txt)