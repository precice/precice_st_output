## Status: Passing 
Build: [1071](https://travis-ci.org/precice/systemtests/builds/610072373) 

Job: [1071.14](https://travis-ci.org/precice/systemtests/jobs/610072388) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ffab6e4cf6eb...2e77de77c876) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:system_info[0K
travis_time:end:05901918:start=1573425348762070922,finish=1573425348768283101,duration=6212179,event=show_system_info[0Ktravis_time:start:0504747e[0Ktravis_time:end:0504747e:start=1573425348771661105,finish=1573425348797192849,duration=25531744,event=rm_riak_source[0Ktravis_time:start:0bd5fa42[0Ktravis_time:end:0bd5fa42:start=1573425348801266319,finish=1573425348810790277,duration=9523958,event=fix_rwky_redis[0Ktravis_time:start:2aef7108[0Ktravis_time:end:2aef7108:start=1573425348814821612,finish=1573425349202516202,duration=387694590,event=wait_for_network[0Ktravis_time:start:06ed497a[0Ktravis_time:end:06ed497a:start=1573425349207407811,finish=1573425350281524588,duration=1074116777,event=update_apt_keys[0Ktravis_time:start:141d1ca0[0Ktravis_time:end:141d1ca0:start=1573425350287006862,finish=1573425351394026549,duration=1107019687,event=fix_hhvm_source[0Ktravis_time:start:081674f7[0Ktravis_time:end:081674f7:start=1573425351400255212,finish=1573425351410990955,duration=10735743,event=update_mongo_arch[0Ktravis_time:start:09d2446f[0Ktravis_time:end:09d2446f:start=1573425351416996656,finish=1573425351461116513,duration=44119857,event=fix_sudo_enabled_trusty[0Ktravis_time:start:043ed597[0Ktravis_time:end:043ed597:start=1573425351465592248,finish=1573425351469209892,duration=3617644,event=update_glibc[0Ktravis_time:start:1986f1f8[0Ktravis_time:end:1986f1f8:start=1573425351472960438,finish=1573425351484196638,duration=11236200,event=clean_up_path[0Ktravis_time:start:0461eacd[0Ktravis_time:end:0461eacd:start=1573425351492343683,finish=1573425351502449952,duration=10106269,event=fix_resolv_conf[0Ktravis_time:start:003381b4[0Ktravis_time:end:003381b4:start=1573425351507539565,finish=1573425351518932941,duration=11393376,event=fix_etc_hosts[0Ktravis_time:start:035f0520[0Ktravis_time:end:035f0520:start=1573425351523272534,finish=1573425351533914798,duration=10642264,event=fix_mvn_settings_xml[0Ktravis_time:start:26a314d0[0Ktravis_time:end:26a314d0:start=1573425351538998302,finish=1573425351552455198,duration=13456896,event=no_ipv6_localhost[0Ktravis_time:start:0b65e4be[0Ktravis_time:end:0b65e4be:start=1573425351557044771,finish=1573425351560778094,duration=3733323,event=fix_etc_mavenrc[0Ktravis_time:start:05f5c9b5[0Ktravis_time:end:05f5c9b5:start=1573425351565511719,finish=1573425351570423682,duration=4911963,event=fix_wwdr_certificate[0Ktravis_time:start:0b12ab20[0Ktravis_time:end:0b12ab20:start=1573425351575374222,finish=1573425351608331244,duration=32957022,event=put_localhost_first[0Ktravis_time:start:233dcc00[0Ktravis_time:end:233dcc00:start=1573425351613998648,finish=1573425351618184395,duration=4185747,event=home_paths[0Ktravis_time:start:0f712267[0Ktravis_time:end:0f712267:start=1573425351622988011,finish=1573425351638485530,duration=15497519,event=disable_initramfs[0Ktravis_time:start:17bb29a2[0Ktravis_time:end:17bb29a2:start=1573425351642791068,finish=1573425352004261172,duration=361470104,event=disable_ssh_roaming[0Ktravis_time:start:086d02f4[0Ktravis_time:end:086d02f4:start=1573425352009555682,finish=1573425352012339924,duration=2784242,event=debug_tools[0Ktravis_time:start:18369c24[0Ktravis_time:end:18369c24:start=1573425352016824251,finish=1573425352020626303,duration=3802052,event=uninstall_oclint[0Ktravis_time:start:0deec0dc[0Ktravis_time:end:0deec0dc:start=1573425352025068838,finish=1573425352028738899,duration=3670061,event=rvm_use[0Ktravis_time:start:287d0c6c[0Ktravis_time:end:287d0c6c:start=1573425352033492373,finish=1573425352043136009,duration=9643636,event=rm_etc_boto_cfg[0Ktravis_time:start:0b93ecdb[0Ktravis_time:end:0b93ecdb:start=1573425352047471749,finish=1573425352053768929,duration=6297180,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1459a33a[0Ktravis_time:end:1459a33a:start=1573425352058580871,finish=1573425352117672169,duration=59091298,event=enable_i386[0Ktravis_time:start:016e467d[0Ktravis_time:end:016e467d:start=1573425352123160492,finish=1573425352128290603,duration=5130111,event=update_rubygems[0Ktravis_time:start:0a1a283b[0Ktravis_time:end:0a1a283b:start=1573425352133581863,finish=1573425353231296622,duration=1097714759,event=ensure_path_components[0Ktravis_time:start:04644494[0Ktravis_time:end:04644494:start=1573425353236725364,finish=1573425353239695896,duration=2970532,event=redefine_curl[0Ktravis_time:start:008ca793[0Ktravis_time:end:008ca793:start=1573425353244934662,finish=1573425353301800677,duration=56866015,event=nonblock_pipe[0Ktravis_time:start:0103d928[0Ktravis_time:end:0103d928:start=1573425353306543994,finish=1573425356356840244,duration=3050296250,event=apt_get_update[0Ktravis_time:start:040222ab[0Ktravis_time:end:040222ab:start=1573425356361740676,finish=1573425356365098562,duration=3357886,event=deprecate_xcode_64[0Ktravis_time:start:0a0d75c2[0Ktravis_time:end:0a0d75c2:start=1573425356369494062,finish=1573425361136733325,duration=4767239263,event=update_heroku[0Ktravis_time:start:0058026e[0Ktravis_time:end:0058026e:start=1573425361142604913,finish=1573425361146195730,duration=3590817,event=shell_session_update[0Ktravis_time:start:09513385[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3893
travis_fold:end:docker_mtu[0Ktravis_time:end:09513385:start=1573425361150976476,finish=1573425362350483538,duration=1199507062,event=set_docker_mtu[0Ktravis_time:start:04b57148[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:04b57148:start=1573425362356131285,finish=1573425362433053431,duration=76922146,event=resolvconf[0Ktravis_time:start:069ffbc7[0Ktravis_time:end:069ffbc7:start=1573425362438675191,finish=1573425362541277849,duration=102602658,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:13ba1d96[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:13ba1d96:start=1573425362634564525,finish=1573425364160887412,duration=1526322887,event=configure[0Ktravis_time:start:045b8e84[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:045b8e84:start=1573425364167729769,finish=1573425375812022108,duration=11644292339,event=configure[0Ktravis_time:start:0d614fec[0Ktravis_fold:start:services[0Ktravis_time:start:0ebd93e2[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0ebd93e2:start=1573425375841808246,finish=1573425375859238446,duration=17430200,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0ebd93e2:start=1573425375841808246,finish=1573425378865816205,duration=3024007959,event=services[0Ktravis_time:start:0b2f5340[0Ktravis_time:end:0b2f5340:start=1573425378871194612,finish=1573425378874317726,duration=3123114,event=fix_ps4[0Ktravis_time:start:16315550[0K
travis_fold:start:git.checkout[0Ktravis_time:start:11e4f9a3[0K$ git clone --depth=50 --branch=EderK-mpich_deploy https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:11e4f9a3:start=1573425378885650055,finish=1573425385502502397,duration=6616852342,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2e77de77c876e38e0322a21c82436af686fbdc3b
travis_fold:end:git.checkout[0K
travis_time:end:11e4f9a3:start=1573425378885650055,finish=1573425385895614543,duration=7009964488,event=checkout[0Ktravis_time:start:0a7e449a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0a7e449a:start=1573425385902179826,finish=1573425385919703714,duration=17523888,event=env[0Ktravis_time:start:13dfcb48[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:13dfcb48:start=1573425385925801368,finish=1573425385932809495,duration=7008127,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:010bd66e[0K$ python system_testing.py -s of-of
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
Digest: sha256:98e7b7fde8bd6b618c7ffe6b7ed9cd847d62e94c024d4c0ecdbd1eb70a3db786
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:010bd66e:start=1573425386300330370,finish=1573425508340756494,duration=122040426124,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:03a04313[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl

```
[
Full job log](https://api.travis-ci.org/v3/job/610072388/log.txt)