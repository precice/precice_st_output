## Status: Passing 
Build: [1023](https://travis-ci.org/precice/systemtests/builds/602890333) 

Job: [1023.20](https://travis-ci.org/precice/systemtests/jobs/602890354) 

Triggered by: [push](https://github.com/precice/systemtests/compare/14ba7f611330...9921a3e9e3f7) 

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
travis_time:end:00f2e366:start=1572022128654357698,finish=1572022128660543137,duration=6185439,event=show_system_info[0Ktravis_time:start:2e5490d4[0Ktravis_time:end:2e5490d4:start=1572022128663787732,finish=1572022128686528730,duration=22740998,event=rm_riak_source[0Ktravis_time:start:053b0950[0Ktravis_time:end:053b0950:start=1572022128690039885,finish=1572022128695600709,duration=5560824,event=fix_rwky_redis[0Ktravis_time:start:1846271d[0Ktravis_time:end:1846271d:start=1572022128698883407,finish=1572022129088366122,duration=389482715,event=wait_for_network[0Ktravis_time:start:07cf9866[0Ktravis_time:end:07cf9866:start=1572022129092439387,finish=1572022130121583847,duration=1029144460,event=update_apt_keys[0Ktravis_time:start:0ed93273[0Ktravis_time:end:0ed93273:start=1572022130125992509,finish=1572022131162230651,duration=1036238142,event=fix_hhvm_source[0Ktravis_time:start:02f9aef5[0Ktravis_time:end:02f9aef5:start=1572022131167454048,finish=1572022131179410565,duration=11956517,event=update_mongo_arch[0Ktravis_time:start:0df8bee8[0Ktravis_time:end:0df8bee8:start=1572022131184806777,finish=1572022131229287155,duration=44480378,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0001be92[0Ktravis_time:end:0001be92:start=1572022131234827675,finish=1572022131238043972,duration=3216297,event=update_glibc[0Ktravis_time:start:214f1911[0Ktravis_time:end:214f1911:start=1572022131242962510,finish=1572022131254411778,duration=11449268,event=clean_up_path[0Ktravis_time:start:090f7824[0Ktravis_time:end:090f7824:start=1572022131259401575,finish=1572022131268172871,duration=8771296,event=fix_resolv_conf[0Ktravis_time:start:2cecd700[0Ktravis_time:end:2cecd700:start=1572022131275441443,finish=1572022131285848109,duration=10406666,event=fix_etc_hosts[0Ktravis_time:start:1c6b28a5[0Ktravis_time:end:1c6b28a5:start=1572022131290250726,finish=1572022131300076179,duration=9825453,event=fix_mvn_settings_xml[0Ktravis_time:start:045534aa[0Ktravis_time:end:045534aa:start=1572022131306756910,finish=1572022131319004139,duration=12247229,event=no_ipv6_localhost[0Ktravis_time:start:07518de6[0Ktravis_time:end:07518de6:start=1572022131324040688,finish=1572022131327473996,duration=3433308,event=fix_etc_mavenrc[0Ktravis_time:start:1266d980[0Ktravis_time:end:1266d980:start=1572022131332612634,finish=1572022131338015686,duration=5403052,event=fix_wwdr_certificate[0Ktravis_time:start:2bf0d0f4[0Ktravis_time:end:2bf0d0f4:start=1572022131344152802,finish=1572022131370743785,duration=26590983,event=put_localhost_first[0Ktravis_time:start:1f14dba8[0Ktravis_time:end:1f14dba8:start=1572022131375953798,finish=1572022131379752612,duration=3798814,event=home_paths[0Ktravis_time:start:0b90913e[0Ktravis_time:end:0b90913e:start=1572022131386061275,finish=1572022131400073859,duration=14012584,event=disable_initramfs[0Ktravis_time:start:1add04f1[0Ktravis_time:end:1add04f1:start=1572022131405054153,finish=1572022131835630364,duration=430576211,event=disable_ssh_roaming[0Ktravis_time:start:0aef6aec[0Ktravis_time:end:0aef6aec:start=1572022131841768036,finish=1572022131845753898,duration=3985862,event=debug_tools[0Ktravis_time:start:137c6cd6[0Ktravis_time:end:137c6cd6:start=1572022131850524768,finish=1572022131854156791,duration=3632023,event=uninstall_oclint[0Ktravis_time:start:0aaa89fd[0Ktravis_time:end:0aaa89fd:start=1572022131859559606,finish=1572022131863636214,duration=4076608,event=rvm_use[0Ktravis_time:start:208b7ed2[0Ktravis_time:end:208b7ed2:start=1572022131869911289,finish=1572022131880688346,duration=10777057,event=rm_etc_boto_cfg[0Ktravis_time:start:17373afb[0Ktravis_time:end:17373afb:start=1572022131887277359,finish=1572022131890564469,duration=3287110,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0d6a4ee8[0Ktravis_time:end:0d6a4ee8:start=1572022131897261321,finish=1572022131968108198,duration=70846877,event=enable_i386[0Ktravis_time:start:014faf00[0Ktravis_time:end:014faf00:start=1572022131973824170,finish=1572022131978273277,duration=4449107,event=update_rubygems[0Ktravis_time:start:03540b7f[0Ktravis_time:end:03540b7f:start=1572022131982602681,finish=1572022133012974946,duration=1030372265,event=ensure_path_components[0Ktravis_time:start:35fa1770[0Ktravis_time:end:35fa1770:start=1572022133018147420,finish=1572022133021003733,duration=2856313,event=redefine_curl[0Ktravis_time:start:02440b04[0Ktravis_time:end:02440b04:start=1572022133026022735,finish=1572022133080808705,duration=54785970,event=nonblock_pipe[0Ktravis_time:start:02e9e920[0Ktravis_time:end:02e9e920:start=1572022133085807318,finish=1572022136133552866,duration=3047745548,event=apt_get_update[0Ktravis_time:start:13562d9c[0Ktravis_time:end:13562d9c:start=1572022136139098825,finish=1572022136142214049,duration=3115224,event=deprecate_xcode_64[0Ktravis_time:start:2195f4f0[0Ktravis_time:end:2195f4f0:start=1572022136147415395,finish=1572022140876519277,duration=4729103882,event=update_heroku[0Ktravis_time:start:03cd5984[0Ktravis_time:end:03cd5984:start=1572022140881584775,finish=1572022140884395224,duration=2810449,event=shell_session_update[0Ktravis_time:start:2446bef8[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3865
travis_fold:end:docker_mtu[0Ktravis_time:end:2446bef8:start=1572022140888786043,finish=1572022142085993965,duration=1197207922,event=set_docker_mtu[0Ktravis_time:start:144fc10a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:144fc10a:start=1572022142090733468,finish=1572022142155238472,duration=64505004,event=resolvconf[0Ktravis_time:start:02b46db1[0Ktravis_time:end:02b46db1:start=1572022142160525322,finish=1572022142262113280,duration=101587958,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:07414a9e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:07414a9e:start=1572022142344341192,finish=1572022142648541906,duration=304200714,event=configure[0Ktravis_time:start:0a3b312f[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a3b312f:start=1572022142653929081,finish=1572022152366235356,duration=9712306275,event=configure[0Ktravis_time:start:2e4b3e98[0Ktravis_fold:start:services[0Ktravis_time:start:28389384[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:28389384:start=1572022152391444758,finish=1572022152405845946,duration=14401188,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:28389384:start=1572022152391444758,finish=1572022155411486167,duration=3020041409,event=services[0Ktravis_time:start:1c9939f0[0Ktravis_time:end:1c9939f0:start=1572022155416247581,finish=1572022155419100722,duration=2853141,event=fix_ps4[0Ktravis_time:start:0eaa752e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:167712cc[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:167712cc:start=1572022155427501562,finish=1572022161724120308,duration=6296618746,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 9921a3e9e3f7596df67493847bbc01f17a3b226e
travis_fold:end:git.checkout[0K
travis_time:end:167712cc:start=1572022155427501562,finish=1572022162357004622,duration=6929503060,event=checkout[0Ktravis_time:start:00ebc200[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00ebc200:start=1572022162361838830,finish=1572022162371725284,duration=9886454,event=env[0Ktravis_time:start:03bfd2ec[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03bfd2ec:start=1572022162376384783,finish=1572022162382134912,duration=5750129,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:27b2ef9f[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:d1528af363df954e5a3be334a2d22d5061e1360a624636367fe2b227c6d1addd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/602890354/log.txt)