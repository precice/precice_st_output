 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478260) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3c3e92795247...4d912263806c) 
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
travis_time:end:14f9881c:start=1568808969253733444,finish=1568808969259719143,duration=5985699,event=show_system_info[0Ktravis_time:start:07ca0256[0Ktravis_time:end:07ca0256:start=1568808969262489892,finish=1568808969294869000,duration=32379108,event=rm_riak_source[0Ktravis_time:start:0002e0b2[0Ktravis_time:end:0002e0b2:start=1568808969297948215,finish=1568808969303001363,duration=5053148,event=fix_rwky_redis[0Ktravis_time:start:12ed3c0c[0Ktravis_time:end:12ed3c0c:start=1568808969305781525,finish=1568808969664856869,duration=359075344,event=wait_for_network[0Ktravis_time:start:12ad6274[0Ktravis_time:end:12ad6274:start=1568808969680142738,finish=1568808971412491432,duration=1732348694,event=update_apt_keys[0Ktravis_time:start:0bf3ab4e[0Ktravis_time:end:0bf3ab4e:start=1568808971417177673,finish=1568808972465719306,duration=1048541633,event=fix_hhvm_source[0Ktravis_time:start:113cd5b2[0Ktravis_time:end:113cd5b2:start=1568808972470234667,finish=1568808972480605192,duration=10370525,event=update_mongo_arch[0Ktravis_time:start:22257636[0Ktravis_time:end:22257636:start=1568808972484685527,finish=1568808972525275280,duration=40589753,event=fix_sudo_enabled_trusty[0Ktravis_time:start:05d6f830[0Ktravis_time:end:05d6f830:start=1568808972530374557,finish=1568808972533011475,duration=2636918,event=update_glibc[0Ktravis_time:start:1d4566a0[0Ktravis_time:end:1d4566a0:start=1568808972537480799,finish=1568808972547154393,duration=9673594,event=clean_up_path[0Ktravis_time:start:20383b52[0Ktravis_time:end:20383b52:start=1568808972551549505,finish=1568808972560129228,duration=8579723,event=fix_resolv_conf[0Ktravis_time:start:2a40e54f[0Ktravis_time:end:2a40e54f:start=1568808972564634311,finish=1568808972573916858,duration=9282547,event=fix_etc_hosts[0Ktravis_time:start:0ff5eaca[0Ktravis_time:end:0ff5eaca:start=1568808972578066359,finish=1568808972587283649,duration=9217290,event=fix_mvn_settings_xml[0Ktravis_time:start:0b145822[0Ktravis_time:end:0b145822:start=1568808972592785388,finish=1568808972604440763,duration=11655375,event=no_ipv6_localhost[0Ktravis_time:start:023db5f0[0Ktravis_time:end:023db5f0:start=1568808972609171967,finish=1568808972612385990,duration=3214023,event=fix_etc_mavenrc[0Ktravis_time:start:005e5eb9[0Ktravis_time:end:005e5eb9:start=1568808972617055045,finish=1568808972620862604,duration=3807559,event=fix_wwdr_certificate[0Ktravis_time:start:04c13956[0Ktravis_time:end:04c13956:start=1568808972625530414,finish=1568808972653867537,duration=28337123,event=put_localhost_first[0Ktravis_time:start:00db5b50[0Ktravis_time:end:00db5b50:start=1568808972658552100,finish=1568808972662511419,duration=3959319,event=home_paths[0Ktravis_time:start:01bcaf00[0Ktravis_time:end:01bcaf00:start=1568808972667319013,finish=1568808972680723797,duration=13404784,event=disable_initramfs[0Ktravis_time:start:0371f430[0Ktravis_time:end:0371f430:start=1568808972685154504,finish=1568808973081360475,duration=396205971,event=disable_ssh_roaming[0Ktravis_time:start:0c386cb2[0Ktravis_time:end:0c386cb2:start=1568808973085971393,finish=1568808973088561822,duration=2590429,event=debug_tools[0Ktravis_time:start:1b44adfd[0Ktravis_time:end:1b44adfd:start=1568808973092951619,finish=1568808973096685009,duration=3733390,event=uninstall_oclint[0Ktravis_time:start:07ec3876[0Ktravis_time:end:07ec3876:start=1568808973100750650,finish=1568808973104326723,duration=3576073,event=rvm_use[0Ktravis_time:start:219998ac[0Ktravis_time:end:219998ac:start=1568808973109039596,finish=1568808973117066468,duration=8026872,event=rm_etc_boto_cfg[0Ktravis_time:start:0537d84b[0Ktravis_time:end:0537d84b:start=1568808973121921080,finish=1568808973124449672,duration=2528592,event=rm_oraclejdk8_symlink[0Ktravis_time:start:069ba8d8[0Ktravis_time:end:069ba8d8:start=1568808973128806101,finish=1568808973184122955,duration=55316854,event=enable_i386[0Ktravis_time:start:1b651e1a[0Ktravis_time:end:1b651e1a:start=1568808973189139330,finish=1568808973193435398,duration=4296068,event=update_rubygems[0Ktravis_time:start:116e5177[0Ktravis_time:end:116e5177:start=1568808973198472284,finish=1568808974192326709,duration=993854425,event=ensure_path_components[0Ktravis_time:start:010bd762[0Ktravis_time:end:010bd762:start=1568808974198048902,finish=1568808974201035334,duration=2986432,event=redefine_curl[0Ktravis_time:start:120a1b71[0Ktravis_time:end:120a1b71:start=1568808974206266571,finish=1568808974261094905,duration=54828334,event=nonblock_pipe[0Ktravis_time:start:0734834a[0Ktravis_time:end:0734834a:start=1568808974265739753,finish=1568808974312539090,duration=46799337,event=apt_get_update[0Ktravis_time:start:1c6b19a0[0Ktravis_time:end:1c6b19a0:start=1568808974317078131,finish=1568808974319968275,duration=2890144,event=deprecate_xcode_64[0Ktravis_time:start:0dc5707c[0Ktravis_time:end:0dc5707c:start=1568808974324536891,finish=1568808979520631475,duration=5196094584,event=update_heroku[0Ktravis_time:start:236f04cf[0Ktravis_time:end:236f04cf:start=1568808979525534596,finish=1568808979528397306,duration=2862710,event=shell_session_update[0Ktravis_time:start:0c20ae20[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3862
travis_fold:end:docker_mtu[0Ktravis_time:end:0c20ae20:start=1568808979533190117,finish=1568808980723224333,duration=1190034216,event=set_docker_mtu[0Ktravis_time:start:1323df2c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1323df2c:start=1568808980727910594,finish=1568808980791060397,duration=63149803,event=resolvconf[0Ktravis_time:start:0d1c91ae[0Ktravis_time:end:0d1c91ae:start=1568808980796466102,finish=1568808980903586136,duration=107120034,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:106bed2a[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:106bed2a:start=1568808980988194146,finish=1568808981416308971,duration=428114825,event=configure[0Ktravis_time:start:039da0cd[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:039da0cd:start=1568808981421357975,finish=1568808990639138313,duration=9217780338,event=configure[0Ktravis_time:start:1ae5d0c0[0Ktravis_fold:start:services[0Ktravis_time:start:19df6c9a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:19df6c9a:start=1568808990664101107,finish=1568808990678554050,duration=14452943,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:19df6c9a:start=1568808990664101107,finish=1568808993683910118,duration=3019809011,event=services[0Ktravis_time:start:35a2c904[0Ktravis_time:end:35a2c904:start=1568808993688716068,finish=1568808993691431396,duration=2715328,event=fix_ps4[0Ktravis_time:start:08d53ce9[0K
travis_fold:start:git.checkout[0Ktravis_time:start:3330a7e4[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:3330a7e4:start=1568808993700554499,finish=1568809013561191718,duration=19860637219,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4d912263806c85d105a3cfc8dba374f4f3a4853a
travis_fold:end:git.checkout[0K
travis_time:end:3330a7e4:start=1568808993700554499,finish=1568809014080978483,duration=20380423984,event=checkout[0Ktravis_time:start:25985820[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:25985820:start=1568809014085800355,finish=1568809014097238430,duration=11438075,event=env[0Ktravis_time:start:00dbb5ee[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:00dbb5ee:start=1568809014101980596,finish=1568809014107702297,duration=5721701,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:145a34f8[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {dealii-of,of-of,of-of_np,bindings,of-ccx_fsi,nutils-of,su2-ccx,of-ccx,fe-fe}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:145a34f8:start=1568809014445608045,finish=1568809014510359529,duration=64751484,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0fd8afa4[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478282/log.txt)