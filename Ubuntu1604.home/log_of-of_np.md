## Status: Passing 
Build: [993](https://travis-ci.org/precice/systemtests/builds/600693901) 

Job: [993.20](https://travis-ci.org/precice/systemtests/jobs/600693922) 

Triggered by: [push](https://github.com/precice/systemtests/compare/a84a139c2665...500cfbb53a97) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:04cac6f0:start=1571660934321478558,finish=1571660934327544520,duration=6065962,event=show_system_info[0Ktravis_time:start:13665bd0[0Ktravis_time:end:13665bd0:start=1571660934330518636,finish=1571660934354925668,duration=24407032,event=rm_riak_source[0Ktravis_time:start:08bf5860[0Ktravis_time:end:08bf5860:start=1571660934358783172,finish=1571660934365077947,duration=6294775,event=fix_rwky_redis[0Ktravis_time:start:072d1b38[0Ktravis_time:end:072d1b38:start=1571660934368752403,finish=1571660934742750515,duration=373998112,event=wait_for_network[0Ktravis_time:start:1d3f6430[0Ktravis_time:end:1d3f6430:start=1571660934748196953,finish=1571660936334369841,duration=1586172888,event=update_apt_keys[0Ktravis_time:start:164a6e0a[0Ktravis_time:end:164a6e0a:start=1571660936339382615,finish=1571660937450424853,duration=1111042238,event=fix_hhvm_source[0Ktravis_time:start:09e33e2a[0Ktravis_time:end:09e33e2a:start=1571660937455363772,finish=1571660937465844192,duration=10480420,event=update_mongo_arch[0Ktravis_time:start:0e13c07c[0Ktravis_time:end:0e13c07c:start=1571660937470422847,finish=1571660937512148738,duration=41725891,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0dfcbdec[0Ktravis_time:end:0dfcbdec:start=1571660937518700539,finish=1571660937521928665,duration=3228126,event=update_glibc[0Ktravis_time:start:0013e812[0Ktravis_time:end:0013e812:start=1571660937528620612,finish=1571660937537261309,duration=8640697,event=clean_up_path[0Ktravis_time:start:1a1a5c98[0Ktravis_time:end:1a1a5c98:start=1571660937541451576,finish=1571660937549902536,duration=8450960,event=fix_resolv_conf[0Ktravis_time:start:02b610f0[0Ktravis_time:end:02b610f0:start=1571660937554311167,finish=1571660937563516081,duration=9204914,event=fix_etc_hosts[0Ktravis_time:start:08a963ea[0Ktravis_time:end:08a963ea:start=1571660937569905743,finish=1571660937578750102,duration=8844359,event=fix_mvn_settings_xml[0Ktravis_time:start:136f2594[0Ktravis_time:end:136f2594:start=1571660937583559521,finish=1571660937595136159,duration=11576638,event=no_ipv6_localhost[0Ktravis_time:start:03978eac[0Ktravis_time:end:03978eac:start=1571660937600201059,finish=1571660937603226532,duration=3025473,event=fix_etc_mavenrc[0Ktravis_time:start:171e4cbb[0Ktravis_time:end:171e4cbb:start=1571660937608299280,finish=1571660937611951743,duration=3652463,event=fix_wwdr_certificate[0Ktravis_time:start:1879d340[0Ktravis_time:end:1879d340:start=1571660937618939621,finish=1571660937644718764,duration=25779143,event=put_localhost_first[0Ktravis_time:start:04be4cfa[0Ktravis_time:end:04be4cfa:start=1571660937649624506,finish=1571660937653798806,duration=4174300,event=home_paths[0Ktravis_time:start:032cef7a[0Ktravis_time:end:032cef7a:start=1571660937660390665,finish=1571660937672985174,duration=12594509,event=disable_initramfs[0Ktravis_time:start:0af14f7e[0Ktravis_time:end:0af14f7e:start=1571660937677739847,finish=1571660938007119666,duration=329379819,event=disable_ssh_roaming[0Ktravis_time:start:288e46be[0Ktravis_time:end:288e46be:start=1571660938011869149,finish=1571660938014578103,duration=2708954,event=debug_tools[0Ktravis_time:start:0a0544f0[0Ktravis_time:end:0a0544f0:start=1571660938018867672,finish=1571660938024374627,duration=5506955,event=uninstall_oclint[0Ktravis_time:start:003148d8[0Ktravis_time:end:003148d8:start=1571660938029335107,finish=1571660938034185920,duration=4850813,event=rvm_use[0Ktravis_time:start:0a7c04d8[0Ktravis_time:end:0a7c04d8:start=1571660938038917567,finish=1571660938047831086,duration=8913519,event=rm_etc_boto_cfg[0Ktravis_time:start:1ef7439a[0Ktravis_time:end:1ef7439a:start=1571660938052569275,finish=1571660938055508665,duration=2939390,event=rm_oraclejdk8_symlink[0Ktravis_time:start:04bdab28[0Ktravis_time:end:04bdab28:start=1571660938061061863,finish=1571660938118202770,duration=57140907,event=enable_i386[0Ktravis_time:start:012ff646[0Ktravis_time:end:012ff646:start=1571660938123053931,finish=1571660938127425385,duration=4371454,event=update_rubygems[0Ktravis_time:start:23d861b4[0Ktravis_time:end:23d861b4:start=1571660938132082728,finish=1571660939150497002,duration=1018414274,event=ensure_path_components[0Ktravis_time:start:1d64e0a1[0Ktravis_time:end:1d64e0a1:start=1571660939155495606,finish=1571660939158218297,duration=2722691,event=redefine_curl[0Ktravis_time:start:0d7513d0[0Ktravis_time:end:0d7513d0:start=1571660939162600758,finish=1571660939215939592,duration=53338834,event=nonblock_pipe[0Ktravis_time:start:003fcd5d[0Ktravis_time:end:003fcd5d:start=1571660939220922270,finish=1571660942273569112,duration=3052646842,event=apt_get_update[0Ktravis_time:start:1a9e0790[0Ktravis_time:end:1a9e0790:start=1571660942279080440,finish=1571660942283553949,duration=4473509,event=deprecate_xcode_64[0Ktravis_time:start:003f3ace[0Ktravis_time:end:003f3ace:start=1571660942289547026,finish=1571660947139265865,duration=4849718839,event=update_heroku[0Ktravis_time:start:2eb1883a[0Ktravis_time:end:2eb1883a:start=1571660947145389383,finish=1571660947149012109,duration=3622726,event=shell_session_update[0Ktravis_time:start:03dac822[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3886
travis_fold:end:docker_mtu[0Ktravis_time:end:03dac822:start=1571660947154720330,finish=1571660948355107952,duration=1200387622,event=set_docker_mtu[0Ktravis_time:start:116e0998[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:116e0998:start=1571660948360546119,finish=1571660948441193426,duration=80647307,event=resolvconf[0Ktravis_time:start:179dedbd[0Ktravis_time:end:179dedbd:start=1571660948446966633,finish=1571660948564508701,duration=117542068,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:100d902e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:100d902e:start=1571660948666277912,finish=1571660948998574133,duration=332296221,event=configure[0Ktravis_time:start:1ca03e78[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1ca03e78:start=1571660949004838373,finish=1571660959679679186,duration=10674840813,event=configure[0Ktravis_time:start:26c7957c[0Ktravis_fold:start:services[0Ktravis_time:start:0832ac99[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0832ac99:start=1571660959706276541,finish=1571660959722627651,duration=16351110,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0832ac99:start=1571660959706276541,finish=1571660962728228886,duration=3021952345,event=services[0Ktravis_time:start:0dd68d8e[0Ktravis_time:end:0dd68d8e:start=1571660962733863281,finish=1571660962736830620,duration=2967339,event=fix_ps4[0Ktravis_time:start:0aa337a8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:049dc3b5[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:049dc3b5:start=1571660962746284216,finish=1571660969057343089,duration=6311058873,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 500cfbb53a97da6082e1935375882c5b85bda017
travis_fold:end:git.checkout[0K
travis_time:end:049dc3b5:start=1571660962746284216,finish=1571660969105441997,duration=6359157781,event=checkout[0Ktravis_time:start:05d38da8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:05d38da8:start=1571660969110398234,finish=1571660969121503613,duration=11105379,event=env[0Ktravis_time:start:253fc1c9[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:253fc1c9:start=1571660969130272198,finish=1571660969136875992,duration=6603794,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:32bb7512[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:04602e91508ea2c3b26d367af5b44dc79b28546a9dc09a0543218d00fc13e338
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:32bb7512:start=1571660969508260968,finish=1571661091776972459,duration=122268711491,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00ba11a0[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/600693922/log.txt)