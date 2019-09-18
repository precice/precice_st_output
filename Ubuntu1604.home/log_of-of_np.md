 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586518622) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/98) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef) 
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
travis_time:end:00f5a0dc:start=1568824732975647475,finish=1568824732981588814,duration=5941339,event=show_system_info[0Ktravis_time:start:144607a5[0Ktravis_time:end:144607a5:start=1568824732984591009,finish=1568824733014664292,duration=30073283,event=rm_riak_source[0Ktravis_time:start:0283fdf6[0Ktravis_time:end:0283fdf6:start=1568824733018186002,finish=1568824733023857182,duration=5671180,event=fix_rwky_redis[0Ktravis_time:start:0e5aff1c[0Ktravis_time:end:0e5aff1c:start=1568824733026977924,finish=1568824733450242582,duration=423264658,event=wait_for_network[0Ktravis_time:start:0398c55f[0Ktravis_time:end:0398c55f:start=1568824733455938749,finish=1568824738042276813,duration=4586338064,event=update_apt_keys[0Ktravis_time:start:18aff2e0[0Ktravis_time:end:18aff2e0:start=1568824738046551528,finish=1568824739079053323,duration=1032501795,event=fix_hhvm_source[0Ktravis_time:start:2b6c37fa[0Ktravis_time:end:2b6c37fa:start=1568824739083706668,finish=1568824739093610266,duration=9903598,event=update_mongo_arch[0Ktravis_time:start:22f05f9c[0Ktravis_time:end:22f05f9c:start=1568824739098597174,finish=1568824739140644998,duration=42047824,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0cc0db70[0Ktravis_time:end:0cc0db70:start=1568824739145622504,finish=1568824739148469481,duration=2846977,event=update_glibc[0Ktravis_time:start:0cf8493f[0Ktravis_time:end:0cf8493f:start=1568824739154178141,finish=1568824739165716130,duration=11537989,event=clean_up_path[0Ktravis_time:start:2827d478[0Ktravis_time:end:2827d478:start=1568824739171141506,finish=1568824739182098678,duration=10957172,event=fix_resolv_conf[0Ktravis_time:start:179044d3[0Ktravis_time:end:179044d3:start=1568824739187198161,finish=1568824739196866661,duration=9668500,event=fix_etc_hosts[0Ktravis_time:start:103c4f64[0Ktravis_time:end:103c4f64:start=1568824739203304261,finish=1568824739212641282,duration=9337021,event=fix_mvn_settings_xml[0Ktravis_time:start:0e79a19e[0Ktravis_time:end:0e79a19e:start=1568824739216839410,finish=1568824739226989142,duration=10149732,event=no_ipv6_localhost[0Ktravis_time:start:000633cf[0Ktravis_time:end:000633cf:start=1568824739232131112,finish=1568824739234932417,duration=2801305,event=fix_etc_mavenrc[0Ktravis_time:start:0e29c800[0Ktravis_time:end:0e29c800:start=1568824739239173758,finish=1568824739243105089,duration=3931331,event=fix_wwdr_certificate[0Ktravis_time:start:2761d1b7[0Ktravis_time:end:2761d1b7:start=1568824739248271723,finish=1568824739275324407,duration=27052684,event=put_localhost_first[0Ktravis_time:start:09ea19d7[0Ktravis_time:end:09ea19d7:start=1568824739280131633,finish=1568824739284071100,duration=3939467,event=home_paths[0Ktravis_time:start:0159cf29[0Ktravis_time:end:0159cf29:start=1568824739289360786,finish=1568824739301313648,duration=11952862,event=disable_initramfs[0Ktravis_time:start:17c041e0[0Ktravis_time:end:17c041e0:start=1568824739305833125,finish=1568824739593846505,duration=288013380,event=disable_ssh_roaming[0Ktravis_time:start:0ab961ac[0Ktravis_time:end:0ab961ac:start=1568824739598517692,finish=1568824739601936448,duration=3418756,event=debug_tools[0Ktravis_time:start:00251682[0Ktravis_time:end:00251682:start=1568824739606403382,finish=1568824739610745433,duration=4342051,event=uninstall_oclint[0Ktravis_time:start:0585acc8[0Ktravis_time:end:0585acc8:start=1568824739618441105,finish=1568824739622033192,duration=3592087,event=rvm_use[0Ktravis_time:start:022f3646[0Ktravis_time:end:022f3646:start=1568824739626122298,finish=1568824739634185205,duration=8062907,event=rm_etc_boto_cfg[0Ktravis_time:start:0aec7929[0Ktravis_time:end:0aec7929:start=1568824739639629604,finish=1568824739642553655,duration=2924051,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0638b3a7[0Ktravis_time:end:0638b3a7:start=1568824739647018480,finish=1568824739711343213,duration=64324733,event=enable_i386[0Ktravis_time:start:04022ed0[0Ktravis_time:end:04022ed0:start=1568824739715506518,finish=1568824739720527818,duration=5021300,event=update_rubygems[0Ktravis_time:start:13ddd228[0Ktravis_time:end:13ddd228:start=1568824739724850314,finish=1568824740741922836,duration=1017072522,event=ensure_path_components[0Ktravis_time:start:01d12340[0Ktravis_time:end:01d12340:start=1568824740746922031,finish=1568824740749751663,duration=2829632,event=redefine_curl[0Ktravis_time:start:02276951[0Ktravis_time:end:02276951:start=1568824740754298667,finish=1568824740809006472,duration=54707805,event=nonblock_pipe[0Ktravis_time:start:0244946d[0Ktravis_time:end:0244946d:start=1568824740813664621,finish=1568824740854333841,duration=40669220,event=apt_get_update[0Ktravis_time:start:06c0fbf8[0Ktravis_time:end:06c0fbf8:start=1568824740858912640,finish=1568824740862040525,duration=3127885,event=deprecate_xcode_64[0Ktravis_time:start:00ecc994[0Ktravis_time:end:00ecc994:start=1568824740867131345,finish=1568824745957666669,duration=5090535324,event=update_heroku[0Ktravis_time:start:2275e230[0Ktravis_time:end:2275e230:start=1568824745963293580,finish=1568824745966277065,duration=2983485,event=shell_session_update[0Ktravis_time:start:320ef8b7[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3863
travis_fold:end:docker_mtu[0Ktravis_time:end:320ef8b7:start=1568824745971734131,finish=1568824747169710678,duration=1197976547,event=set_docker_mtu[0Ktravis_time:start:0113ad77[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0113ad77:start=1568824747173709726,finish=1568824747241269672,duration=67559946,event=resolvconf[0Ktravis_time:start:07fbd1f4[0Ktravis_time:end:07fbd1f4:start=1568824747246588799,finish=1568824747344802153,duration=98213354,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:041fb360[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:041fb360:start=1568824747427274439,finish=1568824747771069304,duration=343794865,event=configure[0Ktravis_time:start:068f97cd[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:068f97cd:start=1568824747777336725,finish=1568824757352370414,duration=9575033689,event=configure[0Ktravis_time:start:1ab60aac[0Ktravis_fold:start:services[0Ktravis_time:start:0224cd08[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0224cd08:start=1568824757376697303,finish=1568824757391196389,duration=14499086,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0224cd08:start=1568824757376697303,finish=1568824760396403170,duration=3019705867,event=services[0Ktravis_time:start:1e1ef028[0Ktravis_time:end:1e1ef028:start=1568824760401819822,finish=1568824760405576133,duration=3756311,event=fix_ps4[0Ktravis_time:start:17ecdf21[0K
travis_fold:start:git.checkout[0Ktravis_time:start:15262b9e[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:15262b9e:start=1568824760415588762,finish=1568824770968737548,duration=10553148786,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:19cc7c70[0K$ git fetch origin +refs/pull/98/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/98/merge -> FETCH_HEAD
travis_time:end:19cc7c70:start=1568824770973414097,finish=1568824771436744330,duration=463330233,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:19cc7c70:start=1568824770973414097,finish=1568824772387709871,duration=1414295774,event=checkout[0Ktravis_time:start:1ebf9a9c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1ebf9a9c:start=1568824772392998059,finish=1568824772403791026,duration=10792967,event=env[0Ktravis_time:start:368f6cfa[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:368f6cfa:start=1568824772408793799,finish=1568824772414596887,duration=5803088,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:13000066[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,nutils-of,su2-ccx,of-ccx,bindings,of-of,of-ccx_fsi,of-of_np,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:13000066:start=1568824772753733058,finish=1568824772821784481,duration=68051423,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:2ae4cc0b[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586518642/log.txt)