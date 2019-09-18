 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478286) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72) 
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
travis_time:end:02773050:start=1568810129168630881,finish=1568810129175158230,duration=6527349,event=show_system_info[0Ktravis_time:start:002aa6f1[0Ktravis_time:end:002aa6f1:start=1568810129178115640,finish=1568810129208082199,duration=29966559,event=rm_riak_source[0Ktravis_time:start:17ed412e[0Ktravis_time:end:17ed412e:start=1568810129211584095,finish=1568810129217191880,duration=5607785,event=fix_rwky_redis[0Ktravis_time:start:0eacdb78[0Ktravis_time:end:0eacdb78:start=1568810129220393815,finish=1568810129632623692,duration=412229877,event=wait_for_network[0Ktravis_time:start:0989fb93[0Ktravis_time:end:0989fb93:start=1568810129638747289,finish=1568810131221332141,duration=1582584852,event=update_apt_keys[0Ktravis_time:start:2e8a7b49[0Ktravis_time:end:2e8a7b49:start=1568810131226193698,finish=1568810132312066914,duration=1085873216,event=fix_hhvm_source[0Ktravis_time:start:02851359[0Ktravis_time:end:02851359:start=1568810132316243991,finish=1568810132326363080,duration=10119089,event=update_mongo_arch[0Ktravis_time:start:2f422588[0Ktravis_time:end:2f422588:start=1568810132330669871,finish=1568810132372078798,duration=41408927,event=fix_sudo_enabled_trusty[0Ktravis_time:start:02cc5a18[0Ktravis_time:end:02cc5a18:start=1568810132376720829,finish=1568810132379783680,duration=3062851,event=update_glibc[0Ktravis_time:start:0b830b20[0Ktravis_time:end:0b830b20:start=1568810132384514195,finish=1568810132393540682,duration=9026487,event=clean_up_path[0Ktravis_time:start:08a36240[0Ktravis_time:end:08a36240:start=1568810132398360611,finish=1568810132407225411,duration=8864800,event=fix_resolv_conf[0Ktravis_time:start:2e8571a8[0Ktravis_time:end:2e8571a8:start=1568810132411073407,finish=1568810132421215610,duration=10142203,event=fix_etc_hosts[0Ktravis_time:start:082fd68c[0Ktravis_time:end:082fd68c:start=1568810132428495096,finish=1568810132438453502,duration=9958406,event=fix_mvn_settings_xml[0Ktravis_time:start:0ecff190[0Ktravis_time:end:0ecff190:start=1568810132443882269,finish=1568810132457757298,duration=13875029,event=no_ipv6_localhost[0Ktravis_time:start:0dd521b3[0Ktravis_time:end:0dd521b3:start=1568810132462599591,finish=1568810132465342486,duration=2742895,event=fix_etc_mavenrc[0Ktravis_time:start:14c730fb[0Ktravis_time:end:14c730fb:start=1568810132470292604,finish=1568810132473741167,duration=3448563,event=fix_wwdr_certificate[0Ktravis_time:start:28f4a990[0Ktravis_time:end:28f4a990:start=1568810132478409638,finish=1568810132503964154,duration=25554516,event=put_localhost_first[0Ktravis_time:start:041c58f0[0Ktravis_time:end:041c58f0:start=1568810132508651726,finish=1568810132513342694,duration=4690968,event=home_paths[0Ktravis_time:start:0faec2af[0Ktravis_time:end:0faec2af:start=1568810132518607790,finish=1568810132532405536,duration=13797746,event=disable_initramfs[0Ktravis_time:start:2451eb00[0Ktravis_time:end:2451eb00:start=1568810132537080684,finish=1568810132840165567,duration=303084883,event=disable_ssh_roaming[0Ktravis_time:start:04bd4409[0Ktravis_time:end:04bd4409:start=1568810132844685133,finish=1568810132847457145,duration=2772012,event=debug_tools[0Ktravis_time:start:0f196f35[0Ktravis_time:end:0f196f35:start=1568810132852090561,finish=1568810132856061954,duration=3971393,event=uninstall_oclint[0Ktravis_time:start:184c30dc[0Ktravis_time:end:184c30dc:start=1568810132862475821,finish=1568810132866345761,duration=3869940,event=rvm_use[0Ktravis_time:start:1b9ab8b8[0Ktravis_time:end:1b9ab8b8:start=1568810132871926061,finish=1568810132880645870,duration=8719809,event=rm_etc_boto_cfg[0Ktravis_time:start:2347f3ec[0Ktravis_time:end:2347f3ec:start=1568810132887634570,finish=1568810132890452352,duration=2817782,event=rm_oraclejdk8_symlink[0Ktravis_time:start:092f49a0[0Ktravis_time:end:092f49a0:start=1568810132895044293,finish=1568810132952749392,duration=57705099,event=enable_i386[0Ktravis_time:start:1bb6892c[0Ktravis_time:end:1bb6892c:start=1568810132957417381,finish=1568810132962086476,duration=4669095,event=update_rubygems[0Ktravis_time:start:2c3bff34[0Ktravis_time:end:2c3bff34:start=1568810132966669662,finish=1568810133997405947,duration=1030736285,event=ensure_path_components[0Ktravis_time:start:0e9a2459[0Ktravis_time:end:0e9a2459:start=1568810134002710159,finish=1568810134005615037,duration=2904878,event=redefine_curl[0Ktravis_time:start:09ff1abe[0Ktravis_time:end:09ff1abe:start=1568810134010929211,finish=1568810134070246076,duration=59316865,event=nonblock_pipe[0Ktravis_time:start:2334db00[0Ktravis_time:end:2334db00:start=1568810134074321589,finish=1568810134142336201,duration=68014612,event=apt_get_update[0Ktravis_time:start:106ebaa0[0Ktravis_time:end:106ebaa0:start=1568810134147235694,finish=1568810134150030323,duration=2794629,event=deprecate_xcode_64[0Ktravis_time:start:20a683b5[0Ktravis_time:end:20a683b5:start=1568810134154509241,finish=1568810139445612226,duration=5291102985,event=update_heroku[0Ktravis_time:start:03296200[0Ktravis_time:end:03296200:start=1568810139450031448,finish=1568810139452992796,duration=2961348,event=shell_session_update[0Ktravis_time:start:1201e921[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3931
travis_fold:end:docker_mtu[0Ktravis_time:end:1201e921:start=1568810139458064483,finish=1568810140660211562,duration=1202147079,event=set_docker_mtu[0Ktravis_time:start:008458e6[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:008458e6:start=1568810140664444183,finish=1568810140745614640,duration=81170457,event=resolvconf[0Ktravis_time:start:1e1c8a92[0Ktravis_time:end:1e1c8a92:start=1568810140752269861,finish=1568810140897788794,duration=145518933,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:01360eab[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:01360eab:start=1568810140984182847,finish=1568810141583906279,duration=599723432,event=configure[0Ktravis_time:start:04f20667[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:04f20667:start=1568810141590420510,finish=1568810152811588227,duration=11221167717,event=configure[0Ktravis_time:start:0da8cb40[0Ktravis_fold:start:services[0Ktravis_time:start:199620a8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:199620a8:start=1568810152837275345,finish=1568810152851906700,duration=14631355,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:199620a8:start=1568810152837275345,finish=1568810155858585265,duration=3021309920,event=services[0Ktravis_time:start:0f8ebca0[0Ktravis_time:end:0f8ebca0:start=1568810155864259504,finish=1568810155867131916,duration=2872412,event=fix_ps4[0Ktravis_time:start:05552262[0K
travis_fold:start:git.checkout[0Ktravis_time:start:275269f2[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:275269f2:start=1568810155876873483,finish=1568810166283663603,duration=10406790120,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:00bb5440[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:00bb5440:start=1568810166288319819,finish=1568810166744502332,duration=456182513,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:00bb5440:start=1568810166288319819,finish=1568810166985387699,duration=697067880,event=checkout[0Ktravis_time:start:04e41aec[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:04e41aec:start=1568810166990349478,finish=1568810167001590493,duration=11241015,event=env[0Ktravis_time:start:009f4082[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:009f4082:start=1568810167006115373,finish=1568810167012951852,duration=6836479,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00512796[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,su2-ccx,of-ccx_fsi,of-of_np,nutils-of,dealii-of,of-of,bindings,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:00512796:start=1568810167357357310,finish=1568810167421014947,duration=63657637,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:268f88ea[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478299/log.txt)