 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/590479609) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/0cb7c0ec452f...92a2d96de651) 
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
travis_time:end:0bbb1e43:start=1569604091103243558,finish=1569604091109634463,duration=6390905,event=show_system_info[0Ktravis_time:start:123f45ca[0Ktravis_time:end:123f45ca:start=1569604091112856998,finish=1569604091137138169,duration=24281171,event=rm_riak_source[0Ktravis_time:start:0a619870[0Ktravis_time:end:0a619870:start=1569604091141277562,finish=1569604091148117605,duration=6840043,event=fix_rwky_redis[0Ktravis_time:start:23bdac7c[0Ktravis_time:end:23bdac7c:start=1569604091152209112,finish=1569604091597581393,duration=445372281,event=wait_for_network[0Ktravis_time:start:0c196e49[0Ktravis_time:end:0c196e49:start=1569604091602825657,finish=1569604092702893149,duration=1100067492,event=update_apt_keys[0Ktravis_time:start:1298effe[0Ktravis_time:end:1298effe:start=1569604092707321127,finish=1569604093765847480,duration=1058526353,event=fix_hhvm_source[0Ktravis_time:start:2b9fb88e[0Ktravis_time:end:2b9fb88e:start=1569604093770409054,finish=1569604093781883877,duration=11474823,event=update_mongo_arch[0Ktravis_time:start:04301624[0Ktravis_time:end:04301624:start=1569604093787756686,finish=1569604093832645580,duration=44888894,event=fix_sudo_enabled_trusty[0Ktravis_time:start:13cb40ad[0Ktravis_time:end:13cb40ad:start=1569604093836922490,finish=1569604093840141249,duration=3218759,event=update_glibc[0Ktravis_time:start:233e395b[0Ktravis_time:end:233e395b:start=1569604093844354725,finish=1569604093856512344,duration=12157619,event=clean_up_path[0Ktravis_time:start:184f651e[0Ktravis_time:end:184f651e:start=1569604093862119825,finish=1569604093871327435,duration=9207610,event=fix_resolv_conf[0Ktravis_time:start:0533e26c[0Ktravis_time:end:0533e26c:start=1569604093878994253,finish=1569604093889760024,duration=10765771,event=fix_etc_hosts[0Ktravis_time:start:142fa0e8[0Ktravis_time:end:142fa0e8:start=1569604093895525663,finish=1569604093907192477,duration=11666814,event=fix_mvn_settings_xml[0Ktravis_time:start:1df37177[0Ktravis_time:end:1df37177:start=1569604093912362566,finish=1569604093924081711,duration=11719145,event=no_ipv6_localhost[0Ktravis_time:start:0a79bc80[0Ktravis_time:end:0a79bc80:start=1569604093929533264,finish=1569604093932548717,duration=3015453,event=fix_etc_mavenrc[0Ktravis_time:start:090d3cbe[0Ktravis_time:end:090d3cbe:start=1569604093937134466,finish=1569604093941629142,duration=4494676,event=fix_wwdr_certificate[0Ktravis_time:start:08066966[0Ktravis_time:end:08066966:start=1569604093948135458,finish=1569604093975254238,duration=27118780,event=put_localhost_first[0Ktravis_time:start:13999df6[0Ktravis_time:end:13999df6:start=1569604093980577038,finish=1569604093984698541,duration=4121503,event=home_paths[0Ktravis_time:start:18b4ef98[0Ktravis_time:end:18b4ef98:start=1569604093990039954,finish=1569604094003780173,duration=13740219,event=disable_initramfs[0Ktravis_time:start:090ce6a0[0Ktravis_time:end:090ce6a0:start=1569604094010137295,finish=1569604094297109556,duration=286972261,event=disable_ssh_roaming[0Ktravis_time:start:02658a0e[0Ktravis_time:end:02658a0e:start=1569604094302596801,finish=1569604094308059107,duration=5462306,event=debug_tools[0Ktravis_time:start:05c0d854[0Ktravis_time:end:05c0d854:start=1569604094313737426,finish=1569604094318522439,duration=4785013,event=uninstall_oclint[0Ktravis_time:start:0c032c8e[0Ktravis_time:end:0c032c8e:start=1569604094324282563,finish=1569604094330852457,duration=6569894,event=rvm_use[0Ktravis_time:start:13c5fccc[0Ktravis_time:end:13c5fccc:start=1569604094336477911,finish=1569604094346815991,duration=10338080,event=rm_etc_boto_cfg[0Ktravis_time:start:2f59421d[0Ktravis_time:end:2f59421d:start=1569604094351958348,finish=1569604094355950263,duration=3991915,event=rm_oraclejdk8_symlink[0Ktravis_time:start:05e65776[0Ktravis_time:end:05e65776:start=1569604094361119604,finish=1569604094434050376,duration=72930772,event=enable_i386[0Ktravis_time:start:00030e1d[0Ktravis_time:end:00030e1d:start=1569604094439522137,finish=1569604094444609713,duration=5087576,event=update_rubygems[0Ktravis_time:start:1653470d[0Ktravis_time:end:1653470d:start=1569604094449403987,finish=1569604095585236132,duration=1135832145,event=ensure_path_components[0Ktravis_time:start:00a36f11[0Ktravis_time:end:00a36f11:start=1569604095590127890,finish=1569604095593187656,duration=3059766,event=redefine_curl[0Ktravis_time:start:0629453d[0Ktravis_time:end:0629453d:start=1569604095598002314,finish=1569604095652648963,duration=54646649,event=nonblock_pipe[0Ktravis_time:start:048ba4f2[0Ktravis_time:end:048ba4f2:start=1569604095658168268,finish=1569604095701306629,duration=43138361,event=apt_get_update[0Ktravis_time:start:0c9c4eb7[0Ktravis_time:end:0c9c4eb7:start=1569604095706272392,finish=1569604095710392210,duration=4119818,event=deprecate_xcode_64[0Ktravis_time:start:1c2d7bec[0Ktravis_time:end:1c2d7bec:start=1569604095714801206,finish=1569604100636037289,duration=4921236083,event=update_heroku[0Ktravis_time:start:11cebdc4[0Ktravis_time:end:11cebdc4:start=1569604100641440817,finish=1569604100645363134,duration=3922317,event=shell_session_update[0Ktravis_time:start:09e83591[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3891
travis_fold:end:docker_mtu[0Ktravis_time:end:09e83591:start=1569604100650290554,finish=1569604101847730159,duration=1197439605,event=set_docker_mtu[0Ktravis_time:start:0e8d901a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0e8d901a:start=1569604101852333681,finish=1569604101923872086,duration=71538405,event=resolvconf[0Ktravis_time:start:24e2aa24[0Ktravis_time:end:24e2aa24:start=1569604101929143259,finish=1569604102028037544,duration=98894285,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:35490188[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:35490188:start=1569604102115348167,finish=1569604102448093281,duration=332745114,event=configure[0Ktravis_time:start:0df61938[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0df61938:start=1569604102453598917,finish=1569604112345430516,duration=9891831599,event=configure[0Ktravis_time:start:18a7491b[0Ktravis_fold:start:services[0Ktravis_time:start:01ea2eb8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:01ea2eb8:start=1569604112373355789,finish=1569604112389263085,duration=15907296,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:01ea2eb8:start=1569604112373355789,finish=1569604115395952712,duration=3022596923,event=services[0Ktravis_time:start:05966a68[0Ktravis_time:end:05966a68:start=1569604115400824508,finish=1569604115403784748,duration=2960240,event=fix_ps4[0Ktravis_time:start:09e05ecc[0K
travis_fold:start:git.checkout[0Ktravis_time:start:16dd22d8[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:16dd22d8:start=1569604115413306169,finish=1569604121770916211,duration=6357610042,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 92a2d96de651986b4a651cb923faf4ab421973a6
travis_fold:end:git.checkout[0K
travis_time:end:16dd22d8:start=1569604115413306169,finish=1569604122425473819,duration=7012167650,event=checkout[0Ktravis_time:start:28d7abf6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:28d7abf6:start=1569604122431147925,finish=1569604122442469764,duration=11321839,event=env[0Ktravis_time:start:0053c807[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0053c807:start=1569604122451531961,finish=1569604122457517177,duration=5985216,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:11e20cf3[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:17f5650d84b1edf1188baa12b43a57878d5324749f7f656f54914c06ff105fb0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/590479629/log.txt)