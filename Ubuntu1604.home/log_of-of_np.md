 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586479648) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/51ea4812093d...cd89b1900540) 
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
travis_time:end:12ab4349:start=1568813094748856986,finish=1568813094756019457,duration=7162471,event=show_system_info[0Ktravis_time:start:07bd06b0[0Ktravis_time:end:07bd06b0:start=1568813094759244497,finish=1568813094785733256,duration=26488759,event=rm_riak_source[0Ktravis_time:start:0fe53440[0Ktravis_time:end:0fe53440:start=1568813094788959503,finish=1568813094794253091,duration=5293588,event=fix_rwky_redis[0Ktravis_time:start:2275d27c[0Ktravis_time:end:2275d27c:start=1568813094797247863,finish=1568813095208013237,duration=410765374,event=wait_for_network[0Ktravis_time:start:108a2333[0Ktravis_time:end:108a2333:start=1568813095212167165,finish=1568813096818273883,duration=1606106718,event=update_apt_keys[0Ktravis_time:start:0bd8cf44[0Ktravis_time:end:0bd8cf44:start=1568813096823458940,finish=1568813097988749268,duration=1165290328,event=fix_hhvm_source[0Ktravis_time:start:08510892[0Ktravis_time:end:08510892:start=1568813097994425524,finish=1568813098007395825,duration=12970301,event=update_mongo_arch[0Ktravis_time:start:0ca60494[0Ktravis_time:end:0ca60494:start=1568813098012517473,finish=1568813098064085211,duration=51567738,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2da41195[0Ktravis_time:end:2da41195:start=1568813098069549954,finish=1568813098073095890,duration=3545936,event=update_glibc[0Ktravis_time:start:1491d18b[0Ktravis_time:end:1491d18b:start=1568813098078328653,finish=1568813098089951467,duration=11622814,event=clean_up_path[0Ktravis_time:start:0165a260[0Ktravis_time:end:0165a260:start=1568813098095204855,finish=1568813098107545012,duration=12340157,event=fix_resolv_conf[0Ktravis_time:start:2cb8561a[0Ktravis_time:end:2cb8561a:start=1568813098114176793,finish=1568813098127684453,duration=13507660,event=fix_etc_hosts[0Ktravis_time:start:0a80904b[0Ktravis_time:end:0a80904b:start=1568813098133850797,finish=1568813098146538919,duration=12688122,event=fix_mvn_settings_xml[0Ktravis_time:start:04a2fce8[0Ktravis_time:end:04a2fce8:start=1568813098151805145,finish=1568813098164993546,duration=13188401,event=no_ipv6_localhost[0Ktravis_time:start:0ac17bfc[0Ktravis_time:end:0ac17bfc:start=1568813098170710715,finish=1568813098174647176,duration=3936461,event=fix_etc_mavenrc[0Ktravis_time:start:1479da0b[0Ktravis_time:end:1479da0b:start=1568813098180794605,finish=1568813098185308365,duration=4513760,event=fix_wwdr_certificate[0Ktravis_time:start:16693f1b[0Ktravis_time:end:16693f1b:start=1568813098193396621,finish=1568813098225963366,duration=32566745,event=put_localhost_first[0Ktravis_time:start:1c0ed3e1[0Ktravis_time:end:1c0ed3e1:start=1568813098233888254,finish=1568813098238924575,duration=5036321,event=home_paths[0Ktravis_time:start:1ab1ecbe[0Ktravis_time:end:1ab1ecbe:start=1568813098244480626,finish=1568813098260757733,duration=16277107,event=disable_initramfs[0Ktravis_time:start:02da991a[0Ktravis_time:end:02da991a:start=1568813098267008408,finish=1568813098645139079,duration=378130671,event=disable_ssh_roaming[0Ktravis_time:start:39e35191[0Ktravis_time:end:39e35191:start=1568813098649902846,finish=1568813098652765430,duration=2862584,event=debug_tools[0Ktravis_time:start:11342283[0Ktravis_time:end:11342283:start=1568813098657594611,finish=1568813098661348984,duration=3754373,event=uninstall_oclint[0Ktravis_time:start:093e24f8[0Ktravis_time:end:093e24f8:start=1568813098666168009,finish=1568813098670957057,duration=4789048,event=rvm_use[0Ktravis_time:start:0c8a2c7f[0Ktravis_time:end:0c8a2c7f:start=1568813098676173557,finish=1568813098685465115,duration=9291558,event=rm_etc_boto_cfg[0Ktravis_time:start:3768b500[0Ktravis_time:end:3768b500:start=1568813098692057855,finish=1568813098695121665,duration=3063810,event=rm_oraclejdk8_symlink[0Ktravis_time:start:01f0fce0[0Ktravis_time:end:01f0fce0:start=1568813098700034322,finish=1568813098758209194,duration=58174872,event=enable_i386[0Ktravis_time:start:097f99c1[0Ktravis_time:end:097f99c1:start=1568813098763048487,finish=1568813098768338631,duration=5290144,event=update_rubygems[0Ktravis_time:start:012b81ac[0Ktravis_time:end:012b81ac:start=1568813098772828193,finish=1568813099827743920,duration=1054915727,event=ensure_path_components[0Ktravis_time:start:015a01d8[0Ktravis_time:end:015a01d8:start=1568813099832357837,finish=1568813099835328488,duration=2970651,event=redefine_curl[0Ktravis_time:start:009eab0a[0Ktravis_time:end:009eab0a:start=1568813099840647724,finish=1568813099898026565,duration=57378841,event=nonblock_pipe[0Ktravis_time:start:11d687f0[0Ktravis_time:end:11d687f0:start=1568813099903409855,finish=1568813099972864467,duration=69454612,event=apt_get_update[0Ktravis_time:start:0089053d[0Ktravis_time:end:0089053d:start=1568813099978321448,finish=1568813099981767936,duration=3446488,event=deprecate_xcode_64[0Ktravis_time:start:0e09c0af[0Ktravis_time:end:0e09c0af:start=1568813099987356937,finish=1568813105152381762,duration=5165024825,event=update_heroku[0Ktravis_time:start:0c31efbb[0Ktravis_time:end:0c31efbb:start=1568813105156895167,finish=1568813105160160920,duration=3265753,event=shell_session_update[0Ktravis_time:start:1f6a3e38[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3935
travis_fold:end:docker_mtu[0Ktravis_time:end:1f6a3e38:start=1568813105164545789,finish=1568813106368074365,duration=1203528576,event=set_docker_mtu[0Ktravis_time:start:0dc7ae45[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0dc7ae45:start=1568813106373893772,finish=1568813106443799954,duration=69906182,event=resolvconf[0Ktravis_time:start:038c46d0[0Ktravis_time:end:038c46d0:start=1568813106448443823,finish=1568813106553622809,duration=105178986,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:08fdc2b4[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:08fdc2b4:start=1568813106637815449,finish=1568813106978833870,duration=341018421,event=configure[0Ktravis_time:start:0e87aeaa[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0e87aeaa:start=1568813106984379273,finish=1568813118552964412,duration=11568585139,event=configure[0Ktravis_time:start:01dbd300[0Ktravis_fold:start:services[0Ktravis_time:start:0f38cc16[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0f38cc16:start=1568813118578855983,finish=1568813118594138861,duration=15282878,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0f38cc16:start=1568813118578855983,finish=1568813121600149633,duration=3021293650,event=services[0Ktravis_time:start:28a88f22[0Ktravis_time:end:28a88f22:start=1568813121605491490,finish=1568813121608808889,duration=3317399,event=fix_ps4[0Ktravis_time:start:194a9c13[0K
travis_fold:start:git.checkout[0Ktravis_time:start:00fbf59a[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:00fbf59a:start=1568813121617895136,finish=1568813132515527907,duration=10897632771,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf cd89b1900540505af8c571183bfc09ad56bacb7b
travis_fold:end:git.checkout[0K
travis_time:end:00fbf59a:start=1568813121617895136,finish=1568813133015626623,duration=11397731487,event=checkout[0Ktravis_time:start:133d9638[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:133d9638:start=1568813133020381506,finish=1568813133032215448,duration=11833942,event=env[0Ktravis_time:start:39ecf304[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:39ecf304:start=1568813133036878946,finish=1568813133166592868,duration=129713922,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:32a2a19e[0K$ python system_testing.py -s of-of_np
usage: system_testing.py [-h] [-l] -s
                         {bindings,of-of,fe-fe,of-ccx,su2-ccx,nutils-of,of-of_np,of-ccx_fsi,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:32a2a19e:start=1568813133726654951,finish=1568813133798952049,duration=72297098,event=script[0K[31;1mThe command "python system_testing.py -s of-of_np" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0b8b7290[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586479680/log.txt)