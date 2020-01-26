## Status: Failure 
Build: [1519](https://travis-ci.org/precice/systemtests/builds/641972691) 

Job: [1519.15](https://travis-ci.org/precice/systemtests/jobs/641972706) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/161) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/pull/157) 

---
Last 100 lines of the job log at the moment of push:
```
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:06252bc2:start=1580036927781462634,finish=1580036927786443537,duration=4980903,event=show_system_info[0Ktravis_time:start:0daf4058[0Ktravis_time:end:0daf4058:start=1580036927789469483,finish=1580036927812515874,duration=23046391,event=rm_riak_source[0Ktravis_time:start:0635c588[0Ktravis_time:end:0635c588:start=1580036927815284702,finish=1580036927820535077,duration=5250375,event=fix_rwky_redis[0Ktravis_time:start:0d24c96c[0Ktravis_time:end:0d24c96c:start=1580036927824777234,finish=1580036928321225557,duration=496448323,event=wait_for_network[0Ktravis_time:start:11f6ce54[0Ktravis_time:end:11f6ce54:start=1580036928324875587,finish=1580036929550323106,duration=1225447519,event=update_apt_keys[0Ktravis_time:start:0d406fa3[0Ktravis_time:end:0d406fa3:start=1580036929553999631,finish=1580036930428139379,duration=874139748,event=fix_hhvm_source[0Ktravis_time:start:199275aa[0Ktravis_time:end:199275aa:start=1580036930433126623,finish=1580036930444047554,duration=10920931,event=update_mongo_arch[0Ktravis_time:start:03358c9f[0Ktravis_time:end:03358c9f:start=1580036930448314863,finish=1580036930485836406,duration=37521543,event=fix_sudo_enabled_trusty[0Ktravis_time:start:036553a1[0Ktravis_time:end:036553a1:start=1580036930489694688,finish=1580036930492710742,duration=3016054,event=update_glibc[0Ktravis_time:start:18bcd484[0Ktravis_time:end:18bcd484:start=1580036930496680108,finish=1580036930511625031,duration=14944923,event=clean_up_path[0Ktravis_time:start:05b2c23c[0Ktravis_time:end:05b2c23c:start=1580036930515526457,finish=1580036930523029311,duration=7502854,event=fix_resolv_conf[0Ktravis_time:start:039f7952[0Ktravis_time:end:039f7952:start=1580036930527498207,finish=1580036930538439100,duration=10940893,event=fix_etc_hosts[0Ktravis_time:start:0a1c32e1[0Ktravis_time:end:0a1c32e1:start=1580036930542363157,finish=1580036930551479715,duration=9116558,event=fix_mvn_settings_xml[0Ktravis_time:start:001f8eaf[0Ktravis_time:end:001f8eaf:start=1580036930556153830,finish=1580036930564916033,duration=8762203,event=no_ipv6_localhost[0Ktravis_time:start:011be408[0Ktravis_time:end:011be408:start=1580036930569791104,finish=1580036930573249755,duration=3458651,event=fix_etc_mavenrc[0Ktravis_time:start:0eb49454[0Ktravis_time:end:0eb49454:start=1580036930577911283,finish=1580036930581476914,duration=3565631,event=fix_wwdr_certificate[0Ktravis_time:start:2824e2d0[0Ktravis_time:end:2824e2d0:start=1580036930585911791,finish=1580036930610140043,duration=24228252,event=put_localhost_first[0Ktravis_time:start:1df12754[0Ktravis_time:end:1df12754:start=1580036930614606876,finish=1580036930617870941,duration=3264065,event=home_paths[0Ktravis_time:start:07fd96e6[0Ktravis_time:end:07fd96e6:start=1580036930622694307,finish=1580036930632612355,duration=9918048,event=disable_initramfs[0Ktravis_time:start:0af85fe8[0Ktravis_time:end:0af85fe8:start=1580036930636871670,finish=1580036930828943374,duration=192071704,event=disable_ssh_roaming[0Ktravis_time:start:23d649bc[0Ktravis_time:end:23d649bc:start=1580036930833653795,finish=1580036930836402993,duration=2749198,event=debug_tools[0Ktravis_time:start:106ce3c0[0Ktravis_time:end:106ce3c0:start=1580036930842867481,finish=1580036930846344918,duration=3477437,event=uninstall_oclint[0Ktravis_time:start:2294d10a[0Ktravis_time:end:2294d10a:start=1580036930850891806,finish=1580036930855465330,duration=4573524,event=rvm_use[0Ktravis_time:start:0436b129[0Ktravis_time:end:0436b129:start=1580036930860151059,finish=1580036930869229832,duration=9078773,event=rm_etc_boto_cfg[0Ktravis_time:start:0eda91ca[0Ktravis_time:end:0eda91ca:start=1580036930876754404,finish=1580036930879719305,duration=2964901,event=rm_oraclejdk8_symlink[0Ktravis_time:start:254e4d91[0Ktravis_time:end:254e4d91:start=1580036930884047324,finish=1580036930938099074,duration=54051750,event=enable_i386[0Ktravis_time:start:033104d9[0Ktravis_time:end:033104d9:start=1580036930942920605,finish=1580036930947998745,duration=5078140,event=update_rubygems[0Ktravis_time:start:1d619204[0Ktravis_time:end:1d619204:start=1580036930952419459,finish=1580036931838589209,duration=886169750,event=ensure_path_components[0Ktravis_time:start:107503b8[0Ktravis_time:end:107503b8:start=1580036931842798511,finish=1580036931845391462,duration=2592951,event=redefine_curl[0Ktravis_time:start:0378f610[0Ktravis_time:end:0378f610:start=1580036931848904901,finish=1580036931893819056,duration=44914155,event=nonblock_pipe[0Ktravis_time:start:0ddb3d16[0Ktravis_time:end:0ddb3d16:start=1580036931898196615,finish=1580036937927999935,duration=6029803320,event=apt_get_update[0Ktravis_time:start:1fd72ee8[0Ktravis_time:end:1fd72ee8:start=1580036937932584399,finish=1580036937935269821,duration=2685422,event=deprecate_xcode_64[0Ktravis_time:start:0de03549[0Ktravis_time:end:0de03549:start=1580036937939566334,finish=1580036941481151904,duration=3541585570,event=update_heroku[0Ktravis_time:start:074ff190[0Ktravis_time:end:074ff190:start=1580036941484545414,finish=1580036941486798403,duration=2252989,event=shell_session_update[0Ktravis_time:start:065a02d4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3976
travis_fold:end:docker_mtu[0Ktravis_time:end:065a02d4:start=1580036941489875864,finish=1580036942682924494,duration=1193048630,event=set_docker_mtu[0Ktravis_time:start:03a0d8e1[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03a0d8e1:start=1580036942687545641,finish=1580036942746425633,duration=58879992,event=resolvconf[0Ktravis_time:start:29327124[0Ktravis_time:end:29327124:start=1580036942750817404,finish=1580036942824117321,duration=73299917,event=maven_central_mirror[0Ktravis_time:start:16da4b0c[0Ktravis_time:end:16da4b0c:start=1580036942829387709,finish=1580036942889878957,duration=60491248,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:228f2e58[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:228f2e58:start=1580036942958823926,finish=1580036943445452809,duration=486628883,event=configure[0Ktravis_time:start:1eb8fd35[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1eb8fd35:start=1580036943450466199,finish=1580036951488814919,duration=8038348720,event=configure[0Ktravis_time:start:2737e7bf[0Ktravis_fold:start:services[0Ktravis_time:start:22bc7f0e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:22bc7f0e:start=1580036951511405341,finish=1580036951523521999,duration=12116658,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:22bc7f0e:start=1580036951511405341,finish=1580036954528261893,duration=3016856552,event=services[0Ktravis_time:start:13d32d34[0Ktravis_time:end:13d32d34:start=1580036954532399195,finish=1580036954535133030,duration=2733835,event=fix_ps4[0Ktravis_time:start:2c2e8b5c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:14840340[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:14840340:start=1580036954542826239,finish=1580036959805128782,duration=5262302543,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:1cab536c[0K$ git fetch origin +refs/pull/161/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/161/merge -> FETCH_HEAD
travis_time:end:1cab536c:start=1580036959810282327,finish=1580036960286552510,duration=476270183,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:1cab536c:start=1580036959810282327,finish=1580036961064765005,duration=1254482678,event=checkout[0Ktravis_time:start:087b4024[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:087b4024:start=1580036961070266328,finish=1580036961080630372,duration=10364044,event=env[0Ktravis_time:start:002b836f[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:002b836f:start=1580036961085132355,finish=1580036961090700393,duration=5568038,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00f8f550[0K$ python system_testing.py -s of-of
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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ab232f3ec4153d1e6e56dc63acc9ebce94d07174940d32a6b37e4e1c545878e8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B
```
[
Full job log](https://api.travis-ci.org/v3/job/641972706/log.txt)