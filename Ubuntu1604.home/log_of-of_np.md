## Status: Passing 
Build: [1059](https://travis-ci.org/precice/systemtests/builds/608519809) 

Job: [1059.24](https://travis-ci.org/precice/systemtests/jobs/608519833) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:00c5e96e:start=1573094793512003898,finish=1573094793520011935,duration=8008037,event=show_system_info[0Ktravis_time:start:0913220d[0Ktravis_time:end:0913220d:start=1573094793524832898,finish=1573094793556795361,duration=31962463,event=rm_riak_source[0Ktravis_time:start:160fd59b[0Ktravis_time:end:160fd59b:start=1573094793562297612,finish=1573094793570204805,duration=7907193,event=fix_rwky_redis[0Ktravis_time:start:226fcbce[0Ktravis_time:end:226fcbce:start=1573094793574146633,finish=1573094794000724218,duration=426577585,event=wait_for_network[0Ktravis_time:start:00fd126b[0Ktravis_time:end:00fd126b:start=1573094794010531913,finish=1573094795697586528,duration=1687054615,event=update_apt_keys[0Ktravis_time:start:11815d9c[0Ktravis_time:end:11815d9c:start=1573094795704016282,finish=1573094796876159534,duration=1172143252,event=fix_hhvm_source[0Ktravis_time:start:0ad040f1[0Ktravis_time:end:0ad040f1:start=1573094796882026119,finish=1573094796892628531,duration=10602412,event=update_mongo_arch[0Ktravis_time:start:33c7ebfd[0Ktravis_time:end:33c7ebfd:start=1573094796897654362,finish=1573094796941151062,duration=43496700,event=fix_sudo_enabled_trusty[0Ktravis_time:start:048ba2a0[0Ktravis_time:end:048ba2a0:start=1573094796946231243,finish=1573094796949198057,duration=2966814,event=update_glibc[0Ktravis_time:start:06ea3a26[0Ktravis_time:end:06ea3a26:start=1573094796954079994,finish=1573094796964995667,duration=10915673,event=clean_up_path[0Ktravis_time:start:05dbb28f[0Ktravis_time:end:05dbb28f:start=1573094796969629698,finish=1573094796977986563,duration=8356865,event=fix_resolv_conf[0Ktravis_time:start:16254036[0Ktravis_time:end:16254036:start=1573094796985584517,finish=1573094796995914266,duration=10329749,event=fix_etc_hosts[0Ktravis_time:start:107c37a2[0Ktravis_time:end:107c37a2:start=1573094797002614936,finish=1573094797012743632,duration=10128696,event=fix_mvn_settings_xml[0Ktravis_time:start:0783b83c[0Ktravis_time:end:0783b83c:start=1573094797017413457,finish=1573094797028306617,duration=10893160,event=no_ipv6_localhost[0Ktravis_time:start:0cca80de[0Ktravis_time:end:0cca80de:start=1573094797034324589,finish=1573094797037627751,duration=3303162,event=fix_etc_mavenrc[0Ktravis_time:start:2ead3e4f[0Ktravis_time:end:2ead3e4f:start=1573094797042342371,finish=1573094797047176330,duration=4833959,event=fix_wwdr_certificate[0Ktravis_time:start:02952eee[0Ktravis_time:end:02952eee:start=1573094797051989162,finish=1573094797078768682,duration=26779520,event=put_localhost_first[0Ktravis_time:start:01aacd88[0Ktravis_time:end:01aacd88:start=1573094797083809143,finish=1573094797087924486,duration=4115343,event=home_paths[0Ktravis_time:start:089314f5[0Ktravis_time:end:089314f5:start=1573094797094421533,finish=1573094797108742692,duration=14321159,event=disable_initramfs[0Ktravis_time:start:353c4328[0Ktravis_time:end:353c4328:start=1573094797113620064,finish=1573094797466830710,duration=353210646,event=disable_ssh_roaming[0Ktravis_time:start:1366a423[0Ktravis_time:end:1366a423:start=1573094797472529423,finish=1573094797476036219,duration=3506796,event=debug_tools[0Ktravis_time:start:2524b435[0Ktravis_time:end:2524b435:start=1573094797481573554,finish=1573094797486218538,duration=4644984,event=uninstall_oclint[0Ktravis_time:start:22904c03[0Ktravis_time:end:22904c03:start=1573094797494574261,finish=1573094797498592362,duration=4018101,event=rvm_use[0Ktravis_time:start:1040c265[0Ktravis_time:end:1040c265:start=1573094797503661017,finish=1573094797515462005,duration=11800988,event=rm_etc_boto_cfg[0Ktravis_time:start:26537f34[0Ktravis_time:end:26537f34:start=1573094797523172733,finish=1573094797527663472,duration=4490739,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1528df18[0Ktravis_time:end:1528df18:start=1573094797534518772,finish=1573094797612496554,duration=77977782,event=enable_i386[0Ktravis_time:start:0c579264[0Ktravis_time:end:0c579264:start=1573094797622110721,finish=1573094797628570933,duration=6460212,event=update_rubygems[0Ktravis_time:start:1ee2f7a4[0Ktravis_time:end:1ee2f7a4:start=1573094797634826636,finish=1573094798811419487,duration=1176592851,event=ensure_path_components[0Ktravis_time:start:17a232d5[0Ktravis_time:end:17a232d5:start=1573094798816494925,finish=1573094798819575068,duration=3080143,event=redefine_curl[0Ktravis_time:start:09733c43[0Ktravis_time:end:09733c43:start=1573094798824231974,finish=1573094798882473478,duration=58241504,event=nonblock_pipe[0Ktravis_time:start:14a7a358[0Ktravis_time:end:14a7a358:start=1573094798887333363,finish=1573094801934903559,duration=3047570196,event=apt_get_update[0Ktravis_time:start:01055dcf[0Ktravis_time:end:01055dcf:start=1573094801941044247,finish=1573094801945339845,duration=4295598,event=deprecate_xcode_64[0Ktravis_time:start:04c5de48[0Ktravis_time:end:04c5de48:start=1573094801954211899,finish=1573094807566544485,duration=5612332586,event=update_heroku[0Ktravis_time:start:11c7b184[0Ktravis_time:end:11c7b184:start=1573094807571798770,finish=1573094807574558270,duration=2759500,event=shell_session_update[0Ktravis_time:start:018c5c8e[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3867
travis_fold:end:docker_mtu[0Ktravis_time:end:018c5c8e:start=1573094807579097403,finish=1573094808780681405,duration=1201584002,event=set_docker_mtu[0Ktravis_time:start:17ad458c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:17ad458c:start=1573094808786460468,finish=1573094808856744814,duration=70284346,event=resolvconf[0Ktravis_time:start:17fd765c[0Ktravis_time:end:17fd765c:start=1573094808861457041,finish=1573094808974371870,duration=112914829,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:000ab444[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:000ab444:start=1573094809063885868,finish=1573094809469593189,duration=405707321,event=configure[0Ktravis_time:start:0a8fd0e0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a8fd0e0:start=1573094809475694051,finish=1573094821313733842,duration=11838039791,event=configure[0Ktravis_time:start:2584b535[0Ktravis_fold:start:services[0Ktravis_time:start:32df5c70[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:32df5c70:start=1573094821341063400,finish=1573094821355990256,duration=14926856,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:32df5c70:start=1573094821341063400,finish=1573094824361862950,duration=3020799550,event=services[0Ktravis_time:start:17894d6b[0Ktravis_time:end:17894d6b:start=1573094824367526548,finish=1573094824371359917,duration=3833369,event=fix_ps4[0Ktravis_time:start:07a94336[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0b7ab498[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0b7ab498:start=1573094824382844501,finish=1573094830701427427,duration=6318582926,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0b7ab498:start=1573094824382844501,finish=1573094831342187255,duration=6959342754,event=checkout[0Ktravis_time:start:05a02808[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:05a02808:start=1573094831347540124,finish=1573094831359711473,duration=12171349,event=env[0Ktravis_time:start:0ce3ed70[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0ce3ed70:start=1573094831364942126,finish=1573094831374740485,duration=9798359,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:321397c9[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:d472ecf92550f3e4c0d9a2fa3aebe24121d0c77410191a820853bd326e430cf0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:321397c9:start=1573094831737236202,finish=1573094953762859468,duration=122025623266,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:02eb6ad8[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/608519833/log.txt)