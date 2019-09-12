 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584299312) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/95) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903) 
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
travis_time:end:1dc2cbb8:start=1568328052415571032,finish=1568328052423143486,duration=7572454,event=show_system_info[0Ktravis_time:start:05edda2c[0Ktravis_time:end:05edda2c:start=1568328052426037196,finish=1568328052459462462,duration=33425266,event=rm_riak_source[0Ktravis_time:start:12fbdb6f[0Ktravis_time:end:12fbdb6f:start=1568328052462677763,finish=1568328052467896828,duration=5219065,event=fix_rwky_redis[0Ktravis_time:start:069eee40[0Ktravis_time:end:069eee40:start=1568328052471142229,finish=1568328052866071987,duration=394929758,event=wait_for_network[0Ktravis_time:start:00919bb4[0Ktravis_time:end:00919bb4:start=1568328052875579723,finish=1568328054514038312,duration=1638458589,event=update_apt_keys[0Ktravis_time:start:062ae3e8[0Ktravis_time:end:062ae3e8:start=1568328054520626022,finish=1568328055616115843,duration=1095489821,event=fix_hhvm_source[0Ktravis_time:start:1f6df208[0Ktravis_time:end:1f6df208:start=1568328055620489991,finish=1568328055630647130,duration=10157139,event=update_mongo_arch[0Ktravis_time:start:20a67a64[0Ktravis_time:end:20a67a64:start=1568328055635012384,finish=1568328055676744497,duration=41732113,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0bbce7c8[0Ktravis_time:end:0bbce7c8:start=1568328055682318841,finish=1568328055686003794,duration=3684953,event=update_glibc[0Ktravis_time:start:007c84aa[0Ktravis_time:end:007c84aa:start=1568328055691530172,finish=1568328055700391920,duration=8861748,event=clean_up_path[0Ktravis_time:start:0f315a0c[0Ktravis_time:end:0f315a0c:start=1568328055704680980,finish=1568328055713985238,duration=9304258,event=fix_resolv_conf[0Ktravis_time:start:06b76ac0[0Ktravis_time:end:06b76ac0:start=1568328055718896092,finish=1568328055730007252,duration=11111160,event=fix_etc_hosts[0Ktravis_time:start:17c3ca12[0Ktravis_time:end:17c3ca12:start=1568328055734594925,finish=1568328055745015420,duration=10420495,event=fix_mvn_settings_xml[0Ktravis_time:start:25c40357[0Ktravis_time:end:25c40357:start=1568328055750229827,finish=1568328055761999300,duration=11769473,event=no_ipv6_localhost[0Ktravis_time:start:00c4609e[0Ktravis_time:end:00c4609e:start=1568328055766923020,finish=1568328055770226125,duration=3303105,event=fix_etc_mavenrc[0Ktravis_time:start:0fc90f18[0Ktravis_time:end:0fc90f18:start=1568328055774614311,finish=1568328055779465961,duration=4851650,event=fix_wwdr_certificate[0Ktravis_time:start:0b95b84b[0Ktravis_time:end:0b95b84b:start=1568328055783654080,finish=1568328055818054232,duration=34400152,event=put_localhost_first[0Ktravis_time:start:2920eec8[0Ktravis_time:end:2920eec8:start=1568328055821966230,finish=1568328055826188088,duration=4221858,event=home_paths[0Ktravis_time:start:06a350bc[0Ktravis_time:end:06a350bc:start=1568328055830500370,finish=1568328055846994881,duration=16494511,event=disable_initramfs[0Ktravis_time:start:000f26ca[0Ktravis_time:end:000f26ca:start=1568328055852005592,finish=1568328056210861783,duration=358856191,event=disable_ssh_roaming[0Ktravis_time:start:20b73664[0Ktravis_time:end:20b73664:start=1568328056215635125,finish=1568328056218553776,duration=2918651,event=debug_tools[0Ktravis_time:start:0ef3a1c8[0Ktravis_time:end:0ef3a1c8:start=1568328056223579028,finish=1568328056227933830,duration=4354802,event=uninstall_oclint[0Ktravis_time:start:0446b6d2[0Ktravis_time:end:0446b6d2:start=1568328056232915913,finish=1568328056237211343,duration=4295430,event=rvm_use[0Ktravis_time:start:2b76a5e0[0Ktravis_time:end:2b76a5e0:start=1568328056245841830,finish=1568328056253949729,duration=8107899,event=rm_etc_boto_cfg[0Ktravis_time:start:216227c3[0Ktravis_time:end:216227c3:start=1568328056258493916,finish=1568328056261096826,duration=2602910,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0421e937[0Ktravis_time:end:0421e937:start=1568328056266217119,finish=1568328056322982722,duration=56765603,event=enable_i386[0Ktravis_time:start:10a4f856[0Ktravis_time:end:10a4f856:start=1568328056327550877,finish=1568328056331957983,duration=4407106,event=update_rubygems[0Ktravis_time:start:07d31e58[0Ktravis_time:end:07d31e58:start=1568328056335952814,finish=1568328057357776662,duration=1021823848,event=ensure_path_components[0Ktravis_time:start:08005b93[0Ktravis_time:end:08005b93:start=1568328057362330590,finish=1568328057365103335,duration=2772745,event=redefine_curl[0Ktravis_time:start:06985f84[0Ktravis_time:end:06985f84:start=1568328057369418940,finish=1568328057424869703,duration=55450763,event=nonblock_pipe[0Ktravis_time:start:0b1c1035[0Ktravis_time:end:0b1c1035:start=1568328057429415540,finish=1568328057498087771,duration=68672231,event=apt_get_update[0Ktravis_time:start:1f63c0c1[0Ktravis_time:end:1f63c0c1:start=1568328057502544115,finish=1568328057505414045,duration=2869930,event=deprecate_xcode_64[0Ktravis_time:start:14f36ec0[0Ktravis_time:end:14f36ec0:start=1568328057511321732,finish=1568328062952995403,duration=5441673671,event=update_heroku[0Ktravis_time:start:04e7d8e0[0Ktravis_time:end:04e7d8e0:start=1568328062958215262,finish=1568328062961195606,duration=2980344,event=shell_session_update[0Ktravis_time:start:24322ab6[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3860
travis_fold:end:docker_mtu[0Ktravis_time:end:24322ab6:start=1568328062965471910,finish=1568328064174931455,duration=1209459545,event=set_docker_mtu[0Ktravis_time:start:163104fe[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:163104fe:start=1568328064179851658,finish=1568328064249093887,duration=69242229,event=resolvconf[0Ktravis_time:start:11f1f0ed[0Ktravis_time:end:11f1f0ed:start=1568328064253733220,finish=1568328064374530609,duration=120797389,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:136b492b[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:136b492b:start=1568328064458158134,finish=1568328064707289092,duration=249130958,event=configure[0Ktravis_time:start:09b5f348[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:09b5f348:start=1568328064712836803,finish=1568328074380585003,duration=9667748200,event=configure[0Ktravis_time:start:1509c97c[0Ktravis_fold:start:services[0Ktravis_time:start:23d43848[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:23d43848:start=1568328074406771566,finish=1568328074421595076,duration=14823510,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:23d43848:start=1568328074406771566,finish=1568328077426573500,duration=3019801934,event=services[0Ktravis_time:start:018fdaab[0Ktravis_time:end:018fdaab:start=1568328077431221422,finish=1568328077434420880,duration=3199458,event=fix_ps4[0Ktravis_time:start:004b7f83[0K
travis_fold:start:git.checkout[0Ktravis_time:start:281c5318[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:281c5318:start=1568328077443268188,finish=1568328087339866231,duration=9896598043,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:1f3caba1[0K$ git fetch origin +refs/pull/95/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/95/merge -> FETCH_HEAD
travis_time:end:1f3caba1:start=1568328087344286048,finish=1568328087765665974,duration=421379926,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:1f3caba1:start=1568328087344286048,finish=1568328088039469007,duration=695182959,event=checkout[0Ktravis_time:start:0078a4e8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0078a4e8:start=1568328088043596372,finish=1568328088057387846,duration=13791474,event=env[0Ktravis_time:start:133f9570[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:133f9570:start=1568328088062775159,finish=1568328088072751417,duration=9976258,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:01329ca6[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-of_np,su2-ccx,bindings,of-ccx_fsi,of-ccx,nutils-of,of-of,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:01329ca6:start=1568328088422115663,finish=1568328088488746080,duration=66630417,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:060664b9[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584299327/log.txt)