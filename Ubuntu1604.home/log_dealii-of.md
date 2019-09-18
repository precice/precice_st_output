 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586478286) 
## Triggered by: [pull_request](https://github.com/precice/systemtests/pull/96) 
## Last succesfull commits 
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1)
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
travis_time:end:19b4af18:start=1568810765292116351,finish=1568810765298505499,duration=6389148,event=show_system_info[0Ktravis_time:start:0e911000[0Ktravis_time:end:0e911000:start=1568810765301462439,finish=1568810765325549807,duration=24087368,event=rm_riak_source[0Ktravis_time:start:0542f6f7[0Ktravis_time:end:0542f6f7:start=1568810765329325022,finish=1568810765335311967,duration=5986945,event=fix_rwky_redis[0Ktravis_time:start:3a410de6[0Ktravis_time:end:3a410de6:start=1568810765338717162,finish=1568810765730623737,duration=391906575,event=wait_for_network[0Ktravis_time:start:00a7411d[0Ktravis_time:end:00a7411d:start=1568810765735423856,finish=1568810767278615455,duration=1543191599,event=update_apt_keys[0Ktravis_time:start:07ef3438[0Ktravis_time:end:07ef3438:start=1568810767283864974,finish=1568810768334185235,duration=1050320261,event=fix_hhvm_source[0Ktravis_time:start:03107ac0[0Ktravis_time:end:03107ac0:start=1568810768339105087,finish=1568810768349613573,duration=10508486,event=update_mongo_arch[0Ktravis_time:start:18c7798e[0Ktravis_time:end:18c7798e:start=1568810768354189599,finish=1568810768398256530,duration=44066931,event=fix_sudo_enabled_trusty[0Ktravis_time:start:11682cc8[0Ktravis_time:end:11682cc8:start=1568810768402982165,finish=1568810768407425030,duration=4442865,event=update_glibc[0Ktravis_time:start:00715bec[0Ktravis_time:end:00715bec:start=1568810768411979186,finish=1568810768420736778,duration=8757592,event=clean_up_path[0Ktravis_time:start:0f574ad0[0Ktravis_time:end:0f574ad0:start=1568810768425168405,finish=1568810768434787576,duration=9619171,event=fix_resolv_conf[0Ktravis_time:start:0d69c220[0Ktravis_time:end:0d69c220:start=1568810768439161285,finish=1568810768449678462,duration=10517177,event=fix_etc_hosts[0Ktravis_time:start:04817d27[0Ktravis_time:end:04817d27:start=1568810768454053038,finish=1568810768463673409,duration=9620371,event=fix_mvn_settings_xml[0Ktravis_time:start:06210a34[0Ktravis_time:end:06210a34:start=1568810768468479791,finish=1568810768478994286,duration=10514495,event=no_ipv6_localhost[0Ktravis_time:start:150cf6b6[0Ktravis_time:end:150cf6b6:start=1568810768483721280,finish=1568810768486839319,duration=3118039,event=fix_etc_mavenrc[0Ktravis_time:start:1c907358[0Ktravis_time:end:1c907358:start=1568810768492837234,finish=1568810768496948814,duration=4111580,event=fix_wwdr_certificate[0Ktravis_time:start:0af93098[0Ktravis_time:end:0af93098:start=1568810768501916149,finish=1568810768527360318,duration=25444169,event=put_localhost_first[0Ktravis_time:start:152fd0d0[0Ktravis_time:end:152fd0d0:start=1568810768532273527,finish=1568810768535885778,duration=3612251,event=home_paths[0Ktravis_time:start:08e57b77[0Ktravis_time:end:08e57b77:start=1568810768540308549,finish=1568810768553260840,duration=12952291,event=disable_initramfs[0Ktravis_time:start:0a6a6fb0[0Ktravis_time:end:0a6a6fb0:start=1568810768558228967,finish=1568810768882009867,duration=323780900,event=disable_ssh_roaming[0Ktravis_time:start:09cbf3ff[0Ktravis_time:end:09cbf3ff:start=1568810768886436967,finish=1568810768889520973,duration=3084006,event=debug_tools[0Ktravis_time:start:13adecf7[0Ktravis_time:end:13adecf7:start=1568810768894120002,finish=1568810768898874888,duration=4754886,event=uninstall_oclint[0Ktravis_time:start:07c082e8[0Ktravis_time:end:07c082e8:start=1568810768903398512,finish=1568810768907777177,duration=4378665,event=rvm_use[0Ktravis_time:start:0114a993[0Ktravis_time:end:0114a993:start=1568810768915072017,finish=1568810768923579214,duration=8507197,event=rm_etc_boto_cfg[0Ktravis_time:start:0ec56024[0Ktravis_time:end:0ec56024:start=1568810768928995755,finish=1568810768931797845,duration=2802090,event=rm_oraclejdk8_symlink[0Ktravis_time:start:068e2aa0[0Ktravis_time:end:068e2aa0:start=1568810768936366304,finish=1568810768992994943,duration=56628639,event=enable_i386[0Ktravis_time:start:064997ee[0Ktravis_time:end:064997ee:start=1568810768997668520,finish=1568810769002123799,duration=4455279,event=update_rubygems[0Ktravis_time:start:04e477fe[0Ktravis_time:end:04e477fe:start=1568810769006434750,finish=1568810770023920732,duration=1017485982,event=ensure_path_components[0Ktravis_time:start:0840e700[0Ktravis_time:end:0840e700:start=1568810770029185129,finish=1568810770032162434,duration=2977305,event=redefine_curl[0Ktravis_time:start:22405080[0Ktravis_time:end:22405080:start=1568810770036802155,finish=1568810770089788365,duration=52986210,event=nonblock_pipe[0Ktravis_time:start:241797ae[0Ktravis_time:end:241797ae:start=1568810770094519811,finish=1568810770136645203,duration=42125392,event=apt_get_update[0Ktravis_time:start:0ee07a64[0Ktravis_time:end:0ee07a64:start=1568810770141265185,finish=1568810770144033606,duration=2768421,event=deprecate_xcode_64[0Ktravis_time:start:0ef978e8[0Ktravis_time:end:0ef978e8:start=1568810770149270649,finish=1568810774828394387,duration=4679123738,event=update_heroku[0Ktravis_time:start:0759cb46[0Ktravis_time:end:0759cb46:start=1568810774833318919,finish=1568810774836046628,duration=2727709,event=shell_session_update[0Ktravis_time:start:190bbc6f[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3830
travis_fold:end:docker_mtu[0Ktravis_time:end:190bbc6f:start=1568810774840541730,finish=1568810776034894334,duration=1194352604,event=set_docker_mtu[0Ktravis_time:start:12d8f074[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:12d8f074:start=1568810776039807938,finish=1568810776108951090,duration=69143152,event=resolvconf[0Ktravis_time:start:1533b007[0Ktravis_time:end:1533b007:start=1568810776114410205,finish=1568810776211359330,duration=96949125,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0f3949c4[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0f3949c4:start=1568810776294417612,finish=1568810776623710091,duration=329292479,event=configure[0Ktravis_time:start:00a23432[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:00a23432:start=1568810776628400290,finish=1568810786645681646,duration=10017281356,event=configure[0Ktravis_time:start:300dcfdc[0Ktravis_fold:start:services[0Ktravis_time:start:0c9510d2[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0c9510d2:start=1568810786671446167,finish=1568810786685954013,duration=14507846,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0c9510d2:start=1568810786671446167,finish=1568810789691025947,duration=3019579780,event=services[0Ktravis_time:start:00292eba[0Ktravis_time:end:00292eba:start=1568810789695898010,finish=1568810789698957608,duration=3059598,event=fix_ps4[0Ktravis_time:start:0d1e05d8[0K
travis_fold:start:git.checkout[0Ktravis_time:start:08262d47[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:08262d47:start=1568810789707739530,finish=1568810800456950422,duration=10749210892,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:24d47734[0K$ git fetch origin +refs/pull/96/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/96/merge -> FETCH_HEAD
travis_time:end:24d47734:start=1568810800461642760,finish=1568810800885376343,duration=423733583,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:24d47734:start=1568810800461642760,finish=1568810801276862747,duration=815219987,event=checkout[0Ktravis_time:start:2af26214[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:2af26214:start=1568810801281639985,finish=1568810801293359821,duration=11719836,event=env[0Ktravis_time:start:1572f243[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1572f243:start=1568810801299196995,finish=1568810801304976608,duration=5779613,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:06b70abe[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {of-of,nutils-of,of-ccx,bindings,of-of_np,su2-ccx,dealii-of,fe-fe,of-ccx_fsi}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:06b70abe:start=1568810801652371656,finish=1568810801717590941,duration=65219285,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0838554e[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586478304/log.txt)