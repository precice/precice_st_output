## Status: Passing 
Build: [1006](https://travis-ci.org/precice/systemtests/builds/602019179) 

Job: [1006.20](https://travis-ci.org/precice/systemtests/jobs/602019199) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4ea43c307afb...2f3949cca1ae) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:045929fa:start=1571867993455528337,finish=1571867993462855258,duration=7326921,event=show_system_info[0Ktravis_time:start:167e7fa0[0Ktravis_time:end:167e7fa0:start=1571867993465997704,finish=1571867993492429148,duration=26431444,event=rm_riak_source[0Ktravis_time:start:0b13bb78[0Ktravis_time:end:0b13bb78:start=1571867993498485241,finish=1571867993506392781,duration=7907540,event=fix_rwky_redis[0Ktravis_time:start:0e5c182d[0Ktravis_time:end:0e5c182d:start=1571867993509833980,finish=1571867993900672962,duration=390838982,event=wait_for_network[0Ktravis_time:start:2712c721[0Ktravis_time:end:2712c721:start=1571867993905992777,finish=1571867995485263488,duration=1579270711,event=update_apt_keys[0Ktravis_time:start:069c5922[0Ktravis_time:end:069c5922:start=1571867995489860200,finish=1571867996551649211,duration=1061789011,event=fix_hhvm_source[0Ktravis_time:start:0c339bec[0Ktravis_time:end:0c339bec:start=1571867996556199834,finish=1571867996567092009,duration=10892175,event=update_mongo_arch[0Ktravis_time:start:17ff24c4[0Ktravis_time:end:17ff24c4:start=1571867996572020965,finish=1571867996614025359,duration=42004394,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1bbbd113[0Ktravis_time:end:1bbbd113:start=1571867996618649544,finish=1571867996621843644,duration=3194100,event=update_glibc[0Ktravis_time:start:01e9ddae[0Ktravis_time:end:01e9ddae:start=1571867996626695450,finish=1571867996636621959,duration=9926509,event=clean_up_path[0Ktravis_time:start:18a28d20[0Ktravis_time:end:18a28d20:start=1571867996643435576,finish=1571867996651570162,duration=8134586,event=fix_resolv_conf[0Ktravis_time:start:1b5bdeaa[0Ktravis_time:end:1b5bdeaa:start=1571867996656340371,finish=1571867996668777072,duration=12436701,event=fix_etc_hosts[0Ktravis_time:start:05991df2[0Ktravis_time:end:05991df2:start=1571867996673547001,finish=1571867996682708818,duration=9161817,event=fix_mvn_settings_xml[0Ktravis_time:start:1b7c5390[0Ktravis_time:end:1b7c5390:start=1571867996687972017,finish=1571867996698227062,duration=10255045,event=no_ipv6_localhost[0Ktravis_time:start:247ec3d0[0Ktravis_time:end:247ec3d0:start=1571867996702962444,finish=1571867996706103697,duration=3141253,event=fix_etc_mavenrc[0Ktravis_time:start:3289761c[0Ktravis_time:end:3289761c:start=1571867996710388477,finish=1571867996714323281,duration=3934804,event=fix_wwdr_certificate[0Ktravis_time:start:22f34e14[0Ktravis_time:end:22f34e14:start=1571867996719212308,finish=1571867996747110088,duration=27897780,event=put_localhost_first[0Ktravis_time:start:0804b421[0Ktravis_time:end:0804b421:start=1571867996752349275,finish=1571867996756165048,duration=3815773,event=home_paths[0Ktravis_time:start:1631189a[0Ktravis_time:end:1631189a:start=1571867996760971109,finish=1571867996774849525,duration=13878416,event=disable_initramfs[0Ktravis_time:start:086588b8[0Ktravis_time:end:086588b8:start=1571867996779873814,finish=1571867997074823687,duration=294949873,event=disable_ssh_roaming[0Ktravis_time:start:0dcef0cc[0Ktravis_time:end:0dcef0cc:start=1571867997080136459,finish=1571867997083773038,duration=3636579,event=debug_tools[0Ktravis_time:start:17f3514e[0Ktravis_time:end:17f3514e:start=1571867997088860623,finish=1571867997093977001,duration=5116378,event=uninstall_oclint[0Ktravis_time:start:0b35eb6f[0Ktravis_time:end:0b35eb6f:start=1571867997099063294,finish=1571867997107799309,duration=8736015,event=rvm_use[0Ktravis_time:start:1167475f[0Ktravis_time:end:1167475f:start=1571867997113417407,finish=1571867997124419175,duration=11001768,event=rm_etc_boto_cfg[0Ktravis_time:start:080c8b60[0Ktravis_time:end:080c8b60:start=1571867997131013379,finish=1571867997134903257,duration=3889878,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2a3d3a6c[0Ktravis_time:end:2a3d3a6c:start=1571867997139469272,finish=1571867997200037487,duration=60568215,event=enable_i386[0Ktravis_time:start:110421b0[0Ktravis_time:end:110421b0:start=1571867997204960556,finish=1571867997211166007,duration=6205451,event=update_rubygems[0Ktravis_time:start:319b408d[0Ktravis_time:end:319b408d:start=1571867997217408936,finish=1571867998267606516,duration=1050197580,event=ensure_path_components[0Ktravis_time:start:08272f1e[0Ktravis_time:end:08272f1e:start=1571867998272628528,finish=1571867998275583700,duration=2955172,event=redefine_curl[0Ktravis_time:start:0e9aae66[0Ktravis_time:end:0e9aae66:start=1571867998282530212,finish=1571867998337755101,duration=55224889,event=nonblock_pipe[0Ktravis_time:start:177772e0[0Ktravis_time:end:177772e0:start=1571867998343608079,finish=1571868001392702481,duration=3049094402,event=apt_get_update[0Ktravis_time:start:279a151f[0Ktravis_time:end:279a151f:start=1571868001400449886,finish=1571868001404352160,duration=3902274,event=deprecate_xcode_64[0Ktravis_time:start:2d7e8d6c[0Ktravis_time:end:2d7e8d6c:start=1571868001410428285,finish=1571868006419280386,duration=5008852101,event=update_heroku[0Ktravis_time:start:26cc0dc3[0Ktravis_time:end:26cc0dc3:start=1571868006423544070,finish=1571868006426430517,duration=2886447,event=shell_session_update[0Ktravis_time:start:00aa5790[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3957
travis_fold:end:docker_mtu[0Ktravis_time:end:00aa5790:start=1571868006430216165,finish=1571868007624715675,duration=1194499510,event=set_docker_mtu[0Ktravis_time:start:2916c505[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2916c505:start=1571868007630350871,finish=1571868007700292357,duration=69941486,event=resolvconf[0Ktravis_time:start:06edca80[0Ktravis_time:end:06edca80:start=1571868007705397545,finish=1571868007814335334,duration=108937789,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0f2a9e2e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0f2a9e2e:start=1571868007902534493,finish=1571868008319976742,duration=417442249,event=configure[0Ktravis_time:start:02471fde[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02471fde:start=1571868008325205088,finish=1571868018966224493,duration=10641019405,event=configure[0Ktravis_time:start:001852da[0Ktravis_fold:start:services[0Ktravis_time:start:0084da91[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0084da91:start=1571868018992132482,finish=1571868019007363392,duration=15230910,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0084da91:start=1571868018992132482,finish=1571868022013652630,duration=3021520148,event=services[0Ktravis_time:start:077d654a[0Ktravis_time:end:077d654a:start=1571868022018273834,finish=1571868022021229993,duration=2956159,event=fix_ps4[0Ktravis_time:start:2cccfe68[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0232b0dc[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0232b0dc:start=1571868022031087434,finish=1571868028307775802,duration=6276688368,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2f3949cca1ae3a51d8f298d1e4286edbe06c066c
travis_fold:end:git.checkout[0K
travis_time:end:0232b0dc:start=1571868022031087434,finish=1571868028550136750,duration=6519049316,event=checkout[0Ktravis_time:start:19da9c6f[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:19da9c6f:start=1571868028556079894,finish=1571868028570311516,duration=14231622,event=env[0Ktravis_time:start:14d95ec0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:14d95ec0:start=1571868028575932209,finish=1571868028582829008,duration=6896799,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:02286a44[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:71e59392c3eda1815295b9b43606e5b8ae997da323ad190311b227bd2bde769e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:02286a44:start=1571868028941620458,finish=1571868151026422078,duration=122084801620,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:008dfb10[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602019199/log.txt)