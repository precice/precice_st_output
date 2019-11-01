## Status: Passing 
Build: [1052](https://travis-ci.org/precice/systemtests/builds/605812235) 

Job: [1052.18](https://travis-ci.org/precice/systemtests/jobs/605812253) 

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
travis_time:end:031cf7e8:start=1572575970750064435,finish=1572575970756374199,duration=6309764,event=show_system_info[0Ktravis_time:start:23804ff0[0Ktravis_time:end:23804ff0:start=1572575970759632886,finish=1572575970784327441,duration=24694555,event=rm_riak_source[0Ktravis_time:start:1f932924[0Ktravis_time:end:1f932924:start=1572575970788907794,finish=1572575970796713225,duration=7805431,event=fix_rwky_redis[0Ktravis_time:start:18811ea7[0Ktravis_time:end:18811ea7:start=1572575970801512548,finish=1572575971251911223,duration=450398675,event=wait_for_network[0Ktravis_time:start:042e8474[0Ktravis_time:end:042e8474:start=1572575971256965590,finish=1572575972880399535,duration=1623433945,event=update_apt_keys[0Ktravis_time:start:13432cb6[0Ktravis_time:end:13432cb6:start=1572575972886823818,finish=1572575974078743303,duration=1191919485,event=fix_hhvm_source[0Ktravis_time:start:00972548[0Ktravis_time:end:00972548:start=1572575974085600581,finish=1572575974098245573,duration=12644992,event=update_mongo_arch[0Ktravis_time:start:0f98aaef[0Ktravis_time:end:0f98aaef:start=1572575974105300921,finish=1572575974153791293,duration=48490372,event=fix_sudo_enabled_trusty[0Ktravis_time:start:08ff4600[0Ktravis_time:end:08ff4600:start=1572575974159097958,finish=1572575974162227181,duration=3129223,event=update_glibc[0Ktravis_time:start:0ce7a098[0Ktravis_time:end:0ce7a098:start=1572575974168426397,finish=1572575974178900526,duration=10474129,event=clean_up_path[0Ktravis_time:start:170600fc[0Ktravis_time:end:170600fc:start=1572575974183851378,finish=1572575974195693132,duration=11841754,event=fix_resolv_conf[0Ktravis_time:start:0b767e60[0Ktravis_time:end:0b767e60:start=1572575974201708562,finish=1572575974214591486,duration=12882924,event=fix_etc_hosts[0Ktravis_time:start:02f36da8[0Ktravis_time:end:02f36da8:start=1572575974221145660,finish=1572575974233891784,duration=12746124,event=fix_mvn_settings_xml[0Ktravis_time:start:01fce481[0Ktravis_time:end:01fce481:start=1572575974238973671,finish=1572575974251153014,duration=12179343,event=no_ipv6_localhost[0Ktravis_time:start:19c922af[0Ktravis_time:end:19c922af:start=1572575974258710775,finish=1572575974262557677,duration=3846902,event=fix_etc_mavenrc[0Ktravis_time:start:04d41dd9[0Ktravis_time:end:04d41dd9:start=1572575974268761965,finish=1572575974275885235,duration=7123270,event=fix_wwdr_certificate[0Ktravis_time:start:2c8123a4[0Ktravis_time:end:2c8123a4:start=1572575974281503659,finish=1572575974312366268,duration=30862609,event=put_localhost_first[0Ktravis_time:start:1723291a[0Ktravis_time:end:1723291a:start=1572575974319232108,finish=1572575974323534230,duration=4302122,event=home_paths[0Ktravis_time:start:07de0226[0Ktravis_time:end:07de0226:start=1572575974328697289,finish=1572575974346013580,duration=17316291,event=disable_initramfs[0Ktravis_time:start:03943808[0Ktravis_time:end:03943808:start=1572575974351265462,finish=1572575974691496711,duration=340231249,event=disable_ssh_roaming[0Ktravis_time:start:00d77162[0Ktravis_time:end:00d77162:start=1572575974697316282,finish=1572575974701807176,duration=4490894,event=debug_tools[0Ktravis_time:start:0bb8598c[0Ktravis_time:end:0bb8598c:start=1572575974706521385,finish=1572575974712817194,duration=6295809,event=uninstall_oclint[0Ktravis_time:start:0a6a8a85[0Ktravis_time:end:0a6a8a85:start=1572575974718753176,finish=1572575974723739357,duration=4986181,event=rvm_use[0Ktravis_time:start:1c066ef4[0Ktravis_time:end:1c066ef4:start=1572575974727643690,finish=1572575974740953140,duration=13309450,event=rm_etc_boto_cfg[0Ktravis_time:start:00b17515[0Ktravis_time:end:00b17515:start=1572575974746012370,finish=1572575974749216176,duration=3203806,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0a816c68[0Ktravis_time:end:0a816c68:start=1572575974753748728,finish=1572575974819938585,duration=66189857,event=enable_i386[0Ktravis_time:start:0added84[0Ktravis_time:end:0added84:start=1572575974825802185,finish=1572575974831246222,duration=5444037,event=update_rubygems[0Ktravis_time:start:1f9bc900[0Ktravis_time:end:1f9bc900:start=1572575974837074264,finish=1572575975892853249,duration=1055778985,event=ensure_path_components[0Ktravis_time:start:1f660c86[0Ktravis_time:end:1f660c86:start=1572575975898074919,finish=1572575975900936548,duration=2861629,event=redefine_curl[0Ktravis_time:start:05538ab6[0Ktravis_time:end:05538ab6:start=1572575975906007418,finish=1572575975960957801,duration=54950383,event=nonblock_pipe[0Ktravis_time:start:07107515[0Ktravis_time:end:07107515:start=1572575975965959215,finish=1572575979016950991,duration=3050991776,event=apt_get_update[0Ktravis_time:start:06c9e13f[0Ktravis_time:end:06c9e13f:start=1572575979021744184,finish=1572575979024871435,duration=3127251,event=deprecate_xcode_64[0Ktravis_time:start:1d95443c[0Ktravis_time:end:1d95443c:start=1572575979030368703,finish=1572575984082787038,duration=5052418335,event=update_heroku[0Ktravis_time:start:02380a44[0Ktravis_time:end:02380a44:start=1572575984088307406,finish=1572575984093951611,duration=5644205,event=shell_session_update[0Ktravis_time:start:1346dfc0[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3962
travis_fold:end:docker_mtu[0Ktravis_time:end:1346dfc0:start=1572575984099633744,finish=1572575985294341806,duration=1194708062,event=set_docker_mtu[0Ktravis_time:start:131daeaa[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:131daeaa:start=1572575985299910881,finish=1572575985376514151,duration=76603270,event=resolvconf[0Ktravis_time:start:12de66dd[0Ktravis_time:end:12de66dd:start=1572575985382257370,finish=1572575985490983868,duration=108726498,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02a7801b[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02a7801b:start=1572575985578487909,finish=1572575985868569880,duration=290081971,event=configure[0Ktravis_time:start:3869ea0a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:3869ea0a:start=1572575985873999450,finish=1572575998417708871,duration=12543709421,event=configure[0Ktravis_time:start:14b27770[0Ktravis_fold:start:services[0Ktravis_time:start:27f2ff0c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:27f2ff0c:start=1572575998447570976,finish=1572575998465287990,duration=17717014,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:27f2ff0c:start=1572575998447570976,finish=1572576001470993618,duration=3023422642,event=services[0Ktravis_time:start:01f75f6f[0Ktravis_time:end:01f75f6f:start=1572576001476188721,finish=1572576001479574006,duration=3385285,event=fix_ps4[0Ktravis_time:start:0c1fec50[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0d643682[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0d643682:start=1572576001489286619,finish=1572576007786362697,duration=6297076078,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0d643682:start=1572576001489286619,finish=1572576008476657069,duration=6987370450,event=checkout[0Ktravis_time:start:0df675c5[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0df675c5:start=1572576008481817123,finish=1572576008492832170,duration=11015047,event=env[0Ktravis_time:start:0121175b[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0121175b:start=1572576008498336554,finish=1572576008505799863,duration=7463309,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09f3cc52[0K$ python system_testing.py -s of-of
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
Digest: sha256:5f4cf9654d3e8ad6e24ca09f06617acede4a15c96234e007a7edfec2b73ce6cd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/605812253/log.txt)