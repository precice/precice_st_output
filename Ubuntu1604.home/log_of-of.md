 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586515488) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/28722fe13705...2efb54a69d10) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf) 
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
travis_time:end:00c7390e:start=1568819156206415197,finish=1568819156212632864,duration=6217667,event=show_system_info[0Ktravis_time:start:083e18a4[0Ktravis_time:end:083e18a4:start=1568819156215509140,finish=1568819156240828966,duration=25319826,event=rm_riak_source[0Ktravis_time:start:03ccb45a[0Ktravis_time:end:03ccb45a:start=1568819156243930390,finish=1568819156249084839,duration=5154449,event=fix_rwky_redis[0Ktravis_time:start:0154c90e[0Ktravis_time:end:0154c90e:start=1568819156252068918,finish=1568819156652213426,duration=400144508,event=wait_for_network[0Ktravis_time:start:0d13f040[0Ktravis_time:end:0d13f040:start=1568819156665515262,finish=1568819157623631720,duration=958116458,event=update_apt_keys[0Ktravis_time:start:0e7dde28[0Ktravis_time:end:0e7dde28:start=1568819157628257976,finish=1568819158647066847,duration=1018808871,event=fix_hhvm_source[0Ktravis_time:start:0482cac8[0Ktravis_time:end:0482cac8:start=1568819158651843142,finish=1568819158661917669,duration=10074527,event=update_mongo_arch[0Ktravis_time:start:24dd2bbc[0Ktravis_time:end:24dd2bbc:start=1568819158667403113,finish=1568819158709621867,duration=42218754,event=fix_sudo_enabled_trusty[0Ktravis_time:start:12278910[0Ktravis_time:end:12278910:start=1568819158714712916,finish=1568819158717639683,duration=2926767,event=update_glibc[0Ktravis_time:start:13f7d0a8[0Ktravis_time:end:13f7d0a8:start=1568819158722384472,finish=1568819158732164960,duration=9780488,event=clean_up_path[0Ktravis_time:start:082724ac[0Ktravis_time:end:082724ac:start=1568819158736930886,finish=1568819158746521741,duration=9590855,event=fix_resolv_conf[0Ktravis_time:start:2a9d2a77[0Ktravis_time:end:2a9d2a77:start=1568819158750367201,finish=1568819158761037869,duration=10670668,event=fix_etc_hosts[0Ktravis_time:start:15902640[0Ktravis_time:end:15902640:start=1568819158765428296,finish=1568819158775808909,duration=10380613,event=fix_mvn_settings_xml[0Ktravis_time:start:1a156ba6[0Ktravis_time:end:1a156ba6:start=1568819158780135304,finish=1568819158790062150,duration=9926846,event=no_ipv6_localhost[0Ktravis_time:start:035e2f99[0Ktravis_time:end:035e2f99:start=1568819158794248148,finish=1568819158796940052,duration=2691904,event=fix_etc_mavenrc[0Ktravis_time:start:23fcf928[0Ktravis_time:end:23fcf928:start=1568819158801303125,finish=1568819158804868975,duration=3565850,event=fix_wwdr_certificate[0Ktravis_time:start:16785dc0[0Ktravis_time:end:16785dc0:start=1568819158808945503,finish=1568819158834484276,duration=25538773,event=put_localhost_first[0Ktravis_time:start:14155952[0Ktravis_time:end:14155952:start=1568819158838803540,finish=1568819158842409469,duration=3605929,event=home_paths[0Ktravis_time:start:1feae424[0Ktravis_time:end:1feae424:start=1568819158846816905,finish=1568819158860965879,duration=14148974,event=disable_initramfs[0Ktravis_time:start:05bcbe08[0Ktravis_time:end:05bcbe08:start=1568819158865590907,finish=1568819159143107062,duration=277516155,event=disable_ssh_roaming[0Ktravis_time:start:0469ae74[0Ktravis_time:end:0469ae74:start=1568819159147549462,finish=1568819159150243002,duration=2693540,event=debug_tools[0Ktravis_time:start:01edc87c[0Ktravis_time:end:01edc87c:start=1568819159155353012,finish=1568819159159210437,duration=3857425,event=uninstall_oclint[0Ktravis_time:start:15d9bed4[0Ktravis_time:end:15d9bed4:start=1568819159164202136,finish=1568819159168040319,duration=3838183,event=rvm_use[0Ktravis_time:start:33e20ca4[0Ktravis_time:end:33e20ca4:start=1568819159175137776,finish=1568819159183385931,duration=8248155,event=rm_etc_boto_cfg[0Ktravis_time:start:03e57fac[0Ktravis_time:end:03e57fac:start=1568819159188132548,finish=1568819159190779994,duration=2647446,event=rm_oraclejdk8_symlink[0Ktravis_time:start:36623565[0Ktravis_time:end:36623565:start=1568819159194972792,finish=1568819159249420016,duration=54447224,event=enable_i386[0Ktravis_time:start:29a3f4ec[0Ktravis_time:end:29a3f4ec:start=1568819159254001770,finish=1568819159259790193,duration=5788423,event=update_rubygems[0Ktravis_time:start:1b023461[0Ktravis_time:end:1b023461:start=1568819159265110455,finish=1568819160272606857,duration=1007496402,event=ensure_path_components[0Ktravis_time:start:0e22b8f0[0Ktravis_time:end:0e22b8f0:start=1568819160278862006,finish=1568819160282196267,duration=3334261,event=redefine_curl[0Ktravis_time:start:10ac91d4[0Ktravis_time:end:10ac91d4:start=1568819160288373274,finish=1568819160345528274,duration=57155000,event=nonblock_pipe[0Ktravis_time:start:022eec16[0Ktravis_time:end:022eec16:start=1568819160351167001,finish=1568819160391956729,duration=40789728,event=apt_get_update[0Ktravis_time:start:08f1be74[0Ktravis_time:end:08f1be74:start=1568819160396338626,finish=1568819160399619895,duration=3281269,event=deprecate_xcode_64[0Ktravis_time:start:186f4638[0Ktravis_time:end:186f4638:start=1568819160405214035,finish=1568819165120475019,duration=4715260984,event=update_heroku[0Ktravis_time:start:373ad16d[0Ktravis_time:end:373ad16d:start=1568819165125059354,finish=1568819165127724778,duration=2665424,event=shell_session_update[0Ktravis_time:start:21e15aab[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3862
travis_fold:end:docker_mtu[0Ktravis_time:end:21e15aab:start=1568819165132630108,finish=1568819166318937329,duration=1186307221,event=set_docker_mtu[0Ktravis_time:start:0e25adf0[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0e25adf0:start=1568819166322666337,finish=1568819166385992353,duration=63326016,event=resolvconf[0Ktravis_time:start:008b7d1e[0Ktravis_time:end:008b7d1e:start=1568819166390907885,finish=1568819166493025061,duration=102117176,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:05a06150[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:05a06150:start=1568819166575547789,finish=1568819167042650026,duration=467102237,event=configure[0Ktravis_time:start:00b4aa28[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:00b4aa28:start=1568819167047659276,finish=1568819176632259514,duration=9584600238,event=configure[0Ktravis_time:start:08615654[0Ktravis_fold:start:services[0Ktravis_time:start:0f8b7f58[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0f8b7f58:start=1568819176657406810,finish=1568819176671689835,duration=14283025,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0f8b7f58:start=1568819176657406810,finish=1568819179676445692,duration=3019038882,event=services[0Ktravis_time:start:1bd83018[0Ktravis_time:end:1bd83018:start=1568819179680882378,finish=1568819179683750727,duration=2868349,event=fix_ps4[0Ktravis_time:start:180f6280[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1290f057[0K$ git clone --depth=50 --branch=addUbuntu1904 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1290f057:start=1568819179692745291,finish=1568819204637231070,duration=24944485779,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2efb54a69d10db47b6397a7d0e706ba82502d2ac
travis_fold:end:git.checkout[0K
travis_time:end:1290f057:start=1568819179692745291,finish=1568819205223001931,duration=25530256640,event=checkout[0Ktravis_time:start:24d7f07c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:24d7f07c:start=1568819205227970812,finish=1568819205239645221,duration=11674409,event=env[0Ktravis_time:start:1d38e600[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1d38e600:start=1568819205245213301,finish=1568819205252533130,duration=7319829,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0b5efa05[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,dealii-of,nutils-of,su2-ccx,of-ccx,bindings,fe-fe,of-of,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0b5efa05:start=1568819205613388690,finish=1568819205681291396,duration=67902706,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:169c0ce1[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586515504/log.txt)