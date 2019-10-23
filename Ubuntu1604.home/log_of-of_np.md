## Status: Passing 
Build: [1000](https://travis-ci.org/precice/systemtests/builds/601988696) 

Job: [1000.20](https://travis-ci.org/precice/systemtests/jobs/601988716) 

Triggered by: [push](https://github.com/precice/systemtests/compare/500cfbb53a97...73300f5bea0c) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:system_info[0K
travis_time:end:00ce3fbd:start=1571863857822274895,finish=1571863857829702442,duration=7427547,event=show_system_info[0Ktravis_time:start:04d00367[0Ktravis_time:end:04d00367:start=1571863857833038779,finish=1571863857861196058,duration=28157279,event=rm_riak_source[0Ktravis_time:start:158bfe10[0Ktravis_time:end:158bfe10:start=1571863857865301664,finish=1571863857873235669,duration=7934005,event=fix_rwky_redis[0Ktravis_time:start:0e81f9ca[0Ktravis_time:end:0e81f9ca:start=1571863857877431579,finish=1571863858309355303,duration=431923724,event=wait_for_network[0Ktravis_time:start:01630c17[0Ktravis_time:end:01630c17:start=1571863858314188735,finish=1571863859942750607,duration=1628561872,event=update_apt_keys[0Ktravis_time:start:025be68e[0Ktravis_time:end:025be68e:start=1571863859948107650,finish=1571863861070403488,duration=1122295838,event=fix_hhvm_source[0Ktravis_time:start:124156c4[0Ktravis_time:end:124156c4:start=1571863861076175056,finish=1571863861087295566,duration=11120510,event=update_mongo_arch[0Ktravis_time:start:1ad52640[0Ktravis_time:end:1ad52640:start=1571863861093100575,finish=1571863861137636328,duration=44535753,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2ed6a168[0Ktravis_time:end:2ed6a168:start=1571863861142550222,finish=1571863861146099366,duration=3549144,event=update_glibc[0Ktravis_time:start:0bdc469e[0Ktravis_time:end:0bdc469e:start=1571863861151450796,finish=1571863861161291532,duration=9840736,event=clean_up_path[0Ktravis_time:start:0fa0e120[0Ktravis_time:end:0fa0e120:start=1571863861168554169,finish=1571863861177666407,duration=9112238,event=fix_resolv_conf[0Ktravis_time:start:29cd6926[0Ktravis_time:end:29cd6926:start=1571863861182554780,finish=1571863861193618099,duration=11063319,event=fix_etc_hosts[0Ktravis_time:start:0da20a13[0Ktravis_time:end:0da20a13:start=1571863861198470548,finish=1571863861208308443,duration=9837895,event=fix_mvn_settings_xml[0Ktravis_time:start:3378292a[0Ktravis_time:end:3378292a:start=1571863861215095542,finish=1571863861225542190,duration=10446648,event=no_ipv6_localhost[0Ktravis_time:start:126529f6[0Ktravis_time:end:126529f6:start=1571863861230346180,finish=1571863861234402191,duration=4056011,event=fix_etc_mavenrc[0Ktravis_time:start:14ee78f0[0Ktravis_time:end:14ee78f0:start=1571863861238704441,finish=1571863861242337366,duration=3632925,event=fix_wwdr_certificate[0Ktravis_time:start:06f475fa[0Ktravis_time:end:06f475fa:start=1571863861246451529,finish=1571863861272729997,duration=26278468,event=put_localhost_first[0Ktravis_time:start:06207df2[0Ktravis_time:end:06207df2:start=1571863861278601673,finish=1571863861282842447,duration=4240774,event=home_paths[0Ktravis_time:start:0b71d888[0Ktravis_time:end:0b71d888:start=1571863861287422439,finish=1571863861303586601,duration=16164162,event=disable_initramfs[0Ktravis_time:start:07f63158[0Ktravis_time:end:07f63158:start=1571863861308639560,finish=1571863861676601086,duration=367961526,event=disable_ssh_roaming[0Ktravis_time:start:0f11e89c[0Ktravis_time:end:0f11e89c:start=1571863861681806184,finish=1571863861684935734,duration=3129550,event=debug_tools[0Ktravis_time:start:0042e99a[0Ktravis_time:end:0042e99a:start=1571863861689748744,finish=1571863861694570173,duration=4821429,event=uninstall_oclint[0Ktravis_time:start:2532c5a0[0Ktravis_time:end:2532c5a0:start=1571863861700535907,finish=1571863861704512015,duration=3976108,event=rvm_use[0Ktravis_time:start:00a2aa94[0Ktravis_time:end:00a2aa94:start=1571863861709581807,finish=1571863861719252926,duration=9671119,event=rm_etc_boto_cfg[0Ktravis_time:start:0a6309dc[0Ktravis_time:end:0a6309dc:start=1571863861723718763,finish=1571863861727057163,duration=3338400,event=rm_oraclejdk8_symlink[0Ktravis_time:start:174959a0[0Ktravis_time:end:174959a0:start=1571863861732108574,finish=1571863861789466841,duration=57358267,event=enable_i386[0Ktravis_time:start:0e0019c4[0Ktravis_time:end:0e0019c4:start=1571863861794186766,finish=1571863861799250696,duration=5063930,event=update_rubygems[0Ktravis_time:start:03c3e418[0Ktravis_time:end:03c3e418:start=1571863861804302443,finish=1571863862862911502,duration=1058609059,event=ensure_path_components[0Ktravis_time:start:0392d5c4[0Ktravis_time:end:0392d5c4:start=1571863862869465587,finish=1571863862873019444,duration=3553857,event=redefine_curl[0Ktravis_time:start:142cf6fa[0Ktravis_time:end:142cf6fa:start=1571863862878233076,finish=1571863862937903605,duration=59670529,event=nonblock_pipe[0Ktravis_time:start:311b30ab[0Ktravis_time:end:311b30ab:start=1571863862943917538,finish=1571863865990782392,duration=3046864854,event=apt_get_update[0Ktravis_time:start:0675f174[0Ktravis_time:end:0675f174:start=1571863865996213064,finish=1571863865999730523,duration=3517459,event=deprecate_xcode_64[0Ktravis_time:start:19fb6f1e[0Ktravis_time:end:19fb6f1e:start=1571863866005613494,finish=1571863871363438465,duration=5357824971,event=update_heroku[0Ktravis_time:start:09263fa0[0Ktravis_time:end:09263fa0:start=1571863871368309779,finish=1571863871371484192,duration=3174413,event=shell_session_update[0Ktravis_time:start:21c8f91a[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3961
travis_fold:end:docker_mtu[0Ktravis_time:end:21c8f91a:start=1571863871376306984,finish=1571863872581031291,duration=1204724307,event=set_docker_mtu[0Ktravis_time:start:0b923150[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0b923150:start=1571863872586418102,finish=1571863872654423872,duration=68005770,event=resolvconf[0Ktravis_time:start:000aeaba[0Ktravis_time:end:000aeaba:start=1571863872659152612,finish=1571863872766899382,duration=107746770,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1927d176[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1927d176:start=1571863872855254763,finish=1571863873699945456,duration=844690693,event=configure[0Ktravis_time:start:0232ceea[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0232ceea:start=1571863873708328003,finish=1571863885457809779,duration=11749481776,event=configure[0Ktravis_time:start:21ba1020[0Ktravis_fold:start:services[0Ktravis_time:start:13a27156[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:13a27156:start=1571863885487903688,finish=1571863885505081854,duration=17178166,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:13a27156:start=1571863885487903688,finish=1571863888511223035,duration=3023319347,event=services[0Ktravis_time:start:175a0580[0Ktravis_time:end:175a0580:start=1571863888515980749,finish=1571863888519196818,duration=3216069,event=fix_ps4[0Ktravis_time:start:03346d8e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0024a59c[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0024a59c:start=1571863888528190858,finish=1571863894745871195,duration=6217680337,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 73300f5bea0ced6562ee2d5aa26d420608795cda
travis_fold:end:git.checkout[0K
travis_time:end:0024a59c:start=1571863888528190858,finish=1571863895399789798,duration=6871598940,event=checkout[0Ktravis_time:start:2482de62[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2482de62:start=1571863895405039977,finish=1571863895416505375,duration=11465398,event=env[0Ktravis_time:start:1220bc66[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1220bc66:start=1571863895421624201,finish=1571863895427821696,duration=6197495,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:13ce904c[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:800ef878bf82edef081068e05b4fbe89b92f4870c31a470ddb56147df1cb0d1d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:13ce904c:start=1571863895782422782,finish=1571864017315698680,duration=121533275898,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:05cefffa[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/601988716/log.txt)