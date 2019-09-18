 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478260) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3c3e92795247...4d912263806c) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf) 
## Last 100 lines of the job log at the moment of push...
```
 [34m[1mElasticSearch version[0m
5.5.0
[34m[1mInstalled Firefox version[0m
firefox 56.0.2
[34m[1mMongoDB version[0m
MongoDB 3.4.10
[34m[1mPhantomJS version[0m
2.1.1
[34m[1mPre-installed PostgreSQL versions[0m
9.2.24
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
travis_time:end:05341546:start=1568808243589671791,finish=1568808243596750449,duration=7078658,event=show_system_info[0Ktravis_time:start:1c82be1f[0Ktravis_time:end:1c82be1f:start=1568808243599943427,finish=1568808243630507030,duration=30563603,event=rm_riak_source[0Ktravis_time:start:2525f7f0[0Ktravis_time:end:2525f7f0:start=1568808243633665626,finish=1568808243639157639,duration=5492013,event=fix_rwky_redis[0Ktravis_time:start:21374868[0Ktravis_time:end:21374868:start=1568808243642149523,finish=1568808244078368999,duration=436219476,event=wait_for_network[0Ktravis_time:start:017352d6[0Ktravis_time:end:017352d6:start=1568808244082674601,finish=1568808245679086609,duration=1596412008,event=update_apt_keys[0Ktravis_time:start:165fca48[0Ktravis_time:end:165fca48:start=1568808245683913110,finish=1568808246882386024,duration=1198472914,event=fix_hhvm_source[0Ktravis_time:start:2a472bfe[0Ktravis_time:end:2a472bfe:start=1568808246887774711,finish=1568808246898174548,duration=10399837,event=update_mongo_arch[0Ktravis_time:start:1090a9f9[0Ktravis_time:end:1090a9f9:start=1568808246902338303,finish=1568808246949239757,duration=46901454,event=fix_sudo_enabled_trusty[0Ktravis_time:start:26d84d32[0Ktravis_time:end:26d84d32:start=1568808246955095182,finish=1568808246958340671,duration=3245489,event=update_glibc[0Ktravis_time:start:059d9542[0Ktravis_time:end:059d9542:start=1568808246962870712,finish=1568808246972575036,duration=9704324,event=clean_up_path[0Ktravis_time:start:1c24ba7c[0Ktravis_time:end:1c24ba7c:start=1568808246976947783,finish=1568808246986267854,duration=9320071,event=fix_resolv_conf[0Ktravis_time:start:070452c9[0Ktravis_time:end:070452c9:start=1568808246990301420,finish=1568808247001782589,duration=11481169,event=fix_etc_hosts[0Ktravis_time:start:0f448edb[0Ktravis_time:end:0f448edb:start=1568808247006249792,finish=1568808247016939575,duration=10689783,event=fix_mvn_settings_xml[0Ktravis_time:start:07021d8e[0Ktravis_time:end:07021d8e:start=1568808247020916897,finish=1568808247034515274,duration=13598377,event=no_ipv6_localhost[0Ktravis_time:start:2b906354[0Ktravis_time:end:2b906354:start=1568808247038865074,finish=1568808247041924459,duration=3059385,event=fix_etc_mavenrc[0Ktravis_time:start:08b58178[0Ktravis_time:end:08b58178:start=1568808247046101875,finish=1568808247050132659,duration=4030784,event=fix_wwdr_certificate[0Ktravis_time:start:0473eef0[0Ktravis_time:end:0473eef0:start=1568808247054030735,finish=1568808247085489136,duration=31458401,event=put_localhost_first[0Ktravis_time:start:23c05278[0Ktravis_time:end:23c05278:start=1568808247090062808,finish=1568808247095481181,duration=5418373,event=home_paths[0Ktravis_time:start:2bcdd62a[0Ktravis_time:end:2bcdd62a:start=1568808247100091436,finish=1568808247118297577,duration=18206141,event=disable_initramfs[0Ktravis_time:start:1c623b80[0Ktravis_time:end:1c623b80:start=1568808247123427302,finish=1568808247507247625,duration=383820323,event=disable_ssh_roaming[0Ktravis_time:start:265ba900[0Ktravis_time:end:265ba900:start=1568808247511947520,finish=1568808247514815155,duration=2867635,event=debug_tools[0Ktravis_time:start:09aae0e3[0Ktravis_time:end:09aae0e3:start=1568808247520460128,finish=1568808247524451392,duration=3991264,event=uninstall_oclint[0Ktravis_time:start:004cd664[0Ktravis_time:end:004cd664:start=1568808247529050302,finish=1568808247533537322,duration=4487020,event=rvm_use[0Ktravis_time:start:03bf7674[0Ktravis_time:end:03bf7674:start=1568808247537856836,finish=1568808247549084873,duration=11228037,event=rm_etc_boto_cfg[0Ktravis_time:start:065c489f[0Ktravis_time:end:065c489f:start=1568808247553838683,finish=1568808247556597479,duration=2758796,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0bf6fcce[0Ktravis_time:end:0bf6fcce:start=1568808247563319063,finish=1568808247621152281,duration=57833218,event=enable_i386[0Ktravis_time:start:0ce2a1d8[0Ktravis_time:end:0ce2a1d8:start=1568808247627144151,finish=1568808247632324661,duration=5180510,event=update_rubygems[0Ktravis_time:start:1b6dc358[0Ktravis_time:end:1b6dc358:start=1568808247637224739,finish=1568808248768216031,duration=1130991292,event=ensure_path_components[0Ktravis_time:start:1ca0d5cc[0Ktravis_time:end:1ca0d5cc:start=1568808248773772843,finish=1568808248776993531,duration=3220688,event=redefine_curl[0Ktravis_time:start:1a5d8409[0Ktravis_time:end:1a5d8409:start=1568808248781682666,finish=1568808248847755856,duration=66073190,event=nonblock_pipe[0Ktravis_time:start:10e213e9[0Ktravis_time:end:10e213e9:start=1568808248853676520,finish=1568808248908258275,duration=54581755,event=apt_get_update[0Ktravis_time:start:0526d01f[0Ktravis_time:end:0526d01f:start=1568808248912909161,finish=1568808248916029339,duration=3120178,event=deprecate_xcode_64[0Ktravis_time:start:0690bd8c[0Ktravis_time:end:0690bd8c:start=1568808248920223998,finish=1568808254259578488,duration=5339354490,event=update_heroku[0Ktravis_time:start:2fb451e4[0Ktravis_time:end:2fb451e4:start=1568808254264023032,finish=1568808254266813561,duration=2790529,event=shell_session_update[0Ktravis_time:start:1f554db8[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3832
travis_fold:end:docker_mtu[0Ktravis_time:end:1f554db8:start=1568808254271053161,finish=1568808255471362149,duration=1200308988,event=set_docker_mtu[0Ktravis_time:start:23c6e5ee[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:23c6e5ee:start=1568808255476673311,finish=1568808255549954723,duration=73281412,event=resolvconf[0Ktravis_time:start:333333c0[0Ktravis_time:end:333333c0:start=1568808255554864564,finish=1568808255671550153,duration=116685589,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:25ba3908[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:25ba3908:start=1568808255762050550,finish=1568808256463836018,duration=701785468,event=configure[0Ktravis_time:start:0000b398[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0000b398:start=1568808256468952616,finish=1568808266214059946,duration=9745107330,event=configure[0Ktravis_time:start:001a4270[0Ktravis_fold:start:services[0Ktravis_time:start:305f09bc[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:305f09bc:start=1568808266238641250,finish=1568808266253376945,duration=14735695,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:305f09bc:start=1568808266238641250,finish=1568808269258771460,duration=3020130210,event=services[0Ktravis_time:start:0988cb30[0Ktravis_time:end:0988cb30:start=1568808269263805327,finish=1568808269266715600,duration=2910273,event=fix_ps4[0Ktravis_time:start:0f5bf442[0K
travis_fold:start:git.checkout[0Ktravis_time:start:04c89372[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:04c89372:start=1568808269276004025,finish=1568808280134114714,duration=10858110689,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 4d912263806c85d105a3cfc8dba374f4f3a4853a
travis_fold:end:git.checkout[0K
travis_time:end:04c89372:start=1568808269276004025,finish=1568808280299030813,duration=11023026788,event=checkout[0Ktravis_time:start:0faffb2c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0faffb2c:start=1568808280304558153,finish=1568808280421939053,duration=117380900,event=env[0Ktravis_time:start:10da3344[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:10da3344:start=1568808280432213632,finish=1568808280440966636,duration=8753004,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478276/log.txt)