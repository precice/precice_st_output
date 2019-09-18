 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586518622) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/98) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1) 
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
travis_time:end:04a286d2:start=1568824711464957618,finish=1568824711470823077,duration=5865459,event=show_system_info[0Ktravis_time:start:132ee98c[0Ktravis_time:end:132ee98c:start=1568824711473716534,finish=1568824711501248233,duration=27531699,event=rm_riak_source[0Ktravis_time:start:275c77c8[0Ktravis_time:end:275c77c8:start=1568824711504220017,finish=1568824711509623879,duration=5403862,event=fix_rwky_redis[0Ktravis_time:start:0e5bd5d6[0Ktravis_time:end:0e5bd5d6:start=1568824711512493251,finish=1568824711896533726,duration=384040475,event=wait_for_network[0Ktravis_time:start:15e87afc[0Ktravis_time:end:15e87afc:start=1568824711907299052,finish=1568824712880930357,duration=973631305,event=update_apt_keys[0Ktravis_time:start:0af29800[0Ktravis_time:end:0af29800:start=1568824712886653270,finish=1568824713976512234,duration=1089858964,event=fix_hhvm_source[0Ktravis_time:start:00c9a91e[0Ktravis_time:end:00c9a91e:start=1568824713981758927,finish=1568824713991997314,duration=10238387,event=update_mongo_arch[0Ktravis_time:start:12be8c86[0Ktravis_time:end:12be8c86:start=1568824713997187151,finish=1568824714041039615,duration=43852464,event=fix_sudo_enabled_trusty[0Ktravis_time:start:20a9c691[0Ktravis_time:end:20a9c691:start=1568824714046493652,finish=1568824714049544503,duration=3050851,event=update_glibc[0Ktravis_time:start:204b98a1[0Ktravis_time:end:204b98a1:start=1568824714055928895,finish=1568824714065101892,duration=9172997,event=clean_up_path[0Ktravis_time:start:0e4d2ca1[0Ktravis_time:end:0e4d2ca1:start=1568824714070212841,finish=1568824714080499622,duration=10286781,event=fix_resolv_conf[0Ktravis_time:start:19557ae0[0Ktravis_time:end:19557ae0:start=1568824714085086518,finish=1568824714097673816,duration=12587298,event=fix_etc_hosts[0Ktravis_time:start:0f4f8ec0[0Ktravis_time:end:0f4f8ec0:start=1568824714103060338,finish=1568824714112633486,duration=9573148,event=fix_mvn_settings_xml[0Ktravis_time:start:057e7d22[0Ktravis_time:end:057e7d22:start=1568824714118317017,finish=1568824714128670673,duration=10353656,event=no_ipv6_localhost[0Ktravis_time:start:15303704[0Ktravis_time:end:15303704:start=1568824714133578959,finish=1568824714136670397,duration=3091438,event=fix_etc_mavenrc[0Ktravis_time:start:2cb7a4d7[0Ktravis_time:end:2cb7a4d7:start=1568824714142923213,finish=1568824714146833231,duration=3910018,event=fix_wwdr_certificate[0Ktravis_time:start:1c6e95ac[0Ktravis_time:end:1c6e95ac:start=1568824714151476553,finish=1568824714183973113,duration=32496560,event=put_localhost_first[0Ktravis_time:start:0826bb16[0Ktravis_time:end:0826bb16:start=1568824714190162385,finish=1568824714194542917,duration=4380532,event=home_paths[0Ktravis_time:start:01c61a8b[0Ktravis_time:end:01c61a8b:start=1568824714198856923,finish=1568824714214830100,duration=15973177,event=disable_initramfs[0Ktravis_time:start:030355dd[0Ktravis_time:end:030355dd:start=1568824714219862983,finish=1568824714599567406,duration=379704423,event=disable_ssh_roaming[0Ktravis_time:start:06b4f1da[0Ktravis_time:end:06b4f1da:start=1568824714604644899,finish=1568824714608010465,duration=3365566,event=debug_tools[0Ktravis_time:start:07c831d4[0Ktravis_time:end:07c831d4:start=1568824714614170563,finish=1568824714617938813,duration=3768250,event=uninstall_oclint[0Ktravis_time:start:040a3710[0Ktravis_time:end:040a3710:start=1568824714623114903,finish=1568824714626777626,duration=3662723,event=rvm_use[0Ktravis_time:start:033e02f8[0Ktravis_time:end:033e02f8:start=1568824714633064415,finish=1568824714642196178,duration=9131763,event=rm_etc_boto_cfg[0Ktravis_time:start:01cd86aa[0Ktravis_time:end:01cd86aa:start=1568824714647442815,finish=1568824714650351384,duration=2908569,event=rm_oraclejdk8_symlink[0Ktravis_time:start:27359d42[0Ktravis_time:end:27359d42:start=1568824714655144554,finish=1568824714716625549,duration=61480995,event=enable_i386[0Ktravis_time:start:0f5c4a26[0Ktravis_time:end:0f5c4a26:start=1568824714721671291,finish=1568824714726176141,duration=4504850,event=update_rubygems[0Ktravis_time:start:03672d11[0Ktravis_time:end:03672d11:start=1568824714731143668,finish=1568824715845739765,duration=1114596097,event=ensure_path_components[0Ktravis_time:start:000263a0[0Ktravis_time:end:000263a0:start=1568824715850916291,finish=1568824715853881210,duration=2964919,event=redefine_curl[0Ktravis_time:start:026fc9fd[0Ktravis_time:end:026fc9fd:start=1568824715859139215,finish=1568824715913595331,duration=54456116,event=nonblock_pipe[0Ktravis_time:start:17fbc40e[0Ktravis_time:end:17fbc40e:start=1568824715918627989,finish=1568824715960027651,duration=41399662,event=apt_get_update[0Ktravis_time:start:0dc13e84[0Ktravis_time:end:0dc13e84:start=1568824715964242739,finish=1568824715968212953,duration=3970214,event=deprecate_xcode_64[0Ktravis_time:start:0351d288[0Ktravis_time:end:0351d288:start=1568824715974211570,finish=1568824721442253606,duration=5468042036,event=update_heroku[0Ktravis_time:start:35d65c10[0Ktravis_time:end:35d65c10:start=1568824721446286319,finish=1568824721449233780,duration=2947461,event=shell_session_update[0Ktravis_time:start:0d39fd66[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3928
travis_fold:end:docker_mtu[0Ktravis_time:end:0d39fd66:start=1568824721453183084,finish=1568824722673201372,duration=1220018288,event=set_docker_mtu[0Ktravis_time:start:16cdbdcd[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:16cdbdcd:start=1568824722677616650,finish=1568824722751064729,duration=73448079,event=resolvconf[0Ktravis_time:start:14ff9a00[0Ktravis_time:end:14ff9a00:start=1568824722755726110,finish=1568824722857074242,duration=101348132,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0b91492a[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0b91492a:start=1568824722943063950,finish=1568824723806387832,duration=863323882,event=configure[0Ktravis_time:start:0e6d13a8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0e6d13a8:start=1568824723810909077,finish=1568824734827345137,duration=11016436060,event=configure[0Ktravis_time:start:2220a8b9[0Ktravis_fold:start:services[0Ktravis_time:start:1b8d9700[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1b8d9700:start=1568824734853947450,finish=1568824734870448756,duration=16501306,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1b8d9700:start=1568824734853947450,finish=1568824737876441729,duration=3022494279,event=services[0Ktravis_time:start:2e9fb120[0Ktravis_time:end:2e9fb120:start=1568824737881861779,finish=1568824737885258093,duration=3396314,event=fix_ps4[0Ktravis_time:start:1477f9d8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1de52a1e[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1de52a1e:start=1568824737895748701,finish=1568824748330120783,duration=10434372082,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:00393f91[0K$ git fetch origin +refs/pull/98/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/98/merge -> FETCH_HEAD
travis_time:end:00393f91:start=1568824748334245452,finish=1568824748780800231,duration=446554779,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:00393f91:start=1568824748334245452,finish=1568824749065523624,duration=731278172,event=checkout[0Ktravis_time:start:0d42c320[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0d42c320:start=1568824749070920658,finish=1568824749089150177,duration=18229519,event=env[0Ktravis_time:start:0a25c523[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0a25c523:start=1568824749094576534,finish=1568824749102839185,duration=8262651,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:393525f4[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {of-of_np,of-ccx,of-ccx_fsi,fe-fe,nutils-of,bindings,of-of,su2-ccx,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:393525f4:start=1568824749471333105,finish=1568824749542672466,duration=71339361,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0ad6bed4[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586518640/log.txt)