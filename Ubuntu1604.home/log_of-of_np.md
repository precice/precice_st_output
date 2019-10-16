 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598541158) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/478596e1ce45...2f42d88d1871) 
## Last 100 lines of the job log at the moment of push...
```
   hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:12a20960:start=1571218441319210871,finish=1571218441325127716,duration=5916845,event=show_system_info[0Ktravis_time:start:0b8c2bf0[0Ktravis_time:end:0b8c2bf0:start=1571218441328106411,finish=1571218441354788515,duration=26682104,event=rm_riak_source[0Ktravis_time:start:00240fc5[0Ktravis_time:end:00240fc5:start=1571218441358288068,finish=1571218441369950485,duration=11662417,event=fix_rwky_redis[0Ktravis_time:start:03a58694[0Ktravis_time:end:03a58694:start=1571218441374172908,finish=1571218441796938834,duration=422765926,event=wait_for_network[0Ktravis_time:start:112456bc[0Ktravis_time:end:112456bc:start=1571218441802379159,finish=1571218443385082229,duration=1582703070,event=update_apt_keys[0Ktravis_time:start:07f1a264[0Ktravis_time:end:07f1a264:start=1571218443389405455,finish=1571218444407372108,duration=1017966653,event=fix_hhvm_source[0Ktravis_time:start:0c97e707[0Ktravis_time:end:0c97e707:start=1571218444411698788,finish=1571218444421794242,duration=10095454,event=update_mongo_arch[0Ktravis_time:start:0b36334c[0Ktravis_time:end:0b36334c:start=1571218444425874815,finish=1571218444468259753,duration=42384938,event=fix_sudo_enabled_trusty[0Ktravis_time:start:119cbaa3[0Ktravis_time:end:119cbaa3:start=1571218444474438295,finish=1571218444477359140,duration=2920845,event=update_glibc[0Ktravis_time:start:19e0fe10[0Ktravis_time:end:19e0fe10:start=1571218444482438088,finish=1571218444492336876,duration=9898788,event=clean_up_path[0Ktravis_time:start:24394b48[0Ktravis_time:end:24394b48:start=1571218444496196532,finish=1571218444506773944,duration=10577412,event=fix_resolv_conf[0Ktravis_time:start:03dea145[0Ktravis_time:end:03dea145:start=1571218444510606808,finish=1571218444524084306,duration=13477498,event=fix_etc_hosts[0Ktravis_time:start:0ac13fcd[0Ktravis_time:end:0ac13fcd:start=1571218444527923304,finish=1571218444540542605,duration=12619301,event=fix_mvn_settings_xml[0Ktravis_time:start:02d6ab12[0Ktravis_time:end:02d6ab12:start=1571218444545227610,finish=1571218444556196490,duration=10968880,event=no_ipv6_localhost[0Ktravis_time:start:12ac17a2[0Ktravis_time:end:12ac17a2:start=1571218444561439873,finish=1571218444564089958,duration=2650085,event=fix_etc_mavenrc[0Ktravis_time:start:0e160d59[0Ktravis_time:end:0e160d59:start=1571218444568646850,finish=1571218444572063401,duration=3416551,event=fix_wwdr_certificate[0Ktravis_time:start:04b0d24b[0Ktravis_time:end:04b0d24b:start=1571218444576644185,finish=1571218444603014904,duration=26370719,event=put_localhost_first[0Ktravis_time:start:2948a9d4[0Ktravis_time:end:2948a9d4:start=1571218444607138131,finish=1571218444612026288,duration=4888157,event=home_paths[0Ktravis_time:start:1ae2d955[0Ktravis_time:end:1ae2d955:start=1571218444616506926,finish=1571218444628893545,duration=12386619,event=disable_initramfs[0Ktravis_time:start:112fa9ba[0Ktravis_time:end:112fa9ba:start=1571218444633424064,finish=1571218444892117199,duration=258693135,event=disable_ssh_roaming[0Ktravis_time:start:11df89c4[0Ktravis_time:end:11df89c4:start=1571218444896870192,finish=1571218444899775926,duration=2905734,event=debug_tools[0Ktravis_time:start:068e0ac1[0Ktravis_time:end:068e0ac1:start=1571218444904001583,finish=1571218444908476819,duration=4475236,event=uninstall_oclint[0Ktravis_time:start:001d74a4[0Ktravis_time:end:001d74a4:start=1571218444912677986,finish=1571218444916218321,duration=3540335,event=rvm_use[0Ktravis_time:start:2564e200[0Ktravis_time:end:2564e200:start=1571218444920416073,finish=1571218444931211462,duration=10795389,event=rm_etc_boto_cfg[0Ktravis_time:start:0777dd70[0Ktravis_time:end:0777dd70:start=1571218444935335637,finish=1571218444938014702,duration=2679065,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0a10738a[0Ktravis_time:end:0a10738a:start=1571218444942834232,finish=1571218445006200312,duration=63366080,event=enable_i386[0Ktravis_time:start:142272f3[0Ktravis_time:end:142272f3:start=1571218445010774796,finish=1571218445015393524,duration=4618728,event=update_rubygems[0Ktravis_time:start:0862969a[0Ktravis_time:end:0862969a:start=1571218445019601748,finish=1571218446019566398,duration=999964650,event=ensure_path_components[0Ktravis_time:start:0be09900[0Ktravis_time:end:0be09900:start=1571218446025440540,finish=1571218446028281847,duration=2841307,event=redefine_curl[0Ktravis_time:start:18bf20da[0Ktravis_time:end:18bf20da:start=1571218446032063377,finish=1571218446085647651,duration=53584274,event=nonblock_pipe[0Ktravis_time:start:0b2a8dce[0Ktravis_time:end:0b2a8dce:start=1571218446090068338,finish=1571218446131475499,duration=41407161,event=apt_get_update[0Ktravis_time:start:02b77670[0Ktravis_time:end:02b77670:start=1571218446135732785,finish=1571218446138830194,duration=3097409,event=deprecate_xcode_64[0Ktravis_time:start:17e8fe6d[0Ktravis_time:end:17e8fe6d:start=1571218446143062982,finish=1571218450607834773,duration=4464771791,event=update_heroku[0Ktravis_time:start:029ba4e0[0Ktravis_time:end:029ba4e0:start=1571218450612486498,finish=1571218450615289103,duration=2802605,event=shell_session_update[0Ktravis_time:start:1f5fbf07[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3869
travis_fold:end:docker_mtu[0Ktravis_time:end:1f5fbf07:start=1571218450619748960,finish=1571218451825741502,duration=1205992542,event=set_docker_mtu[0Ktravis_time:start:0aa029f8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0aa029f8:start=1571218451830134808,finish=1571218451893920014,duration=63785206,event=resolvconf[0Ktravis_time:start:1431e298[0Ktravis_time:end:1431e298:start=1571218451898463718,finish=1571218451999749410,duration=101285692,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:01e023a0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:01e023a0:start=1571218452080890850,finish=1571218452406951541,duration=326060691,event=configure[0Ktravis_time:start:03740b0c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:03740b0c:start=1571218452411818955,finish=1571218461567802220,duration=9155983265,event=configure[0Ktravis_time:start:2cdb320e[0Ktravis_fold:start:services[0Ktravis_time:start:0cfcf2ae[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0cfcf2ae:start=1571218461592459762,finish=1571218461605837446,duration=13377684,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0cfcf2ae:start=1571218461592459762,finish=1571218464611690086,duration=3019230324,event=services[0Ktravis_time:start:029b1532[0Ktravis_time:end:029b1532:start=1571218464616228947,finish=1571218464619428217,duration=3199270,event=fix_ps4[0Ktravis_time:start:0119142c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00c04c5c[0K$ git clone --depth=50 --branch=EderK-allow_job_failure https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00c04c5c:start=1571218464628828547,finish=1571218470787046473,duration=6158217926,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2f42d88d1871e41599059c9e6d15cf5f1a082b6e
travis_fold:end:git.checkout[0K
travis_time:end:00c04c5c:start=1571218464628828547,finish=1571218471526019342,duration=6897190795,event=checkout[0Ktravis_time:start:14555d16[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:14555d16:start=1571218471530741717,finish=1571218471542294845,duration=11553128,event=env[0Ktravis_time:start:2ace355e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2ace355e:start=1571218471547474430,finish=1571218471553269667,duration=5795237,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:002315b8[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7d002fc20b8a936e9af3f431707439657c2fb037fc483b62dc29cc6c0384e923
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/598541178/log.txt)