## Status: Passing 
Build: [1036](https://travis-ci.org/precice/systemtests/builds/603688824) 

Job: [1036.18](https://travis-ci.org/precice/systemtests/jobs/603688851) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

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
travis_time:end:3463af68:start=1572230218160350474,finish=1572230218166773659,duration=6423185,event=show_system_info[0Ktravis_time:start:297dd930[0Ktravis_time:end:297dd930:start=1572230218169855415,finish=1572230218197161358,duration=27305943,event=rm_riak_source[0Ktravis_time:start:2c9ef71f[0Ktravis_time:end:2c9ef71f:start=1572230218200754246,finish=1572230218208540292,duration=7786046,event=fix_rwky_redis[0Ktravis_time:start:14d88bf3[0Ktravis_time:end:14d88bf3:start=1572230218212350259,finish=1572230218590617729,duration=378267470,event=wait_for_network[0Ktravis_time:start:0f939252[0Ktravis_time:end:0f939252:start=1572230218595723239,finish=1572230220173893043,duration=1578169804,event=update_apt_keys[0Ktravis_time:start:27c98ae0[0Ktravis_time:end:27c98ae0:start=1572230220179121604,finish=1572230221281252607,duration=1102131003,event=fix_hhvm_source[0Ktravis_time:start:195ea21a[0Ktravis_time:end:195ea21a:start=1572230221286228753,finish=1572230221299530878,duration=13302125,event=update_mongo_arch[0Ktravis_time:start:03d6ad72[0Ktravis_time:end:03d6ad72:start=1572230221307323628,finish=1572230221352830449,duration=45506821,event=fix_sudo_enabled_trusty[0Ktravis_time:start:03e1ef28[0Ktravis_time:end:03e1ef28:start=1572230221357126981,finish=1572230221360255449,duration=3128468,event=update_glibc[0Ktravis_time:start:00c739bb[0Ktravis_time:end:00c739bb:start=1572230221364333369,finish=1572230221379391864,duration=15058495,event=clean_up_path[0Ktravis_time:start:239d9cd2[0Ktravis_time:end:239d9cd2:start=1572230221383352674,finish=1572230221394116202,duration=10763528,event=fix_resolv_conf[0Ktravis_time:start:0714b9dc[0Ktravis_time:end:0714b9dc:start=1572230221398119914,finish=1572230221409659465,duration=11539551,event=fix_etc_hosts[0Ktravis_time:start:0b6669f0[0Ktravis_time:end:0b6669f0:start=1572230221413785437,finish=1572230221427155690,duration=13370253,event=fix_mvn_settings_xml[0Ktravis_time:start:13406bde[0Ktravis_time:end:13406bde:start=1572230221432079804,finish=1572230221442870187,duration=10790383,event=no_ipv6_localhost[0Ktravis_time:start:1b0fe4b0[0Ktravis_time:end:1b0fe4b0:start=1572230221447785005,finish=1572230221450648886,duration=2863881,event=fix_etc_mavenrc[0Ktravis_time:start:0a3a27fb[0Ktravis_time:end:0a3a27fb:start=1572230221455403586,finish=1572230221459265561,duration=3861975,event=fix_wwdr_certificate[0Ktravis_time:start:110d6c75[0Ktravis_time:end:110d6c75:start=1572230221465727905,finish=1572230221491743418,duration=26015513,event=put_localhost_first[0Ktravis_time:start:0100b400[0Ktravis_time:end:0100b400:start=1572230221497136800,finish=1572230221501108005,duration=3971205,event=home_paths[0Ktravis_time:start:00712c94[0Ktravis_time:end:00712c94:start=1572230221505117137,finish=1572230221519619988,duration=14502851,event=disable_initramfs[0Ktravis_time:start:0bef2ed1[0Ktravis_time:end:0bef2ed1:start=1572230221524210971,finish=1572230221895333086,duration=371122115,event=disable_ssh_roaming[0Ktravis_time:start:2a3240d8[0Ktravis_time:end:2a3240d8:start=1572230221899388949,finish=1572230221903954854,duration=4565905,event=debug_tools[0Ktravis_time:start:09f38520[0Ktravis_time:end:09f38520:start=1572230221907901891,finish=1572230221911894950,duration=3993059,event=uninstall_oclint[0Ktravis_time:start:13549760[0Ktravis_time:end:13549760:start=1572230221915954879,finish=1572230221919983897,duration=4029018,event=rvm_use[0Ktravis_time:start:0af5d32c[0Ktravis_time:end:0af5d32c:start=1572230221932744020,finish=1572230221941296374,duration=8552354,event=rm_etc_boto_cfg[0Ktravis_time:start:1a145596[0Ktravis_time:end:1a145596:start=1572230221947285213,finish=1572230221950243240,duration=2958027,event=rm_oraclejdk8_symlink[0Ktravis_time:start:15e897cb[0Ktravis_time:end:15e897cb:start=1572230221955258758,finish=1572230222018311552,duration=63052794,event=enable_i386[0Ktravis_time:start:0ba198a1[0Ktravis_time:end:0ba198a1:start=1572230222024737833,finish=1572230222029566855,duration=4829022,event=update_rubygems[0Ktravis_time:start:1887f785[0Ktravis_time:end:1887f785:start=1572230222035226354,finish=1572230223075129069,duration=1039902715,event=ensure_path_components[0Ktravis_time:start:006f6948[0Ktravis_time:end:006f6948:start=1572230223080737744,finish=1572230223083947620,duration=3209876,event=redefine_curl[0Ktravis_time:start:29e4c374[0Ktravis_time:end:29e4c374:start=1572230223089051745,finish=1572230223147317267,duration=58265522,event=nonblock_pipe[0Ktravis_time:start:11efba80[0Ktravis_time:end:11efba80:start=1572230223152933346,finish=1572230226198808663,duration=3045875317,event=apt_get_update[0Ktravis_time:start:06525844[0Ktravis_time:end:06525844:start=1572230226204591402,finish=1572230226207779030,duration=3187628,event=deprecate_xcode_64[0Ktravis_time:start:0ffa67e8[0Ktravis_time:end:0ffa67e8:start=1572230226213407654,finish=1572230231077301632,duration=4863893978,event=update_heroku[0Ktravis_time:start:113b0dc8[0Ktravis_time:end:113b0dc8:start=1572230231082201888,finish=1572230231085548663,duration=3346775,event=shell_session_update[0Ktravis_time:start:024d974c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3886
travis_fold:end:docker_mtu[0Ktravis_time:end:024d974c:start=1572230231089865313,finish=1572230232287426827,duration=1197561514,event=set_docker_mtu[0Ktravis_time:start:0340c380[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0340c380:start=1572230232292284908,finish=1572230232362729656,duration=70444748,event=resolvconf[0Ktravis_time:start:1c30da06[0Ktravis_time:end:1c30da06:start=1572230232368371330,finish=1572230232474744784,duration=106373454,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:01a24418[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:01a24418:start=1572230232559246722,finish=1572230233159059435,duration=599812713,event=configure[0Ktravis_time:start:01b9a540[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:01b9a540:start=1572230233164756928,finish=1572230243416142810,duration=10251385882,event=configure[0Ktravis_time:start:26a7dba0[0Ktravis_fold:start:services[0Ktravis_time:start:0495b4de[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0495b4de:start=1572230243444796062,finish=1572230243460790945,duration=15994883,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0495b4de:start=1572230243444796062,finish=1572230246467473570,duration=3022677508,event=services[0Ktravis_time:start:22149d5c[0Ktravis_time:end:22149d5c:start=1572230246471791733,finish=1572230246474705452,duration=2913719,event=fix_ps4[0Ktravis_time:start:01c108ec[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0105012e[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0105012e:start=1572230246482822579,finish=1572230252953592484,duration=6470769905,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 9921a3e9e3f7596df67493847bbc01f17a3b226e
travis_fold:end:git.checkout[0K
travis_time:end:0105012e:start=1572230246482822579,finish=1572230253801565141,duration=7318742562,event=checkout[0Ktravis_time:start:01518cba[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01518cba:start=1572230253808152750,finish=1572230253819399245,duration=11246495,event=env[0Ktravis_time:start:00cdc56c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00cdc56c:start=1572230253824456874,finish=1572230253831506798,duration=7049924,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1f610232[0K$ python system_testing.py -s of-of
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
Digest: sha256:107316668f285cf4c40b471c4616ea1a6e56b3f2b88abd4e706e18828b74fafb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/603688851/log.txt)