 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478260) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3c3e92795247...4d912263806c) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
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
travis_time:end:13d3e94d:start=1568808337447494904,finish=1568808337453895033,duration=6400129,event=show_system_info[0Ktravis_time:start:07e8a3a0[0Ktravis_time:end:07e8a3a0:start=1568808337457107954,finish=1568808337484939891,duration=27831937,event=rm_riak_source[0Ktravis_time:start:18b05af4[0Ktravis_time:end:18b05af4:start=1568808337488549737,finish=1568808337494315278,duration=5765541,event=fix_rwky_redis[0Ktravis_time:start:106be3aa[0Ktravis_time:end:106be3aa:start=1568808337497666770,finish=1568808337963184312,duration=465517542,event=wait_for_network[0Ktravis_time:start:028b99b0[0Ktravis_time:end:028b99b0:start=1568808337968277794,finish=1568808339180565806,duration=1212288012,event=update_apt_keys[0Ktravis_time:start:003ac2e4[0Ktravis_time:end:003ac2e4:start=1568808339186122426,finish=1568808340293726758,duration=1107604332,event=fix_hhvm_source[0Ktravis_time:start:1fbf70c2[0Ktravis_time:end:1fbf70c2:start=1568808340300238888,finish=1568808340313054458,duration=12815570,event=update_mongo_arch[0Ktravis_time:start:031bd953[0Ktravis_time:end:031bd953:start=1568808340318067439,finish=1568808340365491499,duration=47424060,event=fix_sudo_enabled_trusty[0Ktravis_time:start:098387eb[0Ktravis_time:end:098387eb:start=1568808340370629152,finish=1568808340374157810,duration=3528658,event=update_glibc[0Ktravis_time:start:12badcbf[0Ktravis_time:end:12badcbf:start=1568808340379206252,finish=1568808340389501612,duration=10295360,event=clean_up_path[0Ktravis_time:start:0738cc26[0Ktravis_time:end:0738cc26:start=1568808340393953365,finish=1568808340404011114,duration=10057749,event=fix_resolv_conf[0Ktravis_time:start:018aad4e[0Ktravis_time:end:018aad4e:start=1568808340408536124,finish=1568808340419321662,duration=10785538,event=fix_etc_hosts[0Ktravis_time:start:0010240e[0Ktravis_time:end:0010240e:start=1568808340424020971,finish=1568808340435101432,duration=11080461,event=fix_mvn_settings_xml[0Ktravis_time:start:362108d3[0Ktravis_time:end:362108d3:start=1568808340442401224,finish=1568808340455507470,duration=13106246,event=no_ipv6_localhost[0Ktravis_time:start:13b4820a[0Ktravis_time:end:13b4820a:start=1568808340460232731,finish=1568808340464807185,duration=4574454,event=fix_etc_mavenrc[0Ktravis_time:start:03572b0a[0Ktravis_time:end:03572b0a:start=1568808340471801792,finish=1568808340477024530,duration=5222738,event=fix_wwdr_certificate[0Ktravis_time:start:268646f3[0Ktravis_time:end:268646f3:start=1568808340482223099,finish=1568808340515059852,duration=32836753,event=put_localhost_first[0Ktravis_time:start:0091e930[0Ktravis_time:end:0091e930:start=1568808340520826664,finish=1568808340526109786,duration=5283122,event=home_paths[0Ktravis_time:start:0eb2d680[0Ktravis_time:end:0eb2d680:start=1568808340531611509,finish=1568808340545413778,duration=13802269,event=disable_initramfs[0Ktravis_time:start:0f237b91[0Ktravis_time:end:0f237b91:start=1568808340551641056,finish=1568808340915491059,duration=363850003,event=disable_ssh_roaming[0Ktravis_time:start:036258c0[0Ktravis_time:end:036258c0:start=1568808340922155882,finish=1568808340925852441,duration=3696559,event=debug_tools[0Ktravis_time:start:002b8054[0Ktravis_time:end:002b8054:start=1568808340931741570,finish=1568808340936720109,duration=4978539,event=uninstall_oclint[0Ktravis_time:start:15ab4f26[0Ktravis_time:end:15ab4f26:start=1568808340942823296,finish=1568808340947117683,duration=4294387,event=rvm_use[0Ktravis_time:start:09150ac7[0Ktravis_time:end:09150ac7:start=1568808340951686330,finish=1568808340964344313,duration=12657983,event=rm_etc_boto_cfg[0Ktravis_time:start:1500c65d[0Ktravis_time:end:1500c65d:start=1568808340969531576,finish=1568808340972848195,duration=3316619,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2908a73c[0Ktravis_time:end:2908a73c:start=1568808340977575019,finish=1568808341053489041,duration=75914022,event=enable_i386[0Ktravis_time:start:1535e34a[0Ktravis_time:end:1535e34a:start=1568808341058849776,finish=1568808341064240543,duration=5390767,event=update_rubygems[0Ktravis_time:start:1b70871a[0Ktravis_time:end:1b70871a:start=1568808341069674128,finish=1568808342246483101,duration=1176808973,event=ensure_path_components[0Ktravis_time:start:221651ba[0Ktravis_time:end:221651ba:start=1568808342253154113,finish=1568808342256681466,duration=3527353,event=redefine_curl[0Ktravis_time:start:0d79357a[0Ktravis_time:end:0d79357a:start=1568808342262844625,finish=1568808342323966842,duration=61122217,event=nonblock_pipe[0Ktravis_time:start:001afb12[0Ktravis_time:end:001afb12:start=1568808342329607004,finish=1568808342379499339,duration=49892335,event=apt_get_update[0Ktravis_time:start:0ea4c0d9[0Ktravis_time:end:0ea4c0d9:start=1568808342384544999,finish=1568808342387485864,duration=2940865,event=deprecate_xcode_64[0Ktravis_time:start:19e5171d[0Ktravis_time:end:19e5171d:start=1568808342391963848,finish=1568808347544305713,duration=5152341865,event=update_heroku[0Ktravis_time:start:0b7e3708[0Ktravis_time:end:0b7e3708:start=1568808347550838123,finish=1568808347558226491,duration=7388368,event=shell_session_update[0Ktravis_time:start:12489090[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3834
travis_fold:end:docker_mtu[0Ktravis_time:end:12489090:start=1568808347566667488,finish=1568808348776086077,duration=1209418589,event=set_docker_mtu[0Ktravis_time:start:2d29638a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:2d29638a:start=1568808348781451513,finish=1568808348855168413,duration=73716900,event=resolvconf[0Ktravis_time:start:064404e0[0Ktravis_time:end:064404e0:start=1568808348860380233,finish=1568808348978222468,duration=117842235,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0249ac8c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0249ac8c:start=1568808349071701131,finish=1568808349556708363,duration=485007232,event=configure[0Ktravis_time:start:18d3852c[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:18d3852c:start=1568808349563867222,finish=1568808362781793784,duration=13217926562,event=configure[0Ktravis_time:start:1d952a89[0Ktravis_fold:start:services[0Ktravis_time:start:020dfb5e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:020dfb5e:start=1568808362809603702,finish=1568808362825481446,duration=15877744,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:020dfb5e:start=1568808362809603702,finish=1568808365831942678,duration=3022338976,event=services[0Ktravis_time:start:2d6c3462[0Ktravis_time:end:2d6c3462:start=1568808365838098417,finish=1568808365842285133,duration=4186716,event=fix_ps4[0Ktravis_time:start:0d4700f4[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0232df04[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0232df04:start=1568808365853397488,finish=1568808376067620509,duration=10214223021,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4d912263806c85d105a3cfc8dba374f4f3a4853a
travis_fold:end:git.checkout[0K
travis_time:end:0232df04:start=1568808365853397488,finish=1568808376132094411,duration=10278696923,event=checkout[0Ktravis_time:start:0300c2e4[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0300c2e4:start=1568808376137493011,finish=1568808376149001728,duration=11508717,event=env[0Ktravis_time:start:1c0f405c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1c0f405c:start=1568808376154495430,finish=1568808376160986745,duration=6491315,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:229d271b[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,of-ccx,of-of,nutils-of,of-ccx_fsi,bindings,fe-fe,of-of_np,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:229d271b:start=1568808376577756679,finish=1568808376647903787,duration=70147108,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:18621935[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478277/log.txt)