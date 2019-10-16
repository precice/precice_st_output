 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598441565) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/478596e1ce45) 
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
travis_time:end:05871da8:start=1571194733096079112,finish=1571194733102242384,duration=6163272,event=show_system_info[0Ktravis_time:start:12d0e715[0Ktravis_time:end:12d0e715:start=1571194733105921396,finish=1571194733129801929,duration=23880533,event=rm_riak_source[0Ktravis_time:start:0020e180[0Ktravis_time:end:0020e180:start=1571194733133612765,finish=1571194733140132457,duration=6519692,event=fix_rwky_redis[0Ktravis_time:start:0849421e[0Ktravis_time:end:0849421e:start=1571194733144427265,finish=1571194736303295924,duration=3158868659,event=wait_for_network[0Ktravis_time:start:08983f74[0Ktravis_time:end:08983f74:start=1571194736306910159,finish=1571194737241210865,duration=934300706,event=update_apt_keys[0Ktravis_time:start:09c93228[0Ktravis_time:end:09c93228:start=1571194737244859708,finish=1571194738357965500,duration=1113105792,event=fix_hhvm_source[0Ktravis_time:start:194cb676[0Ktravis_time:end:194cb676:start=1571194738361708990,finish=1571194738373058696,duration=11349706,event=update_mongo_arch[0Ktravis_time:start:2278e930[0Ktravis_time:end:2278e930:start=1571194738376811789,finish=1571194738433091438,duration=56279649,event=fix_sudo_enabled_trusty[0Ktravis_time:start:23fa6e8c[0Ktravis_time:end:23fa6e8c:start=1571194738437559105,finish=1571194738440784337,duration=3225232,event=update_glibc[0Ktravis_time:start:0480cb61[0Ktravis_time:end:0480cb61:start=1571194738445008901,finish=1571194738457635824,duration=12626923,event=clean_up_path[0Ktravis_time:start:0c7ded6a[0Ktravis_time:end:0c7ded6a:start=1571194738462503616,finish=1571194738479616501,duration=17112885,event=fix_resolv_conf[0Ktravis_time:start:01c806c9[0Ktravis_time:end:01c806c9:start=1571194738486788727,finish=1571194738504038054,duration=17249327,event=fix_etc_hosts[0Ktravis_time:start:2f57b404[0Ktravis_time:end:2f57b404:start=1571194738511642935,finish=1571194738536116185,duration=24473250,event=fix_mvn_settings_xml[0Ktravis_time:start:2088aef6[0Ktravis_time:end:2088aef6:start=1571194738551774702,finish=1571194738656403218,duration=104628516,event=no_ipv6_localhost[0Ktravis_time:start:078e35a8[0Ktravis_time:end:078e35a8:start=1571194738670704869,finish=1571194738678523426,duration=7818557,event=fix_etc_mavenrc[0Ktravis_time:start:086075d3[0Ktravis_time:end:086075d3:start=1571194738695163326,finish=1571194738717193951,duration=22030625,event=fix_wwdr_certificate[0Ktravis_time:start:002ec28c[0Ktravis_time:end:002ec28c:start=1571194738725194369,finish=1571194738764109404,duration=38915035,event=put_localhost_first[0Ktravis_time:start:17675b44[0Ktravis_time:end:17675b44:start=1571194738769706545,finish=1571194738774668532,duration=4961987,event=home_paths[0Ktravis_time:start:1e527bcd[0Ktravis_time:end:1e527bcd:start=1571194738781793178,finish=1571194738800576078,duration=18782900,event=disable_initramfs[0Ktravis_time:start:0f7ee0ee[0Ktravis_time:end:0f7ee0ee:start=1571194738807764400,finish=1571194739107332628,duration=299568228,event=disable_ssh_roaming[0Ktravis_time:start:0ea4b29a[0Ktravis_time:end:0ea4b29a:start=1571194739112202724,finish=1571194739115305008,duration=3102284,event=debug_tools[0Ktravis_time:start:0ee3a904[0Ktravis_time:end:0ee3a904:start=1571194739119988093,finish=1571194739124018329,duration=4030236,event=uninstall_oclint[0Ktravis_time:start:0afbefd0[0Ktravis_time:end:0afbefd0:start=1571194739128768605,finish=1571194739132813369,duration=4044764,event=rvm_use[0Ktravis_time:start:3498a7fa[0Ktravis_time:end:3498a7fa:start=1571194739139353166,finish=1571194739148914943,duration=9561777,event=rm_etc_boto_cfg[0Ktravis_time:start:00825280[0Ktravis_time:end:00825280:start=1571194739154777089,finish=1571194739159736017,duration=4958928,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0dda0446[0Ktravis_time:end:0dda0446:start=1571194739165836859,finish=1571194739231677454,duration=65840595,event=enable_i386[0Ktravis_time:start:15d9f408[0Ktravis_time:end:15d9f408:start=1571194739236736960,finish=1571194739242101639,duration=5364679,event=update_rubygems[0Ktravis_time:start:12f81f33[0Ktravis_time:end:12f81f33:start=1571194739248543041,finish=1571194740367503877,duration=1118960836,event=ensure_path_components[0Ktravis_time:start:0423f947[0Ktravis_time:end:0423f947:start=1571194740373703639,finish=1571194740377563426,duration=3859787,event=redefine_curl[0Ktravis_time:start:0100d040[0Ktravis_time:end:0100d040:start=1571194740382793557,finish=1571194740448919939,duration=66126382,event=nonblock_pipe[0Ktravis_time:start:05d4a92c[0Ktravis_time:end:05d4a92c:start=1571194740454941115,finish=1571194740501421619,duration=46480504,event=apt_get_update[0Ktravis_time:start:2a9928c0[0Ktravis_time:end:2a9928c0:start=1571194740505971918,finish=1571194740509245627,duration=3273709,event=deprecate_xcode_64[0Ktravis_time:start:1d6a25a8[0Ktravis_time:end:1d6a25a8:start=1571194740513410236,finish=1571194745593250025,duration=5079839789,event=update_heroku[0Ktravis_time:start:05fa75f0[0Ktravis_time:end:05fa75f0:start=1571194745597858251,finish=1571194745601345255,duration=3487004,event=shell_session_update[0Ktravis_time:start:007045c1[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3908
travis_fold:end:docker_mtu[0Ktravis_time:end:007045c1:start=1571194745605881650,finish=1571194746814772389,duration=1208890739,event=set_docker_mtu[0Ktravis_time:start:10c43b1d[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:10c43b1d:start=1571194746820188907,finish=1571194746893748299,duration=73559392,event=resolvconf[0Ktravis_time:start:028c6b24[0Ktravis_time:end:028c6b24:start=1571194746898271451,finish=1571194747013401097,duration=115129646,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0a19d59f[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0a19d59f:start=1571194747101944486,finish=1571194747596581028,duration=494636542,event=configure[0Ktravis_time:start:19a8bc7e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:19a8bc7e:start=1571194747601965238,finish=1571194761274114073,duration=13672148835,event=configure[0Ktravis_time:start:0503b9fc[0Ktravis_fold:start:services[0Ktravis_time:start:0804f641[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0804f641:start=1571194761302415877,finish=1571194761319064964,duration=16649087,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0804f641:start=1571194761302415877,finish=1571194764325590897,duration=3023175020,event=services[0Ktravis_time:start:1c9d5248[0Ktravis_time:end:1c9d5248:start=1571194764330042716,finish=1571194764333262159,duration=3219443,event=fix_ps4[0Ktravis_time:start:144a3680[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0e421f00[0K$ git clone --depth=50 --branch=EderK-allow_job_failure https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0e421f00:start=1571194764342389650,finish=1571194770850855685,duration=6508466035,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 478596e1ce45f10d128c4f914460a3fe747c5fdd
travis_fold:end:git.checkout[0K
travis_time:end:0e421f00:start=1571194764342389650,finish=1571194771513860546,duration=7171470896,event=checkout[0Ktravis_time:start:1d4cb17e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1d4cb17e:start=1571194771519258190,finish=1571194771531263330,duration=12005140,event=env[0Ktravis_time:start:27a48f71[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:27a48f71:start=1571194771538385584,finish=1571194771545216390,duration=6830806,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:068c70a7[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:8c28a96b26585c04af5ec1ea6f96daea73118195658df2bf9cf7cb3dd45ac81a
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/598441592/log.txt)