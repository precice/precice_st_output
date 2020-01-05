## Status: Failure 
Build: [1396](https://travis-ci.org/precice/systemtests/builds/632899723) 

Job: [1396.19](https://travis-ci.org/precice/systemtests/jobs/632899742) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
  hhvm
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:02c95828:start=1578223750719680837,finish=1578223750724698336,duration=5017499,event=show_system_info[0Ktravis_time:start:0c9c8430[0Ktravis_time:end:0c9c8430:start=1578223750727266997,finish=1578223750746486816,duration=19219819,event=rm_riak_source[0Ktravis_time:start:184e4018[0Ktravis_time:end:184e4018:start=1578223750752600217,finish=1578223750757655881,duration=5055664,event=fix_rwky_redis[0Ktravis_time:start:216ba400[0Ktravis_time:end:216ba400:start=1578223750762790960,finish=1578223751088996394,duration=326205434,event=wait_for_network[0Ktravis_time:start:274afa8f[0Ktravis_time:end:274afa8f:start=1578223751092377450,finish=1578223752097700752,duration=1005323302,event=update_apt_keys[0Ktravis_time:start:09775268[0Ktravis_time:end:09775268:start=1578223752101196755,finish=1578223752943547276,duration=842350521,event=fix_hhvm_source[0Ktravis_time:start:346f34e8[0Ktravis_time:end:346f34e8:start=1578223752948353423,finish=1578223752956656527,duration=8303104,event=update_mongo_arch[0Ktravis_time:start:02ff32dd[0Ktravis_time:end:02ff32dd:start=1578223752961344392,finish=1578223752996426631,duration=35082239,event=fix_sudo_enabled_trusty[0Ktravis_time:start:13288680[0Ktravis_time:end:13288680:start=1578223752999970771,finish=1578223753002130277,duration=2159506,event=update_glibc[0Ktravis_time:start:04441450[0Ktravis_time:end:04441450:start=1578223753005500483,finish=1578223753013334550,duration=7834067,event=clean_up_path[0Ktravis_time:start:013c98a8[0Ktravis_time:end:013c98a8:start=1578223753017135233,finish=1578223753023928518,duration=6793285,event=fix_resolv_conf[0Ktravis_time:start:1a3da73e[0Ktravis_time:end:1a3da73e:start=1578223753028035596,finish=1578223753036685922,duration=8650326,event=fix_etc_hosts[0Ktravis_time:start:0255bc07[0Ktravis_time:end:0255bc07:start=1578223753041141783,finish=1578223753048159813,duration=7018030,event=fix_mvn_settings_xml[0Ktravis_time:start:072516ae[0Ktravis_time:end:072516ae:start=1578223753051860807,finish=1578223753060366641,duration=8505834,event=no_ipv6_localhost[0Ktravis_time:start:04f40e64[0Ktravis_time:end:04f40e64:start=1578223753065139556,finish=1578223753067610329,duration=2470773,event=fix_etc_mavenrc[0Ktravis_time:start:0147bfee[0Ktravis_time:end:0147bfee:start=1578223753071205844,finish=1578223753076704776,duration=5498932,event=fix_wwdr_certificate[0Ktravis_time:start:12a41c00[0Ktravis_time:end:12a41c00:start=1578223753081455048,finish=1578223753100829890,duration=19374842,event=put_localhost_first[0Ktravis_time:start:08ce2c84[0Ktravis_time:end:08ce2c84:start=1578223753104159178,finish=1578223753107571788,duration=3412610,event=home_paths[0Ktravis_time:start:18a1e292[0Ktravis_time:end:18a1e292:start=1578223753110840443,finish=1578223753123571384,duration=12730941,event=disable_initramfs[0Ktravis_time:start:0113d138[0Ktravis_time:end:0113d138:start=1578223753127341260,finish=1578223753407363256,duration=280021996,event=disable_ssh_roaming[0Ktravis_time:start:044e2a41[0Ktravis_time:end:044e2a41:start=1578223753411463426,finish=1578223753413954799,duration=2491373,event=debug_tools[0Ktravis_time:start:06424f08[0Ktravis_time:end:06424f08:start=1578223753419131034,finish=1578223753422074059,duration=2943025,event=uninstall_oclint[0Ktravis_time:start:208905b0[0Ktravis_time:end:208905b0:start=1578223753425875265,finish=1578223753428714941,duration=2839676,event=rvm_use[0Ktravis_time:start:08246569[0Ktravis_time:end:08246569:start=1578223753432091869,finish=1578223753438612649,duration=6520780,event=rm_etc_boto_cfg[0Ktravis_time:start:08ed35a0[0Ktravis_time:end:08ed35a0:start=1578223753442724662,finish=1578223753444792965,duration=2068303,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2268ff85[0Ktravis_time:end:2268ff85:start=1578223753448246340,finish=1578223753490429106,duration=42182766,event=enable_i386[0Ktravis_time:start:2bb9cd76[0Ktravis_time:end:2bb9cd76:start=1578223753494218564,finish=1578223753498118093,duration=3899529,event=update_rubygems[0Ktravis_time:start:1756be46[0Ktravis_time:end:1756be46:start=1578223753501887411,finish=1578223754313542194,duration=811654783,event=ensure_path_components[0Ktravis_time:start:029e64fc[0Ktravis_time:end:029e64fc:start=1578223754317807570,finish=1578223754320759812,duration=2952242,event=redefine_curl[0Ktravis_time:start:0f0ee3d8[0Ktravis_time:end:0f0ee3d8:start=1578223754324372500,finish=1578223754370052350,duration=45679850,event=nonblock_pipe[0Ktravis_time:start:06912a2f[0Ktravis_time:end:06912a2f:start=1578223754374029982,finish=1578223760402099418,duration=6028069436,event=apt_get_update[0Ktravis_time:start:03bfe2be[0Ktravis_time:end:03bfe2be:start=1578223760406203721,finish=1578223760408971048,duration=2767327,event=deprecate_xcode_64[0Ktravis_time:start:184c7f8e[0Ktravis_time:end:184c7f8e:start=1578223760412405161,finish=1578223763856670238,duration=3444265077,event=update_heroku[0Ktravis_time:start:01a112c8[0Ktravis_time:end:01a112c8:start=1578223763860835607,finish=1578223763863272847,duration=2437240,event=shell_session_update[0Ktravis_time:start:07a2f03e[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3892
travis_fold:end:docker_mtu[0Ktravis_time:end:07a2f03e:start=1578223763867268542,finish=1578223765043446815,duration=1176178273,event=set_docker_mtu[0Ktravis_time:start:0414d7a5[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0414d7a5:start=1578223765047190389,finish=1578223765097973836,duration=50783447,event=resolvconf[0Ktravis_time:start:04cc9b0c[0Ktravis_time:end:04cc9b0c:start=1578223765101102206,finish=1578223765175619887,duration=74517681,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0523e856[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0523e856:start=1578223765241666132,finish=1578223766104156727,duration=862490595,event=configure[0Ktravis_time:start:0e863740[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0e863740:start=1578223766107655142,finish=1578223773851007473,duration=7743352331,event=configure[0Ktravis_time:start:261e5e2c[0Ktravis_fold:start:services[0Ktravis_time:start:03b240a0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:03b240a0:start=1578223773872002568,finish=1578223773883790451,duration=11787883,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03b240a0:start=1578223773872002568,finish=1578223776888938434,duration=3016935866,event=services[0Ktravis_time:start:0e0519a5[0Ktravis_time:end:0e0519a5:start=1578223776892373819,finish=1578223776894659147,duration=2285328,event=fix_ps4[0Ktravis_time:start:145ba528[0K
travis_fold:start:git.checkout[0Ktravis_time:start:20936712[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:20936712:start=1578223776901157948,finish=1578223782207871129,duration=5306713181,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:20936712:start=1578223776901157948,finish=1578223782375664294,duration=5474506346,event=checkout[0Ktravis_time:start:0c8c2222[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0c8c2222:start=1578223782379949208,finish=1578223782390714244,duration=10765036,event=env[0Ktravis_time:start:2259bb48[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2259bb48:start=1578223782398332626,finish=1578223782403461382,duration=5128756,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:009474ab[0K$ python system_testing.py -s of-of
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:3ab18c507e8bd47b0be2b872093edcab70bf5a758a63df93a1878c720f6aeddb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B
```
[
Full job log](https://api.travis-ci.org/v3/job/632899742/log.txt)