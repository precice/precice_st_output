 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584299312) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/95) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/04b8ebd5c55ebbaeb7c87975ab50a3cd63e0c4f4...54b96c7718c6c434cfc8b2262d3057a82de97903)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
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
travis_time:end:062b33cf:start=1568327950853043903,finish=1568327950859347038,duration=6303135,event=show_system_info[0Ktravis_time:start:02b03352[0Ktravis_time:end:02b03352:start=1568327950862340298,finish=1568327950888963682,duration=26623384,event=rm_riak_source[0Ktravis_time:start:16c43e26[0Ktravis_time:end:16c43e26:start=1568327950892684799,finish=1568327950898501401,duration=5816602,event=fix_rwky_redis[0Ktravis_time:start:26d12a80[0Ktravis_time:end:26d12a80:start=1568327950901701443,finish=1568327956282450860,duration=5380749417,event=wait_for_network[0Ktravis_time:start:1c37adef[0Ktravis_time:end:1c37adef:start=1568327956287721080,finish=1568327957881203073,duration=1593481993,event=update_apt_keys[0Ktravis_time:start:0cb805d2[0Ktravis_time:end:0cb805d2:start=1568327957886291390,finish=1568327958987943090,duration=1101651700,event=fix_hhvm_source[0Ktravis_time:start:018b7210[0Ktravis_time:end:018b7210:start=1568327958992445436,finish=1568327959004087394,duration=11641958,event=update_mongo_arch[0Ktravis_time:start:11e125af[0Ktravis_time:end:11e125af:start=1568327959009110282,finish=1568327959056574090,duration=47463808,event=fix_sudo_enabled_trusty[0Ktravis_time:start:04cf06d0[0Ktravis_time:end:04cf06d0:start=1568327959061662337,finish=1568327959064601995,duration=2939658,event=update_glibc[0Ktravis_time:start:21173b23[0Ktravis_time:end:21173b23:start=1568327959071032240,finish=1568327959080846145,duration=9813905,event=clean_up_path[0Ktravis_time:start:28e8f99c[0Ktravis_time:end:28e8f99c:start=1568327959085367156,finish=1568327959097368936,duration=12001780,event=fix_resolv_conf[0Ktravis_time:start:05fec2ad[0Ktravis_time:end:05fec2ad:start=1568327959102225405,finish=1568327959113119081,duration=10893676,event=fix_etc_hosts[0Ktravis_time:start:1e861286[0Ktravis_time:end:1e861286:start=1568327959117838034,finish=1568327959128437411,duration=10599377,event=fix_mvn_settings_xml[0Ktravis_time:start:1792a6af[0Ktravis_time:end:1792a6af:start=1568327959133801909,finish=1568327959145160025,duration=11358116,event=no_ipv6_localhost[0Ktravis_time:start:142b2128[0Ktravis_time:end:142b2128:start=1568327959150921350,finish=1568327959154306538,duration=3385188,event=fix_etc_mavenrc[0Ktravis_time:start:17f5971d[0Ktravis_time:end:17f5971d:start=1568327959158840399,finish=1568327959162712347,duration=3871948,event=fix_wwdr_certificate[0Ktravis_time:start:0732f5e8[0Ktravis_time:end:0732f5e8:start=1568327959167526205,finish=1568327959196782276,duration=29256071,event=put_localhost_first[0Ktravis_time:start:10dd08a6[0Ktravis_time:end:10dd08a6:start=1568327959201643200,finish=1568327959205844237,duration=4201037,event=home_paths[0Ktravis_time:start:062c46be[0Ktravis_time:end:062c46be:start=1568327959211045129,finish=1568327959225821051,duration=14775922,event=disable_initramfs[0Ktravis_time:start:057afe18[0Ktravis_time:end:057afe18:start=1568327959230877399,finish=1568327959568043222,duration=337165823,event=disable_ssh_roaming[0Ktravis_time:start:0b8b2e50[0Ktravis_time:end:0b8b2e50:start=1568327959572998704,finish=1568327959576395754,duration=3397050,event=debug_tools[0Ktravis_time:start:0fafb4d4[0Ktravis_time:end:0fafb4d4:start=1568327959581642135,finish=1568327959585581460,duration=3939325,event=uninstall_oclint[0Ktravis_time:start:25ece7e8[0Ktravis_time:end:25ece7e8:start=1568327959590491373,finish=1568327959595957977,duration=5466604,event=rvm_use[0Ktravis_time:start:026494d2[0Ktravis_time:end:026494d2:start=1568327959600581618,finish=1568327959609813092,duration=9231474,event=rm_etc_boto_cfg[0Ktravis_time:start:0a282b42[0Ktravis_time:end:0a282b42:start=1568327959614785436,finish=1568327959618250454,duration=3465018,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0eee6ef8[0Ktravis_time:end:0eee6ef8:start=1568327959622904912,finish=1568327959694100243,duration=71195331,event=enable_i386[0Ktravis_time:start:1e5e9a64[0Ktravis_time:end:1e5e9a64:start=1568327959699548133,finish=1568327959704359823,duration=4811690,event=update_rubygems[0Ktravis_time:start:0d485500[0Ktravis_time:end:0d485500:start=1568327959709884996,finish=1568327960785798341,duration=1075913345,event=ensure_path_components[0Ktravis_time:start:0006fdf0[0Ktravis_time:end:0006fdf0:start=1568327960790215134,finish=1568327960792768295,duration=2553161,event=redefine_curl[0Ktravis_time:start:02a3c274[0Ktravis_time:end:02a3c274:start=1568327960796868083,finish=1568327960851702612,duration=54834529,event=nonblock_pipe[0Ktravis_time:start:1762988a[0Ktravis_time:end:1762988a:start=1568327960856368906,finish=1568327960898755849,duration=42386943,event=apt_get_update[0Ktravis_time:start:069cd294[0Ktravis_time:end:069cd294:start=1568327960903152619,finish=1568327960906267053,duration=3114434,event=deprecate_xcode_64[0Ktravis_time:start:05dd4e42[0Ktravis_time:end:05dd4e42:start=1568327960913181826,finish=1568327965674581208,duration=4761399382,event=update_heroku[0Ktravis_time:start:215a76b0[0Ktravis_time:end:215a76b0:start=1568327965680440000,finish=1568327965684026283,duration=3586283,event=shell_session_update[0Ktravis_time:start:0bc64f9f[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3932
travis_fold:end:docker_mtu[0Ktravis_time:end:0bc64f9f:start=1568327965690048833,finish=1568327966904480814,duration=1214431981,event=set_docker_mtu[0Ktravis_time:start:085d918c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:085d918c:start=1568327966909280899,finish=1568327966977204728,duration=67923829,event=resolvconf[0Ktravis_time:start:38bba872[0Ktravis_time:end:38bba872:start=1568327966982286667,finish=1568327967077573564,duration=95286897,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:024b6eb8[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:024b6eb8:start=1568327967160892836,finish=1568327967522724032,duration=361831196,event=configure[0Ktravis_time:start:177fe378[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:177fe378:start=1568327967527581112,finish=1568327979829233779,duration=12301652667,event=configure[0Ktravis_time:start:220029a8[0Ktravis_fold:start:services[0Ktravis_time:start:1d785c80[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1d785c80:start=1568327979859948151,finish=1568327979878182138,duration=18233987,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1d785c80:start=1568327979859948151,finish=1568327982885103631,duration=3025155480,event=services[0Ktravis_time:start:0ba0797a[0Ktravis_time:end:0ba0797a:start=1568327982890216581,finish=1568327982893627619,duration=3411038,event=fix_ps4[0Ktravis_time:start:0200bcbf[0K
travis_fold:start:git.checkout[0Ktravis_time:start:270bafff[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:270bafff:start=1568327982904011125,finish=1568327994021062586,duration=11117051461,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0aee0459[0K$ git fetch origin +refs/pull/95/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/95/merge -> FETCH_HEAD
travis_time:end:0aee0459:start=1568327994025377891,finish=1568327994473409410,duration=448031519,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0aee0459:start=1568327994025377891,finish=1568327994503646873,duration=478268982,event=checkout[0Ktravis_time:start:2546eb8b[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2546eb8b:start=1568327994509694089,finish=1568327994522107007,duration=12412918,event=env[0Ktravis_time:start:177d6c9e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:177d6c9e:start=1568327994528908835,finish=1568327994537065331,duration=8156496,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0462f78c[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-of_np,nutils-of,of-ccx,of-of,dealii-of,su2-ccx,bindings,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0462f78c:start=1568327994968535937,finish=1568327995043822748,duration=75286811,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:02cdecb8[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584299326/log.txt)