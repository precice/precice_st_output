 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584619352) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3433ca666766...b4f731a5d60e) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef) 
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
travis_time:end:244fc5c9:start=1568391694176831612,finish=1568391694182486968,duration=5655356,event=show_system_info[0Ktravis_time:start:034e0e82[0Ktravis_time:end:034e0e82:start=1568391694185599536,finish=1568391694212254175,duration=26654639,event=rm_riak_source[0Ktravis_time:start:0527b02e[0Ktravis_time:end:0527b02e:start=1568391694215495903,finish=1568391694220582766,duration=5086863,event=fix_rwky_redis[0Ktravis_time:start:0f023948[0Ktravis_time:end:0f023948:start=1568391694223521029,finish=1568391694632945954,duration=409424925,event=wait_for_network[0Ktravis_time:start:11682f98[0Ktravis_time:end:11682f98:start=1568391694636672707,finish=1568391695702713243,duration=1066040536,event=update_apt_keys[0Ktravis_time:start:0dadd936[0Ktravis_time:end:0dadd936:start=1568391695706720268,finish=1568391696749649013,duration=1042928745,event=fix_hhvm_source[0Ktravis_time:start:180a0d66[0Ktravis_time:end:180a0d66:start=1568391696754072535,finish=1568391696764227104,duration=10154569,event=update_mongo_arch[0Ktravis_time:start:025c1b22[0Ktravis_time:end:025c1b22:start=1568391696768066024,finish=1568391696810874672,duration=42808648,event=fix_sudo_enabled_trusty[0Ktravis_time:start:150b5e90[0Ktravis_time:end:150b5e90:start=1568391696815029436,finish=1568391696817860653,duration=2831217,event=update_glibc[0Ktravis_time:start:057e22c1[0Ktravis_time:end:057e22c1:start=1568391696821815716,finish=1568391696831655488,duration=9839772,event=clean_up_path[0Ktravis_time:start:01e1614b[0Ktravis_time:end:01e1614b:start=1568391696835792047,finish=1568391696844037276,duration=8245229,event=fix_resolv_conf[0Ktravis_time:start:04a14e2e[0Ktravis_time:end:04a14e2e:start=1568391696847788133,finish=1568391696858273173,duration=10485040,event=fix_etc_hosts[0Ktravis_time:start:2adeaca5[0Ktravis_time:end:2adeaca5:start=1568391696862917458,finish=1568391696873918642,duration=11001184,event=fix_mvn_settings_xml[0Ktravis_time:start:00a1ac75[0Ktravis_time:end:00a1ac75:start=1568391696878207308,finish=1568391696888554232,duration=10346924,event=no_ipv6_localhost[0Ktravis_time:start:0c3da60e[0Ktravis_time:end:0c3da60e:start=1568391696893817451,finish=1568391696896379171,duration=2561720,event=fix_etc_mavenrc[0Ktravis_time:start:000054de[0Ktravis_time:end:000054de:start=1568391696900995745,finish=1568391696904392462,duration=3396717,event=fix_wwdr_certificate[0Ktravis_time:start:044cd188[0Ktravis_time:end:044cd188:start=1568391696908735047,finish=1568391696934884285,duration=26149238,event=put_localhost_first[0Ktravis_time:start:0075c880[0Ktravis_time:end:0075c880:start=1568391696938679209,finish=1568391696942238653,duration=3559444,event=home_paths[0Ktravis_time:start:109ef543[0Ktravis_time:end:109ef543:start=1568391696946858964,finish=1568391696961255590,duration=14396626,event=disable_initramfs[0Ktravis_time:start:28350a21[0Ktravis_time:end:28350a21:start=1568391696965930910,finish=1568391697218084638,duration=252153728,event=disable_ssh_roaming[0Ktravis_time:start:09a6f3e7[0Ktravis_time:end:09a6f3e7:start=1568391697222432475,finish=1568391697227863210,duration=5430735,event=debug_tools[0Ktravis_time:start:07ed706d[0Ktravis_time:end:07ed706d:start=1568391697231970506,finish=1568391697235693460,duration=3722954,event=uninstall_oclint[0Ktravis_time:start:0028a080[0Ktravis_time:end:0028a080:start=1568391697240040655,finish=1568391697243760496,duration=3719841,event=rvm_use[0Ktravis_time:start:0f4fde20[0Ktravis_time:end:0f4fde20:start=1568391697248411618,finish=1568391697257270319,duration=8858701,event=rm_etc_boto_cfg[0Ktravis_time:start:0b19cfd8[0Ktravis_time:end:0b19cfd8:start=1568391697261802379,finish=1568391697265201803,duration=3399424,event=rm_oraclejdk8_symlink[0Ktravis_time:start:03988718[0Ktravis_time:end:03988718:start=1568391697269896943,finish=1568391697332854756,duration=62957813,event=enable_i386[0Ktravis_time:start:1cc96aaf[0Ktravis_time:end:1cc96aaf:start=1568391697338068300,finish=1568391697342939065,duration=4870765,event=update_rubygems[0Ktravis_time:start:14c67442[0Ktravis_time:end:14c67442:start=1568391697346757767,finish=1568391698366140082,duration=1019382315,event=ensure_path_components[0Ktravis_time:start:010f867e[0Ktravis_time:end:010f867e:start=1568391698371404027,finish=1568391698374453898,duration=3049871,event=redefine_curl[0Ktravis_time:start:0bcd1735[0Ktravis_time:end:0bcd1735:start=1568391698378438789,finish=1568391698435081454,duration=56642665,event=nonblock_pipe[0Ktravis_time:start:03933078[0Ktravis_time:end:03933078:start=1568391698439699330,finish=1568391698481049858,duration=41350528,event=apt_get_update[0Ktravis_time:start:0028323c[0Ktravis_time:end:0028323c:start=1568391698485337534,finish=1568391698488352277,duration=3014743,event=deprecate_xcode_64[0Ktravis_time:start:13409760[0Ktravis_time:end:13409760:start=1568391698492512643,finish=1568391703241846265,duration=4749333622,event=update_heroku[0Ktravis_time:start:1dc2a5fd[0Ktravis_time:end:1dc2a5fd:start=1568391703246366939,finish=1568391703249391146,duration=3024207,event=shell_session_update[0Ktravis_time:start:109a3a0e[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3827
travis_fold:end:docker_mtu[0Ktravis_time:end:109a3a0e:start=1568391703254073190,finish=1568391704457407765,duration=1203334575,event=set_docker_mtu[0Ktravis_time:start:110d496a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:110d496a:start=1568391704463575415,finish=1568391704531920471,duration=68345056,event=resolvconf[0Ktravis_time:start:012a50de[0Ktravis_time:end:012a50de:start=1568391704537518059,finish=1568391704639887849,duration=102369790,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02201bcc[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02201bcc:start=1568391704727217237,finish=1568391704987464962,duration=260247725,event=configure[0Ktravis_time:start:0aa2f4ca[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0aa2f4ca:start=1568391704992657216,finish=1568391715020212184,duration=10027554968,event=configure[0Ktravis_time:start:149e6a4c[0Ktravis_fold:start:services[0Ktravis_time:start:2a5cee24[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:2a5cee24:start=1568391715046621133,finish=1568391715062546310,duration=15925177,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2a5cee24:start=1568391715046621133,finish=1568391718069273347,duration=3022652214,event=services[0Ktravis_time:start:00d416ba[0Ktravis_time:end:00d416ba:start=1568391718073837631,finish=1568391718077338002,duration=3500371,event=fix_ps4[0Ktravis_time:start:140564d0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:16a8baf4[0K$ git clone --depth=50 --branch=code_aster_adapter https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:16a8baf4:start=1568391718086489046,finish=1568391728188401404,duration=10101912358,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b4f731a5d60e7af97ee48400e5c51e279cd9f34f
travis_fold:end:git.checkout[0K
travis_time:end:16a8baf4:start=1568391718086489046,finish=1568391728334845069,duration=10248356023,event=checkout[0Ktravis_time:start:02611bf6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:02611bf6:start=1568391728339610044,finish=1568391728349200861,duration=9590817,event=env[0Ktravis_time:start:20e64cb8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:20e64cb8:start=1568391728353638248,finish=1568391728359646455,duration=6008207,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:08daabfe[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,bindings,dealii-of,of-of_np,su2-ccx,of-of,of-ccx,fe-fe,nutils-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:08daabfe:start=1568391728707920206,finish=1568391728774785423,duration=66865217,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0e0e31a0[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584619367/log.txt)