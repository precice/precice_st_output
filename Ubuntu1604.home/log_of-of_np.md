## Status: Passing 
Build: [1061](https://travis-ci.org/precice/systemtests/builds/609034257) 

Job: [1061.24](https://travis-ci.org/precice/systemtests/jobs/609034281) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:08c86c18:start=1573181196147649995,finish=1573181196153939992,duration=6289997,event=show_system_info[0Ktravis_time:start:13099ce2[0Ktravis_time:end:13099ce2:start=1573181196157130098,finish=1573181196185828920,duration=28698822,event=rm_riak_source[0Ktravis_time:start:0454e332[0Ktravis_time:end:0454e332:start=1573181196189545227,finish=1573181196199463059,duration=9917832,event=fix_rwky_redis[0Ktravis_time:start:1a9ed3b8[0Ktravis_time:end:1a9ed3b8:start=1573181196203272220,finish=1573181196580187541,duration=376915321,event=wait_for_network[0Ktravis_time:start:079265b5[0Ktravis_time:end:079265b5:start=1573181196585612851,finish=1573181198158588463,duration=1572975612,event=update_apt_keys[0Ktravis_time:start:13a419ea[0Ktravis_time:end:13a419ea:start=1573181198163342263,finish=1573181199219877088,duration=1056534825,event=fix_hhvm_source[0Ktravis_time:start:0177dbb4[0Ktravis_time:end:0177dbb4:start=1573181199224288906,finish=1573181199236208467,duration=11919561,event=update_mongo_arch[0Ktravis_time:start:250dceac[0Ktravis_time:end:250dceac:start=1573181199240458354,finish=1573181199284241547,duration=43783193,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0e88654f[0Ktravis_time:end:0e88654f:start=1573181199289431870,finish=1573181199292543055,duration=3111185,event=update_glibc[0Ktravis_time:start:0098bdd4[0Ktravis_time:end:0098bdd4:start=1573181199298681364,finish=1573181199308118056,duration=9436692,event=clean_up_path[0Ktravis_time:start:01d4280e[0Ktravis_time:end:01d4280e:start=1573181199312748599,finish=1573181199322024441,duration=9275842,event=fix_resolv_conf[0Ktravis_time:start:03b37858[0Ktravis_time:end:03b37858:start=1573181199327125660,finish=1573181199337100123,duration=9974463,event=fix_etc_hosts[0Ktravis_time:start:0092ee52[0Ktravis_time:end:0092ee52:start=1573181199343883353,finish=1573181199354108529,duration=10225176,event=fix_mvn_settings_xml[0Ktravis_time:start:3416dd80[0Ktravis_time:end:3416dd80:start=1573181199359245526,finish=1573181199370504724,duration=11259198,event=no_ipv6_localhost[0Ktravis_time:start:0313e528[0Ktravis_time:end:0313e528:start=1573181199375413922,finish=1573181199378285106,duration=2871184,event=fix_etc_mavenrc[0Ktravis_time:start:012e17b4[0Ktravis_time:end:012e17b4:start=1573181199383620890,finish=1573181199388884861,duration=5263971,event=fix_wwdr_certificate[0Ktravis_time:start:06369292[0Ktravis_time:end:06369292:start=1573181199393951912,finish=1573181199421197980,duration=27246068,event=put_localhost_first[0Ktravis_time:start:1bd0fa0f[0Ktravis_time:end:1bd0fa0f:start=1573181199427496832,finish=1573181199432503678,duration=5006846,event=home_paths[0Ktravis_time:start:08997bc2[0Ktravis_time:end:08997bc2:start=1573181199437631891,finish=1573181199451451641,duration=13819750,event=disable_initramfs[0Ktravis_time:start:0f316216[0Ktravis_time:end:0f316216:start=1573181199456231329,finish=1573181199791135562,duration=334904233,event=disable_ssh_roaming[0Ktravis_time:start:068e69bc[0Ktravis_time:end:068e69bc:start=1573181199795787734,finish=1573181199798747835,duration=2960101,event=debug_tools[0Ktravis_time:start:0438fac8[0Ktravis_time:end:0438fac8:start=1573181199803603468,finish=1573181199807294736,duration=3691268,event=uninstall_oclint[0Ktravis_time:start:0018caf4[0Ktravis_time:end:0018caf4:start=1573181199811702576,finish=1573181199816626833,duration=4924257,event=rvm_use[0Ktravis_time:start:2d48663c[0Ktravis_time:end:2d48663c:start=1573181199820911854,finish=1573181199828738796,duration=7826942,event=rm_etc_boto_cfg[0Ktravis_time:start:1f26694c[0Ktravis_time:end:1f26694c:start=1573181199833208785,finish=1573181199837208544,duration=3999759,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2ca1d11b[0Ktravis_time:end:2ca1d11b:start=1573181199841610211,finish=1573181199898758176,duration=57147965,event=enable_i386[0Ktravis_time:start:0ab5e9c0[0Ktravis_time:end:0ab5e9c0:start=1573181199903524379,finish=1573181199908529619,duration=5005240,event=update_rubygems[0Ktravis_time:start:07690ff4[0Ktravis_time:end:07690ff4:start=1573181199913815355,finish=1573181200965751671,duration=1051936316,event=ensure_path_components[0Ktravis_time:start:099f4c68[0Ktravis_time:end:099f4c68:start=1573181200970875141,finish=1573181200973856818,duration=2981677,event=redefine_curl[0Ktravis_time:start:04076100[0Ktravis_time:end:04076100:start=1573181200978427507,finish=1573181201035806340,duration=57378833,event=nonblock_pipe[0Ktravis_time:start:0113c2ce[0Ktravis_time:end:0113c2ce:start=1573181201040735325,finish=1573181204090401411,duration=3049666086,event=apt_get_update[0Ktravis_time:start:09371380[0Ktravis_time:end:09371380:start=1573181204095580805,finish=1573181204098686373,duration=3105568,event=deprecate_xcode_64[0Ktravis_time:start:08058a44[0Ktravis_time:end:08058a44:start=1573181204103609026,finish=1573181208824500730,duration=4720891704,event=update_heroku[0Ktravis_time:start:01608aee[0Ktravis_time:end:01608aee:start=1573181208829136615,finish=1573181208832273704,duration=3137089,event=shell_session_update[0Ktravis_time:start:00a347cc[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3970
travis_fold:end:docker_mtu[0Ktravis_time:end:00a347cc:start=1573181208837987806,finish=1573181210045000306,duration=1207012500,event=set_docker_mtu[0Ktravis_time:start:0e0dc4fc[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0e0dc4fc:start=1573181210050211260,finish=1573181210120672928,duration=70461668,event=resolvconf[0Ktravis_time:start:1948b980[0Ktravis_time:end:1948b980:start=1573181210125515120,finish=1573181210232611666,duration=107096546,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0d253a60[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0d253a60:start=1573181210321238809,finish=1573181210592277610,duration=271038801,event=configure[0Ktravis_time:start:14aeb56c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:14aeb56c:start=1573181210598591668,finish=1573181222426837482,duration=11828245814,event=configure[0Ktravis_time:start:0d13e5c0[0Ktravis_fold:start:services[0Ktravis_time:start:1d050ac2[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1d050ac2:start=1573181222452608022,finish=1573181222467640546,duration=15032524,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1d050ac2:start=1573181222452608022,finish=1573181225473785197,duration=3021177175,event=services[0Ktravis_time:start:0b1bc79e[0Ktravis_time:end:0b1bc79e:start=1573181225478990965,finish=1573181225481849428,duration=2858463,event=fix_ps4[0Ktravis_time:start:2d3a9305[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1790177a[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1790177a:start=1573181225490939376,finish=1573181231732849909,duration=6241910533,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:1790177a:start=1573181225490939376,finish=1573181232404915612,duration=6913976236,event=checkout[0Ktravis_time:start:0a20c996[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0a20c996:start=1573181232409942701,finish=1573181232419580664,duration=9637963,event=env[0Ktravis_time:start:09450165[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:09450165:start=1573181232424210919,finish=1573181232435054117,duration=10843198,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:104dcaa0[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:0df5ddcdd2fbe3eb36701daa030517b98e10ce7531c23f062b5175b29302c75e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:104dcaa0:start=1573181232810172201,finish=1573181354194370361,duration=121384198160,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1de0c6d4[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/609034281/log.txt)