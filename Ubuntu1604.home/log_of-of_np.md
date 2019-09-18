 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
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
travis_time:end:02c883d8:start=1568817503988062977,finish=1568817503993788709,duration=5725732,event=show_system_info[0Ktravis_time:start:362f7fec[0Ktravis_time:end:362f7fec:start=1568817503996697446,finish=1568817504021024522,duration=24327076,event=rm_riak_source[0Ktravis_time:start:0cdb682a[0Ktravis_time:end:0cdb682a:start=1568817504024424796,finish=1568817504029844133,duration=5419337,event=fix_rwky_redis[0Ktravis_time:start:00b453f7[0Ktravis_time:end:00b453f7:start=1568817504032894187,finish=1568817507518667897,duration=3485773710,event=wait_for_network[0Ktravis_time:start:23357598[0Ktravis_time:end:23357598:start=1568817507522689670,finish=1568817512083395811,duration=4560706141,event=update_apt_keys[0Ktravis_time:start:12948f60[0Ktravis_time:end:12948f60:start=1568817512089723936,finish=1568817513145495721,duration=1055771785,event=fix_hhvm_source[0Ktravis_time:start:1443043e[0Ktravis_time:end:1443043e:start=1568817513150251814,finish=1568817513161313458,duration=11061644,event=update_mongo_arch[0Ktravis_time:start:1e3bb028[0Ktravis_time:end:1e3bb028:start=1568817513167061807,finish=1568817513210886447,duration=43824640,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0e3298d8[0Ktravis_time:end:0e3298d8:start=1568817513215774919,finish=1568817513218591854,duration=2816935,event=update_glibc[0Ktravis_time:start:0b929554[0Ktravis_time:end:0b929554:start=1568817513223286885,finish=1568817513232592424,duration=9305539,event=clean_up_path[0Ktravis_time:start:113dfa19[0Ktravis_time:end:113dfa19:start=1568817513237788969,finish=1568817513246612766,duration=8823797,event=fix_resolv_conf[0Ktravis_time:start:0d7511ce[0Ktravis_time:end:0d7511ce:start=1568817513252163715,finish=1568817513262592444,duration=10428729,event=fix_etc_hosts[0Ktravis_time:start:0201e9b2[0Ktravis_time:end:0201e9b2:start=1568817513267651220,finish=1568817513278229918,duration=10578698,event=fix_mvn_settings_xml[0Ktravis_time:start:149ff610[0Ktravis_time:end:149ff610:start=1568817513283765787,finish=1568817513295239719,duration=11473932,event=no_ipv6_localhost[0Ktravis_time:start:0411432c[0Ktravis_time:end:0411432c:start=1568817513300613627,finish=1568817513303494507,duration=2880880,event=fix_etc_mavenrc[0Ktravis_time:start:0d1168d8[0Ktravis_time:end:0d1168d8:start=1568817513310449036,finish=1568817513316127401,duration=5678365,event=fix_wwdr_certificate[0Ktravis_time:start:02bbca6c[0Ktravis_time:end:02bbca6c:start=1568817513322971995,finish=1568817513351679794,duration=28707799,event=put_localhost_first[0Ktravis_time:start:20f8d384[0Ktravis_time:end:20f8d384:start=1568817513357026600,finish=1568817513360942034,duration=3915434,event=home_paths[0Ktravis_time:start:1c7cc010[0Ktravis_time:end:1c7cc010:start=1568817513366153301,finish=1568817513380032718,duration=13879417,event=disable_initramfs[0Ktravis_time:start:072f71be[0Ktravis_time:end:072f71be:start=1568817513385418450,finish=1568817513751466805,duration=366048355,event=disable_ssh_roaming[0Ktravis_time:start:0332f994[0Ktravis_time:end:0332f994:start=1568817513756232505,finish=1568817513759765185,duration=3532680,event=debug_tools[0Ktravis_time:start:0e01a8bb[0Ktravis_time:end:0e01a8bb:start=1568817513764404831,finish=1568817513769043057,duration=4638226,event=uninstall_oclint[0Ktravis_time:start:3a0389cc[0Ktravis_time:end:3a0389cc:start=1568817513778107934,finish=1568817513781703595,duration=3595661,event=rvm_use[0Ktravis_time:start:0407feb9[0Ktravis_time:end:0407feb9:start=1568817513786270668,finish=1568817513794787211,duration=8516543,event=rm_etc_boto_cfg[0Ktravis_time:start:2330c563[0Ktravis_time:end:2330c563:start=1568817513800205355,finish=1568817513803023727,duration=2818372,event=rm_oraclejdk8_symlink[0Ktravis_time:start:123a6ee0[0Ktravis_time:end:123a6ee0:start=1568817513808162920,finish=1568817513862187332,duration=54024412,event=enable_i386[0Ktravis_time:start:1aa2cac0[0Ktravis_time:end:1aa2cac0:start=1568817513866906583,finish=1568817513871497874,duration=4591291,event=update_rubygems[0Ktravis_time:start:09194a56[0Ktravis_time:end:09194a56:start=1568817513875898463,finish=1568817514907475077,duration=1031576614,event=ensure_path_components[0Ktravis_time:start:0ef9c3b4[0Ktravis_time:end:0ef9c3b4:start=1568817514913159489,finish=1568817514916342953,duration=3183464,event=redefine_curl[0Ktravis_time:start:170647dc[0Ktravis_time:end:170647dc:start=1568817514921605269,finish=1568817514982403667,duration=60798398,event=nonblock_pipe[0Ktravis_time:start:13d0f046[0Ktravis_time:end:13d0f046:start=1568817514987256406,finish=1568817515085875617,duration=98619211,event=apt_get_update[0Ktravis_time:start:008ddaa6[0Ktravis_time:end:008ddaa6:start=1568817515091436593,finish=1568817515094115239,duration=2678646,event=deprecate_xcode_64[0Ktravis_time:start:01e44695[0Ktravis_time:end:01e44695:start=1568817515098809672,finish=1568817520338058356,duration=5239248684,event=update_heroku[0Ktravis_time:start:0b633496[0Ktravis_time:end:0b633496:start=1568817520343428049,finish=1568817520346214003,duration=2785954,event=shell_session_update[0Ktravis_time:start:07ee2fc4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3946
travis_fold:end:docker_mtu[0Ktravis_time:end:07ee2fc4:start=1568817520350967134,finish=1568817521544109198,duration=1193142064,event=set_docker_mtu[0Ktravis_time:start:0dcda41c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0dcda41c:start=1568817521549806641,finish=1568817521621576364,duration=71769723,event=resolvconf[0Ktravis_time:start:248bd0e8[0Ktravis_time:end:248bd0e8:start=1568817521627545523,finish=1568817521739241892,duration=111696369,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:012ac76b[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:012ac76b:start=1568817521827391930,finish=1568817522170427775,duration=343035845,event=configure[0Ktravis_time:start:0d52f5d2[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d52f5d2:start=1568817522176356208,finish=1568817533668991820,duration=11492635612,event=configure[0Ktravis_time:start:0b004700[0Ktravis_fold:start:services[0Ktravis_time:start:17e34658[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:17e34658:start=1568817533695543387,finish=1568817533710908043,duration=15364656,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:17e34658:start=1568817533695543387,finish=1568817536717842884,duration=3022299497,event=services[0Ktravis_time:start:13d2e7c0[0Ktravis_time:end:13d2e7c0:start=1568817536723429042,finish=1568817536726887594,duration=3458552,event=fix_ps4[0Ktravis_time:start:1d11fe00[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08ee72ff[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08ee72ff:start=1568817536736931463,finish=1568817548011354741,duration=11274423278,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0b2362f1[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:0b2362f1:start=1568817548017121760,finish=1568817548454152217,duration=437030457,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0b2362f1:start=1568817548017121760,finish=1568817548505594100,duration=488472340,event=checkout[0Ktravis_time:start:0993f730[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0993f730:start=1568817548511337297,finish=1568817548523770004,duration=12432707,event=env[0Ktravis_time:start:08f5d16c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:08f5d16c:start=1568817548530502976,finish=1568817548539179820,duration=8676844,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2ac8773b[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,of-of_np,dealii-of,su2-ccx,of-of,nutils-of,fe-fe,of-ccx,bindings}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:2ac8773b:start=1568817548973289457,finish=1568817549049288815,duration=75999358,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0092c398[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510238/log.txt)