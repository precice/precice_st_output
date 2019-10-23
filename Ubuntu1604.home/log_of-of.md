## Status: Passing 
Build: [1000](https://travis-ci.org/precice/systemtests/builds/601988696) 

Job: [1000.14](https://travis-ci.org/precice/systemtests/jobs/601988710) 

Triggered by: [push](https://github.com/precice/systemtests/compare/500cfbb53a97...73300f5bea0c) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:05979850:start=1571862947037156027,finish=1571862947043648131,duration=6492104,event=show_system_info[0Ktravis_time:start:0edd9cc2[0Ktravis_time:end:0edd9cc2:start=1571862947047198234,finish=1571862947079625751,duration=32427517,event=rm_riak_source[0Ktravis_time:start:031ad0d5[0Ktravis_time:end:031ad0d5:start=1571862947083859666,finish=1571862947091052555,duration=7192889,event=fix_rwky_redis[0Ktravis_time:start:0a2a50f8[0Ktravis_time:end:0a2a50f8:start=1571862947094881855,finish=1571862947482955923,duration=388074068,event=wait_for_network[0Ktravis_time:start:32403e6c[0Ktravis_time:end:32403e6c:start=1571862947488670781,finish=1571862948619776965,duration=1131106184,event=update_apt_keys[0Ktravis_time:start:0eaee458[0Ktravis_time:end:0eaee458:start=1571862948625467703,finish=1571862949704886521,duration=1079418818,event=fix_hhvm_source[0Ktravis_time:start:007344ca[0Ktravis_time:end:007344ca:start=1571862949709460639,finish=1571862949720738391,duration=11277752,event=update_mongo_arch[0Ktravis_time:start:047e3f3e[0Ktravis_time:end:047e3f3e:start=1571862949725762966,finish=1571862949769694573,duration=43931607,event=fix_sudo_enabled_trusty[0Ktravis_time:start:02dd9ac1[0Ktravis_time:end:02dd9ac1:start=1571862949774848695,finish=1571862949777795747,duration=2947052,event=update_glibc[0Ktravis_time:start:29f016a0[0Ktravis_time:end:29f016a0:start=1571862949782648197,finish=1571862949791603677,duration=8955480,event=clean_up_path[0Ktravis_time:start:01261298[0Ktravis_time:end:01261298:start=1571862949796095622,finish=1571862949805697301,duration=9601679,event=fix_resolv_conf[0Ktravis_time:start:162c18a5[0Ktravis_time:end:162c18a5:start=1571862949810920598,finish=1571862949821622340,duration=10701742,event=fix_etc_hosts[0Ktravis_time:start:1fa3e8b1[0Ktravis_time:end:1fa3e8b1:start=1571862949826878697,finish=1571862949837637183,duration=10758486,event=fix_mvn_settings_xml[0Ktravis_time:start:240972e8[0Ktravis_time:end:240972e8:start=1571862949843845650,finish=1571862949855088699,duration=11243049,event=no_ipv6_localhost[0Ktravis_time:start:00033d7e[0Ktravis_time:end:00033d7e:start=1571862949861022168,finish=1571862949865411140,duration=4388972,event=fix_etc_mavenrc[0Ktravis_time:start:1a5fbee4[0Ktravis_time:end:1a5fbee4:start=1571862949871590264,finish=1571862949875888617,duration=4298353,event=fix_wwdr_certificate[0Ktravis_time:start:26e7caba[0Ktravis_time:end:26e7caba:start=1571862949881708500,finish=1571862949909749061,duration=28040561,event=put_localhost_first[0Ktravis_time:start:062a4340[0Ktravis_time:end:062a4340:start=1571862949916011724,finish=1571862949920638901,duration=4627177,event=home_paths[0Ktravis_time:start:257c1e95[0Ktravis_time:end:257c1e95:start=1571862949925427669,finish=1571862949942973011,duration=17545342,event=disable_initramfs[0Ktravis_time:start:00efc580[0Ktravis_time:end:00efc580:start=1571862949948514816,finish=1571862950310485246,duration=361970430,event=disable_ssh_roaming[0Ktravis_time:start:0eebc3cc[0Ktravis_time:end:0eebc3cc:start=1571862950314937036,finish=1571862950317914258,duration=2977222,event=debug_tools[0Ktravis_time:start:0d44bb87[0Ktravis_time:end:0d44bb87:start=1571862950321884164,finish=1571862950325857896,duration=3973732,event=uninstall_oclint[0Ktravis_time:start:23067b87[0Ktravis_time:end:23067b87:start=1571862950329780633,finish=1571862950333499497,duration=3718864,event=rvm_use[0Ktravis_time:start:23a00252[0Ktravis_time:end:23a00252:start=1571862950337464642,finish=1571862950346188825,duration=8724183,event=rm_etc_boto_cfg[0Ktravis_time:start:2e7961fb[0Ktravis_time:end:2e7961fb:start=1571862950350121946,finish=1571862950352975388,duration=2853442,event=rm_oraclejdk8_symlink[0Ktravis_time:start:03236cbd[0Ktravis_time:end:03236cbd:start=1571862950356850936,finish=1571862950417152526,duration=60301590,event=enable_i386[0Ktravis_time:start:064ab816[0Ktravis_time:end:064ab816:start=1571862950421496186,finish=1571862950426426595,duration=4930409,event=update_rubygems[0Ktravis_time:start:25596566[0Ktravis_time:end:25596566:start=1571862950431549965,finish=1571862951470081406,duration=1038531441,event=ensure_path_components[0Ktravis_time:start:02778e20[0Ktravis_time:end:02778e20:start=1571862951475259557,finish=1571862951478226648,duration=2967091,event=redefine_curl[0Ktravis_time:start:1304f25f[0Ktravis_time:end:1304f25f:start=1571862951483632799,finish=1571862951539985939,duration=56353140,event=nonblock_pipe[0Ktravis_time:start:09f63e8e[0Ktravis_time:end:09f63e8e:start=1571862951546193914,finish=1571862954608303230,duration=3062109316,event=apt_get_update[0Ktravis_time:start:01f8cafe[0Ktravis_time:end:01f8cafe:start=1571862954614255069,finish=1571862954618094515,duration=3839446,event=deprecate_xcode_64[0Ktravis_time:start:0aa25754[0Ktravis_time:end:0aa25754:start=1571862954623610636,finish=1571862959778225830,duration=5154615194,event=update_heroku[0Ktravis_time:start:2304c5c7[0Ktravis_time:end:2304c5c7:start=1571862959784541043,finish=1571862959787749387,duration=3208344,event=shell_session_update[0Ktravis_time:start:1808e310[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3877
travis_fold:end:docker_mtu[0Ktravis_time:end:1808e310:start=1571862959792466866,finish=1571862960998287585,duration=1205820719,event=set_docker_mtu[0Ktravis_time:start:0d87a59b[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0d87a59b:start=1571862961003718063,finish=1571862961075862437,duration=72144374,event=resolvconf[0Ktravis_time:start:09c10df4[0Ktravis_time:end:09c10df4:start=1571862961081089430,finish=1571862961197199981,duration=116110551,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0cf9b18a[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0cf9b18a:start=1571862961283368922,finish=1571862961590579425,duration=307210503,event=configure[0Ktravis_time:start:22e96a2c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:22e96a2c:start=1571862961597105215,finish=1571862974483744830,duration=12886639615,event=configure[0Ktravis_time:start:36da72da[0Ktravis_fold:start:services[0Ktravis_time:start:0aad4e20[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0aad4e20:start=1571862974511215925,finish=1571862974526080962,duration=14865037,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0aad4e20:start=1571862974511215925,finish=1571862977531365826,duration=3020149901,event=services[0Ktravis_time:start:37b81af0[0Ktravis_time:end:37b81af0:start=1571862977536015047,finish=1571862977539041822,duration=3026775,event=fix_ps4[0Ktravis_time:start:02fb9e00[0K
travis_fold:start:git.checkout[0Ktravis_time:start:13724424[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:13724424:start=1571862977548656904,finish=1571862983818410623,duration=6269753719,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 73300f5bea0ced6562ee2d5aa26d420608795cda
travis_fold:end:git.checkout[0K
travis_time:end:13724424:start=1571862977548656904,finish=1571862984570481846,duration=7021824942,event=checkout[0Ktravis_time:start:17078ec8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:17078ec8:start=1571862984575181438,finish=1571862984587157217,duration=11975779,event=env[0Ktravis_time:start:032ba58f[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:032ba58f:start=1571862984592452574,finish=1571862984598956679,duration=6504105,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:286101ed[0K$ python system_testing.py -s of-of
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
Digest: sha256:800ef878bf82edef081068e05b4fbe89b92f4870c31a470ddb56147df1cb0d1d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:286101ed:start=1571862984963447676,finish=1571863106315616955,duration=121352169279,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:06a7a160[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/601988710/log.txt)