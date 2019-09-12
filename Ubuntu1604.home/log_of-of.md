 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584291854) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aabfec63ba1b...d9aa1e4cf4f1) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
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
travis_time:end:00100a00:start=1568324112709361347,finish=1568324112715714514,duration=6353167,event=show_system_info[0Ktravis_time:start:02eeeb8c[0Ktravis_time:end:02eeeb8c:start=1568324112718710453,finish=1568324112743348826,duration=24638373,event=rm_riak_source[0Ktravis_time:start:0e5fe053[0Ktravis_time:end:0e5fe053:start=1568324112746593245,finish=1568324112751912613,duration=5319368,event=fix_rwky_redis[0Ktravis_time:start:325b9095[0Ktravis_time:end:325b9095:start=1568324112755094820,finish=1568324116192921029,duration=3437826209,event=wait_for_network[0Ktravis_time:start:090bea6a[0Ktravis_time:end:090bea6a:start=1568324116198633056,finish=1568324117801383334,duration=1602750278,event=update_apt_keys[0Ktravis_time:start:0a6eec01[0Ktravis_time:end:0a6eec01:start=1568324117806890651,finish=1568324119058503280,duration=1251612629,event=fix_hhvm_source[0Ktravis_time:start:1e86ba9b[0Ktravis_time:end:1e86ba9b:start=1568324119062751396,finish=1568324119073608274,duration=10856878,event=update_mongo_arch[0Ktravis_time:start:0f937b24[0Ktravis_time:end:0f937b24:start=1568324119077416226,finish=1568324119124442992,duration=47026766,event=fix_sudo_enabled_trusty[0Ktravis_time:start:3c24b709[0Ktravis_time:end:3c24b709:start=1568324119129339106,finish=1568324119132252646,duration=2913540,event=update_glibc[0Ktravis_time:start:025f0d16[0Ktravis_time:end:025f0d16:start=1568324119137813856,finish=1568324119149726408,duration=11912552,event=clean_up_path[0Ktravis_time:start:0c2a1c9c[0Ktravis_time:end:0c2a1c9c:start=1568324119154529212,finish=1568324119163411808,duration=8882596,event=fix_resolv_conf[0Ktravis_time:start:029a7c50[0Ktravis_time:end:029a7c50:start=1568324119168180898,finish=1568324119178815188,duration=10634290,event=fix_etc_hosts[0Ktravis_time:start:32528550[0Ktravis_time:end:32528550:start=1568324119182952314,finish=1568324119193399062,duration=10446748,event=fix_mvn_settings_xml[0Ktravis_time:start:04356282[0Ktravis_time:end:04356282:start=1568324119199663026,finish=1568324119210225811,duration=10562785,event=no_ipv6_localhost[0Ktravis_time:start:1e7e1e22[0Ktravis_time:end:1e7e1e22:start=1568324119216674614,finish=1568324119219351970,duration=2677356,event=fix_etc_mavenrc[0Ktravis_time:start:047289e2[0Ktravis_time:end:047289e2:start=1568324119224064297,finish=1568324119227966714,duration=3902417,event=fix_wwdr_certificate[0Ktravis_time:start:296ecdd6[0Ktravis_time:end:296ecdd6:start=1568324119232948827,finish=1568324119259644291,duration=26695464,event=put_localhost_first[0Ktravis_time:start:03fcdff7[0Ktravis_time:end:03fcdff7:start=1568324119264358391,finish=1568324119268316202,duration=3957811,event=home_paths[0Ktravis_time:start:376e7151[0Ktravis_time:end:376e7151:start=1568324119273861797,finish=1568324119287548549,duration=13686752,event=disable_initramfs[0Ktravis_time:start:2f29297b[0Ktravis_time:end:2f29297b:start=1568324119291815112,finish=1568324119644845122,duration=353030010,event=disable_ssh_roaming[0Ktravis_time:start:010b83ea[0Ktravis_time:end:010b83ea:start=1568324119649690026,finish=1568324119653234899,duration=3544873,event=debug_tools[0Ktravis_time:start:0368c9b6[0Ktravis_time:end:0368c9b6:start=1568324119657975324,finish=1568324119662904413,duration=4929089,event=uninstall_oclint[0Ktravis_time:start:27297094[0Ktravis_time:end:27297094:start=1568324119667454910,finish=1568324119671908558,duration=4453648,event=rvm_use[0Ktravis_time:start:1cfb42a8[0Ktravis_time:end:1cfb42a8:start=1568324119683420835,finish=1568324119693905024,duration=10484189,event=rm_etc_boto_cfg[0Ktravis_time:start:25d34570[0Ktravis_time:end:25d34570:start=1568324119698700779,finish=1568324119702615582,duration=3914803,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0ea462d6[0Ktravis_time:end:0ea462d6:start=1568324119707364472,finish=1568324119770368960,duration=63004488,event=enable_i386[0Ktravis_time:start:2dc940be[0Ktravis_time:end:2dc940be:start=1568324119776172172,finish=1568324119781888757,duration=5716585,event=update_rubygems[0Ktravis_time:start:26a8c40b[0Ktravis_time:end:26a8c40b:start=1568324119787996652,finish=1568324120999613763,duration=1211617111,event=ensure_path_components[0Ktravis_time:start:00d1a484[0Ktravis_time:end:00d1a484:start=1568324121005985672,finish=1568324121009520458,duration=3534786,event=redefine_curl[0Ktravis_time:start:0155afc6[0Ktravis_time:end:0155afc6:start=1568324121014715143,finish=1568324121078733669,duration=64018526,event=nonblock_pipe[0Ktravis_time:start:032ae6cc[0Ktravis_time:end:032ae6cc:start=1568324121084510424,finish=1568324121135401328,duration=50890904,event=apt_get_update[0Ktravis_time:start:0fe73198[0Ktravis_time:end:0fe73198:start=1568324121141107434,finish=1568324121145128036,duration=4020602,event=deprecate_xcode_64[0Ktravis_time:start:2af29a84[0Ktravis_time:end:2af29a84:start=1568324121149997903,finish=1568324126219776733,duration=5069778830,event=update_heroku[0Ktravis_time:start:0eddbeb1[0Ktravis_time:end:0eddbeb1:start=1568324126225038521,finish=1568324126228002235,duration=2963714,event=shell_session_update[0Ktravis_time:start:08dd9fb0[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3945
travis_fold:end:docker_mtu[0Ktravis_time:end:08dd9fb0:start=1568324126232336054,finish=1568324127425905125,duration=1193569071,event=set_docker_mtu[0Ktravis_time:start:008cbbea[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:008cbbea:start=1568324127431136746,finish=1568324127497632229,duration=66495483,event=resolvconf[0Ktravis_time:start:1e1228a0[0Ktravis_time:end:1e1228a0:start=1568324127501807824,finish=1568324127609770201,duration=107962377,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0140e7dc[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0140e7dc:start=1568324127697477641,finish=1568324128279216498,duration=581738857,event=configure[0Ktravis_time:start:0d0b59e8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d0b59e8:start=1568324128285839278,finish=1568324139225768354,duration=10939929076,event=configure[0Ktravis_time:start:08510ec0[0Ktravis_fold:start:services[0Ktravis_time:start:0e37a190[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0e37a190:start=1568324139251747189,finish=1568324139266411093,duration=14663904,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0e37a190:start=1568324139251747189,finish=1568324142273142071,duration=3021394882,event=services[0Ktravis_time:start:0e18f949[0Ktravis_time:end:0e18f949:start=1568324142278899310,finish=1568324142282174633,duration=3275323,event=fix_ps4[0Ktravis_time:start:17cb30b4[0K
travis_fold:start:git.checkout[0Ktravis_time:start:01173a26[0K$ git clone --depth=50 --branch=test_install https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:01173a26:start=1568324142292847343,finish=1568324153036032466,duration=10743185123,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf d9aa1e4cf4f1a2b30461f455331976a25f5ca603
travis_fold:end:git.checkout[0K
travis_time:end:01173a26:start=1568324142292847343,finish=1568324153072481106,duration=10779633763,event=checkout[0Ktravis_time:start:30300734[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:30300734:start=1568324153078962077,finish=1568324153093501712,duration=14539635,event=env[0Ktravis_time:start:16c47b22[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:16c47b22:start=1568324153101698039,finish=1568324153109408727,duration=7710688,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:033a481c[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {of-of,of-of_np,of-ccx_fsi,nutils-of,fe-fe,su2-ccx,of-ccx,dealii-of,bindings}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:033a481c:start=1568324153527267836,finish=1568324153594333962,duration=67066126,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1e77cc37[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584291873/log.txt)