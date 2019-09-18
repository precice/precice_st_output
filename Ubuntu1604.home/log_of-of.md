 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510170) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/40d6daa277c6...b989e40888b7) 
## Last succesfull commits 
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
travis_time:end:08b28fe0:start=1568815051506605427,finish=1568815051512635187,duration=6029760,event=show_system_info[0Ktravis_time:start:120fc4f0[0Ktravis_time:end:120fc4f0:start=1568815051515608984,finish=1568815051542924993,duration=27316009,event=rm_riak_source[0Ktravis_time:start:12b1494e[0Ktravis_time:end:12b1494e:start=1568815051546787687,finish=1568815051553053980,duration=6266293,event=fix_rwky_redis[0Ktravis_time:start:0def015c[0Ktravis_time:end:0def015c:start=1568815051556693035,finish=1568815052001880885,duration=445187850,event=wait_for_network[0Ktravis_time:start:01de39f8[0Ktravis_time:end:01de39f8:start=1568815052007304543,finish=1568815053607538430,duration=1600233887,event=update_apt_keys[0Ktravis_time:start:091a1ae4[0Ktravis_time:end:091a1ae4:start=1568815053612896051,finish=1568815054740568086,duration=1127672035,event=fix_hhvm_source[0Ktravis_time:start:0714ade8[0Ktravis_time:end:0714ade8:start=1568815054747613283,finish=1568815054760051256,duration=12437973,event=update_mongo_arch[0Ktravis_time:start:09037677[0Ktravis_time:end:09037677:start=1568815054765387361,finish=1568815054813115960,duration=47728599,event=fix_sudo_enabled_trusty[0Ktravis_time:start:091a0548[0Ktravis_time:end:091a0548:start=1568815054819363206,finish=1568815054822615477,duration=3252271,event=update_glibc[0Ktravis_time:start:3709b3f7[0Ktravis_time:end:3709b3f7:start=1568815054829360404,finish=1568815054840720507,duration=11360103,event=clean_up_path[0Ktravis_time:start:01c8c45a[0Ktravis_time:end:01c8c45a:start=1568815054846784060,finish=1568815054856946110,duration=10162050,event=fix_resolv_conf[0Ktravis_time:start:0e61d164[0Ktravis_time:end:0e61d164:start=1568815054863453524,finish=1568815054875031197,duration=11577673,event=fix_etc_hosts[0Ktravis_time:start:0dc0eccd[0Ktravis_time:end:0dc0eccd:start=1568815054881006546,finish=1568815054895733074,duration=14726528,event=fix_mvn_settings_xml[0Ktravis_time:start:10226c66[0Ktravis_time:end:10226c66:start=1568815054901474489,finish=1568815054915657583,duration=14183094,event=no_ipv6_localhost[0Ktravis_time:start:00584f5b[0Ktravis_time:end:00584f5b:start=1568815054920889623,finish=1568815054924490377,duration=3600754,event=fix_etc_mavenrc[0Ktravis_time:start:03ff42fc[0Ktravis_time:end:03ff42fc:start=1568815054929680268,finish=1568815054934495677,duration=4815409,event=fix_wwdr_certificate[0Ktravis_time:start:2cb2eab0[0Ktravis_time:end:2cb2eab0:start=1568815054939481098,finish=1568815054974514456,duration=35033358,event=put_localhost_first[0Ktravis_time:start:02dcd9ec[0Ktravis_time:end:02dcd9ec:start=1568815054979755313,finish=1568815054984173825,duration=4418512,event=home_paths[0Ktravis_time:start:087cd4f0[0Ktravis_time:end:087cd4f0:start=1568815054989702236,finish=1568815055005338061,duration=15635825,event=disable_initramfs[0Ktravis_time:start:1234208f[0Ktravis_time:end:1234208f:start=1568815055011558230,finish=1568815055349278874,duration=337720644,event=disable_ssh_roaming[0Ktravis_time:start:3ac6b74a[0Ktravis_time:end:3ac6b74a:start=1568815055355474680,finish=1568815055359220344,duration=3745664,event=debug_tools[0Ktravis_time:start:0ca3be46[0Ktravis_time:end:0ca3be46:start=1568815055365252652,finish=1568815055369926664,duration=4674012,event=uninstall_oclint[0Ktravis_time:start:0bed6ce0[0Ktravis_time:end:0bed6ce0:start=1568815055375139715,finish=1568815055381302987,duration=6163272,event=rvm_use[0Ktravis_time:start:002eca5c[0Ktravis_time:end:002eca5c:start=1568815055386426863,finish=1568815055396111681,duration=9684818,event=rm_etc_boto_cfg[0Ktravis_time:start:1f610780[0Ktravis_time:end:1f610780:start=1568815055403051357,finish=1568815055406158794,duration=3107437,event=rm_oraclejdk8_symlink[0Ktravis_time:start:033ed597[0Ktravis_time:end:033ed597:start=1568815055412403537,finish=1568815055476007346,duration=63603809,event=enable_i386[0Ktravis_time:start:019bf866[0Ktravis_time:end:019bf866:start=1568815055481652292,finish=1568815055487564588,duration=5912296,event=update_rubygems[0Ktravis_time:start:006d4914[0Ktravis_time:end:006d4914:start=1568815055492481449,finish=1568815056671539820,duration=1179058371,event=ensure_path_components[0Ktravis_time:start:03f08284[0Ktravis_time:end:03f08284:start=1568815056678383731,finish=1568815056681731299,duration=3347568,event=redefine_curl[0Ktravis_time:start:055aa7d7[0Ktravis_time:end:055aa7d7:start=1568815056687527972,finish=1568815056751216150,duration=63688178,event=nonblock_pipe[0Ktravis_time:start:09f97aa0[0Ktravis_time:end:09f97aa0:start=1568815056756714972,finish=1568815056804840622,duration=48125650,event=apt_get_update[0Ktravis_time:start:00dcb5ff[0Ktravis_time:end:00dcb5ff:start=1568815056810801079,finish=1568815056814762551,duration=3961472,event=deprecate_xcode_64[0Ktravis_time:start:081dfbc0[0Ktravis_time:end:081dfbc0:start=1568815056821704439,finish=1568815061857880767,duration=5036176328,event=update_heroku[0Ktravis_time:start:00941592[0Ktravis_time:end:00941592:start=1568815061862557187,finish=1568815061865268338,duration=2711151,event=shell_session_update[0Ktravis_time:start:06f29dd7[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3862
travis_fold:end:docker_mtu[0Ktravis_time:end:06f29dd7:start=1568815061869239070,finish=1568815063068383374,duration=1199144304,event=set_docker_mtu[0Ktravis_time:start:02986248[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:02986248:start=1568815063073907831,finish=1568815063141085702,duration=67177871,event=resolvconf[0Ktravis_time:start:020a5dfe[0Ktravis_time:end:020a5dfe:start=1568815063145929805,finish=1568815063249725417,duration=103795612,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00546711[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00546711:start=1568815063334913342,finish=1568815064154561518,duration=819648176,event=configure[0Ktravis_time:start:2f0e5e82[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2f0e5e82:start=1568815064162602346,finish=1568815076751633263,duration=12589030917,event=configure[0Ktravis_time:start:12ba20e4[0Ktravis_fold:start:services[0Ktravis_time:start:2b774170[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:2b774170:start=1568815076779689885,finish=1568815076796110465,duration=16420580,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2b774170:start=1568815076779689885,finish=1568815079803317207,duration=3023627322,event=services[0Ktravis_time:start:063ede60[0Ktravis_time:end:063ede60:start=1568815079807432728,finish=1568815079810203512,duration=2770784,event=fix_ps4[0Ktravis_time:start:005004b4[0K
travis_fold:start:git.checkout[0Ktravis_time:start:000b9574[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:000b9574:start=1568815079819574767,finish=1568815091285977996,duration=11466403229,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b989e40888b7bc80b4a7d6d823b98fc3ebb61025
travis_fold:end:git.checkout[0K
travis_time:end:000b9574:start=1568815079819574767,finish=1568815091525076672,duration=11705501905,event=checkout[0Ktravis_time:start:142e75a2[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:142e75a2:start=1568815091530976030,finish=1568815091543438272,duration=12462242,event=env[0Ktravis_time:start:17a0d678[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:17a0d678:start=1568815091551380257,finish=1568815091558800369,duration=7420112,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1bcefdc6[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-of_np,su2-ccx,bindings,of-ccx,of-ccx_fsi,nutils-of,of-of,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:1bcefdc6:start=1568815091964646957,finish=1568815092036617116,duration=71970159,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:07c45548[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510184/log.txt)