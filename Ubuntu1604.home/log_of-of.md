 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478286) 
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
travis_time:end:0fe21b2c:start=1568810229654305654,finish=1568810229661249946,duration=6944292,event=show_system_info[0Ktravis_time:start:0c7696c4[0Ktravis_time:end:0c7696c4:start=1568810229664175424,finish=1568810229703178145,duration=39002721,event=rm_riak_source[0Ktravis_time:start:047897da[0Ktravis_time:end:047897da:start=1568810229706332683,finish=1568810229711735278,duration=5402595,event=fix_rwky_redis[0Ktravis_time:start:08b9c89f[0Ktravis_time:end:08b9c89f:start=1568810229714656944,finish=1568810230150757860,duration=436100916,event=wait_for_network[0Ktravis_time:start:2995f614[0Ktravis_time:end:2995f614:start=1568810230155271600,finish=1568810231794975499,duration=1639703899,event=update_apt_keys[0Ktravis_time:start:1d600d70[0Ktravis_time:end:1d600d70:start=1568810231800560758,finish=1568810232899766045,duration=1099205287,event=fix_hhvm_source[0Ktravis_time:start:28cda438[0Ktravis_time:end:28cda438:start=1568810232905305652,finish=1568810232917099930,duration=11794278,event=update_mongo_arch[0Ktravis_time:start:1a3a5754[0Ktravis_time:end:1a3a5754:start=1568810232925073363,finish=1568810232970907753,duration=45834390,event=fix_sudo_enabled_trusty[0Ktravis_time:start:31678110[0Ktravis_time:end:31678110:start=1568810232976256790,finish=1568810232980288285,duration=4031495,event=update_glibc[0Ktravis_time:start:00935e72[0Ktravis_time:end:00935e72:start=1568810232984749020,finish=1568810232995856811,duration=11107791,event=clean_up_path[0Ktravis_time:start:320c26e5[0Ktravis_time:end:320c26e5:start=1568810233001126094,finish=1568810233011104231,duration=9978137,event=fix_resolv_conf[0Ktravis_time:start:02b181ac[0Ktravis_time:end:02b181ac:start=1568810233018321802,finish=1568810233028928616,duration=10606814,event=fix_etc_hosts[0Ktravis_time:start:09dbab0f[0Ktravis_time:end:09dbab0f:start=1568810233034174414,finish=1568810233044024053,duration=9849639,event=fix_mvn_settings_xml[0Ktravis_time:start:18aba52d[0Ktravis_time:end:18aba52d:start=1568810233049012852,finish=1568810233060285863,duration=11273011,event=no_ipv6_localhost[0Ktravis_time:start:130c75b6[0Ktravis_time:end:130c75b6:start=1568810233067270845,finish=1568810233071180087,duration=3909242,event=fix_etc_mavenrc[0Ktravis_time:start:35fc3e60[0Ktravis_time:end:35fc3e60:start=1568810233077408691,finish=1568810233083673458,duration=6264767,event=fix_wwdr_certificate[0Ktravis_time:start:03d1be00[0Ktravis_time:end:03d1be00:start=1568810233087812213,finish=1568810233121585238,duration=33773025,event=put_localhost_first[0Ktravis_time:start:0c29185e[0Ktravis_time:end:0c29185e:start=1568810233126107449,finish=1568810233129978439,duration=3870990,event=home_paths[0Ktravis_time:start:1235e7ec[0Ktravis_time:end:1235e7ec:start=1568810233135211731,finish=1568810233152011326,duration=16799595,event=disable_initramfs[0Ktravis_time:start:07776b90[0Ktravis_time:end:07776b90:start=1568810233156659999,finish=1568810233608100855,duration=451440856,event=disable_ssh_roaming[0Ktravis_time:start:05a165c0[0Ktravis_time:end:05a165c0:start=1568810233613602821,finish=1568810233617499268,duration=3896447,event=debug_tools[0Ktravis_time:start:1badf1dd[0Ktravis_time:end:1badf1dd:start=1568810233622873152,finish=1568810233630660790,duration=7787638,event=uninstall_oclint[0Ktravis_time:start:02fed381[0Ktravis_time:end:02fed381:start=1568810233635945189,finish=1568810233641338498,duration=5393309,event=rvm_use[0Ktravis_time:start:1690b120[0Ktravis_time:end:1690b120:start=1568810233646736868,finish=1568810233658936976,duration=12200108,event=rm_etc_boto_cfg[0Ktravis_time:start:075d87b0[0Ktravis_time:end:075d87b0:start=1568810233664097075,finish=1568810233669111364,duration=5014289,event=rm_oraclejdk8_symlink[0Ktravis_time:start:12689970[0Ktravis_time:end:12689970:start=1568810233673055623,finish=1568810233745186417,duration=72130794,event=enable_i386[0Ktravis_time:start:040a1ea0[0Ktravis_time:end:040a1ea0:start=1568810233750243405,finish=1568810233755470829,duration=5227424,event=update_rubygems[0Ktravis_time:start:2142b5e1[0Ktravis_time:end:2142b5e1:start=1568810233761689266,finish=1568810234816545365,duration=1054856099,event=ensure_path_components[0Ktravis_time:start:177c3e10[0Ktravis_time:end:177c3e10:start=1568810234821641591,finish=1568810234824436617,duration=2795026,event=redefine_curl[0Ktravis_time:start:1309ee51[0Ktravis_time:end:1309ee51:start=1568810234829754144,finish=1568810234886935405,duration=57181261,event=nonblock_pipe[0Ktravis_time:start:33afd364[0Ktravis_time:end:33afd364:start=1568810234892219986,finish=1568810234992927739,duration=100707753,event=apt_get_update[0Ktravis_time:start:007512ef[0Ktravis_time:end:007512ef:start=1568810234996869067,finish=1568810234999850397,duration=2981330,event=deprecate_xcode_64[0Ktravis_time:start:0b55f720[0Ktravis_time:end:0b55f720:start=1568810235004020441,finish=1568810240587752598,duration=5583732157,event=update_heroku[0Ktravis_time:start:24f523bc[0Ktravis_time:end:24f523bc:start=1568810240592006296,finish=1568810240595162658,duration=3156362,event=shell_session_update[0Ktravis_time:start:047250a2[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3859
travis_fold:end:docker_mtu[0Ktravis_time:end:047250a2:start=1568810240599429140,finish=1568810241797399295,duration=1197970155,event=set_docker_mtu[0Ktravis_time:start:1ccf5e6a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1ccf5e6a:start=1568810241802864374,finish=1568810241877556726,duration=74692352,event=resolvconf[0Ktravis_time:start:013dd864[0Ktravis_time:end:013dd864:start=1568810241882556903,finish=1568810241996363907,duration=113807004,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:026737da[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:026737da:start=1568810242085008807,finish=1568810242440254389,duration=355245582,event=configure[0Ktravis_time:start:1cd98c0b[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1cd98c0b:start=1568810242446520627,finish=1568810253230981786,duration=10784461159,event=configure[0Ktravis_time:start:05e523ae[0Ktravis_fold:start:services[0Ktravis_time:start:0074bc38[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0074bc38:start=1568810253260041682,finish=1568810253276309223,duration=16267541,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0074bc38:start=1568810253260041682,finish=1568810256282455908,duration=3022414226,event=services[0Ktravis_time:start:2403cc8b[0Ktravis_time:end:2403cc8b:start=1568810256287932780,finish=1568810256291404582,duration=3471802,event=fix_ps4[0Ktravis_time:start:034b003f[0K
travis_fold:start:git.checkout[0Ktravis_time:start:026d3252[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:026d3252:start=1568810256300379680,finish=1568810266703615725,duration=10403236045,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0796db20[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:0796db20:start=1568810266708341129,finish=1568810267128586962,duration=420245833,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0796db20:start=1568810266708341129,finish=1568810267790232185,duration=1081891056,event=checkout[0Ktravis_time:start:02348946[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:02348946:start=1568810267795511760,finish=1568810267807649740,duration=12137980,event=env[0Ktravis_time:start:001de5de[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:001de5de:start=1568810267816727893,finish=1568810267824594143,duration=7866250,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:15289c74[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-ccx,bindings,dealii-of,of-of_np,su2-ccx,nutils-of,of-of,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:15289c74:start=1568810268198711810,finish=1568810268270635221,duration=71923411,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:10f37b44[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478300/log.txt)