 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584619352) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3433ca666766...b4f731a5d60e) 
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
travis_time:end:0668c5c3:start=1568391479777939565,finish=1568391479783677804,duration=5738239,event=show_system_info[0Ktravis_time:start:0a734b2a[0Ktravis_time:end:0a734b2a:start=1568391479786381940,finish=1568391479811227201,duration=24845261,event=rm_riak_source[0Ktravis_time:start:09d865b8[0Ktravis_time:end:09d865b8:start=1568391479814791331,finish=1568391479820974979,duration=6183648,event=fix_rwky_redis[0Ktravis_time:start:0cfed36f[0Ktravis_time:end:0cfed36f:start=1568391479824146579,finish=1568391480231565206,duration=407418627,event=wait_for_network[0Ktravis_time:start:105897ff[0Ktravis_time:end:105897ff:start=1568391480236508520,finish=1568391481823291794,duration=1586783274,event=update_apt_keys[0Ktravis_time:start:2a2b4bc8[0Ktravis_time:end:2a2b4bc8:start=1568391481827807279,finish=1568391482860948452,duration=1033141173,event=fix_hhvm_source[0Ktravis_time:start:02924ac0[0Ktravis_time:end:02924ac0:start=1568391482865958245,finish=1568391482876013102,duration=10054857,event=update_mongo_arch[0Ktravis_time:start:18f7923f[0Ktravis_time:end:18f7923f:start=1568391482880694950,finish=1568391482922084093,duration=41389143,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0f3eee0a[0Ktravis_time:end:0f3eee0a:start=1568391482927464818,finish=1568391482930604398,duration=3139580,event=update_glibc[0Ktravis_time:start:020ae290[0Ktravis_time:end:020ae290:start=1568391482935895272,finish=1568391482944965035,duration=9069763,event=clean_up_path[0Ktravis_time:start:33678d32[0Ktravis_time:end:33678d32:start=1568391482949471577,finish=1568391482958193805,duration=8722228,event=fix_resolv_conf[0Ktravis_time:start:21ef8068[0Ktravis_time:end:21ef8068:start=1568391482962816984,finish=1568391482971811597,duration=8994613,event=fix_etc_hosts[0Ktravis_time:start:04103e02[0Ktravis_time:end:04103e02:start=1568391482977145998,finish=1568391482986947997,duration=9801999,event=fix_mvn_settings_xml[0Ktravis_time:start:0356fbff[0Ktravis_time:end:0356fbff:start=1568391482991592934,finish=1568391483001713400,duration=10120466,event=no_ipv6_localhost[0Ktravis_time:start:078c4f55[0Ktravis_time:end:078c4f55:start=1568391483006214845,finish=1568391483009162904,duration=2948059,event=fix_etc_mavenrc[0Ktravis_time:start:14350896[0Ktravis_time:end:14350896:start=1568391483013469800,finish=1568391483017385639,duration=3915839,event=fix_wwdr_certificate[0Ktravis_time:start:0a8be708[0Ktravis_time:end:0a8be708:start=1568391483022330694,finish=1568391483046366835,duration=24036141,event=put_localhost_first[0Ktravis_time:start:0632df7e[0Ktravis_time:end:0632df7e:start=1568391483051134767,finish=1568391483054920462,duration=3785695,event=home_paths[0Ktravis_time:start:001652ee[0Ktravis_time:end:001652ee:start=1568391483059338516,finish=1568391483072760401,duration=13421885,event=disable_initramfs[0Ktravis_time:start:103dec25[0Ktravis_time:end:103dec25:start=1568391483077861844,finish=1568391483390731474,duration=312869630,event=disable_ssh_roaming[0Ktravis_time:start:01956739[0Ktravis_time:end:01956739:start=1568391483395696224,finish=1568391483398932841,duration=3236617,event=debug_tools[0Ktravis_time:start:07422e5d[0Ktravis_time:end:07422e5d:start=1568391483402886624,finish=1568391483406891491,duration=4004867,event=uninstall_oclint[0Ktravis_time:start:02a59e00[0Ktravis_time:end:02a59e00:start=1568391483410711225,finish=1568391483414406134,duration=3694909,event=rvm_use[0Ktravis_time:start:03163110[0Ktravis_time:end:03163110:start=1568391483418100015,finish=1568391483435940650,duration=17840635,event=rm_etc_boto_cfg[0Ktravis_time:start:0ca3e37e[0Ktravis_time:end:0ca3e37e:start=1568391483439823938,finish=1568391483442631374,duration=2807436,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0f26f37c[0Ktravis_time:end:0f26f37c:start=1568391483446346378,finish=1568391483505262129,duration=58915751,event=enable_i386[0Ktravis_time:start:026d636c[0Ktravis_time:end:026d636c:start=1568391483509339947,finish=1568391483513869062,duration=4529115,event=update_rubygems[0Ktravis_time:start:1f3dc910[0Ktravis_time:end:1f3dc910:start=1568391483518185061,finish=1568391484531297269,duration=1013112208,event=ensure_path_components[0Ktravis_time:start:314f7f00[0Ktravis_time:end:314f7f00:start=1568391484536703614,finish=1568391484540311385,duration=3607771,event=redefine_curl[0Ktravis_time:start:1496f6b2[0Ktravis_time:end:1496f6b2:start=1568391484545137792,finish=1568391484602286619,duration=57148827,event=nonblock_pipe[0Ktravis_time:start:10640ce8[0Ktravis_time:end:10640ce8:start=1568391484606550361,finish=1568391484651420945,duration=44870584,event=apt_get_update[0Ktravis_time:start:018586fc[0Ktravis_time:end:018586fc:start=1568391484656330848,finish=1568391484658977106,duration=2646258,event=deprecate_xcode_64[0Ktravis_time:start:0bcfe2b0[0Ktravis_time:end:0bcfe2b0:start=1568391484664154075,finish=1568391489425956236,duration=4761802161,event=update_heroku[0Ktravis_time:start:00194940[0Ktravis_time:end:00194940:start=1568391489430581682,finish=1568391489433250080,duration=2668398,event=shell_session_update[0Ktravis_time:start:017a4c67[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3929
travis_fold:end:docker_mtu[0Ktravis_time:end:017a4c67:start=1568391489437606307,finish=1568391490633577517,duration=1195971210,event=set_docker_mtu[0Ktravis_time:start:001dcce8[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:001dcce8:start=1568391490638304629,finish=1568391490705894523,duration=67589894,event=resolvconf[0Ktravis_time:start:0cd62848[0Ktravis_time:end:0cd62848:start=1568391490711651027,finish=1568391490809272664,duration=97621637,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:10d8039c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:10d8039c:start=1568391490896069649,finish=1568391492367451760,duration=1471382111,event=configure[0Ktravis_time:start:030774f8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:030774f8:start=1568391492372727850,finish=1568391501995863814,duration=9623135964,event=configure[0Ktravis_time:start:03767232[0Ktravis_fold:start:services[0Ktravis_time:start:0472a3f4[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0472a3f4:start=1568391502020789571,finish=1568391502034748057,duration=13958486,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0472a3f4:start=1568391502020789571,finish=1568391505039803084,duration=3019013513,event=services[0Ktravis_time:start:04332c98[0Ktravis_time:end:04332c98:start=1568391505044032414,finish=1568391505047235740,duration=3203326,event=fix_ps4[0Ktravis_time:start:0de9d6b6[0K
travis_fold:start:git.checkout[0Ktravis_time:start:031a639e[0K$ git clone --depth=50 --branch=code_aster_adapter https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:031a639e:start=1568391505054759490,finish=1568391515551439926,duration=10496680436,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b4f731a5d60e7af97ee48400e5c51e279cd9f34f
travis_fold:end:git.checkout[0K
travis_time:end:031a639e:start=1568391505054759490,finish=1568391516032218003,duration=10977458513,event=checkout[0Ktravis_time:start:249a16ee[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:249a16ee:start=1568391516036715626,finish=1568391516047245335,duration=10529709,event=env[0Ktravis_time:start:2fdebf6e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:2fdebf6e:start=1568391516051944375,finish=1568391516058544513,duration=6600138,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2bf7ba33[0K$ python system_testing.py -s su2-ccx
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,of-ccx,of-ccx_fsi,nutils-of,of-of_np,bindings,fe-fe,dealii-of,of-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:2bf7ba33:start=1568391516399761215,finish=1568391516465354007,duration=65592792,event=script[0K[31;1mThe command "python system_testing.py -s su2-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:06526ac4[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584619365/log.txt)