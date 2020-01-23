## Status: Failure 
Build: [1481](https://travis-ci.org/precice/systemtests/builds/640895674) 

Job: [1481.19](https://travis-ci.org/precice/systemtests/jobs/640895699) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/148) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

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
travis_time:end:12a1ae07:start=1579788607860208437,finish=1579788607866836779,duration=6628342,event=show_system_info[0Ktravis_time:start:0af0847a[0Ktravis_time:end:0af0847a:start=1579788607869770646,finish=1579788607897886363,duration=28115717,event=rm_riak_source[0Ktravis_time:start:0061d763[0Ktravis_time:end:0061d763:start=1579788607903806381,finish=1579788607915429399,duration=11623018,event=fix_rwky_redis[0Ktravis_time:start:1137b3c7[0Ktravis_time:end:1137b3c7:start=1579788607919091724,finish=1579788608310374232,duration=391282508,event=wait_for_network[0Ktravis_time:start:14d805ca[0Ktravis_time:end:14d805ca:start=1579788608315123859,finish=1579788609192906390,duration=877782531,event=update_apt_keys[0Ktravis_time:start:2751735f[0Ktravis_time:end:2751735f:start=1579788609199205089,finish=1579788610176460199,duration=977255110,event=fix_hhvm_source[0Ktravis_time:start:28e003e8[0Ktravis_time:end:28e003e8:start=1579788610181997091,finish=1579788610191951120,duration=9954029,event=update_mongo_arch[0Ktravis_time:start:10840110[0Ktravis_time:end:10840110:start=1579788610196895610,finish=1579788610234490246,duration=37594636,event=fix_sudo_enabled_trusty[0Ktravis_time:start:202dad50[0Ktravis_time:end:202dad50:start=1579788610239600405,finish=1579788610243388243,duration=3787838,event=update_glibc[0Ktravis_time:start:38a2ef38[0Ktravis_time:end:38a2ef38:start=1579788610247495847,finish=1579788610258200380,duration=10704533,event=clean_up_path[0Ktravis_time:start:0c572acc[0Ktravis_time:end:0c572acc:start=1579788610263553005,finish=1579788610272743179,duration=9190174,event=fix_resolv_conf[0Ktravis_time:start:08282b44[0Ktravis_time:end:08282b44:start=1579788610276294734,finish=1579788610286174773,duration=9880039,event=fix_etc_hosts[0Ktravis_time:start:08a8b335[0Ktravis_time:end:08a8b335:start=1579788610292442638,finish=1579788610301279722,duration=8837084,event=fix_mvn_settings_xml[0Ktravis_time:start:27b50228[0Ktravis_time:end:27b50228:start=1579788610305079101,finish=1579788610317446856,duration=12367755,event=no_ipv6_localhost[0Ktravis_time:start:0d2313c0[0Ktravis_time:end:0d2313c0:start=1579788610321922728,finish=1579788610324591220,duration=2668492,event=fix_etc_mavenrc[0Ktravis_time:start:069f3f8f[0Ktravis_time:end:069f3f8f:start=1579788610328270145,finish=1579788610331549191,duration=3279046,event=fix_wwdr_certificate[0Ktravis_time:start:17ee58d4[0Ktravis_time:end:17ee58d4:start=1579788610334966320,finish=1579788610362375518,duration=27409198,event=put_localhost_first[0Ktravis_time:start:06111bc2[0Ktravis_time:end:06111bc2:start=1579788610366333674,finish=1579788610369902900,duration=3569226,event=home_paths[0Ktravis_time:start:1894f2e2[0Ktravis_time:end:1894f2e2:start=1579788610373798930,finish=1579788610388236972,duration=14438042,event=disable_initramfs[0Ktravis_time:start:12d83966[0Ktravis_time:end:12d83966:start=1579788610393049416,finish=1579788610703348329,duration=310298913,event=disable_ssh_roaming[0Ktravis_time:start:059b5232[0Ktravis_time:end:059b5232:start=1579788610709863441,finish=1579788610712665134,duration=2801693,event=debug_tools[0Ktravis_time:start:04d9cc2e[0Ktravis_time:end:04d9cc2e:start=1579788610718154819,finish=1579788610721511711,duration=3356892,event=uninstall_oclint[0Ktravis_time:start:0c6db802[0Ktravis_time:end:0c6db802:start=1579788610725877232,finish=1579788610729234227,duration=3356995,event=rvm_use[0Ktravis_time:start:1bdb4d70[0Ktravis_time:end:1bdb4d70:start=1579788610734353446,finish=1579788610742417659,duration=8064213,event=rm_etc_boto_cfg[0Ktravis_time:start:072f3a74[0Ktravis_time:end:072f3a74:start=1579788610746809393,finish=1579788610749341263,duration=2531870,event=rm_oraclejdk8_symlink[0Ktravis_time:start:12939390[0Ktravis_time:end:12939390:start=1579788610755687851,finish=1579788610805255391,duration=49567540,event=enable_i386[0Ktravis_time:start:002c0ea4[0Ktravis_time:end:002c0ea4:start=1579788610810227716,finish=1579788610814806757,duration=4579041,event=update_rubygems[0Ktravis_time:start:01a17074[0Ktravis_time:end:01a17074:start=1579788610818722646,finish=1579788611738543363,duration=919820717,event=ensure_path_components[0Ktravis_time:start:13625e7d[0Ktravis_time:end:13625e7d:start=1579788611743234099,finish=1579788611746535565,duration=3301466,event=redefine_curl[0Ktravis_time:start:03b8abf2[0Ktravis_time:end:03b8abf2:start=1579788611750859761,finish=1579788611808922637,duration=58062876,event=nonblock_pipe[0Ktravis_time:start:00be0fcd[0Ktravis_time:end:00be0fcd:start=1579788611813808876,finish=1579788617843149717,duration=6029340841,event=apt_get_update[0Ktravis_time:start:1ad1d050[0Ktravis_time:end:1ad1d050:start=1579788617847162105,finish=1579788617849807974,duration=2645869,event=deprecate_xcode_64[0Ktravis_time:start:0152e788[0Ktravis_time:end:0152e788:start=1579788617854087402,finish=1579788621846323037,duration=3992235635,event=update_heroku[0Ktravis_time:start:04229292[0Ktravis_time:end:04229292:start=1579788621850232957,finish=1579788621853078706,duration=2845749,event=shell_session_update[0Ktravis_time:start:044c1c8a[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3890
travis_fold:end:docker_mtu[0Ktravis_time:end:044c1c8a:start=1579788621856648256,finish=1579788623059637700,duration=1202989444,event=set_docker_mtu[0Ktravis_time:start:1dfd661e[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1dfd661e:start=1579788623064811961,finish=1579788623127072257,duration=62260296,event=resolvconf[0Ktravis_time:start:1568af08[0Ktravis_time:end:1568af08:start=1579788623131607828,finish=1579788623227035550,duration=95427722,event=maven_central_mirror[0Ktravis_time:start:15b134f8[0Ktravis_time:end:15b134f8:start=1579788623230881060,finish=1579788623301829264,duration=70948204,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0a2e378c[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0a2e378c:start=1579788623381387165,finish=1579788623869413581,duration=488026416,event=configure[0Ktravis_time:start:01e70eb4[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:01e70eb4:start=1579788623874843526,finish=1579788634823048301,duration=10948204775,event=configure[0Ktravis_time:start:31d7b2e4[0Ktravis_fold:start:services[0Ktravis_time:start:0e9de2e0[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0e9de2e0:start=1579788634847600640,finish=1579788634861290424,duration=13689784,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0e9de2e0:start=1579788634847600640,finish=1579788637866026362,duration=3018425722,event=services[0Ktravis_time:start:0fd4d14a[0Ktravis_time:end:0fd4d14a:start=1579788637870274192,finish=1579788637872762436,duration=2488244,event=fix_ps4[0Ktravis_time:start:258ff014[0K
travis_fold:start:git.checkout[0Ktravis_time:start:095f5920[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:095f5920:start=1579788637881309128,finish=1579788643368909322,duration=5487600194,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:01540686[0K$ git fetch origin +refs/pull/148/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/148/merge -> FETCH_HEAD
travis_time:end:01540686:start=1579788643374528880,finish=1579788643863972410,duration=489443530,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:01540686:start=1579788643374528880,finish=1579788644167572226,duration=793043346,event=checkout[0Ktravis_time:start:29af8d9e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:29af8d9e:start=1579788644172507937,finish=1579788644183933150,duration=11425213,event=env[0Ktravis_time:start:086f2bd8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:086f2bd8:start=1579788644188899794,finish=1579788644198095191,duration=9195397,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:23cc49a8[0K$ [:script, "python push.py -s -t dealii-of"]
[:script,: command not found
travis_time:end:23cc49a8:start=1579788644508095378,finish=1579788644580460063,duration=72364685,event=script[0K[31;1mThe command "[:script, "python push.py -s -t dealii-of"]" exited with 127.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1b972228[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/640895699/log.txt)