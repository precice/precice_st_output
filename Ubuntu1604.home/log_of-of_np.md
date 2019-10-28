## Status: Passing 
Build: [1042](https://travis-ci.org/precice/systemtests/builds/603824297) 

Job: [1042.20](https://travis-ci.org/precice/systemtests/jobs/603824317) 

Triggered by: [push](https://github.com/precice/systemtests/compare/9921a3e9e3f7...e3f7960c948e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:0698c6b3:start=1572261127429863948,finish=1572261127436152275,duration=6288327,event=show_system_info[0Ktravis_time:start:3756f13e[0Ktravis_time:end:3756f13e:start=1572261127439329590,finish=1572261127464584123,duration=25254533,event=rm_riak_source[0Ktravis_time:start:2a267874[0Ktravis_time:end:2a267874:start=1572261127468593853,finish=1572261127476202369,duration=7608516,event=fix_rwky_redis[0Ktravis_time:start:22f1114e[0Ktravis_time:end:22f1114e:start=1572261127483965054,finish=1572261127895575504,duration=411610450,event=wait_for_network[0Ktravis_time:start:1a7aaa91[0Ktravis_time:end:1a7aaa91:start=1572261127900881905,finish=1572261129466527745,duration=1565645840,event=update_apt_keys[0Ktravis_time:start:2a4f37f0[0Ktravis_time:end:2a4f37f0:start=1572261129471701696,finish=1572261130518879417,duration=1047177721,event=fix_hhvm_source[0Ktravis_time:start:0d00d65e[0Ktravis_time:end:0d00d65e:start=1572261130523947063,finish=1572261130534535185,duration=10588122,event=update_mongo_arch[0Ktravis_time:start:088fd25e[0Ktravis_time:end:088fd25e:start=1572261130541322704,finish=1572261130584827753,duration=43505049,event=fix_sudo_enabled_trusty[0Ktravis_time:start:098b3caf[0Ktravis_time:end:098b3caf:start=1572261130589685435,finish=1572261130593191413,duration=3505978,event=update_glibc[0Ktravis_time:start:0a70e04a[0Ktravis_time:end:0a70e04a:start=1572261130598400009,finish=1572261130610028285,duration=11628276,event=clean_up_path[0Ktravis_time:start:0de4f9b5[0Ktravis_time:end:0de4f9b5:start=1572261130614670319,finish=1572261130623064094,duration=8393775,event=fix_resolv_conf[0Ktravis_time:start:237f8019[0Ktravis_time:end:237f8019:start=1572261130628963542,finish=1572261130639072196,duration=10108654,event=fix_etc_hosts[0Ktravis_time:start:0e43691c[0Ktravis_time:end:0e43691c:start=1572261130644014056,finish=1572261130654725279,duration=10711223,event=fix_mvn_settings_xml[0Ktravis_time:start:01a422dd[0Ktravis_time:end:01a422dd:start=1572261130659518469,finish=1572261130670234179,duration=10715710,event=no_ipv6_localhost[0Ktravis_time:start:0ab86504[0Ktravis_time:end:0ab86504:start=1572261130675153050,finish=1572261130678011477,duration=2858427,event=fix_etc_mavenrc[0Ktravis_time:start:01fbd21c[0Ktravis_time:end:01fbd21c:start=1572261130682922776,finish=1572261130686580938,duration=3658162,event=fix_wwdr_certificate[0Ktravis_time:start:0e526f67[0Ktravis_time:end:0e526f67:start=1572261130694152050,finish=1572261130719928172,duration=25776122,event=put_localhost_first[0Ktravis_time:start:12d70340[0Ktravis_time:end:12d70340:start=1572261130724182962,finish=1572261130727916297,duration=3733335,event=home_paths[0Ktravis_time:start:02fec020[0Ktravis_time:end:02fec020:start=1572261130732589415,finish=1572261130747233668,duration=14644253,event=disable_initramfs[0Ktravis_time:start:1a96ce80[0Ktravis_time:end:1a96ce80:start=1572261130752262449,finish=1572261131018802294,duration=266539845,event=disable_ssh_roaming[0Ktravis_time:start:147d54b4[0Ktravis_time:end:147d54b4:start=1572261131024182743,finish=1572261131027444474,duration=3261731,event=debug_tools[0Ktravis_time:start:1bb6e9e7[0Ktravis_time:end:1bb6e9e7:start=1572261131032378652,finish=1572261131038620081,duration=6241429,event=uninstall_oclint[0Ktravis_time:start:104bff6e[0Ktravis_time:end:104bff6e:start=1572261131043416893,finish=1572261131047473530,duration=4056637,event=rvm_use[0Ktravis_time:start:05f99c2c[0Ktravis_time:end:05f99c2c:start=1572261131051879384,finish=1572261131060852061,duration=8972677,event=rm_etc_boto_cfg[0Ktravis_time:start:0172c602[0Ktravis_time:end:0172c602:start=1572261131065377131,finish=1572261131068205666,duration=2828535,event=rm_oraclejdk8_symlink[0Ktravis_time:start:00d925d8[0Ktravis_time:end:00d925d8:start=1572261131072850508,finish=1572261131137330242,duration=64479734,event=enable_i386[0Ktravis_time:start:06791a5c[0Ktravis_time:end:06791a5c:start=1572261131142923514,finish=1572261131148077369,duration=5153855,event=update_rubygems[0Ktravis_time:start:0d8dfd86[0Ktravis_time:end:0d8dfd86:start=1572261131153527394,finish=1572261132187045157,duration=1033517763,event=ensure_path_components[0Ktravis_time:start:008336b1[0Ktravis_time:end:008336b1:start=1572261132191961583,finish=1572261132194805306,duration=2843723,event=redefine_curl[0Ktravis_time:start:03301e00[0Ktravis_time:end:03301e00:start=1572261132199401270,finish=1572261132256260884,duration=56859614,event=nonblock_pipe[0Ktravis_time:start:0219f28b[0Ktravis_time:end:0219f28b:start=1572261132261137755,finish=1572261135333002651,duration=3071864896,event=apt_get_update[0Ktravis_time:start:19853bd0[0Ktravis_time:end:19853bd0:start=1572261135337250660,finish=1572261135340233103,duration=2982443,event=deprecate_xcode_64[0Ktravis_time:start:1c174581[0Ktravis_time:end:1c174581:start=1572261135344088066,finish=1572261139950421121,duration=4606333055,event=update_heroku[0Ktravis_time:start:013b1714[0Ktravis_time:end:013b1714:start=1572261139954990813,finish=1572261139957967806,duration=2976993,event=shell_session_update[0Ktravis_time:start:09cea7a4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3860
travis_fold:end:docker_mtu[0Ktravis_time:end:09cea7a4:start=1572261139962411016,finish=1572261141169179709,duration=1206768693,event=set_docker_mtu[0Ktravis_time:start:03c2cf52[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03c2cf52:start=1572261141174290453,finish=1572261141241857865,duration=67567412,event=resolvconf[0Ktravis_time:start:0c1d5d8e[0Ktravis_time:end:0c1d5d8e:start=1572261141247168324,finish=1572261141346060597,duration=98892273,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:23120e88[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:23120e88:start=1572261141432303714,finish=1572261141893680959,duration=461377245,event=configure[0Ktravis_time:start:102304bc[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:102304bc:start=1572261141899662795,finish=1572261152671852278,duration=10772189483,event=configure[0Ktravis_time:start:21eed63d[0Ktravis_fold:start:services[0Ktravis_time:start:11425f04[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:11425f04:start=1572261152699381828,finish=1572261152716194439,duration=16812611,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:11425f04:start=1572261152699381828,finish=1572261155723012952,duration=3023631124,event=services[0Ktravis_time:start:10f0f17d[0Ktravis_time:end:10f0f17d:start=1572261155728284200,finish=1572261155731333012,duration=3048812,event=fix_ps4[0Ktravis_time:start:24af0584[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0cdc16a0[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0cdc16a0:start=1572261155742065978,finish=1572261162053625144,duration=6311559166,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0cdc16a0:start=1572261155742065978,finish=1572261162098164072,duration=6356098094,event=checkout[0Ktravis_time:start:05423388[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:05423388:start=1572261162103753239,finish=1572261162118283421,duration=14530182,event=env[0Ktravis_time:start:10a11809[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:10a11809:start=1572261162124148562,finish=1572261162133570498,duration=9421936,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:08b7b100[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:684f2ebeff45e7dab02a0e37e1963e46f66ae2fb29f2d90334d515b440fbcb54
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:08b7b100:start=1572261162492809488,finish=1572261284692126754,duration=122199317266,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:009a3248[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/603824317/log.txt)