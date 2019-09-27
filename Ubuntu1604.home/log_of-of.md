 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/590479609) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/0cb7c0ec452f...92a2d96de651) 
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
travis_time:end:0e9e670a:start=1569603846416595354,finish=1569603846423187017,duration=6591663,event=show_system_info[0Ktravis_time:start:11dae4e4[0Ktravis_time:end:11dae4e4:start=1569603846426784496,finish=1569603846462404564,duration=35620068,event=rm_riak_source[0Ktravis_time:start:010ff8d8[0Ktravis_time:end:010ff8d8:start=1569603846466629449,finish=1569603846473711222,duration=7081773,event=fix_rwky_redis[0Ktravis_time:start:02f3220a[0Ktravis_time:end:02f3220a:start=1569603846477635798,finish=1569603846896903493,duration=419267695,event=wait_for_network[0Ktravis_time:start:01d35598[0Ktravis_time:end:01d35598:start=1569603846901569294,finish=1569603848476723413,duration=1575154119,event=update_apt_keys[0Ktravis_time:start:13ac40f0[0Ktravis_time:end:13ac40f0:start=1569603848482159709,finish=1569603849543140375,duration=1060980666,event=fix_hhvm_source[0Ktravis_time:start:0195a260[0Ktravis_time:end:0195a260:start=1569603849548580779,finish=1569603849560343688,duration=11762909,event=update_mongo_arch[0Ktravis_time:start:0617c140[0Ktravis_time:end:0617c140:start=1569603849565610395,finish=1569603849609645404,duration=44035009,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1ad5b7a6[0Ktravis_time:end:1ad5b7a6:start=1569603849616410301,finish=1569603849620519886,duration=4109585,event=update_glibc[0Ktravis_time:start:0d7cb854[0Ktravis_time:end:0d7cb854:start=1569603849625640263,finish=1569603849635367546,duration=9727283,event=clean_up_path[0Ktravis_time:start:109b89c8[0Ktravis_time:end:109b89c8:start=1569603849641367917,finish=1569603849651763962,duration=10396045,event=fix_resolv_conf[0Ktravis_time:start:09623c30[0Ktravis_time:end:09623c30:start=1569603849657177774,finish=1569603849669149443,duration=11971669,event=fix_etc_hosts[0Ktravis_time:start:021b0646[0Ktravis_time:end:021b0646:start=1569603849674479056,finish=1569603849685518856,duration=11039800,event=fix_mvn_settings_xml[0Ktravis_time:start:2dbe5ca8[0Ktravis_time:end:2dbe5ca8:start=1569603849691187215,finish=1569603849702345501,duration=11158286,event=no_ipv6_localhost[0Ktravis_time:start:04397d88[0Ktravis_time:end:04397d88:start=1569603849708301131,finish=1569603849711600979,duration=3299848,event=fix_etc_mavenrc[0Ktravis_time:start:13fd4b73[0Ktravis_time:end:13fd4b73:start=1569603849716427697,finish=1569603849720445773,duration=4018076,event=fix_wwdr_certificate[0Ktravis_time:start:193c9b60[0Ktravis_time:end:193c9b60:start=1569603849726517911,finish=1569603849754502242,duration=27984331,event=put_localhost_first[0Ktravis_time:start:058740e4[0Ktravis_time:end:058740e4:start=1569603849760470832,finish=1569603849764767371,duration=4296539,event=home_paths[0Ktravis_time:start:073140e6[0Ktravis_time:end:073140e6:start=1569603849770435092,finish=1569603849784509829,duration=14074737,event=disable_initramfs[0Ktravis_time:start:0f6e0100[0Ktravis_time:end:0f6e0100:start=1569603849791232515,finish=1569603850124590953,duration=333358438,event=disable_ssh_roaming[0Ktravis_time:start:273c0c29[0Ktravis_time:end:273c0c29:start=1569603850130177057,finish=1569603850134358601,duration=4181544,event=debug_tools[0Ktravis_time:start:2c35b32c[0Ktravis_time:end:2c35b32c:start=1569603850139279371,finish=1569603850144517467,duration=5238096,event=uninstall_oclint[0Ktravis_time:start:0c990bca[0Ktravis_time:end:0c990bca:start=1569603850149499445,finish=1569603850153812135,duration=4312690,event=rvm_use[0Ktravis_time:start:00f166ce[0Ktravis_time:end:00f166ce:start=1569603850158208010,finish=1569603850171076187,duration=12868177,event=rm_etc_boto_cfg[0Ktravis_time:start:034d9d00[0Ktravis_time:end:034d9d00:start=1569603850176130735,finish=1569603850182264501,duration=6133766,event=rm_oraclejdk8_symlink[0Ktravis_time:start:001dbf1a[0Ktravis_time:end:001dbf1a:start=1569603850186917050,finish=1569603850243627093,duration=56710043,event=enable_i386[0Ktravis_time:start:017fe8da[0Ktravis_time:end:017fe8da:start=1569603850248876014,finish=1569603850253733629,duration=4857615,event=update_rubygems[0Ktravis_time:start:18486640[0Ktravis_time:end:18486640:start=1569603850258840927,finish=1569603851336351212,duration=1077510285,event=ensure_path_components[0Ktravis_time:start:26cde7b0[0Ktravis_time:end:26cde7b0:start=1569603851341807922,finish=1569603851345229165,duration=3421243,event=redefine_curl[0Ktravis_time:start:013adcfc[0Ktravis_time:end:013adcfc:start=1569603851350451355,finish=1569603851409783412,duration=59332057,event=nonblock_pipe[0Ktravis_time:start:040f63fc[0Ktravis_time:end:040f63fc:start=1569603851414443490,finish=1569603851460491836,duration=46048346,event=apt_get_update[0Ktravis_time:start:0413cacc[0Ktravis_time:end:0413cacc:start=1569603851466256621,finish=1569603851469494465,duration=3237844,event=deprecate_xcode_64[0Ktravis_time:start:2af9a48f[0Ktravis_time:end:2af9a48f:start=1569603851475102401,finish=1569603856070865173,duration=4595762772,event=update_heroku[0Ktravis_time:start:025cf897[0Ktravis_time:end:025cf897:start=1569603856076053750,finish=1569603856079059867,duration=3006117,event=shell_session_update[0Ktravis_time:start:2cdf7806[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3891
travis_fold:end:docker_mtu[0Ktravis_time:end:2cdf7806:start=1569603856083943373,finish=1569603857284181165,duration=1200237792,event=set_docker_mtu[0Ktravis_time:start:054cbced[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:054cbced:start=1569603857289557144,finish=1569603857362530875,duration=72973731,event=resolvconf[0Ktravis_time:start:055c77a9[0Ktravis_time:end:055c77a9:start=1569603857368363664,finish=1569603857471095256,duration=102731592,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:28a4d958[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:28a4d958:start=1569603857567136266,finish=1569603857940347337,duration=373211071,event=configure[0Ktravis_time:start:0a928124[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a928124:start=1569603857944819123,finish=1569603871672950536,duration=13728131413,event=configure[0Ktravis_time:start:189a01d0[0Ktravis_fold:start:services[0Ktravis_time:start:04f72a34[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:04f72a34:start=1569603871700939679,finish=1569603871717349778,duration=16410099,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:04f72a34:start=1569603871700939679,finish=1569603874724808171,duration=3023868492,event=services[0Ktravis_time:start:027905e2[0Ktravis_time:end:027905e2:start=1569603874731360223,finish=1569603874734645188,duration=3284965,event=fix_ps4[0Ktravis_time:start:217e5fb0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:280d6754[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:280d6754:start=1569603874744346078,finish=1569603881139412283,duration=6395066205,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 92a2d96de651986b4a651cb923faf4ab421973a6
travis_fold:end:git.checkout[0K
travis_time:end:280d6754:start=1569603874744346078,finish=1569603881261310534,duration=6516964456,event=checkout[0Ktravis_time:start:02713d46[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:02713d46:start=1569603881267049995,finish=1569603881280632301,duration=13582306,event=env[0Ktravis_time:start:0c75a6a0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0c75a6a0:start=1569603881286559721,finish=1569603881293982725,duration=7423004,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:061c1226[0K$ python system_testing.py -s of-of
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
Digest: sha256:17f5650d84b1edf1188baa12b43a57878d5324749f7f656f54914c06ff105fb0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/590479623/log.txt)