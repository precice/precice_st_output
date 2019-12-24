## Status: Failure 
Build: [1360](https://travis-ci.org/precice/systemtests/builds/629054356) 

Job: [1360.23](https://travis-ci.org/precice/systemtests/jobs/629054385) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

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
travis_time:end:12d79757:start=1577186773036734573,finish=1577186773041370297,duration=4635724,event=show_system_info[0Ktravis_time:start:1efb8cc0[0Ktravis_time:end:1efb8cc0:start=1577186773043891346,finish=1577186773061745780,duration=17854434,event=rm_riak_source[0Ktravis_time:start:23885e86[0Ktravis_time:end:23885e86:start=1577186773064800756,finish=1577186773072124765,duration=7324009,event=fix_rwky_redis[0Ktravis_time:start:033d39ea[0Ktravis_time:end:033d39ea:start=1577186773075488687,finish=1577186773404496132,duration=329007445,event=wait_for_network[0Ktravis_time:start:00108bd0[0Ktravis_time:end:00108bd0:start=1577186773410098685,finish=1577186774752987874,duration=1342889189,event=update_apt_keys[0Ktravis_time:start:049054a3[0Ktravis_time:end:049054a3:start=1577186774756866660,finish=1577186775603597803,duration=846731143,event=fix_hhvm_source[0Ktravis_time:start:0d40454c[0Ktravis_time:end:0d40454c:start=1577186775607594699,finish=1577186775616895019,duration=9300320,event=update_mongo_arch[0Ktravis_time:start:301ff4e8[0Ktravis_time:end:301ff4e8:start=1577186775621116554,finish=1577186775657047400,duration=35930846,event=fix_sudo_enabled_trusty[0Ktravis_time:start:00f6fe3d[0Ktravis_time:end:00f6fe3d:start=1577186775661141347,finish=1577186775663698417,duration=2557070,event=update_glibc[0Ktravis_time:start:2b295c5e[0Ktravis_time:end:2b295c5e:start=1577186775667250665,finish=1577186775676289960,duration=9039295,event=clean_up_path[0Ktravis_time:start:11e2d820[0Ktravis_time:end:11e2d820:start=1577186775679438720,finish=1577186775690186015,duration=10747295,event=fix_resolv_conf[0Ktravis_time:start:012770c6[0Ktravis_time:end:012770c6:start=1577186775693808612,finish=1577186775707102003,duration=13293391,event=fix_etc_hosts[0Ktravis_time:start:0204c512[0Ktravis_time:end:0204c512:start=1577186775710666969,finish=1577186775718393686,duration=7726717,event=fix_mvn_settings_xml[0Ktravis_time:start:2e92f0f6[0Ktravis_time:end:2e92f0f6:start=1577186775722098197,finish=1577186775731068302,duration=8970105,event=no_ipv6_localhost[0Ktravis_time:start:1351ebe2[0Ktravis_time:end:1351ebe2:start=1577186775734921510,finish=1577186775737177263,duration=2255753,event=fix_etc_mavenrc[0Ktravis_time:start:02f0e2c4[0Ktravis_time:end:02f0e2c4:start=1577186775741153201,finish=1577186775744481560,duration=3328359,event=fix_wwdr_certificate[0Ktravis_time:start:0933d21e[0Ktravis_time:end:0933d21e:start=1577186775750358044,finish=1577186775771166747,duration=20808703,event=put_localhost_first[0Ktravis_time:start:1b158ec3[0Ktravis_time:end:1b158ec3:start=1577186775775553673,finish=1577186775778730550,duration=3176877,event=home_paths[0Ktravis_time:start:080944fa[0Ktravis_time:end:080944fa:start=1577186775783247444,finish=1577186775794654054,duration=11406610,event=disable_initramfs[0Ktravis_time:start:2bb115bf[0Ktravis_time:end:2bb115bf:start=1577186775798319366,finish=1577186775974310452,duration=175991086,event=disable_ssh_roaming[0Ktravis_time:start:21f21054[0Ktravis_time:end:21f21054:start=1577186775977566491,finish=1577186775979973699,duration=2407208,event=debug_tools[0Ktravis_time:start:1c7b0d3a[0Ktravis_time:end:1c7b0d3a:start=1577186775983121054,finish=1577186775986299236,duration=3178182,event=uninstall_oclint[0Ktravis_time:start:048f66fe[0Ktravis_time:end:048f66fe:start=1577186775989379337,finish=1577186775992458079,duration=3078742,event=rvm_use[0Ktravis_time:start:001a7f00[0Ktravis_time:end:001a7f00:start=1577186775995615522,finish=1577186776009690984,duration=14075462,event=rm_etc_boto_cfg[0Ktravis_time:start:028c27a0[0Ktravis_time:end:028c27a0:start=1577186776013620543,finish=1577186776016037860,duration=2417317,event=rm_oraclejdk8_symlink[0Ktravis_time:start:03636d38[0Ktravis_time:end:03636d38:start=1577186776020230231,finish=1577186776074441810,duration=54211579,event=enable_i386[0Ktravis_time:start:0016687e[0Ktravis_time:end:0016687e:start=1577186776078321532,finish=1577186776082315076,duration=3993544,event=update_rubygems[0Ktravis_time:start:06e12472[0Ktravis_time:end:06e12472:start=1577186776085843987,finish=1577186776927149096,duration=841305109,event=ensure_path_components[0Ktravis_time:start:0ea7eb3a[0Ktravis_time:end:0ea7eb3a:start=1577186776932122169,finish=1577186776934871339,duration=2749170,event=redefine_curl[0Ktravis_time:start:01fe9930[0Ktravis_time:end:01fe9930:start=1577186776939454931,finish=1577186776983987748,duration=44532817,event=nonblock_pipe[0Ktravis_time:start:1aaf5628[0Ktravis_time:end:1aaf5628:start=1577186776988547531,finish=1577186783021545607,duration=6032998076,event=apt_get_update[0Ktravis_time:start:08c431fc[0Ktravis_time:end:08c431fc:start=1577186783025647863,finish=1577186783028306237,duration=2658374,event=deprecate_xcode_64[0Ktravis_time:start:038ce1fc[0Ktravis_time:end:038ce1fc:start=1577186783032054337,finish=1577186786330859544,duration=3298805207,event=update_heroku[0Ktravis_time:start:32e298d0[0Ktravis_time:end:32e298d0:start=1577186786335025390,finish=1577186786337389851,duration=2364461,event=shell_session_update[0Ktravis_time:start:1b1e1c8c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3907
travis_fold:end:docker_mtu[0Ktravis_time:end:1b1e1c8c:start=1577186786341380496,finish=1577186787524506805,duration=1183126309,event=set_docker_mtu[0Ktravis_time:start:14c6c0e8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:14c6c0e8:start=1577186787527706991,finish=1577186787582432487,duration=54725496,event=resolvconf[0Ktravis_time:start:1f72f500[0Ktravis_time:end:1f72f500:start=1577186787585787220,finish=1577186787660162931,duration=74375711,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0265fe44[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0265fe44:start=1577186787731032601,finish=1577186788163778371,duration=432745770,event=configure[0Ktravis_time:start:084cec56[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:084cec56:start=1577186788168022649,finish=1577186796161629688,duration=7993607039,event=configure[0Ktravis_time:start:2560e1a4[0Ktravis_fold:start:services[0Ktravis_time:start:08b7d540[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08b7d540:start=1577186796183649608,finish=1577186796195494864,duration=11845256,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08b7d540:start=1577186796183649608,finish=1577186799201663657,duration=3018014049,event=services[0Ktravis_time:start:1738bcac[0Ktravis_time:end:1738bcac:start=1577186799205714115,finish=1577186799208066138,duration=2352023,event=fix_ps4[0Ktravis_time:start:005e72ec[0K
travis_fold:start:git.checkout[0Ktravis_time:start:167d4e00[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:167d4e00:start=1577186799215897969,finish=1577186804350253834,duration=5134355865,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 968fe698268820917cf52199d2d3dcbaaf61fbaf
travis_fold:end:git.checkout[0K
travis_time:end:167d4e00:start=1577186799215897969,finish=1577186804633454256,duration=5417556287,event=checkout[0Ktravis_time:start:175c49a7[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:175c49a7:start=1577186804637665962,finish=1577186804645612291,duration=7946329,event=env[0Ktravis_time:start:3109cde0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:3109cde0:start=1577186804649537945,finish=1577186804654842133,duration=5304188,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:145fb6ca[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:7c92a2c6bbcb6b6beff92d0a940779769c2477b807c202954c537e2e0deb9bed
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:164e164435f8b470b0a42c8de4ccf6a8a760373ebebaf061ccea3235cb13a096
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/629054385/log.txt)