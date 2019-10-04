 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/593438448) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/46a3f0d5dc83...a992016cf5d2) 
## Last 100 lines of the job log at the moment of push...
```
   hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:09d7af4d:start=1570181691773328366,finish=1570181691779715667,duration=6387301,event=show_system_info[0Ktravis_time:start:0f6878f6[0Ktravis_time:end:0f6878f6:start=1570181691782873275,finish=1570181691812334906,duration=29461631,event=rm_riak_source[0Ktravis_time:start:021e6d30[0Ktravis_time:end:021e6d30:start=1570181691815831706,finish=1570181691828564080,duration=12732374,event=fix_rwky_redis[0Ktravis_time:start:0aa63e34[0Ktravis_time:end:0aa63e34:start=1570181691832716110,finish=1570181692230734259,duration=398018149,event=wait_for_network[0Ktravis_time:start:28ea6634[0Ktravis_time:end:28ea6634:start=1570181692235399292,finish=1570181693164639772,duration=929240480,event=update_apt_keys[0Ktravis_time:start:14b5d083[0Ktravis_time:end:14b5d083:start=1570181693169591747,finish=1570181694312983257,duration=1143391510,event=fix_hhvm_source[0Ktravis_time:start:03fdff34[0Ktravis_time:end:03fdff34:start=1570181694317103071,finish=1570181694329342678,duration=12239607,event=update_mongo_arch[0Ktravis_time:start:0251b551[0Ktravis_time:end:0251b551:start=1570181694333484448,finish=1570181694379806208,duration=46321760,event=fix_sudo_enabled_trusty[0Ktravis_time:start:11861010[0Ktravis_time:end:11861010:start=1570181694386058285,finish=1570181694389091670,duration=3033385,event=update_glibc[0Ktravis_time:start:02b6be88[0Ktravis_time:end:02b6be88:start=1570181694395456277,finish=1570181694404872829,duration=9416552,event=clean_up_path[0Ktravis_time:start:02ac2618[0Ktravis_time:end:02ac2618:start=1570181694410432073,finish=1570181694420017178,duration=9585105,event=fix_resolv_conf[0Ktravis_time:start:1b678c94[0Ktravis_time:end:1b678c94:start=1570181694424634368,finish=1570181694434763905,duration=10129537,event=fix_etc_hosts[0Ktravis_time:start:0274d06d[0Ktravis_time:end:0274d06d:start=1570181694439942080,finish=1570181694450407300,duration=10465220,event=fix_mvn_settings_xml[0Ktravis_time:start:11631618[0Ktravis_time:end:11631618:start=1570181694455470877,finish=1570181694466768318,duration=11297441,event=no_ipv6_localhost[0Ktravis_time:start:0f36eeec[0Ktravis_time:end:0f36eeec:start=1570181694471445614,finish=1570181694474550965,duration=3105351,event=fix_etc_mavenrc[0Ktravis_time:start:0e7b001f[0Ktravis_time:end:0e7b001f:start=1570181694479333790,finish=1570181694483287631,duration=3953841,event=fix_wwdr_certificate[0Ktravis_time:start:0fde874a[0Ktravis_time:end:0fde874a:start=1570181694488556351,finish=1570181694515122678,duration=26566327,event=put_localhost_first[0Ktravis_time:start:0064f320[0Ktravis_time:end:0064f320:start=1570181694519735546,finish=1570181694523983987,duration=4248441,event=home_paths[0Ktravis_time:start:04429222[0Ktravis_time:end:04429222:start=1570181694528903198,finish=1570181694542456814,duration=13553616,event=disable_initramfs[0Ktravis_time:start:04844c58[0Ktravis_time:end:04844c58:start=1570181694548204613,finish=1570181694843173160,duration=294968547,event=disable_ssh_roaming[0Ktravis_time:start:00907c30[0Ktravis_time:end:00907c30:start=1570181694848933415,finish=1570181694851962388,duration=3028973,event=debug_tools[0Ktravis_time:start:0b26caef[0Ktravis_time:end:0b26caef:start=1570181694856097758,finish=1570181694860419283,duration=4321525,event=uninstall_oclint[0Ktravis_time:start:07b61ff0[0Ktravis_time:end:07b61ff0:start=1570181694864622710,finish=1570181694868822682,duration=4199972,event=rvm_use[0Ktravis_time:start:1e07f518[0Ktravis_time:end:1e07f518:start=1570181694883265731,finish=1570181694892364856,duration=9099125,event=rm_etc_boto_cfg[0Ktravis_time:start:03aeabe8[0Ktravis_time:end:03aeabe8:start=1570181694896955611,finish=1570181694899881916,duration=2926305,event=rm_oraclejdk8_symlink[0Ktravis_time:start:13688608[0Ktravis_time:end:13688608:start=1570181694905992334,finish=1570181694964066112,duration=58073778,event=enable_i386[0Ktravis_time:start:0e03a7e2[0Ktravis_time:end:0e03a7e2:start=1570181694968974180,finish=1570181694973745301,duration=4771121,event=update_rubygems[0Ktravis_time:start:001728fc[0Ktravis_time:end:001728fc:start=1570181694978497888,finish=1570181696052369806,duration=1073871918,event=ensure_path_components[0Ktravis_time:start:13d18364[0Ktravis_time:end:13d18364:start=1570181696057987091,finish=1570181696061617504,duration=3630413,event=redefine_curl[0Ktravis_time:start:245511f0[0Ktravis_time:end:245511f0:start=1570181696067641097,finish=1570181696130032544,duration=62391447,event=nonblock_pipe[0Ktravis_time:start:261f489e[0Ktravis_time:end:261f489e:start=1570181696135474368,finish=1570181696207657495,duration=72183127,event=apt_get_update[0Ktravis_time:start:09d73bd6[0Ktravis_time:end:09d73bd6:start=1570181696213612981,finish=1570181696217295126,duration=3682145,event=deprecate_xcode_64[0Ktravis_time:start:03e33d90[0Ktravis_time:end:03e33d90:start=1570181696223564215,finish=1570181701044841090,duration=4821276875,event=update_heroku[0Ktravis_time:start:0f0216e0[0Ktravis_time:end:0f0216e0:start=1570181701050697401,finish=1570181701054614961,duration=3917560,event=shell_session_update[0Ktravis_time:start:1546c28e[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3962
travis_fold:end:docker_mtu[0Ktravis_time:end:1546c28e:start=1570181701060005827,finish=1570181702267108462,duration=1207102635,event=set_docker_mtu[0Ktravis_time:start:31ee398f[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:31ee398f:start=1570181702272985567,finish=1570181702347286703,duration=74301136,event=resolvconf[0Ktravis_time:start:160d59cb[0Ktravis_time:end:160d59cb:start=1570181702353252456,finish=1570181702456520089,duration=103267633,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:205c62f8[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:205c62f8:start=1570181702540922918,finish=1570181703002706660,duration=461783742,event=configure[0Ktravis_time:start:0379b055[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0379b055:start=1570181703007944090,finish=1570181714779734030,duration=11771789940,event=configure[0Ktravis_time:start:197250c8[0Ktravis_fold:start:services[0Ktravis_time:start:055bb1c0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:055bb1c0:start=1570181714807089075,finish=1570181714822861468,duration=15772393,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:055bb1c0:start=1570181714807089075,finish=1570181717829917198,duration=3022828123,event=services[0Ktravis_time:start:08b9f01b[0Ktravis_time:end:08b9f01b:start=1570181717834745575,finish=1570181717837832625,duration=3087050,event=fix_ps4[0Ktravis_time:start:1a7dd6d0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00c91ae4[0K$ git clone --depth=50 --branch=EderK-add_elastictube1d_test https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00c91ae4:start=1570181717847491849,finish=1570181724404864642,duration=6557372793,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf a992016cf5d2d015f4c6ae47963e7f6b19c13d0d
travis_fold:end:git.checkout[0K
travis_time:end:00c91ae4:start=1570181717847491849,finish=1570181724759013459,duration=6911521610,event=checkout[0Ktravis_time:start:227a4498[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:227a4498:start=1570181724764393465,finish=1570181724776190133,duration=11796668,event=env[0Ktravis_time:start:0d0c3e33[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0d0c3e33:start=1570181724781633714,finish=1570181724790344771,duration=8711057,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0d067d6d[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:aa92deb706c423affecf0ab585f41e6d8fd965503ebcd5fae2671f58ae9ea6a1
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/593438476/log.txt)