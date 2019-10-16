 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598441565) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/478596e1ce45) 
## Last 100 lines of the job log at the moment of push...
```
 [34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:0b7a2f4b:start=1571194498879772894,finish=1571194498886188779,duration=6415885,event=show_system_info[0Ktravis_time:start:160a9bcb[0Ktravis_time:end:160a9bcb:start=1571194498889197262,finish=1571194498914577308,duration=25380046,event=rm_riak_source[0Ktravis_time:start:0a54d200[0Ktravis_time:end:0a54d200:start=1571194498917860247,finish=1571194498927381608,duration=9521361,event=fix_rwky_redis[0Ktravis_time:start:0c5d1562[0Ktravis_time:end:0c5d1562:start=1571194498930876705,finish=1571194499355260291,duration=424383586,event=wait_for_network[0Ktravis_time:start:1a8281b3[0Ktravis_time:end:1a8281b3:start=1571194499360934933,finish=1571194500939147412,duration=1578212479,event=update_apt_keys[0Ktravis_time:start:0112eed0[0Ktravis_time:end:0112eed0:start=1571194500944188954,finish=1571194501964730977,duration=1020542023,event=fix_hhvm_source[0Ktravis_time:start:11e22b30[0Ktravis_time:end:11e22b30:start=1571194501969726243,finish=1571194501979691935,duration=9965692,event=update_mongo_arch[0Ktravis_time:start:02f3c430[0Ktravis_time:end:02f3c430:start=1571194501984395509,finish=1571194502026595538,duration=42200029,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0b820549[0Ktravis_time:end:0b820549:start=1571194502031165308,finish=1571194502033891611,duration=2726303,event=update_glibc[0Ktravis_time:start:015f4005[0Ktravis_time:end:015f4005:start=1571194502038467134,finish=1571194502047327151,duration=8860017,event=clean_up_path[0Ktravis_time:start:03226ec0[0Ktravis_time:end:03226ec0:start=1571194502052047876,finish=1571194502061573999,duration=9526123,event=fix_resolv_conf[0Ktravis_time:start:1554df90[0Ktravis_time:end:1554df90:start=1571194502067451299,finish=1571194502077569664,duration=10118365,event=fix_etc_hosts[0Ktravis_time:start:1dfdcc0c[0Ktravis_time:end:1dfdcc0c:start=1571194502083402720,finish=1571194502092472672,duration=9069952,event=fix_mvn_settings_xml[0Ktravis_time:start:3b437770[0Ktravis_time:end:3b437770:start=1571194502097760019,finish=1571194502109453423,duration=11693404,event=no_ipv6_localhost[0Ktravis_time:start:0ea131a6[0Ktravis_time:end:0ea131a6:start=1571194502114237904,finish=1571194502117521667,duration=3283763,event=fix_etc_mavenrc[0Ktravis_time:start:050a9616[0Ktravis_time:end:050a9616:start=1571194502123921089,finish=1571194502127926208,duration=4005119,event=fix_wwdr_certificate[0Ktravis_time:start:181e5526[0Ktravis_time:end:181e5526:start=1571194502132819463,finish=1571194502158940662,duration=26121199,event=put_localhost_first[0Ktravis_time:start:008b4aec[0Ktravis_time:end:008b4aec:start=1571194502165078218,finish=1571194502169428143,duration=4349925,event=home_paths[0Ktravis_time:start:0cd3d274[0Ktravis_time:end:0cd3d274:start=1571194502174708698,finish=1571194502189599627,duration=14890929,event=disable_initramfs[0Ktravis_time:start:0c4f0a68[0Ktravis_time:end:0c4f0a68:start=1571194502194380289,finish=1571194502512204901,duration=317824612,event=disable_ssh_roaming[0Ktravis_time:start:0a7f071a[0Ktravis_time:end:0a7f071a:start=1571194502517441961,finish=1571194502521857421,duration=4415460,event=debug_tools[0Ktravis_time:start:08136f00[0Ktravis_time:end:08136f00:start=1571194502527720975,finish=1571194502531625306,duration=3904331,event=uninstall_oclint[0Ktravis_time:start:018459cb[0Ktravis_time:end:018459cb:start=1571194502536568599,finish=1571194502542915594,duration=6346995,event=rvm_use[0Ktravis_time:start:0cab0998[0Ktravis_time:end:0cab0998:start=1571194502547595110,finish=1571194502555968059,duration=8372949,event=rm_etc_boto_cfg[0Ktravis_time:start:1552d100[0Ktravis_time:end:1552d100:start=1571194502563303073,finish=1571194502566044549,duration=2741476,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0c7d94c0[0Ktravis_time:end:0c7d94c0:start=1571194502571359444,finish=1571194502628672300,duration=57312856,event=enable_i386[0Ktravis_time:start:059309f7[0Ktravis_time:end:059309f7:start=1571194502633398710,finish=1571194502637841202,duration=4442492,event=update_rubygems[0Ktravis_time:start:0edc00e1[0Ktravis_time:end:0edc00e1:start=1571194502642165295,finish=1571194503654283249,duration=1012117954,event=ensure_path_components[0Ktravis_time:start:11462f92[0Ktravis_time:end:11462f92:start=1571194503659433746,finish=1571194503662520018,duration=3086272,event=redefine_curl[0Ktravis_time:start:1949fbd4[0Ktravis_time:end:1949fbd4:start=1571194503667241485,finish=1571194503721052453,duration=53810968,event=nonblock_pipe[0Ktravis_time:start:09a12d00[0Ktravis_time:end:09a12d00:start=1571194503726198174,finish=1571194503767394319,duration=41196145,event=apt_get_update[0Ktravis_time:start:0645f541[0Ktravis_time:end:0645f541:start=1571194503772381073,finish=1571194503776152771,duration=3771698,event=deprecate_xcode_64[0Ktravis_time:start:02395b14[0Ktravis_time:end:02395b14:start=1571194503782495133,finish=1571194508358208529,duration=4575713396,event=update_heroku[0Ktravis_time:start:0758b686[0Ktravis_time:end:0758b686:start=1571194508363490214,finish=1571194508366752710,duration=3262496,event=shell_session_update[0Ktravis_time:start:02fc1ce4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3964
travis_fold:end:docker_mtu[0Ktravis_time:end:02fc1ce4:start=1571194508371120317,finish=1571194509581350678,duration=1210230361,event=set_docker_mtu[0Ktravis_time:start:0bf0e8b1[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0bf0e8b1:start=1571194509585715502,finish=1571194509649822818,duration=64107316,event=resolvconf[0Ktravis_time:start:0508526d[0Ktravis_time:end:0508526d:start=1571194509654369966,finish=1571194509754374864,duration=100004898,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:07632732[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:07632732:start=1571194509838879241,finish=1571194510130307411,duration=291428170,event=configure[0Ktravis_time:start:0a9ece32[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a9ece32:start=1571194510135967594,finish=1571194520437977628,duration=10302010034,event=configure[0Ktravis_time:start:24828e68[0Ktravis_fold:start:services[0Ktravis_time:start:0b3fd91e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0b3fd91e:start=1571194520464734650,finish=1571194520479415943,duration=14681293,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0b3fd91e:start=1571194520464734650,finish=1571194523485675782,duration=3020941132,event=services[0Ktravis_time:start:10ac8d96[0Ktravis_time:end:10ac8d96:start=1571194523490647795,finish=1571194523493493478,duration=2845683,event=fix_ps4[0Ktravis_time:start:008d6706[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0d90fa08[0K$ git clone --depth=50 --branch=EderK-allow_job_failure https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0d90fa08:start=1571194523502444021,finish=1571194529723576252,duration=6221132231,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 478596e1ce45f10d128c4f914460a3fe747c5fdd
travis_fold:end:git.checkout[0K
travis_time:end:0d90fa08:start=1571194523502444021,finish=1571194530358948755,duration=6856504734,event=checkout[0Ktravis_time:start:0501886b[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0501886b:start=1571194530364667801,finish=1571194530376396316,duration=11728515,event=env[0Ktravis_time:start:071fd5d8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:071fd5d8:start=1571194530382476145,finish=1571194530388676056,duration=6199911,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0064e150[0K$ python system_testing.py -s of-of
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
Digest: sha256:8c28a96b26585c04af5ec1ea6f96daea73118195658df2bf9cf7cb3dd45ac81a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
 ```
[Full job log](https://api.travis-ci.org/v3/job/598441584/log.txt)