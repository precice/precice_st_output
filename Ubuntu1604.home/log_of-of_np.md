 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586515488) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/28722fe13705...2efb54a69d10) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf) 
## Last 100 lines of the job log at the moment of push...
```
 9.5.10
9.6.6
[34m[1mRabbitMQ Version[0m
3.6.14
[34m[1mRedis version[0m
redis-server 4.0.6
[34m[1mriak version[0m
2.2.3
[34m[1mPre-installed Go versions[0m
1.7.4
[34m[1mant version[0m
Apache Ant(TM) version 1.9.3 compiled on April 8 2014
[34m[1mmvn version[0m
Apache Maven 3.5.2 (138edd61fd100ec658bfa2d307c43b76940a5d7d; 2017-10-18T07:58:13Z)
Maven home: /usr/local/maven-3.5.2
Java version: 1.8.0_151, vendor: Oracle Corporation
Java home: /usr/lib/jvm/java-8-oracle/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "4.4.0-98-generic", arch: "amd64", family: "unix"
[34m[1mgradle version[0m

------------------------------------------------------------
Gradle 4.0.1
------------------------------------------------------------

Build time:   2017-07-07 14:02:41 UTC
Revision:     38e5dc0f772daecca1d2681885d3d85414eb6826

Groovy:       2.4.11
Ant:          Apache Ant(TM) version 1.9.6 compiled on June 29 2015
JVM:          1.8.0_151 (Oracle Corporation 25.151-b12)
OS:           Linux 4.4.0-98-generic amd64

[34m[1mlein version[0m
Leiningen 2.8.1 on Java 1.8.0_151 Java HotSpot(TM) 64-Bit Server VM
[34m[1mPre-installed Node.js versions[0m
v4.8.6
v6.12.0
v6.12.1
v8.9
v8.9.1
[34m[1mphpenv versions[0m
  system
  5.6
* 5.6.32 (set by /home/travis/.phpenv/version)
  7.0
  7.0.25
  7.1
  7.1.11
  hhvm
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:00e71e80:start=1568819573822357600,finish=1568819573829921136,duration=7563536,event=show_system_info[0Ktravis_time:start:0e225e4a[0Ktravis_time:end:0e225e4a:start=1568819573832994118,finish=1568819573858249686,duration=25255568,event=rm_riak_source[0Ktravis_time:start:000109e8[0Ktravis_time:end:000109e8:start=1568819573862570586,finish=1568819573868280219,duration=5709633,event=fix_rwky_redis[0Ktravis_time:start:02a00ee0[0Ktravis_time:end:02a00ee0:start=1568819573871475197,finish=1568819574763035163,duration=891559966,event=wait_for_network[0Ktravis_time:start:0c83891a[0Ktravis_time:end:0c83891a:start=1568819574768496016,finish=1568819582780000028,duration=8011504012,event=update_apt_keys[0Ktravis_time:start:1173b868[0Ktravis_time:end:1173b868:start=1568819582784376993,finish=1568819583854121939,duration=1069744946,event=fix_hhvm_source[0Ktravis_time:start:17ad018a[0Ktravis_time:end:17ad018a:start=1568819583858827712,finish=1568819583869494476,duration=10666764,event=update_mongo_arch[0Ktravis_time:start:1696d9c4[0Ktravis_time:end:1696d9c4:start=1568819583876132510,finish=1568819583919753923,duration=43621413,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2c096bb8[0Ktravis_time:end:2c096bb8:start=1568819583924737724,finish=1568819583927756680,duration=3018956,event=update_glibc[0Ktravis_time:start:12e9eec4[0Ktravis_time:end:12e9eec4:start=1568819583932083819,finish=1568819583943861648,duration=11777829,event=clean_up_path[0Ktravis_time:start:01ff52c4[0Ktravis_time:end:01ff52c4:start=1568819583948152468,finish=1568819583958407898,duration=10255430,event=fix_resolv_conf[0Ktravis_time:start:1008d218[0Ktravis_time:end:1008d218:start=1568819583963044906,finish=1568819583975111616,duration=12066710,event=fix_etc_hosts[0Ktravis_time:start:17db9fe4[0Ktravis_time:end:17db9fe4:start=1568819583979967681,finish=1568819583990582661,duration=10614980,event=fix_mvn_settings_xml[0Ktravis_time:start:01720c4d[0Ktravis_time:end:01720c4d:start=1568819583995715922,finish=1568819584006829441,duration=11113519,event=no_ipv6_localhost[0Ktravis_time:start:25c3b68a[0Ktravis_time:end:25c3b68a:start=1568819584012110826,finish=1568819584015263746,duration=3152920,event=fix_etc_mavenrc[0Ktravis_time:start:0ab9fe74[0Ktravis_time:end:0ab9fe74:start=1568819584020135137,finish=1568819584023993966,duration=3858829,event=fix_wwdr_certificate[0Ktravis_time:start:22020342[0Ktravis_time:end:22020342:start=1568819584028423163,finish=1568819584059156813,duration=30733650,event=put_localhost_first[0Ktravis_time:start:2100dec0[0Ktravis_time:end:2100dec0:start=1568819584063197150,finish=1568819584067307216,duration=4110066,event=home_paths[0Ktravis_time:start:0668b4fa[0Ktravis_time:end:0668b4fa:start=1568819584074402594,finish=1568819584088248426,duration=13845832,event=disable_initramfs[0Ktravis_time:start:043d4b0d[0Ktravis_time:end:043d4b0d:start=1568819584094168622,finish=1568819584422727355,duration=328558733,event=disable_ssh_roaming[0Ktravis_time:start:20470880[0Ktravis_time:end:20470880:start=1568819584428136180,finish=1568819584431770507,duration=3634327,event=debug_tools[0Ktravis_time:start:1267592f[0Ktravis_time:end:1267592f:start=1568819584437297745,finish=1568819584441292524,duration=3994779,event=uninstall_oclint[0Ktravis_time:start:1b485dc0[0Ktravis_time:end:1b485dc0:start=1568819584445803226,finish=1568819584449669192,duration=3865966,event=rvm_use[0Ktravis_time:start:13d97e20[0Ktravis_time:end:13d97e20:start=1568819584456621901,finish=1568819584465870187,duration=9248286,event=rm_etc_boto_cfg[0Ktravis_time:start:0ea3c0ba[0Ktravis_time:end:0ea3c0ba:start=1568819584471019308,finish=1568819584474678524,duration=3659216,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2b032898[0Ktravis_time:end:2b032898:start=1568819584478756659,finish=1568819584549717877,duration=70961218,event=enable_i386[0Ktravis_time:start:04f43fe8[0Ktravis_time:end:04f43fe8:start=1568819584554882287,finish=1568819584560257810,duration=5375523,event=update_rubygems[0Ktravis_time:start:06c9275e[0Ktravis_time:end:06c9275e:start=1568819584566179731,finish=1568819585618950046,duration=1052770315,event=ensure_path_components[0Ktravis_time:start:0b9224c0[0Ktravis_time:end:0b9224c0:start=1568819585625226281,finish=1568819585628600516,duration=3374235,event=redefine_curl[0Ktravis_time:start:00da2ceb[0Ktravis_time:end:00da2ceb:start=1568819585633952488,finish=1568819585689627135,duration=55674647,event=nonblock_pipe[0Ktravis_time:start:0b18f75e[0Ktravis_time:end:0b18f75e:start=1568819585694708540,finish=1568819588276574613,duration=2581866073,event=apt_get_update[0Ktravis_time:start:064a5cac[0Ktravis_time:end:064a5cac:start=1568819588281596167,finish=1568819588284675641,duration=3079474,event=deprecate_xcode_64[0Ktravis_time:start:038d0867[0Ktravis_time:end:038d0867:start=1568819588289351637,finish=1568819593455908030,duration=5166556393,event=update_heroku[0Ktravis_time:start:09e04f10[0Ktravis_time:end:09e04f10:start=1568819593460598915,finish=1568819593463856724,duration=3257809,event=shell_session_update[0Ktravis_time:start:0e86e132[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3873
travis_fold:end:docker_mtu[0Ktravis_time:end:0e86e132:start=1568819593469782491,finish=1568819594662450122,duration=1192667631,event=set_docker_mtu[0Ktravis_time:start:070f0440[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:070f0440:start=1568819594666719209,finish=1568819594740157918,duration=73438709,event=resolvconf[0Ktravis_time:start:0bcf9f03[0Ktravis_time:end:0bcf9f03:start=1568819594745175761,finish=1568819594856627078,duration=111451317,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1e170a75[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1e170a75:start=1568819594949523289,finish=1568819595954211356,duration=1004688067,event=configure[0Ktravis_time:start:1e7714bc[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1e7714bc:start=1568819595960886114,finish=1568819608502212913,duration=12541326799,event=configure[0Ktravis_time:start:06203d60[0Ktravis_fold:start:services[0Ktravis_time:start:0f65ee57[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0f65ee57:start=1568819608528958328,finish=1568819608544488889,duration=15530561,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0f65ee57:start=1568819608528958328,finish=1568819611550480584,duration=3021522256,event=services[0Ktravis_time:start:0a450aa0[0Ktravis_time:end:0a450aa0:start=1568819611554943978,finish=1568819611557795012,duration=2851034,event=fix_ps4[0Ktravis_time:start:2fa4331a[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0352ac40[0K$ git clone --depth=50 --branch=addUbuntu1904 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0352ac40:start=1568819611566247794,finish=1568819622011793935,duration=10445546141,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2efb54a69d10db47b6397a7d0e706ba82502d2ac
travis_fold:end:git.checkout[0K
travis_time:end:0352ac40:start=1568819611566247794,finish=1568819622051357255,duration=10485109461,event=checkout[0Ktravis_time:start:0c01cf14[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0c01cf14:start=1568819622056198082,finish=1568819622067609151,duration=11411069,event=env[0Ktravis_time:start:020665d1[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:020665d1:start=1568819622076508235,finish=1568819622087294294,duration=10786059,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:031d37f5[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-of_np,bindings,of-of,nutils-of,su2-ccx,of-ccx,dealii-of,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:031d37f5:start=1568819622713029548,finish=1568819622793070494,duration=80040946,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:018843ce[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586515514/log.txt)