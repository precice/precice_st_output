 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584291854) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aabfec63ba1b...d9aa1e4cf4f1) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
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
travis_time:end:33df167f:start=1568324476497289290,finish=1568324476504077585,duration=6788295,event=show_system_info[0Ktravis_time:start:080df51d[0Ktravis_time:end:080df51d:start=1568324476507437620,finish=1568324476533530174,duration=26092554,event=rm_riak_source[0Ktravis_time:start:070abfb6[0Ktravis_time:end:070abfb6:start=1568324476537091818,finish=1568324476542696430,duration=5604612,event=fix_rwky_redis[0Ktravis_time:start:017ea970[0Ktravis_time:end:017ea970:start=1568324476545934335,finish=1568324476958335681,duration=412401346,event=wait_for_network[0Ktravis_time:start:2bcdf660[0Ktravis_time:end:2bcdf660:start=1568324476963683369,finish=1568324477902100180,duration=938416811,event=update_apt_keys[0Ktravis_time:start:158f07c7[0Ktravis_time:end:158f07c7:start=1568324477907871711,finish=1568324479000015070,duration=1092143359,event=fix_hhvm_source[0Ktravis_time:start:2b6d542a[0Ktravis_time:end:2b6d542a:start=1568324479004962775,finish=1568324479015394500,duration=10431725,event=update_mongo_arch[0Ktravis_time:start:12e97859[0Ktravis_time:end:12e97859:start=1568324479021348327,finish=1568324479065158328,duration=43810001,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1bde3c58[0Ktravis_time:end:1bde3c58:start=1568324479070640073,finish=1568324479074066892,duration=3426819,event=update_glibc[0Ktravis_time:start:273734fa[0Ktravis_time:end:273734fa:start=1568324479078817310,finish=1568324479089198795,duration=10381485,event=clean_up_path[0Ktravis_time:start:1d11b83b[0Ktravis_time:end:1d11b83b:start=1568324479093565121,finish=1568324479102447649,duration=8882528,event=fix_resolv_conf[0Ktravis_time:start:05ff5de4[0Ktravis_time:end:05ff5de4:start=1568324479107690369,finish=1568324479117769874,duration=10079505,event=fix_etc_hosts[0Ktravis_time:start:3e027a68[0Ktravis_time:end:3e027a68:start=1568324479124173074,finish=1568324479134545987,duration=10372913,event=fix_mvn_settings_xml[0Ktravis_time:start:0691d280[0Ktravis_time:end:0691d280:start=1568324479141508291,finish=1568324479152305804,duration=10797513,event=no_ipv6_localhost[0Ktravis_time:start:1ebda854[0Ktravis_time:end:1ebda854:start=1568324479159402838,finish=1568324479162361733,duration=2958895,event=fix_etc_mavenrc[0Ktravis_time:start:09142404[0Ktravis_time:end:09142404:start=1568324479167421919,finish=1568324479171362265,duration=3940346,event=fix_wwdr_certificate[0Ktravis_time:start:24d1d070[0Ktravis_time:end:24d1d070:start=1568324479175903561,finish=1568324479204180560,duration=28276999,event=put_localhost_first[0Ktravis_time:start:2af36526[0Ktravis_time:end:2af36526:start=1568324479209024604,finish=1568324479213510836,duration=4486232,event=home_paths[0Ktravis_time:start:095884f1[0Ktravis_time:end:095884f1:start=1568324479218121798,finish=1568324479231960120,duration=13838322,event=disable_initramfs[0Ktravis_time:start:0de83ac0[0Ktravis_time:end:0de83ac0:start=1568324479236584374,finish=1568324479552242994,duration=315658620,event=disable_ssh_roaming[0Ktravis_time:start:37902bb8[0Ktravis_time:end:37902bb8:start=1568324479558502949,finish=1568324479561784773,duration=3281824,event=debug_tools[0Ktravis_time:start:06830037[0Ktravis_time:end:06830037:start=1568324479565716115,finish=1568324479569894572,duration=4178457,event=uninstall_oclint[0Ktravis_time:start:2af8b86c[0Ktravis_time:end:2af8b86c:start=1568324479573942192,finish=1568324479578481499,duration=4539307,event=rvm_use[0Ktravis_time:start:064aef68[0Ktravis_time:end:064aef68:start=1568324479585284354,finish=1568324479594784503,duration=9500149,event=rm_etc_boto_cfg[0Ktravis_time:start:004c673e[0Ktravis_time:end:004c673e:start=1568324479599408588,finish=1568324479602480755,duration=3072167,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1ed53995[0Ktravis_time:end:1ed53995:start=1568324479608226572,finish=1568324479663414238,duration=55187666,event=enable_i386[0Ktravis_time:start:02fbb5c4[0Ktravis_time:end:02fbb5c4:start=1568324479668429167,finish=1568324479673772318,duration=5343151,event=update_rubygems[0Ktravis_time:start:02a45d74[0Ktravis_time:end:02a45d74:start=1568324479678757333,finish=1568324480735728940,duration=1056971607,event=ensure_path_components[0Ktravis_time:start:16bb975d[0Ktravis_time:end:16bb975d:start=1568324480741386744,finish=1568324480744606709,duration=3219965,event=redefine_curl[0Ktravis_time:start:23eceb22[0Ktravis_time:end:23eceb22:start=1568324480749558404,finish=1568324480811312458,duration=61754054,event=nonblock_pipe[0Ktravis_time:start:1056dfc2[0Ktravis_time:end:1056dfc2:start=1568324480815976708,finish=1568324480870213801,duration=54237093,event=apt_get_update[0Ktravis_time:start:204884b1[0Ktravis_time:end:204884b1:start=1568324480875981448,finish=1568324480879705038,duration=3723590,event=deprecate_xcode_64[0Ktravis_time:start:023b6263[0Ktravis_time:end:023b6263:start=1568324480884709760,finish=1568324485924792424,duration=5040082664,event=update_heroku[0Ktravis_time:start:165e6dd5[0Ktravis_time:end:165e6dd5:start=1568324485929947381,finish=1568324485934106656,duration=4159275,event=shell_session_update[0Ktravis_time:start:04158fa6[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3831
travis_fold:end:docker_mtu[0Ktravis_time:end:04158fa6:start=1568324485939172696,finish=1568324487138200786,duration=1199028090,event=set_docker_mtu[0Ktravis_time:start:17cedcc5[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:17cedcc5:start=1568324487143824303,finish=1568324487218209224,duration=74384921,event=resolvconf[0Ktravis_time:start:0758aa6e[0Ktravis_time:end:0758aa6e:start=1568324487223796065,finish=1568324487347041858,duration=123245793,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2c19b71b[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2c19b71b:start=1568324487438963695,finish=1568324487960940879,duration=521977184,event=configure[0Ktravis_time:start:1ff9b59e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1ff9b59e:start=1568324487967222366,finish=1568324500456277432,duration=12489055066,event=configure[0Ktravis_time:start:08fb5c6d[0Ktravis_fold:start:services[0Ktravis_time:start:06f80d30[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06f80d30:start=1568324500483994689,finish=1568324500499474544,duration=15479855,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06f80d30:start=1568324500483994689,finish=1568324503505728441,duration=3021733752,event=services[0Ktravis_time:start:019cb16a[0Ktravis_time:end:019cb16a:start=1568324503510540160,finish=1568324503513544521,duration=3004361,event=fix_ps4[0Ktravis_time:start:0d4277a0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:18b140f0[0K$ git clone --depth=50 --branch=test_install https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:18b140f0:start=1568324503523061166,finish=1568324514209648801,duration=10686587635,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf d9aa1e4cf4f1a2b30461f455331976a25f5ca603
travis_fold:end:git.checkout[0K
travis_time:end:18b140f0:start=1568324503523061166,finish=1568324514392156607,duration=10869095441,event=checkout[0Ktravis_time:start:00c8d41a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00c8d41a:start=1568324514397879180,finish=1568324514411674153,duration=13794973,event=env[0Ktravis_time:start:074b9768[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:074b9768:start=1568324514417424518,finish=1568324514425447711,duration=8023193,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0dd591a0[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {bindings,of-of,fe-fe,of-of_np,nutils-of,of-ccx,dealii-of,su2-ccx,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0dd591a0:start=1568324514812448432,finish=1568324514882889009,duration=70440577,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1a38ec00[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584291877/log.txt)