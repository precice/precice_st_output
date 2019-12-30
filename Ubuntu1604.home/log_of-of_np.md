## Status: Failure 
Build: [1372](https://travis-ci.org/precice/systemtests/builds/630890411) 

Job: [1372.23](https://travis-ci.org/precice/systemtests/jobs/630890444) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:005abaff:start=1577705322603832151,finish=1577705322608884383,duration=5052232,event=show_system_info[0Ktravis_time:start:27ac3a01[0Ktravis_time:end:27ac3a01:start=1577705322611286147,finish=1577705322629545196,duration=18259049,event=rm_riak_source[0Ktravis_time:start:00d01ae7[0Ktravis_time:end:00d01ae7:start=1577705322632847382,finish=1577705322638038651,duration=5191269,event=fix_rwky_redis[0Ktravis_time:start:00395ad2[0Ktravis_time:end:00395ad2:start=1577705322641075660,finish=1577705323005493644,duration=364417984,event=wait_for_network[0Ktravis_time:start:3a7edf3a[0Ktravis_time:end:3a7edf3a:start=1577705323011450060,finish=1577705324157889576,duration=1146439516,event=update_apt_keys[0Ktravis_time:start:01a9f5e6[0Ktravis_time:end:01a9f5e6:start=1577705324161681995,finish=1577705325022423426,duration=860741431,event=fix_hhvm_source[0Ktravis_time:start:0b0e501a[0Ktravis_time:end:0b0e501a:start=1577705325027084843,finish=1577705325036713823,duration=9628980,event=update_mongo_arch[0Ktravis_time:start:06aaaedb[0Ktravis_time:end:06aaaedb:start=1577705325043346412,finish=1577705325077684027,duration=34337615,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0110e5e8[0Ktravis_time:end:0110e5e8:start=1577705325081533614,finish=1577705325084054768,duration=2521154,event=update_glibc[0Ktravis_time:start:17cf93f4[0Ktravis_time:end:17cf93f4:start=1577705325087545342,finish=1577705325096074846,duration=8529504,event=clean_up_path[0Ktravis_time:start:10396647[0Ktravis_time:end:10396647:start=1577705325099679693,finish=1577705325108454304,duration=8774611,event=fix_resolv_conf[0Ktravis_time:start:0521ba85[0Ktravis_time:end:0521ba85:start=1577705325112488013,finish=1577705325120486000,duration=7997987,event=fix_etc_hosts[0Ktravis_time:start:15dd442d[0Ktravis_time:end:15dd442d:start=1577705325123455646,finish=1577705325132516650,duration=9061004,event=fix_mvn_settings_xml[0Ktravis_time:start:28231d02[0Ktravis_time:end:28231d02:start=1577705325135909535,finish=1577705325145871242,duration=9961707,event=no_ipv6_localhost[0Ktravis_time:start:074a80db[0Ktravis_time:end:074a80db:start=1577705325152079645,finish=1577705325154243970,duration=2164325,event=fix_etc_mavenrc[0Ktravis_time:start:1631df90[0Ktravis_time:end:1631df90:start=1577705325157992964,finish=1577705325161163869,duration=3170905,event=fix_wwdr_certificate[0Ktravis_time:start:105f2bd4[0Ktravis_time:end:105f2bd4:start=1577705325164884168,finish=1577705325185364667,duration=20480499,event=put_localhost_first[0Ktravis_time:start:13736a63[0Ktravis_time:end:13736a63:start=1577705325189242932,finish=1577705325192080295,duration=2837363,event=home_paths[0Ktravis_time:start:189cc9b4[0Ktravis_time:end:189cc9b4:start=1577705325196991134,finish=1577705325208213157,duration=11222023,event=disable_initramfs[0Ktravis_time:start:301d3497[0Ktravis_time:end:301d3497:start=1577705325212694693,finish=1577705325394697371,duration=182002678,event=disable_ssh_roaming[0Ktravis_time:start:1d8f00e6[0Ktravis_time:end:1d8f00e6:start=1577705325398532514,finish=1577705325401385536,duration=2853022,event=debug_tools[0Ktravis_time:start:08f4dc4e[0Ktravis_time:end:08f4dc4e:start=1577705325408162180,finish=1577705325411700089,duration=3537909,event=uninstall_oclint[0Ktravis_time:start:12e70413[0Ktravis_time:end:12e70413:start=1577705325415423227,finish=1577705325419741696,duration=4318469,event=rvm_use[0Ktravis_time:start:0a337b86[0Ktravis_time:end:0a337b86:start=1577705325423753021,finish=1577705325436202675,duration=12449654,event=rm_etc_boto_cfg[0Ktravis_time:start:0a24d3a5[0Ktravis_time:end:0a24d3a5:start=1577705325440861628,finish=1577705325443289527,duration=2427899,event=rm_oraclejdk8_symlink[0Ktravis_time:start:18ce5d86[0Ktravis_time:end:18ce5d86:start=1577705325447376884,finish=1577705325493535873,duration=46158989,event=enable_i386[0Ktravis_time:start:018fb6c0[0Ktravis_time:end:018fb6c0:start=1577705325497220746,finish=1577705325502024160,duration=4803414,event=update_rubygems[0Ktravis_time:start:0159adc4[0Ktravis_time:end:0159adc4:start=1577705325505315668,finish=1577705326344530156,duration=839214488,event=ensure_path_components[0Ktravis_time:start:01300340[0Ktravis_time:end:01300340:start=1577705326348671215,finish=1577705326351085455,duration=2414240,event=redefine_curl[0Ktravis_time:start:0306b488[0Ktravis_time:end:0306b488:start=1577705326354339596,finish=1577705326400409380,duration=46069784,event=nonblock_pipe[0Ktravis_time:start:0c896c31[0Ktravis_time:end:0c896c31:start=1577705326405030935,finish=1577705332435754376,duration=6030723441,event=apt_get_update[0Ktravis_time:start:14ba4b70[0Ktravis_time:end:14ba4b70:start=1577705332439789926,finish=1577705332442445738,duration=2655812,event=deprecate_xcode_64[0Ktravis_time:start:1ce75f3e[0Ktravis_time:end:1ce75f3e:start=1577705332446034179,finish=1577705336211083817,duration=3765049638,event=update_heroku[0Ktravis_time:start:03558d6f[0Ktravis_time:end:03558d6f:start=1577705336215149079,finish=1577705336217645868,duration=2496789,event=shell_session_update[0Ktravis_time:start:0154e831[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3904
travis_fold:end:docker_mtu[0Ktravis_time:end:0154e831:start=1577705336221595607,finish=1577705337411640119,duration=1190044512,event=set_docker_mtu[0Ktravis_time:start:18a9c80e[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:18a9c80e:start=1577705337414992035,finish=1577705337475738278,duration=60746243,event=resolvconf[0Ktravis_time:start:23a91550[0Ktravis_time:end:23a91550:start=1577705337479850543,finish=1577705337563964703,duration=84114160,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00627044[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00627044:start=1577705337633006739,finish=1577705337988600974,duration=355594235,event=configure[0Ktravis_time:start:0edc2813[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0edc2813:start=1577705337992899946,finish=1577705346134188400,duration=8141288454,event=configure[0Ktravis_time:start:1592ca74[0Ktravis_fold:start:services[0Ktravis_time:start:02763ba6[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:02763ba6:start=1577705346158168916,finish=1577705346172425017,duration=14256101,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:02763ba6:start=1577705346158168916,finish=1577705349177776668,duration=3019607752,event=services[0Ktravis_time:start:29b2e40c[0Ktravis_time:end:29b2e40c:start=1577705349181509310,finish=1577705349184200916,duration=2691606,event=fix_ps4[0Ktravis_time:start:06d8d412[0K
travis_fold:start:git.checkout[0Ktravis_time:start:13faad71[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:13faad71:start=1577705349191969937,finish=1577705354325687680,duration=5133717743,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 968fe698268820917cf52199d2d3dcbaaf61fbaf
travis_fold:end:git.checkout[0K
travis_time:end:13faad71:start=1577705349191969937,finish=1577705354591689337,duration=5399719400,event=checkout[0Ktravis_time:start:03cbf883[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:03cbf883:start=1577705354596276201,finish=1577705354607945189,duration=11668988,event=env[0Ktravis_time:start:03bd2558[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03bd2558:start=1577705354612211573,finish=1577705354617874221,duration=5662648,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:039177f3[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
All adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Fluid
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput: Solid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Solid', 'Fluid']
Files only in output(right)   : []

```
[
Full job log](https://api.travis-ci.org/v3/job/630890444/log.txt)