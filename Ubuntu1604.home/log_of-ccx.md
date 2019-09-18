 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586479648) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/51ea4812093d...cd89b1900540) 
## Last succesfull commits 
* [calculix-adapter](https://github.com/precice/calculix-adapter/compare/147c091b83fb...59e06f11ba72)
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
travis_time:end:1f3c8a74:start=1568812805135027842,finish=1568812805142124104,duration=7096262,event=show_system_info[0Ktravis_time:start:01700dc6[0Ktravis_time:end:01700dc6:start=1568812805145539706,finish=1568812805175900495,duration=30360789,event=rm_riak_source[0Ktravis_time:start:0e1a31c0[0Ktravis_time:end:0e1a31c0:start=1568812805179504952,finish=1568812805185405779,duration=5900827,event=fix_rwky_redis[0Ktravis_time:start:10c1cb62[0Ktravis_time:end:10c1cb62:start=1568812805188770678,finish=1568812805591124742,duration=402354064,event=wait_for_network[0Ktravis_time:start:2b80f53d[0Ktravis_time:end:2b80f53d:start=1568812805596541053,finish=1568812806696643161,duration=1100102108,event=update_apt_keys[0Ktravis_time:start:11862bc4[0Ktravis_time:end:11862bc4:start=1568812806702808723,finish=1568812807855254129,duration=1152445406,event=fix_hhvm_source[0Ktravis_time:start:00106bc0[0Ktravis_time:end:00106bc0:start=1568812807859761705,finish=1568812807870857279,duration=11095574,event=update_mongo_arch[0Ktravis_time:start:16452c00[0Ktravis_time:end:16452c00:start=1568812807874877956,finish=1568812807922584074,duration=47706118,event=fix_sudo_enabled_trusty[0Ktravis_time:start:064e570b[0Ktravis_time:end:064e570b:start=1568812807928064030,finish=1568812807931362383,duration=3298353,event=update_glibc[0Ktravis_time:start:009419fa[0Ktravis_time:end:009419fa:start=1568812807937458019,finish=1568812807947317181,duration=9859162,event=clean_up_path[0Ktravis_time:start:08076588[0Ktravis_time:end:08076588:start=1568812807952167213,finish=1568812807961577358,duration=9410145,event=fix_resolv_conf[0Ktravis_time:start:11fbe7ba[0Ktravis_time:end:11fbe7ba:start=1568812807966570601,finish=1568812807977125479,duration=10554878,event=fix_etc_hosts[0Ktravis_time:start:0f181ead[0Ktravis_time:end:0f181ead:start=1568812807982270051,finish=1568812807992682544,duration=10412493,event=fix_mvn_settings_xml[0Ktravis_time:start:07370e0b[0Ktravis_time:end:07370e0b:start=1568812807997437077,finish=1568812808009304736,duration=11867659,event=no_ipv6_localhost[0Ktravis_time:start:185c83b2[0Ktravis_time:end:185c83b2:start=1568812808014179547,finish=1568812808017609267,duration=3429720,event=fix_etc_mavenrc[0Ktravis_time:start:04d02e31[0Ktravis_time:end:04d02e31:start=1568812808022350731,finish=1568812808027880904,duration=5530173,event=fix_wwdr_certificate[0Ktravis_time:start:19348353[0Ktravis_time:end:19348353:start=1568812808033515075,finish=1568812808061627576,duration=28112501,event=put_localhost_first[0Ktravis_time:start:017812db[0Ktravis_time:end:017812db:start=1568812808067773088,finish=1568812808071816984,duration=4043896,event=home_paths[0Ktravis_time:start:04cb808c[0Ktravis_time:end:04cb808c:start=1568812808077248724,finish=1568812808092649276,duration=15400552,event=disable_initramfs[0Ktravis_time:start:06c68e88[0Ktravis_time:end:06c68e88:start=1568812808097744076,finish=1568812808444987006,duration=347242930,event=disable_ssh_roaming[0Ktravis_time:start:08f60e7a[0Ktravis_time:end:08f60e7a:start=1568812808450948625,finish=1568812808454175754,duration=3227129,event=debug_tools[0Ktravis_time:start:0b232246[0Ktravis_time:end:0b232246:start=1568812808458739977,finish=1568812808463418727,duration=4678750,event=uninstall_oclint[0Ktravis_time:start:030fb41f[0Ktravis_time:end:030fb41f:start=1568812808471203381,finish=1568812808475501856,duration=4298475,event=rvm_use[0Ktravis_time:start:00439e9e[0Ktravis_time:end:00439e9e:start=1568812808480551734,finish=1568812808490794945,duration=10243211,event=rm_etc_boto_cfg[0Ktravis_time:start:0828cd78[0Ktravis_time:end:0828cd78:start=1568812808496689682,finish=1568812808500092769,duration=3403087,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0ac0db08[0Ktravis_time:end:0ac0db08:start=1568812808506348467,finish=1568812808576839441,duration=70490974,event=enable_i386[0Ktravis_time:start:017a2298[0Ktravis_time:end:017a2298:start=1568812808583814468,finish=1568812808589751900,duration=5937432,event=update_rubygems[0Ktravis_time:start:04ab6a22[0Ktravis_time:end:04ab6a22:start=1568812808595564713,finish=1568812809741750822,duration=1146186109,event=ensure_path_components[0Ktravis_time:start:029f8618[0Ktravis_time:end:029f8618:start=1568812809749631701,finish=1568812809752865849,duration=3234148,event=redefine_curl[0Ktravis_time:start:0c405475[0Ktravis_time:end:0c405475:start=1568812809758463102,finish=1568812809821236565,duration=62773463,event=nonblock_pipe[0Ktravis_time:start:3ac0b0cc[0Ktravis_time:end:3ac0b0cc:start=1568812809826544426,finish=1568812809883005497,duration=56461071,event=apt_get_update[0Ktravis_time:start:074796de[0Ktravis_time:end:074796de:start=1568812809888468588,finish=1568812809891715954,duration=3247366,event=deprecate_xcode_64[0Ktravis_time:start:13a7c760[0Ktravis_time:end:13a7c760:start=1568812809896865178,finish=1568812815349526089,duration=5452660911,event=update_heroku[0Ktravis_time:start:083bcb2a[0Ktravis_time:end:083bcb2a:start=1568812815354842490,finish=1568812815358157673,duration=3315183,event=shell_session_update[0Ktravis_time:start:16445585[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3937
travis_fold:end:docker_mtu[0Ktravis_time:end:16445585:start=1568812815362906315,finish=1568812816565843483,duration=1202937168,event=set_docker_mtu[0Ktravis_time:start:113ae00c[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:113ae00c:start=1568812816571204662,finish=1568812816649788677,duration=78584015,event=resolvconf[0Ktravis_time:start:05d65cd6[0Ktravis_time:end:05d65cd6:start=1568812816656123373,finish=1568812816786256127,duration=130132754,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:3d893db0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:3d893db0:start=1568812816884314754,finish=1568812817260892320,duration=376577566,event=configure[0Ktravis_time:start:041727c6[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:041727c6:start=1568812817267055024,finish=1568812834154225399,duration=16887170375,event=configure[0Ktravis_time:start:0b61a814[0Ktravis_fold:start:services[0Ktravis_time:start:257faa56[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:257faa56:start=1568812834183402477,finish=1568812834200049638,duration=16647161,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:257faa56:start=1568812834183402477,finish=1568812837206657512,duration=3023255035,event=services[0Ktravis_time:start:08ef0bfc[0Ktravis_time:end:08ef0bfc:start=1568812837212252063,finish=1568812837215203219,duration=2951156,event=fix_ps4[0Ktravis_time:start:1bdf73e0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0ca3e036[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0ca3e036:start=1568812837224165556,finish=1568812848509869474,duration=11285703918,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf cd89b1900540505af8c571183bfc09ad56bacb7b
travis_fold:end:git.checkout[0K
travis_time:end:0ca3e036:start=1568812837224165556,finish=1568812848964268726,duration=11740103170,event=checkout[0Ktravis_time:start:05afa53c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:05afa53c:start=1568812848973237476,finish=1568812848987622390,duration=14384914,event=env[0Ktravis_time:start:25c79a6c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:25c79a6c:start=1568812848994426801,finish=1568812849003964298,duration=9537497,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:1ce17b58[0K$ python system_testing.py -s of-ccx
usage: system_testing.py [-h] [-l] -s
                         {of-of,nutils-of,of-ccx_fsi,bindings,fe-fe,dealii-of,of-ccx,of-of_np,su2-ccx}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:1ce17b58:start=1568812849448160860,finish=1568812849532558885,duration=84398025,event=script[0K[31;1mThe command "python system_testing.py -s of-ccx" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:016964b0[0K$ python push.py -t of-ccx
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586479674/log.txt)