 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
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
travis_time:end:01e76296:start=1568817123565365094,finish=1568817123572646420,duration=7281326,event=show_system_info[0Ktravis_time:start:223ccfc9[0Ktravis_time:end:223ccfc9:start=1568817123576080184,finish=1568817123609935138,duration=33854954,event=rm_riak_source[0Ktravis_time:start:216a81d4[0Ktravis_time:end:216a81d4:start=1568817123613466848,finish=1568817123619483338,duration=6016490,event=fix_rwky_redis[0Ktravis_time:start:1a762662[0Ktravis_time:end:1a762662:start=1568817123623245961,finish=1568817124008624019,duration=385378058,event=wait_for_network[0Ktravis_time:start:210e4930[0Ktravis_time:end:210e4930:start=1568817124022397307,finish=1568817125626006016,duration=1603608709,event=update_apt_keys[0Ktravis_time:start:09fabb5f[0Ktravis_time:end:09fabb5f:start=1568817125631505838,finish=1568817126742990794,duration=1111484956,event=fix_hhvm_source[0Ktravis_time:start:13865b38[0Ktravis_time:end:13865b38:start=1568817126747281382,finish=1568817126758129943,duration=10848561,event=update_mongo_arch[0Ktravis_time:start:08e1b956[0Ktravis_time:end:08e1b956:start=1568817126762517993,finish=1568817126805488530,duration=42970537,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0061da04[0Ktravis_time:end:0061da04:start=1568817126809637069,finish=1568817126812303471,duration=2666402,event=update_glibc[0Ktravis_time:start:1a090e98[0Ktravis_time:end:1a090e98:start=1568817126816622867,finish=1568817126825950141,duration=9327274,event=clean_up_path[0Ktravis_time:start:1c3f7880[0Ktravis_time:end:1c3f7880:start=1568817126829923696,finish=1568817126839016365,duration=9092669,event=fix_resolv_conf[0Ktravis_time:start:00e4d761[0Ktravis_time:end:00e4d761:start=1568817126843791629,finish=1568817126854148143,duration=10356514,event=fix_etc_hosts[0Ktravis_time:start:0414d5c8[0Ktravis_time:end:0414d5c8:start=1568817126858945706,finish=1568817126869427634,duration=10481928,event=fix_mvn_settings_xml[0Ktravis_time:start:03d2f28e[0Ktravis_time:end:03d2f28e:start=1568817126873470109,finish=1568817126884639223,duration=11169114,event=no_ipv6_localhost[0Ktravis_time:start:006a2f99[0Ktravis_time:end:006a2f99:start=1568817126889527588,finish=1568817126892346955,duration=2819367,event=fix_etc_mavenrc[0Ktravis_time:start:176b40d0[0Ktravis_time:end:176b40d0:start=1568817126896958766,finish=1568817126900844592,duration=3885826,event=fix_wwdr_certificate[0Ktravis_time:start:14859abc[0Ktravis_time:end:14859abc:start=1568817126906254038,finish=1568817126935366235,duration=29112197,event=put_localhost_first[0Ktravis_time:start:136c2050[0Ktravis_time:end:136c2050:start=1568817126940080064,finish=1568817126944293148,duration=4213084,event=home_paths[0Ktravis_time:start:03e91765[0Ktravis_time:end:03e91765:start=1568817126949040442,finish=1568817126964195719,duration=15155277,event=disable_initramfs[0Ktravis_time:start:00ffd3da[0Ktravis_time:end:00ffd3da:start=1568817126969410238,finish=1568817127345690482,duration=376280244,event=disable_ssh_roaming[0Ktravis_time:start:04012489[0Ktravis_time:end:04012489:start=1568817127351080484,finish=1568817127354204140,duration=3123656,event=debug_tools[0Ktravis_time:start:1cc900ba[0Ktravis_time:end:1cc900ba:start=1568817127359311752,finish=1568817127363259941,duration=3948189,event=uninstall_oclint[0Ktravis_time:start:016eda56[0Ktravis_time:end:016eda56:start=1568817127367940065,finish=1568817127372091266,duration=4151201,event=rvm_use[0Ktravis_time:start:315f28f2[0Ktravis_time:end:315f28f2:start=1568817127376872383,finish=1568817127389501759,duration=12629376,event=rm_etc_boto_cfg[0Ktravis_time:start:048021ce[0Ktravis_time:end:048021ce:start=1568817127395107592,finish=1568817127398584811,duration=3477219,event=rm_oraclejdk8_symlink[0Ktravis_time:start:086075e8[0Ktravis_time:end:086075e8:start=1568817127405129264,finish=1568817127469364866,duration=64235602,event=enable_i386[0Ktravis_time:start:002883ba[0Ktravis_time:end:002883ba:start=1568817127474816910,finish=1568817127480605083,duration=5788173,event=update_rubygems[0Ktravis_time:start:399bf88a[0Ktravis_time:end:399bf88a:start=1568817127487238247,finish=1568817128569676242,duration=1082437995,event=ensure_path_components[0Ktravis_time:start:00fdc5e6[0Ktravis_time:end:00fdc5e6:start=1568817128575162049,finish=1568817128578220910,duration=3058861,event=redefine_curl[0Ktravis_time:start:1862e70b[0Ktravis_time:end:1862e70b:start=1568817128583002479,finish=1568817128640467221,duration=57464742,event=nonblock_pipe[0Ktravis_time:start:28645500[0Ktravis_time:end:28645500:start=1568817128645454567,finish=1568817128688845283,duration=43390716,event=apt_get_update[0Ktravis_time:start:104a76b6[0Ktravis_time:end:104a76b6:start=1568817128694406424,finish=1568817128697283641,duration=2877217,event=deprecate_xcode_64[0Ktravis_time:start:18efa714[0Ktravis_time:end:18efa714:start=1568817128701534261,finish=1568817133832640684,duration=5131106423,event=update_heroku[0Ktravis_time:start:08e4f43c[0Ktravis_time:end:08e4f43c:start=1568817133837462052,finish=1568817133840667520,duration=3205468,event=shell_session_update[0Ktravis_time:start:0002832f[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3832
travis_fold:end:docker_mtu[0Ktravis_time:end:0002832f:start=1568817133845945606,finish=1568817135046921860,duration=1200976254,event=set_docker_mtu[0Ktravis_time:start:0723d2c8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0723d2c8:start=1568817135051253618,finish=1568817135126252209,duration=74998591,event=resolvconf[0Ktravis_time:start:0a3454ff[0Ktravis_time:end:0a3454ff:start=1568817135132255792,finish=1568817135244599979,duration=112344187,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:241f2290[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:241f2290:start=1568817135332525037,finish=1568817135692602742,duration=360077705,event=configure[0Ktravis_time:start:080f7c52[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:080f7c52:start=1568817135699260228,finish=1568817146849809014,duration=11150548786,event=configure[0Ktravis_time:start:1b624600[0Ktravis_fold:start:services[0Ktravis_time:start:050159d3[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:050159d3:start=1568817146876442860,finish=1568817146891853434,duration=15410574,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:050159d3:start=1568817146876442860,finish=1568817149897687785,duration=3021244925,event=services[0Ktravis_time:start:089ec270[0Ktravis_time:end:089ec270:start=1568817149902547161,finish=1568817149906121637,duration=3574476,event=fix_ps4[0Ktravis_time:start:01a0d757[0K
travis_fold:start:git.checkout[0Ktravis_time:start:019a4187[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:019a4187:start=1568817149916133395,finish=1568817160649043663,duration=10732910268,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:2841a722[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:2841a722:start=1568817160653866405,finish=1568817161161311531,duration=507445126,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:2841a722:start=1568817160653866405,finish=1568817161747308047,duration=1093441642,event=checkout[0Ktravis_time:start:09083865[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:09083865:start=1568817161752613263,finish=1568817161764456008,duration=11842745,event=env[0Ktravis_time:start:0370c813[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0370c813:start=1568817161772623686,finish=1568817161779010042,duration=6386356,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:23e934aa[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {bindings,of-ccx,nutils-of,of-of,dealii-of,su2-ccx,fe-fe,of-of_np,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:23e934aa:start=1568817162143779104,finish=1568817162211220334,duration=67441230,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:00db86d8[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510231/log.txt)