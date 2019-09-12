 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584291854) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aabfec63ba1b...d9aa1e4cf4f1) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
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
travis_time:end:0fb77ab5:start=1568324205918751758,finish=1568324205927336666,duration=8584908,event=show_system_info[0Ktravis_time:start:107b2952[0Ktravis_time:end:107b2952:start=1568324205931434460,finish=1568324205962728471,duration=31294011,event=rm_riak_source[0Ktravis_time:start:1dddfa14[0Ktravis_time:end:1dddfa14:start=1568324205967192665,finish=1568324205974424315,duration=7231650,event=fix_rwky_redis[0Ktravis_time:start:12b97bda[0Ktravis_time:end:12b97bda:start=1568324205978443949,finish=1568324206401894013,duration=423450064,event=wait_for_network[0Ktravis_time:start:06c8d238[0Ktravis_time:end:06c8d238:start=1568324206406950913,finish=1568324208039859751,duration=1632908838,event=update_apt_keys[0Ktravis_time:start:0f8f651a[0Ktravis_time:end:0f8f651a:start=1568324208044805533,finish=1568324209216407208,duration=1171601675,event=fix_hhvm_source[0Ktravis_time:start:025176b5[0Ktravis_time:end:025176b5:start=1568324209221944689,finish=1568324209234431313,duration=12486624,event=update_mongo_arch[0Ktravis_time:start:06e9d878[0Ktravis_time:end:06e9d878:start=1568324209239559157,finish=1568324209290617811,duration=51058654,event=fix_sudo_enabled_trusty[0Ktravis_time:start:15b9f3f0[0Ktravis_time:end:15b9f3f0:start=1568324209296070068,finish=1568324209299406693,duration=3336625,event=update_glibc[0Ktravis_time:start:045a0c8a[0Ktravis_time:end:045a0c8a:start=1568324209304489798,finish=1568324209319044552,duration=14554754,event=clean_up_path[0Ktravis_time:start:00f9ef97[0Ktravis_time:end:00f9ef97:start=1568324209323955216,finish=1568324209336687904,duration=12732688,event=fix_resolv_conf[0Ktravis_time:start:1a8b6ee0[0Ktravis_time:end:1a8b6ee0:start=1568324209342062777,finish=1568324209358546743,duration=16483966,event=fix_etc_hosts[0Ktravis_time:start:14415bd0[0Ktravis_time:end:14415bd0:start=1568324209366162192,finish=1568324209379770002,duration=13607810,event=fix_mvn_settings_xml[0Ktravis_time:start:07a59ae5[0Ktravis_time:end:07a59ae5:start=1568324209385734289,finish=1568324209402837899,duration=17103610,event=no_ipv6_localhost[0Ktravis_time:start:01c3bdd8[0Ktravis_time:end:01c3bdd8:start=1568324209409517296,finish=1568324209413052060,duration=3534764,event=fix_etc_mavenrc[0Ktravis_time:start:03f2a700[0Ktravis_time:end:03f2a700:start=1568324209420179456,finish=1568324209425728595,duration=5549139,event=fix_wwdr_certificate[0Ktravis_time:start:23da57aa[0Ktravis_time:end:23da57aa:start=1568324209432186687,finish=1568324209465207492,duration=33020805,event=put_localhost_first[0Ktravis_time:start:19d62d34[0Ktravis_time:end:19d62d34:start=1568324209470493989,finish=1568324209474445833,duration=3951844,event=home_paths[0Ktravis_time:start:263ffbb0[0Ktravis_time:end:263ffbb0:start=1568324209479559135,finish=1568324209495309217,duration=15750082,event=disable_initramfs[0Ktravis_time:start:0f983cb2[0Ktravis_time:end:0f983cb2:start=1568324209501089471,finish=1568324209850710895,duration=349621424,event=disable_ssh_roaming[0Ktravis_time:start:02675dc0[0Ktravis_time:end:02675dc0:start=1568324209856158596,finish=1568324209859287342,duration=3128746,event=debug_tools[0Ktravis_time:start:0731fa46[0Ktravis_time:end:0731fa46:start=1568324209864487598,finish=1568324209868323372,duration=3835774,event=uninstall_oclint[0Ktravis_time:start:29b4c1cc[0Ktravis_time:end:29b4c1cc:start=1568324209873397535,finish=1568324209877123630,duration=3726095,event=rvm_use[0Ktravis_time:start:0c26cd87[0Ktravis_time:end:0c26cd87:start=1568324209881679620,finish=1568324209891790751,duration=10111131,event=rm_etc_boto_cfg[0Ktravis_time:start:030b5970[0Ktravis_time:end:030b5970:start=1568324209898046694,finish=1568324209900919442,duration=2872748,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0a78c4f4[0Ktravis_time:end:0a78c4f4:start=1568324209907448499,finish=1568324209975981073,duration=68532574,event=enable_i386[0Ktravis_time:start:11cb17d2[0Ktravis_time:end:11cb17d2:start=1568324209981133287,finish=1568324209986361841,duration=5228554,event=update_rubygems[0Ktravis_time:start:1308fda4[0Ktravis_time:end:1308fda4:start=1568324209993269999,finish=1568324211132821546,duration=1139551547,event=ensure_path_components[0Ktravis_time:start:09d6fdf0[0Ktravis_time:end:09d6fdf0:start=1568324211138247697,finish=1568324211142024144,duration=3776447,event=redefine_curl[0Ktravis_time:start:29c05ce0[0Ktravis_time:end:29c05ce0:start=1568324211147380745,finish=1568324211211504169,duration=64123424,event=nonblock_pipe[0Ktravis_time:start:1103e12c[0Ktravis_time:end:1103e12c:start=1568324211218807186,finish=1568324211277713477,duration=58906291,event=apt_get_update[0Ktravis_time:start:0cf840ee[0Ktravis_time:end:0cf840ee:start=1568324211282830028,finish=1568324211285894641,duration=3064613,event=deprecate_xcode_64[0Ktravis_time:start:123fa248[0Ktravis_time:end:123fa248:start=1568324211290537903,finish=1568324216866357803,duration=5575819900,event=update_heroku[0Ktravis_time:start:0fa9d540[0Ktravis_time:end:0fa9d540:start=1568324216871592015,finish=1568324216875109995,duration=3517980,event=shell_session_update[0Ktravis_time:start:16992dc7[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3935
travis_fold:end:docker_mtu[0Ktravis_time:end:16992dc7:start=1568324216880615351,finish=1568324218092009934,duration=1211394583,event=set_docker_mtu[0Ktravis_time:start:09cf8519[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:09cf8519:start=1568324218098155833,finish=1568324218173765190,duration=75609357,event=resolvconf[0Ktravis_time:start:13cd3208[0Ktravis_time:end:13cd3208:start=1568324218178884384,finish=1568324218334376151,duration=155491767,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:08235e85[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:08235e85:start=1568324218428977059,finish=1568324218827848404,duration=398871345,event=configure[0Ktravis_time:start:0cf0616e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0cf0616e:start=1568324218833799989,finish=1568324232620043109,duration=13786243120,event=configure[0Ktravis_time:start:2b10bffa[0Ktravis_fold:start:services[0Ktravis_time:start:0759bc6a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0759bc6a:start=1568324232647208058,finish=1568324232663976194,duration=16768136,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0759bc6a:start=1568324232647208058,finish=1568324235670158119,duration=3022950061,event=services[0Ktravis_time:start:00803d42[0Ktravis_time:end:00803d42:start=1568324235675258851,finish=1568324235678109919,duration=2851068,event=fix_ps4[0Ktravis_time:start:11b4123b[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1495e816[0K$ git clone --depth=50 --branch=test_install https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1495e816:start=1568324235688343355,finish=1568324247509314167,duration=11820970812,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf d9aa1e4cf4f1a2b30461f455331976a25f5ca603
travis_fold:end:git.checkout[0K
travis_time:end:1495e816:start=1568324235688343355,finish=1568324247945681620,duration=12257338265,event=checkout[0Ktravis_time:start:209f1ac8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:209f1ac8:start=1568324247951268788,finish=1568324247963756665,duration=12487877,event=env[0Ktravis_time:start:1c227ca0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1c227ca0:start=1568324247968697754,finish=1568324247976093371,duration=7395617,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:10919a00[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,nutils-of,of-of_np,bindings,of-ccx,of-of,su2-ccx,of-ccx_fsi,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:10919a00:start=1568324248390619328,finish=1568324248461586458,duration=70967130,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:153d2c84[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584291874/log.txt)