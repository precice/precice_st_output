## Status: Passing 
Build: [1032](https://travis-ci.org/precice/systemtests/builds/603568985) 

Job: [1032.14](https://travis-ci.org/precice/systemtests/jobs/603568999) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e6ee51b6890c...5e709cade038) 

---
Last 100 lines of the job log at the moment of push:
```
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:03156210:start=1572199140606192551,finish=1572199140612845537,duration=6652986,event=show_system_info[0Ktravis_time:start:05903fcd[0Ktravis_time:end:05903fcd:start=1572199140616315923,finish=1572199140644973400,duration=28657477,event=rm_riak_source[0Ktravis_time:start:0071e3f2[0Ktravis_time:end:0071e3f2:start=1572199140649103150,finish=1572199140655446276,duration=6343126,event=fix_rwky_redis[0Ktravis_time:start:20a5a2df[0Ktravis_time:end:20a5a2df:start=1572199140659831053,finish=1572199141095286611,duration=435455558,event=wait_for_network[0Ktravis_time:start:08df8520[0Ktravis_time:end:08df8520:start=1572199141101439887,finish=1572199142945266351,duration=1843826464,event=update_apt_keys[0Ktravis_time:start:002902f0[0Ktravis_time:end:002902f0:start=1572199142950767138,finish=1572199144044786433,duration=1094019295,event=fix_hhvm_source[0Ktravis_time:start:0c3ad1d2[0Ktravis_time:end:0c3ad1d2:start=1572199144050558676,finish=1572199144062698008,duration=12139332,event=update_mongo_arch[0Ktravis_time:start:10c99dac[0Ktravis_time:end:10c99dac:start=1572199144068283602,finish=1572199144116192802,duration=47909200,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0d005056[0Ktravis_time:end:0d005056:start=1572199144122020982,finish=1572199144125379564,duration=3358582,event=update_glibc[0Ktravis_time:start:01205487[0Ktravis_time:end:01205487:start=1572199144130695011,finish=1572199144141853795,duration=11158784,event=clean_up_path[0Ktravis_time:start:29cc6ca9[0Ktravis_time:end:29cc6ca9:start=1572199144146696777,finish=1572199144157175990,duration=10479213,event=fix_resolv_conf[0Ktravis_time:start:13f8f300[0Ktravis_time:end:13f8f300:start=1572199144162920536,finish=1572199144176440709,duration=13520173,event=fix_etc_hosts[0Ktravis_time:start:06371530[0Ktravis_time:end:06371530:start=1572199144182318967,finish=1572199144196100521,duration=13781554,event=fix_mvn_settings_xml[0Ktravis_time:start:059e84a0[0Ktravis_time:end:059e84a0:start=1572199144201630406,finish=1572199144215400954,duration=13770548,event=no_ipv6_localhost[0Ktravis_time:start:016ce435[0Ktravis_time:end:016ce435:start=1572199144221631747,finish=1572199144225475977,duration=3844230,event=fix_etc_mavenrc[0Ktravis_time:start:1d0b10c0[0Ktravis_time:end:1d0b10c0:start=1572199144230836421,finish=1572199144235948451,duration=5112030,event=fix_wwdr_certificate[0Ktravis_time:start:02052443[0Ktravis_time:end:02052443:start=1572199144242653054,finish=1572199144274766258,duration=32113204,event=put_localhost_first[0Ktravis_time:start:03baa229[0Ktravis_time:end:03baa229:start=1572199144281246106,finish=1572199144286304884,duration=5058778,event=home_paths[0Ktravis_time:start:0cb50c8a[0Ktravis_time:end:0cb50c8a:start=1572199144291992959,finish=1572199144307608520,duration=15615561,event=disable_initramfs[0Ktravis_time:start:03a220a0[0Ktravis_time:end:03a220a0:start=1572199144313486884,finish=1572199144676713236,duration=363226352,event=disable_ssh_roaming[0Ktravis_time:start:16098704[0Ktravis_time:end:16098704:start=1572199144682349265,finish=1572199144685931937,duration=3582672,event=debug_tools[0Ktravis_time:start:13771d68[0Ktravis_time:end:13771d68:start=1572199144691592958,finish=1572199144696025029,duration=4432071,event=uninstall_oclint[0Ktravis_time:start:0298ab20[0Ktravis_time:end:0298ab20:start=1572199144700905072,finish=1572199144706466429,duration=5561357,event=rvm_use[0Ktravis_time:start:1c291422[0Ktravis_time:end:1c291422:start=1572199144711888132,finish=1572199144723552610,duration=11664478,event=rm_etc_boto_cfg[0Ktravis_time:start:1e26142f[0Ktravis_time:end:1e26142f:start=1572199144729105005,finish=1572199144733040246,duration=3935241,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1ed3ccf3[0Ktravis_time:end:1ed3ccf3:start=1572199144738284686,finish=1572199144805415072,duration=67130386,event=enable_i386[0Ktravis_time:start:0202a38c[0Ktravis_time:end:0202a38c:start=1572199144810880780,finish=1572199144816673297,duration=5792517,event=update_rubygems[0Ktravis_time:start:1009ccba[0Ktravis_time:end:1009ccba:start=1572199144821573954,finish=1572199145906876913,duration=1085302959,event=ensure_path_components[0Ktravis_time:start:267b412c[0Ktravis_time:end:267b412c:start=1572199145911676171,finish=1572199145914799642,duration=3123471,event=redefine_curl[0Ktravis_time:start:237afba4[0Ktravis_time:end:237afba4:start=1572199145919855465,finish=1572199145981037533,duration=61182068,event=nonblock_pipe[0Ktravis_time:start:00863a98[0Ktravis_time:end:00863a98:start=1572199145986110000,finish=1572199149166636647,duration=3180526647,event=apt_get_update[0Ktravis_time:start:050d0db0[0Ktravis_time:end:050d0db0:start=1572199149172207788,finish=1572199149175190900,duration=2983112,event=deprecate_xcode_64[0Ktravis_time:start:0187abf2[0Ktravis_time:end:0187abf2:start=1572199149180096105,finish=1572199154401557985,duration=5221461880,event=update_heroku[0Ktravis_time:start:03bc9288[0Ktravis_time:end:03bc9288:start=1572199154406280198,finish=1572199154409299938,duration=3019740,event=shell_session_update[0Ktravis_time:start:125975b9[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3891
travis_fold:end:docker_mtu[0Ktravis_time:end:125975b9:start=1572199154413697919,finish=1572199155618180996,duration=1204483077,event=set_docker_mtu[0Ktravis_time:start:1bb0ad92[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1bb0ad92:start=1572199155623838211,finish=1572199155703185023,duration=79346812,event=resolvconf[0Ktravis_time:start:114d708c[0Ktravis_time:end:114d708c:start=1572199155709820160,finish=1572199155838978459,duration=129158299,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0196a5d0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0196a5d0:start=1572199155939409869,finish=1572199156858492846,duration=919082977,event=configure[0Ktravis_time:start:0233786a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0233786a:start=1572199156864634663,finish=1572199172318548249,duration=15453913586,event=configure[0Ktravis_time:start:00c93708[0Ktravis_fold:start:services[0Ktravis_time:start:02547b40[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:02547b40:start=1572199172345307666,finish=1572199172360388072,duration=15080406,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:02547b40:start=1572199172345307666,finish=1572199175366991011,duration=3021683345,event=services[0Ktravis_time:start:1c6534c8[0Ktravis_time:end:1c6534c8:start=1572199175373406415,finish=1572199175377136799,duration=3730384,event=fix_ps4[0Ktravis_time:start:1e1d7ebe[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00c6a9e0[0K$ git clone --depth=50 --branch=EderK-fix-after_success https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00c6a9e0:start=1572199175388227256,finish=1572199181845308988,duration=6457081732,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 5e709cade038f050986e914ea2a9ab1de43e4de9
travis_fold:end:git.checkout[0K
travis_time:end:00c6a9e0:start=1572199175388227256,finish=1572199182557186313,duration=7168959057,event=checkout[0Ktravis_time:start:0142de14[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0142de14:start=1572199182562729025,finish=1572199182577133048,duration=14404023,event=env[0Ktravis_time:start:140351d3[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:140351d3:start=1572199182583760028,finish=1572199182592684254,duration=8924226,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:18ebc8b0[0K$ python system_testing.py -s of-of
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
Digest: sha256:97bb7e6e100569ab857c2847a688e902aeedb81af15a98a336fc9272ade3829f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating tutorial-data
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/603568999/log.txt)