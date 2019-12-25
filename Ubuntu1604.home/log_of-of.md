## Status: Failure 
Build: [1362](https://travis-ci.org/precice/systemtests/builds/629344851) 

Job: [1362.18](https://travis-ci.org/precice/systemtests/jobs/629344873) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
  hhvm
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:30ea0d46:start=1577274819493282091,finish=1577274819498083287,duration=4801196,event=show_system_info[0Ktravis_time:start:1cc58510[0Ktravis_time:end:1cc58510:start=1577274819500531139,finish=1577274819521634119,duration=21102980,event=rm_riak_source[0Ktravis_time:start:157aff98[0Ktravis_time:end:157aff98:start=1577274819524369759,finish=1577274819531113086,duration=6743327,event=fix_rwky_redis[0Ktravis_time:start:0104379c[0Ktravis_time:end:0104379c:start=1577274819534031595,finish=1577274819867768797,duration=333737202,event=wait_for_network[0Ktravis_time:start:00a987ce[0Ktravis_time:end:00a987ce:start=1577274819871715169,finish=1577274822899148688,duration=3027433519,event=update_apt_keys[0Ktravis_time:start:1977b580[0Ktravis_time:end:1977b580:start=1577274822904784088,finish=1577274823778335356,duration=873551268,event=fix_hhvm_source[0Ktravis_time:start:0c024b9e[0Ktravis_time:end:0c024b9e:start=1577274823782103580,finish=1577274823792019260,duration=9915680,event=update_mongo_arch[0Ktravis_time:start:072f8b2a[0Ktravis_time:end:072f8b2a:start=1577274823795121000,finish=1577274823833342024,duration=38221024,event=fix_sudo_enabled_trusty[0Ktravis_time:start:149346ab[0Ktravis_time:end:149346ab:start=1577274823837409435,finish=1577274823839864104,duration=2454669,event=update_glibc[0Ktravis_time:start:1bf21636[0Ktravis_time:end:1bf21636:start=1577274823843651906,finish=1577274823852230219,duration=8578313,event=clean_up_path[0Ktravis_time:start:0415cabb[0Ktravis_time:end:0415cabb:start=1577274823857089839,finish=1577274823864697188,duration=7607349,event=fix_resolv_conf[0Ktravis_time:start:08b24f6b[0Ktravis_time:end:08b24f6b:start=1577274823869993088,finish=1577274823877982402,duration=7989314,event=fix_etc_hosts[0Ktravis_time:start:04da49c8[0Ktravis_time:end:04da49c8:start=1577274823882070957,finish=1577274823890838740,duration=8767783,event=fix_mvn_settings_xml[0Ktravis_time:start:0f78c365[0Ktravis_time:end:0f78c365:start=1577274823894553359,finish=1577274823905929384,duration=11376025,event=no_ipv6_localhost[0Ktravis_time:start:2669859c[0Ktravis_time:end:2669859c:start=1577274823912184046,finish=1577274823914859815,duration=2675769,event=fix_etc_mavenrc[0Ktravis_time:start:01b83d2a[0Ktravis_time:end:01b83d2a:start=1577274823918813098,finish=1577274823922605647,duration=3792549,event=fix_wwdr_certificate[0Ktravis_time:start:11d4d3dc[0Ktravis_time:end:11d4d3dc:start=1577274823926614676,finish=1577274823952040536,duration=25425860,event=put_localhost_first[0Ktravis_time:start:02948556[0Ktravis_time:end:02948556:start=1577274823958184826,finish=1577274823961173828,duration=2989002,event=home_paths[0Ktravis_time:start:1ba6a128[0Ktravis_time:end:1ba6a128:start=1577274823965269084,finish=1577274823975794059,duration=10524975,event=disable_initramfs[0Ktravis_time:start:05c295e6[0Ktravis_time:end:05c295e6:start=1577274823979608157,finish=1577274824230377066,duration=250768909,event=disable_ssh_roaming[0Ktravis_time:start:164e3698[0Ktravis_time:end:164e3698:start=1577274824234121608,finish=1577274824236423578,duration=2301970,event=debug_tools[0Ktravis_time:start:08705d90[0Ktravis_time:end:08705d90:start=1577274824239895226,finish=1577274824242779423,duration=2884197,event=uninstall_oclint[0Ktravis_time:start:10f279ee[0Ktravis_time:end:10f279ee:start=1577274824247095234,finish=1577274824249835660,duration=2740426,event=rvm_use[0Ktravis_time:start:052d1ae8[0Ktravis_time:end:052d1ae8:start=1577274824253239761,finish=1577274824259747107,duration=6507346,event=rm_etc_boto_cfg[0Ktravis_time:start:1212dcab[0Ktravis_time:end:1212dcab:start=1577274824263377426,finish=1577274824267482105,duration=4104679,event=rm_oraclejdk8_symlink[0Ktravis_time:start:095148ee[0Ktravis_time:end:095148ee:start=1577274824271189234,finish=1577274824320837947,duration=49648713,event=enable_i386[0Ktravis_time:start:00ea89d0[0Ktravis_time:end:00ea89d0:start=1577274824325119462,finish=1577274824328761375,duration=3641913,event=update_rubygems[0Ktravis_time:start:08ad3cf5[0Ktravis_time:end:08ad3cf5:start=1577274824333240472,finish=1577274825163433524,duration=830193052,event=ensure_path_components[0Ktravis_time:start:00220764[0Ktravis_time:end:00220764:start=1577274825169122512,finish=1577274825171646071,duration=2523559,event=redefine_curl[0Ktravis_time:start:01bc1033[0Ktravis_time:end:01bc1033:start=1577274825175148819,finish=1577274825221431174,duration=46282355,event=nonblock_pipe[0Ktravis_time:start:10c89f28[0Ktravis_time:end:10c89f28:start=1577274825226378333,finish=1577274831258281135,duration=6031902802,event=apt_get_update[0Ktravis_time:start:144355b0[0Ktravis_time:end:144355b0:start=1577274831262399040,finish=1577274831264935711,duration=2536671,event=deprecate_xcode_64[0Ktravis_time:start:02de7996[0Ktravis_time:end:02de7996:start=1577274831268356513,finish=1577274834967978850,duration=3699622337,event=update_heroku[0Ktravis_time:start:048078c6[0Ktravis_time:end:048078c6:start=1577274834972031786,finish=1577274834974622468,duration=2590682,event=shell_session_update[0Ktravis_time:start:05fd0150[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3981
travis_fold:end:docker_mtu[0Ktravis_time:end:05fd0150:start=1577274834978614924,finish=1577274836162353570,duration=1183738646,event=set_docker_mtu[0Ktravis_time:start:0d8d51c8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0d8d51c8:start=1577274836166243397,finish=1577274836217878273,duration=51634876,event=resolvconf[0Ktravis_time:start:0c976434[0Ktravis_time:end:0c976434:start=1577274836221249046,finish=1577274836306424426,duration=85175380,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2c597b9c[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2c597b9c:start=1577274836373194123,finish=1577274836718809017,duration=345614894,event=configure[0Ktravis_time:start:1e842028[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1e842028:start=1577274836723616939,finish=1577274844886823588,duration=8163206649,event=configure[0Ktravis_time:start:090356d0[0Ktravis_fold:start:services[0Ktravis_time:start:07a4a374[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:07a4a374:start=1577274844908521361,finish=1577274844921540364,duration=13019003,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:07a4a374:start=1577274844908521361,finish=1577274847926815133,duration=3018293772,event=services[0Ktravis_time:start:2ff5cfe0[0Ktravis_time:end:2ff5cfe0:start=1577274847930934104,finish=1577274847933591395,duration=2657291,event=fix_ps4[0Ktravis_time:start:0ced4179[0K
travis_fold:start:git.checkout[0Ktravis_time:start:2d6e191c[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:2d6e191c:start=1577274847940282010,finish=1577274853060239249,duration=5119957239,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 968fe698268820917cf52199d2d3dcbaaf61fbaf
travis_fold:end:git.checkout[0K
travis_time:end:2d6e191c:start=1577274847940282010,finish=1577274853112794561,duration=5172512551,event=checkout[0Ktravis_time:start:056f2a4f[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:056f2a4f:start=1577274853116670760,finish=1577274853124787374,duration=8116614,event=env[0Ktravis_time:start:008cf3a8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:008cf3a8:start=1577274853128245108,finish=1577274853133384905,duration=5139797,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:070c2eb8[0K$ python system_testing.py -s of-of
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:16b94ae5c4de8bd2512ad80b95088637775c1122d6d63de4bfa00f1defdf566a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B
```
[
Full job log](https://api.travis-ci.org/v3/job/629344873/log.txt)