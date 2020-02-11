## Status: Failure 
Build: [1668](https://travis-ci.org/precice/systemtests/builds/648944980) 

Job: [1668.21](https://travis-ci.org/precice/systemtests/jobs/648945001) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/136) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

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
travis_time:end:0d3a5092:start=1581436917679455511,finish=1581436917688901597,duration=9446086,event=show_system_info[0Ktravis_time:start:1765930f[0Ktravis_time:end:1765930f:start=1581436917692741769,finish=1581436917724202333,duration=31460564,event=rm_riak_source[0Ktravis_time:start:127f3878[0Ktravis_time:end:127f3878:start=1581436917727710617,finish=1581436917736100963,duration=8390346,event=fix_rwky_redis[0Ktravis_time:start:0691e14d[0Ktravis_time:end:0691e14d:start=1581436917741129397,finish=1581436918138877082,duration=397747685,event=wait_for_network[0Ktravis_time:start:0100d529[0Ktravis_time:end:0100d529:start=1581436918143709600,finish=1581436919704415017,duration=1560705417,event=update_apt_keys[0Ktravis_time:start:0405bd74[0Ktravis_time:end:0405bd74:start=1581436919710116996,finish=1581436920724591216,duration=1014474220,event=fix_hhvm_source[0Ktravis_time:start:049c2e00[0Ktravis_time:end:049c2e00:start=1581436920729241230,finish=1581436920741053980,duration=11812750,event=update_mongo_arch[0Ktravis_time:start:1f1c50d8[0Ktravis_time:end:1f1c50d8:start=1581436920747974020,finish=1581436920790393040,duration=42419020,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1fbd28f8[0Ktravis_time:end:1fbd28f8:start=1581436920795489560,finish=1581436920799019901,duration=3530341,event=update_glibc[0Ktravis_time:start:046b8358[0Ktravis_time:end:046b8358:start=1581436920804083629,finish=1581436920816821682,duration=12738053,event=clean_up_path[0Ktravis_time:start:00e725f2[0Ktravis_time:end:00e725f2:start=1581436920821545318,finish=1581436920830504873,duration=8959555,event=fix_resolv_conf[0Ktravis_time:start:1a6a4cd8[0Ktravis_time:end:1a6a4cd8:start=1581436920835403605,finish=1581436920845112215,duration=9708610,event=fix_etc_hosts[0Ktravis_time:start:19c95563[0Ktravis_time:end:19c95563:start=1581436920849868430,finish=1581436920859599751,duration=9731321,event=fix_mvn_settings_xml[0Ktravis_time:start:13047b37[0Ktravis_time:end:13047b37:start=1581436920863989027,finish=1581436920874427472,duration=10438445,event=no_ipv6_localhost[0Ktravis_time:start:03f2743e[0Ktravis_time:end:03f2743e:start=1581436920880775925,finish=1581436920884165937,duration=3390012,event=fix_etc_mavenrc[0Ktravis_time:start:011c1194[0Ktravis_time:end:011c1194:start=1581436920888607595,finish=1581436920894296692,duration=5689097,event=fix_wwdr_certificate[0Ktravis_time:start:0ded3967[0Ktravis_time:end:0ded3967:start=1581436920901130806,finish=1581436920927086527,duration=25955721,event=put_localhost_first[0Ktravis_time:start:12ddaccc[0Ktravis_time:end:12ddaccc:start=1581436920932285062,finish=1581436920936456766,duration=4171704,event=home_paths[0Ktravis_time:start:37e12c36[0Ktravis_time:end:37e12c36:start=1581436920943183825,finish=1581436920955430473,duration=12246648,event=disable_initramfs[0Ktravis_time:start:025435a4[0Ktravis_time:end:025435a4:start=1581436920959939658,finish=1581436921269053877,duration=309114219,event=disable_ssh_roaming[0Ktravis_time:start:377de2c0[0Ktravis_time:end:377de2c0:start=1581436921273252594,finish=1581436921276491051,duration=3238457,event=debug_tools[0Ktravis_time:start:27424437[0Ktravis_time:end:27424437:start=1581436921281201762,finish=1581436921285927178,duration=4725416,event=uninstall_oclint[0Ktravis_time:start:16c602d0[0Ktravis_time:end:16c602d0:start=1581436921290829326,finish=1581436921294626520,duration=3797194,event=rvm_use[0Ktravis_time:start:23868666[0Ktravis_time:end:23868666:start=1581436921298468369,finish=1581436921313017078,duration=14548709,event=rm_etc_boto_cfg[0Ktravis_time:start:0379a3d8[0Ktravis_time:end:0379a3d8:start=1581436921322016993,finish=1581436921325126717,duration=3109724,event=rm_oraclejdk8_symlink[0Ktravis_time:start:20d1ff20[0Ktravis_time:end:20d1ff20:start=1581436921329517520,finish=1581436921386746056,duration=57228536,event=enable_i386[0Ktravis_time:start:00c8aea2[0Ktravis_time:end:00c8aea2:start=1581436921391478096,finish=1581436921396136589,duration=4658493,event=update_rubygems[0Ktravis_time:start:29c83f04[0Ktravis_time:end:29c83f04:start=1581436921400281447,finish=1581436922430386750,duration=1030105303,event=ensure_path_components[0Ktravis_time:start:07549b4b[0Ktravis_time:end:07549b4b:start=1581436922436533155,finish=1581436922440693685,duration=4160530,event=redefine_curl[0Ktravis_time:start:1377e9d6[0Ktravis_time:end:1377e9d6:start=1581436922444695294,finish=1581436922506640837,duration=61945543,event=nonblock_pipe[0Ktravis_time:start:0055f26b[0Ktravis_time:end:0055f26b:start=1581436922511058980,finish=1581436928550156062,duration=6039097082,event=apt_get_update[0Ktravis_time:start:1f7ddf43[0Ktravis_time:end:1f7ddf43:start=1581436928554572003,finish=1581436928557494150,duration=2922147,event=deprecate_xcode_64[0Ktravis_time:start:29ea3ff0[0Ktravis_time:end:29ea3ff0:start=1581436928562364173,finish=1581436932954885982,duration=4392521809,event=update_heroku[0Ktravis_time:start:000d022e[0Ktravis_time:end:000d022e:start=1581436932960474825,finish=1581436932963283016,duration=2808191,event=shell_session_update[0Ktravis_time:start:02220ea0[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3902
travis_fold:end:docker_mtu[0Ktravis_time:end:02220ea0:start=1581436932966991627,finish=1581436934161745555,duration=1194753928,event=set_docker_mtu[0Ktravis_time:start:1ffbd8cf[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1ffbd8cf:start=1581436934166086327,finish=1581436934232197161,duration=66110834,event=resolvconf[0Ktravis_time:start:03fa316d[0Ktravis_time:end:03fa316d:start=1581436934237120762,finish=1581436934333568679,duration=96447917,event=maven_central_mirror[0Ktravis_time:start:222fee51[0Ktravis_time:end:222fee51:start=1581436934339405637,finish=1581436934415337464,duration=75931827,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1a07b680[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1a07b680:start=1581436934503157690,finish=1581436934964875967,duration=461718277,event=configure[0Ktravis_time:start:2b03acf3[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2b03acf3:start=1581436934970122493,finish=1581436949788427937,duration=14818305444,event=configure[0Ktravis_time:start:002f91ea[0Ktravis_fold:start:services[0Ktravis_time:start:039cb5ee[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:039cb5ee:start=1581436949816476003,finish=1581436949834277939,duration=17801936,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:039cb5ee:start=1581436949816476003,finish=1581436952841739612,duration=3025263609,event=services[0Ktravis_time:start:17915724[0Ktravis_time:end:17915724:start=1581436952846919740,finish=1581436952849821622,duration=2901882,event=fix_ps4[0Ktravis_time:start:0c422f44[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0911ff19[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0911ff19:start=1581436952860883887,finish=1581436959969732408,duration=7108848521,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:3575be60[0K$ git fetch origin +refs/pull/136/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/136/merge -> FETCH_HEAD
travis_time:end:3575be60:start=1581436959975232140,finish=1581436960514629798,duration=539397658,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:3575be60:start=1581436959975232140,finish=1581436961344655390,duration=1369423250,event=checkout[0Ktravis_time:start:12d0499e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:12d0499e:start=1581436961349137354,finish=1581436961364226887,duration=15089533,event=env[0Ktravis_time:start:3add6e46[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:3add6e46:start=1581436961372352719,finish=1581436961381405360,duration=9052641,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0a2f7cfe[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-fluid
    image: [secure]/openfoam-adapter-ubuntu1604.home-i_125:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  openfoam-adapter-solid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-solid
    image: [secure]/openfoam-adapter-ubuntu1604.home-i_125:latest
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
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-i_125:latest)...
pull access denied for [secure]/openfoam-adapter-ubuntu1604.home-i_125, repository does not exist or may require 'docker login'
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-i_125; docker-compose config && bash ../../silent_compose.sh 
TESTS FAILED WITH: Command 'export PRECICE_BASE=-ubuntu1604.home-i_125; docker-compose config && bash ../../silent_compose.sh ' returned non-zero exit status 1
travis_time:end:0a2f7cfe:start=1581436961753352037,finish=1581436965295698162,duration=3542346125,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1e8a2d73[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648945001/log.txt)