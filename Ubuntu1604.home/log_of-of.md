## Status: Passing 
Build: [1027](https://travis-ci.org/precice/systemtests/builds/603099773) 

Job: [1027.18](https://travis-ci.org/precice/systemtests/jobs/603099793) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:153ef465:start=1572057462730644249,finish=1572057462736544357,duration=5900108,event=show_system_info[0Ktravis_time:start:1cf05f30[0Ktravis_time:end:1cf05f30:start=1572057462739549906,finish=1572057462764890862,duration=25340956,event=rm_riak_source[0Ktravis_time:start:0ccb150e[0Ktravis_time:end:0ccb150e:start=1572057462768751949,finish=1572057462777056007,duration=8304058,event=fix_rwky_redis[0Ktravis_time:start:2cddda64[0Ktravis_time:end:2cddda64:start=1572057462780287348,finish=1572057463168155047,duration=387867699,event=wait_for_network[0Ktravis_time:start:00d4b13a[0Ktravis_time:end:00d4b13a:start=1572057463173779149,finish=1572057464737331288,duration=1563552139,event=update_apt_keys[0Ktravis_time:start:0d42d11b[0Ktravis_time:end:0d42d11b:start=1572057464742287801,finish=1572057465768485934,duration=1026198133,event=fix_hhvm_source[0Ktravis_time:start:001696d4[0Ktravis_time:end:001696d4:start=1572057465773577190,finish=1572057465784918610,duration=11341420,event=update_mongo_arch[0Ktravis_time:start:134c9c8b[0Ktravis_time:end:134c9c8b:start=1572057465789615742,finish=1572057465830539051,duration=40923309,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1bfb0208[0Ktravis_time:end:1bfb0208:start=1572057465835280623,finish=1572057465838115120,duration=2834497,event=update_glibc[0Ktravis_time:start:05726eec[0Ktravis_time:end:05726eec:start=1572057465842737076,finish=1572057465851830926,duration=9093850,event=clean_up_path[0Ktravis_time:start:04acee43[0Ktravis_time:end:04acee43:start=1572057465856006539,finish=1572057465867183123,duration=11176584,event=fix_resolv_conf[0Ktravis_time:start:1aaeb97a[0Ktravis_time:end:1aaeb97a:start=1572057465871832958,finish=1572057465881185121,duration=9352163,event=fix_etc_hosts[0Ktravis_time:start:0ef41244[0Ktravis_time:end:0ef41244:start=1572057465886625278,finish=1572057465895978612,duration=9353334,event=fix_mvn_settings_xml[0Ktravis_time:start:0e5fc6dc[0Ktravis_time:end:0e5fc6dc:start=1572057465900087751,finish=1572057465911801846,duration=11714095,event=no_ipv6_localhost[0Ktravis_time:start:180c0e8c[0Ktravis_time:end:180c0e8c:start=1572057465916426798,finish=1572057465919158896,duration=2732098,event=fix_etc_mavenrc[0Ktravis_time:start:16b0cc70[0Ktravis_time:end:16b0cc70:start=1572057465923849898,finish=1572057465929666383,duration=5816485,event=fix_wwdr_certificate[0Ktravis_time:start:22f37d96[0Ktravis_time:end:22f37d96:start=1572057465935722166,finish=1572057465962578239,duration=26856073,event=put_localhost_first[0Ktravis_time:start:0c15bfa0[0Ktravis_time:end:0c15bfa0:start=1572057465967784458,finish=1572057465971439209,duration=3654751,event=home_paths[0Ktravis_time:start:003e94b4[0Ktravis_time:end:003e94b4:start=1572057465976862596,finish=1572057465990011737,duration=13149141,event=disable_initramfs[0Ktravis_time:start:13a97dac[0Ktravis_time:end:13a97dac:start=1572057465993653129,finish=1572057466299218778,duration=305565649,event=disable_ssh_roaming[0Ktravis_time:start:21a89768[0Ktravis_time:end:21a89768:start=1572057466303835421,finish=1572057466307274735,duration=3439314,event=debug_tools[0Ktravis_time:start:31dae8b0[0Ktravis_time:end:31dae8b0:start=1572057466311692367,finish=1572057466316170435,duration=4478068,event=uninstall_oclint[0Ktravis_time:start:352d4c11[0Ktravis_time:end:352d4c11:start=1572057466320417191,finish=1572057466324504936,duration=4087745,event=rvm_use[0Ktravis_time:start:20862fe4[0Ktravis_time:end:20862fe4:start=1572057466328105545,finish=1572057466340613703,duration=12508158,event=rm_etc_boto_cfg[0Ktravis_time:start:2235f768[0Ktravis_time:end:2235f768:start=1572057466344932270,finish=1572057466348085461,duration=3153191,event=rm_oraclejdk8_symlink[0Ktravis_time:start:05d97f9c[0Ktravis_time:end:05d97f9c:start=1572057466351750779,finish=1572057466416839621,duration=65088842,event=enable_i386[0Ktravis_time:start:007889be[0Ktravis_time:end:007889be:start=1572057466422257262,finish=1572057466426347995,duration=4090733,event=update_rubygems[0Ktravis_time:start:1d5185a7[0Ktravis_time:end:1d5185a7:start=1572057466431278620,finish=1572057467431770153,duration=1000491533,event=ensure_path_components[0Ktravis_time:start:12e76969[0Ktravis_time:end:12e76969:start=1572057467438276401,finish=1572057467441607065,duration=3330664,event=redefine_curl[0Ktravis_time:start:0a36af04[0Ktravis_time:end:0a36af04:start=1572057467445543789,finish=1572057467502764731,duration=57220942,event=nonblock_pipe[0Ktravis_time:start:07b5eb98[0Ktravis_time:end:07b5eb98:start=1572057467507362828,finish=1572057470576505253,duration=3069142425,event=apt_get_update[0Ktravis_time:start:0b4de644[0Ktravis_time:end:0b4de644:start=1572057470581771544,finish=1572057470585157811,duration=3386267,event=deprecate_xcode_64[0Ktravis_time:start:0615ce46[0Ktravis_time:end:0615ce46:start=1572057470590605698,finish=1572057475197795530,duration=4607189832,event=update_heroku[0Ktravis_time:start:16bd04af[0Ktravis_time:end:16bd04af:start=1572057475203124397,finish=1572057475206281842,duration=3157445,event=shell_session_update[0Ktravis_time:start:0d902abc[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3855
travis_fold:end:docker_mtu[0Ktravis_time:end:0d902abc:start=1572057475211417264,finish=1572057476411163644,duration=1199746380,event=set_docker_mtu[0Ktravis_time:start:01d36ce8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:01d36ce8:start=1572057476418485189,finish=1572057476482142051,duration=63656862,event=resolvconf[0Ktravis_time:start:2693b708[0Ktravis_time:end:2693b708:start=1572057476486506523,finish=1572057476589384827,duration=102878304,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0ac60b07[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0ac60b07:start=1572057476671504749,finish=1572057477127823224,duration=456318475,event=configure[0Ktravis_time:start:0038dcc0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0038dcc0:start=1572057477132631195,finish=1572057486723832546,duration=9591201351,event=configure[0Ktravis_time:start:1923d318[0Ktravis_fold:start:services[0Ktravis_time:start:07195638[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:07195638:start=1572057486748513979,finish=1572057486762098403,duration=13584424,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:07195638:start=1572057486748513979,finish=1572057489768988106,duration=3020474127,event=services[0Ktravis_time:start:01d8c863[0Ktravis_time:end:01d8c863:start=1572057489774620084,finish=1572057489777485253,duration=2865169,event=fix_ps4[0Ktravis_time:start:0eb2d032[0K
travis_fold:start:git.checkout[0Ktravis_time:start:2df2ef95[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:2df2ef95:start=1572057489789562588,finish=1572057497954984989,duration=8165422401,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 9921a3e9e3f7596df67493847bbc01f17a3b226e
travis_fold:end:git.checkout[0K
travis_time:end:2df2ef95:start=1572057489789562588,finish=1572057498863466006,duration=9073903418,event=checkout[0Ktravis_time:start:0a1de292[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0a1de292:start=1572057498868242315,finish=1572057498878547768,duration=10305453,event=env[0Ktravis_time:start:171062d3[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:171062d3:start=1572057498883026705,finish=1572057498889345751,duration=6319046,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0aa62b3e[0K$ python system_testing.py -s of-of
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
Digest: sha256:0e7924ce4e1439b836b1bc657d21d9267c7ce1caa718cc2ed2379b53960d51d0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0aa62b3e:start=1572057499236452706,finish=1572057619942851986,duration=120706399280,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:2bf05f85[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/603099793/log.txt)