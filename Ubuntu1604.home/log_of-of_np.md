## Status: Failure 
Build: [1356](https://travis-ci.org/precice/systemtests/builds/628061312) 

Job: [1356.23](https://travis-ci.org/precice/systemtests/jobs/628061335) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:19152d95:start=1576927522663820331,finish=1576927522668790510,duration=4970179,event=show_system_info[0Ktravis_time:start:28c19ce2[0Ktravis_time:end:28c19ce2:start=1576927522671370582,finish=1576927522693785534,duration=22414952,event=rm_riak_source[0Ktravis_time:start:2199c086[0Ktravis_time:end:2199c086:start=1576927522697487466,finish=1576927522703946151,duration=6458685,event=fix_rwky_redis[0Ktravis_time:start:0d0c6bac[0Ktravis_time:end:0d0c6bac:start=1576927522707431478,finish=1576927523103612858,duration=396181380,event=wait_for_network[0Ktravis_time:start:115d26f0[0Ktravis_time:end:115d26f0:start=1576927523107409712,finish=1576927524853872777,duration=1746463065,event=update_apt_keys[0Ktravis_time:start:027186d1[0Ktravis_time:end:027186d1:start=1576927524857860941,finish=1576927525885060194,duration=1027199253,event=fix_hhvm_source[0Ktravis_time:start:08d9e880[0Ktravis_time:end:08d9e880:start=1576927525889770969,finish=1576927525899425231,duration=9654262,event=update_mongo_arch[0Ktravis_time:start:2f836405[0Ktravis_time:end:2f836405:start=1576927525902504031,finish=1576927525939596550,duration=37092519,event=fix_sudo_enabled_trusty[0Ktravis_time:start:306ca9a1[0Ktravis_time:end:306ca9a1:start=1576927525943812450,finish=1576927525946416350,duration=2603900,event=update_glibc[0Ktravis_time:start:0047f220[0Ktravis_time:end:0047f220:start=1576927525951112229,finish=1576927525958797070,duration=7684841,event=clean_up_path[0Ktravis_time:start:035a9624[0Ktravis_time:end:035a9624:start=1576927525963085131,finish=1576927525971430632,duration=8345501,event=fix_resolv_conf[0Ktravis_time:start:03627930[0Ktravis_time:end:03627930:start=1576927525976366036,finish=1576927525984684578,duration=8318542,event=fix_etc_hosts[0Ktravis_time:start:09c93546[0Ktravis_time:end:09c93546:start=1576927525989430364,finish=1576927525999136783,duration=9706419,event=fix_mvn_settings_xml[0Ktravis_time:start:07c2cb97[0Ktravis_time:end:07c2cb97:start=1576927526003053375,finish=1576927526011493603,duration=8440228,event=no_ipv6_localhost[0Ktravis_time:start:1155f8a0[0Ktravis_time:end:1155f8a0:start=1576927526014557980,finish=1576927526017087246,duration=2529266,event=fix_etc_mavenrc[0Ktravis_time:start:22fd8a5b[0Ktravis_time:end:22fd8a5b:start=1576927526020298654,finish=1576927526023430110,duration=3131456,event=fix_wwdr_certificate[0Ktravis_time:start:27d07031[0Ktravis_time:end:27d07031:start=1576927526026637006,finish=1576927526051994174,duration=25357168,event=put_localhost_first[0Ktravis_time:start:129d3548[0Ktravis_time:end:129d3548:start=1576927526055723898,finish=1576927526058803058,duration=3079160,event=home_paths[0Ktravis_time:start:0efbd08f[0Ktravis_time:end:0efbd08f:start=1576927526063232106,finish=1576927526074002479,duration=10770373,event=disable_initramfs[0Ktravis_time:start:1682ee96[0Ktravis_time:end:1682ee96:start=1576927526078406038,finish=1576927526346609111,duration=268203073,event=disable_ssh_roaming[0Ktravis_time:start:28cd31e4[0Ktravis_time:end:28cd31e4:start=1576927526350286713,finish=1576927526352598282,duration=2311569,event=debug_tools[0Ktravis_time:start:27571d70[0Ktravis_time:end:27571d70:start=1576927526355772498,finish=1576927526361235644,duration=5463146,event=uninstall_oclint[0Ktravis_time:start:0058fef8[0Ktravis_time:end:0058fef8:start=1576927526364419564,finish=1576927526367883138,duration=3463574,event=rvm_use[0Ktravis_time:start:0807c0d8[0Ktravis_time:end:0807c0d8:start=1576927526371221791,finish=1576927526380340133,duration=9118342,event=rm_etc_boto_cfg[0Ktravis_time:start:0a46fe83[0Ktravis_time:end:0a46fe83:start=1576927526383501821,finish=1576927526387559244,duration=4057423,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1d78d110[0Ktravis_time:end:1d78d110:start=1576927526391561364,finish=1576927526436618706,duration=45057342,event=enable_i386[0Ktravis_time:start:2d720222[0Ktravis_time:end:2d720222:start=1576927526440487525,finish=1576927526444484484,duration=3996959,event=update_rubygems[0Ktravis_time:start:02729760[0Ktravis_time:end:02729760:start=1576927526450010892,finish=1576927527306438569,duration=856427677,event=ensure_path_components[0Ktravis_time:start:2104137c[0Ktravis_time:end:2104137c:start=1576927527310591408,finish=1576927527313386836,duration=2795428,event=redefine_curl[0Ktravis_time:start:010466c0[0Ktravis_time:end:010466c0:start=1576927527316505828,finish=1576927527360602900,duration=44097072,event=nonblock_pipe[0Ktravis_time:start:0db26745[0Ktravis_time:end:0db26745:start=1576927527364811514,finish=1576927527467499169,duration=102687655,event=apt_get_update[0Ktravis_time:start:21171cba[0Ktravis_time:end:21171cba:start=1576927527472147831,finish=1576927527474731192,duration=2583361,event=deprecate_xcode_64[0Ktravis_time:start:08624070[0Ktravis_time:end:08624070:start=1576927527478157811,finish=1576927531326217357,duration=3848059546,event=update_heroku[0Ktravis_time:start:0341f460[0Ktravis_time:end:0341f460:start=1576927531330263381,finish=1576927531332481446,duration=2218065,event=shell_session_update[0Ktravis_time:start:2c179482[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3903
travis_fold:end:docker_mtu[0Ktravis_time:end:2c179482:start=1576927531336442697,finish=1576927532522001790,duration=1185559093,event=set_docker_mtu[0Ktravis_time:start:0b4569d6[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0b4569d6:start=1576927532526086426,finish=1576927532580745861,duration=54659435,event=resolvconf[0Ktravis_time:start:1611b4e7[0Ktravis_time:end:1611b4e7:start=1576927532584750338,finish=1576927532671907290,duration=87156952,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0fac7baa[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0fac7baa:start=1576927532749191059,finish=1576927533195528910,duration=446337851,event=configure[0Ktravis_time:start:30923b1b[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:30923b1b:start=1576927533200702497,finish=1576927541529192479,duration=8328489982,event=configure[0Ktravis_time:start:389c9428[0Ktravis_fold:start:services[0Ktravis_time:start:0931d244[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0931d244:start=1576927541552119105,finish=1576927541564145452,duration=12026347,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0931d244:start=1576927541552119105,finish=1576927544569812052,duration=3017692947,event=services[0Ktravis_time:start:0b7605fa[0Ktravis_time:end:0b7605fa:start=1576927544574969691,finish=1576927544577661349,duration=2691658,event=fix_ps4[0Ktravis_time:start:00e3c6ee[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1682affe[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1682affe:start=1576927544587000818,finish=1576927549894904291,duration=5307903473,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ff457bed2521c9ab78f7f6e490c7785219151c1e
travis_fold:end:git.checkout[0K
travis_time:end:1682affe:start=1576927544587000818,finish=1576927550745960074,duration=6158959256,event=checkout[0Ktravis_time:start:0581f898[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0581f898:start=1576927550750464541,finish=1576927550759968791,duration=9504250,event=env[0Ktravis_time:start:2f860728[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2f860728:start=1576927550764186827,finish=1576927550769219724,duration=5032897,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09bfa7a0[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:7c92a2c6bbcb6b6beff92d0a940779769c2477b807c202954c537e2e0deb9bed
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid', 'Solid']
Files only in output(right)   : []
travis_time:end:09bfa7a0:start=1576927551050627241,finish=1576927617737940497,duration=66687313256,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1ab3257e[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/628061335/log.txt)