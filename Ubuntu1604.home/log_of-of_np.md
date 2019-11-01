## Status: Passing 
Build: [1052](https://travis-ci.org/precice/systemtests/builds/605812235) 

Job: [1052.24](https://travis-ci.org/precice/systemtests/jobs/605812259) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:00252598:start=1572576183187335873,finish=1572576183194133223,duration=6797350,event=show_system_info[0Ktravis_time:start:099adf39[0Ktravis_time:end:099adf39:start=1572576183197768772,finish=1572576183224008553,duration=26239781,event=rm_riak_source[0Ktravis_time:start:00d20d62[0Ktravis_time:end:00d20d62:start=1572576183227927065,finish=1572576183236205840,duration=8278775,event=fix_rwky_redis[0Ktravis_time:start:0786de99[0Ktravis_time:end:0786de99:start=1572576183240956752,finish=1572576183637303059,duration=396346307,event=wait_for_network[0Ktravis_time:start:21381bc4[0Ktravis_time:end:21381bc4:start=1572576183642926048,finish=1572576184621692411,duration=978766363,event=update_apt_keys[0Ktravis_time:start:0372d5d4[0Ktravis_time:end:0372d5d4:start=1572576184626905702,finish=1572576185716490230,duration=1089584528,event=fix_hhvm_source[0Ktravis_time:start:24f4e648[0Ktravis_time:end:24f4e648:start=1572576185722449596,finish=1572576185732745802,duration=10296206,event=update_mongo_arch[0Ktravis_time:start:0d2528f8[0Ktravis_time:end:0d2528f8:start=1572576185737028253,finish=1572576185778920947,duration=41892694,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1002bbc8[0Ktravis_time:end:1002bbc8:start=1572576185782993230,finish=1572576185786804183,duration=3810953,event=update_glibc[0Ktravis_time:start:1e3d1ab7[0Ktravis_time:end:1e3d1ab7:start=1572576185790559778,finish=1572576185801771784,duration=11212006,event=clean_up_path[0Ktravis_time:start:036d33e8[0Ktravis_time:end:036d33e8:start=1572576185809092794,finish=1572576185817629523,duration=8536729,event=fix_resolv_conf[0Ktravis_time:start:1098c11e[0Ktravis_time:end:1098c11e:start=1572576185823159985,finish=1572576185833816876,duration=10656891,event=fix_etc_hosts[0Ktravis_time:start:0936d809[0Ktravis_time:end:0936d809:start=1572576185838644115,finish=1572576185848060311,duration=9416196,event=fix_mvn_settings_xml[0Ktravis_time:start:28168014[0Ktravis_time:end:28168014:start=1572576185853188050,finish=1572576185863884208,duration=10696158,event=no_ipv6_localhost[0Ktravis_time:start:086e078e[0Ktravis_time:end:086e078e:start=1572576185867771057,finish=1572576185870806052,duration=3034995,event=fix_etc_mavenrc[0Ktravis_time:start:0a41b0f4[0Ktravis_time:end:0a41b0f4:start=1572576185874455020,finish=1572576185880231476,duration=5776456,event=fix_wwdr_certificate[0Ktravis_time:start:0bc06250[0Ktravis_time:end:0bc06250:start=1572576185884954439,finish=1572576185910692954,duration=25738515,event=put_localhost_first[0Ktravis_time:start:09072c8d[0Ktravis_time:end:09072c8d:start=1572576185915869996,finish=1572576185920287244,duration=4417248,event=home_paths[0Ktravis_time:start:0964d900[0Ktravis_time:end:0964d900:start=1572576185924692871,finish=1572576185937216730,duration=12523859,event=disable_initramfs[0Ktravis_time:start:080f70e4[0Ktravis_time:end:080f70e4:start=1572576185941770582,finish=1572576186331805901,duration=390035319,event=disable_ssh_roaming[0Ktravis_time:start:212af77c[0Ktravis_time:end:212af77c:start=1572576186337691607,finish=1572576186341183424,duration=3491817,event=debug_tools[0Ktravis_time:start:032dc270[0Ktravis_time:end:032dc270:start=1572576186346011567,finish=1572576186350148490,duration=4136923,event=uninstall_oclint[0Ktravis_time:start:1a26499c[0Ktravis_time:end:1a26499c:start=1572576186354974584,finish=1572576186362307409,duration=7332825,event=rvm_use[0Ktravis_time:start:0c13f148[0Ktravis_time:end:0c13f148:start=1572576186367294141,finish=1572576186376375765,duration=9081624,event=rm_etc_boto_cfg[0Ktravis_time:start:35f98c58[0Ktravis_time:end:35f98c58:start=1572576186382624652,finish=1572576186385553044,duration=2928392,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0453f348[0Ktravis_time:end:0453f348:start=1572576186390415339,finish=1572576186457173684,duration=66758345,event=enable_i386[0Ktravis_time:start:096b324d[0Ktravis_time:end:096b324d:start=1572576186461886782,finish=1572576186467191020,duration=5304238,event=update_rubygems[0Ktravis_time:start:03fa6587[0Ktravis_time:end:03fa6587:start=1572576186473156088,finish=1572576187521357960,duration=1048201872,event=ensure_path_components[0Ktravis_time:start:1514a215[0Ktravis_time:end:1514a215:start=1572576187526245236,finish=1572576187529969454,duration=3724218,event=redefine_curl[0Ktravis_time:start:0bb35a00[0Ktravis_time:end:0bb35a00:start=1572576187534795073,finish=1572576187592095824,duration=57300751,event=nonblock_pipe[0Ktravis_time:start:272fd2ca[0Ktravis_time:end:272fd2ca:start=1572576187597537921,finish=1572576190670371764,duration=3072833843,event=apt_get_update[0Ktravis_time:start:060f64a4[0Ktravis_time:end:060f64a4:start=1572576190675686835,finish=1572576190678939655,duration=3252820,event=deprecate_xcode_64[0Ktravis_time:start:01467ec1[0Ktravis_time:end:01467ec1:start=1572576190683687889,finish=1572576195495183395,duration=4811495506,event=update_heroku[0Ktravis_time:start:30332034[0Ktravis_time:end:30332034:start=1572576195501312145,finish=1572576195504604514,duration=3292369,event=shell_session_update[0Ktravis_time:start:009887dc[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3856
travis_fold:end:docker_mtu[0Ktravis_time:end:009887dc:start=1572576195509474439,finish=1572576196707737261,duration=1198262822,event=set_docker_mtu[0Ktravis_time:start:0d82e2bd[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0d82e2bd:start=1572576196712400891,finish=1572576196782191674,duration=69790783,event=resolvconf[0Ktravis_time:start:0373bf74[0Ktravis_time:end:0373bf74:start=1572576196787137180,finish=1572576196908717030,duration=121579850,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0b2bb6e0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0b2bb6e0:start=1572576196995842957,finish=1572576197352868354,duration=357025397,event=configure[0Ktravis_time:start:28b85af0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:28b85af0:start=1572576197359272122,finish=1572576207433635058,duration=10074362936,event=configure[0Ktravis_time:start:35c9fa33[0Ktravis_fold:start:services[0Ktravis_time:start:07519ffc[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:07519ffc:start=1572576207460759814,finish=1572576207476857904,duration=16098090,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:07519ffc:start=1572576207460759814,finish=1572576210483717192,duration=3022957378,event=services[0Ktravis_time:start:2f5718f8[0Ktravis_time:end:2f5718f8:start=1572576210489090718,finish=1572576210492143304,duration=3052586,event=fix_ps4[0Ktravis_time:start:28db0db8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0453f7df[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0453f7df:start=1572576210500711104,finish=1572576216706534810,duration=6205823706,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0453f7df:start=1572576210500711104,finish=1572576217327619699,duration=6826908595,event=checkout[0Ktravis_time:start:22c09593[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:22c09593:start=1572576217334155083,finish=1572576217350572846,duration=16417763,event=env[0Ktravis_time:start:04982944[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:04982944:start=1572576217355536312,finish=1572576217361778276,duration=6241964,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:03486990[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:5f4cf9654d3e8ad6e24ca09f06617acede4a15c96234e007a7edfec2b73ce6cd
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
travis_time:end:03486990:start=1572576217711749790,finish=1572576338527782140,duration=120816032350,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00027280[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/605812259/log.txt)