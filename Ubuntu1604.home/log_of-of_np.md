 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584619352) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3433ca666766...b4f731a5d60e) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
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
travis_time:end:0d149048:start=1568392108229060621,finish=1568392108235143151,duration=6082530,event=show_system_info[0Ktravis_time:start:064290f9[0Ktravis_time:end:064290f9:start=1568392108237958762,finish=1568392108266942878,duration=28984116,event=rm_riak_source[0Ktravis_time:start:0e486c92[0Ktravis_time:end:0e486c92:start=1568392108270219785,finish=1568392108275588530,duration=5368745,event=fix_rwky_redis[0Ktravis_time:start:035f4ea4[0Ktravis_time:end:035f4ea4:start=1568392108278662628,finish=1568392108705457363,duration=426794735,event=wait_for_network[0Ktravis_time:start:1fb2d076[0Ktravis_time:end:1fb2d076:start=1568392108710215897,finish=1568392109671277126,duration=961061229,event=update_apt_keys[0Ktravis_time:start:0ed818ac[0Ktravis_time:end:0ed818ac:start=1568392109676358815,finish=1568392110736676577,duration=1060317762,event=fix_hhvm_source[0Ktravis_time:start:1abfcbc0[0Ktravis_time:end:1abfcbc0:start=1568392110741829487,finish=1568392110752049495,duration=10220008,event=update_mongo_arch[0Ktravis_time:start:10fda1a4[0Ktravis_time:end:10fda1a4:start=1568392110756938721,finish=1568392110800917917,duration=43979196,event=fix_sudo_enabled_trusty[0Ktravis_time:start:159a0ac8[0Ktravis_time:end:159a0ac8:start=1568392110806170629,finish=1568392110809281104,duration=3110475,event=update_glibc[0Ktravis_time:start:03b2d8c0[0Ktravis_time:end:03b2d8c0:start=1568392110813530700,finish=1568392110823420887,duration=9890187,event=clean_up_path[0Ktravis_time:start:2bedb57c[0Ktravis_time:end:2bedb57c:start=1568392110827651802,finish=1568392110836516071,duration=8864269,event=fix_resolv_conf[0Ktravis_time:start:02f8ae5e[0Ktravis_time:end:02f8ae5e:start=1568392110840811053,finish=1568392110851427006,duration=10615953,event=fix_etc_hosts[0Ktravis_time:start:256150c6[0Ktravis_time:end:256150c6:start=1568392110855729025,finish=1568392110866345879,duration=10616854,event=fix_mvn_settings_xml[0Ktravis_time:start:3be5224e[0Ktravis_time:end:3be5224e:start=1568392110870914524,finish=1568392110881597128,duration=10682604,event=no_ipv6_localhost[0Ktravis_time:start:00453308[0Ktravis_time:end:00453308:start=1568392110887210494,finish=1568392110890220452,duration=3009958,event=fix_etc_mavenrc[0Ktravis_time:start:22655934[0Ktravis_time:end:22655934:start=1568392110894638072,finish=1568392110899280107,duration=4642035,event=fix_wwdr_certificate[0Ktravis_time:start:17121527[0Ktravis_time:end:17121527:start=1568392110903571542,finish=1568392110934637055,duration=31065513,event=put_localhost_first[0Ktravis_time:start:2108e9b8[0Ktravis_time:end:2108e9b8:start=1568392110939434130,finish=1568392110943329589,duration=3895459,event=home_paths[0Ktravis_time:start:006b017a[0Ktravis_time:end:006b017a:start=1568392110947850683,finish=1568392110960413350,duration=12562667,event=disable_initramfs[0Ktravis_time:start:03caa7f0[0Ktravis_time:end:03caa7f0:start=1568392110965049992,finish=1568392111286315728,duration=321265736,event=disable_ssh_roaming[0Ktravis_time:start:0a3ed672[0Ktravis_time:end:0a3ed672:start=1568392111290838183,finish=1568392111293577507,duration=2739324,event=debug_tools[0Ktravis_time:start:133b1a26[0Ktravis_time:end:133b1a26:start=1568392111297882669,finish=1568392111301462824,duration=3580155,event=uninstall_oclint[0Ktravis_time:start:00e3ef4a[0Ktravis_time:end:00e3ef4a:start=1568392111305309961,finish=1568392111309057709,duration=3747748,event=rvm_use[0Ktravis_time:start:014076e8[0Ktravis_time:end:014076e8:start=1568392111312707506,finish=1568392111322813632,duration=10106126,event=rm_etc_boto_cfg[0Ktravis_time:start:27b331da[0Ktravis_time:end:27b331da:start=1568392111327239545,finish=1568392111329936671,duration=2697126,event=rm_oraclejdk8_symlink[0Ktravis_time:start:007199f4[0Ktravis_time:end:007199f4:start=1568392111334606664,finish=1568392111390499500,duration=55892836,event=enable_i386[0Ktravis_time:start:09489960[0Ktravis_time:end:09489960:start=1568392111394628641,finish=1568392111400629759,duration=6001118,event=update_rubygems[0Ktravis_time:start:04204be2[0Ktravis_time:end:04204be2:start=1568392111407517214,finish=1568392112439043205,duration=1031525991,event=ensure_path_components[0Ktravis_time:start:07a13490[0Ktravis_time:end:07a13490:start=1568392112443796208,finish=1568392112446743990,duration=2947782,event=redefine_curl[0Ktravis_time:start:14a83110[0Ktravis_time:end:14a83110:start=1568392112451074595,finish=1568392112507262679,duration=56188084,event=nonblock_pipe[0Ktravis_time:start:174a215c[0Ktravis_time:end:174a215c:start=1568392112511863198,finish=1568392112554639611,duration=42776413,event=apt_get_update[0Ktravis_time:start:05f1783e[0Ktravis_time:end:05f1783e:start=1568392112558878741,finish=1568392112561785370,duration=2906629,event=deprecate_xcode_64[0Ktravis_time:start:041a01aa[0Ktravis_time:end:041a01aa:start=1568392112566752372,finish=1568392117377812752,duration=4811060380,event=update_heroku[0Ktravis_time:start:15a83c06[0Ktravis_time:end:15a83c06:start=1568392117382727204,finish=1568392117385650225,duration=2923021,event=shell_session_update[0Ktravis_time:start:175ce5bd[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3928
travis_fold:end:docker_mtu[0Ktravis_time:end:175ce5bd:start=1568392117389969055,finish=1568392118580647460,duration=1190678405,event=set_docker_mtu[0Ktravis_time:start:152a48bd[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:152a48bd:start=1568392118585147579,finish=1568392118653676321,duration=68528742,event=resolvconf[0Ktravis_time:start:2aca2038[0Ktravis_time:end:2aca2038:start=1568392118658678919,finish=1568392118762916419,duration=104237500,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:16e3b37c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:16e3b37c:start=1568392118846586957,finish=1568392119254629938,duration=408042981,event=configure[0Ktravis_time:start:065c3110[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:065c3110:start=1568392119259952260,finish=1568392130009310921,duration=10749358661,event=configure[0Ktravis_time:start:0e323566[0Ktravis_fold:start:services[0Ktravis_time:start:18d61507[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:18d61507:start=1568392130035424966,finish=1568392130052315490,duration=16890524,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:18d61507:start=1568392130035424966,finish=1568392133057323710,duration=3021898744,event=services[0Ktravis_time:start:00ab25b8[0Ktravis_time:end:00ab25b8:start=1568392133061193647,finish=1568392133064069437,duration=2875790,event=fix_ps4[0Ktravis_time:start:351aa0c1[0K
travis_fold:start:git.checkout[0Ktravis_time:start:13eade80[0K$ git clone --depth=50 --branch=code_aster_adapter https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:13eade80:start=1568392133072097143,finish=1568392143348606639,duration=10276509496,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b4f731a5d60e7af97ee48400e5c51e279cd9f34f
travis_fold:end:git.checkout[0K
travis_time:end:13eade80:start=1568392133072097143,finish=1568392143610419351,duration=10538322208,event=checkout[0Ktravis_time:start:1166182e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1166182e:start=1568392143614732793,finish=1568392143624872704,duration=10139911,event=env[0Ktravis_time:start:0061a5ad[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0061a5ad:start=1568392143629520058,finish=1568392143635371349,duration=5851291,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2d40b878[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {dealii-of,nutils-of,of-of_np,bindings,of-ccx_fsi,of-of,su2-ccx,fe-fe,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:2d40b878:start=1568392143986222104,finish=1568392144049858739,duration=63636635,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0e41eefd[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584619372/log.txt)