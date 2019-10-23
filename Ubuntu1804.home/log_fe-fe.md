## Status: Passing 
Build: [1008](https://travis-ci.org/precice/systemtests/builds/602035162) 

Job: [1008.1](https://travis-ci.org/precice/systemtests/jobs/602035163) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e69a3483ba2d...62c825780a87) 

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
travis_time:end:04478669:start=1571866752359892042,finish=1571866752366571781,duration=6679739,event=show_system_info[0Ktravis_time:start:208770f0[0Ktravis_time:end:208770f0:start=1571866752369676612,finish=1571866752400713695,duration=31037083,event=rm_riak_source[0Ktravis_time:start:0f56730a[0Ktravis_time:end:0f56730a:start=1571866752404888848,finish=1571866752410574356,duration=5685508,event=fix_rwky_redis[0Ktravis_time:start:00e638aa[0Ktravis_time:end:00e638aa:start=1571866752417431322,finish=1571866752792425587,duration=374994265,event=wait_for_network[0Ktravis_time:start:03f7f2e4[0Ktravis_time:end:03f7f2e4:start=1571866752797310330,finish=1571866754394749201,duration=1597438871,event=update_apt_keys[0Ktravis_time:start:1909cde7[0Ktravis_time:end:1909cde7:start=1571866754399478475,finish=1571866755480650886,duration=1081172411,event=fix_hhvm_source[0Ktravis_time:start:11ab6148[0Ktravis_time:end:11ab6148:start=1571866755485643107,finish=1571866755496253597,duration=10610490,event=update_mongo_arch[0Ktravis_time:start:02935ba5[0Ktravis_time:end:02935ba5:start=1571866755501494642,finish=1571866755544204819,duration=42710177,event=fix_sudo_enabled_trusty[0Ktravis_time:start:14268459[0Ktravis_time:end:14268459:start=1571866755550064237,finish=1571866755553255650,duration=3191413,event=update_glibc[0Ktravis_time:start:16a7d955[0Ktravis_time:end:16a7d955:start=1571866755557822890,finish=1571866755568407731,duration=10584841,event=clean_up_path[0Ktravis_time:start:031112b6[0Ktravis_time:end:031112b6:start=1571866755575537222,finish=1571866755584787400,duration=9250178,event=fix_resolv_conf[0Ktravis_time:start:167308a6[0Ktravis_time:end:167308a6:start=1571866755589694000,finish=1571866755603169809,duration=13475809,event=fix_etc_hosts[0Ktravis_time:start:11320752[0Ktravis_time:end:11320752:start=1571866755607775567,finish=1571866755618120770,duration=10345203,event=fix_mvn_settings_xml[0Ktravis_time:start:303ffed9[0Ktravis_time:end:303ffed9:start=1571866755625390754,finish=1571866755635644520,duration=10253766,event=no_ipv6_localhost[0Ktravis_time:start:05cd6f68[0Ktravis_time:end:05cd6f68:start=1571866755641496163,finish=1571866755644843395,duration=3347232,event=fix_etc_mavenrc[0Ktravis_time:start:1facbe90[0Ktravis_time:end:1facbe90:start=1571866755650432162,finish=1571866755654194363,duration=3762201,event=fix_wwdr_certificate[0Ktravis_time:start:04e20da4[0Ktravis_time:end:04e20da4:start=1571866755662682802,finish=1571866755688448655,duration=25765853,event=put_localhost_first[0Ktravis_time:start:02a644dc[0Ktravis_time:end:02a644dc:start=1571866755693913466,finish=1571866755698367837,duration=4454371,event=home_paths[0Ktravis_time:start:17601e40[0Ktravis_time:end:17601e40:start=1571866755706403684,finish=1571866755721001212,duration=14597528,event=disable_initramfs[0Ktravis_time:start:11299833[0Ktravis_time:end:11299833:start=1571866755725789390,finish=1571866756091474291,duration=365684901,event=disable_ssh_roaming[0Ktravis_time:start:110d5cd0[0Ktravis_time:end:110d5cd0:start=1571866756095961532,finish=1571866756098950075,duration=2988543,event=debug_tools[0Ktravis_time:start:02f42ca0[0Ktravis_time:end:02f42ca0:start=1571866756103886295,finish=1571866756109124244,duration=5237949,event=uninstall_oclint[0Ktravis_time:start:09855e73[0Ktravis_time:end:09855e73:start=1571866756114148689,finish=1571866756119274292,duration=5125603,event=rvm_use[0Ktravis_time:start:163813c2[0Ktravis_time:end:163813c2:start=1571866756123307509,finish=1571866756134393881,duration=11086372,event=rm_etc_boto_cfg[0Ktravis_time:start:0436a38e[0Ktravis_time:end:0436a38e:start=1571866756138817259,finish=1571866756141990830,duration=3173571,event=rm_oraclejdk8_symlink[0Ktravis_time:start:243ab72f[0Ktravis_time:end:243ab72f:start=1571866756146053636,finish=1571866756207807594,duration=61753958,event=enable_i386[0Ktravis_time:start:020d145a[0Ktravis_time:end:020d145a:start=1571866756213260358,finish=1571866756218392698,duration=5132340,event=update_rubygems[0Ktravis_time:start:014a2518[0Ktravis_time:end:014a2518:start=1571866756223431100,finish=1571866757276490231,duration=1053059131,event=ensure_path_components[0Ktravis_time:start:015a6d08[0Ktravis_time:end:015a6d08:start=1571866757281938100,finish=1571866757284892194,duration=2954094,event=redefine_curl[0Ktravis_time:start:008b52b6[0Ktravis_time:end:008b52b6:start=1571866757291927219,finish=1571866757351130124,duration=59202905,event=nonblock_pipe[0Ktravis_time:start:0213b484[0Ktravis_time:end:0213b484:start=1571866757358103664,finish=1571866760408450286,duration=3050346622,event=apt_get_update[0Ktravis_time:start:132bd492[0Ktravis_time:end:132bd492:start=1571866760413095559,finish=1571866760416097962,duration=3002403,event=deprecate_xcode_64[0Ktravis_time:start:05fb5100[0Ktravis_time:end:05fb5100:start=1571866760420153777,finish=1571866765385609556,duration=4965455779,event=update_heroku[0Ktravis_time:start:257a602b[0Ktravis_time:end:257a602b:start=1571866765391410609,finish=1571866765394450519,duration=3039910,event=shell_session_update[0Ktravis_time:start:26a11096[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3864
travis_fold:end:docker_mtu[0Ktravis_time:end:26a11096:start=1571866765398937172,finish=1571866766599571403,duration=1200634231,event=set_docker_mtu[0Ktravis_time:start:059ae8f2[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:059ae8f2:start=1571866766604533856,finish=1571866766673379827,duration=68845971,event=resolvconf[0Ktravis_time:start:3347258e[0Ktravis_time:end:3347258e:start=1571866766678227642,finish=1571866766781219230,duration=102991588,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00101dfc[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00101dfc:start=1571866766868781983,finish=1571866767447356689,duration=578574706,event=configure[0Ktravis_time:start:137a24c0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:137a24c0:start=1571866767453347816,finish=1571866778330597019,duration=10877249203,event=configure[0Ktravis_time:start:0d277673[0Ktravis_fold:start:services[0Ktravis_time:start:080e3c02[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:080e3c02:start=1571866778357299501,finish=1571866778373193600,duration=15894099,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:080e3c02:start=1571866778357299501,finish=1571866781378536925,duration=3021237424,event=services[0Ktravis_time:start:10425c4f[0Ktravis_time:end:10425c4f:start=1571866781383310818,finish=1571866781386602877,duration=3292059,event=fix_ps4[0Ktravis_time:start:02e13979[0K
travis_fold:start:git.checkout[0Ktravis_time:start:05ac58a5[0K$ git clone --depth=50 --branch=EderK-fix-push_args https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:05ac58a5:start=1571866781396157004,finish=1571866787773166279,duration=6377009275,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 62c825780a87ccd38c4be4616da1c30399112d8e
travis_fold:end:git.checkout[0K
travis_time:end:05ac58a5:start=1571866781396157004,finish=1571866788444119873,duration=7047962869,event=checkout[0Ktravis_time:start:28d03d1f[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:28d03d1f:start=1571866788449397466,finish=1571866788461032857,duration=11635391,event=env[0Ktravis_time:start:15651be2[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:15651be2:start=1571866788466600211,finish=1571866788475335799,duration=8735588,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0d5d133d[0K$ python push.py -s -t fe-fe --base Ubuntu1804.home
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/602035163/log.txt)