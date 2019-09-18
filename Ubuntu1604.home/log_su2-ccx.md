 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510170) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/40d6daa277c6...b989e40888b7) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72) 
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
travis_time:end:0d18da50:start=1568814956381246456,finish=1568814956387252111,duration=6005655,event=show_system_info[0Ktravis_time:start:12742ae2[0Ktravis_time:end:12742ae2:start=1568814956390289307,finish=1568814956418048635,duration=27759328,event=rm_riak_source[0Ktravis_time:start:16b2bbda[0Ktravis_time:end:16b2bbda:start=1568814956421676335,finish=1568814956427343053,duration=5666718,event=fix_rwky_redis[0Ktravis_time:start:02c4eadc[0Ktravis_time:end:02c4eadc:start=1568814956430712263,finish=1568814956806441389,duration=375729126,event=wait_for_network[0Ktravis_time:start:128b5024[0Ktravis_time:end:128b5024:start=1568814956832056507,finish=1568814957906558084,duration=1074501577,event=update_apt_keys[0Ktravis_time:start:013c1387[0Ktravis_time:end:013c1387:start=1568814957910826787,finish=1568814959026589232,duration=1115762445,event=fix_hhvm_source[0Ktravis_time:start:09dd8ef8[0Ktravis_time:end:09dd8ef8:start=1568814959031598503,finish=1568814959042805318,duration=11206815,event=update_mongo_arch[0Ktravis_time:start:05a70e66[0Ktravis_time:end:05a70e66:start=1568814959048006817,finish=1568814959099476454,duration=51469637,event=fix_sudo_enabled_trusty[0Ktravis_time:start:15e16535[0Ktravis_time:end:15e16535:start=1568814959105980204,finish=1568814959109694455,duration=3714251,event=update_glibc[0Ktravis_time:start:0ca46670[0Ktravis_time:end:0ca46670:start=1568814959115334223,finish=1568814959126235918,duration=10901695,event=clean_up_path[0Ktravis_time:start:195e9c70[0Ktravis_time:end:195e9c70:start=1568814959131461346,finish=1568814959141523559,duration=10062213,event=fix_resolv_conf[0Ktravis_time:start:038b8e4f[0Ktravis_time:end:038b8e4f:start=1568814959146801523,finish=1568814959156778301,duration=9976778,event=fix_etc_hosts[0Ktravis_time:start:0d305631[0Ktravis_time:end:0d305631:start=1568814959161238450,finish=1568814959171854583,duration=10616133,event=fix_mvn_settings_xml[0Ktravis_time:start:1e494374[0Ktravis_time:end:1e494374:start=1568814959176910843,finish=1568814959187893429,duration=10982586,event=no_ipv6_localhost[0Ktravis_time:start:05e25b80[0Ktravis_time:end:05e25b80:start=1568814959192816430,finish=1568814959195670580,duration=2854150,event=fix_etc_mavenrc[0Ktravis_time:start:09731a26[0Ktravis_time:end:09731a26:start=1568814959200121468,finish=1568814959204761835,duration=4640367,event=fix_wwdr_certificate[0Ktravis_time:start:029df4c0[0Ktravis_time:end:029df4c0:start=1568814959214958560,finish=1568814959243165815,duration=28207255,event=put_localhost_first[0Ktravis_time:start:2e35d24c[0Ktravis_time:end:2e35d24c:start=1568814959248463286,finish=1568814959253063667,duration=4600381,event=home_paths[0Ktravis_time:start:19dd633c[0Ktravis_time:end:19dd633c:start=1568814959260602182,finish=1568814959273258323,duration=12656141,event=disable_initramfs[0Ktravis_time:start:15608678[0Ktravis_time:end:15608678:start=1568814959278174931,finish=1568814959598482838,duration=320307907,event=disable_ssh_roaming[0Ktravis_time:start:19871d9a[0Ktravis_time:end:19871d9a:start=1568814959603077530,finish=1568814959606595451,duration=3517921,event=debug_tools[0Ktravis_time:start:11475037[0Ktravis_time:end:11475037:start=1568814959612169509,finish=1568814959616153932,duration=3984423,event=uninstall_oclint[0Ktravis_time:start:019a44a8[0Ktravis_time:end:019a44a8:start=1568814959620571570,finish=1568814959624184279,duration=3612709,event=rvm_use[0Ktravis_time:start:007d6b5c[0Ktravis_time:end:007d6b5c:start=1568814959630950355,finish=1568814959638913605,duration=7963250,event=rm_etc_boto_cfg[0Ktravis_time:start:15245c38[0Ktravis_time:end:15245c38:start=1568814959643229736,finish=1568814959646010498,duration=2780762,event=rm_oraclejdk8_symlink[0Ktravis_time:start:11aefcca[0Ktravis_time:end:11aefcca:start=1568814959651054780,finish=1568814959707758933,duration=56704153,event=enable_i386[0Ktravis_time:start:07c316b8[0Ktravis_time:end:07c316b8:start=1568814959712759311,finish=1568814959717643908,duration=4884597,event=update_rubygems[0Ktravis_time:start:3b89ac0a[0Ktravis_time:end:3b89ac0a:start=1568814959723122337,finish=1568814960876816925,duration=1153694588,event=ensure_path_components[0Ktravis_time:start:1d31d5fc[0Ktravis_time:end:1d31d5fc:start=1568814960881770147,finish=1568814960884942365,duration=3172218,event=redefine_curl[0Ktravis_time:start:00a9572c[0Ktravis_time:end:00a9572c:start=1568814960890006820,finish=1568814960946120331,duration=56113511,event=nonblock_pipe[0Ktravis_time:start:2bfc1220[0Ktravis_time:end:2bfc1220:start=1568814960951040682,finish=1568814961006600886,duration=55560204,event=apt_get_update[0Ktravis_time:start:03f50eb2[0Ktravis_time:end:03f50eb2:start=1568814961012171392,finish=1568814961015818409,duration=3647017,event=deprecate_xcode_64[0Ktravis_time:start:016dcb80[0Ktravis_time:end:016dcb80:start=1568814961021141698,finish=1568814966057262860,duration=5036121162,event=update_heroku[0Ktravis_time:start:02924e9e[0Ktravis_time:end:02924e9e:start=1568814966062992604,finish=1568814966066038458,duration=3045854,event=shell_session_update[0Ktravis_time:start:003b98c5[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3834
travis_fold:end:docker_mtu[0Ktravis_time:end:003b98c5:start=1568814966070989881,finish=1568814967270685140,duration=1199695259,event=set_docker_mtu[0Ktravis_time:start:0481bc72[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0481bc72:start=1568814967275607001,finish=1568814967347049562,duration=71442561,event=resolvconf[0Ktravis_time:start:00b95f0c[0Ktravis_time:end:00b95f0c:start=1568814967353206402,finish=1568814967474494140,duration=121287738,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0c386910[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0c386910:start=1568814967562915750,finish=1568814968106642168,duration=543726418,event=configure[0Ktravis_time:start:08973806[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:08973806:start=1568814968112168287,finish=1568814980610835293,duration=12498667006,event=configure[0Ktravis_time:start:07819c80[0Ktravis_fold:start:services[0Ktravis_time:start:0021e6e4[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0021e6e4:start=1568814980636810585,finish=1568814980651794091,duration=14983506,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0021e6e4:start=1568814980636810585,finish=1568814983658241041,duration=3021430456,event=services[0Ktravis_time:start:093c6054[0Ktravis_time:end:093c6054:start=1568814983664482351,finish=1568814983668943131,duration=4460780,event=fix_ps4[0Ktravis_time:start:3939a182[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0dd515b0[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0dd515b0:start=1568814983680004501,finish=1568814994879332243,duration=11199327742,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b989e40888b7bc80b4a7d6d823b98fc3ebb61025
travis_fold:end:git.checkout[0K
travis_time:end:0dd515b0:start=1568814983680004501,finish=1568814995783356846,duration=12103352345,event=checkout[0Ktravis_time:start:01ccef54[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01ccef54:start=1568814995789249320,finish=1568814995802430358,duration=13181038,event=env[0Ktravis_time:start:0f626953[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0f626953:start=1568814995808430603,finish=1568814995815151474,duration=6720871,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:25a25c40[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {nutils-of,fe-fe,of-ccx,of-of_np,of-ccx_fsi,bindings,su2-ccx,dealii-of,of-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:25a25c40:start=1568814996220937702,finish=1568814996292727384,duration=71789682,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:09d01a3c[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510183/log.txt)