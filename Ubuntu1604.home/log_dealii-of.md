## Status: Failure 
Build: [1481](https://travis-ci.org/precice/systemtests/builds/640895674) 

Job: [1481.19](https://travis-ci.org/precice/systemtests/jobs/640895699) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
9.3.20
9.4.15
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
travis_time:end:06e94f99:start=1579803333996758515,finish=1579803334002214117,duration=5455602,event=show_system_info[0Ktravis_time:start:189ef35f[0Ktravis_time:end:189ef35f:start=1579803334005360228,finish=1579803334026546779,duration=21186551,event=rm_riak_source[0Ktravis_time:start:005d3d4a[0Ktravis_time:end:005d3d4a:start=1579803334036135262,finish=1579803334042617305,duration=6482043,event=fix_rwky_redis[0Ktravis_time:start:0594a8f0[0Ktravis_time:end:0594a8f0:start=1579803334046053174,finish=1579803334353205873,duration=307152699,event=wait_for_network[0Ktravis_time:start:07998cc6[0Ktravis_time:end:07998cc6:start=1579803334357895336,finish=1579803335543318470,duration=1185423134,event=update_apt_keys[0Ktravis_time:start:148d52a8[0Ktravis_time:end:148d52a8:start=1579803335547590080,finish=1579803336445334657,duration=897744577,event=fix_hhvm_source[0Ktravis_time:start:11f5c635[0Ktravis_time:end:11f5c635:start=1579803336449661924,finish=1579803336458420561,duration=8758637,event=update_mongo_arch[0Ktravis_time:start:003e675a[0Ktravis_time:end:003e675a:start=1579803336463840069,finish=1579803336498438173,duration=34598104,event=fix_sudo_enabled_trusty[0Ktravis_time:start:06a81a64[0Ktravis_time:end:06a81a64:start=1579803336502710344,finish=1579803336505678425,duration=2968081,event=update_glibc[0Ktravis_time:start:2b34bb5c[0Ktravis_time:end:2b34bb5c:start=1579803336510140893,finish=1579803336517984759,duration=7843866,event=clean_up_path[0Ktravis_time:start:29e9b6e5[0Ktravis_time:end:29e9b6e5:start=1579803336522364653,finish=1579803336530046207,duration=7681554,event=fix_resolv_conf[0Ktravis_time:start:08068539[0Ktravis_time:end:08068539:start=1579803336533964003,finish=1579803336542023981,duration=8059978,event=fix_etc_hosts[0Ktravis_time:start:02527054[0Ktravis_time:end:02527054:start=1579803336545972502,finish=1579803336554929607,duration=8957105,event=fix_mvn_settings_xml[0Ktravis_time:start:2bb47b0e[0Ktravis_time:end:2bb47b0e:start=1579803336558745441,finish=1579803336567159971,duration=8414530,event=no_ipv6_localhost[0Ktravis_time:start:0f160a70[0Ktravis_time:end:0f160a70:start=1579803336572070088,finish=1579803336574317802,duration=2247714,event=fix_etc_mavenrc[0Ktravis_time:start:0453a92c[0Ktravis_time:end:0453a92c:start=1579803336578305016,finish=1579803336581941821,duration=3636805,event=fix_wwdr_certificate[0Ktravis_time:start:08cc42ac[0Ktravis_time:end:08cc42ac:start=1579803336586469623,finish=1579803336610095280,duration=23625657,event=put_localhost_first[0Ktravis_time:start:04c3ed00[0Ktravis_time:end:04c3ed00:start=1579803336613689086,finish=1579803336617324484,duration=3635398,event=home_paths[0Ktravis_time:start:00f6dcf2[0Ktravis_time:end:00f6dcf2:start=1579803336621287648,finish=1579803336632218420,duration=10930772,event=disable_initramfs[0Ktravis_time:start:149ab358[0Ktravis_time:end:149ab358:start=1579803336640035485,finish=1579803336856127387,duration=216091902,event=disable_ssh_roaming[0Ktravis_time:start:05fcec20[0Ktravis_time:end:05fcec20:start=1579803336860165163,finish=1579803336863096796,duration=2931633,event=debug_tools[0Ktravis_time:start:1de7ff32[0Ktravis_time:end:1de7ff32:start=1579803336867240539,finish=1579803336871277697,duration=4037158,event=uninstall_oclint[0Ktravis_time:start:251cefe0[0Ktravis_time:end:251cefe0:start=1579803336881856591,finish=1579803336885258524,duration=3401933,event=rvm_use[0Ktravis_time:start:00aa6409[0Ktravis_time:end:00aa6409:start=1579803336889369196,finish=1579803336897330179,duration=7960983,event=rm_etc_boto_cfg[0Ktravis_time:start:2825a644[0Ktravis_time:end:2825a644:start=1579803336904710961,finish=1579803336907190372,duration=2479411,event=rm_oraclejdk8_symlink[0Ktravis_time:start:152839e4[0Ktravis_time:end:152839e4:start=1579803336911073430,finish=1579803336958680677,duration=47607247,event=enable_i386[0Ktravis_time:start:03ae9b26[0Ktravis_time:end:03ae9b26:start=1579803336962870507,finish=1579803336966446454,duration=3575947,event=update_rubygems[0Ktravis_time:start:34285602[0Ktravis_time:end:34285602:start=1579803336970930904,finish=1579803337841405145,duration=870474241,event=ensure_path_components[0Ktravis_time:start:082ac2fc[0Ktravis_time:end:082ac2fc:start=1579803337845453715,finish=1579803337847977805,duration=2524090,event=redefine_curl[0Ktravis_time:start:001ebe7b[0Ktravis_time:end:001ebe7b:start=1579803337852497629,finish=1579803337895501738,duration=43004109,event=nonblock_pipe[0Ktravis_time:start:0336f276[0Ktravis_time:end:0336f276:start=1579803337899405164,finish=1579803343929906951,duration=6030501787,event=apt_get_update[0Ktravis_time:start:13db6950[0Ktravis_time:end:13db6950:start=1579803343934220343,finish=1579803343936935561,duration=2715218,event=deprecate_xcode_64[0Ktravis_time:start:01875b58[0Ktravis_time:end:01875b58:start=1579803343941105186,finish=1579803347564679062,duration=3623573876,event=update_heroku[0Ktravis_time:start:0eb5002c[0Ktravis_time:end:0eb5002c:start=1579803347568892501,finish=1579803347571924997,duration=3032496,event=shell_session_update[0Ktravis_time:start:1892740e[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3971
travis_fold:end:docker_mtu[0Ktravis_time:end:1892740e:start=1579803347576719363,finish=1579803348767115743,duration=1190396380,event=set_docker_mtu[0Ktravis_time:start:1c9affa0[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1c9affa0:start=1579803348771688848,finish=1579803348831042188,duration=59353340,event=resolvconf[0Ktravis_time:start:05a61b88[0Ktravis_time:end:05a61b88:start=1579803348835230076,finish=1579803348916404606,duration=81174530,event=maven_central_mirror[0Ktravis_time:start:00742450[0Ktravis_time:end:00742450:start=1579803348920850176,finish=1579803348988126771,duration=67276595,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0cb4c3fe[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0cb4c3fe:start=1579803349067058378,finish=1579803349513737126,duration=446678748,event=configure[0Ktravis_time:start:21f18c06[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:21f18c06:start=1579803349518987742,finish=1579803358823359371,duration=9304371629,event=configure[0Ktravis_time:start:06b672fa[0Ktravis_fold:start:services[0Ktravis_time:start:13ee0c8b[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:13ee0c8b:start=1579803358846478290,finish=1579803358859050945,duration=12572655,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:13ee0c8b:start=1579803358846478290,finish=1579803361864295220,duration=3017816930,event=services[0Ktravis_time:start:09710b3a[0Ktravis_time:end:09710b3a:start=1579803361868392413,finish=1579803361871130645,duration=2738232,event=fix_ps4[0Ktravis_time:start:0a4fea10[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1410ed39[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1410ed39:start=1579803361879683443,finish=1579803368089438891,duration=6209755448,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:28f73d39[0K$ git fetch origin +refs/pull/148/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/148/merge -> FETCH_HEAD
travis_time:end:28f73d39:start=1579803368094101165,finish=1579803368681118215,duration=587017050,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:28f73d39:start=1579803368094101165,finish=1579803368759520239,duration=665419074,event=checkout[0Ktravis_time:start:00277c1a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00277c1a:start=1579803368764316255,finish=1579803368775264552,duration=10948297,event=env[0Ktravis_time:start:0051652f[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0051652f:start=1579803368779857761,finish=1579803368786003722,duration=6145961,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0b4aa598[0K$ [:script, "python push.py -s -t dealii-of"]
[:script,: command not found
travis_time:end:0b4aa598:start=1579803369083238715,finish=1579803369154198616,duration=70959901,event=script[0K[31;1mThe command "[:script, "python push.py -s -t dealii-of"]" exited with 127.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0edf573c[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/640895699/log.txt)