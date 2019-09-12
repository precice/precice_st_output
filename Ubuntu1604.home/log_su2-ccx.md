 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584291854) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aabfec63ba1b...d9aa1e4cf4f1) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb) 
## Last 100 lines of the job log at the moment of push...
```
 [34m[1mInstalled Firefox version[0m
firefox 56.0.2
[34m[1mMongoDB version[0m
MongoDB 3.4.10
[34m[1mPhantomJS version[0m
2.1.1
[34m[1mPre-installed PostgreSQL versions[0m
9.2.24
9.3.20
9.4.15
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
travis_time:end:0f2bb613:start=1568324027892440031,finish=1568324027898650496,duration=6210465,event=show_system_info[0Ktravis_time:start:22982538[0Ktravis_time:end:22982538:start=1568324027901512856,finish=1568324027930862832,duration=29349976,event=rm_riak_source[0Ktravis_time:start:0b0c09b8[0Ktravis_time:end:0b0c09b8:start=1568324027934110353,finish=1568324027939505328,duration=5394975,event=fix_rwky_redis[0Ktravis_time:start:0d586898[0Ktravis_time:end:0d586898:start=1568324027942481368,finish=1568324028336117836,duration=393636468,event=wait_for_network[0Ktravis_time:start:11308219[0Ktravis_time:end:11308219:start=1568324028345968672,finish=1568324029913149350,duration=1567180678,event=update_apt_keys[0Ktravis_time:start:06da9659[0Ktravis_time:end:06da9659:start=1568324029917728087,finish=1568324030989508499,duration=1071780412,event=fix_hhvm_source[0Ktravis_time:start:0b15fd14[0Ktravis_time:end:0b15fd14:start=1568324030994436091,finish=1568324031005334941,duration=10898850,event=update_mongo_arch[0Ktravis_time:start:17ac1cc0[0Ktravis_time:end:17ac1cc0:start=1568324031009871494,finish=1568324031054938286,duration=45066792,event=fix_sudo_enabled_trusty[0Ktravis_time:start:00fe7c9f[0Ktravis_time:end:00fe7c9f:start=1568324031059786434,finish=1568324031062688501,duration=2902067,event=update_glibc[0Ktravis_time:start:02c2fda8[0Ktravis_time:end:02c2fda8:start=1568324031066890530,finish=1568324031075562015,duration=8671485,event=clean_up_path[0Ktravis_time:start:12ef40b3[0Ktravis_time:end:12ef40b3:start=1568324031080612076,finish=1568324031089344895,duration=8732819,event=fix_resolv_conf[0Ktravis_time:start:03f141c4[0Ktravis_time:end:03f141c4:start=1568324031093801838,finish=1568324031103881766,duration=10079928,event=fix_etc_hosts[0Ktravis_time:start:03e89d3c[0Ktravis_time:end:03e89d3c:start=1568324031108106730,finish=1568324031117262144,duration=9155414,event=fix_mvn_settings_xml[0Ktravis_time:start:279f87ca[0Ktravis_time:end:279f87ca:start=1568324031122020808,finish=1568324031132022622,duration=10001814,event=no_ipv6_localhost[0Ktravis_time:start:013b80be[0Ktravis_time:end:013b80be:start=1568324031137299785,finish=1568324031142456200,duration=5156415,event=fix_etc_mavenrc[0Ktravis_time:start:02ed8ab2[0Ktravis_time:end:02ed8ab2:start=1568324031146992663,finish=1568324031150587184,duration=3594521,event=fix_wwdr_certificate[0Ktravis_time:start:193f5123[0Ktravis_time:end:193f5123:start=1568324031154950295,finish=1568324031179806210,duration=24855915,event=put_localhost_first[0Ktravis_time:start:1ea49e74[0Ktravis_time:end:1ea49e74:start=1568324031184307180,finish=1568324031190159566,duration=5852386,event=home_paths[0Ktravis_time:start:240fbc6a[0Ktravis_time:end:240fbc6a:start=1568324031194433982,finish=1568324031207199120,duration=12765138,event=disable_initramfs[0Ktravis_time:start:1e99f6e7[0Ktravis_time:end:1e99f6e7:start=1568324031212231889,finish=1568324031579150770,duration=366918881,event=disable_ssh_roaming[0Ktravis_time:start:20714eca[0Ktravis_time:end:20714eca:start=1568324031583754152,finish=1568324031586555915,duration=2801763,event=debug_tools[0Ktravis_time:start:22600e01[0Ktravis_time:end:22600e01:start=1568324031591066447,finish=1568324031594670289,duration=3603842,event=uninstall_oclint[0Ktravis_time:start:16875788[0Ktravis_time:end:16875788:start=1568324031599380764,finish=1568324031602814431,duration=3433667,event=rvm_use[0Ktravis_time:start:0ff14039[0Ktravis_time:end:0ff14039:start=1568324031606966747,finish=1568324031615157632,duration=8190885,event=rm_etc_boto_cfg[0Ktravis_time:start:011b2f80[0Ktravis_time:end:011b2f80:start=1568324031620554366,finish=1568324031623510626,duration=2956260,event=rm_oraclejdk8_symlink[0Ktravis_time:start:00518b00[0Ktravis_time:end:00518b00:start=1568324031627766696,finish=1568324031686267227,duration=58500531,event=enable_i386[0Ktravis_time:start:00d53170[0Ktravis_time:end:00d53170:start=1568324031691154994,finish=1568324031696203132,duration=5048138,event=update_rubygems[0Ktravis_time:start:018df530[0Ktravis_time:end:018df530:start=1568324031700974621,finish=1568324032741326863,duration=1040352242,event=ensure_path_components[0Ktravis_time:start:000ace22[0Ktravis_time:end:000ace22:start=1568324032746556563,finish=1568324032749886580,duration=3330017,event=redefine_curl[0Ktravis_time:start:0005da26[0Ktravis_time:end:0005da26:start=1568324032756208001,finish=1568324032815452482,duration=59244481,event=nonblock_pipe[0Ktravis_time:start:00491c5f[0Ktravis_time:end:00491c5f:start=1568324032820151424,finish=1568324032890082277,duration=69930853,event=apt_get_update[0Ktravis_time:start:31c545b0[0Ktravis_time:end:31c545b0:start=1568324032894724954,finish=1568324032898203267,duration=3478313,event=deprecate_xcode_64[0Ktravis_time:start:08b5bfbc[0Ktravis_time:end:08b5bfbc:start=1568324032902790885,finish=1568324037965332107,duration=5062541222,event=update_heroku[0Ktravis_time:start:0c6cc1cc[0Ktravis_time:end:0c6cc1cc:start=1568324037969931285,finish=1568324037973118325,duration=3187040,event=shell_session_update[0Ktravis_time:start:0ed3e05f[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3830
travis_fold:end:docker_mtu[0Ktravis_time:end:0ed3e05f:start=1568324037977070738,finish=1568324039174829992,duration=1197759254,event=set_docker_mtu[0Ktravis_time:start:042fbfa1[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:042fbfa1:start=1568324039179686634,finish=1568324039248515887,duration=68829253,event=resolvconf[0Ktravis_time:start:03e8db9c[0Ktravis_time:end:03e8db9c:start=1568324039253886628,finish=1568324039355241210,duration=101354582,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1b4e477f[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1b4e477f:start=1568324039438496592,finish=1568324039851711003,duration=413214411,event=configure[0Ktravis_time:start:138bcad7[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:138bcad7:start=1568324039857150320,finish=1568324050568933854,duration=10711783534,event=configure[0Ktravis_time:start:15b992f8[0Ktravis_fold:start:services[0Ktravis_time:start:2cb4bd48[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:2cb4bd48:start=1568324050595807835,finish=1568324050612994628,duration=17186793,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2cb4bd48:start=1568324050595807835,finish=1568324053619995196,duration=3024187361,event=services[0Ktravis_time:start:196bffd0[0Ktravis_time:end:196bffd0:start=1568324053625168093,finish=1568324053628400722,duration=3232629,event=fix_ps4[0Ktravis_time:start:2313db10[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00987974[0K$ git clone --depth=50 --branch=test_install https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00987974:start=1568324053637933278,finish=1568324063687823483,duration=10049890205,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf d9aa1e4cf4f1a2b30461f455331976a25f5ca603
travis_fold:end:git.checkout[0K
travis_time:end:00987974:start=1568324053637933278,finish=1568324064270692500,duration=10632759222,event=checkout[0Ktravis_time:start:002ae4c8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:002ae4c8:start=1568324064276606271,finish=1568324064287542127,duration=10935856,event=env[0Ktravis_time:start:07a930a0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:07a930a0:start=1568324064296829990,finish=1568324064302989000,duration=6159010,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:04c0923a[0K$ python system_testing.py -s su2-ccx
 ```
[Full job log](https://api.travis-ci.org/v3/job/584291872/log.txt)