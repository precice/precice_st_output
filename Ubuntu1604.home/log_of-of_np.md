## Status: Passing 
Build: [1056](https://travis-ci.org/precice/systemtests/builds/606935491) 

Job: [1056.24](https://travis-ci.org/precice/systemtests/jobs/606935518) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:2c0fd0b4:start=1572835599217636594,finish=1572835599223729086,duration=6092492,event=show_system_info[0Ktravis_time:start:2a7dd7f8[0Ktravis_time:end:2a7dd7f8:start=1572835599226864269,finish=1572835599252663244,duration=25798975,event=rm_riak_source[0Ktravis_time:start:04f853e1[0Ktravis_time:end:04f853e1:start=1572835599256362322,finish=1572835599262101518,duration=5739196,event=fix_rwky_redis[0Ktravis_time:start:012ae86c[0Ktravis_time:end:012ae86c:start=1572835599266337612,finish=1572835599684800684,duration=418463072,event=wait_for_network[0Ktravis_time:start:0c6c5962[0Ktravis_time:end:0c6c5962:start=1572835599690053191,finish=1572835601532213859,duration=1842160668,event=update_apt_keys[0Ktravis_time:start:1525f32c[0Ktravis_time:end:1525f32c:start=1572835601536984041,finish=1572835602624596761,duration=1087612720,event=fix_hhvm_source[0Ktravis_time:start:09ea104c[0Ktravis_time:end:09ea104c:start=1572835602629465359,finish=1572835602640636434,duration=11171075,event=update_mongo_arch[0Ktravis_time:start:012e7e16[0Ktravis_time:end:012e7e16:start=1572835602645223053,finish=1572835602688787975,duration=43564922,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0bc5537c[0Ktravis_time:end:0bc5537c:start=1572835602692816793,finish=1572835602695543045,duration=2726252,event=update_glibc[0Ktravis_time:start:0bc61c7a[0Ktravis_time:end:0bc61c7a:start=1572835602699294469,finish=1572835602710051090,duration=10756621,event=clean_up_path[0Ktravis_time:start:10813a46[0Ktravis_time:end:10813a46:start=1572835602713570328,finish=1572835602723922696,duration=10352368,event=fix_resolv_conf[0Ktravis_time:start:00d602a1[0Ktravis_time:end:00d602a1:start=1572835602728364666,finish=1572835602739609348,duration=11244682,event=fix_etc_hosts[0Ktravis_time:start:0133cc44[0Ktravis_time:end:0133cc44:start=1572835602744212947,finish=1572835602754677385,duration=10464438,event=fix_mvn_settings_xml[0Ktravis_time:start:126c97b3[0Ktravis_time:end:126c97b3:start=1572835602760954749,finish=1572835602772070741,duration=11115992,event=no_ipv6_localhost[0Ktravis_time:start:1038ef4c[0Ktravis_time:end:1038ef4c:start=1572835602776868184,finish=1572835602780986429,duration=4118245,event=fix_etc_mavenrc[0Ktravis_time:start:0c48aace[0Ktravis_time:end:0c48aace:start=1572835602785064742,finish=1572835602788789206,duration=3724464,event=fix_wwdr_certificate[0Ktravis_time:start:05cc89ed[0Ktravis_time:end:05cc89ed:start=1572835602794555451,finish=1572835602821663689,duration=27108238,event=put_localhost_first[0Ktravis_time:start:26b12710[0Ktravis_time:end:26b12710:start=1572835602827366472,finish=1572835602830996932,duration=3630460,event=home_paths[0Ktravis_time:start:10f655d4[0Ktravis_time:end:10f655d4:start=1572835602835841771,finish=1572835602850397565,duration=14555794,event=disable_initramfs[0Ktravis_time:start:0044bc7e[0Ktravis_time:end:0044bc7e:start=1572835602855706711,finish=1572835603197856584,duration=342149873,event=disable_ssh_roaming[0Ktravis_time:start:165ce7d2[0Ktravis_time:end:165ce7d2:start=1572835603202977580,finish=1572835603206101671,duration=3124091,event=debug_tools[0Ktravis_time:start:1749d2f4[0Ktravis_time:end:1749d2f4:start=1572835603212388912,finish=1572835603216517858,duration=4128946,event=uninstall_oclint[0Ktravis_time:start:1ed9e52e[0Ktravis_time:end:1ed9e52e:start=1572835603221538766,finish=1572835603226105941,duration=4567175,event=rvm_use[0Ktravis_time:start:31884d3c[0Ktravis_time:end:31884d3c:start=1572835603233238806,finish=1572835603242038017,duration=8799211,event=rm_etc_boto_cfg[0Ktravis_time:start:001febb8[0Ktravis_time:end:001febb8:start=1572835603247379681,finish=1572835603251010895,duration=3631214,event=rm_oraclejdk8_symlink[0Ktravis_time:start:02a64650[0Ktravis_time:end:02a64650:start=1572835603257450967,finish=1572835603313107255,duration=55656288,event=enable_i386[0Ktravis_time:start:0122b870[0Ktravis_time:end:0122b870:start=1572835603318563726,finish=1572835603323490772,duration=4927046,event=update_rubygems[0Ktravis_time:start:0b63fdc9[0Ktravis_time:end:0b63fdc9:start=1572835603328283954,finish=1572835604336322789,duration=1008038835,event=ensure_path_components[0Ktravis_time:start:14dd3e78[0Ktravis_time:end:14dd3e78:start=1572835604341673117,finish=1572835604344793376,duration=3120259,event=redefine_curl[0Ktravis_time:start:018872e0[0Ktravis_time:end:018872e0:start=1572835604348830175,finish=1572835604404570424,duration=55740249,event=nonblock_pipe[0Ktravis_time:start:0371aeb4[0Ktravis_time:end:0371aeb4:start=1572835604409852567,finish=1572835607457288991,duration=3047436424,event=apt_get_update[0Ktravis_time:start:1f0c73ac[0Ktravis_time:end:1f0c73ac:start=1572835607462323811,finish=1572835607465345734,duration=3021923,event=deprecate_xcode_64[0Ktravis_time:start:371da398[0Ktravis_time:end:371da398:start=1572835607469406512,finish=1572835612728976465,duration=5259569953,event=update_heroku[0Ktravis_time:start:034afd0c[0Ktravis_time:end:034afd0c:start=1572835612733810712,finish=1572835612736674975,duration=2864263,event=shell_session_update[0Ktravis_time:start:02b89222[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3955
travis_fold:end:docker_mtu[0Ktravis_time:end:02b89222:start=1572835612741261235,finish=1572835613944563528,duration=1203302293,event=set_docker_mtu[0Ktravis_time:start:10955abc[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:10955abc:start=1572835613948598047,finish=1572835614018663349,duration=70065302,event=resolvconf[0Ktravis_time:start:060b9d5d[0Ktravis_time:end:060b9d5d:start=1572835614023603876,finish=1572835614118641914,duration=95038038,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1fe88270[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1fe88270:start=1572835614202507943,finish=1572835614685950589,duration=483442646,event=configure[0Ktravis_time:start:2d625cce[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2d625cce:start=1572835614691875489,finish=1572835624225207388,duration=9533331899,event=configure[0Ktravis_time:start:0b02297e[0Ktravis_fold:start:services[0Ktravis_time:start:216c7cde[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:216c7cde:start=1572835624251584382,finish=1572835624266516134,duration=14931752,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:216c7cde:start=1572835624251584382,finish=1572835627271747385,duration=3020163003,event=services[0Ktravis_time:start:10b45ac8[0Ktravis_time:end:10b45ac8:start=1572835627276746274,finish=1572835627279516946,duration=2770672,event=fix_ps4[0Ktravis_time:start:190c2282[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1011d750[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1011d750:start=1572835627288589973,finish=1572835633658029828,duration=6369439855,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:1011d750:start=1572835627288589973,finish=1572835634233326829,duration=6944736856,event=checkout[0Ktravis_time:start:0d9f68ae[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0d9f68ae:start=1572835634237886627,finish=1572835634251228112,duration=13341485,event=env[0Ktravis_time:start:06c0b745[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:06c0b745:start=1572835634259028035,finish=1572835634265339772,duration=6311737,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:23838d98[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:61bc80da6f66c50f0becba80f8502ed08e6c12ff77e5f6f4d4e1419680c98209
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:23838d98:start=1572835634605881719,finish=1572835756270224796,duration=121664343077,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:030a9158[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/606935518/log.txt)