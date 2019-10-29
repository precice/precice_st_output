## Status: Passing 
Build: [1045](https://travis-ci.org/precice/systemtests/builds/604222443) 

Job: [1045.18](https://travis-ci.org/precice/systemtests/jobs/604222463) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:042c2108:start=1572316865798793714,finish=1572316865804832122,duration=6038408,event=show_system_info[0Ktravis_time:start:029c61d2[0Ktravis_time:end:029c61d2:start=1572316865807742426,finish=1572316865833022435,duration=25280009,event=rm_riak_source[0Ktravis_time:start:1306aee6[0Ktravis_time:end:1306aee6:start=1572316865836117415,finish=1572316865847104856,duration=10987441,event=fix_rwky_redis[0Ktravis_time:start:0820b598[0Ktravis_time:end:0820b598:start=1572316865850424922,finish=1572316866256950750,duration=406525828,event=wait_for_network[0Ktravis_time:start:21787990[0Ktravis_time:end:21787990:start=1572316866261579014,finish=1572316867839340156,duration=1577761142,event=update_apt_keys[0Ktravis_time:start:156b8c80[0Ktravis_time:end:156b8c80:start=1572316867843588430,finish=1572316868943387553,duration=1099799123,event=fix_hhvm_source[0Ktravis_time:start:0400beb5[0Ktravis_time:end:0400beb5:start=1572316868948201380,finish=1572316868958061909,duration=9860529,event=update_mongo_arch[0Ktravis_time:start:0c375c74[0Ktravis_time:end:0c375c74:start=1572316868962333143,finish=1572316869003557868,duration=41224725,event=fix_sudo_enabled_trusty[0Ktravis_time:start:094a65b0[0Ktravis_time:end:094a65b0:start=1572316869008986755,finish=1572316869011698647,duration=2711892,event=update_glibc[0Ktravis_time:start:2803e940[0Ktravis_time:end:2803e940:start=1572316869016155095,finish=1572316869026535892,duration=10380797,event=clean_up_path[0Ktravis_time:start:1ad504bb[0Ktravis_time:end:1ad504bb:start=1572316869031045094,finish=1572316869039718940,duration=8673846,event=fix_resolv_conf[0Ktravis_time:start:0dddef14[0Ktravis_time:end:0dddef14:start=1572316869044779961,finish=1572316869054233229,duration=9453268,event=fix_etc_hosts[0Ktravis_time:start:1164572a[0Ktravis_time:end:1164572a:start=1572316869058834553,finish=1572316869068406830,duration=9572277,event=fix_mvn_settings_xml[0Ktravis_time:start:0db6fd20[0Ktravis_time:end:0db6fd20:start=1572316869072694692,finish=1572316869082313252,duration=9618560,event=no_ipv6_localhost[0Ktravis_time:start:09de703e[0Ktravis_time:end:09de703e:start=1572316869087913653,finish=1572316869090566707,duration=2653054,event=fix_etc_mavenrc[0Ktravis_time:start:08445321[0Ktravis_time:end:08445321:start=1572316869095281443,finish=1572316869099296248,duration=4014805,event=fix_wwdr_certificate[0Ktravis_time:start:0eed483c[0Ktravis_time:end:0eed483c:start=1572316869103845606,finish=1572316869129685152,duration=25839546,event=put_localhost_first[0Ktravis_time:start:06a07c2f[0Ktravis_time:end:06a07c2f:start=1572316869134338566,finish=1572316869138427416,duration=4088850,event=home_paths[0Ktravis_time:start:058373df[0Ktravis_time:end:058373df:start=1572316869142970050,finish=1572316869157253542,duration=14283492,event=disable_initramfs[0Ktravis_time:start:0407c498[0Ktravis_time:end:0407c498:start=1572316869161326394,finish=1572316869493313506,duration=331987112,event=disable_ssh_roaming[0Ktravis_time:start:120d0f07[0Ktravis_time:end:120d0f07:start=1572316869498517750,finish=1572316869501745023,duration=3227273,event=debug_tools[0Ktravis_time:start:102bcef3[0Ktravis_time:end:102bcef3:start=1572316869506718485,finish=1572316869510550517,duration=3832032,event=uninstall_oclint[0Ktravis_time:start:07e1ec84[0Ktravis_time:end:07e1ec84:start=1572316869517557316,finish=1572316869521359247,duration=3801931,event=rvm_use[0Ktravis_time:start:013aedb2[0Ktravis_time:end:013aedb2:start=1572316869526404225,finish=1572316869535200148,duration=8795923,event=rm_etc_boto_cfg[0Ktravis_time:start:0b042184[0Ktravis_time:end:0b042184:start=1572316869541015411,finish=1572316869543752847,duration=2737436,event=rm_oraclejdk8_symlink[0Ktravis_time:start:09916695[0Ktravis_time:end:09916695:start=1572316869549631598,finish=1572316869604481770,duration=54850172,event=enable_i386[0Ktravis_time:start:1f6c7fa8[0Ktravis_time:end:1f6c7fa8:start=1572316869609305836,finish=1572316869613669136,duration=4363300,event=update_rubygems[0Ktravis_time:start:0b2de2a0[0Ktravis_time:end:0b2de2a0:start=1572316869618937019,finish=1572316870627626584,duration=1008689565,event=ensure_path_components[0Ktravis_time:start:2ddc3978[0Ktravis_time:end:2ddc3978:start=1572316870632513328,finish=1572316870635332640,duration=2819312,event=redefine_curl[0Ktravis_time:start:2fcf25b6[0Ktravis_time:end:2fcf25b6:start=1572316870639013570,finish=1572316870693397112,duration=54383542,event=nonblock_pipe[0Ktravis_time:start:19ddfdec[0Ktravis_time:end:19ddfdec:start=1572316870697919233,finish=1572316873745682865,duration=3047763632,event=apt_get_update[0Ktravis_time:start:05e0cb00[0Ktravis_time:end:05e0cb00:start=1572316873750984539,finish=1572316873753725970,duration=2741431,event=deprecate_xcode_64[0Ktravis_time:start:02b5c784[0Ktravis_time:end:02b5c784:start=1572316873757445943,finish=1572316878601343337,duration=4843897394,event=update_heroku[0Ktravis_time:start:151b6e34[0Ktravis_time:end:151b6e34:start=1572316878606520873,finish=1572316878609219265,duration=2698392,event=shell_session_update[0Ktravis_time:start:1748835c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3859
travis_fold:end:docker_mtu[0Ktravis_time:end:1748835c:start=1572316878613759033,finish=1572316879814496716,duration=1200737683,event=set_docker_mtu[0Ktravis_time:start:09933796[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:09933796:start=1572316879819268633,finish=1572316879889375343,duration=70106710,event=resolvconf[0Ktravis_time:start:18a0fc86[0Ktravis_time:end:18a0fc86:start=1572316879894676877,finish=1572316880000204578,duration=105527701,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:29f85356[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:29f85356:start=1572316880081560768,finish=1572316880702306697,duration=620745929,event=configure[0Ktravis_time:start:0a6e2fa9[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a6e2fa9:start=1572316880707217602,finish=1572316890565388296,duration=9858170694,event=configure[0Ktravis_time:start:0dd287e4[0Ktravis_fold:start:services[0Ktravis_time:start:12fa024b[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:12fa024b:start=1572316890590683800,finish=1572316890604216020,duration=13532220,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:12fa024b:start=1572316890590683800,finish=1572316893610534745,duration=3019850945,event=services[0Ktravis_time:start:0bd6939c[0Ktravis_time:end:0bd6939c:start=1572316893615367334,finish=1572316893618281586,duration=2914252,event=fix_ps4[0Ktravis_time:start:1ee328a2[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08a6dbb1[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08a6dbb1:start=1572316893628543227,finish=1572316899851851931,duration=6223308704,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:08a6dbb1:start=1572316893628543227,finish=1572316900684706104,duration=7056162877,event=checkout[0Ktravis_time:start:1d3c7300[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1d3c7300:start=1572316900689004337,finish=1572316900697200791,duration=8196454,event=env[0Ktravis_time:start:19d58909[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:19d58909:start=1572316900701922498,finish=1572316900709094485,duration=7171987,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1e43eed0[0K$ python system_testing.py -s of-of
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:edfe062e8b0068c848afcd6ba420e0377dd633d043a2a3c41f75a315b9d7b1b6
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:1e43eed0:start=1572316901051597854,finish=1572317022213120420,duration=121161522566,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:13699caf[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/604222463/log.txt)