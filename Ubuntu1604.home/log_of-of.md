## Status: Passing 
Build: [990](https://travis-ci.org/precice/systemtests/builds/600304885) 

Job: [990.14](https://travis-ci.org/precice/systemtests/jobs/600304899) 

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
travis_time:end:1ff7a72e:start=1571576190757364835,finish=1571576190763977326,duration=6612491,event=show_system_info[0Ktravis_time:start:0047d735[0Ktravis_time:end:0047d735:start=1571576190767153854,finish=1571576190791898743,duration=24744889,event=rm_riak_source[0Ktravis_time:start:0c79e01f[0Ktravis_time:end:0c79e01f:start=1571576190795120564,finish=1571576190800610643,duration=5490079,event=fix_rwky_redis[0Ktravis_time:start:20374caa[0Ktravis_time:end:20374caa:start=1571576190803869593,finish=1571576191217960773,duration=414091180,event=wait_for_network[0Ktravis_time:start:3bdbf9a3[0Ktravis_time:end:3bdbf9a3:start=1571576191223922373,finish=1571576192931856447,duration=1707934074,event=update_apt_keys[0Ktravis_time:start:023bd9d0[0Ktravis_time:end:023bd9d0:start=1571576192936901391,finish=1571576194012514089,duration=1075612698,event=fix_hhvm_source[0Ktravis_time:start:04528241[0Ktravis_time:end:04528241:start=1571576194017932373,finish=1571576194030292637,duration=12360264,event=update_mongo_arch[0Ktravis_time:start:03edd840[0Ktravis_time:end:03edd840:start=1571576194035801724,finish=1571576194080879234,duration=45077510,event=fix_sudo_enabled_trusty[0Ktravis_time:start:28cb5c64[0Ktravis_time:end:28cb5c64:start=1571576194086024242,finish=1571576194089969102,duration=3944860,event=update_glibc[0Ktravis_time:start:03e6af22[0Ktravis_time:end:03e6af22:start=1571576194095211260,finish=1571576194104470730,duration=9259470,event=clean_up_path[0Ktravis_time:start:008cdc4b[0Ktravis_time:end:008cdc4b:start=1571576194109735620,finish=1571576194120363508,duration=10627888,event=fix_resolv_conf[0Ktravis_time:start:24c53b80[0Ktravis_time:end:24c53b80:start=1571576194125996864,finish=1571576194138480138,duration=12483274,event=fix_etc_hosts[0Ktravis_time:start:1cf43960[0Ktravis_time:end:1cf43960:start=1571576194142793379,finish=1571576194153655619,duration=10862240,event=fix_mvn_settings_xml[0Ktravis_time:start:16b6c28e[0Ktravis_time:end:16b6c28e:start=1571576194159419279,finish=1571576194171011539,duration=11592260,event=no_ipv6_localhost[0Ktravis_time:start:1b843698[0Ktravis_time:end:1b843698:start=1571576194176433674,finish=1571576194181909813,duration=5476139,event=fix_etc_mavenrc[0Ktravis_time:start:21d46ae1[0Ktravis_time:end:21d46ae1:start=1571576194186484689,finish=1571576194191536592,duration=5051903,event=fix_wwdr_certificate[0Ktravis_time:start:23d11c64[0Ktravis_time:end:23d11c64:start=1571576194197395502,finish=1571576194226038537,duration=28643035,event=put_localhost_first[0Ktravis_time:start:06180f58[0Ktravis_time:end:06180f58:start=1571576194231070019,finish=1571576194234912732,duration=3842713,event=home_paths[0Ktravis_time:start:2b9ccb06[0Ktravis_time:end:2b9ccb06:start=1571576194239796386,finish=1571576194255193853,duration=15397467,event=disable_initramfs[0Ktravis_time:start:0b280c70[0Ktravis_time:end:0b280c70:start=1571576194260750997,finish=1571576194525710539,duration=264959542,event=disable_ssh_roaming[0Ktravis_time:start:03aac218[0Ktravis_time:end:03aac218:start=1571576194531506436,finish=1571576194535096417,duration=3589981,event=debug_tools[0Ktravis_time:start:185c4d6b[0Ktravis_time:end:185c4d6b:start=1571576194540142325,finish=1571576194546384150,duration=6241825,event=uninstall_oclint[0Ktravis_time:start:0247daae[0Ktravis_time:end:0247daae:start=1571576194550876424,finish=1571576194554515864,duration=3639440,event=rvm_use[0Ktravis_time:start:00b22b28[0Ktravis_time:end:00b22b28:start=1571576194559231929,finish=1571576194567789568,duration=8557639,event=rm_etc_boto_cfg[0Ktravis_time:start:008f0e35[0Ktravis_time:end:008f0e35:start=1571576194572623890,finish=1571576194575327933,duration=2704043,event=rm_oraclejdk8_symlink[0Ktravis_time:start:07d36636[0Ktravis_time:end:07d36636:start=1571576194580239828,finish=1571576194638828778,duration=58588950,event=enable_i386[0Ktravis_time:start:0120c4fc[0Ktravis_time:end:0120c4fc:start=1571576194644897505,finish=1571576194650014889,duration=5117384,event=update_rubygems[0Ktravis_time:start:220f1760[0Ktravis_time:end:220f1760:start=1571576194655021521,finish=1571576195717253151,duration=1062231630,event=ensure_path_components[0Ktravis_time:start:0064e150[0Ktravis_time:end:0064e150:start=1571576195721768154,finish=1571576195725079263,duration=3311109,event=redefine_curl[0Ktravis_time:start:19ae7d48[0Ktravis_time:end:19ae7d48:start=1571576195729229235,finish=1571576195783235137,duration=54005902,event=nonblock_pipe[0Ktravis_time:start:003e3e54[0Ktravis_time:end:003e3e54:start=1571576195787952505,finish=1571576195830980897,duration=43028392,event=apt_get_update[0Ktravis_time:start:1ce484b9[0Ktravis_time:end:1ce484b9:start=1571576195836037166,finish=1571576195839195671,duration=3158505,event=deprecate_xcode_64[0Ktravis_time:start:03c590ba[0Ktravis_time:end:03c590ba:start=1571576195844551741,finish=1571576200371069308,duration=4526517567,event=update_heroku[0Ktravis_time:start:15d3ef89[0Ktravis_time:end:15d3ef89:start=1571576200376993056,finish=1571576200380447846,duration=3454790,event=shell_session_update[0Ktravis_time:start:10ef10fe[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3859
travis_fold:end:docker_mtu[0Ktravis_time:end:10ef10fe:start=1571576200384558164,finish=1571576201574212516,duration=1189654352,event=set_docker_mtu[0Ktravis_time:start:1976adbc[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1976adbc:start=1571576201578615389,finish=1571576201647440398,duration=68825009,event=resolvconf[0Ktravis_time:start:0743ba04[0Ktravis_time:end:0743ba04:start=1571576201651895924,finish=1571576201746662466,duration=94766542,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1a1d489d[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1a1d489d:start=1571576201831616770,finish=1571576202073217564,duration=241600794,event=configure[0Ktravis_time:start:063afc92[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:063afc92:start=1571576202078237022,finish=1571576211979257562,duration=9901020540,event=configure[0Ktravis_time:start:076a8254[0Ktravis_fold:start:services[0Ktravis_time:start:0c82709c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0c82709c:start=1571576212005545971,finish=1571576212020626737,duration=15080766,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0c82709c:start=1571576212005545971,finish=1571576215025875031,duration=3020329060,event=services[0Ktravis_time:start:11367e7c[0Ktravis_time:end:11367e7c:start=1571576215029850455,finish=1571576215032473950,duration=2623495,event=fix_ps4[0Ktravis_time:start:1567ce84[0K
travis_fold:start:git.checkout[0Ktravis_time:start:24ef823e[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:24ef823e:start=1571576215040326961,finish=1571576221331910153,duration=6291583192,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf a84a139c2665659f688bd5b27b53f4e910966493
travis_fold:end:git.checkout[0K
travis_time:end:24ef823e:start=1571576215040326961,finish=1571576221600527753,duration=6560200792,event=checkout[0Ktravis_time:start:169460d0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:169460d0:start=1571576221605912469,finish=1571576221615171874,duration=9259405,event=env[0Ktravis_time:start:306f8b44[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:306f8b44:start=1571576221619688484,finish=1571576221630013076,duration=10324592,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:3693e9c9[0K$ python system_testing.py -s of-of
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9a6ec2cc70ceed2d43eb990b726e61e5e7a3b457101d40bf784f81c204130d95
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient

```
[
Full job log](https://api.travis-ci.org/v3/job/600304899/log.txt)