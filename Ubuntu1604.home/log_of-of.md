## Status: Passing 
Build: [1056](https://travis-ci.org/precice/systemtests/builds/606935491) 

Job: [1056.18](https://travis-ci.org/precice/systemtests/jobs/606935512) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:17b1deb2:start=1572835344534147567,finish=1572835344541223171,duration=7075604,event=show_system_info[0Ktravis_time:start:02449d70[0Ktravis_time:end:02449d70:start=1572835344544598819,finish=1572835344569815753,duration=25216934,event=rm_riak_source[0Ktravis_time:start:01f5db0a[0Ktravis_time:end:01f5db0a:start=1572835344574031584,finish=1572835344582354692,duration=8323108,event=fix_rwky_redis[0Ktravis_time:start:0d93b040[0Ktravis_time:end:0d93b040:start=1572835344585792901,finish=1572835345089230228,duration=503437327,event=wait_for_network[0Ktravis_time:start:18bf766d[0Ktravis_time:end:18bf766d:start=1572835345094708627,finish=1572835346232628819,duration=1137920192,event=update_apt_keys[0Ktravis_time:start:14fd563d[0Ktravis_time:end:14fd563d:start=1572835346237638196,finish=1572835347328338181,duration=1090699985,event=fix_hhvm_source[0Ktravis_time:start:0981d456[0Ktravis_time:end:0981d456:start=1572835347333577930,finish=1572835347344348721,duration=10770791,event=update_mongo_arch[0Ktravis_time:start:04df368b[0Ktravis_time:end:04df368b:start=1572835347350965603,finish=1572835347393891214,duration=42925611,event=fix_sudo_enabled_trusty[0Ktravis_time:start:06e99e08[0Ktravis_time:end:06e99e08:start=1572835347399296913,finish=1572835347402960094,duration=3663181,event=update_glibc[0Ktravis_time:start:0eb4849c[0Ktravis_time:end:0eb4849c:start=1572835347407954521,finish=1572835347420060181,duration=12105660,event=clean_up_path[0Ktravis_time:start:117cc2a6[0Ktravis_time:end:117cc2a6:start=1572835347425038739,finish=1572835347435183319,duration=10144580,event=fix_resolv_conf[0Ktravis_time:start:11746f32[0Ktravis_time:end:11746f32:start=1572835347439756973,finish=1572835347449820148,duration=10063175,event=fix_etc_hosts[0Ktravis_time:start:05f80a01[0Ktravis_time:end:05f80a01:start=1572835347455690453,finish=1572835347465940236,duration=10249783,event=fix_mvn_settings_xml[0Ktravis_time:start:0ad3da90[0Ktravis_time:end:0ad3da90:start=1572835347471024378,finish=1572835347481494596,duration=10470218,event=no_ipv6_localhost[0Ktravis_time:start:0f8cd21a[0Ktravis_time:end:0f8cd21a:start=1572835347486260955,finish=1572835347488986423,duration=2725468,event=fix_etc_mavenrc[0Ktravis_time:start:164a319b[0Ktravis_time:end:164a319b:start=1572835347493727533,finish=1572835347497478341,duration=3750808,event=fix_wwdr_certificate[0Ktravis_time:start:1da19e3c[0Ktravis_time:end:1da19e3c:start=1572835347504189881,finish=1572835347532296444,duration=28106563,event=put_localhost_first[0Ktravis_time:start:018345ae[0Ktravis_time:end:018345ae:start=1572835347537392377,finish=1572835347543217641,duration=5825264,event=home_paths[0Ktravis_time:start:0d79c7c3[0Ktravis_time:end:0d79c7c3:start=1572835347548660731,finish=1572835347562545550,duration=13884819,event=disable_initramfs[0Ktravis_time:start:0cb3b332[0Ktravis_time:end:0cb3b332:start=1572835347567541308,finish=1572835347856578135,duration=289036827,event=disable_ssh_roaming[0Ktravis_time:start:00709e04[0Ktravis_time:end:00709e04:start=1572835347861644336,finish=1572835347864858198,duration=3213862,event=debug_tools[0Ktravis_time:start:2910b3b8[0Ktravis_time:end:2910b3b8:start=1572835347868895025,finish=1572835347872509969,duration=3614944,event=uninstall_oclint[0Ktravis_time:start:003aecce[0Ktravis_time:end:003aecce:start=1572835347876459353,finish=1572835347879952508,duration=3493155,event=rvm_use[0Ktravis_time:start:0265352a[0Ktravis_time:end:0265352a:start=1572835347886228867,finish=1572835347895389925,duration=9161058,event=rm_etc_boto_cfg[0Ktravis_time:start:342541e8[0Ktravis_time:end:342541e8:start=1572835347902340127,finish=1572835347906903283,duration=4563156,event=rm_oraclejdk8_symlink[0Ktravis_time:start:01b1dd3f[0Ktravis_time:end:01b1dd3f:start=1572835347911629342,finish=1572835347969945657,duration=58316315,event=enable_i386[0Ktravis_time:start:04b2f510[0Ktravis_time:end:04b2f510:start=1572835347975444490,finish=1572835347980878511,duration=5434021,event=update_rubygems[0Ktravis_time:start:18bf854e[0Ktravis_time:end:18bf854e:start=1572835347985296880,finish=1572835349035752354,duration=1050455474,event=ensure_path_components[0Ktravis_time:start:0891985d[0Ktravis_time:end:0891985d:start=1572835349042437869,finish=1572835349046331081,duration=3893212,event=redefine_curl[0Ktravis_time:start:0447dfde[0Ktravis_time:end:0447dfde:start=1572835349051288367,finish=1572835349110181302,duration=58892935,event=nonblock_pipe[0Ktravis_time:start:0e4c8278[0Ktravis_time:end:0e4c8278:start=1572835349115209442,finish=1572835352218041216,duration=3102831774,event=apt_get_update[0Ktravis_time:start:22d7f9ca[0Ktravis_time:end:22d7f9ca:start=1572835352222311211,finish=1572835352225367340,duration=3056129,event=deprecate_xcode_64[0Ktravis_time:start:1f73e3f8[0Ktravis_time:end:1f73e3f8:start=1572835352229567322,finish=1572835357129849178,duration=4900281856,event=update_heroku[0Ktravis_time:start:0ae277b8[0Ktravis_time:end:0ae277b8:start=1572835357135476151,finish=1572835357138500103,duration=3023952,event=shell_session_update[0Ktravis_time:start:049d4990[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3941
travis_fold:end:docker_mtu[0Ktravis_time:end:049d4990:start=1572835357142546832,finish=1572835358340140224,duration=1197593392,event=set_docker_mtu[0Ktravis_time:start:0410d150[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0410d150:start=1572835358344321541,finish=1572835358413513754,duration=69192213,event=resolvconf[0Ktravis_time:start:18538fce[0Ktravis_time:end:18538fce:start=1572835358418884217,finish=1572835358528950375,duration=110066158,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1010c5ec[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1010c5ec:start=1572835358615089899,finish=1572835359288660337,duration=673570438,event=configure[0Ktravis_time:start:0f2baa2c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0f2baa2c:start=1572835359301171554,finish=1572835370392796217,duration=11091624663,event=configure[0Ktravis_time:start:111757ec[0Ktravis_fold:start:services[0Ktravis_time:start:06160116[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06160116:start=1572835370419762932,finish=1572835370435276963,duration=15514031,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06160116:start=1572835370419762932,finish=1572835373440421066,duration=3020658134,event=services[0Ktravis_time:start:157ce075[0Ktravis_time:end:157ce075:start=1572835373444949442,finish=1572835373448059260,duration=3109818,event=fix_ps4[0Ktravis_time:start:108be7c2[0K
travis_fold:start:git.checkout[0Ktravis_time:start:04eedacb[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:04eedacb:start=1572835373457272297,finish=1572835379852756354,duration=6395484057,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:04eedacb:start=1572835373457272297,finish=1572835380680957538,duration=7223685241,event=checkout[0Ktravis_time:start:01027bf6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01027bf6:start=1572835380686504306,finish=1572835380700667329,duration=14163023,event=env[0Ktravis_time:start:1f801512[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1f801512:start=1572835380706125317,finish=1572835380713892121,duration=7766804,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:10b946ef[0K$ python system_testing.py -s of-of
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
Digest: sha256:61bc80da6f66c50f0becba80f8502ed08e6c12ff77e5f6f4d4e1419680c98209
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:10b946ef:start=1572835381095387431,finish=1572835502325505590,duration=121230118159,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:07e27cc1[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/606935512/log.txt)