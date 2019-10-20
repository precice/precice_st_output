## Status: Passing 
Build: [990](https://travis-ci.org/precice/systemtests/builds/600304885) 

Job: [990.20](https://travis-ci.org/precice/systemtests/jobs/600304905) 

Triggered by: [push](https://github.com/precice/systemtests/compare/26213e77ad5d...a84a139c2665) 

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
travis_time:end:08adf1be:start=1571576617596548209,finish=1571576617602820399,duration=6272190,event=show_system_info[0Ktravis_time:start:0af415cd[0Ktravis_time:end:0af415cd:start=1571576617606264019,finish=1571576617630058142,duration=23794123,event=rm_riak_source[0Ktravis_time:start:21321468[0Ktravis_time:end:21321468:start=1571576617633715671,finish=1571576617639899958,duration=6184287,event=fix_rwky_redis[0Ktravis_time:start:33b05f80[0Ktravis_time:end:33b05f80:start=1571576617648331574,finish=1571576618039254415,duration=390922841,event=wait_for_network[0Ktravis_time:start:20888c20[0Ktravis_time:end:20888c20:start=1571576618044688664,finish=1571576619816978184,duration=1772289520,event=update_apt_keys[0Ktravis_time:start:03c46ce6[0Ktravis_time:end:03c46ce6:start=1571576619822697116,finish=1571576620947460057,duration=1124762941,event=fix_hhvm_source[0Ktravis_time:start:2ab8fdee[0Ktravis_time:end:2ab8fdee:start=1571576620953954209,finish=1571576620965093202,duration=11138993,event=update_mongo_arch[0Ktravis_time:start:02b85700[0Ktravis_time:end:02b85700:start=1571576620970460502,finish=1571576621016750037,duration=46289535,event=fix_sudo_enabled_trusty[0Ktravis_time:start:399bbd6d[0Ktravis_time:end:399bbd6d:start=1571576621022611717,finish=1571576621025705914,duration=3094197,event=update_glibc[0Ktravis_time:start:29b44687[0Ktravis_time:end:29b44687:start=1571576621030788852,finish=1571576621041005907,duration=10217055,event=clean_up_path[0Ktravis_time:start:28c2a2f0[0Ktravis_time:end:28c2a2f0:start=1571576621046142113,finish=1571576621056836830,duration=10694717,event=fix_resolv_conf[0Ktravis_time:start:0202cbd4[0Ktravis_time:end:0202cbd4:start=1571576621063987108,finish=1571576621074989961,duration=11002853,event=fix_etc_hosts[0Ktravis_time:start:1c2b44e6[0Ktravis_time:end:1c2b44e6:start=1571576621080779406,finish=1571576621091609395,duration=10829989,event=fix_mvn_settings_xml[0Ktravis_time:start:15be57de[0Ktravis_time:end:15be57de:start=1571576621096833440,finish=1571576621109263069,duration=12429629,event=no_ipv6_localhost[0Ktravis_time:start:1c201498[0Ktravis_time:end:1c201498:start=1571576621115324850,finish=1571576621118597465,duration=3272615,event=fix_etc_mavenrc[0Ktravis_time:start:13827ed0[0Ktravis_time:end:13827ed0:start=1571576621123436319,finish=1571576621130146653,duration=6710334,event=fix_wwdr_certificate[0Ktravis_time:start:00fb3d46[0Ktravis_time:end:00fb3d46:start=1571576621136179263,finish=1571576621164396628,duration=28217365,event=put_localhost_first[0Ktravis_time:start:0b27c47e[0Ktravis_time:end:0b27c47e:start=1571576621170746749,finish=1571576621175439174,duration=4692425,event=home_paths[0Ktravis_time:start:14ac2226[0Ktravis_time:end:14ac2226:start=1571576621180210830,finish=1571576621194556042,duration=14345212,event=disable_initramfs[0Ktravis_time:start:0134a77d[0Ktravis_time:end:0134a77d:start=1571576621200606940,finish=1571576621508074032,duration=307467092,event=disable_ssh_roaming[0Ktravis_time:start:064a6d6e[0Ktravis_time:end:064a6d6e:start=1571576621512734828,finish=1571576621515556396,duration=2821568,event=debug_tools[0Ktravis_time:start:096d02c0[0Ktravis_time:end:096d02c0:start=1571576621521651320,finish=1571576621527186866,duration=5535546,event=uninstall_oclint[0Ktravis_time:start:0f58c620[0Ktravis_time:end:0f58c620:start=1571576621532464073,finish=1571576621536276556,duration=3812483,event=rvm_use[0Ktravis_time:start:0b10dbc4[0Ktravis_time:end:0b10dbc4:start=1571576621541488301,finish=1571576621551796001,duration=10307700,event=rm_etc_boto_cfg[0Ktravis_time:start:19ea2c03[0Ktravis_time:end:19ea2c03:start=1571576621557446803,finish=1571576621560802322,duration=3355519,event=rm_oraclejdk8_symlink[0Ktravis_time:start:081721c2[0Ktravis_time:end:081721c2:start=1571576621566560846,finish=1571576621638078645,duration=71517799,event=enable_i386[0Ktravis_time:start:10e18ef7[0Ktravis_time:end:10e18ef7:start=1571576621643678926,finish=1571576621648304287,duration=4625361,event=update_rubygems[0Ktravis_time:start:081f2a00[0Ktravis_time:end:081f2a00:start=1571576621655105545,finish=1571576622718362341,duration=1063256796,event=ensure_path_components[0Ktravis_time:start:1c2101f4[0Ktravis_time:end:1c2101f4:start=1571576622724116921,finish=1571576622727560072,duration=3443151,event=redefine_curl[0Ktravis_time:start:0a428dc2[0Ktravis_time:end:0a428dc2:start=1571576622733623477,finish=1571576622791976397,duration=58352920,event=nonblock_pipe[0Ktravis_time:start:150af3e0[0Ktravis_time:end:150af3e0:start=1571576622797641597,finish=1571576622853400163,duration=55758566,event=apt_get_update[0Ktravis_time:start:2811142f[0Ktravis_time:end:2811142f:start=1571576622859579832,finish=1571576622862628704,duration=3048872,event=deprecate_xcode_64[0Ktravis_time:start:06d3395c[0Ktravis_time:end:06d3395c:start=1571576622867538173,finish=1571576627617898448,duration=4750360275,event=update_heroku[0Ktravis_time:start:14705ea4[0Ktravis_time:end:14705ea4:start=1571576627623233447,finish=1571576627626918289,duration=3684842,event=shell_session_update[0Ktravis_time:start:0a7772e9[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3863
travis_fold:end:docker_mtu[0Ktravis_time:end:0a7772e9:start=1571576627632468043,finish=1571576628838003418,duration=1205535375,event=set_docker_mtu[0Ktravis_time:start:09055ebb[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:09055ebb:start=1571576628843437715,finish=1571576628916171402,duration=72733687,event=resolvconf[0Ktravis_time:start:0aed7984[0Ktravis_time:end:0aed7984:start=1571576628921654664,finish=1571576629025949104,duration=104294440,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:3a48b37e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:3a48b37e:start=1571576629114104531,finish=1571576629470939785,duration=356835254,event=configure[0Ktravis_time:start:00141aa1[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:00141aa1:start=1571576629476679154,finish=1571576640539150802,duration=11062471648,event=configure[0Ktravis_time:start:12a02d14[0Ktravis_fold:start:services[0Ktravis_time:start:1d5d6dd1[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1d5d6dd1:start=1571576640566162310,finish=1571576640581230311,duration=15068001,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1d5d6dd1:start=1571576640566162310,finish=1571576643587496715,duration=3021334405,event=services[0Ktravis_time:start:0b0789bc[0Ktravis_time:end:0b0789bc:start=1571576643592382065,finish=1571576643595623625,duration=3241560,event=fix_ps4[0Ktravis_time:start:00091cb0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0f38fcf4[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0f38fcf4:start=1571576643606435735,finish=1571576649901903631,duration=6295467896,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf a84a139c2665659f688bd5b27b53f4e910966493
travis_fold:end:git.checkout[0K
travis_time:end:0f38fcf4:start=1571576643606435735,finish=1571576650731078464,duration=7124642729,event=checkout[0Ktravis_time:start:03294ee2[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:03294ee2:start=1571576650736953395,finish=1571576650751207739,duration=14254344,event=env[0Ktravis_time:start:28746322[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:28746322:start=1571576650757277943,finish=1571576650765382324,duration=8104381,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0ec1f558[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:9a6ec2cc70ceed2d43eb990b726e61e5e7a3b457101d40bf784f81c204130d95
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/600304905/log.txt)