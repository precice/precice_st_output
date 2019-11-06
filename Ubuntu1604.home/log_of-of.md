## Status: Passing 
Build: [1058](https://travis-ci.org/precice/systemtests/builds/607962841) 

Job: [1058.18](https://travis-ci.org/precice/systemtests/jobs/607962861) 

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
travis_time:end:0a3ebd4f:start=1573008687362064144,finish=1573008687371389657,duration=9325513,event=show_system_info[0Ktravis_time:start:08bc5150[0Ktravis_time:end:08bc5150:start=1573008687374310750,finish=1573008687413232623,duration=38921873,event=rm_riak_source[0Ktravis_time:start:0039c204[0Ktravis_time:end:0039c204:start=1573008687416800160,finish=1573008687432390339,duration=15590179,event=fix_rwky_redis[0Ktravis_time:start:048105de[0Ktravis_time:end:048105de:start=1573008687435673452,finish=1573008687906446673,duration=470773221,event=wait_for_network[0Ktravis_time:start:192b2c47[0Ktravis_time:end:192b2c47:start=1573008687910914585,finish=1573008688934271134,duration=1023356549,event=update_apt_keys[0Ktravis_time:start:2bfb4c59[0Ktravis_time:end:2bfb4c59:start=1573008688938529677,finish=1573008689986261628,duration=1047731951,event=fix_hhvm_source[0Ktravis_time:start:0242e05a[0Ktravis_time:end:0242e05a:start=1573008689991079672,finish=1573008690005040773,duration=13961101,event=update_mongo_arch[0Ktravis_time:start:07f704b0[0Ktravis_time:end:07f704b0:start=1573008690009811764,finish=1573008690062119083,duration=52307319,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1ea3e34e[0Ktravis_time:end:1ea3e34e:start=1573008690066442846,finish=1573008690069075036,duration=2632190,event=update_glibc[0Ktravis_time:start:0df03f63[0Ktravis_time:end:0df03f63:start=1573008690073152313,finish=1573008690082066272,duration=8913959,event=clean_up_path[0Ktravis_time:start:06cd1814[0Ktravis_time:end:06cd1814:start=1573008690088508079,finish=1573008690096896151,duration=8388072,event=fix_resolv_conf[0Ktravis_time:start:1be74b84[0Ktravis_time:end:1be74b84:start=1573008690101132308,finish=1573008690111136722,duration=10004414,event=fix_etc_hosts[0Ktravis_time:start:03237220[0Ktravis_time:end:03237220:start=1573008690115848032,finish=1573008690134581582,duration=18733550,event=fix_mvn_settings_xml[0Ktravis_time:start:0cc74d4e[0Ktravis_time:end:0cc74d4e:start=1573008690139322487,finish=1573008690149745371,duration=10422884,event=no_ipv6_localhost[0Ktravis_time:start:22df11c0[0Ktravis_time:end:22df11c0:start=1573008690154658979,finish=1573008690157436049,duration=2777070,event=fix_etc_mavenrc[0Ktravis_time:start:2b475681[0Ktravis_time:end:2b475681:start=1573008690162843566,finish=1573008690166227870,duration=3384304,event=fix_wwdr_certificate[0Ktravis_time:start:09c8c6e1[0Ktravis_time:end:09c8c6e1:start=1573008690171490059,finish=1573008690199318526,duration=27828467,event=put_localhost_first[0Ktravis_time:start:0c6cddca[0Ktravis_time:end:0c6cddca:start=1573008690203520149,finish=1573008690211510415,duration=7990266,event=home_paths[0Ktravis_time:start:0cc34fed[0Ktravis_time:end:0cc34fed:start=1573008690217385682,finish=1573008690230594897,duration=13209215,event=disable_initramfs[0Ktravis_time:start:1ea50d50[0Ktravis_time:end:1ea50d50:start=1573008690235700457,finish=1573008690575198268,duration=339497811,event=disable_ssh_roaming[0Ktravis_time:start:05d010b0[0Ktravis_time:end:05d010b0:start=1573008690580181098,finish=1573008690583245283,duration=3064185,event=debug_tools[0Ktravis_time:start:05d4c430[0Ktravis_time:end:05d4c430:start=1573008690587562076,finish=1573008690591084384,duration=3522308,event=uninstall_oclint[0Ktravis_time:start:14b4c1a5[0Ktravis_time:end:14b4c1a5:start=1573008690595608657,finish=1573008690601410328,duration=5801671,event=rvm_use[0Ktravis_time:start:00015a9e[0Ktravis_time:end:00015a9e:start=1573008690606208410,finish=1573008690618952035,duration=12743625,event=rm_etc_boto_cfg[0Ktravis_time:start:04ff8138[0Ktravis_time:end:04ff8138:start=1573008690624366451,finish=1573008690627110890,duration=2744439,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2c55c93c[0Ktravis_time:end:2c55c93c:start=1573008690631854995,finish=1573008690694835036,duration=62980041,event=enable_i386[0Ktravis_time:start:00c775fa[0Ktravis_time:end:00c775fa:start=1573008690699123862,finish=1573008690709067680,duration=9943818,event=update_rubygems[0Ktravis_time:start:16e33306[0Ktravis_time:end:16e33306:start=1573008690713669652,finish=1573008691753982870,duration=1040313218,event=ensure_path_components[0Ktravis_time:start:00c705d6[0Ktravis_time:end:00c705d6:start=1573008691758542931,finish=1573008691763170188,duration=4627257,event=redefine_curl[0Ktravis_time:start:2a3d4500[0Ktravis_time:end:2a3d4500:start=1573008691767690718,finish=1573008691829360833,duration=61670115,event=nonblock_pipe[0Ktravis_time:start:1509c4f8[0Ktravis_time:end:1509c4f8:start=1573008691833757250,finish=1573008694912279506,duration=3078522256,event=apt_get_update[0Ktravis_time:start:0d1eae3c[0Ktravis_time:end:0d1eae3c:start=1573008694917186631,finish=1573008694920237159,duration=3050528,event=deprecate_xcode_64[0Ktravis_time:start:06e7a548[0Ktravis_time:end:06e7a548:start=1573008694925745277,finish=1573008699742364327,duration=4816619050,event=update_heroku[0Ktravis_time:start:09a68591[0Ktravis_time:end:09a68591:start=1573008699746554498,finish=1573008699753708683,duration=7154185,event=shell_session_update[0Ktravis_time:start:14578cd7[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 4066
travis_fold:end:docker_mtu[0Ktravis_time:end:14578cd7:start=1573008699757793024,finish=1573008700959499139,duration=1201706115,event=set_docker_mtu[0Ktravis_time:start:017c1294[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:017c1294:start=1573008700964973269,finish=1573008701034981950,duration=70008681,event=resolvconf[0Ktravis_time:start:17d01756[0Ktravis_time:end:17d01756:start=1573008701039730138,finish=1573008701141436158,duration=101706020,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0e25c7ec[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0e25c7ec:start=1573008701230807368,finish=1573008702031552382,duration=800745014,event=configure[0Ktravis_time:start:2e6b8194[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2e6b8194:start=1573008702041318881,finish=1573008712171935212,duration=10130616331,event=configure[0Ktravis_time:start:0449a65c[0Ktravis_fold:start:services[0Ktravis_time:start:00c33cc3[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:00c33cc3:start=1573008712214605163,finish=1573008712229455224,duration=14850061,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:00c33cc3:start=1573008712214605163,finish=1573008715237638645,duration=3023033482,event=services[0Ktravis_time:start:0cb5940c[0Ktravis_time:end:0cb5940c:start=1573008715241919797,finish=1573008715244909531,duration=2989734,event=fix_ps4[0Ktravis_time:start:0006a480[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1ba99600[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1ba99600:start=1573008715267040406,finish=1573008721514949576,duration=6247909170,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:1ba99600:start=1573008715267040406,finish=1573008721968428282,duration=6701387876,event=checkout[0Ktravis_time:start:054b2640[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:054b2640:start=1573008721977480333,finish=1573008721988297959,duration=10817626,event=env[0Ktravis_time:start:13c93e00[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:13c93e00:start=1573008722000207068,finish=1573008722008420658,duration=8213590,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0010f3e0[0K$ python system_testing.py -s of-of
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
Digest: sha256:1f11411670b7e8e03ddcfb87356be9d1396f52a11746c00e8586258ce97e581e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/607962861/log.txt)