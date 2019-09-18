 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478260) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3c3e92795247...4d912263806c) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
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
travis_time:end:2623a5ea:start=1568808145422281005,finish=1568808145429281294,duration=7000289,event=show_system_info[0Ktravis_time:start:0485844c[0Ktravis_time:end:0485844c:start=1568808145432336367,finish=1568808145458698567,duration=26362200,event=rm_riak_source[0Ktravis_time:start:2e1cb692[0Ktravis_time:end:2e1cb692:start=1568808145462160598,finish=1568808145467843402,duration=5682804,event=fix_rwky_redis[0Ktravis_time:start:32375b88[0Ktravis_time:end:32375b88:start=1568808145471005895,finish=1568808151095591262,duration=5624585367,event=wait_for_network[0Ktravis_time:start:04dd0e24[0Ktravis_time:end:04dd0e24:start=1568808151101396694,finish=1568808154464882114,duration=3363485420,event=update_apt_keys[0Ktravis_time:start:00a9d3b2[0Ktravis_time:end:00a9d3b2:start=1568808154470005392,finish=1568808155538517025,duration=1068511633,event=fix_hhvm_source[0Ktravis_time:start:012a829e[0Ktravis_time:end:012a829e:start=1568808155543456702,finish=1568808155554363854,duration=10907152,event=update_mongo_arch[0Ktravis_time:start:003f0fe0[0Ktravis_time:end:003f0fe0:start=1568808155559124277,finish=1568808155603290979,duration=44166702,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0b60ed46[0Ktravis_time:end:0b60ed46:start=1568808155608259846,finish=1568808155611317997,duration=3058151,event=update_glibc[0Ktravis_time:start:1c3fb5eb[0Ktravis_time:end:1c3fb5eb:start=1568808155615712442,finish=1568808155625717563,duration=10005121,event=clean_up_path[0Ktravis_time:start:288984ce[0Ktravis_time:end:288984ce:start=1568808155630118965,finish=1568808155638918279,duration=8799314,event=fix_resolv_conf[0Ktravis_time:start:07d03a94[0Ktravis_time:end:07d03a94:start=1568808155643563645,finish=1568808155652814974,duration=9251329,event=fix_etc_hosts[0Ktravis_time:start:00aa35fa[0Ktravis_time:end:00aa35fa:start=1568808155656778970,finish=1568808155666977124,duration=10198154,event=fix_mvn_settings_xml[0Ktravis_time:start:0686beb8[0Ktravis_time:end:0686beb8:start=1568808155671524277,finish=1568808155681917021,duration=10392744,event=no_ipv6_localhost[0Ktravis_time:start:26f565ef[0Ktravis_time:end:26f565ef:start=1568808155686579706,finish=1568808155689321199,duration=2741493,event=fix_etc_mavenrc[0Ktravis_time:start:04155bb4[0Ktravis_time:end:04155bb4:start=1568808155693901414,finish=1568808155697899228,duration=3997814,event=fix_wwdr_certificate[0Ktravis_time:start:0efa918c[0Ktravis_time:end:0efa918c:start=1568808155702867894,finish=1568808155730543133,duration=27675239,event=put_localhost_first[0Ktravis_time:start:04a2ec80[0Ktravis_time:end:04a2ec80:start=1568808155735386920,finish=1568808155739457042,duration=4070122,event=home_paths[0Ktravis_time:start:08d7d920[0Ktravis_time:end:08d7d920:start=1568808155743723286,finish=1568808155757362270,duration=13638984,event=disable_initramfs[0Ktravis_time:start:16ac657a[0Ktravis_time:end:16ac657a:start=1568808155762018904,finish=1568808156137083385,duration=375064481,event=disable_ssh_roaming[0Ktravis_time:start:0d04caa3[0Ktravis_time:end:0d04caa3:start=1568808156141524112,finish=1568808156144307874,duration=2783762,event=debug_tools[0Ktravis_time:start:01c90812[0Ktravis_time:end:01c90812:start=1568808156148875170,finish=1568808156152462850,duration=3587680,event=uninstall_oclint[0Ktravis_time:start:0d0e44d5[0Ktravis_time:end:0d0e44d5:start=1568808156157225613,finish=1568808156160740039,duration=3514426,event=rvm_use[0Ktravis_time:start:091edc60[0Ktravis_time:end:091edc60:start=1568808156165413314,finish=1568808156174187180,duration=8773866,event=rm_etc_boto_cfg[0Ktravis_time:start:28c60965[0Ktravis_time:end:28c60965:start=1568808156178892257,finish=1568808156182312671,duration=3420414,event=rm_oraclejdk8_symlink[0Ktravis_time:start:04b74db4[0Ktravis_time:end:04b74db4:start=1568808156187500909,finish=1568808156252252409,duration=64751500,event=enable_i386[0Ktravis_time:start:02f84b1c[0Ktravis_time:end:02f84b1c:start=1568808156257013899,finish=1568808156262009954,duration=4996055,event=update_rubygems[0Ktravis_time:start:3446ad80[0Ktravis_time:end:3446ad80:start=1568808156267170937,finish=1568808157306432969,duration=1039262032,event=ensure_path_components[0Ktravis_time:start:0d231097[0Ktravis_time:end:0d231097:start=1568808157312468875,finish=1568808157315577078,duration=3108203,event=redefine_curl[0Ktravis_time:start:0431660f[0Ktravis_time:end:0431660f:start=1568808157320733525,finish=1568808157376019533,duration=55286008,event=nonblock_pipe[0Ktravis_time:start:1403d400[0Ktravis_time:end:1403d400:start=1568808157380413531,finish=1568808157425737613,duration=45324082,event=apt_get_update[0Ktravis_time:start:046116a8[0Ktravis_time:end:046116a8:start=1568808157430263004,finish=1568808157433435310,duration=3172306,event=deprecate_xcode_64[0Ktravis_time:start:10bb4694[0Ktravis_time:end:10bb4694:start=1568808157438052006,finish=1568808162635725230,duration=5197673224,event=update_heroku[0Ktravis_time:start:09651090[0Ktravis_time:end:09651090:start=1568808162640352812,finish=1568808162643917019,duration=3564207,event=shell_session_update[0Ktravis_time:start:3b80c738[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3902
travis_fold:end:docker_mtu[0Ktravis_time:end:3b80c738:start=1568808162648506516,finish=1568808163854306948,duration=1205800432,event=set_docker_mtu[0Ktravis_time:start:2815a340[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2815a340:start=1568808163859216729,finish=1568808163936388297,duration=77171568,event=resolvconf[0Ktravis_time:start:15a7d734[0Ktravis_time:end:15a7d734:start=1568808163942636844,finish=1568808164069950468,duration=127313624,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0fde59eb[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0fde59eb:start=1568808164156729485,finish=1568808164483107275,duration=326377790,event=configure[0Ktravis_time:start:037b8baf[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:037b8baf:start=1568808164488707132,finish=1568808175168347070,duration=10679639938,event=configure[0Ktravis_time:start:1957d720[0Ktravis_fold:start:services[0Ktravis_time:start:1ab4f0b0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1ab4f0b0:start=1568808175194284387,finish=1568808175208718845,duration=14434458,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1ab4f0b0:start=1568808175194284387,finish=1568808178213766678,duration=3019482291,event=services[0Ktravis_time:start:06617611[0Ktravis_time:end:06617611:start=1568808178217946974,finish=1568808178220671990,duration=2725016,event=fix_ps4[0Ktravis_time:start:0f8a7f28[0K
travis_fold:start:git.checkout[0Ktravis_time:start:05b20edf[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:05b20edf:start=1568808178228404639,finish=1568808188567311990,duration=10338907351,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4d912263806c85d105a3cfc8dba374f4f3a4853a
travis_fold:end:git.checkout[0K
travis_time:end:05b20edf:start=1568808178228404639,finish=1568808189083442448,duration=10855037809,event=checkout[0Ktravis_time:start:0bef53c2[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0bef53c2:start=1568808189089073253,finish=1568808189101791293,duration=12718040,event=env[0Ktravis_time:start:00a4d3c8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00a4d3c8:start=1568808189106494386,finish=1568808189115408649,duration=8914263,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0ba5399d[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-ccx,nutils-of,dealii-of,fe-fe,su2-ccx,of-of_np,of-ccx_fsi,bindings,of-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0ba5399d:start=1568808189476331629,finish=1568808189543698961,duration=67367332,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:093a07e8[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478275/log.txt)