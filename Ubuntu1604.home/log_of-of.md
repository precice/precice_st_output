## Status: Failure 
Build: [1388](https://travis-ci.org/precice/systemtests/builds/632603195) 

Job: [1388.19](https://travis-ci.org/precice/systemtests/jobs/632603214) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/968fe698268820917cf52199d2d3dcbaaf61fbaf...4c749ac41fec1ac0cc04f8e71fcd731e33705ab1) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
  hhvm
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:1afab8a6:start=1578137359712549957,finish=1578137359717493191,duration=4943234,event=show_system_info[0Ktravis_time:start:17beece8[0Ktravis_time:end:17beece8:start=1578137359719938768,finish=1578137359740461874,duration=20523106,event=rm_riak_source[0Ktravis_time:start:037ada08[0Ktravis_time:end:037ada08:start=1578137359743058006,finish=1578137359747874708,duration=4816702,event=fix_rwky_redis[0Ktravis_time:start:26a7c341[0Ktravis_time:end:26a7c341:start=1578137359750680364,finish=1578137360123921974,duration=373241610,event=wait_for_network[0Ktravis_time:start:04c1195d[0Ktravis_time:end:04c1195d:start=1578137360128453516,finish=1578137361738531175,duration=1610077659,event=update_apt_keys[0Ktravis_time:start:2be4dd50[0Ktravis_time:end:2be4dd50:start=1578137361742783016,finish=1578137362648069926,duration=905286910,event=fix_hhvm_source[0Ktravis_time:start:121ecf54[0Ktravis_time:end:121ecf54:start=1578137362654111448,finish=1578137362663041035,duration=8929587,event=update_mongo_arch[0Ktravis_time:start:031d899a[0Ktravis_time:end:031d899a:start=1578137362667506306,finish=1578137362703075075,duration=35568769,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0e8b6648[0Ktravis_time:end:0e8b6648:start=1578137362707701823,finish=1578137362710163942,duration=2462119,event=update_glibc[0Ktravis_time:start:186c87c0[0Ktravis_time:end:186c87c0:start=1578137362714018442,finish=1578137362722692234,duration=8673792,event=clean_up_path[0Ktravis_time:start:000b2f3e[0Ktravis_time:end:000b2f3e:start=1578137362727451286,finish=1578137362734789239,duration=7337953,event=fix_resolv_conf[0Ktravis_time:start:11ee9c90[0Ktravis_time:end:11ee9c90:start=1578137362741616721,finish=1578137362749738425,duration=8121704,event=fix_etc_hosts[0Ktravis_time:start:106a5de3[0Ktravis_time:end:106a5de3:start=1578137362754090639,finish=1578137362763127371,duration=9036732,event=fix_mvn_settings_xml[0Ktravis_time:start:03f24420[0Ktravis_time:end:03f24420:start=1578137362767969953,finish=1578137362776391992,duration=8422039,event=no_ipv6_localhost[0Ktravis_time:start:02fc6f82[0Ktravis_time:end:02fc6f82:start=1578137362779442900,finish=1578137362781871102,duration=2428202,event=fix_etc_mavenrc[0Ktravis_time:start:1328ac9f[0Ktravis_time:end:1328ac9f:start=1578137362789153589,finish=1578137362792309630,duration=3156041,event=fix_wwdr_certificate[0Ktravis_time:start:1cae81a4[0Ktravis_time:end:1cae81a4:start=1578137362795423268,finish=1578137362823164657,duration=27741389,event=put_localhost_first[0Ktravis_time:start:035b00c0[0Ktravis_time:end:035b00c0:start=1578137362826294575,finish=1578137362830386884,duration=4092309,event=home_paths[0Ktravis_time:start:0882319e[0Ktravis_time:end:0882319e:start=1578137362836633955,finish=1578137362847624422,duration=10990467,event=disable_initramfs[0Ktravis_time:start:24017a94[0Ktravis_time:end:24017a94:start=1578137362850617098,finish=1578137363059984193,duration=209367095,event=disable_ssh_roaming[0Ktravis_time:start:089b2d20[0Ktravis_time:end:089b2d20:start=1578137363063563764,finish=1578137363066363624,duration=2799860,event=debug_tools[0Ktravis_time:start:069ad2a0[0Ktravis_time:end:069ad2a0:start=1578137363069938291,finish=1578137363073649473,duration=3711182,event=uninstall_oclint[0Ktravis_time:start:00e87f39[0Ktravis_time:end:00e87f39:start=1578137363080023007,finish=1578137363083155474,duration=3132467,event=rvm_use[0Ktravis_time:start:18896322[0Ktravis_time:end:18896322:start=1578137363086595091,finish=1578137363095121193,duration=8526102,event=rm_etc_boto_cfg[0Ktravis_time:start:0a1d9696[0Ktravis_time:end:0a1d9696:start=1578137363098499904,finish=1578137363104509847,duration=6009943,event=rm_oraclejdk8_symlink[0Ktravis_time:start:08d2b250[0Ktravis_time:end:08d2b250:start=1578137363107573945,finish=1578137363157046151,duration=49472206,event=enable_i386[0Ktravis_time:start:0334a550[0Ktravis_time:end:0334a550:start=1578137363161357174,finish=1578137363165075273,duration=3718099,event=update_rubygems[0Ktravis_time:start:0c204dc2[0Ktravis_time:end:0c204dc2:start=1578137363169941755,finish=1578137364012656044,duration=842714289,event=ensure_path_components[0Ktravis_time:start:092c5d00[0Ktravis_time:end:092c5d00:start=1578137364016984796,finish=1578137364019295496,duration=2310700,event=redefine_curl[0Ktravis_time:start:204fed84[0Ktravis_time:end:204fed84:start=1578137364022902690,finish=1578137364069156775,duration=46254085,event=nonblock_pipe[0Ktravis_time:start:0f7554cc[0Ktravis_time:end:0f7554cc:start=1578137364072994323,finish=1578137370101822384,duration=6028828061,event=apt_get_update[0Ktravis_time:start:0e062860[0Ktravis_time:end:0e062860:start=1578137370105812912,finish=1578137370108479025,duration=2666113,event=deprecate_xcode_64[0Ktravis_time:start:01b12fe6[0Ktravis_time:end:01b12fe6:start=1578137370112593980,finish=1578137373899124773,duration=3786530793,event=update_heroku[0Ktravis_time:start:1e55b1aa[0Ktravis_time:end:1e55b1aa:start=1578137373903355676,finish=1578137373905596406,duration=2240730,event=shell_session_update[0Ktravis_time:start:0eb90698[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3890
travis_fold:end:docker_mtu[0Ktravis_time:end:0eb90698:start=1578137373909508569,finish=1578137375098253060,duration=1188744491,event=set_docker_mtu[0Ktravis_time:start:2e16d553[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2e16d553:start=1578137375102256638,finish=1578137375159100964,duration=56844326,event=resolvconf[0Ktravis_time:start:35b80bf4[0Ktravis_time:end:35b80bf4:start=1578137375163218920,finish=1578137375247555377,duration=84336457,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:11868ddf[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:11868ddf:start=1578137375315246682,finish=1578137375675865350,duration=360618668,event=configure[0Ktravis_time:start:0bfa5fb5[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0bfa5fb5:start=1578137375680669918,finish=1578137383559909735,duration=7879239817,event=configure[0Ktravis_time:start:1f7c68e1[0Ktravis_fold:start:services[0Ktravis_time:start:34de35c0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:34de35c0:start=1578137383583274937,finish=1578137383596504704,duration=13229767,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:34de35c0:start=1578137383583274937,finish=1578137386601409673,duration=3018134736,event=services[0Ktravis_time:start:0ba8e58a[0Ktravis_time:end:0ba8e58a:start=1578137386605032912,finish=1578137386607412644,duration=2379732,event=fix_ps4[0Ktravis_time:start:04e800ac[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0a05bfc1[0K$ git clone --depth=50 --branch=develop https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0a05bfc1:start=1578137386614013993,finish=1578137392029175023,duration=5415161030,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4c749ac41fec1ac0cc04f8e71fcd731e33705ab1
travis_fold:end:git.checkout[0K
travis_time:end:0a05bfc1:start=1578137386614013993,finish=1578137392058542610,duration=5444528617,event=checkout[0Ktravis_time:start:1e6339c9[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1e6339c9:start=1578137392063106569,finish=1578137392074072073,duration=10965504,event=env[0Ktravis_time:start:1b4d5bc4[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1b4d5bc4:start=1578137392078566127,finish=1578137392084926729,duration=6360602,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1a1caede[0K$ python system_testing.py -s of-of
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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0a70c4bda4b8a4b21007a5392fa06b986eb68a743e629af06920da7302579693
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B
```
[
Full job log](https://api.travis-ci.org/v3/job/632603214/log.txt)