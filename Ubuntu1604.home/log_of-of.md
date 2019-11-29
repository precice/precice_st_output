## Status: Passing 
Build: [1205](https://travis-ci.org/precice/systemtests/builds/618334138) 

Job: [1205.14](https://travis-ci.org/precice/systemtests/jobs/618334152) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f6ac64c472af...3b2ed1c3a41a) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:system_info[0K
travis_time:end:18ffba78:start=1574986650866076107,finish=1574986650872460736,duration=6384629,event=show_system_info[0Ktravis_time:start:214f5490[0Ktravis_time:end:214f5490:start=1574986650878198283,finish=1574986650905514273,duration=27315990,event=rm_riak_source[0Ktravis_time:start:03b8b1a4[0Ktravis_time:end:03b8b1a4:start=1574986650910019310,finish=1574986650921425446,duration=11406136,event=fix_rwky_redis[0Ktravis_time:start:216d2b0a[0Ktravis_time:end:216d2b0a:start=1574986650925146320,finish=1574986651513885378,duration=588739058,event=wait_for_network[0Ktravis_time:start:0c34a16c[0Ktravis_time:end:0c34a16c:start=1574986651519539891,finish=1574986653111608769,duration=1592068878,event=update_apt_keys[0Ktravis_time:start:1a01e400[0Ktravis_time:end:1a01e400:start=1574986653117460257,finish=1574986654224349945,duration=1106889688,event=fix_hhvm_source[0Ktravis_time:start:08296848[0Ktravis_time:end:08296848:start=1574986654229586847,finish=1574986654241249440,duration=11662593,event=update_mongo_arch[0Ktravis_time:start:0f137896[0Ktravis_time:end:0f137896:start=1574986654246714863,finish=1574986654294179360,duration=47464497,event=fix_sudo_enabled_trusty[0Ktravis_time:start:015b7356[0Ktravis_time:end:015b7356:start=1574986654299987736,finish=1574986654303220401,duration=3232665,event=update_glibc[0Ktravis_time:start:09d9e230[0Ktravis_time:end:09d9e230:start=1574986654309002860,finish=1574986654321059470,duration=12056610,event=clean_up_path[0Ktravis_time:start:185362d4[0Ktravis_time:end:185362d4:start=1574986654326427223,finish=1574986654337685090,duration=11257867,event=fix_resolv_conf[0Ktravis_time:start:0a369bbc[0Ktravis_time:end:0a369bbc:start=1574986654342919149,finish=1574986654355204600,duration=12285451,event=fix_etc_hosts[0Ktravis_time:start:09ded8f6[0Ktravis_time:end:09ded8f6:start=1574986654359933639,finish=1574986654369285764,duration=9352125,event=fix_mvn_settings_xml[0Ktravis_time:start:01c01868[0Ktravis_time:end:01c01868:start=1574986654374382004,finish=1574986654385859001,duration=11476997,event=no_ipv6_localhost[0Ktravis_time:start:1944c83a[0Ktravis_time:end:1944c83a:start=1574986654391040429,finish=1574986654394295300,duration=3254871,event=fix_etc_mavenrc[0Ktravis_time:start:0d07c058[0Ktravis_time:end:0d07c058:start=1574986654400754962,finish=1574986654405016049,duration=4261087,event=fix_wwdr_certificate[0Ktravis_time:start:0c963234[0Ktravis_time:end:0c963234:start=1574986654409858247,finish=1574986654438949360,duration=29091113,event=put_localhost_first[0Ktravis_time:start:2a5ca932[0Ktravis_time:end:2a5ca932:start=1574986654444223305,finish=1574986654448610314,duration=4387009,event=home_paths[0Ktravis_time:start:13e20a05[0Ktravis_time:end:13e20a05:start=1574986654453671645,finish=1574986654468603740,duration=14932095,event=disable_initramfs[0Ktravis_time:start:1a1d92ac[0Ktravis_time:end:1a1d92ac:start=1574986654473783678,finish=1574986654789867216,duration=316083538,event=disable_ssh_roaming[0Ktravis_time:start:2602e000[0Ktravis_time:end:2602e000:start=1574986654796703082,finish=1574986654800086854,duration=3383772,event=debug_tools[0Ktravis_time:start:2c0376e8[0Ktravis_time:end:2c0376e8:start=1574986654804709042,finish=1574986654809085438,duration=4376396,event=uninstall_oclint[0Ktravis_time:start:189abe4c[0Ktravis_time:end:189abe4c:start=1574986654816429887,finish=1574986654820255288,duration=3825401,event=rvm_use[0Ktravis_time:start:08c49a0f[0Ktravis_time:end:08c49a0f:start=1574986654824790242,finish=1574986654833944804,duration=9154562,event=rm_etc_boto_cfg[0Ktravis_time:start:0aef2508[0Ktravis_time:end:0aef2508:start=1574986654839621921,finish=1574986654842762556,duration=3140635,event=rm_oraclejdk8_symlink[0Ktravis_time:start:231555bc[0Ktravis_time:end:231555bc:start=1574986654847620604,finish=1574986654905995245,duration=58374641,event=enable_i386[0Ktravis_time:start:094deb40[0Ktravis_time:end:094deb40:start=1574986654912406223,finish=1574986654917723238,duration=5317015,event=update_rubygems[0Ktravis_time:start:08c5be0c[0Ktravis_time:end:08c5be0c:start=1574986654923615686,finish=1574986656080119839,duration=1156504153,event=ensure_path_components[0Ktravis_time:start:2171d6ba[0Ktravis_time:end:2171d6ba:start=1574986656086185220,finish=1574986656089422948,duration=3237728,event=redefine_curl[0Ktravis_time:start:022bb829[0Ktravis_time:end:022bb829:start=1574986656095410450,finish=1574986656155374441,duration=59963991,event=nonblock_pipe[0Ktravis_time:start:0340f968[0Ktravis_time:end:0340f968:start=1574986656160558022,finish=1574986659211894681,duration=3051336659,event=apt_get_update[0Ktravis_time:start:00d1eebe[0Ktravis_time:end:00d1eebe:start=1574986659219010533,finish=1574986659223133387,duration=4122854,event=deprecate_xcode_64[0Ktravis_time:start:37d773b4[0Ktravis_time:end:37d773b4:start=1574986659228758532,finish=1574986664274235319,duration=5045476787,event=update_heroku[0Ktravis_time:start:2ec525ec[0Ktravis_time:end:2ec525ec:start=1574986664279566046,finish=1574986664283262438,duration=3696392,event=shell_session_update[0Ktravis_time:start:35d971e8[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3960
travis_fold:end:docker_mtu[0Ktravis_time:end:35d971e8:start=1574986664289126573,finish=1574986665490947412,duration=1201820839,event=set_docker_mtu[0Ktravis_time:start:00aad167[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:00aad167:start=1574986665496781892,finish=1574986665570422794,duration=73640902,event=resolvconf[0Ktravis_time:start:04a4f204[0Ktravis_time:end:04a4f204:start=1574986665575198354,finish=1574986665674867547,duration=99669193,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:17b323d0[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:17b323d0:start=1574986665765029587,finish=1574986666054386551,duration=289356964,event=configure[0Ktravis_time:start:131b9f92[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:131b9f92:start=1574986666060313489,finish=1574986677766336072,duration=11706022583,event=configure[0Ktravis_time:start:1eb3a460[0Ktravis_fold:start:services[0Ktravis_time:start:2b7c1fb4[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:2b7c1fb4:start=1574986677795369213,finish=1574986677811663094,duration=16293881,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2b7c1fb4:start=1574986677795369213,finish=1574986680819237587,duration=3023868374,event=services[0Ktravis_time:start:21c5929a[0Ktravis_time:end:21c5929a:start=1574986680824437224,finish=1574986680827682887,duration=3245663,event=fix_ps4[0Ktravis_time:start:04c11700[0K
travis_fold:start:git.checkout[0Ktravis_time:start:03c1ac94[0K$ git clone --depth=50 --branch=compatibility_PR_576_on_[secure]_core https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:03c1ac94:start=1574986680838879794,finish=1574986687223651951,duration=6384772157,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3b2ed1c3a41a6dfa009f9cc83cedd5535382de8c
travis_fold:end:git.checkout[0K
travis_time:end:03c1ac94:start=1574986680838879794,finish=1574986687416023546,duration=6577143752,event=checkout[0Ktravis_time:start:21d79362[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:21d79362:start=1574986687422158611,finish=1574986687432451135,duration=10292524,event=env[0Ktravis_time:start:26795ca4[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:26795ca4:start=1574986687438217273,finish=1574986687445633046,duration=7415773,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0aa421f8[0K$ python system_testing.py -s of-of
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
Digest: sha256:e64d281cd35453d9fd31b71b7b9bc5d2f481aff68bb487c09f73e28a34da94d1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0aa421f8:start=1574986687838953807,finish=1574986808870091490,duration=121031137683,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618334152/log.txt)