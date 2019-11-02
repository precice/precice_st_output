## Status: Passing 
Build: [1054](https://travis-ci.org/precice/systemtests/builds/606282132) 

Job: [1054.18](https://travis-ci.org/precice/systemtests/jobs/606282156) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:0bb41c6c:start=1572662583360322463,finish=1572662583367072968,duration=6750505,event=show_system_info[0Ktravis_time:start:06e87c5a[0Ktravis_time:end:06e87c5a:start=1572662583370369209,finish=1572662583402252772,duration=31883563,event=rm_riak_source[0Ktravis_time:start:0f2ac108[0Ktravis_time:end:0f2ac108:start=1572662583406887567,finish=1572662583413963926,duration=7076359,event=fix_rwky_redis[0Ktravis_time:start:1b36f479[0Ktravis_time:end:1b36f479:start=1572662583418104663,finish=1572662583822744306,duration=404639643,event=wait_for_network[0Ktravis_time:start:01eac798[0Ktravis_time:end:01eac798:start=1572662583835618496,finish=1572662585435033525,duration=1599415029,event=update_apt_keys[0Ktravis_time:start:0d9928c8[0Ktravis_time:end:0d9928c8:start=1572662585442482098,finish=1572662586539008339,duration=1096526241,event=fix_hhvm_source[0Ktravis_time:start:08064480[0Ktravis_time:end:08064480:start=1572662586545479376,finish=1572662586557246003,duration=11766627,event=update_mongo_arch[0Ktravis_time:start:18179f52[0Ktravis_time:end:18179f52:start=1572662586562883535,finish=1572662586609190307,duration=46306772,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2146ad51[0Ktravis_time:end:2146ad51:start=1572662586614762150,finish=1572662586618553703,duration=3791553,event=update_glibc[0Ktravis_time:start:03beb768[0Ktravis_time:end:03beb768:start=1572662586623948548,finish=1572662586635513224,duration=11564676,event=clean_up_path[0Ktravis_time:start:0b8c0b26[0Ktravis_time:end:0b8c0b26:start=1572662586642747479,finish=1572662586652752771,duration=10005292,event=fix_resolv_conf[0Ktravis_time:start:085b5e2b[0Ktravis_time:end:085b5e2b:start=1572662586660929328,finish=1572662586672008941,duration=11079613,event=fix_etc_hosts[0Ktravis_time:start:13142514[0Ktravis_time:end:13142514:start=1572662586677834525,finish=1572662586690200035,duration=12365510,event=fix_mvn_settings_xml[0Ktravis_time:start:0a235940[0Ktravis_time:end:0a235940:start=1572662586695136328,finish=1572662586706590183,duration=11453855,event=no_ipv6_localhost[0Ktravis_time:start:0c6f84a5[0Ktravis_time:end:0c6f84a5:start=1572662586710786023,finish=1572662586713741301,duration=2955278,event=fix_etc_mavenrc[0Ktravis_time:start:1671c0e5[0Ktravis_time:end:1671c0e5:start=1572662586717770229,finish=1572662586721717268,duration=3947039,event=fix_wwdr_certificate[0Ktravis_time:start:2204cd48[0Ktravis_time:end:2204cd48:start=1572662586725765796,finish=1572662586757521946,duration=31756150,event=put_localhost_first[0Ktravis_time:start:1d51e0a8[0Ktravis_time:end:1d51e0a8:start=1572662586761878306,finish=1572662586766090643,duration=4212337,event=home_paths[0Ktravis_time:start:2c085d34[0Ktravis_time:end:2c085d34:start=1572662586771290431,finish=1572662586788013746,duration=16723315,event=disable_initramfs[0Ktravis_time:start:04bc97eb[0Ktravis_time:end:04bc97eb:start=1572662586794177525,finish=1572662587152951515,duration=358773990,event=disable_ssh_roaming[0Ktravis_time:start:17d63645[0Ktravis_time:end:17d63645:start=1572662587159036519,finish=1572662587161881945,duration=2845426,event=debug_tools[0Ktravis_time:start:13c9bdd4[0Ktravis_time:end:13c9bdd4:start=1572662587166391421,finish=1572662587170013194,duration=3621773,event=uninstall_oclint[0Ktravis_time:start:045f1eea[0Ktravis_time:end:045f1eea:start=1572662587174453167,finish=1572662587178349915,duration=3896748,event=rvm_use[0Ktravis_time:start:00d0ae08[0Ktravis_time:end:00d0ae08:start=1572662587184966582,finish=1572662587194547738,duration=9581156,event=rm_etc_boto_cfg[0Ktravis_time:start:0e1e1a50[0Ktravis_time:end:0e1e1a50:start=1572662587199725545,finish=1572662587205604430,duration=5878885,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0f0a5fc0[0Ktravis_time:end:0f0a5fc0:start=1572662587211306911,finish=1572662587273880733,duration=62573822,event=enable_i386[0Ktravis_time:start:074e9ed8[0Ktravis_time:end:074e9ed8:start=1572662587279584832,finish=1572662587285257832,duration=5673000,event=update_rubygems[0Ktravis_time:start:27424a56[0Ktravis_time:end:27424a56:start=1572662587292435943,finish=1572662588493153694,duration=1200717751,event=ensure_path_components[0Ktravis_time:start:06d125c0[0Ktravis_time:end:06d125c0:start=1572662588498500303,finish=1572662588501755366,duration=3255063,event=redefine_curl[0Ktravis_time:start:077de448[0Ktravis_time:end:077de448:start=1572662588506916110,finish=1572662588565773402,duration=58857292,event=nonblock_pipe[0Ktravis_time:start:0f81f8cb[0Ktravis_time:end:0f81f8cb:start=1572662588571022579,finish=1572662591618394911,duration=3047372332,event=apt_get_update[0Ktravis_time:start:0c1ce36c[0Ktravis_time:end:0c1ce36c:start=1572662591623880422,finish=1572662591627337315,duration=3456893,event=deprecate_xcode_64[0Ktravis_time:start:0890223a[0Ktravis_time:end:0890223a:start=1572662591632946127,finish=1572662596787627578,duration=5154681451,event=update_heroku[0Ktravis_time:start:200313a8[0Ktravis_time:end:200313a8:start=1572662596793145830,finish=1572662596796972311,duration=3826481,event=shell_session_update[0Ktravis_time:start:0a027e0c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3895
travis_fold:end:docker_mtu[0Ktravis_time:end:0a027e0c:start=1572662596801732348,finish=1572662598014263266,duration=1212530918,event=set_docker_mtu[0Ktravis_time:start:337107c0[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:337107c0:start=1572662598019662900,finish=1572662598095965200,duration=76302300,event=resolvconf[0Ktravis_time:start:0c2ea1c9[0Ktravis_time:end:0c2ea1c9:start=1572662598102490987,finish=1572662598215871087,duration=113380100,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0a2a3eb2[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0a2a3eb2:start=1572662598307842855,finish=1572662598558090196,duration=250247341,event=configure[0Ktravis_time:start:090de540[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:090de540:start=1572662598563961056,finish=1572662610055875076,duration=11491914020,event=configure[0Ktravis_time:start:07c706a2[0Ktravis_fold:start:services[0Ktravis_time:start:12082140[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:12082140:start=1572662610084041371,finish=1572662610100654826,duration=16613455,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:12082140:start=1572662610084041371,finish=1572662613106904749,duration=3022863378,event=services[0Ktravis_time:start:2379d8e6[0Ktravis_time:end:2379d8e6:start=1572662613112527402,finish=1572662613116453812,duration=3926410,event=fix_ps4[0Ktravis_time:start:00b45460[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0814a29e[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0814a29e:start=1572662613125717622,finish=1572662619588832159,duration=6463114537,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0814a29e:start=1572662613125717622,finish=1572662620049969569,duration=6924251947,event=checkout[0Ktravis_time:start:092dfa02[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:092dfa02:start=1572662620055134915,finish=1572662620067604150,duration=12469235,event=env[0Ktravis_time:start:14c58094[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:14c58094:start=1572662620073245272,finish=1572662620080462499,duration=7217227,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:14d0c9ba[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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

Creating network "testcomposeofof_default" with the default driver
Creating network "testcomposeofof_[secure]comm" with the default driver
Creating volume "testcomposeofof_output" with default driver
Creating volume "testcomposeofof_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7b35f009c5169ca242753a754e0675197b77bde0b0ee3330c95449a33e668f39
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:14d0c9ba:start=1572662620485908196,finish=1572662742481296736,duration=121995388540,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00c806f1[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/606282156/log.txt)