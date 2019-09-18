 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478286) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf) 
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
travis_time:end:060f9700:start=1568810345894525765,finish=1568810345900411815,duration=5886050,event=show_system_info[0Ktravis_time:start:1d10a340[0Ktravis_time:end:1d10a340:start=1568810345903276247,finish=1568810345937180987,duration=33904740,event=rm_riak_source[0Ktravis_time:start:1cfa339d[0Ktravis_time:end:1cfa339d:start=1568810345940265407,finish=1568810345945330701,duration=5065294,event=fix_rwky_redis[0Ktravis_time:start:0d22a014[0Ktravis_time:end:0d22a014:start=1568810345948151544,finish=1568810346365480087,duration=417328543,event=wait_for_network[0Ktravis_time:start:1af93dde[0Ktravis_time:end:1af93dde:start=1568810346385127294,finish=1568810349027740854,duration=2642613560,event=update_apt_keys[0Ktravis_time:start:06891546[0Ktravis_time:end:06891546:start=1568810349032748447,finish=1568810350114840073,duration=1082091626,event=fix_hhvm_source[0Ktravis_time:start:01bc2b6e[0Ktravis_time:end:01bc2b6e:start=1568810350119652212,finish=1568810350130194525,duration=10542313,event=update_mongo_arch[0Ktravis_time:start:083cf08e[0Ktravis_time:end:083cf08e:start=1568810350136263365,finish=1568810350182250697,duration=45987332,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2080672a[0Ktravis_time:end:2080672a:start=1568810350187671997,finish=1568810350190656755,duration=2984758,event=update_glibc[0Ktravis_time:start:09bca9a8[0Ktravis_time:end:09bca9a8:start=1568810350196307993,finish=1568810350208748068,duration=12440075,event=clean_up_path[0Ktravis_time:start:0a6bc32c[0Ktravis_time:end:0a6bc32c:start=1568810350214416633,finish=1568810350228375084,duration=13958451,event=fix_resolv_conf[0Ktravis_time:start:1db6f434[0Ktravis_time:end:1db6f434:start=1568810350234096998,finish=1568810350245047570,duration=10950572,event=fix_etc_hosts[0Ktravis_time:start:09a324d9[0Ktravis_time:end:09a324d9:start=1568810350251671301,finish=1568810350262988078,duration=11316777,event=fix_mvn_settings_xml[0Ktravis_time:start:056e6f88[0Ktravis_time:end:056e6f88:start=1568810350270150846,finish=1568810350282094423,duration=11943577,event=no_ipv6_localhost[0Ktravis_time:start:103eca50[0Ktravis_time:end:103eca50:start=1568810350287830441,finish=1568810350291598124,duration=3767683,event=fix_etc_mavenrc[0Ktravis_time:start:0628a590[0Ktravis_time:end:0628a590:start=1568810350297217998,finish=1568810350303102142,duration=5884144,event=fix_wwdr_certificate[0Ktravis_time:start:0ab4f638[0Ktravis_time:end:0ab4f638:start=1568810350308366495,finish=1568810350338818255,duration=30451760,event=put_localhost_first[0Ktravis_time:start:009a14ba[0Ktravis_time:end:009a14ba:start=1568810350343632213,finish=1568810350348014712,duration=4382499,event=home_paths[0Ktravis_time:start:09774bb8[0Ktravis_time:end:09774bb8:start=1568810350352916821,finish=1568810350369704771,duration=16787950,event=disable_initramfs[0Ktravis_time:start:211f18bf[0Ktravis_time:end:211f18bf:start=1568810350374250677,finish=1568810350806349013,duration=432098336,event=disable_ssh_roaming[0Ktravis_time:start:05267ee0[0Ktravis_time:end:05267ee0:start=1568810350810865355,finish=1568810350814196779,duration=3331424,event=debug_tools[0Ktravis_time:start:0242fad9[0Ktravis_time:end:0242fad9:start=1568810350819047603,finish=1568810350823696354,duration=4648751,event=uninstall_oclint[0Ktravis_time:start:0e6dc234[0Ktravis_time:end:0e6dc234:start=1568810350828203223,finish=1568810350833052783,duration=4849560,event=rvm_use[0Ktravis_time:start:02e1f7ac[0Ktravis_time:end:02e1f7ac:start=1568810350837667180,finish=1568810350848300288,duration=10633108,event=rm_etc_boto_cfg[0Ktravis_time:start:1621bd26[0Ktravis_time:end:1621bd26:start=1568810350852990352,finish=1568810350856350324,duration=3359972,event=rm_oraclejdk8_symlink[0Ktravis_time:start:002ab03e[0Ktravis_time:end:002ab03e:start=1568810350865855092,finish=1568810350924825122,duration=58970030,event=enable_i386[0Ktravis_time:start:0ae3a5a1[0Ktravis_time:end:0ae3a5a1:start=1568810350930073902,finish=1568810350935372484,duration=5298582,event=update_rubygems[0Ktravis_time:start:0179e318[0Ktravis_time:end:0179e318:start=1568810350940409077,finish=1568810352010456362,duration=1070047285,event=ensure_path_components[0Ktravis_time:start:05afef30[0Ktravis_time:end:05afef30:start=1568810352015683082,finish=1568810352018809654,duration=3126572,event=redefine_curl[0Ktravis_time:start:07e02826[0Ktravis_time:end:07e02826:start=1568810352026145739,finish=1568810352083441706,duration=57295967,event=nonblock_pipe[0Ktravis_time:start:14c1b1d8[0Ktravis_time:end:14c1b1d8:start=1568810352088008603,finish=1568810352134738887,duration=46730284,event=apt_get_update[0Ktravis_time:start:17b31316[0Ktravis_time:end:17b31316:start=1568810352140551598,finish=1568810352143680288,duration=3128690,event=deprecate_xcode_64[0Ktravis_time:start:159bccc6[0Ktravis_time:end:159bccc6:start=1568810352148656166,finish=1568810357503257849,duration=5354601683,event=update_heroku[0Ktravis_time:start:2693dd50[0Ktravis_time:end:2693dd50:start=1568810357507606822,finish=1568810357510497682,duration=2890860,event=shell_session_update[0Ktravis_time:start:1f088f9c[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3930
travis_fold:end:docker_mtu[0Ktravis_time:end:1f088f9c:start=1568810357514643295,finish=1568810358715679357,duration=1201036062,event=set_docker_mtu[0Ktravis_time:start:0b1cdf62[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0b1cdf62:start=1568810358721838937,finish=1568810358792646147,duration=70807210,event=resolvconf[0Ktravis_time:start:1039c182[0Ktravis_time:end:1039c182:start=1568810358799947278,finish=1568810358917649595,duration=117702317,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:208d7598[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:208d7598:start=1568810359006558869,finish=1568810359448985181,duration=442426312,event=configure[0Ktravis_time:start:0749e5af[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0749e5af:start=1568810359455112024,finish=1568810369634899465,duration=10179787441,event=configure[0Ktravis_time:start:0236386b[0Ktravis_fold:start:services[0Ktravis_time:start:007cb48c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:007cb48c:start=1568810369662586945,finish=1568810369680676264,duration=18089319,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:007cb48c:start=1568810369662586945,finish=1568810372687737183,duration=3025150238,event=services[0Ktravis_time:start:06835926[0Ktravis_time:end:06835926:start=1568810372693069071,finish=1568810372695799239,duration=2730168,event=fix_ps4[0Ktravis_time:start:11d11d54[0K
travis_fold:start:git.checkout[0Ktravis_time:start:051b90f9[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:051b90f9:start=1568810372705609528,finish=1568810382889428067,duration=10183818539,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:2b561cee[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:2b561cee:start=1568810382893645845,finish=1568810383323296567,duration=429650722,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:2b561cee:start=1568810382893645845,finish=1568810384199024779,duration=1305378934,event=checkout[0Ktravis_time:start:30993f60[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:30993f60:start=1568810384204110872,finish=1568810384216675520,duration=12564648,event=env[0Ktravis_time:start:1040ec74[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1040ec74:start=1568810384222643640,finish=1568810384230081480,duration=7437840,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0d1e8c45[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {nutils-of,bindings,of-of,dealii-of,su2-ccx,fe-fe,of-ccx,of-ccx_fsi,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0d1e8c45:start=1568810384600315012,finish=1568810384670987322,duration=70672310,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:04d0bf78[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478301/log.txt)