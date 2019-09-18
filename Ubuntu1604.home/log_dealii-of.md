 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586477733) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3c3e92795247) 
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
travis_time:end:0265b780:start=1568806747201654870,finish=1568806747208744060,duration=7089190,event=show_system_info[0Ktravis_time:start:094dc053[0Ktravis_time:end:094dc053:start=1568806747212408840,finish=1568806747239584926,duration=27176086,event=rm_riak_source[0Ktravis_time:start:3489d094[0Ktravis_time:end:3489d094:start=1568806747243247918,finish=1568806747249233196,duration=5985278,event=fix_rwky_redis[0Ktravis_time:start:04c3d03a[0Ktravis_time:end:04c3d03a:start=1568806747252630980,finish=1568806747658649342,duration=406018362,event=wait_for_network[0Ktravis_time:start:2572778a[0Ktravis_time:end:2572778a:start=1568806747665912563,finish=1568806749320299881,duration=1654387318,event=update_apt_keys[0Ktravis_time:start:07f57007[0Ktravis_time:end:07f57007:start=1568806749324302806,finish=1568806750408750690,duration=1084447884,event=fix_hhvm_source[0Ktravis_time:start:0984f056[0Ktravis_time:end:0984f056:start=1568806750414305693,finish=1568806750425710113,duration=11404420,event=update_mongo_arch[0Ktravis_time:start:017ed992[0Ktravis_time:end:017ed992:start=1568806750430574705,finish=1568806750474981048,duration=44406343,event=fix_sudo_enabled_trusty[0Ktravis_time:start:02e2ccd0[0Ktravis_time:end:02e2ccd0:start=1568806750480059920,finish=1568806750482842515,duration=2782595,event=update_glibc[0Ktravis_time:start:06c0e12d[0Ktravis_time:end:06c0e12d:start=1568806750487298172,finish=1568806750496729973,duration=9431801,event=clean_up_path[0Ktravis_time:start:09892dd4[0Ktravis_time:end:09892dd4:start=1568806750501369713,finish=1568806750510294095,duration=8924382,event=fix_resolv_conf[0Ktravis_time:start:1caba1cc[0Ktravis_time:end:1caba1cc:start=1568806750514652803,finish=1568806750525154621,duration=10501818,event=fix_etc_hosts[0Ktravis_time:start:1725f94c[0Ktravis_time:end:1725f94c:start=1568806750529795335,finish=1568806750540760349,duration=10965014,event=fix_mvn_settings_xml[0Ktravis_time:start:244b6b80[0Ktravis_time:end:244b6b80:start=1568806750545379078,finish=1568806750557082715,duration=11703637,event=no_ipv6_localhost[0Ktravis_time:start:0e7829a8[0Ktravis_time:end:0e7829a8:start=1568806750560939380,finish=1568806750563645743,duration=2706363,event=fix_etc_mavenrc[0Ktravis_time:start:009df27f[0Ktravis_time:end:009df27f:start=1568806750567588451,finish=1568806750573724264,duration=6135813,event=fix_wwdr_certificate[0Ktravis_time:start:12ee2952[0Ktravis_time:end:12ee2952:start=1568806750578698808,finish=1568806750606514452,duration=27815644,event=put_localhost_first[0Ktravis_time:start:01012c3b[0Ktravis_time:end:01012c3b:start=1568806750611167763,finish=1568806750615027941,duration=3860178,event=home_paths[0Ktravis_time:start:14fa8478[0Ktravis_time:end:14fa8478:start=1568806750620638533,finish=1568806750634767904,duration=14129371,event=disable_initramfs[0Ktravis_time:start:013fde42[0Ktravis_time:end:013fde42:start=1568806750639885070,finish=1568806750942829569,duration=302944499,event=disable_ssh_roaming[0Ktravis_time:start:098f3337[0Ktravis_time:end:098f3337:start=1568806750947409636,finish=1568806750950773994,duration=3364358,event=debug_tools[0Ktravis_time:start:0583c324[0Ktravis_time:end:0583c324:start=1568806750955926044,finish=1568806750962147538,duration=6221494,event=uninstall_oclint[0Ktravis_time:start:155b9aa3[0Ktravis_time:end:155b9aa3:start=1568806750966793370,finish=1568806750970755584,duration=3962214,event=rvm_use[0Ktravis_time:start:0664194d[0Ktravis_time:end:0664194d:start=1568806750975360055,finish=1568806750984385569,duration=9025514,event=rm_etc_boto_cfg[0Ktravis_time:start:1ae00cf8[0Ktravis_time:end:1ae00cf8:start=1568806750990060076,finish=1568806750993210309,duration=3150233,event=rm_oraclejdk8_symlink[0Ktravis_time:start:17fb1c40[0Ktravis_time:end:17fb1c40:start=1568806750997738781,finish=1568806751059941983,duration=62203202,event=enable_i386[0Ktravis_time:start:1194f6e8[0Ktravis_time:end:1194f6e8:start=1568806751064552657,finish=1568806751069499214,duration=4946557,event=update_rubygems[0Ktravis_time:start:16b38662[0Ktravis_time:end:16b38662:start=1568806751076389221,finish=1568806752118342932,duration=1041953711,event=ensure_path_components[0Ktravis_time:start:009627a8[0Ktravis_time:end:009627a8:start=1568806752123301731,finish=1568806752126574217,duration=3272486,event=redefine_curl[0Ktravis_time:start:07fc6a8c[0Ktravis_time:end:07fc6a8c:start=1568806752131154681,finish=1568806752184860397,duration=53705716,event=nonblock_pipe[0Ktravis_time:start:0dad4a72[0Ktravis_time:end:0dad4a72:start=1568806752189670238,finish=1568806752229848723,duration=40178485,event=apt_get_update[0Ktravis_time:start:0cc1a804[0Ktravis_time:end:0cc1a804:start=1568806752235278814,finish=1568806752238593522,duration=3314708,event=deprecate_xcode_64[0Ktravis_time:start:017e0b2d[0Ktravis_time:end:017e0b2d:start=1568806752243708083,finish=1568806757130049412,duration=4886341329,event=update_heroku[0Ktravis_time:start:06596474[0Ktravis_time:end:06596474:start=1568806757135350041,finish=1568806757138122018,duration=2771977,event=shell_session_update[0Ktravis_time:start:17629494[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3931
travis_fold:end:docker_mtu[0Ktravis_time:end:17629494:start=1568806757142680260,finish=1568806758353044211,duration=1210363951,event=set_docker_mtu[0Ktravis_time:start:1a26a1fa[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1a26a1fa:start=1568806758357998542,finish=1568806758425702802,duration=67704260,event=resolvconf[0Ktravis_time:start:1b74b278[0Ktravis_time:end:1b74b278:start=1568806758431330224,finish=1568806758535408069,duration=104077845,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:083a62ea[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:083a62ea:start=1568806758621867653,finish=1568806759135792318,duration=513924665,event=configure[0Ktravis_time:start:0c898c74[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0c898c74:start=1568806759142033764,finish=1568806771462652663,duration=12320618899,event=configure[0Ktravis_time:start:021d04ea[0Ktravis_fold:start:services[0Ktravis_time:start:1bf4814d[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1bf4814d:start=1568806771490633974,finish=1568806771506499159,duration=15865185,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1bf4814d:start=1568806771490633974,finish=1568806774513027167,duration=3022393193,event=services[0Ktravis_time:start:27a3427a[0Ktravis_time:end:27a3427a:start=1568806774518054015,finish=1568806774521558475,duration=3504460,event=fix_ps4[0Ktravis_time:start:1fcaafc0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:091fd0e3[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:091fd0e3:start=1568806774530175226,finish=1568806785931084882,duration=11400909656,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3c3e927952479f3d81847ce6139ede1bec7f9aff
travis_fold:end:git.checkout[0K
travis_time:end:091fd0e3:start=1568806774530175226,finish=1568806786773670884,duration=12243495658,event=checkout[0Ktravis_time:start:10fb5d00[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:10fb5d00:start=1568806786778798216,finish=1568806786793443378,duration=14645162,event=env[0Ktravis_time:start:083554d2[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:083554d2:start=1568806786798125793,finish=1568806786803907241,duration=5781448,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0b1617b8[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,of-of_np,of-ccx_fsi,bindings,of-of,dealii-of,fe-fe,nutils-of,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0b1617b8:start=1568806787161756689,finish=1568806787229101005,duration=67344316,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:070227c0[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586477761/log.txt)