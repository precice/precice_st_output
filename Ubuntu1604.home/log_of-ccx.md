 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586518622) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/98) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72) 
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
travis_time:end:0b6468b8:start=1568824426121955288,finish=1568824426128512476,duration=6557188,event=show_system_info[0Ktravis_time:start:00ec9c2e[0Ktravis_time:end:00ec9c2e:start=1568824426131624163,finish=1568824426160087448,duration=28463285,event=rm_riak_source[0Ktravis_time:start:00fd6c08[0Ktravis_time:end:00fd6c08:start=1568824426163718526,finish=1568824426169416723,duration=5698197,event=fix_rwky_redis[0Ktravis_time:start:1b5c4b3a[0Ktravis_time:end:1b5c4b3a:start=1568824426172593349,finish=1568824429725304980,duration=3552711631,event=wait_for_network[0Ktravis_time:start:0161d963[0Ktravis_time:end:0161d963:start=1568824429728830936,finish=1568824431417675372,duration=1688844436,event=update_apt_keys[0Ktravis_time:start:072b23fb[0Ktravis_time:end:072b23fb:start=1568824431421150831,finish=1568824437500851276,duration=6079700445,event=fix_hhvm_source[0Ktravis_time:start:10bdcf58[0Ktravis_time:end:10bdcf58:start=1568824437505702881,finish=1568824437517306661,duration=11603780,event=update_mongo_arch[0Ktravis_time:start:0608f9d0[0Ktravis_time:end:0608f9d0:start=1568824437521059221,finish=1568824437581229465,duration=60170244,event=fix_sudo_enabled_trusty[0Ktravis_time:start:14d57a3b[0Ktravis_time:end:14d57a3b:start=1568824437585801635,finish=1568824437589120389,duration=3318754,event=update_glibc[0Ktravis_time:start:02485256[0Ktravis_time:end:02485256:start=1568824437593303740,finish=1568824437605918623,duration=12614883,event=clean_up_path[0Ktravis_time:start:029172ca[0Ktravis_time:end:029172ca:start=1568824437610432285,finish=1568824437622183206,duration=11750921,event=fix_resolv_conf[0Ktravis_time:start:08b4184c[0Ktravis_time:end:08b4184c:start=1568824437626080718,finish=1568824437640545201,duration=14464483,event=fix_etc_hosts[0Ktravis_time:start:00101548[0Ktravis_time:end:00101548:start=1568824437644909092,finish=1568824437703171261,duration=58262169,event=fix_mvn_settings_xml[0Ktravis_time:start:08b012a5[0Ktravis_time:end:08b012a5:start=1568824437727116699,finish=1568824437804812191,duration=77695492,event=no_ipv6_localhost[0Ktravis_time:start:26598de6[0Ktravis_time:end:26598de6:start=1568824437809325205,finish=1568824437811935158,duration=2609953,event=fix_etc_mavenrc[0Ktravis_time:start:1116b3c0[0Ktravis_time:end:1116b3c0:start=1568824437815682409,finish=1568824437819065388,duration=3382979,event=fix_wwdr_certificate[0Ktravis_time:start:04af9370[0Ktravis_time:end:04af9370:start=1568824437823831614,finish=1568824437849738536,duration=25906922,event=put_localhost_first[0Ktravis_time:start:27201cc0[0Ktravis_time:end:27201cc0:start=1568824437854262999,finish=1568824437857807326,duration=3544327,event=home_paths[0Ktravis_time:start:10ea1c54[0Ktravis_time:end:10ea1c54:start=1568824437862503775,finish=1568824437875029450,duration=12525675,event=disable_initramfs[0Ktravis_time:start:05fb8a84[0Ktravis_time:end:05fb8a84:start=1568824437879550119,finish=1568824438122776757,duration=243226638,event=disable_ssh_roaming[0Ktravis_time:start:220d321c[0Ktravis_time:end:220d321c:start=1568824438127304571,finish=1568824438130797333,duration=3492762,event=debug_tools[0Ktravis_time:start:009e1ec0[0Ktravis_time:end:009e1ec0:start=1568824438137171656,finish=1568824438141377604,duration=4205948,event=uninstall_oclint[0Ktravis_time:start:12b1ea60[0Ktravis_time:end:12b1ea60:start=1568824438147698554,finish=1568824438151548053,duration=3849499,event=rvm_use[0Ktravis_time:start:0f3f401e[0Ktravis_time:end:0f3f401e:start=1568824438157315495,finish=1568824438167723069,duration=10407574,event=rm_etc_boto_cfg[0Ktravis_time:start:0e222e98[0Ktravis_time:end:0e222e98:start=1568824438175681400,finish=1568824438178725168,duration=3043768,event=rm_oraclejdk8_symlink[0Ktravis_time:start:075261f9[0Ktravis_time:end:075261f9:start=1568824438183898031,finish=1568824438240343415,duration=56445384,event=enable_i386[0Ktravis_time:start:087845da[0Ktravis_time:end:087845da:start=1568824438245420580,finish=1568824438250618014,duration=5197434,event=update_rubygems[0Ktravis_time:start:00733b1e[0Ktravis_time:end:00733b1e:start=1568824438255800593,finish=1568824439286323273,duration=1030522680,event=ensure_path_components[0Ktravis_time:start:241287d2[0Ktravis_time:end:241287d2:start=1568824439293151776,finish=1568824439296781399,duration=3629623,event=redefine_curl[0Ktravis_time:start:03dcd36a[0Ktravis_time:end:03dcd36a:start=1568824439301726463,finish=1568824439361025393,duration=59298930,event=nonblock_pipe[0Ktravis_time:start:15f3045c[0Ktravis_time:end:15f3045c:start=1568824439367226800,finish=1568824439408870663,duration=41643863,event=apt_get_update[0Ktravis_time:start:0002b0e0[0Ktravis_time:end:0002b0e0:start=1568824439413576034,finish=1568824439416522911,duration=2946877,event=deprecate_xcode_64[0Ktravis_time:start:0496da9e[0Ktravis_time:end:0496da9e:start=1568824439422334316,finish=1568824444036639821,duration=4614305505,event=update_heroku[0Ktravis_time:start:016303c8[0Ktravis_time:end:016303c8:start=1568824444041225410,finish=1568824444044302496,duration=3077086,event=shell_session_update[0Ktravis_time:start:004c2bd5[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3882
travis_fold:end:docker_mtu[0Ktravis_time:end:004c2bd5:start=1568824444048677759,finish=1568824445240340998,duration=1191663239,event=set_docker_mtu[0Ktravis_time:start:2b2b1018[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2b2b1018:start=1568824445245176399,finish=1568824445313444410,duration=68268011,event=resolvconf[0Ktravis_time:start:1ec4ea30[0Ktravis_time:end:1ec4ea30:start=1568824445318650390,finish=1568824445422064043,duration=103413653,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:08d019b4[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:08d019b4:start=1568824445513668863,finish=1568824446842957549,duration=1329288686,event=configure[0Ktravis_time:start:11b3ee44[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:11b3ee44:start=1568824446849266161,finish=1568824457046384658,duration=10197118497,event=configure[0Ktravis_time:start:2621c703[0Ktravis_fold:start:services[0Ktravis_time:start:03ea5e44[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:03ea5e44:start=1568824457071036898,finish=1568824457085914641,duration=14877743,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03ea5e44:start=1568824457071036898,finish=1568824460092064821,duration=3021027923,event=services[0Ktravis_time:start:0d301be0[0Ktravis_time:end:0d301be0:start=1568824460096495318,finish=1568824460099199428,duration=2704110,event=fix_ps4[0Ktravis_time:start:22da72c0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1881869d[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1881869d:start=1568824460107973646,finish=1568824470130337710,duration=10022364064,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0557d38a[0K$ git fetch origin +refs/pull/98/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/98/merge -> FETCH_HEAD
travis_time:end:0557d38a:start=1568824470135119798,finish=1568824470567601617,duration=432481819,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0557d38a:start=1568824470135119798,finish=1568824470681749665,duration=546629867,event=checkout[0Ktravis_time:start:104cf430[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:104cf430:start=1568824470686456672,finish=1568824470698207374,duration=11750702,event=env[0Ktravis_time:start:15a91cd6[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:15a91cd6:start=1568824470703478083,finish=1568824470709634235,duration=6156152,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09e7b760[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {bindings,of-of,su2-ccx,nutils-of,of-of_np,dealii-of,fe-fe,of-ccx,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:09e7b760:start=1568824471058680480,finish=1568824471124128806,duration=65448326,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:116dc418[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586518637/log.txt)