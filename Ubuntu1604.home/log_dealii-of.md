 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586515488) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/28722fe13705...2efb54a69d10) 
## Last succesfull commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/6dc2f7a30a5a...e0bf66da1bdf)
* [systemtests](https://github.com/precice/systemtests/compare/54b96c7718c6c434cfc8b2262d3057a82de97903...51ea4812093d2ae31257f4fbeb796550d815c6ef)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/436446ec1401fb5693dc0df2b718330ca26744f9...71eeed0aa3ca179a906793d59f6576c8e42850c1) 
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
travis_time:end:130d53eb:start=1568819496621231877,finish=1568819496627603492,duration=6371615,event=show_system_info[0Ktravis_time:start:116236c5[0Ktravis_time:end:116236c5:start=1568819496630733072,finish=1568819496659090256,duration=28357184,event=rm_riak_source[0Ktravis_time:start:0d18562f[0Ktravis_time:end:0d18562f:start=1568819496662292633,finish=1568819496667885507,duration=5592874,event=fix_rwky_redis[0Ktravis_time:start:14b9daf0[0Ktravis_time:end:14b9daf0:start=1568819496671083436,finish=1568819497036407952,duration=365324516,event=wait_for_network[0Ktravis_time:start:15b11a94[0Ktravis_time:end:15b11a94:start=1568819497040257837,finish=1568819498196155939,duration=1155898102,event=update_apt_keys[0Ktravis_time:start:05d4e485[0Ktravis_time:end:05d4e485:start=1568819498202390153,finish=1568819499325828059,duration=1123437906,event=fix_hhvm_source[0Ktravis_time:start:03721793[0Ktravis_time:end:03721793:start=1568819499330848084,finish=1568819499341002617,duration=10154533,event=update_mongo_arch[0Ktravis_time:start:0ad8bdbc[0Ktravis_time:end:0ad8bdbc:start=1568819499345574615,finish=1568819499388864184,duration=43289569,event=fix_sudo_enabled_trusty[0Ktravis_time:start:2cc7bfdc[0Ktravis_time:end:2cc7bfdc:start=1568819499393461970,finish=1568819499396885855,duration=3423885,event=update_glibc[0Ktravis_time:start:3cad7bb8[0Ktravis_time:end:3cad7bb8:start=1568819499401548853,finish=1568819499414280490,duration=12731637,event=clean_up_path[0Ktravis_time:start:1e248e17[0Ktravis_time:end:1e248e17:start=1568819499418837999,finish=1568819499432607326,duration=13769327,event=fix_resolv_conf[0Ktravis_time:start:0416e938[0Ktravis_time:end:0416e938:start=1568819499437506374,finish=1568819499447305541,duration=9799167,event=fix_etc_hosts[0Ktravis_time:start:03b20c6e[0Ktravis_time:end:03b20c6e:start=1568819499452881177,finish=1568819499462274878,duration=9393701,event=fix_mvn_settings_xml[0Ktravis_time:start:06d890f7[0Ktravis_time:end:06d890f7:start=1568819499467111968,finish=1568819499477288290,duration=10176322,event=no_ipv6_localhost[0Ktravis_time:start:0d3f045a[0Ktravis_time:end:0d3f045a:start=1568819499482190500,finish=1568819499485325808,duration=3135308,event=fix_etc_mavenrc[0Ktravis_time:start:1c21e448[0Ktravis_time:end:1c21e448:start=1568819499489719501,finish=1568819499494754073,duration=5034572,event=fix_wwdr_certificate[0Ktravis_time:start:1297de22[0Ktravis_time:end:1297de22:start=1568819499499710025,finish=1568819499524669723,duration=24959698,event=put_localhost_first[0Ktravis_time:start:0fbe80c0[0Ktravis_time:end:0fbe80c0:start=1568819499529857822,finish=1568819499534065629,duration=4207807,event=home_paths[0Ktravis_time:start:1051f9a9[0Ktravis_time:end:1051f9a9:start=1568819499539511343,finish=1568819499552840878,duration=13329535,event=disable_initramfs[0Ktravis_time:start:0a705ccc[0Ktravis_time:end:0a705ccc:start=1568819499558601363,finish=1568819499933052865,duration=374451502,event=disable_ssh_roaming[0Ktravis_time:start:090856b5[0Ktravis_time:end:090856b5:start=1568819499938331807,finish=1568819499941470076,duration=3138269,event=debug_tools[0Ktravis_time:start:1c67064c[0Ktravis_time:end:1c67064c:start=1568819499947431533,finish=1568819499952627856,duration=5196323,event=uninstall_oclint[0Ktravis_time:start:038f7fc0[0Ktravis_time:end:038f7fc0:start=1568819499958407043,finish=1568819499962546466,duration=4139423,event=rvm_use[0Ktravis_time:start:06735b30[0Ktravis_time:end:06735b30:start=1568819499967249959,finish=1568819499976405620,duration=9155661,event=rm_etc_boto_cfg[0Ktravis_time:start:1067c447[0Ktravis_time:end:1067c447:start=1568819499982003243,finish=1568819499984934337,duration=2931094,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2c6d11c4[0Ktravis_time:end:2c6d11c4:start=1568819499990485243,finish=1568819500048459665,duration=57974422,event=enable_i386[0Ktravis_time:start:087ac9ec[0Ktravis_time:end:087ac9ec:start=1568819500053701219,finish=1568819500059864864,duration=6163645,event=update_rubygems[0Ktravis_time:start:0309af73[0Ktravis_time:end:0309af73:start=1568819500064514793,finish=1568819501114133732,duration=1049618939,event=ensure_path_components[0Ktravis_time:start:09982c6e[0Ktravis_time:end:09982c6e:start=1568819501118696587,finish=1568819501122200739,duration=3504152,event=redefine_curl[0Ktravis_time:start:0c8a9b6e[0Ktravis_time:end:0c8a9b6e:start=1568819501126748233,finish=1568819501184079131,duration=57330898,event=nonblock_pipe[0Ktravis_time:start:02a8e8fc[0Ktravis_time:end:02a8e8fc:start=1568819501188986845,finish=1568819501236664980,duration=47678135,event=apt_get_update[0Ktravis_time:start:0475a756[0Ktravis_time:end:0475a756:start=1568819501242264612,finish=1568819501245357709,duration=3093097,event=deprecate_xcode_64[0Ktravis_time:start:0a188da8[0Ktravis_time:end:0a188da8:start=1568819501251570092,finish=1568819506802074021,duration=5550503929,event=update_heroku[0Ktravis_time:start:04698137[0Ktravis_time:end:04698137:start=1568819506806963208,finish=1568819506809866893,duration=2903685,event=shell_session_update[0Ktravis_time:start:05b732c0[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3919
travis_fold:end:docker_mtu[0Ktravis_time:end:05b732c0:start=1568819506814818180,finish=1568819508012486271,duration=1197668091,event=set_docker_mtu[0Ktravis_time:start:0dfb73fa[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0dfb73fa:start=1568819508018002278,finish=1568819508092153471,duration=74151193,event=resolvconf[0Ktravis_time:start:146018bf[0Ktravis_time:end:146018bf:start=1568819508098377469,finish=1568819508228293075,duration=129915606,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:06950a14[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:06950a14:start=1568819508315932922,finish=1568819508579009108,duration=263076186,event=configure[0Ktravis_time:start:168c52c8[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:168c52c8:start=1568819508585833173,finish=1568819518464047695,duration=9878214522,event=configure[0Ktravis_time:start:06382ade[0Ktravis_fold:start:services[0Ktravis_time:start:31f2aea5[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:31f2aea5:start=1568819518489779416,finish=1568819518506043794,duration=16264378,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:31f2aea5:start=1568819518489779416,finish=1568819521513493481,duration=3023714065,event=services[0Ktravis_time:start:0159a539[0Ktravis_time:end:0159a539:start=1568819521519121346,finish=1568819521522049827,duration=2928481,event=fix_ps4[0Ktravis_time:start:1a0b7cba[0K
travis_fold:start:git.checkout[0Ktravis_time:start:03b15c6d[0K$ git clone --depth=50 --branch=addUbuntu1904 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:03b15c6d:start=1568819521532182743,finish=1568819532105090339,duration=10572907596,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 2efb54a69d10db47b6397a7d0e706ba82502d2ac
travis_fold:end:git.checkout[0K
travis_time:end:03b15c6d:start=1568819521532182743,finish=1568819532198306376,duration=10666123633,event=checkout[0Ktravis_time:start:1b4598a8[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1b4598a8:start=1568819532203628731,finish=1568819532215934199,duration=12305468,event=env[0Ktravis_time:start:06c873c0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:06c873c0:start=1568819532222519770,finish=1568819532228790097,duration=6270327,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:330e4a3c[0K$ python system_testing.py -s dealii-of
usage: system_testing.py [-h] [-l] -s
                         {fe-fe,of-of,nutils-of,of-ccx_fsi,of-ccx,dealii-of,bindings,su2-ccx,of-of_np}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:330e4a3c:start=1568819532591448371,finish=1568819532660197652,duration=68749281,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:11cb00fa[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586515510/log.txt)