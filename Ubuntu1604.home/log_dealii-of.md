 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584619352) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3433ca666766...b4f731a5d60e) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
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
travis_time:end:00f845a3:start=1568391994458224230,finish=1568391994464665601,duration=6441371,event=show_system_info[0Ktravis_time:start:29767f9c[0Ktravis_time:end:29767f9c:start=1568391994467664033,finish=1568391994498193058,duration=30529025,event=rm_riak_source[0Ktravis_time:start:1894efa4[0Ktravis_time:end:1894efa4:start=1568391994501449966,finish=1568391994506973190,duration=5523224,event=fix_rwky_redis[0Ktravis_time:start:124a476c[0Ktravis_time:end:124a476c:start=1568391994510157138,finish=1568391997005395039,duration=2495237901,event=wait_for_network[0Ktravis_time:start:14a99cb4[0Ktravis_time:end:14a99cb4:start=1568391997009892694,finish=1568392001133559461,duration=4123666767,event=update_apt_keys[0Ktravis_time:start:35ac0c42[0Ktravis_time:end:35ac0c42:start=1568392001139002855,finish=1568392002267509779,duration=1128506924,event=fix_hhvm_source[0Ktravis_time:start:0f422c2c[0Ktravis_time:end:0f422c2c:start=1568392002273513310,finish=1568392002284920875,duration=11407565,event=update_mongo_arch[0Ktravis_time:start:008888b9[0Ktravis_time:end:008888b9:start=1568392002290534051,finish=1568392002335921833,duration=45387782,event=fix_sudo_enabled_trusty[0Ktravis_time:start:04655c09[0Ktravis_time:end:04655c09:start=1568392002341888513,finish=1568392002346347666,duration=4459153,event=update_glibc[0Ktravis_time:start:01940dc0[0Ktravis_time:end:01940dc0:start=1568392002353137711,finish=1568392002363937768,duration=10800057,event=clean_up_path[0Ktravis_time:start:12d812a8[0Ktravis_time:end:12d812a8:start=1568392002368907849,finish=1568392002380116775,duration=11208926,event=fix_resolv_conf[0Ktravis_time:start:01e806b2[0Ktravis_time:end:01e806b2:start=1568392002385921342,finish=1568392002396275096,duration=10353754,event=fix_etc_hosts[0Ktravis_time:start:0048968a[0Ktravis_time:end:0048968a:start=1568392002401330912,finish=1568392002411511367,duration=10180455,event=fix_mvn_settings_xml[0Ktravis_time:start:156b4ef4[0Ktravis_time:end:156b4ef4:start=1568392002416859805,finish=1568392002427324029,duration=10464224,event=no_ipv6_localhost[0Ktravis_time:start:1e9cd9a0[0Ktravis_time:end:1e9cd9a0:start=1568392002432406779,finish=1568392002435215420,duration=2808641,event=fix_etc_mavenrc[0Ktravis_time:start:08a0a048[0Ktravis_time:end:08a0a048:start=1568392002440248158,finish=1568392002444471459,duration=4223301,event=fix_wwdr_certificate[0Ktravis_time:start:13914fc0[0Ktravis_time:end:13914fc0:start=1568392002449735783,finish=1568392002479179893,duration=29444110,event=put_localhost_first[0Ktravis_time:start:01659672[0Ktravis_time:end:01659672:start=1568392002484243362,finish=1568392002488301250,duration=4057888,event=home_paths[0Ktravis_time:start:179e810d[0Ktravis_time:end:179e810d:start=1568392002492658368,finish=1568392002506364768,duration=13706400,event=disable_initramfs[0Ktravis_time:start:05504cdd[0Ktravis_time:end:05504cdd:start=1568392002512835781,finish=1568392003231456715,duration=718620934,event=disable_ssh_roaming[0Ktravis_time:start:0040b594[0Ktravis_time:end:0040b594:start=1568392003237447390,finish=1568392003241545394,duration=4098004,event=debug_tools[0Ktravis_time:start:06cd6968[0Ktravis_time:end:06cd6968:start=1568392003246707415,finish=1568392003250536305,duration=3828890,event=uninstall_oclint[0Ktravis_time:start:237a8f50[0Ktravis_time:end:237a8f50:start=1568392003255457887,finish=1568392003259672788,duration=4214901,event=rvm_use[0Ktravis_time:start:2553f88e[0Ktravis_time:end:2553f88e:start=1568392003264564691,finish=1568392003277842665,duration=13277974,event=rm_etc_boto_cfg[0Ktravis_time:start:017dfee6[0Ktravis_time:end:017dfee6:start=1568392003282342345,finish=1568392003286773830,duration=4431485,event=rm_oraclejdk8_symlink[0Ktravis_time:start:052e3060[0Ktravis_time:end:052e3060:start=1568392003291882151,finish=1568392003349755361,duration=57873210,event=enable_i386[0Ktravis_time:start:10505c82[0Ktravis_time:end:10505c82:start=1568392003354228253,finish=1568392003359274201,duration=5045948,event=update_rubygems[0Ktravis_time:start:11900a17[0Ktravis_time:end:11900a17:start=1568392003363121893,finish=1568392004447019560,duration=1083897667,event=ensure_path_components[0Ktravis_time:start:01f2bf68[0Ktravis_time:end:01f2bf68:start=1568392004452739248,finish=1568392004455636682,duration=2897434,event=redefine_curl[0Ktravis_time:start:3a8f48de[0Ktravis_time:end:3a8f48de:start=1568392004460707296,finish=1568392004520545167,duration=59837871,event=nonblock_pipe[0Ktravis_time:start:0c585567[0Ktravis_time:end:0c585567:start=1568392004524908526,finish=1568392004595187992,duration=70279466,event=apt_get_update[0Ktravis_time:start:0ea28529[0Ktravis_time:end:0ea28529:start=1568392004600380061,finish=1568392004603429259,duration=3049198,event=deprecate_xcode_64[0Ktravis_time:start:00879c36[0Ktravis_time:end:00879c36:start=1568392004608971479,finish=1568392010567492788,duration=5958521309,event=update_heroku[0Ktravis_time:start:1e2e610c[0Ktravis_time:end:1e2e610c:start=1568392010572518925,finish=1568392010576776941,duration=4258016,event=shell_session_update[0Ktravis_time:start:016ddca8[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3943
travis_fold:end:docker_mtu[0Ktravis_time:end:016ddca8:start=1568392010582534763,finish=1568392011783898302,duration=1201363539,event=set_docker_mtu[0Ktravis_time:start:03f7f5bd[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:03f7f5bd:start=1568392011790621603,finish=1568392011865019685,duration=74398082,event=resolvconf[0Ktravis_time:start:0d8cd2cf[0Ktravis_time:end:0d8cd2cf:start=1568392011871554402,finish=1568392011992298853,duration=120744451,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00cb153d[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00cb153d:start=1568392012083674137,finish=1568392012493419157,duration=409745020,event=configure[0Ktravis_time:start:0694ad8a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0694ad8a:start=1568392012498821469,finish=1568392022720607201,duration=10221785732,event=configure[0Ktravis_time:start:1ce1aea8[0Ktravis_fold:start:services[0Ktravis_time:start:1b306920[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1b306920:start=1568392022748950301,finish=1568392022766921420,duration=17971119,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1b306920:start=1568392022748950301,finish=1568392025773404758,duration=3024454457,event=services[0Ktravis_time:start:0d1ee004[0Ktravis_time:end:0d1ee004:start=1568392025778339574,finish=1568392025781031133,duration=2691559,event=fix_ps4[0Ktravis_time:start:0c7e1a60[0K
travis_fold:start:git.checkout[0Ktravis_time:start:20ee0621[0K$ git clone --depth=50 --branch=code_aster_adapter https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:20ee0621:start=1568392025790734379,finish=1568392035987551984,duration=10196817605,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b4f731a5d60e7af97ee48400e5c51e279cd9f34f
travis_fold:end:git.checkout[0K
travis_time:end:20ee0621:start=1568392025790734379,finish=1568392036943611840,duration=11152877461,event=checkout[0Ktravis_time:start:04b84d18[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:04b84d18:start=1568392036948593703,finish=1568392036959115665,duration=10521962,event=env[0Ktravis_time:start:0518a250[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0518a250:start=1568392036966642190,finish=1568392036973868166,duration=7225976,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1472e9f2[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {dealii-of,of-ccx_fsi,of-ccx,nutils-of,bindings,of-of,su2-ccx,fe-fe,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:1472e9f2:start=1568392037344413278,finish=1568392037413389341,duration=68976063,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0a56bee0[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584619370/log.txt)