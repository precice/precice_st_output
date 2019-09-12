 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584299312) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/95) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
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
travis_time:end:03bc0f0e:start=1568328326496884022,finish=1568328326503350366,duration=6466344,event=show_system_info[0Ktravis_time:start:000b3414[0Ktravis_time:end:000b3414:start=1568328326506151129,finish=1568328326532580861,duration=26429732,event=rm_riak_source[0Ktravis_time:start:079ce738[0Ktravis_time:end:079ce738:start=1568328326535781020,finish=1568328326540936000,duration=5154980,event=fix_rwky_redis[0Ktravis_time:start:088a61de[0Ktravis_time:end:088a61de:start=1568328326543914696,finish=1568328326907460387,duration=363545691,event=wait_for_network[0Ktravis_time:start:16da1850[0Ktravis_time:end:16da1850:start=1568328326918513070,finish=1568328328006693467,duration=1088180397,event=update_apt_keys[0Ktravis_time:start:04cea316[0Ktravis_time:end:04cea316:start=1568328328012342439,finish=1568328329121772483,duration=1109430044,event=fix_hhvm_source[0Ktravis_time:start:10bb0034[0Ktravis_time:end:10bb0034:start=1568328329126741147,finish=1568328329137298932,duration=10557785,event=update_mongo_arch[0Ktravis_time:start:1a067b46[0Ktravis_time:end:1a067b46:start=1568328329141746112,finish=1568328329185292013,duration=43545901,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1a9d74a6[0Ktravis_time:end:1a9d74a6:start=1568328329190061775,finish=1568328329192825868,duration=2764093,event=update_glibc[0Ktravis_time:start:0c785e34[0Ktravis_time:end:0c785e34:start=1568328329197299437,finish=1568328329205990419,duration=8690982,event=clean_up_path[0Ktravis_time:start:0fd8cef8[0Ktravis_time:end:0fd8cef8:start=1568328329210299881,finish=1568328329218699697,duration=8399816,event=fix_resolv_conf[0Ktravis_time:start:1be4b3e2[0Ktravis_time:end:1be4b3e2:start=1568328329222527298,finish=1568328329232862645,duration=10335347,event=fix_etc_hosts[0Ktravis_time:start:1293d2be[0Ktravis_time:end:1293d2be:start=1568328329236588046,finish=1568328329247539589,duration=10951543,event=fix_mvn_settings_xml[0Ktravis_time:start:00ee8d75[0Ktravis_time:end:00ee8d75:start=1568328329252001589,finish=1568328329262542574,duration=10540985,event=no_ipv6_localhost[0Ktravis_time:start:013fe6c7[0Ktravis_time:end:013fe6c7:start=1568328329266952161,finish=1568328329270215936,duration=3263775,event=fix_etc_mavenrc[0Ktravis_time:start:029445ac[0Ktravis_time:end:029445ac:start=1568328329275750814,finish=1568328329279587361,duration=3836547,event=fix_wwdr_certificate[0Ktravis_time:start:1b0eafb0[0Ktravis_time:end:1b0eafb0:start=1568328329286945991,finish=1568328329313679935,duration=26733944,event=put_localhost_first[0Ktravis_time:start:04c73e00[0Ktravis_time:end:04c73e00:start=1568328329318838723,finish=1568328329322616620,duration=3777897,event=home_paths[0Ktravis_time:start:02856450[0Ktravis_time:end:02856450:start=1568328329327563565,finish=1568328329340225541,duration=12661976,event=disable_initramfs[0Ktravis_time:start:115c3dff[0Ktravis_time:end:115c3dff:start=1568328329344715119,finish=1568328329687097097,duration=342381978,event=disable_ssh_roaming[0Ktravis_time:start:02d44c0c[0Ktravis_time:end:02d44c0c:start=1568328329692154667,finish=1568328329695230939,duration=3076272,event=debug_tools[0Ktravis_time:start:15ab3fd4[0Ktravis_time:end:15ab3fd4:start=1568328329700220642,finish=1568328329703980378,duration=3759736,event=uninstall_oclint[0Ktravis_time:start:07ed2f88[0Ktravis_time:end:07ed2f88:start=1568328329708612243,finish=1568328329712220707,duration=3608464,event=rvm_use[0Ktravis_time:start:153cb862[0Ktravis_time:end:153cb862:start=1568328329716485518,finish=1568328329727270890,duration=10785372,event=rm_etc_boto_cfg[0Ktravis_time:start:29049d0e[0Ktravis_time:end:29049d0e:start=1568328329731754672,finish=1568328329734363923,duration=2609251,event=rm_oraclejdk8_symlink[0Ktravis_time:start:07d5d97c[0Ktravis_time:end:07d5d97c:start=1568328329739028417,finish=1568328329795101021,duration=56072604,event=enable_i386[0Ktravis_time:start:00cbb254[0Ktravis_time:end:00cbb254:start=1568328329800046172,finish=1568328329804417130,duration=4370958,event=update_rubygems[0Ktravis_time:start:27c6e2e3[0Ktravis_time:end:27c6e2e3:start=1568328329808895370,finish=1568328330832658531,duration=1023763161,event=ensure_path_components[0Ktravis_time:start:0a98962b[0Ktravis_time:end:0a98962b:start=1568328330837300828,finish=1568328330840236482,duration=2935654,event=redefine_curl[0Ktravis_time:start:15ef6916[0Ktravis_time:end:15ef6916:start=1568328330844538251,finish=1568328330899681980,duration=55143729,event=nonblock_pipe[0Ktravis_time:start:13788330[0Ktravis_time:end:13788330:start=1568328330903905687,finish=1568328330945550484,duration=41644797,event=apt_get_update[0Ktravis_time:start:13fa34b0[0Ktravis_time:end:13fa34b0:start=1568328330949957702,finish=1568328330952564593,duration=2606891,event=deprecate_xcode_64[0Ktravis_time:start:34fd8149[0Ktravis_time:end:34fd8149:start=1568328330957221739,finish=1568328335928011055,duration=4970789316,event=update_heroku[0Ktravis_time:start:06d274d0[0Ktravis_time:end:06d274d0:start=1568328335932725454,finish=1568328335936141390,duration=3415936,event=shell_session_update[0Ktravis_time:start:0194d060[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3867
travis_fold:end:docker_mtu[0Ktravis_time:end:0194d060:start=1568328335940574117,finish=1568328337142048268,duration=1201474151,event=set_docker_mtu[0Ktravis_time:start:3aea7ec2[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:3aea7ec2:start=1568328337147500402,finish=1568328337215499888,duration=67999486,event=resolvconf[0Ktravis_time:start:1846bafe[0Ktravis_time:end:1846bafe:start=1568328337220396884,finish=1568328337336208699,duration=115811815,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1ce7d19c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1ce7d19c:start=1568328337423264113,finish=1568328337674569123,duration=251305010,event=configure[0Ktravis_time:start:1513f665[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1513f665:start=1568328337679948720,finish=1568328347733408490,duration=10053459770,event=configure[0Ktravis_time:start:14e65e90[0Ktravis_fold:start:services[0Ktravis_time:start:1d8e36d8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1d8e36d8:start=1568328347760014831,finish=1568328347776285298,duration=16270467,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1d8e36d8:start=1568328347760014831,finish=1568328350782071708,duration=3022056877,event=services[0Ktravis_time:start:01efbe00[0Ktravis_time:end:01efbe00:start=1568328350787512633,finish=1568328350790563054,duration=3050421,event=fix_ps4[0Ktravis_time:start:1423ada8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0bf59b70[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0bf59b70:start=1568328350800332071,finish=1568328360954720526,duration=10154388455,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:24c04c50[0K$ git fetch origin +refs/pull/95/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/95/merge -> FETCH_HEAD
travis_time:end:24c04c50:start=1568328360959295550,finish=1568328361420350967,duration=461055417,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:24c04c50:start=1568328360959295550,finish=1568328362299046726,duration=1339751176,event=checkout[0Ktravis_time:start:035d99f6[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:035d99f6:start=1568328362305049931,finish=1568328362317759778,duration=12709847,event=env[0Ktravis_time:start:26490f12[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:26490f12:start=1568328362323623201,finish=1568328362330465644,duration=6842443,event=[0K$ python --version
Python 3.5.6
$ pip --version
 ```
[Full job log](https://api.travis-ci.org/v3/job/584299332/log.txt)