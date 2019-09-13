 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/584619352) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/3433ca666766...b4f731a5d60e) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
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
travis_time:end:108c9082:start=1568391593463119086,finish=1568391593469623025,duration=6503939,event=show_system_info[0Ktravis_time:start:02139f31[0Ktravis_time:end:02139f31:start=1568391593472587056,finish=1568391593500141146,duration=27554090,event=rm_riak_source[0Ktravis_time:start:05c036d0[0Ktravis_time:end:05c036d0:start=1568391593503321450,finish=1568391593508580906,duration=5259456,event=fix_rwky_redis[0Ktravis_time:start:00424c71[0Ktravis_time:end:00424c71:start=1568391593511557655,finish=1568391594146238188,duration=634680533,event=wait_for_network[0Ktravis_time:start:081537c0[0Ktravis_time:end:081537c0:start=1568391594150232165,finish=1568391595102469539,duration=952237374,event=update_apt_keys[0Ktravis_time:start:006e82a2[0Ktravis_time:end:006e82a2:start=1568391595107237286,finish=1568391596208095196,duration=1100857910,event=fix_hhvm_source[0Ktravis_time:start:3216cf89[0Ktravis_time:end:3216cf89:start=1568391596214041249,finish=1568391596224886447,duration=10845198,event=update_mongo_arch[0Ktravis_time:start:06ab5322[0Ktravis_time:end:06ab5322:start=1568391596231171089,finish=1568391596273504859,duration=42333770,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0dbed4e0[0Ktravis_time:end:0dbed4e0:start=1568391596278368423,finish=1568391596281693349,duration=3324926,event=update_glibc[0Ktravis_time:start:0ec151ac[0Ktravis_time:end:0ec151ac:start=1568391596286053457,finish=1568391596299412498,duration=13359041,event=clean_up_path[0Ktravis_time:start:1c784f50[0Ktravis_time:end:1c784f50:start=1568391596303769985,finish=1568391596315170036,duration=11400051,event=fix_resolv_conf[0Ktravis_time:start:02460360[0Ktravis_time:end:02460360:start=1568391596319638968,finish=1568391596331528000,duration=11889032,event=fix_etc_hosts[0Ktravis_time:start:06da487c[0Ktravis_time:end:06da487c:start=1568391596336747517,finish=1568391596347199815,duration=10452298,event=fix_mvn_settings_xml[0Ktravis_time:start:1ccf27ef[0Ktravis_time:end:1ccf27ef:start=1568391596352429621,finish=1568391596363400869,duration=10971248,event=no_ipv6_localhost[0Ktravis_time:start:0158e8d8[0Ktravis_time:end:0158e8d8:start=1568391596368427499,finish=1568391596371423419,duration=2995920,event=fix_etc_mavenrc[0Ktravis_time:start:2165f1ad[0Ktravis_time:end:2165f1ad:start=1568391596376731781,finish=1568391596380810269,duration=4078488,event=fix_wwdr_certificate[0Ktravis_time:start:0a02df24[0Ktravis_time:end:0a02df24:start=1568391596385974750,finish=1568391596408847551,duration=22872801,event=put_localhost_first[0Ktravis_time:start:02a4c476[0Ktravis_time:end:02a4c476:start=1568391596412960004,finish=1568391596416629778,duration=3669774,event=home_paths[0Ktravis_time:start:07a72bf8[0Ktravis_time:end:07a72bf8:start=1568391596421514869,finish=1568391596434782641,duration=13267772,event=disable_initramfs[0Ktravis_time:start:0e4931d6[0Ktravis_time:end:0e4931d6:start=1568391596439081130,finish=1568391596805726837,duration=366645707,event=disable_ssh_roaming[0Ktravis_time:start:2e689ce5[0Ktravis_time:end:2e689ce5:start=1568391596809824075,finish=1568391596812444706,duration=2620631,event=debug_tools[0Ktravis_time:start:069c41d0[0Ktravis_time:end:069c41d0:start=1568391596816919668,finish=1568391596821592492,duration=4672824,event=uninstall_oclint[0Ktravis_time:start:09a83e25[0Ktravis_time:end:09a83e25:start=1568391596825984854,finish=1568391596829516374,duration=3531520,event=rvm_use[0Ktravis_time:start:0cfa4024[0Ktravis_time:end:0cfa4024:start=1568391596833427570,finish=1568391596842333217,duration=8905647,event=rm_etc_boto_cfg[0Ktravis_time:start:0d668267[0Ktravis_time:end:0d668267:start=1568391596846479905,finish=1568391596849097123,duration=2617218,event=rm_oraclejdk8_symlink[0Ktravis_time:start:024ab372[0Ktravis_time:end:024ab372:start=1568391596853398635,finish=1568391596907025288,duration=53626653,event=enable_i386[0Ktravis_time:start:2b439750[0Ktravis_time:end:2b439750:start=1568391596912579669,finish=1568391596917177843,duration=4598174,event=update_rubygems[0Ktravis_time:start:132b9bf8[0Ktravis_time:end:132b9bf8:start=1568391596922001217,finish=1568391597949723273,duration=1027722056,event=ensure_path_components[0Ktravis_time:start:2c445618[0Ktravis_time:end:2c445618:start=1568391597954463806,finish=1568391597957344115,duration=2880309,event=redefine_curl[0Ktravis_time:start:09a9f197[0Ktravis_time:end:09a9f197:start=1568391597961772350,finish=1568391598017103133,duration=55330783,event=nonblock_pipe[0Ktravis_time:start:12d4e056[0Ktravis_time:end:12d4e056:start=1568391598021338145,finish=1568391598062373849,duration=41035704,event=apt_get_update[0Ktravis_time:start:0be25fa1[0Ktravis_time:end:0be25fa1:start=1568391598066921612,finish=1568391598070059096,duration=3137484,event=deprecate_xcode_64[0Ktravis_time:start:1822a52e[0Ktravis_time:end:1822a52e:start=1568391598075196141,finish=1568391603168711365,duration=5093515224,event=update_heroku[0Ktravis_time:start:2a8e29d2[0Ktravis_time:end:2a8e29d2:start=1568391603173498327,finish=1568391603177025493,duration=3527166,event=shell_session_update[0Ktravis_time:start:09558c54[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3833
travis_fold:end:docker_mtu[0Ktravis_time:end:09558c54:start=1568391603181486818,finish=1568391604383553182,duration=1202066364,event=set_docker_mtu[0Ktravis_time:start:082b4e77[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:082b4e77:start=1568391604387688706,finish=1568391604457166064,duration=69477358,event=resolvconf[0Ktravis_time:start:000c3fa5[0Ktravis_time:end:000c3fa5:start=1568391604462293863,finish=1568391604570218261,duration=107924398,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:12559322[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:12559322:start=1568391604653198782,finish=1568391605222796827,duration=569598045,event=configure[0Ktravis_time:start:0d00b8a3[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d00b8a3:start=1568391605227858053,finish=1568391614886106377,duration=9658248324,event=configure[0Ktravis_time:start:22c28940[0Ktravis_fold:start:services[0Ktravis_time:start:0cb67b04[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0cb67b04:start=1568391614913349181,finish=1568391614930045860,duration=16696679,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0cb67b04:start=1568391614913349181,finish=1568391617935182525,duration=3021833344,event=services[0Ktravis_time:start:26598801[0Ktravis_time:end:26598801:start=1568391617939333500,finish=1568391617942182397,duration=2848897,event=fix_ps4[0Ktravis_time:start:1d7238c0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:25e663f6[0K$ git clone --depth=50 --branch=code_aster_adapter https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:25e663f6:start=1568391617949977353,finish=1568391627993630226,duration=10043652873,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf b4f731a5d60e7af97ee48400e5c51e279cd9f34f
travis_fold:end:git.checkout[0K
travis_time:end:25e663f6:start=1568391617949977353,finish=1568391628945412872,duration=10995435519,event=checkout[0Ktravis_time:start:0336f57e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0336f57e:start=1568391628951012450,finish=1568391628961627591,duration=10615141,event=env[0Ktravis_time:start:0fe96754[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0fe96754:start=1568391628966930300,finish=1568391628979554886,duration=12624586,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:101dcd8c[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {nutils-of,fe-fe,dealii-of,su2-ccx,of-of,of-ccx_fsi,of-ccx,bindings,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:101dcd8c:start=1568391629323254568,finish=1568391629389570804,duration=66316236,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:15afbc3c[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/584619366/log.txt)