## Status: Passing 
Build: [1009](https://travis-ci.org/precice/systemtests/builds/602036792) 

Job: [1009.1](https://travis-ci.org/precice/systemtests/jobs/602036793) 

Triggered by: [push](https://github.com/precice/systemtests/compare/62c825780a87...da6963fe0a4b) 

---
Last 100 lines of the job log at the moment of push:
```
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
travis_time:end:247f6b02:start=1571867206519395077,finish=1571867206526325269,duration=6930192,event=show_system_info[0Ktravis_time:start:0a632d7a[0Ktravis_time:end:0a632d7a:start=1571867206529868548,finish=1571867206558360092,duration=28491544,event=rm_riak_source[0Ktravis_time:start:111d5f7c[0Ktravis_time:end:111d5f7c:start=1571867206562340119,finish=1571867206571824625,duration=9484506,event=fix_rwky_redis[0Ktravis_time:start:2dedeeaa[0Ktravis_time:end:2dedeeaa:start=1571867206576301051,finish=1571867206966193076,duration=389892025,event=wait_for_network[0Ktravis_time:start:070ecf17[0Ktravis_time:end:070ecf17:start=1571867206971925126,finish=1571867207968328129,duration=996403003,event=update_apt_keys[0Ktravis_time:start:0789e014[0Ktravis_time:end:0789e014:start=1571867207974253946,finish=1571867209128324056,duration=1154070110,event=fix_hhvm_source[0Ktravis_time:start:1f53451c[0Ktravis_time:end:1f53451c:start=1571867209133605919,finish=1571867209144436477,duration=10830558,event=update_mongo_arch[0Ktravis_time:start:060cb9f1[0Ktravis_time:end:060cb9f1:start=1571867209150353740,finish=1571867209196957367,duration=46603627,event=fix_sudo_enabled_trusty[0Ktravis_time:start:327980e8[0Ktravis_time:end:327980e8:start=1571867209203734303,finish=1571867209207066064,duration=3331761,event=update_glibc[0Ktravis_time:start:00ecc880[0Ktravis_time:end:00ecc880:start=1571867209212461389,finish=1571867209225324002,duration=12862613,event=clean_up_path[0Ktravis_time:start:26a60d28[0Ktravis_time:end:26a60d28:start=1571867209230227305,finish=1571867209239820678,duration=9593373,event=fix_resolv_conf[0Ktravis_time:start:0d8f8d8d[0Ktravis_time:end:0d8f8d8d:start=1571867209245170965,finish=1571867209257256398,duration=12085433,event=fix_etc_hosts[0Ktravis_time:start:0a943220[0Ktravis_time:end:0a943220:start=1571867209263051444,finish=1571867209275426423,duration=12374979,event=fix_mvn_settings_xml[0Ktravis_time:start:165344c6[0Ktravis_time:end:165344c6:start=1571867209280692079,finish=1571867209293066915,duration=12374836,event=no_ipv6_localhost[0Ktravis_time:start:0c37f74b[0Ktravis_time:end:0c37f74b:start=1571867209297907646,finish=1571867209301611664,duration=3704018,event=fix_etc_mavenrc[0Ktravis_time:start:063bdd90[0Ktravis_time:end:063bdd90:start=1571867209307882968,finish=1571867209312818362,duration=4935394,event=fix_wwdr_certificate[0Ktravis_time:start:056bd784[0Ktravis_time:end:056bd784:start=1571867209318948993,finish=1571867209347262565,duration=28313572,event=put_localhost_first[0Ktravis_time:start:01957584[0Ktravis_time:end:01957584:start=1571867209352688392,finish=1571867209357881597,duration=5193205,event=home_paths[0Ktravis_time:start:01dbc9ce[0Ktravis_time:end:01dbc9ce:start=1571867209363154235,finish=1571867209378900939,duration=15746704,event=disable_initramfs[0Ktravis_time:start:0948d772[0Ktravis_time:end:0948d772:start=1571867209385772133,finish=1571867209792995597,duration=407223464,event=disable_ssh_roaming[0Ktravis_time:start:005c8122[0Ktravis_time:end:005c8122:start=1571867209799106786,finish=1571867209802455281,duration=3348495,event=debug_tools[0Ktravis_time:start:1c0b74ac[0Ktravis_time:end:1c0b74ac:start=1571867209809888227,finish=1571867209814203238,duration=4315011,event=uninstall_oclint[0Ktravis_time:start:106695d1[0Ktravis_time:end:106695d1:start=1571867209819861373,finish=1571867209824013662,duration=4152289,event=rvm_use[0Ktravis_time:start:224c6eb4[0Ktravis_time:end:224c6eb4:start=1571867209829176245,finish=1571867209840244885,duration=11068640,event=rm_etc_boto_cfg[0Ktravis_time:start:0be1012b[0Ktravis_time:end:0be1012b:start=1571867209846501116,finish=1571867209849706016,duration=3204900,event=rm_oraclejdk8_symlink[0Ktravis_time:start:15cf235c[0Ktravis_time:end:15cf235c:start=1571867209857153293,finish=1571867209920684715,duration=63531422,event=enable_i386[0Ktravis_time:start:262abb3a[0Ktravis_time:end:262abb3a:start=1571867209925902839,finish=1571867209931023254,duration=5120415,event=update_rubygems[0Ktravis_time:start:0a906288[0Ktravis_time:end:0a906288:start=1571867209938046987,finish=1571867211190152422,duration=1252105435,event=ensure_path_components[0Ktravis_time:start:000342f6[0Ktravis_time:end:000342f6:start=1571867211196159384,finish=1571867211199487842,duration=3328458,event=redefine_curl[0Ktravis_time:start:145cc8f3[0Ktravis_time:end:145cc8f3:start=1571867211205211194,finish=1571867211272241873,duration=67030679,event=nonblock_pipe[0Ktravis_time:start:0a507538[0Ktravis_time:end:0a507538:start=1571867211277266679,finish=1571867214351174262,duration=3073907583,event=apt_get_update[0Ktravis_time:start:1d5341ff[0Ktravis_time:end:1d5341ff:start=1571867214355999624,finish=1571867214359276984,duration=3277360,event=deprecate_xcode_64[0Ktravis_time:start:214cf326[0Ktravis_time:end:214cf326:start=1571867214363614788,finish=1571867219740229906,duration=5376615118,event=update_heroku[0Ktravis_time:start:0164c9bb[0Ktravis_time:end:0164c9bb:start=1571867219745324229,finish=1571867219748551494,duration=3227265,event=shell_session_update[0Ktravis_time:start:0ecc5f34[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3957
travis_fold:end:docker_mtu[0Ktravis_time:end:0ecc5f34:start=1571867219753120093,finish=1571867220969489858,duration=1216369765,event=set_docker_mtu[0Ktravis_time:start:24602a9a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:24602a9a:start=1571867220974765484,finish=1571867221048853859,duration=74088375,event=resolvconf[0Ktravis_time:start:062173f8[0Ktravis_time:end:062173f8:start=1571867221054143057,finish=1571867221169092492,duration=114949435,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:13780ccc[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:13780ccc:start=1571867221261009945,finish=1571867221887036170,duration=626026225,event=configure[0Ktravis_time:start:02f08a80[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02f08a80:start=1571867221893873391,finish=1571867238534645291,duration=16640771900,event=configure[0Ktravis_time:start:1c85327a[0Ktravis_fold:start:services[0Ktravis_time:start:23d1c4ae[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:23d1c4ae:start=1571867238564685351,finish=1571867238580524927,duration=15839576,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:23d1c4ae:start=1571867238564685351,finish=1571867241587272656,duration=3022587305,event=services[0Ktravis_time:start:0033f9a9[0Ktravis_time:end:0033f9a9:start=1571867241592010936,finish=1571867241595025935,duration=3014999,event=fix_ps4[0Ktravis_time:start:2bccfc20[0K
travis_fold:start:git.checkout[0Ktravis_time:start:05e5b190[0K$ git clone --depth=50 --branch=EderK-fix-push_args https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:05e5b190:start=1571867241604898429,finish=1571867248163484181,duration=6558585752,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf da6963fe0a4b1a074047bf9d0d7e89c744c6922e
travis_fold:end:git.checkout[0K
travis_time:end:05e5b190:start=1571867241604898429,finish=1571867248274830973,duration=6669932544,event=checkout[0Ktravis_time:start:0f436205[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0f436205:start=1571867248281488651,finish=1571867248293574415,duration=12085764,event=env[0Ktravis_time:start:03646878[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:03646878:start=1571867248301632823,finish=1571867248309503288,duration=7870465,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:051a6daf[0K$ python push.py -s -t fe-fe
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602036793/log.txt)