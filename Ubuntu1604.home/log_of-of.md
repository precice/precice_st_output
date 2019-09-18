 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef) 
## Last 100 lines of the job log at the moment of push...
```
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
travis_time:end:0673f1c1:start=1568817190356409133,finish=1568817190362677017,duration=6267884,event=show_system_info[0Ktravis_time:start:02d0a0dc[0Ktravis_time:end:02d0a0dc:start=1568817190365769904,finish=1568817190392551003,duration=26781099,event=rm_riak_source[0Ktravis_time:start:041afa0c[0Ktravis_time:end:041afa0c:start=1568817190395703456,finish=1568817190401015387,duration=5311931,event=fix_rwky_redis[0Ktravis_time:start:0f29d8bb[0Ktravis_time:end:0f29d8bb:start=1568817190404059987,finish=1568817190767083881,duration=363023894,event=wait_for_network[0Ktravis_time:start:19cf1928[0Ktravis_time:end:19cf1928:start=1568817190778868256,finish=1568817191896461283,duration=1117593027,event=update_apt_keys[0Ktravis_time:start:00fe5d9c[0Ktravis_time:end:00fe5d9c:start=1568817191903579687,finish=1568817193011705124,duration=1108125437,event=fix_hhvm_source[0Ktravis_time:start:11ec52d7[0Ktravis_time:end:11ec52d7:start=1568817193017315961,finish=1568817193027891872,duration=10575911,event=update_mongo_arch[0Ktravis_time:start:020cb0a1[0Ktravis_time:end:020cb0a1:start=1568817193033029628,finish=1568817193076622607,duration=43592979,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1d740780[0Ktravis_time:end:1d740780:start=1568817193081717689,finish=1568817193085243867,duration=3526178,event=update_glibc[0Ktravis_time:start:0463621d[0Ktravis_time:end:0463621d:start=1568817193090126270,finish=1568817193100601667,duration=10475397,event=clean_up_path[0Ktravis_time:start:1007dde4[0Ktravis_time:end:1007dde4:start=1568817193107177307,finish=1568817193117733462,duration=10556155,event=fix_resolv_conf[0Ktravis_time:start:17d50842[0Ktravis_time:end:17d50842:start=1568817193123866895,finish=1568817193134527625,duration=10660730,event=fix_etc_hosts[0Ktravis_time:start:298447ce[0Ktravis_time:end:298447ce:start=1568817193142621166,finish=1568817193153610599,duration=10989433,event=fix_mvn_settings_xml[0Ktravis_time:start:033a20c7[0Ktravis_time:end:033a20c7:start=1568817193159500140,finish=1568817193169963308,duration=10463168,event=no_ipv6_localhost[0Ktravis_time:start:07a34510[0Ktravis_time:end:07a34510:start=1568817193174985406,finish=1568817193178764577,duration=3779171,event=fix_etc_mavenrc[0Ktravis_time:start:2ba32077[0Ktravis_time:end:2ba32077:start=1568817193183928357,finish=1568817193187634983,duration=3706626,event=fix_wwdr_certificate[0Ktravis_time:start:2ca6669e[0Ktravis_time:end:2ca6669e:start=1568817193192642255,finish=1568817193221507073,duration=28864818,event=put_localhost_first[0Ktravis_time:start:01baa396[0Ktravis_time:end:01baa396:start=1568817193226349023,finish=1568817193230205593,duration=3856570,event=home_paths[0Ktravis_time:start:01cba0e8[0Ktravis_time:end:01cba0e8:start=1568817193234959747,finish=1568817193252584256,duration=17624509,event=disable_initramfs[0Ktravis_time:start:19114f5a[0Ktravis_time:end:19114f5a:start=1568817193257936430,finish=1568817193559014049,duration=301077619,event=disable_ssh_roaming[0Ktravis_time:start:0012a9ad[0Ktravis_time:end:0012a9ad:start=1568817193564019859,finish=1568817193567202967,duration=3183108,event=debug_tools[0Ktravis_time:start:1045f2bb[0Ktravis_time:end:1045f2bb:start=1568817193573058469,finish=1568817193577629885,duration=4571416,event=uninstall_oclint[0Ktravis_time:start:08b4a02a[0Ktravis_time:end:08b4a02a:start=1568817193582332997,finish=1568817193588108087,duration=5775090,event=rvm_use[0Ktravis_time:start:016205e2[0Ktravis_time:end:016205e2:start=1568817193596656530,finish=1568817193605899081,duration=9242551,event=rm_etc_boto_cfg[0Ktravis_time:start:04d4fbd0[0Ktravis_time:end:04d4fbd0:start=1568817193610871187,finish=1568817193614144367,duration=3273180,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0024154a[0Ktravis_time:end:0024154a:start=1568817193619386193,finish=1568817193682106638,duration=62720445,event=enable_i386[0Ktravis_time:start:0114de25[0Ktravis_time:end:0114de25:start=1568817193686719771,finish=1568817193693207021,duration=6487250,event=update_rubygems[0Ktravis_time:start:02cb7260[0Ktravis_time:end:02cb7260:start=1568817193698548669,finish=1568817194834091953,duration=1135543284,event=ensure_path_components[0Ktravis_time:start:01e63890[0Ktravis_time:end:01e63890:start=1568817194839215525,finish=1568817194842058085,duration=2842560,event=redefine_curl[0Ktravis_time:start:21f71090[0Ktravis_time:end:21f71090:start=1568817194846344465,finish=1568817194902165983,duration=55821518,event=nonblock_pipe[0Ktravis_time:start:0dc1f010[0Ktravis_time:end:0dc1f010:start=1568817194908042699,finish=1568817194950353716,duration=42311017,event=apt_get_update[0Ktravis_time:start:0008fabc[0Ktravis_time:end:0008fabc:start=1568817194955147980,finish=1568817194958630916,duration=3482936,event=deprecate_xcode_64[0Ktravis_time:start:05fb9fd8[0Ktravis_time:end:05fb9fd8:start=1568817194962916131,finish=1568817200200135126,duration=5237218995,event=update_heroku[0Ktravis_time:start:0d6b5f60[0Ktravis_time:end:0d6b5f60:start=1568817200204491134,finish=1568817200207430053,duration=2938919,event=shell_session_update[0Ktravis_time:start:014191bc[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3928
travis_fold:end:docker_mtu[0Ktravis_time:end:014191bc:start=1568817200211662081,finish=1568817201415554548,duration=1203892467,event=set_docker_mtu[0Ktravis_time:start:03a9c479[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03a9c479:start=1568817201419761824,finish=1568817201493522638,duration=73760814,event=resolvconf[0Ktravis_time:start:03786114[0Ktravis_time:end:03786114:start=1568817201498343047,finish=1568817201609928545,duration=111585498,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1b97bcc4[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1b97bcc4:start=1568817201699290428,finish=1568817202166075266,duration=466784838,event=configure[0Ktravis_time:start:041ef908[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:041ef908:start=1568817202172079757,finish=1568817213485966042,duration=11313886285,event=configure[0Ktravis_time:start:29c51842[0Ktravis_fold:start:services[0Ktravis_time:start:0d7c45f0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0d7c45f0:start=1568817213513161249,finish=1568817213529771392,duration=16610143,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0d7c45f0:start=1568817213513161249,finish=1568817216534354548,duration=3021193299,event=services[0Ktravis_time:start:011ed51a[0Ktravis_time:end:011ed51a:start=1568817216538658389,finish=1568817216542416634,duration=3758245,event=fix_ps4[0Ktravis_time:start:14bed9f2[0K
travis_fold:start:git.checkout[0Ktravis_time:start:05f567ee[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:05f567ee:start=1568817216553040310,finish=1568817227234567914,duration=10681527604,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:05afd972[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:05afd972:start=1568817227238870318,finish=1568817227703401827,duration=464531509,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:05afd972:start=1568817227238870318,finish=1568817227882893773,duration=644023455,event=checkout[0Ktravis_time:start:09d321f5[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:09d321f5:start=1568817227887797898,finish=1568817227898744904,duration=10947006,event=env[0Ktravis_time:start:2491ded3[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2491ded3:start=1568817227903418830,finish=1568817227913235376,duration=9816546,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:08e0a37c[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {of-of_np,dealii-of,of-ccx,fe-fe,of-of,nutils-of,su2-ccx,bindings,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:08e0a37c:start=1568817228296668033,finish=1568817228365569810,duration=68901777,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:05e0853c[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510232/log.txt)