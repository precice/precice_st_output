 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510170) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/40d6daa277c6...b989e40888b7) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
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
travis_time:end:1196154a:start=1568815073772032117,finish=1568815073777485160,duration=5453043,event=show_system_info[0Ktravis_time:start:01f97b20[0Ktravis_time:end:01f97b20:start=1568815073780243242,finish=1568815073802842051,duration=22598809,event=rm_riak_source[0Ktravis_time:start:08ed2e70[0Ktravis_time:end:08ed2e70:start=1568815073805590966,finish=1568815073810405805,duration=4814839,event=fix_rwky_redis[0Ktravis_time:start:11ec2540[0Ktravis_time:end:11ec2540:start=1568815073813141014,finish=1568815074171455040,duration=358314026,event=wait_for_network[0Ktravis_time:start:070e8b5d[0Ktravis_time:end:070e8b5d:start=1568815074191652079,finish=1568815075876218609,duration=1684566530,event=update_apt_keys[0Ktravis_time:start:19172f4e[0Ktravis_time:end:19172f4e:start=1568815075880754877,finish=1568815076895105969,duration=1014351092,event=fix_hhvm_source[0Ktravis_time:start:055fc907[0Ktravis_time:end:055fc907:start=1568815076900527804,finish=1568815076911839479,duration=11311675,event=update_mongo_arch[0Ktravis_time:start:2631cb64[0Ktravis_time:end:2631cb64:start=1568815076916691166,finish=1568815076958776313,duration=42085147,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0293e6c4[0Ktravis_time:end:0293e6c4:start=1568815076963717388,finish=1568815076966345897,duration=2628509,event=update_glibc[0Ktravis_time:start:1b63e924[0Ktravis_time:end:1b63e924:start=1568815076970782644,finish=1568815076980155197,duration=9372553,event=clean_up_path[0Ktravis_time:start:1efaa40c[0Ktravis_time:end:1efaa40c:start=1568815076984606420,finish=1568815076993837355,duration=9230935,event=fix_resolv_conf[0Ktravis_time:start:141e3241[0Ktravis_time:end:141e3241:start=1568815076998011580,finish=1568815077008010435,duration=9998855,event=fix_etc_hosts[0Ktravis_time:start:17311030[0Ktravis_time:end:17311030:start=1568815077012526296,finish=1568815077022833684,duration=10307388,event=fix_mvn_settings_xml[0Ktravis_time:start:10146c2a[0Ktravis_time:end:10146c2a:start=1568815077027662019,finish=1568815077038231115,duration=10569096,event=no_ipv6_localhost[0Ktravis_time:start:07cafcf4[0Ktravis_time:end:07cafcf4:start=1568815077042838567,finish=1568815077045532838,duration=2694271,event=fix_etc_mavenrc[0Ktravis_time:start:0acf5105[0Ktravis_time:end:0acf5105:start=1568815077050275856,finish=1568815077053744995,duration=3469139,event=fix_wwdr_certificate[0Ktravis_time:start:247c79d0[0Ktravis_time:end:247c79d0:start=1568815077059360059,finish=1568815077083495397,duration=24135338,event=put_localhost_first[0Ktravis_time:start:11478027[0Ktravis_time:end:11478027:start=1568815077087987763,finish=1568815077091560217,duration=3572454,event=home_paths[0Ktravis_time:start:0153a5b0[0Ktravis_time:end:0153a5b0:start=1568815077095850748,finish=1568815077108990119,duration=13139371,event=disable_initramfs[0Ktravis_time:start:079efcb4[0Ktravis_time:end:079efcb4:start=1568815077112989322,finish=1568815077360465564,duration=247476242,event=disable_ssh_roaming[0Ktravis_time:start:142d9be6[0Ktravis_time:end:142d9be6:start=1568815077364707933,finish=1568815077368421152,duration=3713219,event=debug_tools[0Ktravis_time:start:03604dc5[0Ktravis_time:end:03604dc5:start=1568815077372441883,finish=1568815077376701684,duration=4259801,event=uninstall_oclint[0Ktravis_time:start:09e522b5[0Ktravis_time:end:09e522b5:start=1568815077380766154,finish=1568815077384890402,duration=4124248,event=rvm_use[0Ktravis_time:start:15054774[0Ktravis_time:end:15054774:start=1568815077391726332,finish=1568815077399623114,duration=7896782,event=rm_etc_boto_cfg[0Ktravis_time:start:075b87f2[0Ktravis_time:end:075b87f2:start=1568815077403695525,finish=1568815077406415671,duration=2720146,event=rm_oraclejdk8_symlink[0Ktravis_time:start:05c2f614[0Ktravis_time:end:05c2f614:start=1568815077410044431,finish=1568815077463657241,duration=53612810,event=enable_i386[0Ktravis_time:start:02d35e98[0Ktravis_time:end:02d35e98:start=1568815077467974378,finish=1568815077472060789,duration=4086411,event=update_rubygems[0Ktravis_time:start:001ceaee[0Ktravis_time:end:001ceaee:start=1568815077476064943,finish=1568815078466985021,duration=990920078,event=ensure_path_components[0Ktravis_time:start:18424ab5[0Ktravis_time:end:18424ab5:start=1568815078471961729,finish=1568815078474910906,duration=2949177,event=redefine_curl[0Ktravis_time:start:00075efe[0Ktravis_time:end:00075efe:start=1568815078479512175,finish=1568815078532295015,duration=52782840,event=nonblock_pipe[0Ktravis_time:start:027224ac[0Ktravis_time:end:027224ac:start=1568815078537585640,finish=1568815078576695994,duration=39110354,event=apt_get_update[0Ktravis_time:start:02ae0180[0Ktravis_time:end:02ae0180:start=1568815078581087096,finish=1568815078583908328,duration=2821232,event=deprecate_xcode_64[0Ktravis_time:start:0fa8a42b[0Ktravis_time:end:0fa8a42b:start=1568815078588764920,finish=1568815083164387479,duration=4575622559,event=update_heroku[0Ktravis_time:start:0ee2b3b0[0Ktravis_time:end:0ee2b3b0:start=1568815083168835005,finish=1568815083172026121,duration=3191116,event=shell_session_update[0Ktravis_time:start:00854800[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3873
travis_fold:end:docker_mtu[0Ktravis_time:end:00854800:start=1568815083176161697,finish=1568815084374353512,duration=1198191815,event=set_docker_mtu[0Ktravis_time:start:071b379a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:071b379a:start=1568815084379750546,finish=1568815084441229636,duration=61479090,event=resolvconf[0Ktravis_time:start:26622ff2[0Ktravis_time:end:26622ff2:start=1568815084445801136,finish=1568815084549454856,duration=103653720,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:233a9254[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:233a9254:start=1568815084629736916,finish=1568815084934999967,duration=305263051,event=configure[0Ktravis_time:start:2ca48636[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:2ca48636:start=1568815084939930785,finish=1568815094608902533,duration=9668971748,event=configure[0Ktravis_time:start:11ebfa62[0Ktravis_fold:start:services[0Ktravis_time:start:2904b2a0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:2904b2a0:start=1568815094634164223,finish=1568815094648395719,duration=14231496,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:2904b2a0:start=1568815094634164223,finish=1568815097653124073,duration=3018959850,event=services[0Ktravis_time:start:0d4c9c49[0Ktravis_time:end:0d4c9c49:start=1568815097657711753,finish=1568815097661136382,duration=3424629,event=fix_ps4[0Ktravis_time:start:0277e058[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1b1f490d[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1b1f490d:start=1568815097670267919,finish=1568815107828370333,duration=10158102414,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b989e40888b7bc80b4a7d6d823b98fc3ebb61025
travis_fold:end:git.checkout[0K
travis_time:end:1b1f490d:start=1568815097670267919,finish=1568815108645720454,duration=10975452535,event=checkout[0Ktravis_time:start:0bdd27c4[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0bdd27c4:start=1568815108650381682,finish=1568815108661811323,duration=11429641,event=env[0Ktravis_time:start:16f9f69e[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:16f9f69e:start=1568815108667761674,finish=1568815108673237819,duration=5476145,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0a077bd3[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,fe-fe,bindings,of-ccx_fsi,dealii-of,nutils-of,of-of_np,of-of,of-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0a077bd3:start=1568815109003293089,finish=1568815109067196343,duration=63903254,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:09906987[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510185/log.txt)