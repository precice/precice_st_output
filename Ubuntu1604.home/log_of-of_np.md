## Status: Passing 
Build: [1047](https://travis-ci.org/precice/systemtests/builds/604758622) 

Job: [1047.24](https://travis-ci.org/precice/systemtests/jobs/604758653) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:13430cb8:start=1572403393629286485,finish=1572403393636088228,duration=6801743,event=show_system_info[0Ktravis_time:start:060ffc7d[0Ktravis_time:end:060ffc7d:start=1572403393639488649,finish=1572403393671099146,duration=31610497,event=rm_riak_source[0Ktravis_time:start:0df282fa[0Ktravis_time:end:0df282fa:start=1572403393674773018,finish=1572403393681194410,duration=6421392,event=fix_rwky_redis[0Ktravis_time:start:01ed7da4[0Ktravis_time:end:01ed7da4:start=1572403393684901490,finish=1572403394069028804,duration=384127314,event=wait_for_network[0Ktravis_time:start:3570ccdc[0Ktravis_time:end:3570ccdc:start=1572403394075867250,finish=1572403395699857782,duration=1623990532,event=update_apt_keys[0Ktravis_time:start:028cb926[0Ktravis_time:end:028cb926:start=1572403395705262102,finish=1572403396809743260,duration=1104481158,event=fix_hhvm_source[0Ktravis_time:start:2627158c[0Ktravis_time:end:2627158c:start=1572403396815328096,finish=1572403396826647972,duration=11319876,event=update_mongo_arch[0Ktravis_time:start:19b07bba[0Ktravis_time:end:19b07bba:start=1572403396831619299,finish=1572403396875070058,duration=43450759,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0e465938[0Ktravis_time:end:0e465938:start=1572403396880094356,finish=1572403396882925653,duration=2831297,event=update_glibc[0Ktravis_time:start:15bbe54c[0Ktravis_time:end:15bbe54c:start=1572403396887516752,finish=1572403396898232187,duration=10715435,event=clean_up_path[0Ktravis_time:start:0c819c71[0Ktravis_time:end:0c819c71:start=1572403396903388362,finish=1572403396913181116,duration=9792754,event=fix_resolv_conf[0Ktravis_time:start:084a0bf7[0Ktravis_time:end:084a0bf7:start=1572403396918390602,finish=1572403396928696677,duration=10306075,event=fix_etc_hosts[0Ktravis_time:start:254c03e9[0Ktravis_time:end:254c03e9:start=1572403396934817451,finish=1572403396947113680,duration=12296229,event=fix_mvn_settings_xml[0Ktravis_time:start:00077f88[0Ktravis_time:end:00077f88:start=1572403396952386314,finish=1572403396965049113,duration=12662799,event=no_ipv6_localhost[0Ktravis_time:start:1f859a66[0Ktravis_time:end:1f859a66:start=1572403396970853592,finish=1572403396973960044,duration=3106452,event=fix_etc_mavenrc[0Ktravis_time:start:06a13e83[0Ktravis_time:end:06a13e83:start=1572403396978879772,finish=1572403396982775467,duration=3895695,event=fix_wwdr_certificate[0Ktravis_time:start:134c76c0[0Ktravis_time:end:134c76c0:start=1572403396988022563,finish=1572403397015384166,duration=27361603,event=put_localhost_first[0Ktravis_time:start:020ea09e[0Ktravis_time:end:020ea09e:start=1572403397021383119,finish=1572403397026299836,duration=4916717,event=home_paths[0Ktravis_time:start:01139440[0Ktravis_time:end:01139440:start=1572403397031133055,finish=1572403397047800972,duration=16667917,event=disable_initramfs[0Ktravis_time:start:28baf75b[0Ktravis_time:end:28baf75b:start=1572403397053251202,finish=1572403397465162371,duration=411911169,event=disable_ssh_roaming[0Ktravis_time:start:1a4f846c[0Ktravis_time:end:1a4f846c:start=1572403397471439378,finish=1572403397475056062,duration=3616684,event=debug_tools[0Ktravis_time:start:02917cc8[0Ktravis_time:end:02917cc8:start=1572403397481268331,finish=1572403397485945342,duration=4677011,event=uninstall_oclint[0Ktravis_time:start:010cb88b[0Ktravis_time:end:010cb88b:start=1572403397491761457,finish=1572403397496260619,duration=4499162,event=rvm_use[0Ktravis_time:start:01a17068[0Ktravis_time:end:01a17068:start=1572403397501955954,finish=1572403397512473562,duration=10517608,event=rm_etc_boto_cfg[0Ktravis_time:start:14173544[0Ktravis_time:end:14173544:start=1572403397520730074,finish=1572403397524350613,duration=3620539,event=rm_oraclejdk8_symlink[0Ktravis_time:start:044674ac[0Ktravis_time:end:044674ac:start=1572403397529988602,finish=1572403397592472066,duration=62483464,event=enable_i386[0Ktravis_time:start:09e4d9c8[0Ktravis_time:end:09e4d9c8:start=1572403397597418120,finish=1572403397603658593,duration=6240473,event=update_rubygems[0Ktravis_time:start:0c01f1fe[0Ktravis_time:end:0c01f1fe:start=1572403397609037018,finish=1572403398687510374,duration=1078473356,event=ensure_path_components[0Ktravis_time:start:027520c8[0Ktravis_time:end:027520c8:start=1572403398692650285,finish=1572403398695908851,duration=3258566,event=redefine_curl[0Ktravis_time:start:0acaefbd[0Ktravis_time:end:0acaefbd:start=1572403398701137122,finish=1572403398760888914,duration=59751792,event=nonblock_pipe[0Ktravis_time:start:054fdb98[0Ktravis_time:end:054fdb98:start=1572403398765754621,finish=1572403401839787413,duration=3074032792,event=apt_get_update[0Ktravis_time:start:109cdc88[0Ktravis_time:end:109cdc88:start=1572403401844893011,finish=1572403401848425944,duration=3532933,event=deprecate_xcode_64[0Ktravis_time:start:08439114[0Ktravis_time:end:08439114:start=1572403401853262521,finish=1572403406734865593,duration=4881603072,event=update_heroku[0Ktravis_time:start:003dfe38[0Ktravis_time:end:003dfe38:start=1572403406739798658,finish=1572403406743127936,duration=3329278,event=shell_session_update[0Ktravis_time:start:00ffcc93[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3955
travis_fold:end:docker_mtu[0Ktravis_time:end:00ffcc93:start=1572403406747688739,finish=1572403407958766929,duration=1211078190,event=set_docker_mtu[0Ktravis_time:start:030fe3da[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:030fe3da:start=1572403407964058003,finish=1572403408031635674,duration=67577671,event=resolvconf[0Ktravis_time:start:043d2c1b[0Ktravis_time:end:043d2c1b:start=1572403408036919265,finish=1572403408144667300,duration=107748035,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:26910a0e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:26910a0e:start=1572403408228296726,finish=1572403408674360015,duration=446063289,event=configure[0Ktravis_time:start:041f37c6[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:041f37c6:start=1572403408679596495,finish=1572403418866555017,duration=10186958522,event=configure[0Ktravis_time:start:1b4532c4[0Ktravis_fold:start:services[0Ktravis_time:start:00697266[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:00697266:start=1572403418892783140,finish=1572403418907117020,duration=14333880,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:00697266:start=1572403418892783140,finish=1572403421912217919,duration=3019434779,event=services[0Ktravis_time:start:167c75ac[0Ktravis_time:end:167c75ac:start=1572403421916952533,finish=1572403421919770618,duration=2818085,event=fix_ps4[0Ktravis_time:start:1ce01840[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08281600[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08281600:start=1572403421927928414,finish=1572403428206935446,duration=6279007032,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:08281600:start=1572403421927928414,finish=1572403428360496169,duration=6432567755,event=checkout[0Ktravis_time:start:02c95afe[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:02c95afe:start=1572403428365186610,finish=1572403428377100724,duration=11914114,event=env[0Ktravis_time:start:1d9619ec[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1d9619ec:start=1572403428381584563,finish=1572403428388266417,duration=6681854,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2eb159c6[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
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

Creating network "testcomposeofofnp_default" with the default driver
Creating network "testcomposeofofnp_[secure]comm" with the default driver
Creating volume "testcomposeofofnp_output" with default driver
Creating volume "testcomposeofofnp_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:a1923cb1231d1cc4e515c0bc821b7531290bcdde9aa979b85e6c7f36d0b76068
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2eb159c6:start=1572403428748091336,finish=1572403555766203111,duration=127018111775,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0452224b[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/604758653/log.txt)