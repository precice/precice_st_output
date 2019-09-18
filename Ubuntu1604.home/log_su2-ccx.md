 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586479648) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/51ea4812093d...cd89b1900540) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb) 
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
travis_time:end:30b77ebc:start=1568812706185060550,finish=1568812706191533844,duration=6473294,event=show_system_info[0Ktravis_time:start:0f047094[0Ktravis_time:end:0f047094:start=1568812706194502205,finish=1568812706220264697,duration=25762492,event=rm_riak_source[0Ktravis_time:start:2f997a30[0Ktravis_time:end:2f997a30:start=1568812706223440033,finish=1568812706228831690,duration=5391657,event=fix_rwky_redis[0Ktravis_time:start:096204b4[0Ktravis_time:end:096204b4:start=1568812706231861932,finish=1568812706626942561,duration=395080629,event=wait_for_network[0Ktravis_time:start:1daa40f0[0Ktravis_time:end:1daa40f0:start=1568812706631788815,finish=1568812708229645478,duration=1597856663,event=update_apt_keys[0Ktravis_time:start:0b12247b[0Ktravis_time:end:0b12247b:start=1568812708234196367,finish=1568812709280969125,duration=1046772758,event=fix_hhvm_source[0Ktravis_time:start:12e2daf9[0Ktravis_time:end:12e2daf9:start=1568812709287203554,finish=1568812709298902466,duration=11698912,event=update_mongo_arch[0Ktravis_time:start:0626cc36[0Ktravis_time:end:0626cc36:start=1568812709304066421,finish=1568812709348428158,duration=44361737,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2e80b60d[0Ktravis_time:end:2e80b60d:start=1568812709354845809,finish=1568812709358352908,duration=3507099,event=update_glibc[0Ktravis_time:start:208a477a[0Ktravis_time:end:208a477a:start=1568812709364314597,finish=1568812709373872042,duration=9557445,event=clean_up_path[0Ktravis_time:start:10773e26[0Ktravis_time:end:10773e26:start=1568812709378728546,finish=1568812709389557668,duration=10829122,event=fix_resolv_conf[0Ktravis_time:start:2f5936bc[0Ktravis_time:end:2f5936bc:start=1568812709394141758,finish=1568812709403774352,duration=9632594,event=fix_etc_hosts[0Ktravis_time:start:0176854e[0Ktravis_time:end:0176854e:start=1568812709409065450,finish=1568812709418373467,duration=9308017,event=fix_mvn_settings_xml[0Ktravis_time:start:0100466a[0Ktravis_time:end:0100466a:start=1568812709422918794,finish=1568812709434265379,duration=11346585,event=no_ipv6_localhost[0Ktravis_time:start:08622b10[0Ktravis_time:end:08622b10:start=1568812709439965911,finish=1568812709443339668,duration=3373757,event=fix_etc_mavenrc[0Ktravis_time:start:0e57b58a[0Ktravis_time:end:0e57b58a:start=1568812709449230234,finish=1568812709453229390,duration=3999156,event=fix_wwdr_certificate[0Ktravis_time:start:121b04e3[0Ktravis_time:end:121b04e3:start=1568812709458941940,finish=1568812709487189230,duration=28247290,event=put_localhost_first[0Ktravis_time:start:0f229df4[0Ktravis_time:end:0f229df4:start=1568812709492305922,finish=1568812709498062361,duration=5756439,event=home_paths[0Ktravis_time:start:065c9f5b[0Ktravis_time:end:065c9f5b:start=1568812709503296126,finish=1568812709517229468,duration=13933342,event=disable_initramfs[0Ktravis_time:start:01178958[0Ktravis_time:end:01178958:start=1568812709522088782,finish=1568812709841298377,duration=319209595,event=disable_ssh_roaming[0Ktravis_time:start:38f4d558[0Ktravis_time:end:38f4d558:start=1568812709846675026,finish=1568812709850942565,duration=4267539,event=debug_tools[0Ktravis_time:start:111bdbaa[0Ktravis_time:end:111bdbaa:start=1568812709856427145,finish=1568812709860397466,duration=3970321,event=uninstall_oclint[0Ktravis_time:start:071dbe10[0Ktravis_time:end:071dbe10:start=1568812709865848335,finish=1568812709869703599,duration=3855264,event=rvm_use[0Ktravis_time:start:2f5d57b2[0Ktravis_time:end:2f5d57b2:start=1568812709877991295,finish=1568812709887290359,duration=9299064,event=rm_etc_boto_cfg[0Ktravis_time:start:0dbeb64c[0Ktravis_time:end:0dbeb64c:start=1568812709892191662,finish=1568812709895207232,duration=3015570,event=rm_oraclejdk8_symlink[0Ktravis_time:start:08f06bbe[0Ktravis_time:end:08f06bbe:start=1568812709900917506,finish=1568812709959332039,duration=58414533,event=enable_i386[0Ktravis_time:start:23a891cf[0Ktravis_time:end:23a891cf:start=1568812709963735754,finish=1568812709968300115,duration=4564361,event=update_rubygems[0Ktravis_time:start:0033c810[0Ktravis_time:end:0033c810:start=1568812709972787835,finish=1568812710989673582,duration=1016885747,event=ensure_path_components[0Ktravis_time:start:0de39028[0Ktravis_time:end:0de39028:start=1568812710994623773,finish=1568812710997665893,duration=3042120,event=redefine_curl[0Ktravis_time:start:12456fec[0Ktravis_time:end:12456fec:start=1568812711002536649,finish=1568812711056799782,duration=54263133,event=nonblock_pipe[0Ktravis_time:start:24374a9b[0Ktravis_time:end:24374a9b:start=1568812711061609947,finish=1568812711104154497,duration=42544550,event=apt_get_update[0Ktravis_time:start:125e9cf8[0Ktravis_time:end:125e9cf8:start=1568812711108899467,finish=1568812711112137281,duration=3237814,event=deprecate_xcode_64[0Ktravis_time:start:0d503be8[0Ktravis_time:end:0d503be8:start=1568812711116515179,finish=1568812716010632311,duration=4894117132,event=update_heroku[0Ktravis_time:start:1bc9002c[0Ktravis_time:end:1bc9002c:start=1568812716016099762,finish=1568812716019326728,duration=3226966,event=shell_session_update[0Ktravis_time:start:05e8488d[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3876
travis_fold:end:docker_mtu[0Ktravis_time:end:05e8488d:start=1568812716024249032,finish=1568812717228852618,duration=1204603586,event=set_docker_mtu[0Ktravis_time:start:09a7640e[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:09a7640e:start=1568812717233548474,finish=1568812717301599449,duration=68050975,event=resolvconf[0Ktravis_time:start:0d72665b[0Ktravis_time:end:0d72665b:start=1568812717306194417,finish=1568812717416627158,duration=110432741,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:128b18a0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:128b18a0:start=1568812717499806568,finish=1568812718009607962,duration=509801394,event=configure[0Ktravis_time:start:06e21a98[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:06e21a98:start=1568812718015025377,finish=1568812729178335867,duration=11163310490,event=configure[0Ktravis_time:start:0f2f01b4[0Ktravis_fold:start:services[0Ktravis_time:start:06e4cfa0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06e4cfa0:start=1568812729205758868,finish=1568812729222819761,duration=17060893,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06e4cfa0:start=1568812729205758868,finish=1568812732228647494,duration=3022888626,event=services[0Ktravis_time:start:038941ec[0Ktravis_time:end:038941ec:start=1568812732233225926,finish=1568812732235960924,duration=2734998,event=fix_ps4[0Ktravis_time:start:365f993e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:000e49b8[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:000e49b8:start=1568812732245734634,finish=1568812742559112330,duration=10313377696,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf cd89b1900540505af8c571183bfc09ad56bacb7b
travis_fold:end:git.checkout[0K
travis_time:end:000e49b8:start=1568812732245734634,finish=1568812743046593784,duration=10800859150,event=checkout[0Ktravis_time:start:139df432[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:139df432:start=1568812743051998932,finish=1568812743063911662,duration=11912730,event=env[0Ktravis_time:start:2692ba00[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2692ba00:start=1568812743069452661,finish=1568812743078372491,duration=8919830,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:18ad6af9[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {nutils-of,of-of,of-of_np,fe-fe,su2-ccx,of-ccx,of-ccx_fsi,bindings,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:18ad6af9:start=1568812743439136404,finish=1568812743504439680,duration=65303276,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:08c05be0[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586479672/log.txt)