## Status: Passing 
Build: [1047](https://travis-ci.org/precice/systemtests/builds/604758622) 

Job: [1047.18](https://travis-ci.org/precice/systemtests/jobs/604758647) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:196fef99:start=1572403174959490169,finish=1572403174965614698,duration=6124529,event=show_system_info[0Ktravis_time:start:11c5c90e[0Ktravis_time:end:11c5c90e:start=1572403174968688240,finish=1572403174993268396,duration=24580156,event=rm_riak_source[0Ktravis_time:start:091fc35c[0Ktravis_time:end:091fc35c:start=1572403174996571128,finish=1572403175005542347,duration=8971219,event=fix_rwky_redis[0Ktravis_time:start:2a2fd6f0[0Ktravis_time:end:2a2fd6f0:start=1572403175010631385,finish=1572403175379940963,duration=369309578,event=wait_for_network[0Ktravis_time:start:0b6fc00a[0Ktravis_time:end:0b6fc00a:start=1572403175384225204,finish=1572403176922618295,duration=1538393091,event=update_apt_keys[0Ktravis_time:start:1b399aa1[0Ktravis_time:end:1b399aa1:start=1572403176927765805,finish=1572403177992489359,duration=1064723554,event=fix_hhvm_source[0Ktravis_time:start:2c5d91ba[0Ktravis_time:end:2c5d91ba:start=1572403177997634559,finish=1572403178007550260,duration=9915701,event=update_mongo_arch[0Ktravis_time:start:05df7036[0Ktravis_time:end:05df7036:start=1572403178012177287,finish=1572403178052567735,duration=40390448,event=fix_sudo_enabled_trusty[0Ktravis_time:start:05397c2e[0Ktravis_time:end:05397c2e:start=1572403178058313965,finish=1572403178060897592,duration=2583627,event=update_glibc[0Ktravis_time:start:09a39b00[0Ktravis_time:end:09a39b00:start=1572403178065047861,finish=1572403178073498399,duration=8450538,event=clean_up_path[0Ktravis_time:start:2d502d73[0Ktravis_time:end:2d502d73:start=1572403178079186835,finish=1572403178087375996,duration=8189161,event=fix_resolv_conf[0Ktravis_time:start:1b56d177[0Ktravis_time:end:1b56d177:start=1572403178091822243,finish=1572403178101452350,duration=9630107,event=fix_etc_hosts[0Ktravis_time:start:0021bc68[0Ktravis_time:end:0021bc68:start=1572403178106424753,finish=1572403178115739137,duration=9314384,event=fix_mvn_settings_xml[0Ktravis_time:start:23ca91c8[0Ktravis_time:end:23ca91c8:start=1572403178122883763,finish=1572403178132644545,duration=9760782,event=no_ipv6_localhost[0Ktravis_time:start:16206c8e[0Ktravis_time:end:16206c8e:start=1572403178137117843,finish=1572403178139635287,duration=2517444,event=fix_etc_mavenrc[0Ktravis_time:start:10e4e088[0Ktravis_time:end:10e4e088:start=1572403178145630580,finish=1572403178149084429,duration=3453849,event=fix_wwdr_certificate[0Ktravis_time:start:016708f1[0Ktravis_time:end:016708f1:start=1572403178152665393,finish=1572403178179106505,duration=26441112,event=put_localhost_first[0Ktravis_time:start:13df4d14[0Ktravis_time:end:13df4d14:start=1572403178182853199,finish=1572403178186754540,duration=3901341,event=home_paths[0Ktravis_time:start:00a1a441[0Ktravis_time:end:00a1a441:start=1572403178194515836,finish=1572403178206679064,duration=12163228,event=disable_initramfs[0Ktravis_time:start:07f1a147[0Ktravis_time:end:07f1a147:start=1572403178210273373,finish=1572403178543061423,duration=332788050,event=disable_ssh_roaming[0Ktravis_time:start:07289d34[0Ktravis_time:end:07289d34:start=1572403178547516331,finish=1572403178550290274,duration=2773943,event=debug_tools[0Ktravis_time:start:18544380[0Ktravis_time:end:18544380:start=1572403178554463406,finish=1572403178557900267,duration=3436861,event=uninstall_oclint[0Ktravis_time:start:04f7a594[0Ktravis_time:end:04f7a594:start=1572403178562255110,finish=1572403178566620392,duration=4365282,event=rvm_use[0Ktravis_time:start:0efc95a4[0Ktravis_time:end:0efc95a4:start=1572403178570988111,finish=1572403178582924430,duration=11936319,event=rm_etc_boto_cfg[0Ktravis_time:start:061117b3[0Ktravis_time:end:061117b3:start=1572403178587158432,finish=1572403178590010632,duration=2852200,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1dfd98dc[0Ktravis_time:end:1dfd98dc:start=1572403178594289844,finish=1572403178649014937,duration=54725093,event=enable_i386[0Ktravis_time:start:060242d8[0Ktravis_time:end:060242d8:start=1572403178653649724,finish=1572403178658374731,duration=4725007,event=update_rubygems[0Ktravis_time:start:1ae91160[0Ktravis_time:end:1ae91160:start=1572403178662791196,finish=1572403179657901857,duration=995110661,event=ensure_path_components[0Ktravis_time:start:00f1d320[0Ktravis_time:end:00f1d320:start=1572403179663033692,finish=1572403179666258344,duration=3224652,event=redefine_curl[0Ktravis_time:start:02d965d2[0Ktravis_time:end:02d965d2:start=1572403179670242852,finish=1572403179722979043,duration=52736191,event=nonblock_pipe[0Ktravis_time:start:0363cd80[0Ktravis_time:end:0363cd80:start=1572403179727550366,finish=1572403182770021992,duration=3042471626,event=apt_get_update[0Ktravis_time:start:0cf981c0[0Ktravis_time:end:0cf981c0:start=1572403182774701591,finish=1572403182777403399,duration=2701808,event=deprecate_xcode_64[0Ktravis_time:start:0df01915[0Ktravis_time:end:0df01915:start=1572403182781045617,finish=1572403187500512044,duration=4719466427,event=update_heroku[0Ktravis_time:start:07d56710[0Ktravis_time:end:07d56710:start=1572403187505190129,finish=1572403187507944675,duration=2754546,event=shell_session_update[0Ktravis_time:start:0fab4005[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3887
travis_fold:end:docker_mtu[0Ktravis_time:end:0fab4005:start=1572403187511965161,finish=1572403188696447159,duration=1184481998,event=set_docker_mtu[0Ktravis_time:start:0e210782[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0e210782:start=1572403188701054135,finish=1572403188767222792,duration=66168657,event=resolvconf[0Ktravis_time:start:0ef82fb8[0Ktravis_time:end:0ef82fb8:start=1572403188771402202,finish=1572403188871764055,duration=100361853,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0026f906[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0026f906:start=1572403188955173561,finish=1572403189353599914,duration=398426353,event=configure[0Ktravis_time:start:28c8f762[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:28c8f762:start=1572403189359045296,finish=1572403198696857699,duration=9337812403,event=configure[0Ktravis_time:start:18ec1480[0Ktravis_fold:start:services[0Ktravis_time:start:34a1642c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:34a1642c:start=1572403198721800229,finish=1572403198735996334,duration=14196105,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:34a1642c:start=1572403198721800229,finish=1572403201740899725,duration=3019099496,event=services[0Ktravis_time:start:10760102[0Ktravis_time:end:10760102:start=1572403201745995764,finish=1572403201748840010,duration=2844246,event=fix_ps4[0Ktravis_time:start:18c43000[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0b6d5140[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0b6d5140:start=1572403201756849323,finish=1572403207957879367,duration=6201030044,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0b6d5140:start=1572403201756849323,finish=1572403208912960553,duration=7156111230,event=checkout[0Ktravis_time:start:076d3c4f[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:076d3c4f:start=1572403208917588202,finish=1572403208931296158,duration=13707956,event=env[0Ktravis_time:start:05017643[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:05017643:start=1572403208936884840,finish=1572403208947974178,duration=11089338,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:01905690[0K$ python system_testing.py -s of-of
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
Digest: sha256:a1923cb1231d1cc4e515c0bc821b7531290bcdde9aa979b85e6c7f36d0b76068
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:01905690:start=1572403209285390846,finish=1572403329973401533,duration=120688010687,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:29f736b4[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/604758647/log.txt)