## Status: Failure 
Build: [1362](https://travis-ci.org/precice/systemtests/builds/629344851) 

Job: [1362.23](https://travis-ci.org/precice/systemtests/jobs/629344878) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

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
travis_time:end:0cfa67fe:start=1577274988656010620,finish=1577274988661948532,duration=5937912,event=show_system_info[0Ktravis_time:start:04ba4f66[0Ktravis_time:end:04ba4f66:start=1577274988666071849,finish=1577274988683886117,duration=17814268,event=rm_riak_source[0Ktravis_time:start:002d8fcb[0Ktravis_time:end:002d8fcb:start=1577274988686695742,finish=1577274988691359343,duration=4663601,event=fix_rwky_redis[0Ktravis_time:start:12d46e2a[0Ktravis_time:end:12d46e2a:start=1577274988694144016,finish=1577274989012402872,duration=318258856,event=wait_for_network[0Ktravis_time:start:00698614[0Ktravis_time:end:00698614:start=1577274989016915994,finish=1577274990305845595,duration=1288929601,event=update_apt_keys[0Ktravis_time:start:0fe85a6b[0Ktravis_time:end:0fe85a6b:start=1577274990309403268,finish=1577274991139480892,duration=830077624,event=fix_hhvm_source[0Ktravis_time:start:2a33e650[0Ktravis_time:end:2a33e650:start=1577274991143460691,finish=1577274991152511317,duration=9050626,event=update_mongo_arch[0Ktravis_time:start:022c1e70[0Ktravis_time:end:022c1e70:start=1577274991156055558,finish=1577274991192560775,duration=36505217,event=fix_sudo_enabled_trusty[0Ktravis_time:start:06c11a4e[0Ktravis_time:end:06c11a4e:start=1577274991196555509,finish=1577274991198890711,duration=2335202,event=update_glibc[0Ktravis_time:start:292679a0[0Ktravis_time:end:292679a0:start=1577274991202930754,finish=1577274991209781325,duration=6850571,event=clean_up_path[0Ktravis_time:start:04fbacf1[0Ktravis_time:end:04fbacf1:start=1577274991213738353,finish=1577274991220295706,duration=6557353,event=fix_resolv_conf[0Ktravis_time:start:043e7250[0Ktravis_time:end:043e7250:start=1577274991224936612,finish=1577274991232416526,duration=7479914,event=fix_etc_hosts[0Ktravis_time:start:0d57f220[0Ktravis_time:end:0d57f220:start=1577274991235766183,finish=1577274991245446842,duration=9680659,event=fix_mvn_settings_xml[0Ktravis_time:start:077e71f0[0Ktravis_time:end:077e71f0:start=1577274991249184804,finish=1577274991256905909,duration=7721105,event=no_ipv6_localhost[0Ktravis_time:start:0482ae5c[0Ktravis_time:end:0482ae5c:start=1577274991261136514,finish=1577274991263328157,duration=2191643,event=fix_etc_mavenrc[0Ktravis_time:start:02c5158a[0Ktravis_time:end:02c5158a:start=1577274991268445781,finish=1577274991271447259,duration=3001478,event=fix_wwdr_certificate[0Ktravis_time:start:0112fb75[0Ktravis_time:end:0112fb75:start=1577274991275442378,finish=1577274991297443704,duration=22001326,event=put_localhost_first[0Ktravis_time:start:0021c420[0Ktravis_time:end:0021c420:start=1577274991301337561,finish=1577274991304835707,duration=3498146,event=home_paths[0Ktravis_time:start:25e7c8eb[0Ktravis_time:end:25e7c8eb:start=1577274991308827078,finish=1577274991321606451,duration=12779373,event=disable_initramfs[0Ktravis_time:start:1be01c2f[0Ktravis_time:end:1be01c2f:start=1577274991325430119,finish=1577274991544853361,duration=219423242,event=disable_ssh_roaming[0Ktravis_time:start:1cd7c17d[0Ktravis_time:end:1cd7c17d:start=1577274991549020410,finish=1577274991551551204,duration=2530794,event=debug_tools[0Ktravis_time:start:0df7f1a2[0Ktravis_time:end:0df7f1a2:start=1577274991555502847,finish=1577274991558358564,duration=2855717,event=uninstall_oclint[0Ktravis_time:start:1f5f82cc[0Ktravis_time:end:1f5f82cc:start=1577274991561888092,finish=1577274991564680493,duration=2792401,event=rvm_use[0Ktravis_time:start:087b5897[0Ktravis_time:end:087b5897:start=1577274991568058851,finish=1577274991576484954,duration=8426103,event=rm_etc_boto_cfg[0Ktravis_time:start:2009321d[0Ktravis_time:end:2009321d:start=1577274991580743740,finish=1577274991582979723,duration=2235983,event=rm_oraclejdk8_symlink[0Ktravis_time:start:013afb8c[0Ktravis_time:end:013afb8c:start=1577274991586884115,finish=1577274991636504150,duration=49620035,event=enable_i386[0Ktravis_time:start:05906aea[0Ktravis_time:end:05906aea:start=1577274991640730870,finish=1577274991643984703,duration=3253833,event=update_rubygems[0Ktravis_time:start:0c0fc876[0Ktravis_time:end:0c0fc876:start=1577274991648005636,finish=1577274992460205705,duration=812200069,event=ensure_path_components[0Ktravis_time:start:06a564b8[0Ktravis_time:end:06a564b8:start=1577274992464395635,finish=1577274992467119490,duration=2723855,event=redefine_curl[0Ktravis_time:start:018440c6[0Ktravis_time:end:018440c6:start=1577274992470566257,finish=1577274992512960409,duration=42394152,event=nonblock_pipe[0Ktravis_time:start:14867306[0Ktravis_time:end:14867306:start=1577274992516748763,finish=1577274998545363896,duration=6028615133,event=apt_get_update[0Ktravis_time:start:010a92b7[0Ktravis_time:end:010a92b7:start=1577274998549272889,finish=1577274998551770477,duration=2497588,event=deprecate_xcode_64[0Ktravis_time:start:0575068e[0Ktravis_time:end:0575068e:start=1577274998555147014,finish=1577275001822125593,duration=3266978579,event=update_heroku[0Ktravis_time:start:2371b88a[0Ktravis_time:end:2371b88a:start=1577275001825825808,finish=1577275001828625777,duration=2799969,event=shell_session_update[0Ktravis_time:start:2d0e5260[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3903
travis_fold:end:docker_mtu[0Ktravis_time:end:2d0e5260:start=1577275001832330378,finish=1577275003011851876,duration=1179521498,event=set_docker_mtu[0Ktravis_time:start:0069ffda[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0069ffda:start=1577275003015009735,finish=1577275003070127742,duration=55118007,event=resolvconf[0Ktravis_time:start:18e6d1c2[0Ktravis_time:end:18e6d1c2:start=1577275003073026293,finish=1577275003152399016,duration=79372723,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:12544918[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:12544918:start=1577275003218644203,finish=1577275003619530994,duration=400886791,event=configure[0Ktravis_time:start:1bac19d0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1bac19d0:start=1577275003623988254,finish=1577275011433389932,duration=7809401678,event=configure[0Ktravis_time:start:043d3200[0Ktravis_fold:start:services[0Ktravis_time:start:0b65b1b0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0b65b1b0:start=1577275011455461153,finish=1577275011468821132,duration=13359979,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0b65b1b0:start=1577275011455461153,finish=1577275014474632175,duration=3019171022,event=services[0Ktravis_time:start:002ef3b3[0Ktravis_time:end:002ef3b3:start=1577275014479171467,finish=1577275014481893409,duration=2721942,event=fix_ps4[0Ktravis_time:start:0d8a6562[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0b4d0fb6[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0b4d0fb6:start=1577275014488636525,finish=1577275019568233571,duration=5079597046,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 968fe698268820917cf52199d2d3dcbaaf61fbaf
travis_fold:end:git.checkout[0K
travis_time:end:0b4d0fb6:start=1577275014488636525,finish=1577275020058641294,duration=5570004769,event=checkout[0Ktravis_time:start:08ca66ea[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:08ca66ea:start=1577275020063250802,finish=1577275020070900737,duration=7649935,event=env[0Ktravis_time:start:0141b9d0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0141b9d0:start=1577275020081789098,finish=1577275020086882867,duration=5093769,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:261e0c34[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:16b94ae5c4de8bd2512ad80b95088637775c1122d6d63de4bfa00f1defdf566a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/629344878/log.txt)