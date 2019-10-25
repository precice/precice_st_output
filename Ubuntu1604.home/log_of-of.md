## Status: Passing 
Build: [1023](https://travis-ci.org/precice/systemtests/builds/602890333) 

Job: [1023.14](https://travis-ci.org/precice/systemtests/jobs/602890347) 

Triggered by: [push](https://github.com/precice/systemtests/compare/14ba7f611330...9921a3e9e3f7) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:05caee5f:start=1572021704625483604,finish=1572021704632480444,duration=6996840,event=show_system_info[0Ktravis_time:start:3486bf4c[0Ktravis_time:end:3486bf4c:start=1572021704636052463,finish=1572021704661315525,duration=25263062,event=rm_riak_source[0Ktravis_time:start:1fce9fea[0Ktravis_time:end:1fce9fea:start=1572021704668329771,finish=1572021704675917969,duration=7588198,event=fix_rwky_redis[0Ktravis_time:start:0371a964[0Ktravis_time:end:0371a964:start=1572021704680582117,finish=1572021705186213639,duration=505631522,event=wait_for_network[0Ktravis_time:start:0279a0c2[0Ktravis_time:end:0279a0c2:start=1572021705191674708,finish=1572021706270889891,duration=1079215183,event=update_apt_keys[0Ktravis_time:start:33088dc4[0Ktravis_time:end:33088dc4:start=1572021706277055675,finish=1572021707405162149,duration=1128106474,event=fix_hhvm_source[0Ktravis_time:start:1b27608b[0Ktravis_time:end:1b27608b:start=1572021707410545225,finish=1572021707421955312,duration=11410087,event=update_mongo_arch[0Ktravis_time:start:2092238e[0Ktravis_time:end:2092238e:start=1572021707427461972,finish=1572021707473428831,duration=45966859,event=fix_sudo_enabled_trusty[0Ktravis_time:start:110221e8[0Ktravis_time:end:110221e8:start=1572021707478694897,finish=1572021707482257022,duration=3562125,event=update_glibc[0Ktravis_time:start:14badb58[0Ktravis_time:end:14badb58:start=1572021707487325212,finish=1572021707498554329,duration=11229117,event=clean_up_path[0Ktravis_time:start:097fd5a1[0Ktravis_time:end:097fd5a1:start=1572021707503760824,finish=1572021707514802462,duration=11041638,event=fix_resolv_conf[0Ktravis_time:start:1a149a46[0Ktravis_time:end:1a149a46:start=1572021707519701723,finish=1572021707531294871,duration=11593148,event=fix_etc_hosts[0Ktravis_time:start:06ad6ba4[0Ktravis_time:end:06ad6ba4:start=1572021707535828664,finish=1572021707548484220,duration=12655556,event=fix_mvn_settings_xml[0Ktravis_time:start:0e2e6560[0Ktravis_time:end:0e2e6560:start=1572021707553971568,finish=1572021707566473314,duration=12501746,event=no_ipv6_localhost[0Ktravis_time:start:06364f74[0Ktravis_time:end:06364f74:start=1572021707572471556,finish=1572021707576058132,duration=3586576,event=fix_etc_mavenrc[0Ktravis_time:start:02456889[0Ktravis_time:end:02456889:start=1572021707580982349,finish=1572021707586727912,duration=5745563,event=fix_wwdr_certificate[0Ktravis_time:start:081e9500[0Ktravis_time:end:081e9500:start=1572021707592094749,finish=1572021707623118311,duration=31023562,event=put_localhost_first[0Ktravis_time:start:09d2e670[0Ktravis_time:end:09d2e670:start=1572021707628186935,finish=1572021707632565347,duration=4378412,event=home_paths[0Ktravis_time:start:03d937d0[0Ktravis_time:end:03d937d0:start=1572021707639245076,finish=1572021707656398580,duration=17153504,event=disable_initramfs[0Ktravis_time:start:0ec739da[0Ktravis_time:end:0ec739da:start=1572021707661826244,finish=1572021707920085024,duration=258258780,event=disable_ssh_roaming[0Ktravis_time:start:0157e3f4[0Ktravis_time:end:0157e3f4:start=1572021707925699368,finish=1572021707928915320,duration=3215952,event=debug_tools[0Ktravis_time:start:00776c73[0Ktravis_time:end:00776c73:start=1572021707934098112,finish=1572021707938166000,duration=4067888,event=uninstall_oclint[0Ktravis_time:start:235bf960[0Ktravis_time:end:235bf960:start=1572021707943645292,finish=1572021707949703975,duration=6058683,event=rvm_use[0Ktravis_time:start:088d1200[0Ktravis_time:end:088d1200:start=1572021707954719581,finish=1572021707964625518,duration=9905937,event=rm_etc_boto_cfg[0Ktravis_time:start:224a5df6[0Ktravis_time:end:224a5df6:start=1572021707971672927,finish=1572021707975362369,duration=3689442,event=rm_oraclejdk8_symlink[0Ktravis_time:start:14726028[0Ktravis_time:end:14726028:start=1572021707980993101,finish=1572021708042625424,duration=61632323,event=enable_i386[0Ktravis_time:start:0b64f14e[0Ktravis_time:end:0b64f14e:start=1572021708048311004,finish=1572021708053816151,duration=5505147,event=update_rubygems[0Ktravis_time:start:112fc081[0Ktravis_time:end:112fc081:start=1572021708061610096,finish=1572021709146939078,duration=1085328982,event=ensure_path_components[0Ktravis_time:start:206ecbf8[0Ktravis_time:end:206ecbf8:start=1572021709152311741,finish=1572021709155845972,duration=3534231,event=redefine_curl[0Ktravis_time:start:2d4cf43d[0Ktravis_time:end:2d4cf43d:start=1572021709161483616,finish=1572021709222373764,duration=60890148,event=nonblock_pipe[0Ktravis_time:start:02f8e4d4[0Ktravis_time:end:02f8e4d4:start=1572021709228235766,finish=1572021712278503021,duration=3050267255,event=apt_get_update[0Ktravis_time:start:07bce984[0Ktravis_time:end:07bce984:start=1572021712285554624,finish=1572021712290097591,duration=4542967,event=deprecate_xcode_64[0Ktravis_time:start:01c47d2c[0Ktravis_time:end:01c47d2c:start=1572021712297420440,finish=1572021716902383520,duration=4604963080,event=update_heroku[0Ktravis_time:start:18061812[0Ktravis_time:end:18061812:start=1572021716908909516,finish=1572021716913857117,duration=4947601,event=shell_session_update[0Ktravis_time:start:094d0878[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3851
travis_fold:end:docker_mtu[0Ktravis_time:end:094d0878:start=1572021716919650560,finish=1572021718118992459,duration=1199341899,event=set_docker_mtu[0Ktravis_time:start:01b8ecd0[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:01b8ecd0:start=1572021718126306511,finish=1572021718203560622,duration=77254111,event=resolvconf[0Ktravis_time:start:1497c6cb[0Ktravis_time:end:1497c6cb:start=1572021718209660556,finish=1572021718319137565,duration=109477009,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0bf42ed0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0bf42ed0:start=1572021718415848550,finish=1572021718811601370,duration=395752820,event=configure[0Ktravis_time:start:11d643c0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:11d643c0:start=1572021718817688076,finish=1572021734073904154,duration=15256216078,event=configure[0Ktravis_time:start:009838c0[0Ktravis_fold:start:services[0Ktravis_time:start:17181f52[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:17181f52:start=1572021734101183382,finish=1572021734116936581,duration=15753199,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:17181f52:start=1572021734101183382,finish=1572021737124026701,duration=3022843319,event=services[0Ktravis_time:start:1c4384d0[0Ktravis_time:end:1c4384d0:start=1572021737130103556,finish=1572021737133387586,duration=3284030,event=fix_ps4[0Ktravis_time:start:138373e9[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1e1b7ab1[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1e1b7ab1:start=1572021737147798138,finish=1572021743645268152,duration=6497470014,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 9921a3e9e3f7596df67493847bbc01f17a3b226e
travis_fold:end:git.checkout[0K
travis_time:end:1e1b7ab1:start=1572021737147798138,finish=1572021744218695726,duration=7070897588,event=checkout[0Ktravis_time:start:0cb338d5[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0cb338d5:start=1572021744224046294,finish=1572021744235819623,duration=11773329,event=env[0Ktravis_time:start:09a758ea[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:09a758ea:start=1572021744242441324,finish=1572021744255840544,duration=13399220,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:024b54e4[0K$ python system_testing.py -s of-of
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
Digest: sha256:d1528af363df954e5a3be334a2d22d5061e1360a624636367fe2b227c6d1addd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:024b54e4:start=1572021744642241489,finish=1572021866850098645,duration=122207857156,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:025bb607[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602890347/log.txt)