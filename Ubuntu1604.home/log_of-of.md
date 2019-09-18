 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586479648) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/51ea4812093d...cd89b1900540) 
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
travis_time:end:0f074fa9:start=1568812785425989697,finish=1568812785435536047,duration=9546350,event=show_system_info[0Ktravis_time:start:02a43686[0Ktravis_time:end:02a43686:start=1568812785438117602,finish=1568812785463689922,duration=25572320,event=rm_riak_source[0Ktravis_time:start:05d0165a[0Ktravis_time:end:05d0165a:start=1568812785466341221,finish=1568812785474870004,duration=8528783,event=fix_rwky_redis[0Ktravis_time:start:332fa000[0Ktravis_time:end:332fa000:start=1568812785477429916,finish=1568812785899588884,duration=422158968,event=wait_for_network[0Ktravis_time:start:188131ec[0Ktravis_time:end:188131ec:start=1568812785905057316,finish=1568812787647027883,duration=1741970567,event=update_apt_keys[0Ktravis_time:start:071cc07f[0Ktravis_time:end:071cc07f:start=1568812787651019732,finish=1568812788680477811,duration=1029458079,event=fix_hhvm_source[0Ktravis_time:start:07069fc7[0Ktravis_time:end:07069fc7:start=1568812788684924269,finish=1568812788699192487,duration=14268218,event=update_mongo_arch[0Ktravis_time:start:0325bb34[0Ktravis_time:end:0325bb34:start=1568812788704070730,finish=1568812788753512380,duration=49441650,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2308af22[0Ktravis_time:end:2308af22:start=1568812788757514281,finish=1568812788760009172,duration=2494891,event=update_glibc[0Ktravis_time:start:105ac208[0Ktravis_time:end:105ac208:start=1568812788763858173,finish=1568812788773567256,duration=9709083,event=clean_up_path[0Ktravis_time:start:07118a19[0Ktravis_time:end:07118a19:start=1568812788779347909,finish=1568812788787918785,duration=8570876,event=fix_resolv_conf[0Ktravis_time:start:01cca60c[0Ktravis_time:end:01cca60c:start=1568812788792463776,finish=1568812788802937933,duration=10474157,event=fix_etc_hosts[0Ktravis_time:start:002fc0f4[0Ktravis_time:end:002fc0f4:start=1568812788806929823,finish=1568812788826621434,duration=19691611,event=fix_mvn_settings_xml[0Ktravis_time:start:20512f16[0Ktravis_time:end:20512f16:start=1568812788831586789,finish=1568812788843033655,duration=11446866,event=no_ipv6_localhost[0Ktravis_time:start:10b64394[0Ktravis_time:end:10b64394:start=1568812788847140195,finish=1568812788850046619,duration=2906424,event=fix_etc_mavenrc[0Ktravis_time:start:00658c02[0Ktravis_time:end:00658c02:start=1568812788854200588,finish=1568812788858267662,duration=4067074,event=fix_wwdr_certificate[0Ktravis_time:start:0dbd9ad3[0Ktravis_time:end:0dbd9ad3:start=1568812788862251772,finish=1568812788892114227,duration=29862455,event=put_localhost_first[0Ktravis_time:start:01f6eedc[0Ktravis_time:end:01f6eedc:start=1568812788896633076,finish=1568812788904439726,duration=7806650,event=home_paths[0Ktravis_time:start:006106c5[0Ktravis_time:end:006106c5:start=1568812788909070393,finish=1568812788923815642,duration=14745249,event=disable_initramfs[0Ktravis_time:start:022358e0[0Ktravis_time:end:022358e0:start=1568812788928116387,finish=1568812789187861281,duration=259744894,event=disable_ssh_roaming[0Ktravis_time:start:315e42c1[0Ktravis_time:end:315e42c1:start=1568812789192706686,finish=1568812789195381940,duration=2675254,event=debug_tools[0Ktravis_time:start:19458d14[0Ktravis_time:end:19458d14:start=1568812789200164229,finish=1568812789203941990,duration=3777761,event=uninstall_oclint[0Ktravis_time:start:054a9b6d[0Ktravis_time:end:054a9b6d:start=1568812789208558907,finish=1568812789212394072,duration=3835165,event=rvm_use[0Ktravis_time:start:0ae28f1a[0Ktravis_time:end:0ae28f1a:start=1568812789216149693,finish=1568812789230719572,duration=14569879,event=rm_etc_boto_cfg[0Ktravis_time:start:0a784904[0Ktravis_time:end:0a784904:start=1568812789235583173,finish=1568812789238365387,duration=2782214,event=rm_oraclejdk8_symlink[0Ktravis_time:start:03647cf5[0Ktravis_time:end:03647cf5:start=1568812789242674455,finish=1568812789299758126,duration=57083671,event=enable_i386[0Ktravis_time:start:0c22258b[0Ktravis_time:end:0c22258b:start=1568812789304019023,finish=1568812789313708877,duration=9689854,event=update_rubygems[0Ktravis_time:start:33185f66[0Ktravis_time:end:33185f66:start=1568812789317640345,finish=1568812790326596183,duration=1008955838,event=ensure_path_components[0Ktravis_time:start:01ed7370[0Ktravis_time:end:01ed7370:start=1568812790330633297,finish=1568812790333399728,duration=2766431,event=redefine_curl[0Ktravis_time:start:04f3fd80[0Ktravis_time:end:04f3fd80:start=1568812790338254834,finish=1568812790395001634,duration=56746800,event=nonblock_pipe[0Ktravis_time:start:00a05800[0Ktravis_time:end:00a05800:start=1568812790400222299,finish=1568812790447151917,duration=46929618,event=apt_get_update[0Ktravis_time:start:1f35ba3c[0Ktravis_time:end:1f35ba3c:start=1568812790451617336,finish=1568812790455285342,duration=3668006,event=deprecate_xcode_64[0Ktravis_time:start:00c69dc8[0Ktravis_time:end:00c69dc8:start=1568812790459456602,finish=1568812795176532777,duration=4717076175,event=update_heroku[0Ktravis_time:start:08617092[0Ktravis_time:end:08617092:start=1568812795180605570,finish=1568812795187197204,duration=6591634,event=shell_session_update[0Ktravis_time:start:00a20030[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3952
travis_fold:end:docker_mtu[0Ktravis_time:end:00a20030:start=1568812795191259433,finish=1568812796382701669,duration=1191442236,event=set_docker_mtu[0Ktravis_time:start:0ee18ff2[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0ee18ff2:start=1568812796386514652,finish=1568812796450472299,duration=63957647,event=resolvconf[0Ktravis_time:start:00fb9730[0Ktravis_time:end:00fb9730:start=1568812796455214655,finish=1568812796545330077,duration=90115422,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:299be2d0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:299be2d0:start=1568812796629548882,finish=1568812797659305609,duration=1029756727,event=configure[0Ktravis_time:start:25f37eec[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:25f37eec:start=1568812797668469980,finish=1568812806867784787,duration=9199314807,event=configure[0Ktravis_time:start:14d56b82[0Ktravis_fold:start:services[0Ktravis_time:start:234f6029[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:234f6029:start=1568812806909979024,finish=1568812806923498103,duration=13519079,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:234f6029:start=1568812806909979024,finish=1568812809931684303,duration=3021705279,event=services[0Ktravis_time:start:09004af4[0Ktravis_time:end:09004af4:start=1568812809937993829,finish=1568812809941093492,duration=3099663,event=fix_ps4[0Ktravis_time:start:067c7871[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0faa9a8d[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0faa9a8d:start=1568812809961589281,finish=1568812820592484886,duration=10630895605,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf cd89b1900540505af8c571183bfc09ad56bacb7b
travis_fold:end:git.checkout[0K
travis_time:end:0faa9a8d:start=1568812809961589281,finish=1568812821134109265,duration=11172519984,event=checkout[0Ktravis_time:start:0ae4c4ee[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0ae4c4ee:start=1568812821143277043,finish=1568812821154687249,duration=11410206,event=env[0Ktravis_time:start:0b125d97[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0b125d97:start=1568812821168615150,finish=1568812821174079268,duration=5464118,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1641c72c[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-ccx,bindings,of-of,nutils-of,of-of_np,dealii-of,su2-ccx,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:1641c72c:start=1568812821560910656,finish=1568812821624678601,duration=63767945,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:066665c6[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586479673/log.txt)