 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586477733) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3c3e92795247) 
## Last succesfull commits 
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
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
travis_time:end:0e25a5b3:start=1568806159752648183,finish=1568806159759619954,duration=6971771,event=show_system_info[0Ktravis_time:start:0c4b2ec5[0Ktravis_time:end:0c4b2ec5:start=1568806159762521484,finish=1568806159791668106,duration=29146622,event=rm_riak_source[0Ktravis_time:start:15d80618[0Ktravis_time:end:15d80618:start=1568806159794736535,finish=1568806159799840107,duration=5103572,event=fix_rwky_redis[0Ktravis_time:start:02834f1a[0Ktravis_time:end:02834f1a:start=1568806159802747245,finish=1568806160216431038,duration=413683793,event=wait_for_network[0Ktravis_time:start:15f8eeb7[0Ktravis_time:end:15f8eeb7:start=1568806160224689638,finish=1568806161872053757,duration=1647364119,event=update_apt_keys[0Ktravis_time:start:110bab60[0Ktravis_time:end:110bab60:start=1568806161876843548,finish=1568806162989183010,duration=1112339462,event=fix_hhvm_source[0Ktravis_time:start:01640caa[0Ktravis_time:end:01640caa:start=1568806162994474151,finish=1568806163004531080,duration=10056929,event=update_mongo_arch[0Ktravis_time:start:06c1fb15[0Ktravis_time:end:06c1fb15:start=1568806163009027430,finish=1568806163050574070,duration=41546640,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0b4cac20[0Ktravis_time:end:0b4cac20:start=1568806163055167921,finish=1568806163058006690,duration=2838769,event=update_glibc[0Ktravis_time:start:0d289440[0Ktravis_time:end:0d289440:start=1568806163062125648,finish=1568806163070977366,duration=8851718,event=clean_up_path[0Ktravis_time:start:02626de9[0Ktravis_time:end:02626de9:start=1568806163075108203,finish=1568806163083806653,duration=8698450,event=fix_resolv_conf[0Ktravis_time:start:1e0698a2[0Ktravis_time:end:1e0698a2:start=1568806163088146147,finish=1568806163098116585,duration=9970438,event=fix_etc_hosts[0Ktravis_time:start:234a57af[0Ktravis_time:end:234a57af:start=1568806163102363265,finish=1568806163112236286,duration=9873021,event=fix_mvn_settings_xml[0Ktravis_time:start:010d6604[0Ktravis_time:end:010d6604:start=1568806163117008390,finish=1568806163127315780,duration=10307390,event=no_ipv6_localhost[0Ktravis_time:start:18ddc0da[0Ktravis_time:end:18ddc0da:start=1568806163132482299,finish=1568806163135359539,duration=2877240,event=fix_etc_mavenrc[0Ktravis_time:start:2074df64[0Ktravis_time:end:2074df64:start=1568806163140128369,finish=1568806163143752953,duration=3624584,event=fix_wwdr_certificate[0Ktravis_time:start:138f6701[0Ktravis_time:end:138f6701:start=1568806163148308120,finish=1568806163175379662,duration=27071542,event=put_localhost_first[0Ktravis_time:start:03965e20[0Ktravis_time:end:03965e20:start=1568806163180132671,finish=1568806163184349420,duration=4216749,event=home_paths[0Ktravis_time:start:0afda98f[0Ktravis_time:end:0afda98f:start=1568806163189242648,finish=1568806163213253434,duration=24010786,event=disable_initramfs[0Ktravis_time:start:125b0fe0[0Ktravis_time:end:125b0fe0:start=1568806163217737162,finish=1568806163612697711,duration=394960549,event=disable_ssh_roaming[0Ktravis_time:start:00f80a18[0Ktravis_time:end:00f80a18:start=1568806163617579534,finish=1568806163620551545,duration=2972011,event=debug_tools[0Ktravis_time:start:00957ef0[0Ktravis_time:end:00957ef0:start=1568806163625067474,finish=1568806163629604753,duration=4537279,event=uninstall_oclint[0Ktravis_time:start:0005ddbc[0Ktravis_time:end:0005ddbc:start=1568806163634188469,finish=1568806163638740237,duration=4551768,event=rvm_use[0Ktravis_time:start:2357d758[0Ktravis_time:end:2357d758:start=1568806163643435764,finish=1568806163654720083,duration=11284319,event=rm_etc_boto_cfg[0Ktravis_time:start:21f59de4[0Ktravis_time:end:21f59de4:start=1568806163658592765,finish=1568806163661431009,duration=2838244,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1c29c9f1[0Ktravis_time:end:1c29c9f1:start=1568806163665184662,finish=1568806163732496278,duration=67311616,event=enable_i386[0Ktravis_time:start:0050b705[0Ktravis_time:end:0050b705:start=1568806163737057366,finish=1568806163742026144,duration=4968778,event=update_rubygems[0Ktravis_time:start:04411bea[0Ktravis_time:end:04411bea:start=1568806163746627334,finish=1568806164804279185,duration=1057651851,event=ensure_path_components[0Ktravis_time:start:27415404[0Ktravis_time:end:27415404:start=1568806164809615746,finish=1568806164812539067,duration=2923321,event=redefine_curl[0Ktravis_time:start:006e91e8[0Ktravis_time:end:006e91e8:start=1568806164817219402,finish=1568806164877162452,duration=59943050,event=nonblock_pipe[0Ktravis_time:start:03907f70[0Ktravis_time:end:03907f70:start=1568806164881867250,finish=1568806164925813643,duration=43946393,event=apt_get_update[0Ktravis_time:start:15b05620[0Ktravis_time:end:15b05620:start=1568806164930822392,finish=1568806164934171119,duration=3348727,event=deprecate_xcode_64[0Ktravis_time:start:0999496e[0Ktravis_time:end:0999496e:start=1568806164939069371,finish=1568806170516794860,duration=5577725489,event=update_heroku[0Ktravis_time:start:0c3c784e[0Ktravis_time:end:0c3c784e:start=1568806170521345695,finish=1568806170524227758,duration=2882063,event=shell_session_update[0Ktravis_time:start:0faa3516[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3867
travis_fold:end:docker_mtu[0Ktravis_time:end:0faa3516:start=1568806170528719054,finish=1568806171721505207,duration=1192786153,event=set_docker_mtu[0Ktravis_time:start:0e4f6b9d[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0e4f6b9d:start=1568806171726515633,finish=1568806171792073443,duration=65557810,event=resolvconf[0Ktravis_time:start:3470412f[0Ktravis_time:end:3470412f:start=1568806171796717321,finish=1568806171912904414,duration=116187093,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:041f114c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:041f114c:start=1568806171996410687,finish=1568806172313840865,duration=317430178,event=configure[0Ktravis_time:start:0092520d[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0092520d:start=1568806172319130989,finish=1568806182184768281,duration=9865637292,event=configure[0Ktravis_time:start:1428685e[0Ktravis_fold:start:services[0Ktravis_time:start:0a666e40[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0a666e40:start=1568806182211001948,finish=1568806182225859046,duration=14857098,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0a666e40:start=1568806182211001948,finish=1568806185230988579,duration=3019986631,event=services[0Ktravis_time:start:2b8795e0[0Ktravis_time:end:2b8795e0:start=1568806185236432607,finish=1568806185239506439,duration=3073832,event=fix_ps4[0Ktravis_time:start:07724cda[0K
travis_fold:start:git.checkout[0Ktravis_time:start:027597ee[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:027597ee:start=1568806185250013503,finish=1568806195521622648,duration=10271609145,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3c3e927952479f3d81847ce6139ede1bec7f9aff
travis_fold:end:git.checkout[0K
travis_time:end:027597ee:start=1568806185250013503,finish=1568806195982909039,duration=10732895536,event=checkout[0Ktravis_time:start:244e8d00[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:244e8d00:start=1568806195988058032,finish=1568806196000153621,duration=12095589,event=env[0Ktravis_time:start:164ebe94[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:164ebe94:start=1568806196005532770,finish=1568806196011544454,duration=6011684,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:01bac6b5[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-ccx,fe-fe,of-ccx_fsi,nutils-of,of-of,bindings,dealii-of,su2-ccx,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:01bac6b5:start=1568806196366439109,finish=1568806196434118786,duration=67679677,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:18aaf037[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586477746/log.txt)