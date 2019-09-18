 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510218) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
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
travis_time:end:2a59de5e:start=1568817219594609899,finish=1568817219600530135,duration=5920236,event=show_system_info[0Ktravis_time:start:0a16da9a[0Ktravis_time:end:0a16da9a:start=1568817219603571920,finish=1568817219627268717,duration=23696797,event=rm_riak_source[0Ktravis_time:start:05cddaa5[0Ktravis_time:end:05cddaa5:start=1568817219630456893,finish=1568817219635598798,duration=5141905,event=fix_rwky_redis[0Ktravis_time:start:0d168b42[0Ktravis_time:end:0d168b42:start=1568817219638624581,finish=1568817220058679643,duration=420055062,event=wait_for_network[0Ktravis_time:start:365ac07b[0Ktravis_time:end:365ac07b:start=1568817220063083040,finish=1568817221739373898,duration=1676290858,event=update_apt_keys[0Ktravis_time:start:053754f0[0Ktravis_time:end:053754f0:start=1568817221743400209,finish=1568817222807382793,duration=1063982584,event=fix_hhvm_source[0Ktravis_time:start:06764c45[0Ktravis_time:end:06764c45:start=1568817222811823911,finish=1568817222823106279,duration=11282368,event=update_mongo_arch[0Ktravis_time:start:0ce72b00[0Ktravis_time:end:0ce72b00:start=1568817222827377248,finish=1568817222875498423,duration=48121175,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0333ff60[0Ktravis_time:end:0333ff60:start=1568817222880903167,finish=1568817222883926194,duration=3023027,event=update_glibc[0Ktravis_time:start:0fc39c00[0Ktravis_time:end:0fc39c00:start=1568817222888008627,finish=1568817222900184431,duration=12175804,event=clean_up_path[0Ktravis_time:start:13eadcac[0Ktravis_time:end:13eadcac:start=1568817222904516829,finish=1568817222913576215,duration=9059386,event=fix_resolv_conf[0Ktravis_time:start:19e1b647[0Ktravis_time:end:19e1b647:start=1568817222918613706,finish=1568817222929026658,duration=10412952,event=fix_etc_hosts[0Ktravis_time:start:00376833[0Ktravis_time:end:00376833:start=1568817222934264662,finish=1568817222944114623,duration=9849961,event=fix_mvn_settings_xml[0Ktravis_time:start:024830d6[0Ktravis_time:end:024830d6:start=1568817222948694586,finish=1568817222959339049,duration=10644463,event=no_ipv6_localhost[0Ktravis_time:start:0aab1078[0Ktravis_time:end:0aab1078:start=1568817222964823650,finish=1568817222967571778,duration=2748128,event=fix_etc_mavenrc[0Ktravis_time:start:0cccc21b[0Ktravis_time:end:0cccc21b:start=1568817222971655155,finish=1568817222975368527,duration=3713372,event=fix_wwdr_certificate[0Ktravis_time:start:067eca94[0Ktravis_time:end:067eca94:start=1568817222979452229,finish=1568817223004600069,duration=25147840,event=put_localhost_first[0Ktravis_time:start:1159effe[0Ktravis_time:end:1159effe:start=1568817223008738767,finish=1568817223012245657,duration=3506890,event=home_paths[0Ktravis_time:start:0c7ae035[0Ktravis_time:end:0c7ae035:start=1568817223017774288,finish=1568817223031088670,duration=13314382,event=disable_initramfs[0Ktravis_time:start:023762ee[0Ktravis_time:end:023762ee:start=1568817223036473396,finish=1568817223361774148,duration=325300752,event=disable_ssh_roaming[0Ktravis_time:start:04a88b66[0Ktravis_time:end:04a88b66:start=1568817223366976046,finish=1568817223371050067,duration=4074021,event=debug_tools[0Ktravis_time:start:336df432[0Ktravis_time:end:336df432:start=1568817223376601454,finish=1568817223380645937,duration=4044483,event=uninstall_oclint[0Ktravis_time:start:01b73f54[0Ktravis_time:end:01b73f54:start=1568817223389204815,finish=1568817223392940527,duration=3735712,event=rvm_use[0Ktravis_time:start:18dbd2a8[0Ktravis_time:end:18dbd2a8:start=1568817223398089837,finish=1568817223406914781,duration=8824944,event=rm_etc_boto_cfg[0Ktravis_time:start:0e15bc7f[0Ktravis_time:end:0e15bc7f:start=1568817223412424602,finish=1568817223415764189,duration=3339587,event=rm_oraclejdk8_symlink[0Ktravis_time:start:05ee70d7[0Ktravis_time:end:05ee70d7:start=1568817223421143494,finish=1568817223478071191,duration=56927697,event=enable_i386[0Ktravis_time:start:1062251b[0Ktravis_time:end:1062251b:start=1568817223483106416,finish=1568817223487487247,duration=4380831,event=update_rubygems[0Ktravis_time:start:0f057ba9[0Ktravis_time:end:0f057ba9:start=1568817223491708460,finish=1568817224515633202,duration=1023924742,event=ensure_path_components[0Ktravis_time:start:03a779a4[0Ktravis_time:end:03a779a4:start=1568817224520287419,finish=1568817224523191729,duration=2904310,event=redefine_curl[0Ktravis_time:start:2f9c1410[0Ktravis_time:end:2f9c1410:start=1568817224528697762,finish=1568817224583599826,duration=54902064,event=nonblock_pipe[0Ktravis_time:start:30f855bb[0Ktravis_time:end:30f855bb:start=1568817224587991481,finish=1568817224629013173,duration=41021692,event=apt_get_update[0Ktravis_time:start:053fcb59[0Ktravis_time:end:053fcb59:start=1568817224632848436,finish=1568817224635760452,duration=2912016,event=deprecate_xcode_64[0Ktravis_time:start:0dea0a01[0Ktravis_time:end:0dea0a01:start=1568817224639528528,finish=1568817229303349335,duration=4663820807,event=update_heroku[0Ktravis_time:start:037935b4[0Ktravis_time:end:037935b4:start=1568817229308073103,finish=1568817229311024270,duration=2951167,event=shell_session_update[0Ktravis_time:start:17f5be45[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3878
travis_fold:end:docker_mtu[0Ktravis_time:end:17f5be45:start=1568817229315316665,finish=1568817230512885255,duration=1197568590,event=set_docker_mtu[0Ktravis_time:start:125ff8ba[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:125ff8ba:start=1568817230517971468,finish=1568817230585172833,duration=67201365,event=resolvconf[0Ktravis_time:start:2b9a2d64[0Ktravis_time:end:2b9a2d64:start=1568817230590293762,finish=1568817230703882218,duration=113588456,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:028b38b6[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:028b38b6:start=1568817230786811725,finish=1568817231186926716,duration=400114991,event=configure[0Ktravis_time:start:13500f10[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:13500f10:start=1568817231192099279,finish=1568817240931285978,duration=9739186699,event=configure[0Ktravis_time:start:001fa2ac[0Ktravis_fold:start:services[0Ktravis_time:start:0012dc80[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0012dc80:start=1568817240957189422,finish=1568817240972205022,duration=15015600,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0012dc80:start=1568817240957189422,finish=1568817243977982812,duration=3020793390,event=services[0Ktravis_time:start:02bcd56b[0Ktravis_time:end:02bcd56b:start=1568817243982270717,finish=1568817243984881107,duration=2610390,event=fix_ps4[0Ktravis_time:start:05fd8789[0K
travis_fold:start:git.checkout[0Ktravis_time:start:008da7aa[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:008da7aa:start=1568817243993402467,finish=1568817254346227608,duration=10352825141,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:008d7554[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:008d7554:start=1568817254352360274,finish=1568817254793547782,duration=441187508,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:008d7554:start=1568817254352360274,finish=1568817255088833167,duration=736472893,event=checkout[0Ktravis_time:start:0310312a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0310312a:start=1568817255093940297,finish=1568817255106725497,duration=12785200,event=env[0Ktravis_time:start:0c60e700[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0c60e700:start=1568817255112313503,finish=1568817255121378669,duration=9065166,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0a8f31bc[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,of-ccx,fe-fe,su2-ccx,dealii-of,of-of,nutils-of,of-of_np,bindings}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0a8f31bc:start=1568817255490854368,finish=1568817255559753290,duration=68898922,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:07b52790[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510233/log.txt)