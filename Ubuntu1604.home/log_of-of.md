## Status: Passing 
Build: [1059](https://travis-ci.org/precice/systemtests/builds/608519809) 

Job: [1059.18](https://travis-ci.org/precice/systemtests/jobs/608519827) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

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
travis_time:end:092d0bdb:start=1573094559233328214,finish=1573094559239055384,duration=5727170,event=show_system_info[0Ktravis_time:start:1297da58[0Ktravis_time:end:1297da58:start=1573094559242020710,finish=1573094559265696425,duration=23675715,event=rm_riak_source[0Ktravis_time:start:07579844[0Ktravis_time:end:07579844:start=1573094559268849279,finish=1573094559276363894,duration=7514615,event=fix_rwky_redis[0Ktravis_time:start:17aa03e0[0Ktravis_time:end:17aa03e0:start=1573094559279620378,finish=1573094559679028766,duration=399408388,event=wait_for_network[0Ktravis_time:start:05d11c82[0Ktravis_time:end:05d11c82:start=1573094559684316784,finish=1573094561276625065,duration=1592308281,event=update_apt_keys[0Ktravis_time:start:2f19aaae[0Ktravis_time:end:2f19aaae:start=1573094561280946693,finish=1573094562321537630,duration=1040590937,event=fix_hhvm_source[0Ktravis_time:start:1871d76e[0Ktravis_time:end:1871d76e:start=1573094562325977921,finish=1573094562335857941,duration=9880020,event=update_mongo_arch[0Ktravis_time:start:1305e6ab[0Ktravis_time:end:1305e6ab:start=1573094562339968582,finish=1573094562380717195,duration=40748613,event=fix_sudo_enabled_trusty[0Ktravis_time:start:02733558[0Ktravis_time:end:02733558:start=1573094562385614395,finish=1573094562389157143,duration=3542748,event=update_glibc[0Ktravis_time:start:05eec1b8[0Ktravis_time:end:05eec1b8:start=1573094562394479626,finish=1573094562402806876,duration=8327250,event=clean_up_path[0Ktravis_time:start:03b9e6a8[0Ktravis_time:end:03b9e6a8:start=1573094562406853291,finish=1573094562416572976,duration=9719685,event=fix_resolv_conf[0Ktravis_time:start:0f27244e[0Ktravis_time:end:0f27244e:start=1573094562421257665,finish=1573094562432051216,duration=10793551,event=fix_etc_hosts[0Ktravis_time:start:05c42831[0Ktravis_time:end:05c42831:start=1573094562436442337,finish=1573094562447061957,duration=10619620,event=fix_mvn_settings_xml[0Ktravis_time:start:10cda948[0Ktravis_time:end:10cda948:start=1573094562451304932,finish=1573094562462186823,duration=10881891,event=no_ipv6_localhost[0Ktravis_time:start:13834356[0Ktravis_time:end:13834356:start=1573094562467208814,finish=1573094562469869054,duration=2660240,event=fix_etc_mavenrc[0Ktravis_time:start:01a277e4[0Ktravis_time:end:01a277e4:start=1573094562474376068,finish=1573094562478146261,duration=3770193,event=fix_wwdr_certificate[0Ktravis_time:start:2760d0c4[0Ktravis_time:end:2760d0c4:start=1573094562481947530,finish=1573094562510172507,duration=28224977,event=put_localhost_first[0Ktravis_time:start:16f5d530[0Ktravis_time:end:16f5d530:start=1573094562515606039,finish=1573094562519679061,duration=4073022,event=home_paths[0Ktravis_time:start:0dfd4470[0Ktravis_time:end:0dfd4470:start=1573094562525024343,finish=1573094562540905082,duration=15880739,event=disable_initramfs[0Ktravis_time:start:23f5380e[0Ktravis_time:end:23f5380e:start=1573094562545076296,finish=1573094562860325660,duration=315249364,event=disable_ssh_roaming[0Ktravis_time:start:05464b96[0Ktravis_time:end:05464b96:start=1573094562865027282,finish=1573094562868270244,duration=3242962,event=debug_tools[0Ktravis_time:start:2186a7b0[0Ktravis_time:end:2186a7b0:start=1573094562872989543,finish=1573094562877783787,duration=4794244,event=uninstall_oclint[0Ktravis_time:start:144a9b4c[0Ktravis_time:end:144a9b4c:start=1573094562884086178,finish=1573094562887664428,duration=3578250,event=rvm_use[0Ktravis_time:start:185225ac[0Ktravis_time:end:185225ac:start=1573094562892349403,finish=1573094562901117635,duration=8768232,event=rm_etc_boto_cfg[0Ktravis_time:start:053bf240[0Ktravis_time:end:053bf240:start=1573094562907409871,finish=1573094562910413863,duration=3003992,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1b49ebc8[0Ktravis_time:end:1b49ebc8:start=1573094562915494629,finish=1573094562984227006,duration=68732377,event=enable_i386[0Ktravis_time:start:367e2a2b[0Ktravis_time:end:367e2a2b:start=1573094562990598043,finish=1573094562995235915,duration=4637872,event=update_rubygems[0Ktravis_time:start:167a05e8[0Ktravis_time:end:167a05e8:start=1573094563000967543,finish=1573094564008508807,duration=1007541264,event=ensure_path_components[0Ktravis_time:start:26d36b40[0Ktravis_time:end:26d36b40:start=1573094564013917992,finish=1573094564017028011,duration=3110019,event=redefine_curl[0Ktravis_time:start:00b654b1[0Ktravis_time:end:00b654b1:start=1573094564021889839,finish=1573094564078788071,duration=56898232,event=nonblock_pipe[0Ktravis_time:start:335863d4[0Ktravis_time:end:335863d4:start=1573094564084112257,finish=1573094567128149888,duration=3044037631,event=apt_get_update[0Ktravis_time:start:01df9959[0Ktravis_time:end:01df9959:start=1573094567132415251,finish=1573094567135156446,duration=2741195,event=deprecate_xcode_64[0Ktravis_time:start:1710a560[0Ktravis_time:end:1710a560:start=1573094567138874572,finish=1573094571957465179,duration=4818590607,event=update_heroku[0Ktravis_time:start:03443ac9[0Ktravis_time:end:03443ac9:start=1573094571962013978,finish=1573094571964817732,duration=2803754,event=shell_session_update[0Ktravis_time:start:1ee72ca3[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3886
travis_fold:end:docker_mtu[0Ktravis_time:end:1ee72ca3:start=1573094571969799360,finish=1573094573169213562,duration=1199414202,event=set_docker_mtu[0Ktravis_time:start:236beaf0[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:236beaf0:start=1573094573173832381,finish=1573094573238863659,duration=65031278,event=resolvconf[0Ktravis_time:start:0ff4ceb4[0Ktravis_time:end:0ff4ceb4:start=1573094573243345376,finish=1573094573338374959,duration=95029583,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1be3899c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1be3899c:start=1573094573424661452,finish=1573094574437338498,duration=1012677046,event=configure[0Ktravis_time:start:039487c7[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:039487c7:start=1573094574442795438,finish=1573094584437277986,duration=9994482548,event=configure[0Ktravis_time:start:0016705c[0Ktravis_fold:start:services[0Ktravis_time:start:0d8cc0b2[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0d8cc0b2:start=1573094584463169450,finish=1573094584477745131,duration=14575681,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0d8cc0b2:start=1573094584463169450,finish=1573094587484914163,duration=3021744713,event=services[0Ktravis_time:start:1ba0e5b2[0Ktravis_time:end:1ba0e5b2:start=1573094587489957328,finish=1573094587492651177,duration=2693849,event=fix_ps4[0Ktravis_time:start:03a43eb8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:230e0990[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:230e0990:start=1573094587501151448,finish=1573094593737166775,duration=6236015327,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:230e0990:start=1573094587501151448,finish=1573094594409297384,duration=6908145936,event=checkout[0Ktravis_time:start:0310d814[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0310d814:start=1573094594413940961,finish=1573094594425641240,duration=11700279,event=env[0Ktravis_time:start:0f0410ac[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0f0410ac:start=1573094594433354986,finish=1573094594439150111,duration=5795125,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0332161e[0K$ python system_testing.py -s of-of
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
Digest: sha256:d472ecf92550f3e4c0d9a2fa3aebe24121d0c77410191a820853bd326e430cf0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/608519827/log.txt)