## Status: Passing 
Build: [1057](https://travis-ci.org/precice/systemtests/builds/607431677) 

Job: [1057.24](https://travis-ci.org/precice/systemtests/jobs/607431701) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:32018373:start=1572922031302855967,finish=1572922031309394744,duration=6538777,event=show_system_info[0Ktravis_time:start:00865095[0Ktravis_time:end:00865095:start=1572922031312740397,finish=1572922031345978698,duration=33238301,event=rm_riak_source[0Ktravis_time:start:0b9d94d6[0Ktravis_time:end:0b9d94d6:start=1572922031350015329,finish=1572922031357443085,duration=7427756,event=fix_rwky_redis[0Ktravis_time:start:156b8404[0Ktravis_time:end:156b8404:start=1572922031361077890,finish=1572922031870691262,duration=509613372,event=wait_for_network[0Ktravis_time:start:0aa17098[0Ktravis_time:end:0aa17098:start=1572922031877063391,finish=1572922033483262735,duration=1606199344,event=update_apt_keys[0Ktravis_time:start:0c7f8eb1[0Ktravis_time:end:0c7f8eb1:start=1572922033487910166,finish=1572922034597768980,duration=1109858814,event=fix_hhvm_source[0Ktravis_time:start:07b61410[0Ktravis_time:end:07b61410:start=1572922034602992039,finish=1572922034614946218,duration=11954179,event=update_mongo_arch[0Ktravis_time:start:2640e16c[0Ktravis_time:end:2640e16c:start=1572922034619825045,finish=1572922034666421968,duration=46596923,event=fix_sudo_enabled_trusty[0Ktravis_time:start:00b1117a[0Ktravis_time:end:00b1117a:start=1572922034672088583,finish=1572922034675506645,duration=3418062,event=update_glibc[0Ktravis_time:start:01250238[0Ktravis_time:end:01250238:start=1572922034680574910,finish=1572922034690376130,duration=9801220,event=clean_up_path[0Ktravis_time:start:04b55142[0Ktravis_time:end:04b55142:start=1572922034696381201,finish=1572922034706231877,duration=9850676,event=fix_resolv_conf[0Ktravis_time:start:06e800e8[0Ktravis_time:end:06e800e8:start=1572922034710711814,finish=1572922034721836308,duration=11124494,event=fix_etc_hosts[0Ktravis_time:start:0a42574d[0Ktravis_time:end:0a42574d:start=1572922034728018161,finish=1572922034739323893,duration=11305732,event=fix_mvn_settings_xml[0Ktravis_time:start:2c26f3b8[0Ktravis_time:end:2c26f3b8:start=1572922034744191097,finish=1572922034756015097,duration=11824000,event=no_ipv6_localhost[0Ktravis_time:start:01f26618[0Ktravis_time:end:01f26618:start=1572922034761516125,finish=1572922034764666695,duration=3150570,event=fix_etc_mavenrc[0Ktravis_time:start:02e81150[0Ktravis_time:end:02e81150:start=1572922034770446988,finish=1572922034774437891,duration=3990903,event=fix_wwdr_certificate[0Ktravis_time:start:252f23ff[0Ktravis_time:end:252f23ff:start=1572922034779344024,finish=1572922034808908008,duration=29563984,event=put_localhost_first[0Ktravis_time:start:1831a91c[0Ktravis_time:end:1831a91c:start=1572922034814528049,finish=1572922034819238721,duration=4710672,event=home_paths[0Ktravis_time:start:01d2cea8[0Ktravis_time:end:01d2cea8:start=1572922034824731275,finish=1572922034839636021,duration=14904746,event=disable_initramfs[0Ktravis_time:start:1de482e0[0Ktravis_time:end:1de482e0:start=1572922034845176817,finish=1572922035194164204,duration=348987387,event=disable_ssh_roaming[0Ktravis_time:start:0d46e30a[0Ktravis_time:end:0d46e30a:start=1572922035199479720,finish=1572922035202588461,duration=3108741,event=debug_tools[0Ktravis_time:start:035aed18[0Ktravis_time:end:035aed18:start=1572922035209100248,finish=1572922035213158061,duration=4057813,event=uninstall_oclint[0Ktravis_time:start:1e14ecf2[0Ktravis_time:end:1e14ecf2:start=1572922035217563792,finish=1572922035221493564,duration=3929772,event=rvm_use[0Ktravis_time:start:0d60a040[0Ktravis_time:end:0d60a040:start=1572922035226460124,finish=1572922035236127347,duration=9667223,event=rm_etc_boto_cfg[0Ktravis_time:start:0d1c5cf2[0Ktravis_time:end:0d1c5cf2:start=1572922035243061472,finish=1572922035246570437,duration=3508965,event=rm_oraclejdk8_symlink[0Ktravis_time:start:08ba6248[0Ktravis_time:end:08ba6248:start=1572922035251532176,finish=1572922035313827352,duration=62295176,event=enable_i386[0Ktravis_time:start:21526c5c[0Ktravis_time:end:21526c5c:start=1572922035320179628,finish=1572922035325682052,duration=5502424,event=update_rubygems[0Ktravis_time:start:1f538106[0Ktravis_time:end:1f538106:start=1572922035331936455,finish=1572922036514578548,duration=1182642093,event=ensure_path_components[0Ktravis_time:start:14cdab72[0Ktravis_time:end:14cdab72:start=1572922036519883582,finish=1572922036523309151,duration=3425569,event=redefine_curl[0Ktravis_time:start:0ed7cb75[0Ktravis_time:end:0ed7cb75:start=1572922036529238364,finish=1572922036589333647,duration=60095283,event=nonblock_pipe[0Ktravis_time:start:02831e4c[0Ktravis_time:end:02831e4c:start=1572922036595174807,finish=1572922039653580789,duration=3058405982,event=apt_get_update[0Ktravis_time:start:112b3050[0Ktravis_time:end:112b3050:start=1572922039660188103,finish=1572922039663341334,duration=3153231,event=deprecate_xcode_64[0Ktravis_time:start:09e26758[0Ktravis_time:end:09e26758:start=1572922039668356499,finish=1572922044645296046,duration=4976939547,event=update_heroku[0Ktravis_time:start:00866148[0Ktravis_time:end:00866148:start=1572922044651074983,finish=1572922044654303803,duration=3228820,event=shell_session_update[0Ktravis_time:start:361884ca[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3895
travis_fold:end:docker_mtu[0Ktravis_time:end:361884ca:start=1572922044658512671,finish=1572922045855098232,duration=1196585561,event=set_docker_mtu[0Ktravis_time:start:0fe618ce[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0fe618ce:start=1572922045860893396,finish=1572922045937216988,duration=76323592,event=resolvconf[0Ktravis_time:start:02471ae0[0Ktravis_time:end:02471ae0:start=1572922045942911056,finish=1572922046052075648,duration=109164592,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:07cb4721[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:07cb4721:start=1572922046145287352,finish=1572922047756897280,duration=1611609928,event=configure[0Ktravis_time:start:03b3adc3[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:03b3adc3:start=1572922047764761504,finish=1572922059281884301,duration=11517122797,event=configure[0Ktravis_time:start:21517888[0Ktravis_fold:start:services[0Ktravis_time:start:11cf16c0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:11cf16c0:start=1572922059310770704,finish=1572922059326442687,duration=15671983,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:11cf16c0:start=1572922059310770704,finish=1572922062333005541,duration=3022234837,event=services[0Ktravis_time:start:0be6d298[0Ktravis_time:end:0be6d298:start=1572922062338091104,finish=1572922062341072662,duration=2981558,event=fix_ps4[0Ktravis_time:start:001d5725[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08961f5d[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08961f5d:start=1572922062350484995,finish=1572922068980111920,duration=6629626925,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:08961f5d:start=1572922062350484995,finish=1572922069830510377,duration=7480025382,event=checkout[0Ktravis_time:start:08167a32[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:08167a32:start=1572922069836373429,finish=1572922069849128993,duration=12755564,event=env[0Ktravis_time:start:07860d80[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:07860d80:start=1572922069855384412,finish=1572922069862075772,duration=6691360,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:03fd8984[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:05fe1ccc5198ad34e3a536b114ccdb3c99481211760a11e8e6218a3edb849bae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03fd8984:start=1572922070254089029,finish=1572922191402677119,duration=121148588090,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:016f4ebc[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/607431701/log.txt)