## Status: Passing 
Build: [1122](https://travis-ci.org/precice/systemtests/builds/613794885) 

Job: [1122.24](https://travis-ci.org/precice/systemtests/jobs/613794909) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/e39228c1c8cf63923ead04a7e05071545b49caa0...ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:11df10fc:start=1574132093077355475,finish=1574132093083800097,duration=6444622,event=show_system_info[0Ktravis_time:start:0427b3a8[0Ktravis_time:end:0427b3a8:start=1574132093087269999,finish=1574132093111442820,duration=24172821,event=rm_riak_source[0Ktravis_time:start:0fa22c98[0Ktravis_time:end:0fa22c98:start=1574132093114830646,finish=1574132093122108754,duration=7278108,event=fix_rwky_redis[0Ktravis_time:start:09ee894f[0Ktravis_time:end:09ee894f:start=1574132093125641892,finish=1574132093525413927,duration=399772035,event=wait_for_network[0Ktravis_time:start:04c9fe9c[0Ktravis_time:end:04c9fe9c:start=1574132093530217419,finish=1574132094847489755,duration=1317272336,event=update_apt_keys[0Ktravis_time:start:0969ade2[0Ktravis_time:end:0969ade2:start=1574132094853853696,finish=1574132095970555252,duration=1116701556,event=fix_hhvm_source[0Ktravis_time:start:0e882b09[0Ktravis_time:end:0e882b09:start=1574132095977221142,finish=1574132095990418281,duration=13197139,event=update_mongo_arch[0Ktravis_time:start:06f128c6[0Ktravis_time:end:06f128c6:start=1574132095997247061,finish=1574132096044089814,duration=46842753,event=fix_sudo_enabled_trusty[0Ktravis_time:start:003692ca[0Ktravis_time:end:003692ca:start=1574132096050984982,finish=1574132096054442037,duration=3457055,event=update_glibc[0Ktravis_time:start:02a5a55d[0Ktravis_time:end:02a5a55d:start=1574132096062790568,finish=1574132096073728519,duration=10937951,event=clean_up_path[0Ktravis_time:start:0d3deaa8[0Ktravis_time:end:0d3deaa8:start=1574132096080276267,finish=1574132096091848356,duration=11572089,event=fix_resolv_conf[0Ktravis_time:start:22ff3058[0Ktravis_time:end:22ff3058:start=1574132096096582121,finish=1574132096109605996,duration=13023875,event=fix_etc_hosts[0Ktravis_time:start:176284b1[0Ktravis_time:end:176284b1:start=1574132096114733650,finish=1574132096127362693,duration=12629043,event=fix_mvn_settings_xml[0Ktravis_time:start:0076d23e[0Ktravis_time:end:0076d23e:start=1574132096134708387,finish=1574132096149361861,duration=14653474,event=no_ipv6_localhost[0Ktravis_time:start:00101198[0Ktravis_time:end:00101198:start=1574132096156862628,finish=1574132096160603399,duration=3740771,event=fix_etc_mavenrc[0Ktravis_time:start:06de6cc6[0Ktravis_time:end:06de6cc6:start=1574132096165440914,finish=1574132096172988989,duration=7548075,event=fix_wwdr_certificate[0Ktravis_time:start:011ad926[0Ktravis_time:end:011ad926:start=1574132096179120075,finish=1574132096212632745,duration=33512670,event=put_localhost_first[0Ktravis_time:start:212e2129[0Ktravis_time:end:212e2129:start=1574132096218869715,finish=1574132096223483731,duration=4614016,event=home_paths[0Ktravis_time:start:1400a1c6[0Ktravis_time:end:1400a1c6:start=1574132096229288684,finish=1574132096245857869,duration=16569185,event=disable_initramfs[0Ktravis_time:start:10c5349e[0Ktravis_time:end:10c5349e:start=1574132096251835648,finish=1574132096608142392,duration=356306744,event=disable_ssh_roaming[0Ktravis_time:start:0f708c30[0Ktravis_time:end:0f708c30:start=1574132096614201614,finish=1574132096618309270,duration=4107656,event=debug_tools[0Ktravis_time:start:14340f28[0Ktravis_time:end:14340f28:start=1574132096625229701,finish=1574132096630466385,duration=5236684,event=uninstall_oclint[0Ktravis_time:start:17ff2ec2[0Ktravis_time:end:17ff2ec2:start=1574132096636031608,finish=1574132096641334940,duration=5303332,event=rvm_use[0Ktravis_time:start:25fe3aa0[0Ktravis_time:end:25fe3aa0:start=1574132096646936493,finish=1574132096658427816,duration=11491323,event=rm_etc_boto_cfg[0Ktravis_time:start:1e15d7dc[0Ktravis_time:end:1e15d7dc:start=1574132096665018415,finish=1574132096668605196,duration=3586781,event=rm_oraclejdk8_symlink[0Ktravis_time:start:05609902[0Ktravis_time:end:05609902:start=1574132096674072583,finish=1574132096739881756,duration=65809173,event=enable_i386[0Ktravis_time:start:04175f3c[0Ktravis_time:end:04175f3c:start=1574132096745378681,finish=1574132096752233626,duration=6854945,event=update_rubygems[0Ktravis_time:start:0f7f7e66[0Ktravis_time:end:0f7f7e66:start=1574132096757182303,finish=1574132098020388814,duration=1263206511,event=ensure_path_components[0Ktravis_time:start:01047ec2[0Ktravis_time:end:01047ec2:start=1574132098027122118,finish=1574132098030650746,duration=3528628,event=redefine_curl[0Ktravis_time:start:1b2e1ea3[0Ktravis_time:end:1b2e1ea3:start=1574132098036307982,finish=1574132098103348152,duration=67040170,event=nonblock_pipe[0Ktravis_time:start:09a19c12[0Ktravis_time:end:09a19c12:start=1574132098109023184,finish=1574132101166642060,duration=3057618876,event=apt_get_update[0Ktravis_time:start:108de360[0Ktravis_time:end:108de360:start=1574132101171200710,finish=1574132101174316640,duration=3115930,event=deprecate_xcode_64[0Ktravis_time:start:0ee85840[0Ktravis_time:end:0ee85840:start=1574132101178324025,finish=1574132106747697405,duration=5569373380,event=update_heroku[0Ktravis_time:start:0796648b[0Ktravis_time:end:0796648b:start=1574132106752912108,finish=1574132106756223065,duration=3310957,event=shell_session_update[0Ktravis_time:start:0b7930f1[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3872
travis_fold:end:docker_mtu[0Ktravis_time:end:0b7930f1:start=1574132106761998031,finish=1574132107963910605,duration=1201912574,event=set_docker_mtu[0Ktravis_time:start:3630bd86[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:3630bd86:start=1574132107970163748,finish=1574132108068313431,duration=98149683,event=resolvconf[0Ktravis_time:start:0cfdcb3e[0Ktravis_time:end:0cfdcb3e:start=1574132108074359167,finish=1574132108217644864,duration=143285697,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0e648578[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0e648578:start=1574132108312429751,finish=1574132108589441064,duration=277011313,event=configure[0Ktravis_time:start:06feb1f8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:06feb1f8:start=1574132108594871542,finish=1574132121952044450,duration=13357172908,event=configure[0Ktravis_time:start:0da7f555[0Ktravis_fold:start:services[0Ktravis_time:start:19402194[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:19402194:start=1574132121980835153,finish=1574132121996652497,duration=15817344,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:19402194:start=1574132121980835153,finish=1574132125004322046,duration=3023486893,event=services[0Ktravis_time:start:1f0c6438[0Ktravis_time:end:1f0c6438:start=1574132125009742706,finish=1574132125013540189,duration=3797483,event=fix_ps4[0Ktravis_time:start:24cfb748[0K
travis_fold:start:git.checkout[0Ktravis_time:start:140c4463[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:140c4463:start=1574132125027078983,finish=1574132131392413938,duration=6365334955,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf ec4ef9d4aedd0087dfb3a8ed98fdf7a1267c7751
travis_fold:end:git.checkout[0K
travis_time:end:140c4463:start=1574132125027078983,finish=1574132131731153491,duration=6704074508,event=checkout[0Ktravis_time:start:11fefd82[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:11fefd82:start=1574132131735704221,finish=1574132131746770572,duration=11066351,event=env[0Ktravis_time:start:0175ddae[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0175ddae:start=1574132131752005555,finish=1574132131760623175,duration=8617620,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:18bc4b80[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:844e14e1d93b14d3bb4ad6659f7796969c12548b32aeb379689f4a726d61cf48
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:18bc4b80:start=1574132132132305369,finish=1574132253893199640,duration=121760894271,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:3015e732[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/613794909/log.txt)