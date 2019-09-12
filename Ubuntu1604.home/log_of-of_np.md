 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584291854) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aabfec63ba1b...d9aa1e4cf4f1) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903) 
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
travis_time:end:1655ee3c:start=1568324521946201525,finish=1568324521952509442,duration=6307917,event=show_system_info[0Ktravis_time:start:00a6af54[0Ktravis_time:end:00a6af54:start=1568324521955592044,finish=1568324521983919567,duration=28327523,event=rm_riak_source[0Ktravis_time:start:17dd9234[0Ktravis_time:end:17dd9234:start=1568324521987232924,finish=1568324521992626284,duration=5393360,event=fix_rwky_redis[0Ktravis_time:start:00950e98[0Ktravis_time:end:00950e98:start=1568324521995804285,finish=1568324522415606253,duration=419801968,event=wait_for_network[0Ktravis_time:start:00820d34[0Ktravis_time:end:00820d34:start=1568324522421352953,finish=1568324524013689776,duration=1592336823,event=update_apt_keys[0Ktravis_time:start:28a6d47d[0Ktravis_time:end:28a6d47d:start=1568324524018301854,finish=1568324525061064901,duration=1042763047,event=fix_hhvm_source[0Ktravis_time:start:05e7286c[0Ktravis_time:end:05e7286c:start=1568324525065560707,finish=1568324525075942344,duration=10381637,event=update_mongo_arch[0Ktravis_time:start:009cbf0a[0Ktravis_time:end:009cbf0a:start=1568324525081283683,finish=1568324525125242337,duration=43958654,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0c613b7e[0Ktravis_time:end:0c613b7e:start=1568324525130285193,finish=1568324525133012473,duration=2727280,event=update_glibc[0Ktravis_time:start:09351d54[0Ktravis_time:end:09351d54:start=1568324525138043327,finish=1568324525149850492,duration=11807165,event=clean_up_path[0Ktravis_time:start:0991c60e[0Ktravis_time:end:0991c60e:start=1568324525155494175,finish=1568324525166150246,duration=10656071,event=fix_resolv_conf[0Ktravis_time:start:04dce25e[0Ktravis_time:end:04dce25e:start=1568324525171441547,finish=1568324525184022167,duration=12580620,event=fix_etc_hosts[0Ktravis_time:start:088dd180[0Ktravis_time:end:088dd180:start=1568324525190315326,finish=1568324525205140312,duration=14824986,event=fix_mvn_settings_xml[0Ktravis_time:start:0cd2972a[0Ktravis_time:end:0cd2972a:start=1568324525209742314,finish=1568324525221815908,duration=12073594,event=no_ipv6_localhost[0Ktravis_time:start:044fb5c8[0Ktravis_time:end:044fb5c8:start=1568324525228907141,finish=1568324525231768016,duration=2860875,event=fix_etc_mavenrc[0Ktravis_time:start:28839a24[0Ktravis_time:end:28839a24:start=1568324525237350510,finish=1568324525242299882,duration=4949372,event=fix_wwdr_certificate[0Ktravis_time:start:00f185fa[0Ktravis_time:end:00f185fa:start=1568324525246231097,finish=1568324525286105764,duration=39874667,event=put_localhost_first[0Ktravis_time:start:0a92ab0c[0Ktravis_time:end:0a92ab0c:start=1568324525290338041,finish=1568324525294116203,duration=3778162,event=home_paths[0Ktravis_time:start:0a0d33de[0Ktravis_time:end:0a0d33de:start=1568324525300730965,finish=1568324525313734657,duration=13003692,event=disable_initramfs[0Ktravis_time:start:257822b8[0Ktravis_time:end:257822b8:start=1568324525319196490,finish=1568324525639540708,duration=320344218,event=disable_ssh_roaming[0Ktravis_time:start:0f02d393[0Ktravis_time:end:0f02d393:start=1568324525643842555,finish=1568324525646451722,duration=2609167,event=debug_tools[0Ktravis_time:start:0abe6f24[0Ktravis_time:end:0abe6f24:start=1568324525650636939,finish=1568324525654053322,duration=3416383,event=uninstall_oclint[0Ktravis_time:start:0df7c500[0Ktravis_time:end:0df7c500:start=1568324525658188285,finish=1568324525661483548,duration=3295263,event=rvm_use[0Ktravis_time:start:0542cab7[0Ktravis_time:end:0542cab7:start=1568324525665332373,finish=1568324525673397939,duration=8065566,event=rm_etc_boto_cfg[0Ktravis_time:start:15b5ae84[0Ktravis_time:end:15b5ae84:start=1568324525677742221,finish=1568324525680526897,duration=2784676,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1ff9e395[0Ktravis_time:end:1ff9e395:start=1568324525684660820,finish=1568324525736106574,duration=51445754,event=enable_i386[0Ktravis_time:start:18da826b[0Ktravis_time:end:18da826b:start=1568324525740210939,finish=1568324525744308254,duration=4097315,event=update_rubygems[0Ktravis_time:start:005f3f98[0Ktravis_time:end:005f3f98:start=1568324525748239668,finish=1568324526772726672,duration=1024487004,event=ensure_path_components[0Ktravis_time:start:09fd29a2[0Ktravis_time:end:09fd29a2:start=1568324526777904645,finish=1568324526780650810,duration=2746165,event=redefine_curl[0Ktravis_time:start:0fcda780[0Ktravis_time:end:0fcda780:start=1568324526785116373,finish=1568324526838604812,duration=53488439,event=nonblock_pipe[0Ktravis_time:start:2a277a1c[0Ktravis_time:end:2a277a1c:start=1568324526842882635,finish=1568324526883305468,duration=40422833,event=apt_get_update[0Ktravis_time:start:1324787d[0Ktravis_time:end:1324787d:start=1568324526888001957,finish=1568324526891066332,duration=3064375,event=deprecate_xcode_64[0Ktravis_time:start:00d5e84f[0Ktravis_time:end:00d5e84f:start=1568324526895886087,finish=1568324532273923427,duration=5378037340,event=update_heroku[0Ktravis_time:start:0bd44080[0Ktravis_time:end:0bd44080:start=1568324532278579276,finish=1568324532282231257,duration=3651981,event=shell_session_update[0Ktravis_time:start:006c2a9c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3873
travis_fold:end:docker_mtu[0Ktravis_time:end:006c2a9c:start=1568324532288104635,finish=1568324533500411965,duration=1212307330,event=set_docker_mtu[0Ktravis_time:start:1e2a9630[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1e2a9630:start=1568324533505538956,finish=1568324533583370338,duration=77831382,event=resolvconf[0Ktravis_time:start:29106224[0Ktravis_time:end:29106224:start=1568324533590294170,finish=1568324533722292146,duration=131997976,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:12e3b0d0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:12e3b0d0:start=1568324533818142919,finish=1568324534209111780,duration=390968861,event=configure[0Ktravis_time:start:15309d87[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:15309d87:start=1568324534215341691,finish=1568324544908208547,duration=10692866856,event=configure[0Ktravis_time:start:0e8ca5d5[0Ktravis_fold:start:services[0Ktravis_time:start:3c68b587[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:3c68b587:start=1568324544935825596,finish=1568324544952421789,duration=16596193,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:3c68b587:start=1568324544935825596,finish=1568324547958494895,duration=3022669299,event=services[0Ktravis_time:start:03d97dbe[0Ktravis_time:end:03d97dbe:start=1568324547962776195,finish=1568324547965452295,duration=2676100,event=fix_ps4[0Ktravis_time:start:05ae0710[0K
travis_fold:start:git.checkout[0Ktravis_time:start:02651c22[0K$ git clone --depth=50 --branch=test_install https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:02651c22:start=1568324547974588969,finish=1568324558193797335,duration=10219208366,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf d9aa1e4cf4f1a2b30461f455331976a25f5ca603
travis_fold:end:git.checkout[0K
travis_time:end:02651c22:start=1568324547974588969,finish=1568324558361771612,duration=10387182643,event=checkout[0Ktravis_time:start:1603e6eb[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1603e6eb:start=1568324558366777333,finish=1568324558379633537,duration=12856204,event=env[0Ktravis_time:start:0f9782a9[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0f9782a9:start=1568324558385856256,finish=1568324558392492420,duration=6636164,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00e79a28[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,fe-fe,bindings,dealii-of,of-ccx,su2-ccx,nutils-of,of-of_np,of-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:00e79a28:start=1568324558753284820,finish=1568324558822543288,duration=69258468,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:3c6b2c44[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584291879/log.txt)