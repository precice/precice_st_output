 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586518622) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/98) 
## Last succesfull commits 
* [su2-adapter](https://github.com/precice/su2-adapter/compare/a3186951163a...e8f7f22f56cb)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef) 
## Last 100 lines of the job log at the moment of push...
```
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
travis_time:end:0ffff1fe:start=1568824246851026581,finish=1568824246858584839,duration=7558258,event=show_system_info[0Ktravis_time:start:01431051[0Ktravis_time:end:01431051:start=1568824246861874316,finish=1568824246890628963,duration=28754647,event=rm_riak_source[0Ktravis_time:start:18605070[0Ktravis_time:end:18605070:start=1568824246894055538,finish=1568824246899469003,duration=5413465,event=fix_rwky_redis[0Ktravis_time:start:0ae14ef8[0Ktravis_time:end:0ae14ef8:start=1568824246902509811,finish=1568824247293279474,duration=390769663,event=wait_for_network[0Ktravis_time:start:069b9090[0Ktravis_time:end:069b9090:start=1568824247306420753,finish=1568824248962957087,duration=1656536334,event=update_apt_keys[0Ktravis_time:start:104dd5ac[0Ktravis_time:end:104dd5ac:start=1568824248968925868,finish=1568824250248299761,duration=1279373893,event=fix_hhvm_source[0Ktravis_time:start:047ac146[0Ktravis_time:end:047ac146:start=1568824250254704381,finish=1568824250268332359,duration=13627978,event=update_mongo_arch[0Ktravis_time:start:23aed66f[0Ktravis_time:end:23aed66f:start=1568824250273858540,finish=1568824250327532771,duration=53674231,event=fix_sudo_enabled_trusty[0Ktravis_time:start:173b303c[0Ktravis_time:end:173b303c:start=1568824250333666878,finish=1568824250337297818,duration=3630940,event=update_glibc[0Ktravis_time:start:1d22cf30[0Ktravis_time:end:1d22cf30:start=1568824250343176752,finish=1568824250357869145,duration=14692393,event=clean_up_path[0Ktravis_time:start:0f13bf18[0Ktravis_time:end:0f13bf18:start=1568824250365866964,finish=1568824250381293901,duration=15426937,event=fix_resolv_conf[0Ktravis_time:start:0e10bd68[0Ktravis_time:end:0e10bd68:start=1568824250388304837,finish=1568824250402146683,duration=13841846,event=fix_etc_hosts[0Ktravis_time:start:12ac92f9[0Ktravis_time:end:12ac92f9:start=1568824250408914265,finish=1568824250426124630,duration=17210365,event=fix_mvn_settings_xml[0Ktravis_time:start:1f02defe[0Ktravis_time:end:1f02defe:start=1568824250433461326,finish=1568824250447403095,duration=13941769,event=no_ipv6_localhost[0Ktravis_time:start:03d69338[0Ktravis_time:end:03d69338:start=1568824250455338935,finish=1568824250459090228,duration=3751293,event=fix_etc_mavenrc[0Ktravis_time:start:39e7f741[0Ktravis_time:end:39e7f741:start=1568824250464423067,finish=1568824250468297638,duration=3874571,event=fix_wwdr_certificate[0Ktravis_time:start:03ce2cc8[0Ktravis_time:end:03ce2cc8:start=1568824250474438172,finish=1568824250513435567,duration=38997395,event=put_localhost_first[0Ktravis_time:start:168bdd1a[0Ktravis_time:end:168bdd1a:start=1568824250519913103,finish=1568824250525579433,duration=5666330,event=home_paths[0Ktravis_time:start:0df0fe00[0Ktravis_time:end:0df0fe00:start=1568824250531737977,finish=1568824250551543056,duration=19805079,event=disable_initramfs[0Ktravis_time:start:2a54fff0[0Ktravis_time:end:2a54fff0:start=1568824250558321465,finish=1568824250955028677,duration=396707212,event=disable_ssh_roaming[0Ktravis_time:start:02363722[0Ktravis_time:end:02363722:start=1568824250964601178,finish=1568824250968982005,duration=4380827,event=debug_tools[0Ktravis_time:start:158da9a4[0Ktravis_time:end:158da9a4:start=1568824250977221156,finish=1568824250982730986,duration=5509830,event=uninstall_oclint[0Ktravis_time:start:17007d6b[0Ktravis_time:end:17007d6b:start=1568824250990951474,finish=1568824250996896089,duration=5944615,event=rvm_use[0Ktravis_time:start:090df0fe[0Ktravis_time:end:090df0fe:start=1568824251003137815,finish=1568824251015168533,duration=12030718,event=rm_etc_boto_cfg[0Ktravis_time:start:196d2080[0Ktravis_time:end:196d2080:start=1568824251022762154,finish=1568824251026625982,duration=3863828,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0db64156[0Ktravis_time:end:0db64156:start=1568824251036418320,finish=1568824251112374610,duration=75956290,event=enable_i386[0Ktravis_time:start:0a78bc17[0Ktravis_time:end:0a78bc17:start=1568824251119643472,finish=1568824251126004201,duration=6360729,event=update_rubygems[0Ktravis_time:start:111c1a46[0Ktravis_time:end:111c1a46:start=1568824251132101854,finish=1568824252395240355,duration=1263138501,event=ensure_path_components[0Ktravis_time:start:029e7345[0Ktravis_time:end:029e7345:start=1568824252399980611,finish=1568824252402836000,duration=2855389,event=redefine_curl[0Ktravis_time:start:22462350[0Ktravis_time:end:22462350:start=1568824252407538302,finish=1568824252464985506,duration=57447204,event=nonblock_pipe[0Ktravis_time:start:0786e0f0[0Ktravis_time:end:0786e0f0:start=1568824252470774511,finish=1568824252515212444,duration=44437933,event=apt_get_update[0Ktravis_time:start:00803a62[0Ktravis_time:end:00803a62:start=1568824252520433788,finish=1568824252523596513,duration=3162725,event=deprecate_xcode_64[0Ktravis_time:start:0534824a[0Ktravis_time:end:0534824a:start=1568824252528123903,finish=1568824258026723133,duration=5498599230,event=update_heroku[0Ktravis_time:start:381e76bb[0Ktravis_time:end:381e76bb:start=1568824258032934286,finish=1568824258037029883,duration=4095597,event=shell_session_update[0Ktravis_time:start:1bfa6340[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3928
travis_fold:end:docker_mtu[0Ktravis_time:end:1bfa6340:start=1568824258044425113,finish=1568824259265143655,duration=1220718542,event=set_docker_mtu[0Ktravis_time:start:01f883fa[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:01f883fa:start=1568824259269993818,finish=1568824259357282258,duration=87288440,event=resolvconf[0Ktravis_time:start:08c59cb0[0Ktravis_time:end:08c59cb0:start=1568824259365727501,finish=1568824259500784206,duration=135056705,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:01d974cc[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:01d974cc:start=1568824259623391619,finish=1568824260001241883,duration=377850264,event=configure[0Ktravis_time:start:00fd28bc[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:00fd28bc:start=1568824260007475250,finish=1568824273910097569,duration=13902622319,event=configure[0Ktravis_time:start:1968f896[0Ktravis_fold:start:services[0Ktravis_time:start:08f1797d[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08f1797d:start=1568824273936631104,finish=1568824273952770187,duration=16139083,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08f1797d:start=1568824273936631104,finish=1568824276959112913,duration=3022481809,event=services[0Ktravis_time:start:0e1c687c[0Ktravis_time:end:0e1c687c:start=1568824276963505678,finish=1568824276966745497,duration=3239819,event=fix_ps4[0Ktravis_time:start:02588928[0K
travis_fold:start:git.checkout[0Ktravis_time:start:007b0f60[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:007b0f60:start=1568824276976439567,finish=1568824288692318166,duration=11715878599,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0f9fa613[0K$ git fetch origin +refs/pull/98/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/98/merge -> FETCH_HEAD
travis_time:end:0f9fa613:start=1568824288698822669,finish=1568824289137988702,duration=439166033,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0f9fa613:start=1568824288698822669,finish=1568824289739396656,duration=1040573987,event=checkout[0Ktravis_time:start:2a8456fe[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2a8456fe:start=1568824289745815012,finish=1568824289761760359,duration=15945347,event=env[0Ktravis_time:start:02b4ec86[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:02b4ec86:start=1568824289769115766,finish=1568824289778285486,duration=9169720,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:033c68b8[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-of_np,dealii-of,of-of,su2-ccx,of-ccx_fsi,nutils-of,bindings,fe-fe,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:033c68b8:start=1568824290266604027,finish=1568824290342661557,duration=76057530,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:12f17400[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586518635/log.txt)