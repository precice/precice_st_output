 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599531436) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3f2f194851e3...aeaaaab693ed) 
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
travis_time:end:13a59200:start=1571392337294498030,finish=1571392337301137268,duration=6639238,event=show_system_info[0Ktravis_time:start:02d833ec[0Ktravis_time:end:02d833ec:start=1571392337303999426,finish=1571392337329318137,duration=25318711,event=rm_riak_source[0Ktravis_time:start:0744d5de[0Ktravis_time:end:0744d5de:start=1571392337335215791,finish=1571392337341409098,duration=6193307,event=fix_rwky_redis[0Ktravis_time:start:168b0e28[0Ktravis_time:end:168b0e28:start=1571392337345672789,finish=1571392337716623903,duration=370951114,event=wait_for_network[0Ktravis_time:start:02b01ac6[0Ktravis_time:end:02b01ac6:start=1571392337722181304,finish=1571392338797826750,duration=1075645446,event=update_apt_keys[0Ktravis_time:start:2b89afa5[0Ktravis_time:end:2b89afa5:start=1571392338802187933,finish=1571392339818417031,duration=1016229098,event=fix_hhvm_source[0Ktravis_time:start:1152cdf8[0Ktravis_time:end:1152cdf8:start=1571392339823428229,finish=1571392339832882261,duration=9454032,event=update_mongo_arch[0Ktravis_time:start:0fafcd78[0Ktravis_time:end:0fafcd78:start=1571392339836949310,finish=1571392339880192482,duration=43243172,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1670a0a0[0Ktravis_time:end:1670a0a0:start=1571392339884997538,finish=1571392339887684183,duration=2686645,event=update_glibc[0Ktravis_time:start:012e6ca0[0Ktravis_time:end:012e6ca0:start=1571392339892134957,finish=1571392339900675923,duration=8540966,event=clean_up_path[0Ktravis_time:start:0c14db98[0Ktravis_time:end:0c14db98:start=1571392339906403429,finish=1571392339914508997,duration=8105568,event=fix_resolv_conf[0Ktravis_time:start:0eb83bb2[0Ktravis_time:end:0eb83bb2:start=1571392339919688272,finish=1571392339930009412,duration=10321140,event=fix_etc_hosts[0Ktravis_time:start:2bad383a[0Ktravis_time:end:2bad383a:start=1571392339935064066,finish=1571392339943908348,duration=8844282,event=fix_mvn_settings_xml[0Ktravis_time:start:25f105b6[0Ktravis_time:end:25f105b6:start=1571392339951152711,finish=1571392339961121376,duration=9968665,event=no_ipv6_localhost[0Ktravis_time:start:010d0a27[0Ktravis_time:end:010d0a27:start=1571392339965823197,finish=1571392339969086706,duration=3263509,event=fix_etc_mavenrc[0Ktravis_time:start:021c82fc[0Ktravis_time:end:021c82fc:start=1571392339973257166,finish=1571392339978419230,duration=5162064,event=fix_wwdr_certificate[0Ktravis_time:start:056d1674[0Ktravis_time:end:056d1674:start=1571392339983227439,finish=1571392340008100389,duration=24872950,event=put_localhost_first[0Ktravis_time:start:0e8b7f3c[0Ktravis_time:end:0e8b7f3c:start=1571392340012490985,finish=1571392340016218046,duration=3727061,event=home_paths[0Ktravis_time:start:0026a31e[0Ktravis_time:end:0026a31e:start=1571392340020821381,finish=1571392340033387777,duration=12566396,event=disable_initramfs[0Ktravis_time:start:08346aa4[0Ktravis_time:end:08346aa4:start=1571392340038493280,finish=1571392340348674645,duration=310181365,event=disable_ssh_roaming[0Ktravis_time:start:306f2db4[0Ktravis_time:end:306f2db4:start=1571392340353656319,finish=1571392340356324783,duration=2668464,event=debug_tools[0Ktravis_time:start:0240e010[0Ktravis_time:end:0240e010:start=1571392340360714875,finish=1571392340364241665,duration=3526790,event=uninstall_oclint[0Ktravis_time:start:17b0b04b[0Ktravis_time:end:17b0b04b:start=1571392340369461809,finish=1571392340372899833,duration=3438024,event=rvm_use[0Ktravis_time:start:02de6fbe[0Ktravis_time:end:02de6fbe:start=1571392340377442606,finish=1571392340385973413,duration=8530807,event=rm_etc_boto_cfg[0Ktravis_time:start:004d9d4e[0Ktravis_time:end:004d9d4e:start=1571392340391100678,finish=1571392340393924621,duration=2823943,event=rm_oraclejdk8_symlink[0Ktravis_time:start:02c0607b[0Ktravis_time:end:02c0607b:start=1571392340398567096,finish=1571392340462480812,duration=63913716,event=enable_i386[0Ktravis_time:start:14182c20[0Ktravis_time:end:14182c20:start=1571392340467679776,finish=1571392340472602324,duration=4922548,event=update_rubygems[0Ktravis_time:start:1794dcf2[0Ktravis_time:end:1794dcf2:start=1571392340477262372,finish=1571392341528466611,duration=1051204239,event=ensure_path_components[0Ktravis_time:start:0cf67bb8[0Ktravis_time:end:0cf67bb8:start=1571392341533282858,finish=1571392341536057136,duration=2774278,event=redefine_curl[0Ktravis_time:start:0aaa6570[0Ktravis_time:end:0aaa6570:start=1571392341540116803,finish=1571392341591779822,duration=51663019,event=nonblock_pipe[0Ktravis_time:start:24d03929[0Ktravis_time:end:24d03929:start=1571392341595830475,finish=1571392341637620727,duration=41790252,event=apt_get_update[0Ktravis_time:start:02d28f6e[0Ktravis_time:end:02d28f6e:start=1571392341642236850,finish=1571392341645496158,duration=3259308,event=deprecate_xcode_64[0Ktravis_time:start:0664ba8f[0Ktravis_time:end:0664ba8f:start=1571392341650203284,finish=1571392346125640062,duration=4475436778,event=update_heroku[0Ktravis_time:start:103094ac[0Ktravis_time:end:103094ac:start=1571392346130800127,finish=1571392346134487088,duration=3686961,event=shell_session_update[0Ktravis_time:start:0cffa92a[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3890
travis_fold:end:docker_mtu[0Ktravis_time:end:0cffa92a:start=1571392346139129231,finish=1571392347341487904,duration=1202358673,event=set_docker_mtu[0Ktravis_time:start:0374ef14[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0374ef14:start=1571392347345730482,finish=1571392347415533033,duration=69802551,event=resolvconf[0Ktravis_time:start:00824d75[0Ktravis_time:end:00824d75:start=1571392347420593232,finish=1571392347516954267,duration=96361035,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:08bed7a6[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:08bed7a6:start=1571392347600358375,finish=1571392348114604227,duration=514245852,event=configure[0Ktravis_time:start:1a9c92af[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1a9c92af:start=1571392348120609232,finish=1571392357884535623,duration=9763926391,event=configure[0Ktravis_time:start:17d4cc84[0Ktravis_fold:start:services[0Ktravis_time:start:21f4cdb5[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:21f4cdb5:start=1571392357911809328,finish=1571392357926646552,duration=14837224,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:21f4cdb5:start=1571392357911809328,finish=1571392360933286668,duration=3021477340,event=services[0Ktravis_time:start:118d159c[0Ktravis_time:end:118d159c:start=1571392360938245731,finish=1571392360941039137,duration=2793406,event=fix_ps4[0Ktravis_time:start:00008ebf[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0136a6bc[0K$ git clone --depth=50 --branch=IshaanDesai-testing_fe-fe_complexDomain https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0136a6bc:start=1571392360950882801,finish=1571392367189971333,duration=6239088532,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf aeaaaab693ed8a49abea293f250adef6287ca59d
travis_fold:end:git.checkout[0K
travis_time:end:0136a6bc:start=1571392360950882801,finish=1571392367344787550,duration=6393904749,event=checkout[0Ktravis_time:start:2b142e3c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2b142e3c:start=1571392367349420796,finish=1571392367359903116,duration=10482320,event=env[0Ktravis_time:start:21d0ca96[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:21d0ca96:start=1571392367364459236,finish=1571392367370041167,duration=5581931,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:122c0e3c[0K$ python system_testing.py -s of-of
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
Digest: sha256:ad692be02c5fed5891c3c0ecac2c2952067014e26d8596600ed9bd76fc76529f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/599531450/log.txt)