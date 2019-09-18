 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478286) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
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
travis_time:end:1b6867b0:start=1568810882593830769,finish=1568810882599953001,duration=6122232,event=show_system_info[0Ktravis_time:start:033044d6[0Ktravis_time:end:033044d6:start=1568810882602790120,finish=1568810882625579213,duration=22789093,event=rm_riak_source[0Ktravis_time:start:2bc2f940[0Ktravis_time:end:2bc2f940:start=1568810882628744316,finish=1568810882633958617,duration=5214301,event=fix_rwky_redis[0Ktravis_time:start:23222d7a[0Ktravis_time:end:23222d7a:start=1568810882636987858,finish=1568810883046255080,duration=409267222,event=wait_for_network[0Ktravis_time:start:01773133[0Ktravis_time:end:01773133:start=1568810883050725275,finish=1568810883970010398,duration=919285123,event=update_apt_keys[0Ktravis_time:start:01b8d232[0Ktravis_time:end:01b8d232:start=1568810883974988769,finish=1568810885035241123,duration=1060252354,event=fix_hhvm_source[0Ktravis_time:start:2a142000[0Ktravis_time:end:2a142000:start=1568810885040065185,finish=1568810885051134217,duration=11069032,event=update_mongo_arch[0Ktravis_time:start:02a11eb5[0Ktravis_time:end:02a11eb5:start=1568810885055645809,finish=1568810885098101156,duration=42455347,event=fix_sudo_enabled_trusty[0Ktravis_time:start:36ad3b80[0Ktravis_time:end:36ad3b80:start=1568810885102482722,finish=1568810885105129878,duration=2647156,event=update_glibc[0Ktravis_time:start:0273d6e3[0Ktravis_time:end:0273d6e3:start=1568810885109312369,finish=1568810885118159029,duration=8846660,event=clean_up_path[0Ktravis_time:start:0539206e[0Ktravis_time:end:0539206e:start=1568810885121948812,finish=1568810885130858648,duration=8909836,event=fix_resolv_conf[0Ktravis_time:start:02960784[0Ktravis_time:end:02960784:start=1568810885135833303,finish=1568810885145883469,duration=10050166,event=fix_etc_hosts[0Ktravis_time:start:0d362d00[0Ktravis_time:end:0d362d00:start=1568810885151174028,finish=1568810885162068139,duration=10894111,event=fix_mvn_settings_xml[0Ktravis_time:start:10e645ca[0Ktravis_time:end:10e645ca:start=1568810885166883375,finish=1568810885178069006,duration=11185631,event=no_ipv6_localhost[0Ktravis_time:start:070a715f[0Ktravis_time:end:070a715f:start=1568810885183028332,finish=1568810885185874340,duration=2846008,event=fix_etc_mavenrc[0Ktravis_time:start:0006ab30[0Ktravis_time:end:0006ab30:start=1568810885191173068,finish=1568810885195037185,duration=3864117,event=fix_wwdr_certificate[0Ktravis_time:start:0c8beda9[0Ktravis_time:end:0c8beda9:start=1568810885201945950,finish=1568810885227685964,duration=25740014,event=put_localhost_first[0Ktravis_time:start:1d21cbc5[0Ktravis_time:end:1d21cbc5:start=1568810885232819574,finish=1568810885236836199,duration=4016625,event=home_paths[0Ktravis_time:start:0247228e[0Ktravis_time:end:0247228e:start=1568810885242531213,finish=1568810885258120669,duration=15589456,event=disable_initramfs[0Ktravis_time:start:0009ca18[0Ktravis_time:end:0009ca18:start=1568810885262630319,finish=1568810885582601373,duration=319971054,event=disable_ssh_roaming[0Ktravis_time:start:0020c4c0[0Ktravis_time:end:0020c4c0:start=1568810885587283853,finish=1568810885591875861,duration=4592008,event=debug_tools[0Ktravis_time:start:2e399898[0Ktravis_time:end:2e399898:start=1568810885596503922,finish=1568810885600352715,duration=3848793,event=uninstall_oclint[0Ktravis_time:start:05aae454[0Ktravis_time:end:05aae454:start=1568810885605169565,finish=1568810885608972437,duration=3802872,event=rvm_use[0Ktravis_time:start:08bb3774[0Ktravis_time:end:08bb3774:start=1568810885616906165,finish=1568810885625701985,duration=8795820,event=rm_etc_boto_cfg[0Ktravis_time:start:041556c8[0Ktravis_time:end:041556c8:start=1568810885630595031,finish=1568810885633581069,duration=2986038,event=rm_oraclejdk8_symlink[0Ktravis_time:start:00ba21f0[0Ktravis_time:end:00ba21f0:start=1568810885638783034,finish=1568810885694963390,duration=56180356,event=enable_i386[0Ktravis_time:start:001b3b5e[0Ktravis_time:end:001b3b5e:start=1568810885700000634,finish=1568810885704799948,duration=4799314,event=update_rubygems[0Ktravis_time:start:2b449566[0Ktravis_time:end:2b449566:start=1568810885709661868,finish=1568810886735815628,duration=1026153760,event=ensure_path_components[0Ktravis_time:start:04de9f5a[0Ktravis_time:end:04de9f5a:start=1568810886740613190,finish=1568810886743344366,duration=2731176,event=redefine_curl[0Ktravis_time:start:0242aa9b[0Ktravis_time:end:0242aa9b:start=1568810886748384774,finish=1568810886800167823,duration=51783049,event=nonblock_pipe[0Ktravis_time:start:21414564[0Ktravis_time:end:21414564:start=1568810886805276047,finish=1568810886847547640,duration=42271593,event=apt_get_update[0Ktravis_time:start:0b13d5c4[0Ktravis_time:end:0b13d5c4:start=1568810886852248441,finish=1568810886855057371,duration=2808930,event=deprecate_xcode_64[0Ktravis_time:start:2ec25796[0Ktravis_time:end:2ec25796:start=1568810886859060682,finish=1568810891558274679,duration=4699213997,event=update_heroku[0Ktravis_time:start:180e6be3[0Ktravis_time:end:180e6be3:start=1568810891562155630,finish=1568810891565058015,duration=2902385,event=shell_session_update[0Ktravis_time:start:0f3698ab[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3834
travis_fold:end:docker_mtu[0Ktravis_time:end:0f3698ab:start=1568810891568807813,finish=1568810892767044113,duration=1198236300,event=set_docker_mtu[0Ktravis_time:start:0517cd64[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0517cd64:start=1568810892771835955,finish=1568810892839375898,duration=67539943,event=resolvconf[0Ktravis_time:start:0e99e470[0Ktravis_time:end:0e99e470:start=1568810892844623070,finish=1568810892948829128,duration=104206058,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0bb47cc0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0bb47cc0:start=1568810893031803243,finish=1568810893335740862,duration=303937619,event=configure[0Ktravis_time:start:1c11202e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:1c11202e:start=1568810893340748613,finish=1568810904646688815,duration=11305940202,event=configure[0Ktravis_time:start:02652b80[0Ktravis_fold:start:services[0Ktravis_time:start:1289b4c8[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1289b4c8:start=1568810904672180285,finish=1568810904688222489,duration=16042204,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1289b4c8:start=1568810904672180285,finish=1568810907692979577,duration=3020799292,event=services[0Ktravis_time:start:0107f1f3[0Ktravis_time:end:0107f1f3:start=1568810907697911157,finish=1568810907700738680,duration=2827523,event=fix_ps4[0Ktravis_time:start:2f49dfb6[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0bef633f[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0bef633f:start=1568810907709746669,finish=1568810917998403027,duration=10288656358,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:12f2e010[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:12f2e010:start=1568810918003100095,finish=1568810918438861644,duration=435761549,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:12f2e010:start=1568810918003100095,finish=1568810919394812661,duration=1391712566,event=checkout[0Ktravis_time:start:0518a3ac[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0518a3ac:start=1568810919399530134,finish=1568810919411309988,duration=11779854,event=env[0Ktravis_time:start:01633cad[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:01633cad:start=1568810919416457112,finish=1568810919423213094,duration=6755982,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:09584c5e[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,dealii-of,of-ccx_fsi,fe-fe,of-ccx,of-of,nutils-of,bindings,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:09584c5e:start=1568810919782518450,finish=1568810919850732702,duration=68214252,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:046ce78e[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478306/log.txt)