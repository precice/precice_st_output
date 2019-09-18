 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510170) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/40d6daa277c6...b989e40888b7) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1) 
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
travis_time:end:0cb4d293:start=1568815264372462693,finish=1568815264378800500,duration=6337807,event=show_system_info[0Ktravis_time:start:005e3ccb[0Ktravis_time:end:005e3ccb:start=1568815264381800128,finish=1568815264414235173,duration=32435045,event=rm_riak_source[0Ktravis_time:start:03364d79[0Ktravis_time:end:03364d79:start=1568815264417739830,finish=1568815264423370588,duration=5630758,event=fix_rwky_redis[0Ktravis_time:start:02a50bd2[0Ktravis_time:end:02a50bd2:start=1568815264426703714,finish=1568815264847838548,duration=421134834,event=wait_for_network[0Ktravis_time:start:075fa472[0Ktravis_time:end:075fa472:start=1568815264852412123,finish=1568815265816087498,duration=963675375,event=update_apt_keys[0Ktravis_time:start:250546f2[0Ktravis_time:end:250546f2:start=1568815265821343010,finish=1568815266999530733,duration=1178187723,event=fix_hhvm_source[0Ktravis_time:start:002d2358[0Ktravis_time:end:002d2358:start=1568815267004473709,finish=1568815267014577507,duration=10103798,event=update_mongo_arch[0Ktravis_time:start:121d6184[0Ktravis_time:end:121d6184:start=1568815267019486841,finish=1568815267061630972,duration=42144131,event=fix_sudo_enabled_trusty[0Ktravis_time:start:03cd7d80[0Ktravis_time:end:03cd7d80:start=1568815267067467606,finish=1568815267070931135,duration=3463529,event=update_glibc[0Ktravis_time:start:0c9428e1[0Ktravis_time:end:0c9428e1:start=1568815267075182532,finish=1568815267085327358,duration=10144826,event=clean_up_path[0Ktravis_time:start:2807d474[0Ktravis_time:end:2807d474:start=1568815267089564492,finish=1568815267099503415,duration=9938923,event=fix_resolv_conf[0Ktravis_time:start:1e553bce[0Ktravis_time:end:1e553bce:start=1568815267106719090,finish=1568815267116856939,duration=10137849,event=fix_etc_hosts[0Ktravis_time:start:04363057[0Ktravis_time:end:04363057:start=1568815267121784801,finish=1568815267132174024,duration=10389223,event=fix_mvn_settings_xml[0Ktravis_time:start:22fe8000[0Ktravis_time:end:22fe8000:start=1568815267136525051,finish=1568815267147435481,duration=10910430,event=no_ipv6_localhost[0Ktravis_time:start:0d7a05d9[0Ktravis_time:end:0d7a05d9:start=1568815267152580602,finish=1568815267155542380,duration=2961778,event=fix_etc_mavenrc[0Ktravis_time:start:16d571a8[0Ktravis_time:end:16d571a8:start=1568815267160429636,finish=1568815267164061232,duration=3631596,event=fix_wwdr_certificate[0Ktravis_time:start:1faa6576[0Ktravis_time:end:1faa6576:start=1568815267169111487,finish=1568815267195716249,duration=26604762,event=put_localhost_first[0Ktravis_time:start:0845bba2[0Ktravis_time:end:0845bba2:start=1568815267200269181,finish=1568815267204558822,duration=4289641,event=home_paths[0Ktravis_time:start:0d822db8[0Ktravis_time:end:0d822db8:start=1568815267211794585,finish=1568815267224727187,duration=12932602,event=disable_initramfs[0Ktravis_time:start:07e1fce7[0Ktravis_time:end:07e1fce7:start=1568815267229889467,finish=1568815267611888500,duration=381999033,event=disable_ssh_roaming[0Ktravis_time:start:15f4cee4[0Ktravis_time:end:15f4cee4:start=1568815267617615067,finish=1568815267620578568,duration=2963501,event=debug_tools[0Ktravis_time:start:32fff2ee[0Ktravis_time:end:32fff2ee:start=1568815267627241753,finish=1568815267631184163,duration=3942410,event=uninstall_oclint[0Ktravis_time:start:292dc3d8[0Ktravis_time:end:292dc3d8:start=1568815267635964171,finish=1568815267639440481,duration=3476310,event=rvm_use[0Ktravis_time:start:006be471[0Ktravis_time:end:006be471:start=1568815267644153771,finish=1568815267653034477,duration=8880706,event=rm_etc_boto_cfg[0Ktravis_time:start:1e37d607[0Ktravis_time:end:1e37d607:start=1568815267657448426,finish=1568815267660824409,duration=3375983,event=rm_oraclejdk8_symlink[0Ktravis_time:start:135e634b[0Ktravis_time:end:135e634b:start=1568815267665393487,finish=1568815267726752056,duration=61358569,event=enable_i386[0Ktravis_time:start:014059fb[0Ktravis_time:end:014059fb:start=1568815267731972922,finish=1568815267737220249,duration=5247327,event=update_rubygems[0Ktravis_time:start:0db3b18b[0Ktravis_time:end:0db3b18b:start=1568815267742096174,finish=1568815268778096571,duration=1036000397,event=ensure_path_components[0Ktravis_time:start:3e2f0e78[0Ktravis_time:end:3e2f0e78:start=1568815268783200232,finish=1568815268786091567,duration=2891335,event=redefine_curl[0Ktravis_time:start:0421034f[0Ktravis_time:end:0421034f:start=1568815268791939583,finish=1568815268853083054,duration=61143471,event=nonblock_pipe[0Ktravis_time:start:06d607be[0Ktravis_time:end:06d607be:start=1568815268858252472,finish=1568815268899418996,duration=41166524,event=apt_get_update[0Ktravis_time:start:14827148[0Ktravis_time:end:14827148:start=1568815268904777169,finish=1568815268907686247,duration=2909078,event=deprecate_xcode_64[0Ktravis_time:start:00ea5c5e[0Ktravis_time:end:00ea5c5e:start=1568815268912339199,finish=1568815274129664325,duration=5217325126,event=update_heroku[0Ktravis_time:start:04358aa2[0Ktravis_time:end:04358aa2:start=1568815274135818137,finish=1568815274138973181,duration=3155044,event=shell_session_update[0Ktravis_time:start:023a0262[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3934
travis_fold:end:docker_mtu[0Ktravis_time:end:023a0262:start=1568815274143834387,finish=1568815275346848782,duration=1203014395,event=set_docker_mtu[0Ktravis_time:start:013be7f0[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:013be7f0:start=1568815275352046499,finish=1568815275424976702,duration=72930203,event=resolvconf[0Ktravis_time:start:1337c0f5[0Ktravis_time:end:1337c0f5:start=1568815275430182469,finish=1568815275547768146,duration=117585677,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:161e2c17[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:161e2c17:start=1568815275643157651,finish=1568815276005454317,duration=362296666,event=configure[0Ktravis_time:start:1524cd6c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1524cd6c:start=1568815276011239234,finish=1568815286988973461,duration=10977734227,event=configure[0Ktravis_time:start:0188407f[0Ktravis_fold:start:services[0Ktravis_time:start:03fb0f3e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:03fb0f3e:start=1568815287015232632,finish=1568815287030183816,duration=14951184,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03fb0f3e:start=1568815287015232632,finish=1568815290036020374,duration=3020787742,event=services[0Ktravis_time:start:2adab847[0Ktravis_time:end:2adab847:start=1568815290041317651,finish=1568815290044413003,duration=3095352,event=fix_ps4[0Ktravis_time:start:013aeb1e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:05bf230e[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:05bf230e:start=1568815290053943237,finish=1568815300810439460,duration=10756496223,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b989e40888b7bc80b4a7d6d823b98fc3ebb61025
travis_fold:end:git.checkout[0K
travis_time:end:05bf230e:start=1568815290053943237,finish=1568815301557643878,duration=11503700641,event=checkout[0Ktravis_time:start:09d8b18e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:09d8b18e:start=1568815301562971423,finish=1568815301575370101,duration=12398678,event=env[0Ktravis_time:start:0d354eec[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0d354eec:start=1568815301580478575,finish=1568815301586686889,duration=6208314,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1d368ea5[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {dealii-of,bindings,fe-fe,of-of_np,su2-ccx,of-of,of-ccx,of-ccx_fsi,nutils-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:1d368ea5:start=1568815301950545992,finish=1568815302015817369,duration=65271377,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:2c372914[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510188/log.txt)