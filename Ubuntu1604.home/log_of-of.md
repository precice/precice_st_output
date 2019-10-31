## Status: Passing 
Build: [1048](https://travis-ci.org/precice/systemtests/builds/605292585) 

Job: [1048.18](https://travis-ci.org/precice/systemtests/jobs/605292603) 

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
travis_time:end:0b94e4a2:start=1572489498873563044,finish=1572489498880085889,duration=6522845,event=show_system_info[0Ktravis_time:start:1b51285c[0Ktravis_time:end:1b51285c:start=1572489498883300623,finish=1572489498909086875,duration=25786252,event=rm_riak_source[0Ktravis_time:start:05557b48[0Ktravis_time:end:05557b48:start=1572489498912591106,finish=1572489498918606248,duration=6015142,event=fix_rwky_redis[0Ktravis_time:start:2b787c70[0Ktravis_time:end:2b787c70:start=1572489498921903392,finish=1572489499281855002,duration=359951610,event=wait_for_network[0Ktravis_time:start:0c394661[0Ktravis_time:end:0c394661:start=1572489499286833549,finish=1572489500917289782,duration=1630456233,event=update_apt_keys[0Ktravis_time:start:3778b386[0Ktravis_time:end:3778b386:start=1572489500923858995,finish=1572489502007331830,duration=1083472835,event=fix_hhvm_source[0Ktravis_time:start:108b3939[0Ktravis_time:end:108b3939:start=1572489502013069589,finish=1572489502023391046,duration=10321457,event=update_mongo_arch[0Ktravis_time:start:3097120d[0Ktravis_time:end:3097120d:start=1572489502028309483,finish=1572489502071738173,duration=43428690,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0aff6800[0Ktravis_time:end:0aff6800:start=1572489502076933653,finish=1572489502079886007,duration=2952354,event=update_glibc[0Ktravis_time:start:33812a2d[0Ktravis_time:end:33812a2d:start=1572489502084657937,finish=1572489502095222189,duration=10564252,event=clean_up_path[0Ktravis_time:start:1337b01a[0Ktravis_time:end:1337b01a:start=1572489502100722594,finish=1572489502109565823,duration=8843229,event=fix_resolv_conf[0Ktravis_time:start:02b895ee[0Ktravis_time:end:02b895ee:start=1572489502116002729,finish=1572489502125804795,duration=9802066,event=fix_etc_hosts[0Ktravis_time:start:2f41d560[0Ktravis_time:end:2f41d560:start=1572489502131304954,finish=1572489502141660820,duration=10355866,event=fix_mvn_settings_xml[0Ktravis_time:start:03be3b58[0Ktravis_time:end:03be3b58:start=1572489502146740862,finish=1572489502159167995,duration=12427133,event=no_ipv6_localhost[0Ktravis_time:start:1d704ff8[0Ktravis_time:end:1d704ff8:start=1572489502164256031,finish=1572489502167611918,duration=3355887,event=fix_etc_mavenrc[0Ktravis_time:start:0e5a2f0e[0Ktravis_time:end:0e5a2f0e:start=1572489502172784930,finish=1572489502178532565,duration=5747635,event=fix_wwdr_certificate[0Ktravis_time:start:27b16968[0Ktravis_time:end:27b16968:start=1572489502183957867,finish=1572489502210348141,duration=26390274,event=put_localhost_first[0Ktravis_time:start:02a67596[0Ktravis_time:end:02a67596:start=1572489502216252294,finish=1572489502220654266,duration=4401972,event=home_paths[0Ktravis_time:start:1d775384[0Ktravis_time:end:1d775384:start=1572489502226676903,finish=1572489502240026312,duration=13349409,event=disable_initramfs[0Ktravis_time:start:039ea5d6[0Ktravis_time:end:039ea5d6:start=1572489502246587278,finish=1572489502646304684,duration=399717406,event=disable_ssh_roaming[0Ktravis_time:start:2545990b[0Ktravis_time:end:2545990b:start=1572489502651164226,finish=1572489502654145308,duration=2981082,event=debug_tools[0Ktravis_time:start:01895cd4[0Ktravis_time:end:01895cd4:start=1572489502658875299,finish=1572489502662604675,duration=3729376,event=uninstall_oclint[0Ktravis_time:start:237870fc[0Ktravis_time:end:237870fc:start=1572489502667139311,finish=1572489502671320410,duration=4181099,event=rvm_use[0Ktravis_time:start:01a42b04[0Ktravis_time:end:01a42b04:start=1572489502674961765,finish=1572489502686249345,duration=11287580,event=rm_etc_boto_cfg[0Ktravis_time:start:1345fec0[0Ktravis_time:end:1345fec0:start=1572489502690741485,finish=1572489502694126853,duration=3385368,event=rm_oraclejdk8_symlink[0Ktravis_time:start:082f7125[0Ktravis_time:end:082f7125:start=1572489502698214363,finish=1572489502760128638,duration=61914275,event=enable_i386[0Ktravis_time:start:03bc866b[0Ktravis_time:end:03bc866b:start=1572489502765664906,finish=1572489502770514297,duration=4849391,event=update_rubygems[0Ktravis_time:start:03aacf94[0Ktravis_time:end:03aacf94:start=1572489502775492077,finish=1572489503813167477,duration=1037675400,event=ensure_path_components[0Ktravis_time:start:1f29a407[0Ktravis_time:end:1f29a407:start=1572489503818995891,finish=1572489503822686284,duration=3690393,event=redefine_curl[0Ktravis_time:start:033326ac[0Ktravis_time:end:033326ac:start=1572489503827074849,finish=1572489503879661567,duration=52586718,event=nonblock_pipe[0Ktravis_time:start:0040df36[0Ktravis_time:end:0040df36:start=1572489503884015070,finish=1572489506927986303,duration=3043971233,event=apt_get_update[0Ktravis_time:start:161bdf88[0Ktravis_time:end:161bdf88:start=1572489506932929799,finish=1572489506936043143,duration=3113344,event=deprecate_xcode_64[0Ktravis_time:start:061d79ab[0Ktravis_time:end:061d79ab:start=1572489506940315706,finish=1572489511720072756,duration=4779757050,event=update_heroku[0Ktravis_time:start:0e6145d0[0Ktravis_time:end:0e6145d0:start=1572489511725814348,finish=1572489511728544190,duration=2729842,event=shell_session_update[0Ktravis_time:start:0ce22078[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3889
travis_fold:end:docker_mtu[0Ktravis_time:end:0ce22078:start=1572489511733614209,finish=1572489512930783946,duration=1197169737,event=set_docker_mtu[0Ktravis_time:start:0f41249a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0f41249a:start=1572489512935544148,finish=1572489513001836544,duration=66292396,event=resolvconf[0Ktravis_time:start:205ef315[0Ktravis_time:end:205ef315:start=1572489513007323102,finish=1572489513115962562,duration=108639460,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:04accd3c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:04accd3c:start=1572489513198506303,finish=1572489514434396596,duration=1235890293,event=configure[0Ktravis_time:start:02ba9b11[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02ba9b11:start=1572489514439926013,finish=1572489523920065231,duration=9480139218,event=configure[0Ktravis_time:start:238494a0[0Ktravis_fold:start:services[0Ktravis_time:start:178323f0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:178323f0:start=1572489523948400315,finish=1572489523966251185,duration=17850870,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:178323f0:start=1572489523948400315,finish=1572489526971877781,duration=3023477466,event=services[0Ktravis_time:start:06e2a96b[0Ktravis_time:end:06e2a96b:start=1572489526976179191,finish=1572489526979295879,duration=3116688,event=fix_ps4[0Ktravis_time:start:0564bbc2[0K
travis_fold:start:git.checkout[0Ktravis_time:start:09dd0800[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:09dd0800:start=1572489526988077569,finish=1572489534099234250,duration=7111156681,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:09dd0800:start=1572489526988077569,finish=1572489534174639527,duration=7186561958,event=checkout[0Ktravis_time:start:20ba1800[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:20ba1800:start=1572489534179611142,finish=1572489534193027258,duration=13416116,event=env[0Ktravis_time:start:03843c04[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03843c04:start=1572489534199846895,finish=1572489534206443315,duration=6596420,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:03645156[0K$ python system_testing.py -s of-of
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
Digest: sha256:fb635a84da883c6511a60b5b910a60599e4ef789b46704d8959215aa07274e1c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/605292603/log.txt)