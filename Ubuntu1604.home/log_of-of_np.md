 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586477733) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3c3e92795247) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef) 
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
travis_time:end:1ee80439:start=1568806918782107971,finish=1568806918787944487,duration=5836516,event=show_system_info[0Ktravis_time:start:081ec00d[0Ktravis_time:end:081ec00d:start=1568806918790796786,finish=1568806918817333934,duration=26537148,event=rm_riak_source[0Ktravis_time:start:1698ab76[0Ktravis_time:end:1698ab76:start=1568806918820660681,finish=1568806918825868542,duration=5207861,event=fix_rwky_redis[0Ktravis_time:start:08e7a399[0Ktravis_time:end:08e7a399:start=1568806918829041523,finish=1568806922011191875,duration=3182150352,event=wait_for_network[0Ktravis_time:start:0d468d70[0Ktravis_time:end:0d468d70:start=1568806922017691114,finish=1568806923593466203,duration=1575775089,event=update_apt_keys[0Ktravis_time:start:06273769[0Ktravis_time:end:06273769:start=1568806923598414531,finish=1568806924625853979,duration=1027439448,event=fix_hhvm_source[0Ktravis_time:start:0a158bca[0Ktravis_time:end:0a158bca:start=1568806924631402860,finish=1568806924641693643,duration=10290783,event=update_mongo_arch[0Ktravis_time:start:1d8ca902[0Ktravis_time:end:1d8ca902:start=1568806924647755776,finish=1568806924689367385,duration=41611609,event=fix_sudo_enabled_trusty[0Ktravis_time:start:26cdf944[0Ktravis_time:end:26cdf944:start=1568806924694996742,finish=1568806924698694559,duration=3697817,event=update_glibc[0Ktravis_time:start:087bd4ac[0Ktravis_time:end:087bd4ac:start=1568806924703226014,finish=1568806924713155288,duration=9929274,event=clean_up_path[0Ktravis_time:start:111d2dc9[0Ktravis_time:end:111d2dc9:start=1568806924718133224,finish=1568806924726623476,duration=8490252,event=fix_resolv_conf[0Ktravis_time:start:0dfb8c48[0Ktravis_time:end:0dfb8c48:start=1568806924731186767,finish=1568806924742709298,duration=11522531,event=fix_etc_hosts[0Ktravis_time:start:1c2d43a0[0Ktravis_time:end:1c2d43a0:start=1568806924748549615,finish=1568806924759771179,duration=11221564,event=fix_mvn_settings_xml[0Ktravis_time:start:12a54a9c[0Ktravis_time:end:12a54a9c:start=1568806924764460886,finish=1568806924774465158,duration=10004272,event=no_ipv6_localhost[0Ktravis_time:start:01e07618[0Ktravis_time:end:01e07618:start=1568806924779300015,finish=1568806924782076329,duration=2776314,event=fix_etc_mavenrc[0Ktravis_time:start:04acbc29[0Ktravis_time:end:04acbc29:start=1568806924786725162,finish=1568806924790843481,duration=4118319,event=fix_wwdr_certificate[0Ktravis_time:start:10f153aa[0Ktravis_time:end:10f153aa:start=1568806924796681639,finish=1568806924822306533,duration=25624894,event=put_localhost_first[0Ktravis_time:start:23166fde[0Ktravis_time:end:23166fde:start=1568806924826616173,finish=1568806924830932658,duration=4316485,event=home_paths[0Ktravis_time:start:16bf8b22[0Ktravis_time:end:16bf8b22:start=1568806924836319402,finish=1568806924850677941,duration=14358539,event=disable_initramfs[0Ktravis_time:start:0624021e[0Ktravis_time:end:0624021e:start=1568806924856093718,finish=1568806925125330216,duration=269236498,event=disable_ssh_roaming[0Ktravis_time:start:0481dcb7[0Ktravis_time:end:0481dcb7:start=1568806925130130491,finish=1568806925132882796,duration=2752305,event=debug_tools[0Ktravis_time:start:0164a190[0Ktravis_time:end:0164a190:start=1568806925138000445,finish=1568806925143798646,duration=5798201,event=uninstall_oclint[0Ktravis_time:start:0a0d4051[0Ktravis_time:end:0a0d4051:start=1568806925148978361,finish=1568806925153810338,duration=4831977,event=rvm_use[0Ktravis_time:start:1c641871[0Ktravis_time:end:1c641871:start=1568806925158879941,finish=1568806925169591860,duration=10711919,event=rm_etc_boto_cfg[0Ktravis_time:start:00499d7a[0Ktravis_time:end:00499d7a:start=1568806925173870815,finish=1568806925176515684,duration=2644869,event=rm_oraclejdk8_symlink[0Ktravis_time:start:00f71610[0Ktravis_time:end:00f71610:start=1568806925180704113,finish=1568806925237910047,duration=57205934,event=enable_i386[0Ktravis_time:start:0016442e[0Ktravis_time:end:0016442e:start=1568806925242672863,finish=1568806925247171328,duration=4498465,event=update_rubygems[0Ktravis_time:start:0132354f[0Ktravis_time:end:0132354f:start=1568806925251766438,finish=1568806926277068610,duration=1025302172,event=ensure_path_components[0Ktravis_time:start:0db655b1[0Ktravis_time:end:0db655b1:start=1568806926282080011,finish=1568806926285930309,duration=3850298,event=redefine_curl[0Ktravis_time:start:2e2562f4[0Ktravis_time:end:2e2562f4:start=1568806926291230938,finish=1568806926348461754,duration=57230816,event=nonblock_pipe[0Ktravis_time:start:0b68cf80[0Ktravis_time:end:0b68cf80:start=1568806926353634446,finish=1568806926420358933,duration=66724487,event=apt_get_update[0Ktravis_time:start:0163bfd8[0Ktravis_time:end:0163bfd8:start=1568806926424808324,finish=1568806926427819189,duration=3010865,event=deprecate_xcode_64[0Ktravis_time:start:03d048e9[0Ktravis_time:end:03d048e9:start=1568806926431797946,finish=1568806931429241103,duration=4997443157,event=update_heroku[0Ktravis_time:start:00c83cf0[0Ktravis_time:end:00c83cf0:start=1568806931433787751,finish=1568806931436792788,duration=3005037,event=shell_session_update[0Ktravis_time:start:1b1e0e5d[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3871
travis_fold:end:docker_mtu[0Ktravis_time:end:1b1e0e5d:start=1568806931441050481,finish=1568806932628808824,duration=1187758343,event=set_docker_mtu[0Ktravis_time:start:0da8682f[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0da8682f:start=1568806932633211074,finish=1568806932697858387,duration=64647313,event=resolvconf[0Ktravis_time:start:11eb7012[0Ktravis_time:end:11eb7012:start=1568806932702385880,finish=1568806932798085710,duration=95699830,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0c1159de[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0c1159de:start=1568806932881865345,finish=1568806933173572563,duration=291707218,event=configure[0Ktravis_time:start:0faedd2e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0faedd2e:start=1568806933179009766,finish=1568806942928384541,duration=9749374775,event=configure[0Ktravis_time:start:0b724860[0Ktravis_fold:start:services[0Ktravis_time:start:0e48420a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0e48420a:start=1568806942954211268,finish=1568806942968702179,duration=14490911,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0e48420a:start=1568806942954211268,finish=1568806945974731136,duration=3020519868,event=services[0Ktravis_time:start:03f74ec0[0Ktravis_time:end:03f74ec0:start=1568806945979619446,finish=1568806945982359826,duration=2740380,event=fix_ps4[0Ktravis_time:start:17c97422[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0f1b1a16[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0f1b1a16:start=1568806945990730798,finish=1568806956760588010,duration=10769857212,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3c3e927952479f3d81847ce6139ede1bec7f9aff
travis_fold:end:git.checkout[0K
travis_time:end:0f1b1a16:start=1568806945990730798,finish=1568806957450811009,duration=11460080211,event=checkout[0Ktravis_time:start:036cd3da[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:036cd3da:start=1568806957455515253,finish=1568806957468432902,duration=12917649,event=env[0Ktravis_time:start:06ec8520[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:06ec8520:start=1568806957476315681,finish=1568806957482318099,duration=6002418,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:0164ec08[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,nutils-of,of-ccx,of-ccx_fsi,of-of,of-of_np,bindings,dealii-of,fe-fe}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:0164ec08:start=1568806957828620327,finish=1568806957890577518,duration=61957191,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:02e4f710[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586477763/log.txt)