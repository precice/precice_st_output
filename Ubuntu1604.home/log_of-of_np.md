## Status: Passing 
Build: [982](https://travis-ci.org/precice/systemtests/builds/599837428) 

Job: [982.20](https://travis-ci.org/precice/systemtests/jobs/599837448) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5939c36bf85d...26213e77ad5d) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:052a0400:start=1571441587701295194,finish=1571441587707518312,duration=6223118,event=show_system_info[0Ktravis_time:start:0a2d5d0c[0Ktravis_time:end:0a2d5d0c:start=1571441587710451467,finish=1571441587734172518,duration=23721051,event=rm_riak_source[0Ktravis_time:start:1a8dae3b[0Ktravis_time:end:1a8dae3b:start=1571441587737738901,finish=1571441587743344424,duration=5605523,event=fix_rwky_redis[0Ktravis_time:start:0a1a282f[0Ktravis_time:end:0a1a282f:start=1571441587746424747,finish=1571441588124766473,duration=378341726,event=wait_for_network[0Ktravis_time:start:02b08924[0Ktravis_time:end:02b08924:start=1571441588132325361,finish=1571441589203180164,duration=1070854803,event=update_apt_keys[0Ktravis_time:start:13d69a4e[0Ktravis_time:end:13d69a4e:start=1571441589208547551,finish=1571441590306711031,duration=1098163480,event=fix_hhvm_source[0Ktravis_time:start:0abe34f0[0Ktravis_time:end:0abe34f0:start=1571441590312799819,finish=1571441590324980025,duration=12180206,event=update_mongo_arch[0Ktravis_time:start:01f5f506[0Ktravis_time:end:01f5f506:start=1571441590330385922,finish=1571441590377273226,duration=46887304,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0d25acfc[0Ktravis_time:end:0d25acfc:start=1571441590383177097,finish=1571441590386954324,duration=3777227,event=update_glibc[0Ktravis_time:start:01a26b74[0Ktravis_time:end:01a26b74:start=1571441590392058903,finish=1571441590405211086,duration=13152183,event=clean_up_path[0Ktravis_time:start:00a8a410[0Ktravis_time:end:00a8a410:start=1571441590410318988,finish=1571441590421758945,duration=11439957,event=fix_resolv_conf[0Ktravis_time:start:005694ae[0Ktravis_time:end:005694ae:start=1571441590428161103,finish=1571441590439722861,duration=11561758,event=fix_etc_hosts[0Ktravis_time:start:29a5feae[0Ktravis_time:end:29a5feae:start=1571441590444331706,finish=1571441590455764668,duration=11432962,event=fix_mvn_settings_xml[0Ktravis_time:start:37b0949c[0Ktravis_time:end:37b0949c:start=1571441590460626974,finish=1571441590472563182,duration=11936208,event=no_ipv6_localhost[0Ktravis_time:start:05163240[0Ktravis_time:end:05163240:start=1571441590480268841,finish=1571441590483855786,duration=3586945,event=fix_etc_mavenrc[0Ktravis_time:start:0124bf02[0Ktravis_time:end:0124bf02:start=1571441590488544306,finish=1571441590492923665,duration=4379359,event=fix_wwdr_certificate[0Ktravis_time:start:099e22c6[0Ktravis_time:end:099e22c6:start=1571441590498262160,finish=1571441590528456347,duration=30194187,event=put_localhost_first[0Ktravis_time:start:00492e80[0Ktravis_time:end:00492e80:start=1571441590533446227,finish=1571441590537669788,duration=4223561,event=home_paths[0Ktravis_time:start:01c6c10d[0Ktravis_time:end:01c6c10d:start=1571441590543050151,finish=1571441590560622222,duration=17572071,event=disable_initramfs[0Ktravis_time:start:115bc363[0Ktravis_time:end:115bc363:start=1571441590566628763,finish=1571441590960743753,duration=394114990,event=disable_ssh_roaming[0Ktravis_time:start:0db1aa78[0Ktravis_time:end:0db1aa78:start=1571441590967568599,finish=1571441590971868436,duration=4299837,event=debug_tools[0Ktravis_time:start:2b3ac89e[0Ktravis_time:end:2b3ac89e:start=1571441590976087934,finish=1571441590983070877,duration=6982943,event=uninstall_oclint[0Ktravis_time:start:00eeddfa[0Ktravis_time:end:00eeddfa:start=1571441590987133648,finish=1571441590991233168,duration=4099520,event=rvm_use[0Ktravis_time:start:10886a78[0Ktravis_time:end:10886a78:start=1571441590995179286,finish=1571441591010521119,duration=15341833,event=rm_etc_boto_cfg[0Ktravis_time:start:0be6b6de[0Ktravis_time:end:0be6b6de:start=1571441591014815963,finish=1571441591018127690,duration=3311727,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0693b1c3[0Ktravis_time:end:0693b1c3:start=1571441591022301496,finish=1571441591088384898,duration=66083402,event=enable_i386[0Ktravis_time:start:05bf7b20[0Ktravis_time:end:05bf7b20:start=1571441591093305912,finish=1571441591098816977,duration=5511065,event=update_rubygems[0Ktravis_time:start:0e297e54[0Ktravis_time:end:0e297e54:start=1571441591105241890,finish=1571441592194237684,duration=1088995794,event=ensure_path_components[0Ktravis_time:start:0bbd24d4[0Ktravis_time:end:0bbd24d4:start=1571441592201356389,finish=1571441592205172131,duration=3815742,event=redefine_curl[0Ktravis_time:start:147360f8[0Ktravis_time:end:147360f8:start=1571441592212787809,finish=1571441592273218427,duration=60430618,event=nonblock_pipe[0Ktravis_time:start:085406ca[0Ktravis_time:end:085406ca:start=1571441592278405996,finish=1571441592326179298,duration=47773302,event=apt_get_update[0Ktravis_time:start:060adb29[0Ktravis_time:end:060adb29:start=1571441592331095412,finish=1571441592334168128,duration=3072716,event=deprecate_xcode_64[0Ktravis_time:start:006e02fb[0Ktravis_time:end:006e02fb:start=1571441592340623212,finish=1571441597642186244,duration=5301563032,event=update_heroku[0Ktravis_time:start:1cf0b138[0Ktravis_time:end:1cf0b138:start=1571441597647401325,finish=1571441597651178109,duration=3776784,event=shell_session_update[0Ktravis_time:start:03002405[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3892
travis_fold:end:docker_mtu[0Ktravis_time:end:03002405:start=1571441597656337734,finish=1571441598851979076,duration=1195641342,event=set_docker_mtu[0Ktravis_time:start:1b28be8f[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1b28be8f:start=1571441598856934865,finish=1571441598926477671,duration=69542806,event=resolvconf[0Ktravis_time:start:00d54702[0Ktravis_time:end:00d54702:start=1571441598931536388,finish=1571441599044184968,duration=112648580,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2251849e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2251849e:start=1571441599131024662,finish=1571441599390832927,duration=259808265,event=configure[0Ktravis_time:start:0e89cfc5[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0e89cfc5:start=1571441599395893584,finish=1571441610121501423,duration=10725607839,event=configure[0Ktravis_time:start:244bbe3e[0Ktravis_fold:start:services[0Ktravis_time:start:0caae5cc[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0caae5cc:start=1571441610148519589,finish=1571441610162996634,duration=14477045,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0caae5cc:start=1571441610148519589,finish=1571441613170340752,duration=3021821163,event=services[0Ktravis_time:start:0836c88a[0Ktravis_time:end:0836c88a:start=1571441613177606445,finish=1571441613181445571,duration=3839126,event=fix_ps4[0Ktravis_time:start:0ebc4a93[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0e8c1138[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0e8c1138:start=1571441613193740261,finish=1571441619612034188,duration=6418293927,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 26213e77ad5d4262d59179ab7deb34279ed0b034
travis_fold:end:git.checkout[0K
travis_time:end:0e8c1138:start=1571441613193740261,finish=1571441620085201324,duration=6891461063,event=checkout[0Ktravis_time:start:023bff21[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:023bff21:start=1571441620091516863,finish=1571441620103986506,duration=12469643,event=env[0Ktravis_time:start:0c6107be[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0c6107be:start=1571441620114537030,finish=1571441620122643409,duration=8106379,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0495d818[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:0cf236788b7b5d560910641f19761ea96d86c59e5d53f118ea87e104e836311f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0495d818:start=1571441620499506608,finish=1571441743133845226,duration=122634338618,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:07e33827[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/599837448/log.txt)