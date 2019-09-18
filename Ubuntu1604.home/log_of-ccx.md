 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586517772) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63e83084ff16...628c8f57e99a) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
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
travis_time:end:0edbee7c:start=1568823195038320656,finish=1568823195045340263,duration=7019607,event=show_system_info[0Ktravis_time:start:1c935486[0Ktravis_time:end:1c935486:start=1568823195048356774,finish=1568823195073106478,duration=24749704,event=rm_riak_source[0Ktravis_time:start:0fb8c3f1[0Ktravis_time:end:0fb8c3f1:start=1568823195076187573,finish=1568823195081334735,duration=5147162,event=fix_rwky_redis[0Ktravis_time:start:12387180[0Ktravis_time:end:12387180:start=1568823195084277105,finish=1568823195528875519,duration=444598414,event=wait_for_network[0Ktravis_time:start:01ff70ce[0Ktravis_time:end:01ff70ce:start=1568823195533754055,finish=1568823197115171748,duration=1581417693,event=update_apt_keys[0Ktravis_time:start:07402df4[0Ktravis_time:end:07402df4:start=1568823197120283130,finish=1568823198189736321,duration=1069453191,event=fix_hhvm_source[0Ktravis_time:start:026bc935[0Ktravis_time:end:026bc935:start=1568823198194298832,finish=1568823198206951790,duration=12652958,event=update_mongo_arch[0Ktravis_time:start:1d320cb9[0Ktravis_time:end:1d320cb9:start=1568823198213379235,finish=1568823198256956486,duration=43577251,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0d40d050[0Ktravis_time:end:0d40d050:start=1568823198261809942,finish=1568823198265475625,duration=3665683,event=update_glibc[0Ktravis_time:start:0e034720[0Ktravis_time:end:0e034720:start=1568823198270599088,finish=1568823198284601130,duration=14002042,event=clean_up_path[0Ktravis_time:start:0e24fda2[0Ktravis_time:end:0e24fda2:start=1568823198289731436,finish=1568823198301920925,duration=12189489,event=fix_resolv_conf[0Ktravis_time:start:0274808d[0Ktravis_time:end:0274808d:start=1568823198307907063,finish=1568823198318481749,duration=10574686,event=fix_etc_hosts[0Ktravis_time:start:115aeddc[0Ktravis_time:end:115aeddc:start=1568823198322835639,finish=1568823198334230651,duration=11395012,event=fix_mvn_settings_xml[0Ktravis_time:start:24c7556a[0Ktravis_time:end:24c7556a:start=1568823198340757861,finish=1568823198351814075,duration=11056214,event=no_ipv6_localhost[0Ktravis_time:start:0656c5bc[0Ktravis_time:end:0656c5bc:start=1568823198356922951,finish=1568823198359691470,duration=2768519,event=fix_etc_mavenrc[0Ktravis_time:start:04e269d8[0Ktravis_time:end:04e269d8:start=1568823198365520682,finish=1568823198371377025,duration=5856343,event=fix_wwdr_certificate[0Ktravis_time:start:0048888b[0Ktravis_time:end:0048888b:start=1568823198377093351,finish=1568823198405569408,duration=28476057,event=put_localhost_first[0Ktravis_time:start:2d9f42de[0Ktravis_time:end:2d9f42de:start=1568823198410728229,finish=1568823198415704201,duration=4975972,event=home_paths[0Ktravis_time:start:03d1b440[0Ktravis_time:end:03d1b440:start=1568823198422030293,finish=1568823198439019933,duration=16989640,event=disable_initramfs[0Ktravis_time:start:0ae21648[0Ktravis_time:end:0ae21648:start=1568823198445361240,finish=1568823198757297519,duration=311936279,event=disable_ssh_roaming[0Ktravis_time:start:27df5020[0Ktravis_time:end:27df5020:start=1568823198763130972,finish=1568823198766152832,duration=3021860,event=debug_tools[0Ktravis_time:start:07e90b40[0Ktravis_time:end:07e90b40:start=1568823198771473747,finish=1568823198777570764,duration=6097017,event=uninstall_oclint[0Ktravis_time:start:2af84609[0Ktravis_time:end:2af84609:start=1568823198781552172,finish=1568823198785535045,duration=3982873,event=rvm_use[0Ktravis_time:start:04481de0[0Ktravis_time:end:04481de0:start=1568823198789650136,finish=1568823198804974593,duration=15324457,event=rm_etc_boto_cfg[0Ktravis_time:start:07bf6a14[0Ktravis_time:end:07bf6a14:start=1568823198809389283,finish=1568823198812950353,duration=3561070,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2ad24356[0Ktravis_time:end:2ad24356:start=1568823198817438169,finish=1568823198885643077,duration=68204908,event=enable_i386[0Ktravis_time:start:086e1790[0Ktravis_time:end:086e1790:start=1568823198892465375,finish=1568823198896816227,duration=4350852,event=update_rubygems[0Ktravis_time:start:2af5a210[0Ktravis_time:end:2af5a210:start=1568823198901399361,finish=1568823200014943475,duration=1113544114,event=ensure_path_components[0Ktravis_time:start:314f49c4[0Ktravis_time:end:314f49c4:start=1568823200019569442,finish=1568823200022353900,duration=2784458,event=redefine_curl[0Ktravis_time:start:2184dc00[0Ktravis_time:end:2184dc00:start=1568823200027076102,finish=1568823200081138675,duration=54062573,event=nonblock_pipe[0Ktravis_time:start:081b6400[0Ktravis_time:end:081b6400:start=1568823200086809392,finish=1568823200132797827,duration=45988435,event=apt_get_update[0Ktravis_time:start:00c01168[0Ktravis_time:end:00c01168:start=1568823200138267918,finish=1568823200140812389,duration=2544471,event=deprecate_xcode_64[0Ktravis_time:start:0a63390a[0Ktravis_time:end:0a63390a:start=1568823200145806100,finish=1568823205620150612,duration=5474344512,event=update_heroku[0Ktravis_time:start:01520455[0Ktravis_time:end:01520455:start=1568823205624414790,finish=1568823205627446820,duration=3032030,event=shell_session_update[0Ktravis_time:start:03fe2044[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3859
travis_fold:end:docker_mtu[0Ktravis_time:end:03fe2044:start=1568823205631478951,finish=1568823206835443867,duration=1203964916,event=set_docker_mtu[0Ktravis_time:start:0575bb63[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0575bb63:start=1568823206840254239,finish=1568823206914402491,duration=74148252,event=resolvconf[0Ktravis_time:start:0674d592[0Ktravis_time:end:0674d592:start=1568823206918478254,finish=1568823207034742953,duration=116264699,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:10745120[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:10745120:start=1568823207126197216,finish=1568823208372360186,duration=1246162970,event=configure[0Ktravis_time:start:28895f3a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:28895f3a:start=1568823208378269696,finish=1568823219317469900,duration=10939200204,event=configure[0Ktravis_time:start:1e2c8f9f[0Ktravis_fold:start:services[0Ktravis_time:start:0ca501b3[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0ca501b3:start=1568823219343128716,finish=1568823219358678578,duration=15549862,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0ca501b3:start=1568823219343128716,finish=1568823222366350986,duration=3023222270,event=services[0Ktravis_time:start:00082638[0Ktravis_time:end:00082638:start=1568823222371786858,finish=1568823222374900035,duration=3113177,event=fix_ps4[0Ktravis_time:start:00d31e9e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08e2f07b[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-fixpip1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08e2f07b:start=1568823222384540984,finish=1568823234619562402,duration=12235021418,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 628c8f57e99ad5b8d85cdaca6e230b3407aa4aee
travis_fold:end:git.checkout[0K
travis_time:end:08e2f07b:start=1568823222384540984,finish=1568823234960061763,duration=12575520779,event=checkout[0Ktravis_time:start:0486ea30[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0486ea30:start=1568823234964362449,finish=1568823234978289738,duration=13927289,event=env[0Ktravis_time:start:179fc858[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:179fc858:start=1568823234989475940,finish=1568823234998909541,duration=9433601,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:20c2f950[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,of-ccx,of-of_np,of-ccx_fsi,dealii-of,of-of,fe-fe,bindings,nutils-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:20c2f950:start=1568823235437776474,finish=1568823235514567173,duration=76790699,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0b4f7c45[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586517793/log.txt)