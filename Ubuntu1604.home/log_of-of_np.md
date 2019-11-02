## Status: Passing 
Build: [1054](https://travis-ci.org/precice/systemtests/builds/606282132) 

Job: [1054.24](https://travis-ci.org/precice/systemtests/jobs/606282162) 

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
travis_time:end:12e40d98:start=1572662820416772298,finish=1572662820422901211,duration=6128913,event=show_system_info[0Ktravis_time:start:02f1d2d8[0Ktravis_time:end:02f1d2d8:start=1572662820425914806,finish=1572662820453070181,duration=27155375,event=rm_riak_source[0Ktravis_time:start:12232d07[0Ktravis_time:end:12232d07:start=1572662820456615465,finish=1572662820463992521,duration=7377056,event=fix_rwky_redis[0Ktravis_time:start:0d6a9898[0Ktravis_time:end:0d6a9898:start=1572662820467643419,finish=1572662820913128745,duration=445485326,event=wait_for_network[0Ktravis_time:start:0d0359fc[0Ktravis_time:end:0d0359fc:start=1572662820918800677,finish=1572662821939752631,duration=1020951954,event=update_apt_keys[0Ktravis_time:start:0332a04e[0Ktravis_time:end:0332a04e:start=1572662821945098418,finish=1572662823011709534,duration=1066611116,event=fix_hhvm_source[0Ktravis_time:start:0e4661a4[0Ktravis_time:end:0e4661a4:start=1572662823016403399,finish=1572662823027560670,duration=11157271,event=update_mongo_arch[0Ktravis_time:start:0535e0b0[0Ktravis_time:end:0535e0b0:start=1572662823033409126,finish=1572662823076916834,duration=43507708,event=fix_sudo_enabled_trusty[0Ktravis_time:start:06c592ee[0Ktravis_time:end:06c592ee:start=1572662823083014787,finish=1572662823086507608,duration=3492821,event=update_glibc[0Ktravis_time:start:0c474d00[0Ktravis_time:end:0c474d00:start=1572662823092362833,finish=1572662823104429724,duration=12066891,event=clean_up_path[0Ktravis_time:start:0211b514[0Ktravis_time:end:0211b514:start=1572662823109468420,finish=1572662823119451028,duration=9982608,event=fix_resolv_conf[0Ktravis_time:start:0e3198b8[0Ktravis_time:end:0e3198b8:start=1572662823123928158,finish=1572662823133916209,duration=9988051,event=fix_etc_hosts[0Ktravis_time:start:1517a197[0Ktravis_time:end:1517a197:start=1572662823141150932,finish=1572662823150891407,duration=9740475,event=fix_mvn_settings_xml[0Ktravis_time:start:01f8cc57[0Ktravis_time:end:01f8cc57:start=1572662823157259173,finish=1572662823168909706,duration=11650533,event=no_ipv6_localhost[0Ktravis_time:start:24d4e93a[0Ktravis_time:end:24d4e93a:start=1572662823175325657,finish=1572662823178792500,duration=3466843,event=fix_etc_mavenrc[0Ktravis_time:start:0e8ac092[0Ktravis_time:end:0e8ac092:start=1572662823185556457,finish=1572662823189859641,duration=4303184,event=fix_wwdr_certificate[0Ktravis_time:start:0c00fb8e[0Ktravis_time:end:0c00fb8e:start=1572662823194988701,finish=1572662823222872909,duration=27884208,event=put_localhost_first[0Ktravis_time:start:29789138[0Ktravis_time:end:29789138:start=1572662823229139557,finish=1572662823233421357,duration=4281800,event=home_paths[0Ktravis_time:start:14b02517[0Ktravis_time:end:14b02517:start=1572662823238434524,finish=1572662823252475954,duration=14041430,event=disable_initramfs[0Ktravis_time:start:00b5ac80[0Ktravis_time:end:00b5ac80:start=1572662823258324954,finish=1572662823590206391,duration=331881437,event=disable_ssh_roaming[0Ktravis_time:start:004736f4[0Ktravis_time:end:004736f4:start=1572662823594790053,finish=1572662823598346873,duration=3556820,event=debug_tools[0Ktravis_time:start:0e3fe5a5[0Ktravis_time:end:0e3fe5a5:start=1572662823602931307,finish=1572662823607527904,duration=4596597,event=uninstall_oclint[0Ktravis_time:start:233f1ffe[0Ktravis_time:end:233f1ffe:start=1572662823615077006,finish=1572662823619131822,duration=4054816,event=rvm_use[0Ktravis_time:start:20c76120[0Ktravis_time:end:20c76120:start=1572662823623932606,finish=1572662823633073324,duration=9140718,event=rm_etc_boto_cfg[0Ktravis_time:start:0f801ee8[0Ktravis_time:end:0f801ee8:start=1572662823638959918,finish=1572662823642324484,duration=3364566,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1321e993[0Ktravis_time:end:1321e993:start=1572662823647815081,finish=1572662823704965196,duration=57150115,event=enable_i386[0Ktravis_time:start:034537e6[0Ktravis_time:end:034537e6:start=1572662823710662114,finish=1572662823716101603,duration=5439489,event=update_rubygems[0Ktravis_time:start:0112dd81[0Ktravis_time:end:0112dd81:start=1572662823722573255,finish=1572662824765630794,duration=1043057539,event=ensure_path_components[0Ktravis_time:start:02ae1acd[0Ktravis_time:end:02ae1acd:start=1572662824770088991,finish=1572662824773850537,duration=3761546,event=redefine_curl[0Ktravis_time:start:05371af0[0Ktravis_time:end:05371af0:start=1572662824778729637,finish=1572662824834368882,duration=55639245,event=nonblock_pipe[0Ktravis_time:start:0c3bedd8[0Ktravis_time:end:0c3bedd8:start=1572662824839810910,finish=1572662827887512458,duration=3047701548,event=apt_get_update[0Ktravis_time:start:098b5583[0Ktravis_time:end:098b5583:start=1572662827892976868,finish=1572662827896215094,duration=3238226,event=deprecate_xcode_64[0Ktravis_time:start:1cb6cdd4[0Ktravis_time:end:1cb6cdd4:start=1572662827900333517,finish=1572662832767468184,duration=4867134667,event=update_heroku[0Ktravis_time:start:0411a684[0Ktravis_time:end:0411a684:start=1572662832771468105,finish=1572662832774416328,duration=2948223,event=shell_session_update[0Ktravis_time:start:118ce878[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3857
travis_fold:end:docker_mtu[0Ktravis_time:end:118ce878:start=1572662832778352954,finish=1572662833970763621,duration=1192410667,event=set_docker_mtu[0Ktravis_time:start:1bf45680[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1bf45680:start=1572662833974853878,finish=1572662834043561983,duration=68708105,event=resolvconf[0Ktravis_time:start:36d40202[0Ktravis_time:end:36d40202:start=1572662834047549524,finish=1572662834162598244,duration=115048720,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1099cbc7[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1099cbc7:start=1572662834250692815,finish=1572662834663826227,duration=413133412,event=configure[0Ktravis_time:start:096cf490[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:096cf490:start=1572662834669799071,finish=1572662845223914330,duration=10554115259,event=configure[0Ktravis_time:start:158bf29b[0Ktravis_fold:start:services[0Ktravis_time:start:08cae538[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08cae538:start=1572662845249261432,finish=1572662845263693914,duration=14432482,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08cae538:start=1572662845249261432,finish=1572662848270517381,duration=3021255949,event=services[0Ktravis_time:start:3069c615[0Ktravis_time:end:3069c615:start=1572662848276158486,finish=1572662848278864270,duration=2705784,event=fix_ps4[0Ktravis_time:start:1c15be18[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0b8a1702[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0b8a1702:start=1572662848287690541,finish=1572662854556360893,duration=6268670352,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0b8a1702:start=1572662848287690541,finish=1572662855025214738,duration=6737524197,event=checkout[0Ktravis_time:start:016c3150[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:016c3150:start=1572662855030091972,finish=1572662855041238872,duration=11146900,event=env[0Ktravis_time:start:1e127500[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1e127500:start=1572662855046852097,finish=1572662855055536028,duration=8683931,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:22428a96[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:7b35f009c5169ca242753a754e0675197b77bde0b0ee3330c95449a33e668f39
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/606282162/log.txt)