 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586517772) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63e83084ff16...628c8f57e99a) 
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
travis_time:end:0bbc1ba4:start=1568823391594044708,finish=1568823391607242993,duration=13198285,event=show_system_info[0Ktravis_time:start:20a4f347[0Ktravis_time:end:20a4f347:start=1568823391610277437,finish=1568823391644442055,duration=34164618,event=rm_riak_source[0Ktravis_time:start:255bc518[0Ktravis_time:end:255bc518:start=1568823391647563092,finish=1568823391652946663,duration=5383571,event=fix_rwky_redis[0Ktravis_time:start:19988918[0Ktravis_time:end:19988918:start=1568823391655980693,finish=1568823392087692659,duration=431711966,event=wait_for_network[0Ktravis_time:start:0bd6184e[0Ktravis_time:end:0bd6184e:start=1568823392095374598,finish=1568823393752765573,duration=1657390975,event=update_apt_keys[0Ktravis_time:start:1d3efb00[0Ktravis_time:end:1d3efb00:start=1568823393757283762,finish=1568823394887412655,duration=1130128893,event=fix_hhvm_source[0Ktravis_time:start:0625f734[0Ktravis_time:end:0625f734:start=1568823394892689699,finish=1568823394903070919,duration=10381220,event=update_mongo_arch[0Ktravis_time:start:01fcb6cf[0Ktravis_time:end:01fcb6cf:start=1568823394907063459,finish=1568823394955931911,duration=48868452,event=fix_sudo_enabled_trusty[0Ktravis_time:start:10e18780[0Ktravis_time:end:10e18780:start=1568823394961079316,finish=1568823394964141183,duration=3061867,event=update_glibc[0Ktravis_time:start:0a5633e1[0Ktravis_time:end:0a5633e1:start=1568823394969015168,finish=1568823394982733745,duration=13718577,event=clean_up_path[0Ktravis_time:start:2bc32a23[0Ktravis_time:end:2bc32a23:start=1568823394987390297,finish=1568823394999984386,duration=12594089,event=fix_resolv_conf[0Ktravis_time:start:011bcb7a[0Ktravis_time:end:011bcb7a:start=1568823395005483088,finish=1568823395016262631,duration=10779543,event=fix_etc_hosts[0Ktravis_time:start:110e886c[0Ktravis_time:end:110e886c:start=1568823395022438652,finish=1568823395032093933,duration=9655281,event=fix_mvn_settings_xml[0Ktravis_time:start:0659d300[0Ktravis_time:end:0659d300:start=1568823395037787245,finish=1568823395049306597,duration=11519352,event=no_ipv6_localhost[0Ktravis_time:start:1da4589a[0Ktravis_time:end:1da4589a:start=1568823395054911907,finish=1568823395057873801,duration=2961894,event=fix_etc_mavenrc[0Ktravis_time:start:092a5c8a[0Ktravis_time:end:092a5c8a:start=1568823395063836520,finish=1568823395067481381,duration=3644861,event=fix_wwdr_certificate[0Ktravis_time:start:02008438[0Ktravis_time:end:02008438:start=1568823395072931462,finish=1568823395099093161,duration=26161699,event=put_localhost_first[0Ktravis_time:start:00d9e7c4[0Ktravis_time:end:00d9e7c4:start=1568823395105166425,finish=1568823395109279163,duration=4112738,event=home_paths[0Ktravis_time:start:07b373fe[0Ktravis_time:end:07b373fe:start=1568823395114709922,finish=1568823395133761011,duration=19051089,event=disable_initramfs[0Ktravis_time:start:0e0b78f0[0Ktravis_time:end:0e0b78f0:start=1568823395139174350,finish=1568823395568090452,duration=428916102,event=disable_ssh_roaming[0Ktravis_time:start:032b96b3[0Ktravis_time:end:032b96b3:start=1568823395574451570,finish=1568823395578280590,duration=3829020,event=debug_tools[0Ktravis_time:start:021f5afd[0Ktravis_time:end:021f5afd:start=1568823395583414301,finish=1568823395588654825,duration=5240524,event=uninstall_oclint[0Ktravis_time:start:152fe518[0Ktravis_time:end:152fe518:start=1568823395596218893,finish=1568823395601781136,duration=5562243,event=rvm_use[0Ktravis_time:start:1eddd821[0Ktravis_time:end:1eddd821:start=1568823395607437284,finish=1568823395623802525,duration=16365241,event=rm_etc_boto_cfg[0Ktravis_time:start:12eb177c[0Ktravis_time:end:12eb177c:start=1568823395628451811,finish=1568823395631249191,duration=2797380,event=rm_oraclejdk8_symlink[0Ktravis_time:start:18024e6a[0Ktravis_time:end:18024e6a:start=1568823395635259479,finish=1568823395698697051,duration=63437572,event=enable_i386[0Ktravis_time:start:0fdac69c[0Ktravis_time:end:0fdac69c:start=1568823395704343048,finish=1568823395709461571,duration=5118523,event=update_rubygems[0Ktravis_time:start:05239950[0Ktravis_time:end:05239950:start=1568823395718673591,finish=1568823396779934262,duration=1061260671,event=ensure_path_components[0Ktravis_time:start:0df75848[0Ktravis_time:end:0df75848:start=1568823396784608073,finish=1568823396787744319,duration=3136246,event=redefine_curl[0Ktravis_time:start:1276d6a8[0Ktravis_time:end:1276d6a8:start=1568823396791984943,finish=1568823396854330672,duration=62345729,event=nonblock_pipe[0Ktravis_time:start:141eb616[0Ktravis_time:end:141eb616:start=1568823396861142079,finish=1568823396903499185,duration=42357106,event=apt_get_update[0Ktravis_time:start:054b9a92[0Ktravis_time:end:054b9a92:start=1568823396908752213,finish=1568823396912713370,duration=3961157,event=deprecate_xcode_64[0Ktravis_time:start:0227de80[0Ktravis_time:end:0227de80:start=1568823396918827124,finish=1568823402047585312,duration=5128758188,event=update_heroku[0Ktravis_time:start:026c8a20[0Ktravis_time:end:026c8a20:start=1568823402051936275,finish=1568823402055267898,duration=3331623,event=shell_session_update[0Ktravis_time:start:0b0b52e8[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3862
travis_fold:end:docker_mtu[0Ktravis_time:end:0b0b52e8:start=1568823402059652147,finish=1568823403263375310,duration=1203723163,event=set_docker_mtu[0Ktravis_time:start:146ff673[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:146ff673:start=1568823403268015630,finish=1568823403341814269,duration=73798639,event=resolvconf[0Ktravis_time:start:05e587e5[0Ktravis_time:end:05e587e5:start=1568823403348940084,finish=1568823403453271676,duration=104331592,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2d40ffe7[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2d40ffe7:start=1568823403545266379,finish=1568823403983246767,duration=437980388,event=configure[0Ktravis_time:start:03f41fa8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:03f41fa8:start=1568823403990416831,finish=1568823414027710381,duration=10037293550,event=configure[0Ktravis_time:start:1bde4620[0Ktravis_fold:start:services[0Ktravis_time:start:28dde460[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:28dde460:start=1568823414053885032,finish=1568823414069534000,duration=15648968,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:28dde460:start=1568823414053885032,finish=1568823417075841286,duration=3021956254,event=services[0Ktravis_time:start:2c0a3e10[0Ktravis_time:end:2c0a3e10:start=1568823417081438768,finish=1568823417085792622,duration=4353854,event=fix_ps4[0Ktravis_time:start:08eee4d6[0K
travis_fold:start:git.checkout[0Ktravis_time:start:068b53ca[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-fixpip1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:068b53ca:start=1568823417095420326,finish=1568823427367115832,duration=10271695506,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 628c8f57e99ad5b8d85cdaca6e230b3407aa4aee
travis_fold:end:git.checkout[0K
travis_time:end:068b53ca:start=1568823417095420326,finish=1568823427680410443,duration=10584990117,event=checkout[0Ktravis_time:start:2dc00f40[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2dc00f40:start=1568823427686436398,finish=1568823427699726749,duration=13290351,event=env[0Ktravis_time:start:0940dcfa[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0940dcfa:start=1568823427706518562,finish=1568823427719282158,duration=12763596,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:053c57d6[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,dealii-of,bindings,of-of_np,of-ccx_fsi,su2-ccx,of-ccx,nutils-of,of-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:053c57d6:start=1568823428079347284,finish=1568823428148372589,duration=69025305,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1eacaf3d[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586517810/log.txt)