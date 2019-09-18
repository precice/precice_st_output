 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478260) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3c3e92795247...4d912263806c) 
## Last succesfull commits 
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
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
travis_time:end:00802d5f:start=1568808786283357765,finish=1568808786289971904,duration=6614139,event=show_system_info[0Ktravis_time:start:02000533[0Ktravis_time:end:02000533:start=1568808786293020716,finish=1568808786321165917,duration=28145201,event=rm_riak_source[0Ktravis_time:start:039159cc[0Ktravis_time:end:039159cc:start=1568808786324297001,finish=1568808786329382371,duration=5085370,event=fix_rwky_redis[0Ktravis_time:start:2d5c04f4[0Ktravis_time:end:2d5c04f4:start=1568808786332245638,finish=1568808786762823290,duration=430577652,event=wait_for_network[0Ktravis_time:start:13175dc0[0Ktravis_time:end:13175dc0:start=1568808786767327254,finish=1568808788380493021,duration=1613165767,event=update_apt_keys[0Ktravis_time:start:1002a96b[0Ktravis_time:end:1002a96b:start=1568808788384381958,finish=1568808789505616970,duration=1121235012,event=fix_hhvm_source[0Ktravis_time:start:0dd21f01[0Ktravis_time:end:0dd21f01:start=1568808789510663631,finish=1568808789521387628,duration=10723997,event=update_mongo_arch[0Ktravis_time:start:1abf65a2[0Ktravis_time:end:1abf65a2:start=1568808789526462957,finish=1568808789569315823,duration=42852866,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0fb97922[0Ktravis_time:end:0fb97922:start=1568808789574001429,finish=1568808789576973479,duration=2972050,event=update_glibc[0Ktravis_time:start:0a1dfcd2[0Ktravis_time:end:0a1dfcd2:start=1568808789580778411,finish=1568808789591212944,duration=10434533,event=clean_up_path[0Ktravis_time:start:165384a6[0Ktravis_time:end:165384a6:start=1568808789597668735,finish=1568808789606121265,duration=8452530,event=fix_resolv_conf[0Ktravis_time:start:13d16530[0Ktravis_time:end:13d16530:start=1568808789609945840,finish=1568808789621289615,duration=11343775,event=fix_etc_hosts[0Ktravis_time:start:266b9be8[0Ktravis_time:end:266b9be8:start=1568808789626550743,finish=1568808789635893533,duration=9342790,event=fix_mvn_settings_xml[0Ktravis_time:start:0d98facd[0Ktravis_time:end:0d98facd:start=1568808789640879113,finish=1568808789654197650,duration=13318537,event=no_ipv6_localhost[0Ktravis_time:start:0d656646[0Ktravis_time:end:0d656646:start=1568808789658633239,finish=1568808789662002979,duration=3369740,event=fix_etc_mavenrc[0Ktravis_time:start:04ea4454[0Ktravis_time:end:04ea4454:start=1568808789665968423,finish=1568808789669812775,duration=3844352,event=fix_wwdr_certificate[0Ktravis_time:start:0d1b1bf2[0Ktravis_time:end:0d1b1bf2:start=1568808789674159522,finish=1568808789704331972,duration=30172450,event=put_localhost_first[0Ktravis_time:start:021c8310[0Ktravis_time:end:021c8310:start=1568808789708897962,finish=1568808789713576148,duration=4678186,event=home_paths[0Ktravis_time:start:0c282312[0Ktravis_time:end:0c282312:start=1568808789719479174,finish=1568808789733136746,duration=13657572,event=disable_initramfs[0Ktravis_time:start:1ad24ed0[0Ktravis_time:end:1ad24ed0:start=1568808789737811754,finish=1568808790088331986,duration=350520232,event=disable_ssh_roaming[0Ktravis_time:start:01eb2014[0Ktravis_time:end:01eb2014:start=1568808790093152894,finish=1568808790095806409,duration=2653515,event=debug_tools[0Ktravis_time:start:265cd2aa[0Ktravis_time:end:265cd2aa:start=1568808790100503059,finish=1568808790103983658,duration=3480599,event=uninstall_oclint[0Ktravis_time:start:136111fc[0Ktravis_time:end:136111fc:start=1568808790108371676,finish=1568808790111740955,duration=3369279,event=rvm_use[0Ktravis_time:start:0ed27857[0Ktravis_time:end:0ed27857:start=1568808790116125960,finish=1568808790124372676,duration=8246716,event=rm_etc_boto_cfg[0Ktravis_time:start:19a31c06[0Ktravis_time:end:19a31c06:start=1568808790129313072,finish=1568808790132531745,duration=3218673,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0154b06c[0Ktravis_time:end:0154b06c:start=1568808790137541880,finish=1568808790194425062,duration=56883182,event=enable_i386[0Ktravis_time:start:14a5750f[0Ktravis_time:end:14a5750f:start=1568808790199385142,finish=1568808790204061342,duration=4676200,event=update_rubygems[0Ktravis_time:start:2a4faf25[0Ktravis_time:end:2a4faf25:start=1568808790208703031,finish=1568808791229388927,duration=1020685896,event=ensure_path_components[0Ktravis_time:start:0162d8a8[0Ktravis_time:end:0162d8a8:start=1568808791233957947,finish=1568808791236860454,duration=2902507,event=redefine_curl[0Ktravis_time:start:06beeda4[0Ktravis_time:end:06beeda4:start=1568808791240559801,finish=1568808791294808312,duration=54248511,event=nonblock_pipe[0Ktravis_time:start:00584f94[0Ktravis_time:end:00584f94:start=1568808791299815623,finish=1568808791340750592,duration=40934969,event=apt_get_update[0Ktravis_time:start:0441f213[0Ktravis_time:end:0441f213:start=1568808791345240100,finish=1568808791347963231,duration=2723131,event=deprecate_xcode_64[0Ktravis_time:start:0842fdb7[0Ktravis_time:end:0842fdb7:start=1568808791352687144,finish=1568808796513428355,duration=5160741211,event=update_heroku[0Ktravis_time:start:000af380[0Ktravis_time:end:000af380:start=1568808796517733204,finish=1568808796520436484,duration=2703280,event=shell_session_update[0Ktravis_time:start:1192c110[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3915
travis_fold:end:docker_mtu[0Ktravis_time:end:1192c110:start=1568808796525009297,finish=1568808797720205473,duration=1195196176,event=set_docker_mtu[0Ktravis_time:start:04c09b60[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:04c09b60:start=1568808797724815931,finish=1568808797794973690,duration=70157759,event=resolvconf[0Ktravis_time:start:135f21dc[0Ktravis_time:end:135f21dc:start=1568808797799833714,finish=1568808797910531935,duration=110698221,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1a9a98d8[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1a9a98d8:start=1568808797994324688,finish=1568808798375857492,duration=381532804,event=configure[0Ktravis_time:start:0052d21c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0052d21c:start=1568808798381507810,finish=1568808808181036750,duration=9799528940,event=configure[0Ktravis_time:start:20a05ce2[0Ktravis_fold:start:services[0Ktravis_time:start:3a98a497[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:3a98a497:start=1568808808206326947,finish=1568808808221106758,duration=14779811,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:3a98a497:start=1568808808206326947,finish=1568808811225906818,duration=3019579871,event=services[0Ktravis_time:start:0451fb0c[0Ktravis_time:end:0451fb0c:start=1568808811230089184,finish=1568808811232716759,duration=2627575,event=fix_ps4[0Ktravis_time:start:100be4c0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:2d9bba2a[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:2d9bba2a:start=1568808811241795479,finish=1568808821396887105,duration=10155091626,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4d912263806c85d105a3cfc8dba374f4f3a4853a
travis_fold:end:git.checkout[0K
travis_time:end:2d9bba2a:start=1568808811241795479,finish=1568808821727044348,duration=10485248869,event=checkout[0Ktravis_time:start:34dc5184[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:34dc5184:start=1568808821731577612,finish=1568808821741490157,duration=9912545,event=env[0Ktravis_time:start:07745394[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:07745394:start=1568808821745967539,finish=1568808821751534597,duration=5567058,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0dbec650[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {of-of,of-ccx_fsi,fe-fe,su2-ccx,dealii-of,nutils-of,bindings,of-of_np,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0dbec650:start=1568808822091561649,finish=1568808822155644011,duration=64082362,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1dce0b8c[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478280/log.txt)