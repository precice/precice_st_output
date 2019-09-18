 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586515488) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/28722fe13705...2efb54a69d10) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
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
travis_time:end:1d7bd729:start=1568819274111966136,finish=1568819274117862450,duration=5896314,event=show_system_info[0Ktravis_time:start:1bca7d93[0Ktravis_time:end:1bca7d93:start=1568819274120743337,finish=1568819274144279667,duration=23536330,event=rm_riak_source[0Ktravis_time:start:0e2fdeea[0Ktravis_time:end:0e2fdeea:start=1568819274147503062,finish=1568819274152718564,duration=5215502,event=fix_rwky_redis[0Ktravis_time:start:378a4760[0Ktravis_time:end:378a4760:start=1568819274155690181,finish=1568819274566412281,duration=410722100,event=wait_for_network[0Ktravis_time:start:1297be3f[0Ktravis_time:end:1297be3f:start=1568819274570577464,finish=1568819275497669526,duration=927092062,event=update_apt_keys[0Ktravis_time:start:15919c80[0Ktravis_time:end:15919c80:start=1568819275502250366,finish=1568819276542823082,duration=1040572716,event=fix_hhvm_source[0Ktravis_time:start:00615c45[0Ktravis_time:end:00615c45:start=1568819276547426005,finish=1568819276557814167,duration=10388162,event=update_mongo_arch[0Ktravis_time:start:002d8c7c[0Ktravis_time:end:002d8c7c:start=1568819276563055998,finish=1568819276604843976,duration=41787978,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2e291cb0[0Ktravis_time:end:2e291cb0:start=1568819276609583254,finish=1568819276612502629,duration=2919375,event=update_glibc[0Ktravis_time:start:1f01a510[0Ktravis_time:end:1f01a510:start=1568819276616915199,finish=1568819276628383018,duration=11467819,event=clean_up_path[0Ktravis_time:start:007759c8[0Ktravis_time:end:007759c8:start=1568819276632556307,finish=1568819276640865573,duration=8309266,event=fix_resolv_conf[0Ktravis_time:start:02c45430[0Ktravis_time:end:02c45430:start=1568819276645553325,finish=1568819276654830503,duration=9277178,event=fix_etc_hosts[0Ktravis_time:start:033e843a[0Ktravis_time:end:033e843a:start=1568819276659550303,finish=1568819276668736931,duration=9186628,event=fix_mvn_settings_xml[0Ktravis_time:start:0c6c807c[0Ktravis_time:end:0c6c807c:start=1568819276673865856,finish=1568819276683683071,duration=9817215,event=no_ipv6_localhost[0Ktravis_time:start:103c75c6[0Ktravis_time:end:103c75c6:start=1568819276688602034,finish=1568819276691405065,duration=2803031,event=fix_etc_mavenrc[0Ktravis_time:start:199a50b0[0Ktravis_time:end:199a50b0:start=1568819276695824598,finish=1568819276699351974,duration=3527376,event=fix_wwdr_certificate[0Ktravis_time:start:1e055a8c[0Ktravis_time:end:1e055a8c:start=1568819276704387727,finish=1568819276730963860,duration=26576133,event=put_localhost_first[0Ktravis_time:start:13d05a80[0Ktravis_time:end:13d05a80:start=1568819276736541058,finish=1568819276740671743,duration=4130685,event=home_paths[0Ktravis_time:start:1e527da3[0Ktravis_time:end:1e527da3:start=1568819276745713603,finish=1568819276761147163,duration=15433560,event=disable_initramfs[0Ktravis_time:start:16e43e71[0Ktravis_time:end:16e43e71:start=1568819276766231944,finish=1568819277101168745,duration=334936801,event=disable_ssh_roaming[0Ktravis_time:start:20c917bc[0Ktravis_time:end:20c917bc:start=1568819277105930877,finish=1568819277108674389,duration=2743512,event=debug_tools[0Ktravis_time:start:00486387[0Ktravis_time:end:00486387:start=1568819277113556972,finish=1568819277117200437,duration=3643465,event=uninstall_oclint[0Ktravis_time:start:18fc7000[0Ktravis_time:end:18fc7000:start=1568819277121139716,finish=1568819277124944772,duration=3805056,event=rvm_use[0Ktravis_time:start:0c6c2648[0Ktravis_time:end:0c6c2648:start=1568819277129555698,finish=1568819277138584694,duration=9028996,event=rm_etc_boto_cfg[0Ktravis_time:start:06cd4244[0Ktravis_time:end:06cd4244:start=1568819277143536561,finish=1568819277146443754,duration=2907193,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0fd864e0[0Ktravis_time:end:0fd864e0:start=1568819277151076519,finish=1568819277207597871,duration=56521352,event=enable_i386[0Ktravis_time:start:06f121c0[0Ktravis_time:end:06f121c0:start=1568819277212389201,finish=1568819277216928226,duration=4539025,event=update_rubygems[0Ktravis_time:start:13155e4b[0Ktravis_time:end:13155e4b:start=1568819277221627923,finish=1568819278232046801,duration=1010418878,event=ensure_path_components[0Ktravis_time:start:230276d6[0Ktravis_time:end:230276d6:start=1568819278237135505,finish=1568819278240116176,duration=2980671,event=redefine_curl[0Ktravis_time:start:18bee789[0Ktravis_time:end:18bee789:start=1568819278245244770,finish=1568819278301586750,duration=56341980,event=nonblock_pipe[0Ktravis_time:start:0640ee2a[0Ktravis_time:end:0640ee2a:start=1568819278306534560,finish=1568819278359088980,duration=52554420,event=apt_get_update[0Ktravis_time:start:03ca7498[0Ktravis_time:end:03ca7498:start=1568819278363847390,finish=1568819278366546069,duration=2698679,event=deprecate_xcode_64[0Ktravis_time:start:15dbcf54[0Ktravis_time:end:15dbcf54:start=1568819278370690687,finish=1568819283351916848,duration=4981226161,event=update_heroku[0Ktravis_time:start:00896b00[0Ktravis_time:end:00896b00:start=1568819283356941753,finish=1568819283359808624,duration=2866871,event=shell_session_update[0Ktravis_time:start:135fad0a[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3846
travis_fold:end:docker_mtu[0Ktravis_time:end:135fad0a:start=1568819283364735882,finish=1568819284562057878,duration=1197321996,event=set_docker_mtu[0Ktravis_time:start:01d861ac[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:01d861ac:start=1568819284566899531,finish=1568819284636181190,duration=69281659,event=resolvconf[0Ktravis_time:start:01ffc7a3[0Ktravis_time:end:01ffc7a3:start=1568819284641426500,finish=1568819284747990274,duration=106563774,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:15b4dbc0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:15b4dbc0:start=1568819284831274087,finish=1568819285222869520,duration=391595433,event=configure[0Ktravis_time:start:014626e2[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:014626e2:start=1568819285228062408,finish=1568819295146042771,duration=9917980363,event=configure[0Ktravis_time:start:050f1788[0Ktravis_fold:start:services[0Ktravis_time:start:19a1b66e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:19a1b66e:start=1568819295172547698,finish=1568819295188316748,duration=15769050,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:19a1b66e:start=1568819295172547698,finish=1568819298193637687,duration=3021089989,event=services[0Ktravis_time:start:133cc3e2[0Ktravis_time:end:133cc3e2:start=1568819298199237441,finish=1568819298202460980,duration=3223539,event=fix_ps4[0Ktravis_time:start:1138df70[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0120d5bd[0K$ git clone --depth=50 --branch=addUbuntu1904 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0120d5bd:start=1568819298212185982,finish=1568819308276108270,duration=10063922288,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2efb54a69d10db47b6397a7d0e706ba82502d2ac
travis_fold:end:git.checkout[0K
travis_time:end:0120d5bd:start=1568819298212185982,finish=1568819308501074420,duration=10288888438,event=checkout[0Ktravis_time:start:0292a240[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0292a240:start=1568819308506816774,finish=1568819308519213616,duration=12396842,event=env[0Ktravis_time:start:02ca112a[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:02ca112a:start=1568819308525567695,finish=1568819308537328782,duration=11761087,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0e66b800[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,dealii-of,of-ccx,of-of_np,su2-ccx,of-of,fe-fe,nutils-of,bindings}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0e66b800:start=1568819308898681894,finish=1568819308966433347,duration=67751453,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:13153bc4[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586515506/log.txt)