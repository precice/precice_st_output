 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/594964989) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/92a2d96de651...58fea094b8a4) 
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
travis_time:end:03338cc4:start=1570520244905575088,finish=1570520244913544413,duration=7969325,event=show_system_info[0Ktravis_time:start:190beb04[0Ktravis_time:end:190beb04:start=1570520244916518768,finish=1570520244940558881,duration=24040113,event=rm_riak_source[0Ktravis_time:start:00fbf930[0Ktravis_time:end:00fbf930:start=1570520244943969453,finish=1570520244952368859,duration=8399406,event=fix_rwky_redis[0Ktravis_time:start:0039df5f[0Ktravis_time:end:0039df5f:start=1570520244957330407,finish=1570520245344773114,duration=387442707,event=wait_for_network[0Ktravis_time:start:23398223[0Ktravis_time:end:23398223:start=1570520245348933816,finish=1570520246961410852,duration=1612477036,event=update_apt_keys[0Ktravis_time:start:26e994a0[0Ktravis_time:end:26e994a0:start=1570520246966310147,finish=1570520248007550915,duration=1041240768,event=fix_hhvm_source[0Ktravis_time:start:0212f9d0[0Ktravis_time:end:0212f9d0:start=1570520248012550890,finish=1570520248022599061,duration=10048171,event=update_mongo_arch[0Ktravis_time:start:02fd5578[0Ktravis_time:end:02fd5578:start=1570520248027575259,finish=1570520248069765573,duration=42190314,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0a5641a0[0Ktravis_time:end:0a5641a0:start=1570520248074165253,finish=1570520248076829275,duration=2664022,event=update_glibc[0Ktravis_time:start:1cc17dec[0Ktravis_time:end:1cc17dec:start=1570520248081909550,finish=1570520248090830627,duration=8921077,event=clean_up_path[0Ktravis_time:start:0b78b3b3[0Ktravis_time:end:0b78b3b3:start=1570520248094858057,finish=1570520248103745231,duration=8887174,event=fix_resolv_conf[0Ktravis_time:start:1c8cfcb0[0Ktravis_time:end:1c8cfcb0:start=1570520248108549305,finish=1570520248118094310,duration=9545005,event=fix_etc_hosts[0Ktravis_time:start:09e35dab[0Ktravis_time:end:09e35dab:start=1570520248124873666,finish=1570520248135105204,duration=10231538,event=fix_mvn_settings_xml[0Ktravis_time:start:26184039[0Ktravis_time:end:26184039:start=1570520248139995188,finish=1570520248150513506,duration=10518318,event=no_ipv6_localhost[0Ktravis_time:start:0661f225[0Ktravis_time:end:0661f225:start=1570520248155122636,finish=1570520248157632828,duration=2510192,event=fix_etc_mavenrc[0Ktravis_time:start:202c1bee[0Ktravis_time:end:202c1bee:start=1570520248162778300,finish=1570520248167865573,duration=5087273,event=fix_wwdr_certificate[0Ktravis_time:start:0bd62e36[0Ktravis_time:end:0bd62e36:start=1570520248172458923,finish=1570520248197376168,duration=24917245,event=put_localhost_first[0Ktravis_time:start:004ed064[0Ktravis_time:end:004ed064:start=1570520248202867448,finish=1570520248210551234,duration=7683786,event=home_paths[0Ktravis_time:start:2a0d0216[0Ktravis_time:end:2a0d0216:start=1570520248215127876,finish=1570520248228203209,duration=13075333,event=disable_initramfs[0Ktravis_time:start:00f40c65[0Ktravis_time:end:00f40c65:start=1570520248233600429,finish=1570520248604627984,duration=371027555,event=disable_ssh_roaming[0Ktravis_time:start:05c6a27f[0Ktravis_time:end:05c6a27f:start=1570520248609494701,finish=1570520248612328686,duration=2833985,event=debug_tools[0Ktravis_time:start:05fdc7a8[0Ktravis_time:end:05fdc7a8:start=1570520248617393787,finish=1570520248621048382,duration=3654595,event=uninstall_oclint[0Ktravis_time:start:2b6183d4[0Ktravis_time:end:2b6183d4:start=1570520248625811108,finish=1570520248632210092,duration=6398984,event=rvm_use[0Ktravis_time:start:001e9bd3[0Ktravis_time:end:001e9bd3:start=1570520248636796066,finish=1570520248645081233,duration=8285167,event=rm_etc_boto_cfg[0Ktravis_time:start:12857d48[0Ktravis_time:end:12857d48:start=1570520248652452452,finish=1570520248655310914,duration=2858462,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0b8efb1b[0Ktravis_time:end:0b8efb1b:start=1570520248659003396,finish=1570520248715113407,duration=56110011,event=enable_i386[0Ktravis_time:start:18f6e11e[0Ktravis_time:end:18f6e11e:start=1570520248720561059,finish=1570520248725089176,duration=4528117,event=update_rubygems[0Ktravis_time:start:1d2b5a9e[0Ktravis_time:end:1d2b5a9e:start=1570520248729599069,finish=1570520249743253226,duration=1013654157,event=ensure_path_components[0Ktravis_time:start:0ec07183[0Ktravis_time:end:0ec07183:start=1570520249747926645,finish=1570520249750883158,duration=2956513,event=redefine_curl[0Ktravis_time:start:13fce267[0Ktravis_time:end:13fce267:start=1570520249755083868,finish=1570520249809114713,duration=54030845,event=nonblock_pipe[0Ktravis_time:start:008ac77a[0Ktravis_time:end:008ac77a:start=1570520249813428785,finish=1570520249878423862,duration=64995077,event=apt_get_update[0Ktravis_time:start:235bb94f[0Ktravis_time:end:235bb94f:start=1570520249883112747,finish=1570520249885956516,duration=2843769,event=deprecate_xcode_64[0Ktravis_time:start:129d67ac[0Ktravis_time:end:129d67ac:start=1570520249890234701,finish=1570520254696625963,duration=4806391262,event=update_heroku[0Ktravis_time:start:016ed877[0Ktravis_time:end:016ed877:start=1570520254701382582,finish=1570520254704066140,duration=2683558,event=shell_session_update[0Ktravis_time:start:0f33333b[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3889
travis_fold:end:docker_mtu[0Ktravis_time:end:0f33333b:start=1570520254707763744,finish=1570520255896776391,duration=1189012647,event=set_docker_mtu[0Ktravis_time:start:03691a7c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03691a7c:start=1570520255900498627,finish=1570520255966936658,duration=66438031,event=resolvconf[0Ktravis_time:start:018518da[0Ktravis_time:end:018518da:start=1570520255971739130,finish=1570520256080901013,duration=109161883,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2e7aa5ec[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2e7aa5ec:start=1570520256163353318,finish=1570520256825224519,duration=661871201,event=configure[0Ktravis_time:start:0d59250b[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d59250b:start=1570520256831102246,finish=1570520267064394747,duration=10233292501,event=configure[0Ktravis_time:start:0e247208[0Ktravis_fold:start:services[0Ktravis_time:start:1f7b9119[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1f7b9119:start=1570520267089874218,finish=1570520267104973184,duration=15098966,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1f7b9119:start=1570520267089874218,finish=1570520270111680640,duration=3021806422,event=services[0Ktravis_time:start:26f11774[0Ktravis_time:end:26f11774:start=1570520270116975914,finish=1570520270119787557,duration=2811643,event=fix_ps4[0Ktravis_time:start:2471df48[0K
travis_fold:start:git.checkout[0Ktravis_time:start:02b30b08[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:02b30b08:start=1570520270128877454,finish=1570520276348632491,duration=6219755037,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 58fea094b8a40df0d7d8ea6b460b42ec6cd296d4
travis_fold:end:git.checkout[0K
travis_time:end:02b30b08:start=1570520270128877454,finish=1570520276645828157,duration=6516950703,event=checkout[0Ktravis_time:start:0c4c9a0c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0c4c9a0c:start=1570520276649596778,finish=1570520276660188291,duration=10591513,event=env[0Ktravis_time:start:01a190c8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01a190c8:start=1570520276664919038,finish=1570520276670736282,duration=5817244,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0ed4e864[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:c65296c31938f09bcdc7e786618bfb96816d62bf502e46560432dc0890d7c016
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/594965009/log.txt)