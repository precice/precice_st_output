 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599812196) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63f291b1fec7...efe9b440d9b6) 
## Last 100 lines of the job log at the moment of push...
```
 [34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:074b0f9e:start=1571435110255846898,finish=1571435110261429851,duration=5582953,event=show_system_info[0Ktravis_time:start:0a6c3b7b[0Ktravis_time:end:0a6c3b7b:start=1571435110264495425,finish=1571435110287084812,duration=22589387,event=rm_riak_source[0Ktravis_time:start:05f657d9[0Ktravis_time:end:05f657d9:start=1571435110290566370,finish=1571435110299211533,duration=8645163,event=fix_rwky_redis[0Ktravis_time:start:0400934a[0Ktravis_time:end:0400934a:start=1571435110304747785,finish=1571435110740407412,duration=435659627,event=wait_for_network[0Ktravis_time:start:00623718[0Ktravis_time:end:00623718:start=1571435110745009007,finish=1571435111770164045,duration=1025155038,event=update_apt_keys[0Ktravis_time:start:0a182718[0Ktravis_time:end:0a182718:start=1571435111775975656,finish=1571435112800615854,duration=1024640198,event=fix_hhvm_source[0Ktravis_time:start:051a667a[0Ktravis_time:end:051a667a:start=1571435112806028717,finish=1571435112816178272,duration=10149555,event=update_mongo_arch[0Ktravis_time:start:0314b03b[0Ktravis_time:end:0314b03b:start=1571435112820266310,finish=1571435112861979908,duration=41713598,event=fix_sudo_enabled_trusty[0Ktravis_time:start:28a6511a[0Ktravis_time:end:28a6511a:start=1571435112866788075,finish=1571435112869692813,duration=2904738,event=update_glibc[0Ktravis_time:start:01d38f76[0Ktravis_time:end:01d38f76:start=1571435112875076870,finish=1571435112884012590,duration=8935720,event=clean_up_path[0Ktravis_time:start:032fb464[0Ktravis_time:end:032fb464:start=1571435112888157180,finish=1571435112897384732,duration=9227552,event=fix_resolv_conf[0Ktravis_time:start:12b42e67[0Ktravis_time:end:12b42e67:start=1571435112903899908,finish=1571435112913249547,duration=9349639,event=fix_etc_hosts[0Ktravis_time:start:0a10e26c[0Ktravis_time:end:0a10e26c:start=1571435112917901582,finish=1571435112926969003,duration=9067421,event=fix_mvn_settings_xml[0Ktravis_time:start:0f524310[0Ktravis_time:end:0f524310:start=1571435112931670545,finish=1571435112943925528,duration=12254983,event=no_ipv6_localhost[0Ktravis_time:start:07949f51[0Ktravis_time:end:07949f51:start=1571435112949239172,finish=1571435112952176725,duration=2937553,event=fix_etc_mavenrc[0Ktravis_time:start:1ce99ca8[0Ktravis_time:end:1ce99ca8:start=1571435112958947320,finish=1571435112963462347,duration=4515027,event=fix_wwdr_certificate[0Ktravis_time:start:0820d688[0Ktravis_time:end:0820d688:start=1571435112968804160,finish=1571435112997100622,duration=28296462,event=put_localhost_first[0Ktravis_time:start:01593160[0Ktravis_time:end:01593160:start=1571435113002332790,finish=1571435113006924571,duration=4591781,event=home_paths[0Ktravis_time:start:28b8ffe2[0Ktravis_time:end:28b8ffe2:start=1571435113012229411,finish=1571435113027129646,duration=14900235,event=disable_initramfs[0Ktravis_time:start:13d2c347[0Ktravis_time:end:13d2c347:start=1571435113033879395,finish=1571435113371827203,duration=337947808,event=disable_ssh_roaming[0Ktravis_time:start:09738ab8[0Ktravis_time:end:09738ab8:start=1571435113376373393,finish=1571435113379096284,duration=2722891,event=debug_tools[0Ktravis_time:start:0aca38ca[0Ktravis_time:end:0aca38ca:start=1571435113383234708,finish=1571435113387077775,duration=3843067,event=uninstall_oclint[0Ktravis_time:start:2b32bdab[0Ktravis_time:end:2b32bdab:start=1571435113391143755,finish=1571435113394401806,duration=3258051,event=rvm_use[0Ktravis_time:start:13a224b8[0Ktravis_time:end:13a224b8:start=1571435113398555513,finish=1571435113407315557,duration=8760044,event=rm_etc_boto_cfg[0Ktravis_time:start:13bae350[0Ktravis_time:end:13bae350:start=1571435113411692548,finish=1571435113414749620,duration=3057072,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0691df4b[0Ktravis_time:end:0691df4b:start=1571435113418909063,finish=1571435113472492039,duration=53582976,event=enable_i386[0Ktravis_time:start:00520f89[0Ktravis_time:end:00520f89:start=1571435113477286851,finish=1571435113481598050,duration=4311199,event=update_rubygems[0Ktravis_time:start:254bb670[0Ktravis_time:end:254bb670:start=1571435113486283871,finish=1571435114480176957,duration=993893086,event=ensure_path_components[0Ktravis_time:start:0703b90f[0Ktravis_time:end:0703b90f:start=1571435114484770401,finish=1571435114487847567,duration=3077166,event=redefine_curl[0Ktravis_time:start:02ff7f6b[0Ktravis_time:end:02ff7f6b:start=1571435114492714446,finish=1571435114545819189,duration=53104743,event=nonblock_pipe[0Ktravis_time:start:0206d349[0Ktravis_time:end:0206d349:start=1571435114550007698,finish=1571435114590408405,duration=40400707,event=apt_get_update[0Ktravis_time:start:11d607c0[0Ktravis_time:end:11d607c0:start=1571435114594502985,finish=1571435114597254786,duration=2751801,event=deprecate_xcode_64[0Ktravis_time:start:01794e13[0Ktravis_time:end:01794e13:start=1571435114601698127,finish=1571435119192589611,duration=4590891484,event=update_heroku[0Ktravis_time:start:1a82a85d[0Ktravis_time:end:1a82a85d:start=1571435119198008301,finish=1571435119200932713,duration=2924412,event=shell_session_update[0Ktravis_time:start:06d98e9a[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3960
travis_fold:end:docker_mtu[0Ktravis_time:end:06d98e9a:start=1571435119205745073,finish=1571435120406989986,duration=1201244913,event=set_docker_mtu[0Ktravis_time:start:0f07899c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0f07899c:start=1571435120411725444,finish=1571435120475765410,duration=64039966,event=resolvconf[0Ktravis_time:start:05600100[0Ktravis_time:end:05600100:start=1571435120480632153,finish=1571435120576091767,duration=95459614,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0b25afa7[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0b25afa7:start=1571435120657191578,finish=1571435121520294287,duration=863102709,event=configure[0Ktravis_time:start:02b38750[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02b38750:start=1571435121525747607,finish=1571435130556068391,duration=9030320784,event=configure[0Ktravis_time:start:01274418[0Ktravis_fold:start:services[0Ktravis_time:start:00953bbc[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:00953bbc:start=1571435130581167942,finish=1571435130595406709,duration=14238767,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:00953bbc:start=1571435130581167942,finish=1571435133602168601,duration=3021000659,event=services[0Ktravis_time:start:18eeb28c[0Ktravis_time:end:18eeb28c:start=1571435133607325412,finish=1571435133610137433,duration=2812021,event=fix_ps4[0Ktravis_time:start:136a0209[0K
travis_fold:start:git.checkout[0Ktravis_time:start:071247e6[0K$ git clone --depth=50 --branch=IshaanDesai-testing_fe-fe_complexDomain https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:071247e6:start=1571435133619906152,finish=1571435140190415843,duration=6570509691,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf efe9b440d9b6bdfdff0bed8da10df93e865a3d2e
travis_fold:end:git.checkout[0K
travis_time:end:071247e6:start=1571435133619906152,finish=1571435140340064093,duration=6720157941,event=checkout[0Ktravis_time:start:000b9cd6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:000b9cd6:start=1571435140344482180,finish=1571435140355719744,duration=11237564,event=env[0Ktravis_time:start:0fc1f873[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0fc1f873:start=1571435140360319389,finish=1571435140366059564,duration=5740175,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:05f88f0c[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8e9ef052033a14d0f1539684ea21cf608caecbb20bc75664dcdb75cf1c3a9b4b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599812219/log.txt)