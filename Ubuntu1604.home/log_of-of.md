## Status: Failure 
Build: [1384](https://travis-ci.org/precice/systemtests/builds/631624532) 

Job: [1384.15](https://travis-ci.org/precice/systemtests/jobs/631624547) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/131) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:0540f07e:start=1577904713134092928,finish=1577904713139747083,duration=5654155,event=show_system_info[0Ktravis_time:start:3930eb18[0Ktravis_time:end:3930eb18:start=1577904713143599741,finish=1577904713162819692,duration=19219951,event=rm_riak_source[0Ktravis_time:start:05bc6e68[0Ktravis_time:end:05bc6e68:start=1577904713168519475,finish=1577904713173159223,duration=4639748,event=fix_rwky_redis[0Ktravis_time:start:22a0b9c6[0Ktravis_time:end:22a0b9c6:start=1577904713176018584,finish=1577904713568431959,duration=392413375,event=wait_for_network[0Ktravis_time:start:002ed8d8[0Ktravis_time:end:002ed8d8:start=1577904713573170536,finish=1577904714464541985,duration=891371449,event=update_apt_keys[0Ktravis_time:start:1d43a374[0Ktravis_time:end:1d43a374:start=1577904714468640452,finish=1577904715363633118,duration=894992666,event=fix_hhvm_source[0Ktravis_time:start:007f4293[0Ktravis_time:end:007f4293:start=1577904715368410886,finish=1577904715377093655,duration=8682769,event=update_mongo_arch[0Ktravis_time:start:1ef53c04[0Ktravis_time:end:1ef53c04:start=1577904715381113667,finish=1577904715418228888,duration=37115221,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0eed546c[0Ktravis_time:end:0eed546c:start=1577904715422219391,finish=1577904715424608303,duration=2388912,event=update_glibc[0Ktravis_time:start:1034ba33[0Ktravis_time:end:1034ba33:start=1577904715428896127,finish=1577904715436040444,duration=7144317,event=clean_up_path[0Ktravis_time:start:2219734e[0Ktravis_time:end:2219734e:start=1577904715440319734,finish=1577904715447418341,duration=7098607,event=fix_resolv_conf[0Ktravis_time:start:012804b0[0Ktravis_time:end:012804b0:start=1577904715450228684,finish=1577904715460445234,duration=10216550,event=fix_etc_hosts[0Ktravis_time:start:237bd032[0Ktravis_time:end:237bd032:start=1577904715463970486,finish=1577904715473409758,duration=9439272,event=fix_mvn_settings_xml[0Ktravis_time:start:0dc53480[0Ktravis_time:end:0dc53480:start=1577904715477016271,finish=1577904715486740884,duration=9724613,event=no_ipv6_localhost[0Ktravis_time:start:24632628[0Ktravis_time:end:24632628:start=1577904715490328181,finish=1577904715492471650,duration=2143469,event=fix_etc_mavenrc[0Ktravis_time:start:30480dfc[0Ktravis_time:end:30480dfc:start=1577904715496949439,finish=1577904715499905744,duration=2956305,event=fix_wwdr_certificate[0Ktravis_time:start:02d22590[0Ktravis_time:end:02d22590:start=1577904715504075598,finish=1577904715524911384,duration=20835786,event=put_localhost_first[0Ktravis_time:start:076955fb[0Ktravis_time:end:076955fb:start=1577904715527854348,finish=1577904715531414188,duration=3559840,event=home_paths[0Ktravis_time:start:13b5c148[0Ktravis_time:end:13b5c148:start=1577904715534741941,finish=1577904715547961046,duration=13219105,event=disable_initramfs[0Ktravis_time:start:03505ba2[0Ktravis_time:end:03505ba2:start=1577904715551599310,finish=1577904715754043212,duration=202443902,event=disable_ssh_roaming[0Ktravis_time:start:0271d9ee[0Ktravis_time:end:0271d9ee:start=1577904715759066289,finish=1577904715761270687,duration=2204398,event=debug_tools[0Ktravis_time:start:14b6872e[0Ktravis_time:end:14b6872e:start=1577904715764786365,finish=1577904715767633211,duration=2846846,event=uninstall_oclint[0Ktravis_time:start:010dbab4[0Ktravis_time:end:010dbab4:start=1577904715771123945,finish=1577904715773955235,duration=2831290,event=rvm_use[0Ktravis_time:start:000df4ca[0Ktravis_time:end:000df4ca:start=1577904715777380798,finish=1577904715786253816,duration=8873018,event=rm_etc_boto_cfg[0Ktravis_time:start:040046f1[0Ktravis_time:end:040046f1:start=1577904715789899864,finish=1577904715792198723,duration=2298859,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0b52ff0c[0Ktravis_time:end:0b52ff0c:start=1577904715796088695,finish=1577904715840385239,duration=44296544,event=enable_i386[0Ktravis_time:start:11b98294[0Ktravis_time:end:11b98294:start=1577904715844318901,finish=1577904715847938549,duration=3619648,event=update_rubygems[0Ktravis_time:start:127efa80[0Ktravis_time:end:127efa80:start=1577904715851698368,finish=1577904716683980469,duration=832282101,event=ensure_path_components[0Ktravis_time:start:01f43b88[0Ktravis_time:end:01f43b88:start=1577904716688846349,finish=1577904716692028168,duration=3181819,event=redefine_curl[0Ktravis_time:start:1a8682c8[0Ktravis_time:end:1a8682c8:start=1577904716696861001,finish=1577904716745706654,duration=48845653,event=nonblock_pipe[0Ktravis_time:start:241ad8cb[0Ktravis_time:end:241ad8cb:start=1577904716749034938,finish=1577904722777108792,duration=6028073854,event=apt_get_update[0Ktravis_time:start:01440937[0Ktravis_time:end:01440937:start=1577904722781224990,finish=1577904722783594807,duration=2369817,event=deprecate_xcode_64[0Ktravis_time:start:041e56b4[0Ktravis_time:end:041e56b4:start=1577904722786608961,finish=1577904726297678579,duration=3511069618,event=update_heroku[0Ktravis_time:start:11d0c6f2[0Ktravis_time:end:11d0c6f2:start=1577904726301772630,finish=1577904726304403523,duration=2630893,event=shell_session_update[0Ktravis_time:start:01fdccac[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3900
travis_fold:end:docker_mtu[0Ktravis_time:end:01fdccac:start=1577904726308978563,finish=1577904727500208192,duration=1191229629,event=set_docker_mtu[0Ktravis_time:start:2d9c9aec[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2d9c9aec:start=1577904727503967245,finish=1577904727555876916,duration=51909671,event=resolvconf[0Ktravis_time:start:047bde5c[0Ktravis_time:end:047bde5c:start=1577904727559605090,finish=1577904727640068424,duration=80463334,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0a06343a[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0a06343a:start=1577904727711528786,finish=1577904728228545813,duration=517017027,event=configure[0Ktravis_time:start:0df0564e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0df0564e:start=1577904728233023762,finish=1577904736385365546,duration=8152341784,event=configure[0Ktravis_time:start:0d01d468[0Ktravis_fold:start:services[0Ktravis_time:start:159ad0ac[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:159ad0ac:start=1577904736407692817,finish=1577904736420324513,duration=12631696,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:159ad0ac:start=1577904736407692817,finish=1577904739425583937,duration=3017891120,event=services[0Ktravis_time:start:01f570bb[0Ktravis_time:end:01f570bb:start=1577904739429115333,finish=1577904739431528348,duration=2413015,event=fix_ps4[0Ktravis_time:start:2198a3cd[0K
travis_fold:start:git.checkout[0Ktravis_time:start:014f5b1f[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:014f5b1f:start=1577904739438120522,finish=1577904744966111554,duration=5527991032,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:035d1d50[0K$ git fetch origin +refs/pull/131/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/131/merge -> FETCH_HEAD
travis_time:end:035d1d50:start=1577904744970470021,finish=1577904748655054644,duration=3684584623,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:035d1d50:start=1577904744970470021,finish=1577904749589637540,duration=4619167519,event=checkout[0Ktravis_time:start:06637bc6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:06637bc6:start=1577904749593818904,finish=1577904749605095911,duration=11277007,event=env[0Ktravis_time:start:03eaaf3c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03eaaf3c:start=1577904749612820037,finish=1577904749618487634,duration=5667597,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0d05edc3[0K$ python system_testing.py -s of-of
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
Digest: sha256:2eadc3a0c70c4b90e6aa86c93f35b0b1f6d1f10272fd491ce30485450f51e8ca
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B
```
[
Full job log](https://api.travis-ci.org/v3/job/631624547/log.txt)