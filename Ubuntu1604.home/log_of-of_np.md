## Status: Passing 
Build: [1055](https://travis-ci.org/precice/systemtests/builds/606615476) 

Job: [1055.24](https://travis-ci.org/precice/systemtests/jobs/606615500) 

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
travis_time:end:0c60d710:start=1572749054621746696,finish=1572749054629513053,duration=7766357,event=show_system_info[0Ktravis_time:start:199051ad[0Ktravis_time:end:199051ad:start=1572749054633094403,finish=1572749054659434871,duration=26340468,event=rm_riak_source[0Ktravis_time:start:020ce9df[0Ktravis_time:end:020ce9df:start=1572749054663557069,finish=1572749054671531361,duration=7974292,event=fix_rwky_redis[0Ktravis_time:start:0308edb6[0Ktravis_time:end:0308edb6:start=1572749054675401523,finish=1572749055070847158,duration=395445635,event=wait_for_network[0Ktravis_time:start:19a13460[0Ktravis_time:end:19a13460:start=1572749055079664853,finish=1572749056150855180,duration=1071190327,event=update_apt_keys[0Ktravis_time:start:105a8dc2[0Ktravis_time:end:105a8dc2:start=1572749056155872433,finish=1572749057240070666,duration=1084198233,event=fix_hhvm_source[0Ktravis_time:start:0a6c776f[0Ktravis_time:end:0a6c776f:start=1572749057244724412,finish=1572749057255686112,duration=10961700,event=update_mongo_arch[0Ktravis_time:start:1a073cc0[0Ktravis_time:end:1a073cc0:start=1572749057261152400,finish=1572749057307944592,duration=46792192,event=fix_sudo_enabled_trusty[0Ktravis_time:start:04bc27f2[0Ktravis_time:end:04bc27f2:start=1572749057313227446,finish=1572749057316157522,duration=2930076,event=update_glibc[0Ktravis_time:start:0aff67c4[0Ktravis_time:end:0aff67c4:start=1572749057321131435,finish=1572749057331639119,duration=10507684,event=clean_up_path[0Ktravis_time:start:176c5590[0Ktravis_time:end:176c5590:start=1572749057336217561,finish=1572749057345897944,duration=9680383,event=fix_resolv_conf[0Ktravis_time:start:1901e7fd[0Ktravis_time:end:1901e7fd:start=1572749057351775240,finish=1572749057361880178,duration=10104938,event=fix_etc_hosts[0Ktravis_time:start:01398a10[0Ktravis_time:end:01398a10:start=1572749057367780176,finish=1572749057378148396,duration=10368220,event=fix_mvn_settings_xml[0Ktravis_time:start:00b478bb[0Ktravis_time:end:00b478bb:start=1572749057383157699,finish=1572749057394000473,duration=10842774,event=no_ipv6_localhost[0Ktravis_time:start:050f7700[0Ktravis_time:end:050f7700:start=1572749057399753263,finish=1572749057402978509,duration=3225246,event=fix_etc_mavenrc[0Ktravis_time:start:0115f433[0Ktravis_time:end:0115f433:start=1572749057410964682,finish=1572749057415310138,duration=4345456,event=fix_wwdr_certificate[0Ktravis_time:start:17ccab58[0Ktravis_time:end:17ccab58:start=1572749057420007392,finish=1572749057447819973,duration=27812581,event=put_localhost_first[0Ktravis_time:start:07781016[0Ktravis_time:end:07781016:start=1572749057454206203,finish=1572749057458738105,duration=4531902,event=home_paths[0Ktravis_time:start:09deb45e[0Ktravis_time:end:09deb45e:start=1572749057463873826,finish=1572749057477951694,duration=14077868,event=disable_initramfs[0Ktravis_time:start:00255528[0Ktravis_time:end:00255528:start=1572749057482439571,finish=1572749057802337525,duration=319897954,event=disable_ssh_roaming[0Ktravis_time:start:0b2985e1[0Ktravis_time:end:0b2985e1:start=1572749057808140175,finish=1572749057811335918,duration=3195743,event=debug_tools[0Ktravis_time:start:0c1284a4[0Ktravis_time:end:0c1284a4:start=1572749057816448206,finish=1572749057821443575,duration=4995369,event=uninstall_oclint[0Ktravis_time:start:25b9fed0[0Ktravis_time:end:25b9fed0:start=1572749057828468784,finish=1572749057832424900,duration=3956116,event=rvm_use[0Ktravis_time:start:0c3d3360[0Ktravis_time:end:0c3d3360:start=1572749057837064820,finish=1572749057846231038,duration=9166218,event=rm_etc_boto_cfg[0Ktravis_time:start:149cec30[0Ktravis_time:end:149cec30:start=1572749057852088369,finish=1572749057855145717,duration=3057348,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0d9c4188[0Ktravis_time:end:0d9c4188:start=1572749057860030145,finish=1572749057919329531,duration=59299386,event=enable_i386[0Ktravis_time:start:03968868[0Ktravis_time:end:03968868:start=1572749057924824985,finish=1572749057929581852,duration=4756867,event=update_rubygems[0Ktravis_time:start:02a59e2e[0Ktravis_time:end:02a59e2e:start=1572749057935761418,finish=1572749059001063851,duration=1065302433,event=ensure_path_components[0Ktravis_time:start:05db0b84[0Ktravis_time:end:05db0b84:start=1572749059006871479,finish=1572749059010842613,duration=3971134,event=redefine_curl[0Ktravis_time:start:277420a0[0Ktravis_time:end:277420a0:start=1572749059017142386,finish=1572749059078132994,duration=60990608,event=nonblock_pipe[0Ktravis_time:start:046fcd2b[0Ktravis_time:end:046fcd2b:start=1572749059083342634,finish=1572749062159323186,duration=3075980552,event=apt_get_update[0Ktravis_time:start:17b734b0[0Ktravis_time:end:17b734b0:start=1572749062165557936,finish=1572749062169473939,duration=3916003,event=deprecate_xcode_64[0Ktravis_time:start:26fe8db0[0Ktravis_time:end:26fe8db0:start=1572749062175082629,finish=1572749067048808505,duration=4873725876,event=update_heroku[0Ktravis_time:start:032cba44[0Ktravis_time:end:032cba44:start=1572749067054240298,finish=1572749067057239837,duration=2999539,event=shell_session_update[0Ktravis_time:start:035688f0[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3864
travis_fold:end:docker_mtu[0Ktravis_time:end:035688f0:start=1572749067062474556,finish=1572749068262740955,duration=1200266399,event=set_docker_mtu[0Ktravis_time:start:00b95e38[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:00b95e38:start=1572749068267491998,finish=1572749068339772244,duration=72280246,event=resolvconf[0Ktravis_time:start:1cbd1500[0Ktravis_time:end:1cbd1500:start=1572749068344944386,finish=1572749068456268878,duration=111324492,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:33aeb631[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:33aeb631:start=1572749068545548654,finish=1572749068800669010,duration=255120356,event=configure[0Ktravis_time:start:2247aaa0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2247aaa0:start=1572749068806110830,finish=1572749082512076395,duration=13705965565,event=configure[0Ktravis_time:start:26f96f70[0Ktravis_fold:start:services[0Ktravis_time:start:0022e668[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0022e668:start=1572749082541700440,finish=1572749082560849219,duration=19148779,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0022e668:start=1572749082541700440,finish=1572749085567643471,duration=3025943031,event=services[0Ktravis_time:start:0261bacc[0Ktravis_time:end:0261bacc:start=1572749085571851228,finish=1572749085574954204,duration=3102976,event=fix_ps4[0Ktravis_time:start:06509666[0K
travis_fold:start:git.checkout[0Ktravis_time:start:01482147[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:01482147:start=1572749085583528119,finish=1572749091866308487,duration=6282780368,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:01482147:start=1572749085583528119,finish=1572749092702691299,duration=7119163180,event=checkout[0Ktravis_time:start:21d9ed94[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:21d9ed94:start=1572749092707548009,finish=1572749092722216736,duration=14668727,event=env[0Ktravis_time:start:006d461f[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:006d461f:start=1572749092731471204,finish=1572749092739124975,duration=7653771,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1c522614[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:e1ede29dae04cac520d17c81301087123c03455b9bb7251d4b5da0388fc8b489
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/606615500/log.txt)