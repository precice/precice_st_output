 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586477733) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3c3e92795247) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf) 
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
travis_time:end:10bf18e3:start=1568806326035397035,finish=1568806326043540758,duration=8143723,event=show_system_info[0Ktravis_time:start:1ddae9f9[0Ktravis_time:end:1ddae9f9:start=1568806326046728490,finish=1568806326072779035,duration=26050545,event=rm_riak_source[0Ktravis_time:start:06b11432[0Ktravis_time:end:06b11432:start=1568806326076346042,finish=1568806326082055886,duration=5709844,event=fix_rwky_redis[0Ktravis_time:start:0a5b30ce[0Ktravis_time:end:0a5b30ce:start=1568806326085314520,finish=1568806326474131788,duration=388817268,event=wait_for_network[0Ktravis_time:start:2472fcb0[0Ktravis_time:end:2472fcb0:start=1568806326490418235,finish=1568806328189456655,duration=1699038420,event=update_apt_keys[0Ktravis_time:start:103fcab2[0Ktravis_time:end:103fcab2:start=1568806328194047136,finish=1568806329224189153,duration=1030142017,event=fix_hhvm_source[0Ktravis_time:start:08a495ba[0Ktravis_time:end:08a495ba:start=1568806329228281171,finish=1568806329239397187,duration=11116016,event=update_mongo_arch[0Ktravis_time:start:0567d09a[0Ktravis_time:end:0567d09a:start=1568806329243337863,finish=1568806329288858051,duration=45520188,event=fix_sudo_enabled_trusty[0Ktravis_time:start:058f6218[0Ktravis_time:end:058f6218:start=1568806329293307005,finish=1568806329296152474,duration=2845469,event=update_glibc[0Ktravis_time:start:21a94158[0Ktravis_time:end:21a94158:start=1568806329300517223,finish=1568806329309694066,duration=9176843,event=clean_up_path[0Ktravis_time:start:18846861[0Ktravis_time:end:18846861:start=1568806329314513719,finish=1568806329324022865,duration=9509146,event=fix_resolv_conf[0Ktravis_time:start:2410d874[0Ktravis_time:end:2410d874:start=1568806329330132651,finish=1568806329342718226,duration=12585575,event=fix_etc_hosts[0Ktravis_time:start:04dae19e[0Ktravis_time:end:04dae19e:start=1568806329348568253,finish=1568806329360251375,duration=11683122,event=fix_mvn_settings_xml[0Ktravis_time:start:09d90080[0Ktravis_time:end:09d90080:start=1568806329365887673,finish=1568806329377378357,duration=11490684,event=no_ipv6_localhost[0Ktravis_time:start:0a632f26[0Ktravis_time:end:0a632f26:start=1568806329384410212,finish=1568806329388064629,duration=3654417,event=fix_etc_mavenrc[0Ktravis_time:start:101e7214[0Ktravis_time:end:101e7214:start=1568806329394375352,finish=1568806329399576376,duration=5201024,event=fix_wwdr_certificate[0Ktravis_time:start:0b6f6dfe[0Ktravis_time:end:0b6f6dfe:start=1568806329405086533,finish=1568806329434188054,duration=29101521,event=put_localhost_first[0Ktravis_time:start:03d90984[0Ktravis_time:end:03d90984:start=1568806329439823339,finish=1568806329443799068,duration=3975729,event=home_paths[0Ktravis_time:start:29f546cb[0Ktravis_time:end:29f546cb:start=1568806329448834146,finish=1568806329465697544,duration=16863398,event=disable_initramfs[0Ktravis_time:start:3aebbaa1[0Ktravis_time:end:3aebbaa1:start=1568806329471246271,finish=1568806329746177662,duration=274931391,event=disable_ssh_roaming[0Ktravis_time:start:00b73a35[0Ktravis_time:end:00b73a35:start=1568806329752406672,finish=1568806329756586580,duration=4179908,event=debug_tools[0Ktravis_time:start:0336d663[0Ktravis_time:end:0336d663:start=1568806329763766302,finish=1568806329768286215,duration=4519913,event=uninstall_oclint[0Ktravis_time:start:02dd27c8[0Ktravis_time:end:02dd27c8:start=1568806329773763442,finish=1568806329778602197,duration=4838755,event=rvm_use[0Ktravis_time:start:09aed923[0Ktravis_time:end:09aed923:start=1568806329786214058,finish=1568806329796456733,duration=10242675,event=rm_etc_boto_cfg[0Ktravis_time:start:0da668f0[0Ktravis_time:end:0da668f0:start=1568806329802613598,finish=1568806329806343307,duration=3729709,event=rm_oraclejdk8_symlink[0Ktravis_time:start:03059d6c[0Ktravis_time:end:03059d6c:start=1568806329813101654,finish=1568806329891945563,duration=78843909,event=enable_i386[0Ktravis_time:start:05792240[0Ktravis_time:end:05792240:start=1568806329897908468,finish=1568806329903700156,duration=5791688,event=update_rubygems[0Ktravis_time:start:00023a12[0Ktravis_time:end:00023a12:start=1568806329908551841,finish=1568806331084353207,duration=1175801366,event=ensure_path_components[0Ktravis_time:start:05f9a321[0Ktravis_time:end:05f9a321:start=1568806331090103573,finish=1568806331093426627,duration=3323054,event=redefine_curl[0Ktravis_time:start:1241c28c[0Ktravis_time:end:1241c28c:start=1568806331099374751,finish=1568806331157541124,duration=58166373,event=nonblock_pipe[0Ktravis_time:start:1a73102c[0Ktravis_time:end:1a73102c:start=1568806331163288128,finish=1568806331213181518,duration=49893390,event=apt_get_update[0Ktravis_time:start:03300cc1[0Ktravis_time:end:03300cc1:start=1568806331220353243,finish=1568806331224164605,duration=3811362,event=deprecate_xcode_64[0Ktravis_time:start:03c3b6d2[0Ktravis_time:end:03c3b6d2:start=1568806331230005498,finish=1568806336199174142,duration=4969168644,event=update_heroku[0Ktravis_time:start:2a8336ed[0Ktravis_time:end:2a8336ed:start=1568806336205014332,finish=1568806336208135744,duration=3121412,event=shell_session_update[0Ktravis_time:start:1010b6c4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3832
travis_fold:end:docker_mtu[0Ktravis_time:end:1010b6c4:start=1568806336212887378,finish=1568806337424201621,duration=1211314243,event=set_docker_mtu[0Ktravis_time:start:0788c852[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0788c852:start=1568806337430703930,finish=1568806337510926545,duration=80222615,event=resolvconf[0Ktravis_time:start:2eee72d4[0Ktravis_time:end:2eee72d4:start=1568806337516160502,finish=1568806337627638427,duration=111477925,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:05431c86[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:05431c86:start=1568806337723539077,finish=1568806338214635760,duration=491096683,event=configure[0Ktravis_time:start:149dcace[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:149dcace:start=1568806338223550837,finish=1568806349491415972,duration=11267865135,event=configure[0Ktravis_time:start:000aab2c[0Ktravis_fold:start:services[0Ktravis_time:start:18393ad8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:18393ad8:start=1568806349517064342,finish=1568806349531884152,duration=14819810,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:18393ad8:start=1568806349517064342,finish=1568806352538097723,duration=3021033381,event=services[0Ktravis_time:start:11065b7c[0Ktravis_time:end:11065b7c:start=1568806352545051679,finish=1568806352548534025,duration=3482346,event=fix_ps4[0Ktravis_time:start:13ebd8be[0K
travis_fold:start:git.checkout[0Ktravis_time:start:05013444[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:05013444:start=1568806352559094660,finish=1568806363296582629,duration=10737487969,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3c3e927952479f3d81847ce6139ede1bec7f9aff
travis_fold:end:git.checkout[0K
travis_time:end:05013444:start=1568806352559094660,finish=1568806363538787009,duration=10979692349,event=checkout[0Ktravis_time:start:02a9be9c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:02a9be9c:start=1568806363543816444,finish=1568806363555759791,duration=11943347,event=env[0Ktravis_time:start:249fe7e0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:249fe7e0:start=1568806363563926548,finish=1568806363571132574,duration=7206026,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0aadb640[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {nutils-of,dealii-of,su2-ccx,of-ccx_fsi,of-of,bindings,of-of_np,fe-fe,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0aadb640:start=1568806363938654210,finish=1568806364008425784,duration=69771574,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:21a73d60[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586477748/log.txt)