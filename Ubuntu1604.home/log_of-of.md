 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/591102069) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/887c8e1583c8^...46a3f0d5dc83) 
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
travis_time:end:0d758f22:start=1569766590569920657,finish=1569766590576225856,duration=6305199,event=show_system_info[0Ktravis_time:start:03fd2f09[0Ktravis_time:end:03fd2f09:start=1569766590579807976,finish=1569766590607486913,duration=27678937,event=rm_riak_source[0Ktravis_time:start:347dd4c5[0Ktravis_time:end:347dd4c5:start=1569766590611832899,finish=1569766590622250784,duration=10417885,event=fix_rwky_redis[0Ktravis_time:start:02fcd3b4[0Ktravis_time:end:02fcd3b4:start=1569766590626368855,finish=1569766591030108262,duration=403739407,event=wait_for_network[0Ktravis_time:start:0ce46878[0Ktravis_time:end:0ce46878:start=1569766591036759007,finish=1569766592022281899,duration=985522892,event=update_apt_keys[0Ktravis_time:start:1abb00f4[0Ktravis_time:end:1abb00f4:start=1569766592029125710,finish=1569766593173633576,duration=1144507866,event=fix_hhvm_source[0Ktravis_time:start:1c8d6dc0[0Ktravis_time:end:1c8d6dc0:start=1569766593180505169,finish=1569766593193373576,duration=12868407,event=update_mongo_arch[0Ktravis_time:start:12dbdd70[0Ktravis_time:end:12dbdd70:start=1569766593198100137,finish=1569766593248947132,duration=50846995,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2032ad00[0Ktravis_time:end:2032ad00:start=1569766593254572854,finish=1569766593258262142,duration=3689288,event=update_glibc[0Ktravis_time:start:26d2b00d[0Ktravis_time:end:26d2b00d:start=1569766593263606122,finish=1569766593274037861,duration=10431739,event=clean_up_path[0Ktravis_time:start:00b2f03e[0Ktravis_time:end:00b2f03e:start=1569766593279237195,finish=1569766593290172190,duration=10934995,event=fix_resolv_conf[0Ktravis_time:start:1a24f0da[0Ktravis_time:end:1a24f0da:start=1569766593296085905,finish=1569766593308377517,duration=12291612,event=fix_etc_hosts[0Ktravis_time:start:064b0df0[0Ktravis_time:end:064b0df0:start=1569766593313694452,finish=1569766593325168411,duration=11473959,event=fix_mvn_settings_xml[0Ktravis_time:start:022ab038[0Ktravis_time:end:022ab038:start=1569766593330842207,finish=1569766593342700026,duration=11857819,event=no_ipv6_localhost[0Ktravis_time:start:2150ae08[0Ktravis_time:end:2150ae08:start=1569766593348768759,finish=1569766593351987033,duration=3218274,event=fix_etc_mavenrc[0Ktravis_time:start:012c6738[0Ktravis_time:end:012c6738:start=1569766593356546432,finish=1569766593360556114,duration=4009682,event=fix_wwdr_certificate[0Ktravis_time:start:0253e570[0Ktravis_time:end:0253e570:start=1569766593366534891,finish=1569766593398074063,duration=31539172,event=put_localhost_first[0Ktravis_time:start:10568f7c[0Ktravis_time:end:10568f7c:start=1569766593404304698,finish=1569766593410244677,duration=5939979,event=home_paths[0Ktravis_time:start:0073b140[0Ktravis_time:end:0073b140:start=1569766593416183991,finish=1569766593431692849,duration=15508858,event=disable_initramfs[0Ktravis_time:start:01f1f706[0Ktravis_time:end:01f1f706:start=1569766593437715940,finish=1569766593764367634,duration=326651694,event=disable_ssh_roaming[0Ktravis_time:start:02292230[0Ktravis_time:end:02292230:start=1569766593771010367,finish=1569766593774522859,duration=3512492,event=debug_tools[0Ktravis_time:start:36378954[0Ktravis_time:end:36378954:start=1569766593780033255,finish=1569766593784549267,duration=4516012,event=uninstall_oclint[0Ktravis_time:start:18a01e33[0Ktravis_time:end:18a01e33:start=1569766593790859461,finish=1569766593797829793,duration=6970332,event=rvm_use[0Ktravis_time:start:07f22af6[0Ktravis_time:end:07f22af6:start=1569766593802601136,finish=1569766593812901249,duration=10300113,event=rm_etc_boto_cfg[0Ktravis_time:start:12f8d43e[0Ktravis_time:end:12f8d43e:start=1569766593819838311,finish=1569766593822915331,duration=3077020,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0d5f704d[0Ktravis_time:end:0d5f704d:start=1569766593827663939,finish=1569766593888457912,duration=60793973,event=enable_i386[0Ktravis_time:start:2bbb3502[0Ktravis_time:end:2bbb3502:start=1569766593895198211,finish=1569766593901565502,duration=6367291,event=update_rubygems[0Ktravis_time:start:01a452f0[0Ktravis_time:end:01a452f0:start=1569766593906876886,finish=1569766595120883292,duration=1214006406,event=ensure_path_components[0Ktravis_time:start:138cb12c[0Ktravis_time:end:138cb12c:start=1569766595127109277,finish=1569766595130735974,duration=3626697,event=redefine_curl[0Ktravis_time:start:10c9649f[0Ktravis_time:end:10c9649f:start=1569766595136395741,finish=1569766595201879429,duration=65483688,event=nonblock_pipe[0Ktravis_time:start:35812396[0Ktravis_time:end:35812396:start=1569766595208729275,finish=1569766595262026101,duration=53296826,event=apt_get_update[0Ktravis_time:start:01c41800[0Ktravis_time:end:01c41800:start=1569766595268108000,finish=1569766595271417462,duration=3309462,event=deprecate_xcode_64[0Ktravis_time:start:15657a1a[0Ktravis_time:end:15657a1a:start=1569766595278148491,finish=1569766600491562132,duration=5213413641,event=update_heroku[0Ktravis_time:start:1c918404[0Ktravis_time:end:1c918404:start=1569766600497003766,finish=1569766600500752922,duration=3749156,event=shell_session_update[0Ktravis_time:start:1c3a1fd8[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3950
travis_fold:end:docker_mtu[0Ktravis_time:end:1c3a1fd8:start=1569766600506508075,finish=1569766601708573979,duration=1202065904,event=set_docker_mtu[0Ktravis_time:start:001d0bc8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:001d0bc8:start=1569766601713917237,finish=1569766601783308041,duration=69390804,event=resolvconf[0Ktravis_time:start:045e44f8[0Ktravis_time:end:045e44f8:start=1569766601788945638,finish=1569766601895144145,duration=106198507,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:229b9a68[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:229b9a68:start=1569766601990521584,finish=1569766602268577233,duration=278055649,event=configure[0Ktravis_time:start:3abac068[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:3abac068:start=1569766602275735721,finish=1569766615064884694,duration=12789148973,event=configure[0Ktravis_time:start:13940bd8[0Ktravis_fold:start:services[0Ktravis_time:start:2ca5d5b7[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:2ca5d5b7:start=1569766615096191335,finish=1569766615114423961,duration=18232626,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2ca5d5b7:start=1569766615096191335,finish=1569766618121729338,duration=3025538003,event=services[0Ktravis_time:start:11cbef40[0Ktravis_time:end:11cbef40:start=1569766618126865317,finish=1569766618130243626,duration=3378309,event=fix_ps4[0Ktravis_time:start:0138a2ae[0K
travis_fold:start:git.checkout[0Ktravis_time:start:06e4c7ea[0K$ git clone --depth=50 --branch=EderK-add_elastictube1d_test https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:06e4c7ea:start=1569766618139743344,finish=1569766624642399656,duration=6502656312,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 46a3f0d5dc83e5c096b4266f9ef2e2d15da8b298
travis_fold:end:git.checkout[0K
travis_time:end:06e4c7ea:start=1569766618139743344,finish=1569766625184621051,duration=7044877707,event=checkout[0Ktravis_time:start:12c6160c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:12c6160c:start=1569766625190784569,finish=1569766625204385647,duration=13601078,event=env[0Ktravis_time:start:22355364[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:22355364:start=1569766625212192465,finish=1569766625219045714,duration=6853249,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0639ae18[0K$ python system_testing.py -s of-of
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
Digest: sha256:1a0c04933b6b2e3ee94062e56f4f3ec75051cdfd9e4225a98902526ee5e64525
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/591102083/log.txt)