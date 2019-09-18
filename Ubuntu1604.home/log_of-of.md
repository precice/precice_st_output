 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586518622) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/98) 
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
travis_time:end:07756b60:start=1568824339810040073,finish=1568824339816460076,duration=6420003,event=show_system_info[0Ktravis_time:start:16cb8a4e[0Ktravis_time:end:16cb8a4e:start=1568824339819420894,finish=1568824339845238264,duration=25817370,event=rm_riak_source[0Ktravis_time:start:06963894[0Ktravis_time:end:06963894:start=1568824339848409874,finish=1568824339853520655,duration=5110781,event=fix_rwky_redis[0Ktravis_time:start:0fa68366[0Ktravis_time:end:0fa68366:start=1568824339856403906,finish=1568824340280885772,duration=424481866,event=wait_for_network[0Ktravis_time:start:053c11c8[0Ktravis_time:end:053c11c8:start=1568824340295515965,finish=1568824348076593561,duration=7781077596,event=update_apt_keys[0Ktravis_time:start:1a6690e9[0Ktravis_time:end:1a6690e9:start=1568824348080726929,finish=1568824349170295871,duration=1089568942,event=fix_hhvm_source[0Ktravis_time:start:12587432[0Ktravis_time:end:12587432:start=1568824349175339199,finish=1568824349186111171,duration=10771972,event=update_mongo_arch[0Ktravis_time:start:118887f6[0Ktravis_time:end:118887f6:start=1568824349191634208,finish=1568824349234748489,duration=43114281,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0617c0c7[0Ktravis_time:end:0617c0c7:start=1568824349239127263,finish=1568824349241932593,duration=2805330,event=update_glibc[0Ktravis_time:start:0882d61f[0Ktravis_time:end:0882d61f:start=1568824349245958714,finish=1568824349255302174,duration=9343460,event=clean_up_path[0Ktravis_time:start:0be3f53c[0Ktravis_time:end:0be3f53c:start=1568824349259279476,finish=1568824349267689754,duration=8410278,event=fix_resolv_conf[0Ktravis_time:start:0c6fc232[0Ktravis_time:end:0c6fc232:start=1568824349272380595,finish=1568824349282764061,duration=10383466,event=fix_etc_hosts[0Ktravis_time:start:1bddd270[0Ktravis_time:end:1bddd270:start=1568824349287377978,finish=1568824349298018463,duration=10640485,event=fix_mvn_settings_xml[0Ktravis_time:start:1c2fb49f[0Ktravis_time:end:1c2fb49f:start=1568824349303294386,finish=1568824349313987325,duration=10692939,event=no_ipv6_localhost[0Ktravis_time:start:36443cbc[0Ktravis_time:end:36443cbc:start=1568824349320742809,finish=1568824349323936126,duration=3193317,event=fix_etc_mavenrc[0Ktravis_time:start:0039eefb[0Ktravis_time:end:0039eefb:start=1568824349329201438,finish=1568824349332736843,duration=3535405,event=fix_wwdr_certificate[0Ktravis_time:start:1eb3b442[0Ktravis_time:end:1eb3b442:start=1568824349340194343,finish=1568824349365039706,duration=24845363,event=put_localhost_first[0Ktravis_time:start:0580a41e[0Ktravis_time:end:0580a41e:start=1568824349369638033,finish=1568824349373630286,duration=3992253,event=home_paths[0Ktravis_time:start:0af80f8e[0Ktravis_time:end:0af80f8e:start=1568824349378664272,finish=1568824349392754635,duration=14090363,event=disable_initramfs[0Ktravis_time:start:01762879[0Ktravis_time:end:01762879:start=1568824349397560807,finish=1568824349737149404,duration=339588597,event=disable_ssh_roaming[0Ktravis_time:start:037cdafa[0Ktravis_time:end:037cdafa:start=1568824349741945116,finish=1568824349745049605,duration=3104489,event=debug_tools[0Ktravis_time:start:01b521fc[0Ktravis_time:end:01b521fc:start=1568824349749755672,finish=1568824349753615725,duration=3860053,event=uninstall_oclint[0Ktravis_time:start:03dfbdb9[0Ktravis_time:end:03dfbdb9:start=1568824349758300738,finish=1568824349762139761,duration=3839023,event=rvm_use[0Ktravis_time:start:04a3b29c[0Ktravis_time:end:04a3b29c:start=1568824349767011551,finish=1568824349775391657,duration=8380106,event=rm_etc_boto_cfg[0Ktravis_time:start:12f37157[0Ktravis_time:end:12f37157:start=1568824349779904104,finish=1568824349782725393,duration=2821289,event=rm_oraclejdk8_symlink[0Ktravis_time:start:133b495e[0Ktravis_time:end:133b495e:start=1568824349787957401,finish=1568824349841299972,duration=53342571,event=enable_i386[0Ktravis_time:start:152d3d84[0Ktravis_time:end:152d3d84:start=1568824349846955663,finish=1568824349852765517,duration=5809854,event=update_rubygems[0Ktravis_time:start:01a0ce38[0Ktravis_time:end:01a0ce38:start=1568824349859024733,finish=1568824350900162131,duration=1041137398,event=ensure_path_components[0Ktravis_time:start:0dca75ee[0Ktravis_time:end:0dca75ee:start=1568824350905624666,finish=1568824350908506726,duration=2882060,event=redefine_curl[0Ktravis_time:start:04593fe8[0Ktravis_time:end:04593fe8:start=1568824350913009949,finish=1568824350969672016,duration=56662067,event=nonblock_pipe[0Ktravis_time:start:2b4910bf[0Ktravis_time:end:2b4910bf:start=1568824350974888244,finish=1568824351042470608,duration=67582364,event=apt_get_update[0Ktravis_time:start:048f30ba[0Ktravis_time:end:048f30ba:start=1568824351046863493,finish=1568824351049613166,duration=2749673,event=deprecate_xcode_64[0Ktravis_time:start:063ca800[0Ktravis_time:end:063ca800:start=1568824351053386636,finish=1568824356134036735,duration=5080650099,event=update_heroku[0Ktravis_time:start:07fa7bac[0Ktravis_time:end:07fa7bac:start=1568824356138261326,finish=1568824356141311234,duration=3049908,event=shell_session_update[0Ktravis_time:start:017cb577[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3862
travis_fold:end:docker_mtu[0Ktravis_time:end:017cb577:start=1568824356145293262,finish=1568824357348966494,duration=1203673232,event=set_docker_mtu[0Ktravis_time:start:03ba0866[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03ba0866:start=1568824357353540460,finish=1568824357423819738,duration=70279278,event=resolvconf[0Ktravis_time:start:02165060[0Ktravis_time:end:02165060:start=1568824357428658270,finish=1568824357539343451,duration=110685181,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:115a0d5e[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:115a0d5e:start=1568824357627311253,finish=1568824358053343351,duration=426032098,event=configure[0Ktravis_time:start:02c7f7a8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02c7f7a8:start=1568824358059145943,finish=1568824369250452828,duration=11191306885,event=configure[0Ktravis_time:start:0835f79e[0Ktravis_fold:start:services[0Ktravis_time:start:0b0cba7f[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0b0cba7f:start=1568824369277941710,finish=1568824369293821829,duration=15880119,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0b0cba7f:start=1568824369277941710,finish=1568824372299578315,duration=3021636605,event=services[0Ktravis_time:start:04bc1f38[0Ktravis_time:end:04bc1f38:start=1568824372304527064,finish=1568824372307530997,duration=3003933,event=fix_ps4[0Ktravis_time:start:0c8ab505[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0ae32d78[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0ae32d78:start=1568824372317114897,finish=1568824382629047431,duration=10311932534,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:050fd9a8[0K$ git fetch origin +refs/pull/98/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/98/merge -> FETCH_HEAD
travis_time:end:050fd9a8:start=1568824382633448264,finish=1568824383173412589,duration=539964325,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:050fd9a8:start=1568824382633448264,finish=1568824383742112045,duration=1108663781,event=checkout[0Ktravis_time:start:08a26f86[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:08a26f86:start=1568824383746513550,finish=1568824383763144483,duration=16630933,event=env[0Ktravis_time:start:254618b0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:254618b0:start=1568824383769271323,finish=1568824383775689510,duration=6418187,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1666bbea[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {of-ccx,of-of_np,dealii-of,of-ccx_fsi,nutils-of,bindings,fe-fe,su2-ccx,of-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:1666bbea:start=1568824384150906351,finish=1568824384220062910,duration=69156559,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:04e4ba2e[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586518636/log.txt)