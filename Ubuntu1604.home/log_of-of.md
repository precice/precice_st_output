## Status: Passing 
Build: [1231](https://travis-ci.org/precice/systemtests/builds/618755773) 

Job: [1231.14](https://travis-ci.org/precice/systemtests/jobs/618755787) 

Triggered by: [push](https://github.com/precice/systemtests/compare/3b2ed1c3a41a...be71f6e722f0) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:02a1ecdc:start=1575065654230531832,finish=1575065654236566625,duration=6034793,event=show_system_info[0Ktravis_time:start:0ae941da[0Ktravis_time:end:0ae941da:start=1575065654240154688,finish=1575065654267074156,duration=26919468,event=rm_riak_source[0Ktravis_time:start:04485938[0Ktravis_time:end:04485938:start=1575065654271838621,finish=1575065654282101603,duration=10262982,event=fix_rwky_redis[0Ktravis_time:start:02c9f340[0Ktravis_time:end:02c9f340:start=1575065654285981342,finish=1575065654658815574,duration=372834232,event=wait_for_network[0Ktravis_time:start:0126bfcf[0Ktravis_time:end:0126bfcf:start=1575065654664326176,finish=1575065655573797479,duration=909471303,event=update_apt_keys[0Ktravis_time:start:0b14a47e[0Ktravis_time:end:0b14a47e:start=1575065655580090784,finish=1575065656613179357,duration=1033088573,event=fix_hhvm_source[0Ktravis_time:start:102356c1[0Ktravis_time:end:102356c1:start=1575065656618051979,finish=1575065656628217259,duration=10165280,event=update_mongo_arch[0Ktravis_time:start:000645ea[0Ktravis_time:end:000645ea:start=1575065656632544242,finish=1575065656676115647,duration=43571405,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0bd71104[0Ktravis_time:end:0bd71104:start=1575065656680306696,finish=1575065656683221763,duration=2915067,event=update_glibc[0Ktravis_time:start:000349b0[0Ktravis_time:end:000349b0:start=1575065656687069268,finish=1575065656699760698,duration=12691430,event=clean_up_path[0Ktravis_time:start:283a2e58[0Ktravis_time:end:283a2e58:start=1575065656703664499,finish=1575065656715288095,duration=11623596,event=fix_resolv_conf[0Ktravis_time:start:11d1372c[0Ktravis_time:end:11d1372c:start=1575065656719264386,finish=1575065656730220369,duration=10955983,event=fix_etc_hosts[0Ktravis_time:start:2d0ff4e8[0Ktravis_time:end:2d0ff4e8:start=1575065656736783598,finish=1575065656746108633,duration=9325035,event=fix_mvn_settings_xml[0Ktravis_time:start:1bf845b5[0Ktravis_time:end:1bf845b5:start=1575065656751062716,finish=1575065656763660554,duration=12597838,event=no_ipv6_localhost[0Ktravis_time:start:0b855b64[0Ktravis_time:end:0b855b64:start=1575065656768662692,finish=1575065656771853588,duration=3190896,event=fix_etc_mavenrc[0Ktravis_time:start:09d8cf7c[0Ktravis_time:end:09d8cf7c:start=1575065656776772006,finish=1575065656782208964,duration=5436958,event=fix_wwdr_certificate[0Ktravis_time:start:0b2f1d41[0Ktravis_time:end:0b2f1d41:start=1575065656787782780,finish=1575065656814221681,duration=26438901,event=put_localhost_first[0Ktravis_time:start:2032aefe[0Ktravis_time:end:2032aefe:start=1575065656819802810,finish=1575065656824893811,duration=5091001,event=home_paths[0Ktravis_time:start:1811a318[0Ktravis_time:end:1811a318:start=1575065656829714855,finish=1575065656842739779,duration=13024924,event=disable_initramfs[0Ktravis_time:start:1094072c[0Ktravis_time:end:1094072c:start=1575065656846938469,finish=1575065657141802285,duration=294863816,event=disable_ssh_roaming[0Ktravis_time:start:00245e20[0Ktravis_time:end:00245e20:start=1575065657146708038,finish=1575065657149617117,duration=2909079,event=debug_tools[0Ktravis_time:start:009faaa0[0Ktravis_time:end:009faaa0:start=1575065657154572724,finish=1575065657158566821,duration=3994097,event=uninstall_oclint[0Ktravis_time:start:208cf153[0Ktravis_time:end:208cf153:start=1575065657163120681,finish=1575065657167051401,duration=3930720,event=rvm_use[0Ktravis_time:start:19409a4c[0Ktravis_time:end:19409a4c:start=1575065657171894567,finish=1575065657182704691,duration=10810124,event=rm_etc_boto_cfg[0Ktravis_time:start:00f1a9d3[0Ktravis_time:end:00f1a9d3:start=1575065657187881748,finish=1575065657191007916,duration=3126168,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2080fa3a[0Ktravis_time:end:2080fa3a:start=1575065657196222844,finish=1575065657255547387,duration=59324543,event=enable_i386[0Ktravis_time:start:073a022c[0Ktravis_time:end:073a022c:start=1575065657260238924,finish=1575065657265631763,duration=5392839,event=update_rubygems[0Ktravis_time:start:1a3fdbae[0Ktravis_time:end:1a3fdbae:start=1575065657269686036,finish=1575065658299410123,duration=1029724087,event=ensure_path_components[0Ktravis_time:start:12e3ca1c[0Ktravis_time:end:12e3ca1c:start=1575065658304719757,finish=1575065658307794384,duration=3074627,event=redefine_curl[0Ktravis_time:start:07118ef4[0Ktravis_time:end:07118ef4:start=1575065658311839411,finish=1575065658366455228,duration=54615817,event=nonblock_pipe[0Ktravis_time:start:08190300[0Ktravis_time:end:08190300:start=1575065658371351025,finish=1575065661523591408,duration=3152240383,event=apt_get_update[0Ktravis_time:start:014029f6[0Ktravis_time:end:014029f6:start=1575065661528948568,finish=1575065661531882306,duration=2933738,event=deprecate_xcode_64[0Ktravis_time:start:0e256fe7[0Ktravis_time:end:0e256fe7:start=1575065661536418621,finish=1575065665927120251,duration=4390701630,event=update_heroku[0Ktravis_time:start:06cd96fe[0Ktravis_time:end:06cd96fe:start=1575065665932319308,finish=1575065665935378330,duration=3059022,event=shell_session_update[0Ktravis_time:start:0237c1ad[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3957
travis_fold:end:docker_mtu[0Ktravis_time:end:0237c1ad:start=1575065665941556434,finish=1575065667141025413,duration=1199468979,event=set_docker_mtu[0Ktravis_time:start:21906348[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:21906348:start=1575065667147278898,finish=1575065667222610256,duration=75331358,event=resolvconf[0Ktravis_time:start:1d623c12[0Ktravis_time:end:1d623c12:start=1575065667227233585,finish=1575065667331849211,duration=104615626,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02cbc85c[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02cbc85c:start=1575065667418194215,finish=1575065668007661041,duration=589466826,event=configure[0Ktravis_time:start:1c840b54[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1c840b54:start=1575065668012829035,finish=1575065678773250681,duration=10760421646,event=configure[0Ktravis_time:start:135ca2a2[0Ktravis_fold:start:services[0Ktravis_time:start:1023eb6c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1023eb6c:start=1575065678802099805,finish=1575065678818453740,duration=16353935,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1023eb6c:start=1575065678802099805,finish=1575065681825067063,duration=3022967258,event=services[0Ktravis_time:start:34f16490[0Ktravis_time:end:34f16490:start=1575065681830162683,finish=1575065681833204017,duration=3041334,event=fix_ps4[0Ktravis_time:start:1330df88[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0e114f04[0K$ git clone --depth=50 --branch=compatibility_PR_576_on_[secure]_core https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0e114f04:start=1575065681843180104,finish=1575065688089296594,duration=6246116490,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf be71f6e722f05592add416fad2e64434441bdcf3
travis_fold:end:git.checkout[0K
travis_time:end:0e114f04:start=1575065681843180104,finish=1575065688168225869,duration=6325045765,event=checkout[0Ktravis_time:start:0aa42d24[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0aa42d24:start=1575065688174486643,finish=1575065688188044493,duration=13557850,event=env[0Ktravis_time:start:01e52d19[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01e52d19:start=1575065688194097775,finish=1575065688205796445,duration=11698670,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:02a0ce9a[0K$ python system_testing.py -s of-of
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
Digest: sha256:b7e68fef65a78dc590afe65c6c8d8a08f2a5ec422fbdb27a0b74270776bff2fd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:02a0ce9a:start=1575065688575078806,finish=1575065809479426794,duration=120904347988,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0580b03c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618755787/log.txt)