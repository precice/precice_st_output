## Status: Passing 
Build: [1032](https://travis-ci.org/precice/systemtests/builds/603568985) 

Job: [1032.20](https://travis-ci.org/precice/systemtests/jobs/603569005) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e6ee51b6890c...5e709cade038) 

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
travis_time:end:146168f4:start=1572199371616609785,finish=1572199371622889235,duration=6279450,event=show_system_info[0Ktravis_time:start:256e64b0[0Ktravis_time:end:256e64b0:start=1572199371625947444,finish=1572199371652007733,duration=26060289,event=rm_riak_source[0Ktravis_time:start:0e3fef41[0Ktravis_time:end:0e3fef41:start=1572199371655325843,finish=1572199371662134359,duration=6808516,event=fix_rwky_redis[0Ktravis_time:start:07e76430[0Ktravis_time:end:07e76430:start=1572199371665651745,finish=1572199372070602028,duration=404950283,event=wait_for_network[0Ktravis_time:start:03f7e21c[0Ktravis_time:end:03f7e21c:start=1572199372076352558,finish=1572199373010033415,duration=933680857,event=update_apt_keys[0Ktravis_time:start:0128305a[0Ktravis_time:end:0128305a:start=1572199373015824099,finish=1572199374091413870,duration=1075589771,event=fix_hhvm_source[0Ktravis_time:start:31e2bbda[0Ktravis_time:end:31e2bbda:start=1572199374096963119,finish=1572199374108856295,duration=11893176,event=update_mongo_arch[0Ktravis_time:start:1186aea0[0Ktravis_time:end:1186aea0:start=1572199374113919845,finish=1572199374158706409,duration=44786564,event=fix_sudo_enabled_trusty[0Ktravis_time:start:07d6145e[0Ktravis_time:end:07d6145e:start=1572199374163833946,finish=1572199374167137005,duration=3303059,event=update_glibc[0Ktravis_time:start:0ab20004[0Ktravis_time:end:0ab20004:start=1572199374172748241,finish=1572199374182165045,duration=9416804,event=clean_up_path[0Ktravis_time:start:2ad64622[0Ktravis_time:end:2ad64622:start=1572199374188635259,finish=1572199374197922057,duration=9286798,event=fix_resolv_conf[0Ktravis_time:start:2af044fa[0Ktravis_time:end:2af044fa:start=1572199374201870904,finish=1572199374214156541,duration=12285637,event=fix_etc_hosts[0Ktravis_time:start:1337a9d2[0Ktravis_time:end:1337a9d2:start=1572199374218141927,finish=1572199374228541144,duration=10399217,event=fix_mvn_settings_xml[0Ktravis_time:start:11bd569e[0Ktravis_time:end:11bd569e:start=1572199374233704661,finish=1572199374243899485,duration=10194824,event=no_ipv6_localhost[0Ktravis_time:start:03c0f02a[0Ktravis_time:end:03c0f02a:start=1572199374248867786,finish=1572199374251615921,duration=2748135,event=fix_etc_mavenrc[0Ktravis_time:start:16fff152[0Ktravis_time:end:16fff152:start=1572199374257952665,finish=1572199374261999266,duration=4046601,event=fix_wwdr_certificate[0Ktravis_time:start:03035ab1[0Ktravis_time:end:03035ab1:start=1572199374266673016,finish=1572199374292938230,duration=26265214,event=put_localhost_first[0Ktravis_time:start:1972ba20[0Ktravis_time:end:1972ba20:start=1572199374298735583,finish=1572199374305225720,duration=6490137,event=home_paths[0Ktravis_time:start:02ff9049[0Ktravis_time:end:02ff9049:start=1572199374310679589,finish=1572199374324618197,duration=13938608,event=disable_initramfs[0Ktravis_time:start:0c87afe0[0Ktravis_time:end:0c87afe0:start=1572199374329220657,finish=1572199374656070033,duration=326849376,event=disable_ssh_roaming[0Ktravis_time:start:067afb6e[0Ktravis_time:end:067afb6e:start=1572199374661013876,finish=1572199374664066177,duration=3052301,event=debug_tools[0Ktravis_time:start:354a8282[0Ktravis_time:end:354a8282:start=1572199374668660330,finish=1572199374673484387,duration=4824057,event=uninstall_oclint[0Ktravis_time:start:22f21e90[0Ktravis_time:end:22f21e90:start=1572199374678001724,finish=1572199374682872855,duration=4871131,event=rvm_use[0Ktravis_time:start:2c8edfb0[0Ktravis_time:end:2c8edfb0:start=1572199374692338311,finish=1572199374701406734,duration=9068423,event=rm_etc_boto_cfg[0Ktravis_time:start:23b559a0[0Ktravis_time:end:23b559a0:start=1572199374706516252,finish=1572199374710462036,duration=3945784,event=rm_oraclejdk8_symlink[0Ktravis_time:start:28480035[0Ktravis_time:end:28480035:start=1572199374715474474,finish=1572199374776839214,duration=61364740,event=enable_i386[0Ktravis_time:start:097b2c48[0Ktravis_time:end:097b2c48:start=1572199374781913088,finish=1572199374786547677,duration=4634589,event=update_rubygems[0Ktravis_time:start:1a336310[0Ktravis_time:end:1a336310:start=1572199374790785711,finish=1572199375844348456,duration=1053562745,event=ensure_path_components[0Ktravis_time:start:00d2ae70[0Ktravis_time:end:00d2ae70:start=1572199375849386549,finish=1572199375852391895,duration=3005346,event=redefine_curl[0Ktravis_time:start:0b09fdc0[0Ktravis_time:end:0b09fdc0:start=1572199375857710047,finish=1572199375915801146,duration=58091099,event=nonblock_pipe[0Ktravis_time:start:182f4ac0[0Ktravis_time:end:182f4ac0:start=1572199375919977977,finish=1572199378971154617,duration=3051176640,event=apt_get_update[0Ktravis_time:start:08b3937a[0Ktravis_time:end:08b3937a:start=1572199378975741866,finish=1572199378978698803,duration=2956937,event=deprecate_xcode_64[0Ktravis_time:start:03596dc0[0Ktravis_time:end:03596dc0:start=1572199378983730613,finish=1572199384109997471,duration=5126266858,event=update_heroku[0Ktravis_time:start:029de854[0Ktravis_time:end:029de854:start=1572199384114635910,finish=1572199384117532670,duration=2896760,event=shell_session_update[0Ktravis_time:start:09dfd6a4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3890
travis_fold:end:docker_mtu[0Ktravis_time:end:09dfd6a4:start=1572199384124165102,finish=1572199385328400641,duration=1204235539,event=set_docker_mtu[0Ktravis_time:start:116dcd3c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:116dcd3c:start=1572199385332823611,finish=1572199385405235117,duration=72411506,event=resolvconf[0Ktravis_time:start:0ade8a7a[0Ktravis_time:end:0ade8a7a:start=1572199385410032976,finish=1572199385523066438,duration=113033462,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:26809320[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:26809320:start=1572199385612005537,finish=1572199385818644305,duration=206638768,event=configure[0Ktravis_time:start:00f15126[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:00f15126:start=1572199385824641689,finish=1572199397732429810,duration=11907788121,event=configure[0Ktravis_time:start:00051c84[0Ktravis_fold:start:services[0Ktravis_time:start:08096ddf[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08096ddf:start=1572199397760352095,finish=1572199397775106602,duration=14754507,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08096ddf:start=1572199397760352095,finish=1572199400780253684,duration=3019901589,event=services[0Ktravis_time:start:11364de8[0Ktravis_time:end:11364de8:start=1572199400785260370,finish=1572199400788157412,duration=2897042,event=fix_ps4[0Ktravis_time:start:0fcc3a26[0K
travis_fold:start:git.checkout[0Ktravis_time:start:10c49c16[0K$ git clone --depth=50 --branch=EderK-fix-after_success https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:10c49c16:start=1572199400798270739,finish=1572199407088027604,duration=6289756865,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 5e709cade038f050986e914ea2a9ab1de43e4de9
travis_fold:end:git.checkout[0K
travis_time:end:10c49c16:start=1572199400798270739,finish=1572199407155348865,duration=6357078126,event=checkout[0Ktravis_time:start:04d78b61[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:04d78b61:start=1572199407161162432,finish=1572199407171452419,duration=10289987,event=env[0Ktravis_time:start:07f7fcfd[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:07f7fcfd:start=1572199407176687704,finish=1572199407190126300,duration=13438596,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0ab19d40[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:97bb7e6e100569ab857c2847a688e902aeedb81af15a98a336fc9272ade3829f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/603569005/log.txt)