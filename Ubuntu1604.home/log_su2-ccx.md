 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586515488) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/28722fe13705...2efb54a69d10) 
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
travis_time:end:31f06920:start=1568819054713236508,finish=1568819054719193543,duration=5957035,event=show_system_info[0Ktravis_time:start:14b9f464[0Ktravis_time:end:14b9f464:start=1568819054722239787,finish=1568819054747310557,duration=25070770,event=rm_riak_source[0Ktravis_time:start:01155d02[0Ktravis_time:end:01155d02:start=1568819054750578664,finish=1568819054755895561,duration=5316897,event=fix_rwky_redis[0Ktravis_time:start:02b4bafe[0Ktravis_time:end:02b4bafe:start=1568819054758921388,finish=1568819055169758850,duration=410837462,event=wait_for_network[0Ktravis_time:start:0049a408[0Ktravis_time:end:0049a408:start=1568819055175402291,finish=1568819056773256611,duration=1597854320,event=update_apt_keys[0Ktravis_time:start:0af0d6c4[0Ktravis_time:end:0af0d6c4:start=1568819056777895910,finish=1568819057786172279,duration=1008276369,event=fix_hhvm_source[0Ktravis_time:start:116f4ab8[0Ktravis_time:end:116f4ab8:start=1568819057790256949,finish=1568819057800649735,duration=10392786,event=update_mongo_arch[0Ktravis_time:start:255c7040[0Ktravis_time:end:255c7040:start=1568819057804594580,finish=1568819057847512213,duration=42917633,event=fix_sudo_enabled_trusty[0Ktravis_time:start:22ead988[0Ktravis_time:end:22ead988:start=1568819057852162657,finish=1568819057854911687,duration=2749030,event=update_glibc[0Ktravis_time:start:06eb2de0[0Ktravis_time:end:06eb2de0:start=1568819057859349968,finish=1568819057868018741,duration=8668773,event=clean_up_path[0Ktravis_time:start:01386e19[0Ktravis_time:end:01386e19:start=1568819057872298360,finish=1568819057881208812,duration=8910452,event=fix_resolv_conf[0Ktravis_time:start:0fbb0980[0Ktravis_time:end:0fbb0980:start=1568819057885261736,finish=1568819057894639540,duration=9377804,event=fix_etc_hosts[0Ktravis_time:start:0b64f5b0[0Ktravis_time:end:0b64f5b0:start=1568819057899590829,finish=1568819057908603454,duration=9012625,event=fix_mvn_settings_xml[0Ktravis_time:start:06ec2f61[0Ktravis_time:end:06ec2f61:start=1568819057913033863,finish=1568819057923208897,duration=10175034,event=no_ipv6_localhost[0Ktravis_time:start:0f585576[0Ktravis_time:end:0f585576:start=1568819057928061187,finish=1568819057930911679,duration=2850492,event=fix_etc_mavenrc[0Ktravis_time:start:137448a8[0Ktravis_time:end:137448a8:start=1568819057935507693,finish=1568819057939304234,duration=3796541,event=fix_wwdr_certificate[0Ktravis_time:start:037905cb[0Ktravis_time:end:037905cb:start=1568819057944421519,finish=1568819057969342144,duration=24920625,event=put_localhost_first[0Ktravis_time:start:08516e14[0Ktravis_time:end:08516e14:start=1568819057974420538,finish=1568819057978335568,duration=3915030,event=home_paths[0Ktravis_time:start:0f4ebb20[0Ktravis_time:end:0f4ebb20:start=1568819057985261296,finish=1568819057997078763,duration=11817467,event=disable_initramfs[0Ktravis_time:start:0a2b561d[0Ktravis_time:end:0a2b561d:start=1568819058001514857,finish=1568819058299133338,duration=297618481,event=disable_ssh_roaming[0Ktravis_time:start:24941d74[0Ktravis_time:end:24941d74:start=1568819058303742359,finish=1568819058306653697,duration=2911338,event=debug_tools[0Ktravis_time:start:333dac2a[0Ktravis_time:end:333dac2a:start=1568819058311261621,finish=1568819058315587285,duration=4325664,event=uninstall_oclint[0Ktravis_time:start:262d27c0[0Ktravis_time:end:262d27c0:start=1568819058320598084,finish=1568819058324067615,duration=3469531,event=rvm_use[0Ktravis_time:start:1fd08689[0Ktravis_time:end:1fd08689:start=1568819058328661851,finish=1568819058337954830,duration=9292979,event=rm_etc_boto_cfg[0Ktravis_time:start:00242cbe[0Ktravis_time:end:00242cbe:start=1568819058342441813,finish=1568819058345058686,duration=2616873,event=rm_oraclejdk8_symlink[0Ktravis_time:start:22731564[0Ktravis_time:end:22731564:start=1568819058349072677,finish=1568819058403345530,duration=54272853,event=enable_i386[0Ktravis_time:start:03200c91[0Ktravis_time:end:03200c91:start=1568819058408167572,finish=1568819058412638358,duration=4470786,event=update_rubygems[0Ktravis_time:start:01c767bc[0Ktravis_time:end:01c767bc:start=1568819058417510579,finish=1568819059441188383,duration=1023677804,event=ensure_path_components[0Ktravis_time:start:099ef1c0[0Ktravis_time:end:099ef1c0:start=1568819059445750167,finish=1568819059448358279,duration=2608112,event=redefine_curl[0Ktravis_time:start:03de3e10[0Ktravis_time:end:03de3e10:start=1568819059452672505,finish=1568819059508182319,duration=55509814,event=nonblock_pipe[0Ktravis_time:start:004fac97[0Ktravis_time:end:004fac97:start=1568819059512206108,finish=1568819059555056003,duration=42849895,event=apt_get_update[0Ktravis_time:start:2faaeb10[0Ktravis_time:end:2faaeb10:start=1568819059559720168,finish=1568819059562272262,duration=2552094,event=deprecate_xcode_64[0Ktravis_time:start:1e071f70[0Ktravis_time:end:1e071f70:start=1568819059566337602,finish=1568819063990527613,duration=4424190011,event=update_heroku[0Ktravis_time:start:1bd00ae7[0Ktravis_time:end:1bd00ae7:start=1568819063995257659,finish=1568819063998726348,duration=3468689,event=shell_session_update[0Ktravis_time:start:15a5133e[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3830
travis_fold:end:docker_mtu[0Ktravis_time:end:15a5133e:start=1568819064003025787,finish=1568819065199133224,duration=1196107437,event=set_docker_mtu[0Ktravis_time:start:023e0f74[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:023e0f74:start=1568819065204181871,finish=1568819065268254872,duration=64073001,event=resolvconf[0Ktravis_time:start:0773bc28[0Ktravis_time:end:0773bc28:start=1568819065272616478,finish=1568819065366415704,duration=93799226,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:25ddb5f2[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:25ddb5f2:start=1568819065448120460,finish=1568819065986992440,duration=538871980,event=configure[0Ktravis_time:start:1a30d05a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1a30d05a:start=1568819065992804412,finish=1568819076131207709,duration=10138403297,event=configure[0Ktravis_time:start:26badc0b[0Ktravis_fold:start:services[0Ktravis_time:start:08eb846a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08eb846a:start=1568819076156111155,finish=1568819076169495044,duration=13383889,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08eb846a:start=1568819076156111155,finish=1568819079175521206,duration=3019410051,event=services[0Ktravis_time:start:0d5ef2d8[0Ktravis_time:end:0d5ef2d8:start=1568819079180562156,finish=1568819079183465416,duration=2903260,event=fix_ps4[0Ktravis_time:start:0fdf52e5[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1d276e64[0K$ git clone --depth=50 --branch=addUbuntu1904 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1d276e64:start=1568819079192522200,finish=1568819089252142150,duration=10059619950,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2efb54a69d10db47b6397a7d0e706ba82502d2ac
travis_fold:end:git.checkout[0K
travis_time:end:1d276e64:start=1568819079192522200,finish=1568819089457253150,duration=10264730950,event=checkout[0Ktravis_time:start:083bda50[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:083bda50:start=1568819089462297099,finish=1568819089473473441,duration=11176342,event=env[0Ktravis_time:start:0170f0bb[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0170f0bb:start=1568819089478775881,finish=1568819089484415457,duration=5639576,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:071bdc56[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {bindings,nutils-of,of-of,of-ccx_fsi,dealii-of,fe-fe,of-of_np,of-ccx,su2-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:071bdc56:start=1568819089833469599,finish=1568819089898563296,duration=65093697,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:090da92c[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586515503/log.txt)