 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586510170) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/40d6daa277c6...b989e40888b7) 
## Last succesfull commits 
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
travis_time:end:0cf483b7:start=1568815388174986289,finish=1568815388181132821,duration=6146532,event=show_system_info[0Ktravis_time:start:0b094f98[0Ktravis_time:end:0b094f98:start=1568815388184221971,finish=1568815388207122441,duration=22900470,event=rm_riak_source[0Ktravis_time:start:04381420[0Ktravis_time:end:04381420:start=1568815388210261855,finish=1568815388215430024,duration=5168169,event=fix_rwky_redis[0Ktravis_time:start:0d99ec5c[0Ktravis_time:end:0d99ec5c:start=1568815388218383123,finish=1568815388633688109,duration=415304986,event=wait_for_network[0Ktravis_time:start:0fb862c6[0Ktravis_time:end:0fb862c6:start=1568815388638519694,finish=1568815389553298177,duration=914778483,event=update_apt_keys[0Ktravis_time:start:05ff4f74[0Ktravis_time:end:05ff4f74:start=1568815389557745913,finish=1568815390604533896,duration=1046787983,event=fix_hhvm_source[0Ktravis_time:start:078bb840[0Ktravis_time:end:078bb840:start=1568815390609222266,finish=1568815390619396109,duration=10173843,event=update_mongo_arch[0Ktravis_time:start:069d22b7[0Ktravis_time:end:069d22b7:start=1568815390624427929,finish=1568815390668381076,duration=43953147,event=fix_sudo_enabled_trusty[0Ktravis_time:start:11c604c0[0Ktravis_time:end:11c604c0:start=1568815390673991203,finish=1568815390678092855,duration=4101652,event=update_glibc[0Ktravis_time:start:29c42ee6[0Ktravis_time:end:29c42ee6:start=1568815390683006522,finish=1568815390696925046,duration=13918524,event=clean_up_path[0Ktravis_time:start:04d12260[0Ktravis_time:end:04d12260:start=1568815390701749142,finish=1568815390715196116,duration=13446974,event=fix_resolv_conf[0Ktravis_time:start:0ee09bb0[0Ktravis_time:end:0ee09bb0:start=1568815390719370846,finish=1568815390730277462,duration=10906616,event=fix_etc_hosts[0Ktravis_time:start:1a70cf3f[0Ktravis_time:end:1a70cf3f:start=1568815390738060652,finish=1568815390748491887,duration=10431235,event=fix_mvn_settings_xml[0Ktravis_time:start:09550200[0Ktravis_time:end:09550200:start=1568815390754162827,finish=1568815390764946415,duration=10783588,event=no_ipv6_localhost[0Ktravis_time:start:0c33ac7a[0Ktravis_time:end:0c33ac7a:start=1568815390769785617,finish=1568815390772855431,duration=3069814,event=fix_etc_mavenrc[0Ktravis_time:start:1c4415cb[0Ktravis_time:end:1c4415cb:start=1568815390778084194,finish=1568815390782887544,duration=4803350,event=fix_wwdr_certificate[0Ktravis_time:start:2220a4a1[0Ktravis_time:end:2220a4a1:start=1568815390787725568,finish=1568815390813722499,duration=25996931,event=put_localhost_first[0Ktravis_time:start:160ec930[0Ktravis_time:end:160ec930:start=1568815390819385467,finish=1568815390823913079,duration=4527612,event=home_paths[0Ktravis_time:start:14e02ff4[0Ktravis_time:end:14e02ff4:start=1568815390828331647,finish=1568815390841475452,duration=13143805,event=disable_initramfs[0Ktravis_time:start:04ee11f0[0Ktravis_time:end:04ee11f0:start=1568815390847628146,finish=1568815391132353543,duration=284725397,event=disable_ssh_roaming[0Ktravis_time:start:23c696a8[0Ktravis_time:end:23c696a8:start=1568815391137931597,finish=1568815391141558289,duration=3626692,event=debug_tools[0Ktravis_time:start:156267a8[0Ktravis_time:end:156267a8:start=1568815391147111066,finish=1568815391151139022,duration=4027956,event=uninstall_oclint[0Ktravis_time:start:010b934e[0Ktravis_time:end:010b934e:start=1568815391157998301,finish=1568815391163694439,duration=5696138,event=rvm_use[0Ktravis_time:start:1f774781[0Ktravis_time:end:1f774781:start=1568815391168864335,finish=1568815391178698664,duration=9834329,event=rm_etc_boto_cfg[0Ktravis_time:start:14173b00[0Ktravis_time:end:14173b00:start=1568815391184527941,finish=1568815391188531116,duration=4003175,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1af19732[0Ktravis_time:end:1af19732:start=1568815391193832936,finish=1568815391250271133,duration=56438197,event=enable_i386[0Ktravis_time:start:1afa099b[0Ktravis_time:end:1afa099b:start=1568815391256364338,finish=1568815391261713536,duration=5349198,event=update_rubygems[0Ktravis_time:start:0d36c032[0Ktravis_time:end:0d36c032:start=1568815391266432271,finish=1568815392296288439,duration=1029856168,event=ensure_path_components[0Ktravis_time:start:01accd64[0Ktravis_time:end:01accd64:start=1568815392302988755,finish=1568815392307093590,duration=4104835,event=redefine_curl[0Ktravis_time:start:0f8d1174[0Ktravis_time:end:0f8d1174:start=1568815392311807075,finish=1568815392364951283,duration=53144208,event=nonblock_pipe[0Ktravis_time:start:00f8af5c[0Ktravis_time:end:00f8af5c:start=1568815392371180392,finish=1568815392416717641,duration=45537249,event=apt_get_update[0Ktravis_time:start:0e0556dc[0Ktravis_time:end:0e0556dc:start=1568815392421813050,finish=1568815392424412264,duration=2599214,event=deprecate_xcode_64[0Ktravis_time:start:1cebcd0c[0Ktravis_time:end:1cebcd0c:start=1568815392429290164,finish=1568815396979230694,duration=4549940530,event=update_heroku[0Ktravis_time:start:00ca65c0[0Ktravis_time:end:00ca65c0:start=1568815396984914684,finish=1568815396988326761,duration=3412077,event=shell_session_update[0Ktravis_time:start:25654431[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3859
travis_fold:end:docker_mtu[0Ktravis_time:end:25654431:start=1568815396993715693,finish=1568815398192621260,duration=1198905567,event=set_docker_mtu[0Ktravis_time:start:1e3cee20[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1e3cee20:start=1568815398197956433,finish=1568815398267653239,duration=69696806,event=resolvconf[0Ktravis_time:start:011af885[0Ktravis_time:end:011af885:start=1568815398272189149,finish=1568815398370328956,duration=98139807,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00051be2[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00051be2:start=1568815398459064170,finish=1568815398796238918,duration=337174748,event=configure[0Ktravis_time:start:17222248[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:17222248:start=1568815398801972921,finish=1568815409201081007,duration=10399108086,event=configure[0Ktravis_time:start:33d1c5a8[0Ktravis_fold:start:services[0Ktravis_time:start:1b0130d4[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1b0130d4:start=1568815409227247004,finish=1568815409243408065,duration=16161061,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1b0130d4:start=1568815409227247004,finish=1568815412249096216,duration=3021849212,event=services[0Ktravis_time:start:08fa48f0[0Ktravis_time:end:08fa48f0:start=1568815412255541653,finish=1568815412258656563,duration=3114910,event=fix_ps4[0Ktravis_time:start:09a31c4b[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0d926bf7[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0d926bf7:start=1568815412269069538,finish=1568815422899016187,duration=10629946649,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b989e40888b7bc80b4a7d6d823b98fc3ebb61025
travis_fold:end:git.checkout[0K
travis_time:end:0d926bf7:start=1568815412269069538,finish=1568815423737380686,duration=11468311148,event=checkout[0Ktravis_time:start:22cb7836[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:22cb7836:start=1568815423742736810,finish=1568815423760696688,duration=17959878,event=env[0Ktravis_time:start:006d5ba0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:006d5ba0:start=1568815423766573961,finish=1568815423773446088,duration=6872127,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:11b574cd[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {of-of,bindings,of-ccx,of-ccx_fsi,dealii-of,su2-ccx,of-of_np,fe-fe,nutils-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:11b574cd:start=1568815424143811796,finish=1568815424212351432,duration=68539636,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:05fa8052[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586510190/log.txt)