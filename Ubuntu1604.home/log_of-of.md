 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/594964989) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/92a2d96de651...58fea094b8a4) 
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
travis_time:end:02d54fbc:start=1570520011665191883,finish=1570520011670770031,duration=5578148,event=show_system_info[0Ktravis_time:start:02ce02c6[0Ktravis_time:end:02ce02c6:start=1570520011673728987,finish=1570520011697445727,duration=23716740,event=rm_riak_source[0Ktravis_time:start:367c9a46[0Ktravis_time:end:367c9a46:start=1570520011701055852,finish=1570520011707382401,duration=6326549,event=fix_rwky_redis[0Ktravis_time:start:0ba6cf74[0Ktravis_time:end:0ba6cf74:start=1570520011710760812,finish=1570520012113133244,duration=402372432,event=wait_for_network[0Ktravis_time:start:0014383c[0Ktravis_time:end:0014383c:start=1570520012119179419,finish=1570520013682635197,duration=1563455778,event=update_apt_keys[0Ktravis_time:start:068f255c[0Ktravis_time:end:068f255c:start=1570520013687113008,finish=1570520014711543458,duration=1024430450,event=fix_hhvm_source[0Ktravis_time:start:00085450[0Ktravis_time:end:00085450:start=1570520014717835768,finish=1570520014727497168,duration=9661400,event=update_mongo_arch[0Ktravis_time:start:05443842[0Ktravis_time:end:05443842:start=1570520014732533874,finish=1570520014773228545,duration=40694671,event=fix_sudo_enabled_trusty[0Ktravis_time:start:00d2f3b0[0Ktravis_time:end:00d2f3b0:start=1570520014777050919,finish=1570520014782153453,duration=5102534,event=update_glibc[0Ktravis_time:start:174e78b5[0Ktravis_time:end:174e78b5:start=1570520014785842375,finish=1570520014796293337,duration=10450962,event=clean_up_path[0Ktravis_time:start:11f2fe35[0Ktravis_time:end:11f2fe35:start=1570520014800679086,finish=1570520014810683305,duration=10004219,event=fix_resolv_conf[0Ktravis_time:start:00100554[0Ktravis_time:end:00100554:start=1570520014815247790,finish=1570520014825308149,duration=10060359,event=fix_etc_hosts[0Ktravis_time:start:267409c2[0Ktravis_time:end:267409c2:start=1570520014830975089,finish=1570520014839772917,duration=8797828,event=fix_mvn_settings_xml[0Ktravis_time:start:0cd8ecef[0Ktravis_time:end:0cd8ecef:start=1570520014844672506,finish=1570520014857294244,duration=12621738,event=no_ipv6_localhost[0Ktravis_time:start:07410f90[0Ktravis_time:end:07410f90:start=1570520014862303570,finish=1570520014865018776,duration=2715206,event=fix_etc_mavenrc[0Ktravis_time:start:0fb09414[0Ktravis_time:end:0fb09414:start=1570520014871203488,finish=1570520014875012551,duration=3809063,event=fix_wwdr_certificate[0Ktravis_time:start:2025c29a[0Ktravis_time:end:2025c29a:start=1570520014879434304,finish=1570520014906099759,duration=26665455,event=put_localhost_first[0Ktravis_time:start:1f72f401[0Ktravis_time:end:1f72f401:start=1570520014909818234,finish=1570520014914077446,duration=4259212,event=home_paths[0Ktravis_time:start:222af4f4[0Ktravis_time:end:222af4f4:start=1570520014917814928,finish=1570520014930937407,duration=13122479,event=disable_initramfs[0Ktravis_time:start:0dbe285c[0Ktravis_time:end:0dbe285c:start=1570520014936760700,finish=1570520015223744281,duration=286983581,event=disable_ssh_roaming[0Ktravis_time:start:1327cc52[0Ktravis_time:end:1327cc52:start=1570520015228343474,finish=1570520015231210918,duration=2867444,event=debug_tools[0Ktravis_time:start:0725cebe[0Ktravis_time:end:0725cebe:start=1570520015235535365,finish=1570520015239336988,duration=3801623,event=uninstall_oclint[0Ktravis_time:start:27a71468[0Ktravis_time:end:27a71468:start=1570520015243014769,finish=1570520015246722609,duration=3707840,event=rvm_use[0Ktravis_time:start:11fe56f0[0Ktravis_time:end:11fe56f0:start=1570520015250498746,finish=1570520015262354557,duration=11855811,event=rm_etc_boto_cfg[0Ktravis_time:start:2e0f8687[0Ktravis_time:end:2e0f8687:start=1570520015266009456,finish=1570520015268705740,duration=2696284,event=rm_oraclejdk8_symlink[0Ktravis_time:start:074baeb0[0Ktravis_time:end:074baeb0:start=1570520015272407825,finish=1570520015331129350,duration=58721525,event=enable_i386[0Ktravis_time:start:0d13429c[0Ktravis_time:end:0d13429c:start=1570520015335097890,finish=1570520015341020664,duration=5922774,event=update_rubygems[0Ktravis_time:start:036fb9f6[0Ktravis_time:end:036fb9f6:start=1570520015345516123,finish=1570520016346579158,duration=1001063035,event=ensure_path_components[0Ktravis_time:start:043d86dd[0Ktravis_time:end:043d86dd:start=1570520016351548187,finish=1570520016354433397,duration=2885210,event=redefine_curl[0Ktravis_time:start:01226642[0Ktravis_time:end:01226642:start=1570520016358208397,finish=1570520016411121650,duration=52913253,event=nonblock_pipe[0Ktravis_time:start:089823e6[0Ktravis_time:end:089823e6:start=1570520016415842025,finish=1570520016462700350,duration=46858325,event=apt_get_update[0Ktravis_time:start:37ba132c[0Ktravis_time:end:37ba132c:start=1570520016467966875,finish=1570520016470630310,duration=2663435,event=deprecate_xcode_64[0Ktravis_time:start:0baa5cf0[0Ktravis_time:end:0baa5cf0:start=1570520016475119614,finish=1570520020685119415,duration=4209999801,event=update_heroku[0Ktravis_time:start:0961961e[0Ktravis_time:end:0961961e:start=1570520020690920237,finish=1570520020693839023,duration=2918786,event=shell_session_update[0Ktravis_time:start:06397e48[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3932
travis_fold:end:docker_mtu[0Ktravis_time:end:06397e48:start=1570520020697648140,finish=1570520021897542035,duration=1199893895,event=set_docker_mtu[0Ktravis_time:start:031b38b7[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:031b38b7:start=1570520021902602376,finish=1570520021967349844,duration=64747468,event=resolvconf[0Ktravis_time:start:3ba70860[0Ktravis_time:end:3ba70860:start=1570520021972513820,finish=1570520022065367757,duration=92853937,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:04fbd0d9[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:04fbd0d9:start=1570520022149952346,finish=1570520022585596277,duration=435643931,event=configure[0Ktravis_time:start:02397540[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02397540:start=1570520022590827187,finish=1570520032583316154,duration=9992488967,event=configure[0Ktravis_time:start:1107dd28[0Ktravis_fold:start:services[0Ktravis_time:start:1dc40014[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1dc40014:start=1570520032609076801,finish=1570520032623890417,duration=14813616,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1dc40014:start=1570520032609076801,finish=1570520035629881867,duration=3020805066,event=services[0Ktravis_time:start:0a3a8950[0Ktravis_time:end:0a3a8950:start=1570520035634553969,finish=1570520035637828331,duration=3274362,event=fix_ps4[0Ktravis_time:start:2b1f1b00[0K
travis_fold:start:git.checkout[0Ktravis_time:start:29e71479[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:29e71479:start=1570520035646399349,finish=1570520041891979390,duration=6245580041,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 58fea094b8a40df0d7d8ea6b460b42ec6cd296d4
travis_fold:end:git.checkout[0K
travis_time:end:29e71479:start=1570520035646399349,finish=1570520042719778854,duration=7073379505,event=checkout[0Ktravis_time:start:2f51744a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2f51744a:start=1570520042724251899,finish=1570520042735812477,duration=11560578,event=env[0Ktravis_time:start:29ffddfb[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:29ffddfb:start=1570520042740217766,finish=1570520042745938060,duration=5720294,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:052890a8[0K$ python system_testing.py -s of-of
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
Digest: sha256:c65296c31938f09bcdc7e786618bfb96816d62bf502e46560432dc0890d7c016
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/594965003/log.txt)