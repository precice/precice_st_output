 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584299312) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/95) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903) 
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
travis_time:end:05ece591:start=1568328234946120582,finish=1568328234952623756,duration=6503174,event=show_system_info[0Ktravis_time:start:0ac61cb8[0Ktravis_time:end:0ac61cb8:start=1568328234955593444,finish=1568328234983475014,duration=27881570,event=rm_riak_source[0Ktravis_time:start:06b508b4[0Ktravis_time:end:06b508b4:start=1568328234987053027,finish=1568328234992462980,duration=5409953,event=fix_rwky_redis[0Ktravis_time:start:03789400[0Ktravis_time:end:03789400:start=1568328234995569549,finish=1568328235440169013,duration=444599464,event=wait_for_network[0Ktravis_time:start:10f46772[0Ktravis_time:end:10f46772:start=1568328235448763199,finish=1568328236381286348,duration=932523149,event=update_apt_keys[0Ktravis_time:start:0f585eb6[0Ktravis_time:end:0f585eb6:start=1568328236386449593,finish=1568328237440286739,duration=1053837146,event=fix_hhvm_source[0Ktravis_time:start:08095eac[0Ktravis_time:end:08095eac:start=1568328237445679486,finish=1568328237456097330,duration=10417844,event=update_mongo_arch[0Ktravis_time:start:06f732c0[0Ktravis_time:end:06f732c0:start=1568328237460917469,finish=1568328237503130788,duration=42213319,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0a5957f6[0Ktravis_time:end:0a5957f6:start=1568328237508420897,finish=1568328237511262275,duration=2841378,event=update_glibc[0Ktravis_time:start:35cb4d2c[0Ktravis_time:end:35cb4d2c:start=1568328237515911029,finish=1568328237524419425,duration=8508396,event=clean_up_path[0Ktravis_time:start:0206b84e[0Ktravis_time:end:0206b84e:start=1568328237528700680,finish=1568328237537421703,duration=8721023,event=fix_resolv_conf[0Ktravis_time:start:3be032a0[0Ktravis_time:end:3be032a0:start=1568328237541329366,finish=1568328237551339831,duration=10010465,event=fix_etc_hosts[0Ktravis_time:start:03a483fa[0Ktravis_time:end:03a483fa:start=1568328237558792145,finish=1568328237567981786,duration=9189641,event=fix_mvn_settings_xml[0Ktravis_time:start:00814af4[0Ktravis_time:end:00814af4:start=1568328237572456181,finish=1568328237582603874,duration=10147693,event=no_ipv6_localhost[0Ktravis_time:start:04309c50[0Ktravis_time:end:04309c50:start=1568328237587567325,finish=1568328237590479843,duration=2912518,event=fix_etc_mavenrc[0Ktravis_time:start:0c65b6e3[0Ktravis_time:end:0c65b6e3:start=1568328237595460638,finish=1568328237600157441,duration=4696803,event=fix_wwdr_certificate[0Ktravis_time:start:0251481a[0Ktravis_time:end:0251481a:start=1568328237605154944,finish=1568328237631972459,duration=26817515,event=put_localhost_first[0Ktravis_time:start:0f85fa46[0Ktravis_time:end:0f85fa46:start=1568328237637401941,finish=1568328237642847101,duration=5445160,event=home_paths[0Ktravis_time:start:0e716558[0Ktravis_time:end:0e716558:start=1568328237648513365,finish=1568328237665163270,duration=16649905,event=disable_initramfs[0Ktravis_time:start:0033b713[0Ktravis_time:end:0033b713:start=1568328237669912879,finish=1568328237969185328,duration=299272449,event=disable_ssh_roaming[0Ktravis_time:start:0fe1e7cc[0Ktravis_time:end:0fe1e7cc:start=1568328237974107475,finish=1568328237977077590,duration=2970115,event=debug_tools[0Ktravis_time:start:10f929f6[0Ktravis_time:end:10f929f6:start=1568328237981773340,finish=1568328237986151593,duration=4378253,event=uninstall_oclint[0Ktravis_time:start:036cfd53[0Ktravis_time:end:036cfd53:start=1568328237991022364,finish=1568328237995824195,duration=4801831,event=rvm_use[0Ktravis_time:start:2aa1e503[0Ktravis_time:end:2aa1e503:start=1568328238000812760,finish=1568328238009546482,duration=8733722,event=rm_etc_boto_cfg[0Ktravis_time:start:1122a662[0Ktravis_time:end:1122a662:start=1568328238013803668,finish=1568328238016464350,duration=2660682,event=rm_oraclejdk8_symlink[0Ktravis_time:start:27f79b80[0Ktravis_time:end:27f79b80:start=1568328238021290397,finish=1568328238075238160,duration=53947763,event=enable_i386[0Ktravis_time:start:0918a728[0Ktravis_time:end:0918a728:start=1568328238080054489,finish=1568328238084840071,duration=4785582,event=update_rubygems[0Ktravis_time:start:14350717[0Ktravis_time:end:14350717:start=1568328238089326729,finish=1568328239131310038,duration=1041983309,event=ensure_path_components[0Ktravis_time:start:08285826[0Ktravis_time:end:08285826:start=1568328239136183130,finish=1568328239139211850,duration=3028720,event=redefine_curl[0Ktravis_time:start:08941f96[0Ktravis_time:end:08941f96:start=1568328239144305702,finish=1568328239198870593,duration=54564891,event=nonblock_pipe[0Ktravis_time:start:0768ea91[0Ktravis_time:end:0768ea91:start=1568328239203841489,finish=1568328239256321463,duration=52479974,event=apt_get_update[0Ktravis_time:start:045c3218[0Ktravis_time:end:045c3218:start=1568328239261598805,finish=1568328239264566241,duration=2967436,event=deprecate_xcode_64[0Ktravis_time:start:0b86db75[0Ktravis_time:end:0b86db75:start=1568328239268946931,finish=1568328244406088588,duration=5137141657,event=update_heroku[0Ktravis_time:start:37dd50b8[0Ktravis_time:end:37dd50b8:start=1568328244411214572,finish=1568328244414135589,duration=2921017,event=shell_session_update[0Ktravis_time:start:008c1768[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3818
travis_fold:end:docker_mtu[0Ktravis_time:end:008c1768:start=1568328244419342519,finish=1568328245620489735,duration=1201147216,event=set_docker_mtu[0Ktravis_time:start:1504f2a8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1504f2a8:start=1568328245625623913,finish=1568328245698305003,duration=72681090,event=resolvconf[0Ktravis_time:start:33f58134[0Ktravis_time:end:33f58134:start=1568328245703478548,finish=1568328245819508525,duration=116029977,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:1df0bbfe[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:1df0bbfe:start=1568328245903183814,finish=1568328246501713690,duration=598529876,event=configure[0Ktravis_time:start:005e5260[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:005e5260:start=1568328246507405498,finish=1568328257742055898,duration=11234650400,event=configure[0Ktravis_time:start:075a7870[0Ktravis_fold:start:services[0Ktravis_time:start:095848d4[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:095848d4:start=1568328257768034533,finish=1568328257783509826,duration=15475293,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:095848d4:start=1568328257768034533,finish=1568328260789078179,duration=3021043646,event=services[0Ktravis_time:start:002726c4[0Ktravis_time:end:002726c4:start=1568328260794475825,finish=1568328260797488194,duration=3012369,event=fix_ps4[0Ktravis_time:start:072b8b64[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1f467dd7[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1f467dd7:start=1568328260806994976,finish=1568328271258733219,duration=10451738243,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:06734d64[0K$ git fetch origin +refs/pull/95/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/95/merge -> FETCH_HEAD
travis_time:end:06734d64:start=1568328271264134927,finish=1568328271714015926,duration=449880999,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:06734d64:start=1568328271264134927,finish=1568328271927028087,duration=662893160,event=checkout[0Ktravis_time:start:1ca6decf[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1ca6decf:start=1568328271932326754,finish=1568328271944476009,duration=12149255,event=env[0Ktravis_time:start:040f3f8c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:040f3f8c:start=1568328271949808630,finish=1568328271956177949,duration=6369319,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:05bb70e8[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {dealii-of,of-ccx_fsi,fe-fe,of-of_np,bindings,of-ccx,nutils-of,of-of,su2-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:05bb70e8:start=1568328272312203721,finish=1568328272379770912,duration=67567191,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:00b7633c[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584299330/log.txt)