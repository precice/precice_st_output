 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586517772) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63e83084ff16...628c8f57e99a) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
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
travis_time:end:261fb0e7:start=1568823293046591556,finish=1568823293052496939,duration=5905383,event=show_system_info[0Ktravis_time:start:13b2a0bc[0Ktravis_time:end:13b2a0bc:start=1568823293055534867,finish=1568823293083363408,duration=27828541,event=rm_riak_source[0Ktravis_time:start:0eb5e7b4[0Ktravis_time:end:0eb5e7b4:start=1568823293086754460,finish=1568823293092241790,duration=5487330,event=fix_rwky_redis[0Ktravis_time:start:1508bd5c[0Ktravis_time:end:1508bd5c:start=1568823293095242296,finish=1568823293984293832,duration=889051536,event=wait_for_network[0Ktravis_time:start:0074299e[0Ktravis_time:end:0074299e:start=1568823293988480718,finish=1568823296761929291,duration=2773448573,event=update_apt_keys[0Ktravis_time:start:1f97524c[0Ktravis_time:end:1f97524c:start=1568823296767873128,finish=1568823297843179152,duration=1075306024,event=fix_hhvm_source[0Ktravis_time:start:00aa800b[0Ktravis_time:end:00aa800b:start=1568823297848713014,finish=1568823297859525090,duration=10812076,event=update_mongo_arch[0Ktravis_time:start:00c103ea[0Ktravis_time:end:00c103ea:start=1568823297864465109,finish=1568823297907571354,duration=43106245,event=fix_sudo_enabled_trusty[0Ktravis_time:start:09b97e06[0Ktravis_time:end:09b97e06:start=1568823297912559370,finish=1568823297915724449,duration=3165079,event=update_glibc[0Ktravis_time:start:1c20b7a6[0Ktravis_time:end:1c20b7a6:start=1568823297920919679,finish=1568823297930499351,duration=9579672,event=clean_up_path[0Ktravis_time:start:12bcc90d[0Ktravis_time:end:12bcc90d:start=1568823297934408411,finish=1568823297945318579,duration=10910168,event=fix_resolv_conf[0Ktravis_time:start:114b5a34[0Ktravis_time:end:114b5a34:start=1568823297950557509,finish=1568823297963869899,duration=13312390,event=fix_etc_hosts[0Ktravis_time:start:08b94d00[0Ktravis_time:end:08b94d00:start=1568823297968960881,finish=1568823297980311834,duration=11350953,event=fix_mvn_settings_xml[0Ktravis_time:start:04d347e9[0Ktravis_time:end:04d347e9:start=1568823297985218946,finish=1568823297996814792,duration=11595846,event=no_ipv6_localhost[0Ktravis_time:start:09a1c00d[0Ktravis_time:end:09a1c00d:start=1568823298002793195,finish=1568823298006231992,duration=3438797,event=fix_etc_mavenrc[0Ktravis_time:start:16b04e43[0Ktravis_time:end:16b04e43:start=1568823298012566835,finish=1568823298016868313,duration=4301478,event=fix_wwdr_certificate[0Ktravis_time:start:025fef1f[0Ktravis_time:end:025fef1f:start=1568823298023402977,finish=1568823298049639695,duration=26236718,event=put_localhost_first[0Ktravis_time:start:0731f0ce[0Ktravis_time:end:0731f0ce:start=1568823298054709460,finish=1568823298059114450,duration=4404990,event=home_paths[0Ktravis_time:start:02e0ffd2[0Ktravis_time:end:02e0ffd2:start=1568823298063743393,finish=1568823298077196031,duration=13452638,event=disable_initramfs[0Ktravis_time:start:079c4cac[0Ktravis_time:end:079c4cac:start=1568823298082014536,finish=1568823298382408675,duration=300394139,event=disable_ssh_roaming[0Ktravis_time:start:1871df63[0Ktravis_time:end:1871df63:start=1568823298387277707,finish=1568823298390124870,duration=2847163,event=debug_tools[0Ktravis_time:start:3e84332e[0Ktravis_time:end:3e84332e:start=1568823298394881855,finish=1568823298398634550,duration=3752695,event=uninstall_oclint[0Ktravis_time:start:052582ae[0Ktravis_time:end:052582ae:start=1568823298403519220,finish=1568823298407368011,duration=3848791,event=rvm_use[0Ktravis_time:start:132bf5b6[0Ktravis_time:end:132bf5b6:start=1568823298413563811,finish=1568823298422419388,duration=8855577,event=rm_etc_boto_cfg[0Ktravis_time:start:1335921c[0Ktravis_time:end:1335921c:start=1568823298428235995,finish=1568823298431483549,duration=3247554,event=rm_oraclejdk8_symlink[0Ktravis_time:start:17e61730[0Ktravis_time:end:17e61730:start=1568823298437717328,finish=1568823298497474125,duration=59756797,event=enable_i386[0Ktravis_time:start:093af4e7[0Ktravis_time:end:093af4e7:start=1568823298502806182,finish=1568823298510087046,duration=7280864,event=update_rubygems[0Ktravis_time:start:099137f0[0Ktravis_time:end:099137f0:start=1568823298516332007,finish=1568823299575389526,duration=1059057519,event=ensure_path_components[0Ktravis_time:start:21dc4e77[0Ktravis_time:end:21dc4e77:start=1568823299580715469,finish=1568823299583680087,duration=2964618,event=redefine_curl[0Ktravis_time:start:26131179[0Ktravis_time:end:26131179:start=1568823299587973892,finish=1568823299644143827,duration=56169935,event=nonblock_pipe[0Ktravis_time:start:1114d310[0Ktravis_time:end:1114d310:start=1568823299648281372,finish=1568823299718328071,duration=70046699,event=apt_get_update[0Ktravis_time:start:060b969c[0Ktravis_time:end:060b969c:start=1568823299722759495,finish=1568823299725467047,duration=2707552,event=deprecate_xcode_64[0Ktravis_time:start:262cc0ec[0Ktravis_time:end:262cc0ec:start=1568823299729477246,finish=1568823304954833194,duration=5225355948,event=update_heroku[0Ktravis_time:start:1c574faf[0Ktravis_time:end:1c574faf:start=1568823304959523956,finish=1568823304962253519,duration=2729563,event=shell_session_update[0Ktravis_time:start:000674c4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3932
travis_fold:end:docker_mtu[0Ktravis_time:end:000674c4:start=1568823304966569788,finish=1568823306185603943,duration=1219034155,event=set_docker_mtu[0Ktravis_time:start:02978535[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:02978535:start=1568823306191169926,finish=1568823306267463943,duration=76294017,event=resolvconf[0Ktravis_time:start:015dfc60[0Ktravis_time:end:015dfc60:start=1568823306273375908,finish=1568823306389273127,duration=115897219,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:20185734[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:20185734:start=1568823306486170311,finish=1568823306835920252,duration=349749941,event=configure[0Ktravis_time:start:2509bac1[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2509bac1:start=1568823306842334729,finish=1568823318346214172,duration=11503879443,event=configure[0Ktravis_time:start:31ca8dbb[0Ktravis_fold:start:services[0Ktravis_time:start:335f4d98[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:335f4d98:start=1568823318373008531,finish=1568823318388580293,duration=15571762,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:335f4d98:start=1568823318373008531,finish=1568823321394831626,duration=3021823095,event=services[0Ktravis_time:start:19d3bed8[0Ktravis_time:end:19d3bed8:start=1568823321399925940,finish=1568823321403526793,duration=3600853,event=fix_ps4[0Ktravis_time:start:3426353a[0K
travis_fold:start:git.checkout[0Ktravis_time:start:01c51956[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-fixpip1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:01c51956:start=1568823321414288996,finish=1568823332281171478,duration=10866882482,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 628c8f57e99ad5b8d85cdaca6e230b3407aa4aee
travis_fold:end:git.checkout[0K
travis_time:end:01c51956:start=1568823321414288996,finish=1568823332517736083,duration=11103447087,event=checkout[0Ktravis_time:start:06e77b54[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:06e77b54:start=1568823332523354683,finish=1568823332536309871,duration=12955188,event=env[0Ktravis_time:start:00abb286[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00abb286:start=1568823332542804667,finish=1568823332549778169,duration=6973502,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0d9ca59c[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {of-ccx,of-of,of-of_np,bindings,su2-ccx,dealii-of,fe-fe,nutils-of,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0d9ca59c:start=1568823332920867340,finish=1568823332992872447,duration=72005107,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:02050e79[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586517797/log.txt)