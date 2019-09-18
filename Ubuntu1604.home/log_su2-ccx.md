 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586517772) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63e83084ff16...628c8f57e99a) 
## Last succesfull commits 
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
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
travis_time:end:1951b526:start=1568823042741637211,finish=1568823042747472554,duration=5835343,event=show_system_info[0Ktravis_time:start:31534756[0Ktravis_time:end:31534756:start=1568823042750362677,finish=1568823042776441447,duration=26078770,event=rm_riak_source[0Ktravis_time:start:08b20fe0[0Ktravis_time:end:08b20fe0:start=1568823042779661659,finish=1568823042784960717,duration=5299058,event=fix_rwky_redis[0Ktravis_time:start:00e77be4[0Ktravis_time:end:00e77be4:start=1568823042787861186,finish=1568823043306899297,duration=519038111,event=wait_for_network[0Ktravis_time:start:00686afa[0Ktravis_time:end:00686afa:start=1568823043313008930,finish=1568823044893471523,duration=1580462593,event=update_apt_keys[0Ktravis_time:start:12efcdeb[0Ktravis_time:end:12efcdeb:start=1568823044899584772,finish=1568823045942795784,duration=1043211012,event=fix_hhvm_source[0Ktravis_time:start:295333f8[0Ktravis_time:end:295333f8:start=1568823045947452014,finish=1568823045957670590,duration=10218576,event=update_mongo_arch[0Ktravis_time:start:1783218f[0Ktravis_time:end:1783218f:start=1568823045962129985,finish=1568823046006050294,duration=43920309,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1b690b44[0Ktravis_time:end:1b690b44:start=1568823046010963949,finish=1568823046014532413,duration=3568464,event=update_glibc[0Ktravis_time:start:2276c670[0Ktravis_time:end:2276c670:start=1568823046021483237,finish=1568823046031277624,duration=9794387,event=clean_up_path[0Ktravis_time:start:28b838bb[0Ktravis_time:end:28b838bb:start=1568823046035845153,finish=1568823046045917748,duration=10072595,event=fix_resolv_conf[0Ktravis_time:start:275ce247[0Ktravis_time:end:275ce247:start=1568823046051343480,finish=1568823046061859503,duration=10516023,event=fix_etc_hosts[0Ktravis_time:start:04cdafb8[0Ktravis_time:end:04cdafb8:start=1568823046067191110,finish=1568823046076963251,duration=9772141,event=fix_mvn_settings_xml[0Ktravis_time:start:022be096[0Ktravis_time:end:022be096:start=1568823046083182070,finish=1568823046093256021,duration=10073951,event=no_ipv6_localhost[0Ktravis_time:start:2a437022[0Ktravis_time:end:2a437022:start=1568823046099266930,finish=1568823046102290820,duration=3023890,event=fix_etc_mavenrc[0Ktravis_time:start:0474aca7[0Ktravis_time:end:0474aca7:start=1568823046107011401,finish=1568823046111983738,duration=4972337,event=fix_wwdr_certificate[0Ktravis_time:start:146ec12f[0Ktravis_time:end:146ec12f:start=1568823046116024157,finish=1568823046147895352,duration=31871195,event=put_localhost_first[0Ktravis_time:start:0ca86390[0Ktravis_time:end:0ca86390:start=1568823046153624221,finish=1568823046157338339,duration=3714118,event=home_paths[0Ktravis_time:start:289cfcaa[0Ktravis_time:end:289cfcaa:start=1568823046161522375,finish=1568823046176977224,duration=15454849,event=disable_initramfs[0Ktravis_time:start:1642d734[0Ktravis_time:end:1642d734:start=1568823046180981019,finish=1568823046504244590,duration=323263571,event=disable_ssh_roaming[0Ktravis_time:start:3db78da0[0Ktravis_time:end:3db78da0:start=1568823046510613237,finish=1568823046514298663,duration=3685426,event=debug_tools[0Ktravis_time:start:032a91f8[0Ktravis_time:end:032a91f8:start=1568823046519876972,finish=1568823046524440583,duration=4563611,event=uninstall_oclint[0Ktravis_time:start:00f83a1c[0Ktravis_time:end:00f83a1c:start=1568823046529558309,finish=1568823046533125883,duration=3567574,event=rvm_use[0Ktravis_time:start:0119774b[0Ktravis_time:end:0119774b:start=1568823046539915851,finish=1568823046548169226,duration=8253375,event=rm_etc_boto_cfg[0Ktravis_time:start:0169fad1[0Ktravis_time:end:0169fad1:start=1568823046554193561,finish=1568823046557471689,duration=3278128,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0130179a[0Ktravis_time:end:0130179a:start=1568823046561498801,finish=1568823046624991113,duration=63492312,event=enable_i386[0Ktravis_time:start:0d1df440[0Ktravis_time:end:0d1df440:start=1568823046630367311,finish=1568823046634546106,duration=4178795,event=update_rubygems[0Ktravis_time:start:0406fc60[0Ktravis_time:end:0406fc60:start=1568823046640300880,finish=1568823047680396832,duration=1040095952,event=ensure_path_components[0Ktravis_time:start:0561c297[0Ktravis_time:end:0561c297:start=1568823047685304694,finish=1568823047688591325,duration=3286631,event=redefine_curl[0Ktravis_time:start:23cd0e4f[0Ktravis_time:end:23cd0e4f:start=1568823047693798599,finish=1568823047750530793,duration=56732194,event=nonblock_pipe[0Ktravis_time:start:31676454[0Ktravis_time:end:31676454:start=1568823047755492193,finish=1568823047798238948,duration=42746755,event=apt_get_update[0Ktravis_time:start:04613db2[0Ktravis_time:end:04613db2:start=1568823047802362018,finish=1568823047805189315,duration=2827297,event=deprecate_xcode_64[0Ktravis_time:start:04488c40[0Ktravis_time:end:04488c40:start=1568823047811319541,finish=1568823052692277661,duration=4880958120,event=update_heroku[0Ktravis_time:start:2773a060[0Ktravis_time:end:2773a060:start=1568823052698867885,finish=1568823052702165442,duration=3297557,event=shell_session_update[0Ktravis_time:start:1f620330[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3829
travis_fold:end:docker_mtu[0Ktravis_time:end:1f620330:start=1568823052709129414,finish=1568823053915236964,duration=1206107550,event=set_docker_mtu[0Ktravis_time:start:09d91504[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:09d91504:start=1568823053920069509,finish=1568823053997076347,duration=77006838,event=resolvconf[0Ktravis_time:start:0c3cb8e0[0Ktravis_time:end:0c3cb8e0:start=1568823054002687588,finish=1568823054113802714,duration=111115126,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:083ff455[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:083ff455:start=1568823054207736526,finish=1568823054549549697,duration=341813171,event=configure[0Ktravis_time:start:1afa1599[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1afa1599:start=1568823054554922036,finish=1568823064505444037,duration=9950522001,event=configure[0Ktravis_time:start:048c9cf3[0Ktravis_fold:start:services[0Ktravis_time:start:182deb08[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:182deb08:start=1568823064532017058,finish=1568823064548923714,duration=16906656,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:182deb08:start=1568823064532017058,finish=1568823067554263555,duration=3022246497,event=services[0Ktravis_time:start:39293b6c[0Ktravis_time:end:39293b6c:start=1568823067559423383,finish=1568823067562152013,duration=2728630,event=fix_ps4[0Ktravis_time:start:251eab2c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:255347c0[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-fixpip1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:255347c0:start=1568823067572921892,finish=1568823078633547655,duration=11060625763,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 628c8f57e99ad5b8d85cdaca6e230b3407aa4aee
travis_fold:end:git.checkout[0K
travis_time:end:255347c0:start=1568823067572921892,finish=1568823079235182436,duration=11662260544,event=checkout[0Ktravis_time:start:01fe87dc[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:01fe87dc:start=1568823079240885535,finish=1568823079251129788,duration=10244253,event=env[0Ktravis_time:start:1b687228[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1b687228:start=1568823079255716078,finish=1568823079262153209,duration=6437131,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:17863d21[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {nutils-of,su2-ccx,fe-fe,bindings,of-of,of-ccx,of-ccx_fsi,dealii-of,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:17863d21:start=1568823079642268430,finish=1568823079715350194,duration=73081764,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:32f42ce8[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586517791/log.txt)