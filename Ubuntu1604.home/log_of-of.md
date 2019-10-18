## Status: Passing 
Build: [982](https://travis-ci.org/precice/systemtests/builds/599837428) 

Job: [982.14](https://travis-ci.org/precice/systemtests/jobs/599837442) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5939c36bf85d...26213e77ad5d) 

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
travis_time:end:0d67c954:start=1571441367214552762,finish=1571441367221098414,duration=6545652,event=show_system_info[0Ktravis_time:start:36e37160[0Ktravis_time:end:36e37160:start=1571441367224267489,finish=1571441367248091657,duration=23824168,event=rm_riak_source[0Ktravis_time:start:0003672c[0Ktravis_time:end:0003672c:start=1571441367251708386,finish=1571441367257463082,duration=5754696,event=fix_rwky_redis[0Ktravis_time:start:12157a4f[0Ktravis_time:end:12157a4f:start=1571441367262825218,finish=1571441367639023812,duration=376198594,event=wait_for_network[0Ktravis_time:start:0539fe68[0Ktravis_time:end:0539fe68:start=1571441367644406921,finish=1571441369249943271,duration=1605536350,event=update_apt_keys[0Ktravis_time:start:32449256[0Ktravis_time:end:32449256:start=1571441369254369071,finish=1571441370308681746,duration=1054312675,event=fix_hhvm_source[0Ktravis_time:start:119d5ab4[0Ktravis_time:end:119d5ab4:start=1571441370312866362,finish=1571441370324232720,duration=11366358,event=update_mongo_arch[0Ktravis_time:start:0f0865c7[0Ktravis_time:end:0f0865c7:start=1571441370328426517,finish=1571441370374244895,duration=45818378,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1341f8c1[0Ktravis_time:end:1341f8c1:start=1571441370379159522,finish=1571441370382050770,duration=2891248,event=update_glibc[0Ktravis_time:start:159c68f4[0Ktravis_time:end:159c68f4:start=1571441370388013718,finish=1571441370397786581,duration=9772863,event=clean_up_path[0Ktravis_time:start:051a307d[0Ktravis_time:end:051a307d:start=1571441370402920747,finish=1571441370413355399,duration=10434652,event=fix_resolv_conf[0Ktravis_time:start:01a7e7f9[0Ktravis_time:end:01a7e7f9:start=1571441370418748009,finish=1571441370430094278,duration=11346269,event=fix_etc_hosts[0Ktravis_time:start:02c598cc[0Ktravis_time:end:02c598cc:start=1571441370435306716,finish=1571441370445772639,duration=10465923,event=fix_mvn_settings_xml[0Ktravis_time:start:06092268[0Ktravis_time:end:06092268:start=1571441370449845712,finish=1571441370462605792,duration=12760080,event=no_ipv6_localhost[0Ktravis_time:start:24a92cdc[0Ktravis_time:end:24a92cdc:start=1571441370467416104,finish=1571441370470856290,duration=3440186,event=fix_etc_mavenrc[0Ktravis_time:start:2cd79d09[0Ktravis_time:end:2cd79d09:start=1571441370476476777,finish=1571441370480263675,duration=3786898,event=fix_wwdr_certificate[0Ktravis_time:start:0747eca2[0Ktravis_time:end:0747eca2:start=1571441370485170905,finish=1571441370511630169,duration=26459264,event=put_localhost_first[0Ktravis_time:start:035f3179[0Ktravis_time:end:035f3179:start=1571441370516429574,finish=1571441370521015609,duration=4586035,event=home_paths[0Ktravis_time:start:00698d12[0Ktravis_time:end:00698d12:start=1571441370525709693,finish=1571441370539327174,duration=13617481,event=disable_initramfs[0Ktravis_time:start:02fbec36[0Ktravis_time:end:02fbec36:start=1571441370544515468,finish=1571441370842949574,duration=298434106,event=disable_ssh_roaming[0Ktravis_time:start:0304d3f1[0Ktravis_time:end:0304d3f1:start=1571441370847893652,finish=1571441370850858393,duration=2964741,event=debug_tools[0Ktravis_time:start:0044f6f0[0Ktravis_time:end:0044f6f0:start=1571441370856053679,finish=1571441370860038780,duration=3985101,event=uninstall_oclint[0Ktravis_time:start:017b0d0a[0Ktravis_time:end:017b0d0a:start=1571441370864586535,finish=1571441370870822493,duration=6235958,event=rvm_use[0Ktravis_time:start:0d8c9315[0Ktravis_time:end:0d8c9315:start=1571441370875394037,finish=1571441370883864227,duration=8470190,event=rm_etc_boto_cfg[0Ktravis_time:start:002c4f5d[0Ktravis_time:end:002c4f5d:start=1571441370888623844,finish=1571441370892932844,duration=4309000,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0063a0f0[0Ktravis_time:end:0063a0f0:start=1571441370897459290,finish=1571441370953506727,duration=56047437,event=enable_i386[0Ktravis_time:start:1251d5da[0Ktravis_time:end:1251d5da:start=1571441370958874078,finish=1571441370963483420,duration=4609342,event=update_rubygems[0Ktravis_time:start:02854f50[0Ktravis_time:end:02854f50:start=1571441370968384289,finish=1571441372003754841,duration=1035370552,event=ensure_path_components[0Ktravis_time:start:202e5b38[0Ktravis_time:end:202e5b38:start=1571441372009601753,finish=1571441372013152287,duration=3550534,event=redefine_curl[0Ktravis_time:start:054220a8[0Ktravis_time:end:054220a8:start=1571441372017372777,finish=1571441372070668971,duration=53296194,event=nonblock_pipe[0Ktravis_time:start:13098da8[0Ktravis_time:end:13098da8:start=1571441372075604112,finish=1571441372140495288,duration=64891176,event=apt_get_update[0Ktravis_time:start:0346e783[0Ktravis_time:end:0346e783:start=1571441372145195144,finish=1571441372148018027,duration=2822883,event=deprecate_xcode_64[0Ktravis_time:start:337a114e[0Ktravis_time:end:337a114e:start=1571441372152549125,finish=1571441376730086316,duration=4577537191,event=update_heroku[0Ktravis_time:start:024e2d7a[0Ktravis_time:end:024e2d7a:start=1571441376734914429,finish=1571441376737844806,duration=2930377,event=shell_session_update[0Ktravis_time:start:16c35f30[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3959
travis_fold:end:docker_mtu[0Ktravis_time:end:16c35f30:start=1571441376741596157,finish=1571441377937009303,duration=1195413146,event=set_docker_mtu[0Ktravis_time:start:220f9f7e[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:220f9f7e:start=1571441377941807748,finish=1571441378013080427,duration=71272679,event=resolvconf[0Ktravis_time:start:0a8322aa[0Ktravis_time:end:0a8322aa:start=1571441378018567181,finish=1571441378124335730,duration=105768549,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:013d1d4d[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:013d1d4d:start=1571441378211649812,finish=1571441378682379934,duration=470730122,event=configure[0Ktravis_time:start:086a8352[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:086a8352:start=1571441378688032896,finish=1571441388846803262,duration=10158770366,event=configure[0Ktravis_time:start:02ff875e[0Ktravis_fold:start:services[0Ktravis_time:start:016060f8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:016060f8:start=1571441388873206302,finish=1571441388888063211,duration=14856909,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:016060f8:start=1571441388873206302,finish=1571441391894957272,duration=3021750970,event=services[0Ktravis_time:start:02bc122f[0Ktravis_time:end:02bc122f:start=1571441391900738193,finish=1571441391903632875,duration=2894682,event=fix_ps4[0Ktravis_time:start:0afe79f4[0K
travis_fold:start:git.checkout[0Ktravis_time:start:18bcac35[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:18bcac35:start=1571441391911611405,finish=1571441398105099488,duration=6193488083,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 26213e77ad5d4262d59179ab7deb34279ed0b034
travis_fold:end:git.checkout[0K
travis_time:end:18bcac35:start=1571441391911611405,finish=1571441398183467082,duration=6271855677,event=checkout[0Ktravis_time:start:23c40db2[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:23c40db2:start=1571441398188234598,finish=1571441398201244606,duration=13010008,event=env[0Ktravis_time:start:031ca37e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:031ca37e:start=1571441398207008015,finish=1571441398213723556,duration=6715541,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0e012a20[0K$ python system_testing.py -s of-of
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0cf236788b7b5d560910641f19761ea96d86c59e5d53f118ea87e104e836311f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/599837442/log.txt)