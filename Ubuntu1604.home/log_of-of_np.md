## Status: Passing 
Build: [1058](https://travis-ci.org/precice/systemtests/builds/607962841) 

Job: [1058.24](https://travis-ci.org/precice/systemtests/jobs/607962867) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

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
travis_time:end:0656ff1c:start=1573008933418714330,finish=1573008933425169348,duration=6455018,event=show_system_info[0Ktravis_time:start:1de937a3[0Ktravis_time:end:1de937a3:start=1573008933428748002,finish=1573008933456132471,duration=27384469,event=rm_riak_source[0Ktravis_time:start:3813dc0a[0Ktravis_time:end:3813dc0a:start=1573008933460298013,finish=1573008933467255191,duration=6957178,event=fix_rwky_redis[0Ktravis_time:start:06ebbc9c[0Ktravis_time:end:06ebbc9c:start=1573008933470942871,finish=1573008933847830634,duration=376887763,event=wait_for_network[0Ktravis_time:start:128618f4[0Ktravis_time:end:128618f4:start=1573008933852811087,finish=1573008934782369455,duration=929558368,event=update_apt_keys[0Ktravis_time:start:01ad1d39[0Ktravis_time:end:01ad1d39:start=1573008934787989942,finish=1573008935860080933,duration=1072090991,event=fix_hhvm_source[0Ktravis_time:start:078beaf2[0Ktravis_time:end:078beaf2:start=1573008935864886385,finish=1573008935875289967,duration=10403582,event=update_mongo_arch[0Ktravis_time:start:105c0c0f[0Ktravis_time:end:105c0c0f:start=1573008935881169607,finish=1573008935924050451,duration=42880844,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2d846918[0Ktravis_time:end:2d846918:start=1573008935930164156,finish=1573008935933261628,duration=3097472,event=update_glibc[0Ktravis_time:start:1b259a58[0Ktravis_time:end:1b259a58:start=1573008935938021617,finish=1573008935949432412,duration=11410795,event=clean_up_path[0Ktravis_time:start:1d9a8400[0Ktravis_time:end:1d9a8400:start=1573008935955346295,finish=1573008935965714828,duration=10368533,event=fix_resolv_conf[0Ktravis_time:start:201274b5[0Ktravis_time:end:201274b5:start=1573008935970890080,finish=1573008935980999395,duration=10109315,event=fix_etc_hosts[0Ktravis_time:start:01677c92[0Ktravis_time:end:01677c92:start=1573008935989173172,finish=1573008935999330534,duration=10157362,event=fix_mvn_settings_xml[0Ktravis_time:start:1672e042[0Ktravis_time:end:1672e042:start=1573008936004312586,finish=1573008936015964901,duration=11652315,event=no_ipv6_localhost[0Ktravis_time:start:00112920[0Ktravis_time:end:00112920:start=1573008936020759396,finish=1573008936023913234,duration=3153838,event=fix_etc_mavenrc[0Ktravis_time:start:068c8bc8[0Ktravis_time:end:068c8bc8:start=1573008936028035734,finish=1573008936031943720,duration=3907986,event=fix_wwdr_certificate[0Ktravis_time:start:0e855247[0Ktravis_time:end:0e855247:start=1573008936036029533,finish=1573008936065936248,duration=29906715,event=put_localhost_first[0Ktravis_time:start:1e92e46a[0Ktravis_time:end:1e92e46a:start=1573008936070961550,finish=1573008936076540223,duration=5578673,event=home_paths[0Ktravis_time:start:1f383944[0Ktravis_time:end:1f383944:start=1573008936080832825,finish=1573008936096172080,duration=15339255,event=disable_initramfs[0Ktravis_time:start:1282b24f[0Ktravis_time:end:1282b24f:start=1573008936101429615,finish=1573008936496166697,duration=394737082,event=disable_ssh_roaming[0Ktravis_time:start:0963a230[0Ktravis_time:end:0963a230:start=1573008936500577806,finish=1573008936503485092,duration=2907286,event=debug_tools[0Ktravis_time:start:03946576[0Ktravis_time:end:03946576:start=1573008936508211983,finish=1573008936512975988,duration=4764005,event=uninstall_oclint[0Ktravis_time:start:25303509[0Ktravis_time:end:25303509:start=1573008936517608942,finish=1573008936522303813,duration=4694871,event=rvm_use[0Ktravis_time:start:13c56cba[0Ktravis_time:end:13c56cba:start=1573008936528865128,finish=1573008936537522483,duration=8657355,event=rm_etc_boto_cfg[0Ktravis_time:start:01f75080[0Ktravis_time:end:01f75080:start=1573008936542537933,finish=1573008936545662027,duration=3124094,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0651f0ae[0Ktravis_time:end:0651f0ae:start=1573008936549822079,finish=1573008936610312418,duration=60490339,event=enable_i386[0Ktravis_time:start:061d5200[0Ktravis_time:end:061d5200:start=1573008936615425804,finish=1573008936620049976,duration=4624172,event=update_rubygems[0Ktravis_time:start:1e5f6c01[0Ktravis_time:end:1e5f6c01:start=1573008936625049508,finish=1573008937671823675,duration=1046774167,event=ensure_path_components[0Ktravis_time:start:00542cac[0Ktravis_time:end:00542cac:start=1573008937677234461,finish=1573008937680201615,duration=2967154,event=redefine_curl[0Ktravis_time:start:0aa39a6c[0Ktravis_time:end:0aa39a6c:start=1573008937684170493,finish=1573008937744047271,duration=59876778,event=nonblock_pipe[0Ktravis_time:start:063d4ebc[0Ktravis_time:end:063d4ebc:start=1573008937749761187,finish=1573008940805312199,duration=3055551012,event=apt_get_update[0Ktravis_time:start:0f1c8c38[0Ktravis_time:end:0f1c8c38:start=1573008940810721543,finish=1573008940814204059,duration=3482516,event=deprecate_xcode_64[0Ktravis_time:start:0cbe2be7[0Ktravis_time:end:0cbe2be7:start=1573008940819361739,finish=1573008945668037719,duration=4848675980,event=update_heroku[0Ktravis_time:start:04412ac3[0Ktravis_time:end:04412ac3:start=1573008945672386197,finish=1573008945675262126,duration=2875929,event=shell_session_update[0Ktravis_time:start:36c306b4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3857
travis_fold:end:docker_mtu[0Ktravis_time:end:36c306b4:start=1573008945679109045,finish=1573008946871664785,duration=1192555740,event=set_docker_mtu[0Ktravis_time:start:044a2b47[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:044a2b47:start=1573008946879028053,finish=1573008946948150136,duration=69122083,event=resolvconf[0Ktravis_time:start:0944cedd[0Ktravis_time:end:0944cedd:start=1573008946953485328,finish=1573008947065353001,duration=111867673,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0334534a[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0334534a:start=1573008947153222813,finish=1573008947553572208,duration=400349395,event=configure[0Ktravis_time:start:002fda32[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:002fda32:start=1573008947558889573,finish=1573008958383802011,duration=10824912438,event=configure[0Ktravis_time:start:1981f2e0[0Ktravis_fold:start:services[0Ktravis_time:start:01109890[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:01109890:start=1573008958410199375,finish=1573008958426690473,duration=16491098,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:01109890:start=1573008958410199375,finish=1573008961434778860,duration=3024579485,event=services[0Ktravis_time:start:20424aa8[0Ktravis_time:end:20424aa8:start=1573008961441672187,finish=1573008961445744764,duration=4072577,event=fix_ps4[0Ktravis_time:start:02717ca0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0dbe89a0[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0dbe89a0:start=1573008961458887709,finish=1573008968194406462,duration=6735518753,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0dbe89a0:start=1573008961458887709,finish=1573008968370077965,duration=6911190256,event=checkout[0Ktravis_time:start:101b5250[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:101b5250:start=1573008968375644123,finish=1573008968388889158,duration=13245035,event=env[0Ktravis_time:start:01ae07bd[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01ae07bd:start=1573008968394072636,finish=1573008968402795994,duration=8723358,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:053b7f8c[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:1f11411670b7e8e03ddcfb87356be9d1396f52a11746c00e8586258ce97e581e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/607962867/log.txt)