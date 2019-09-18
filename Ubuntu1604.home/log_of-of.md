 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586477733) 
## Triggered by: [push](https://github.com/precice/systemtests/commit/3c3e92795247) 
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
travis_time:end:048cf8b0:start=1568806238960448863,finish=1568806238965774124,duration=5325261,event=show_system_info[0Ktravis_time:start:03b7a776[0Ktravis_time:end:03b7a776:start=1568806238968570336,finish=1568806238988424598,duration=19854262,event=rm_riak_source[0Ktravis_time:start:142efb58[0Ktravis_time:end:142efb58:start=1568806238991149464,finish=1568806238995969550,duration=4820086,event=fix_rwky_redis[0Ktravis_time:start:155f4c8f[0Ktravis_time:end:155f4c8f:start=1568806238998679680,finish=1568806239450174688,duration=451495008,event=wait_for_network[0Ktravis_time:start:067db0f5[0Ktravis_time:end:067db0f5:start=1568806239466958178,finish=1568806240357490420,duration=890532242,event=update_apt_keys[0Ktravis_time:start:079bfd73[0Ktravis_time:end:079bfd73:start=1568806240361935630,finish=1568806241372504478,duration=1010568848,event=fix_hhvm_source[0Ktravis_time:start:1f45f230[0Ktravis_time:end:1f45f230:start=1568806241376661268,finish=1568806241387835515,duration=11174247,event=update_mongo_arch[0Ktravis_time:start:134b192e[0Ktravis_time:end:134b192e:start=1568806241391716459,finish=1568806241432740943,duration=41024484,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1e5e725c[0Ktravis_time:end:1e5e725c:start=1568806241436850431,finish=1568806241439289288,duration=2438857,event=update_glibc[0Ktravis_time:start:000ab4fc[0Ktravis_time:end:000ab4fc:start=1568806241443574819,finish=1568806241452221999,duration=8647180,event=clean_up_path[0Ktravis_time:start:00d74d99[0Ktravis_time:end:00d74d99:start=1568806241456569677,finish=1568806241464425965,duration=7856288,event=fix_resolv_conf[0Ktravis_time:start:0a3237e0[0Ktravis_time:end:0a3237e0:start=1568806241468970189,finish=1568806241477622630,duration=8652441,event=fix_etc_hosts[0Ktravis_time:start:15af123b[0Ktravis_time:end:15af123b:start=1568806241482128753,finish=1568806241491400279,duration=9271526,event=fix_mvn_settings_xml[0Ktravis_time:start:000ec2bb[0Ktravis_time:end:000ec2bb:start=1568806241495659174,finish=1568806241505223810,duration=9564636,event=no_ipv6_localhost[0Ktravis_time:start:005cefb3[0Ktravis_time:end:005cefb3:start=1568806241511128793,finish=1568806241514168716,duration=3039923,event=fix_etc_mavenrc[0Ktravis_time:start:1c44a7e8[0Ktravis_time:end:1c44a7e8:start=1568806241518496257,finish=1568806241522724501,duration=4228244,event=fix_wwdr_certificate[0Ktravis_time:start:3085c6bc[0Ktravis_time:end:3085c6bc:start=1568806241526961602,finish=1568806241553134660,duration=26173058,event=put_localhost_first[0Ktravis_time:start:02ed6aa0[0Ktravis_time:end:02ed6aa0:start=1568806241556553307,finish=1568806241560408019,duration=3854712,event=home_paths[0Ktravis_time:start:089e1bac[0Ktravis_time:end:089e1bac:start=1568806241564506457,finish=1568806241577797881,duration=13291424,event=disable_initramfs[0Ktravis_time:start:1900b6d0[0Ktravis_time:end:1900b6d0:start=1568806241581361531,finish=1568806241871844644,duration=290483113,event=disable_ssh_roaming[0Ktravis_time:start:034a879c[0Ktravis_time:end:034a879c:start=1568806241877143749,finish=1568806241882012804,duration=4869055,event=debug_tools[0Ktravis_time:start:08475c46[0Ktravis_time:end:08475c46:start=1568806241887065110,finish=1568806241891532321,duration=4467211,event=uninstall_oclint[0Ktravis_time:start:17edade8[0Ktravis_time:end:17edade8:start=1568806241896334372,finish=1568806241904990431,duration=8656059,event=rvm_use[0Ktravis_time:start:0679cd61[0Ktravis_time:end:0679cd61:start=1568806241910068180,finish=1568806241918489815,duration=8421635,event=rm_etc_boto_cfg[0Ktravis_time:start:195bd9da[0Ktravis_time:end:195bd9da:start=1568806241922510890,finish=1568806241925817379,duration=3306489,event=rm_oraclejdk8_symlink[0Ktravis_time:start:041c88da[0Ktravis_time:end:041c88da:start=1568806241931652010,finish=1568806241989595563,duration=57943553,event=enable_i386[0Ktravis_time:start:302bab20[0Ktravis_time:end:302bab20:start=1568806241994536322,finish=1568806241998716033,duration=4179711,event=update_rubygems[0Ktravis_time:start:03913530[0Ktravis_time:end:03913530:start=1568806242003004379,finish=1568806242975114267,duration=972109888,event=ensure_path_components[0Ktravis_time:start:006d76e0[0Ktravis_time:end:006d76e0:start=1568806242979882581,finish=1568806242982855255,duration=2972674,event=redefine_curl[0Ktravis_time:start:07255bdb[0Ktravis_time:end:07255bdb:start=1568806242989475496,finish=1568806243039720779,duration=50245283,event=nonblock_pipe[0Ktravis_time:start:10cffaf4[0Ktravis_time:end:10cffaf4:start=1568806243044199257,finish=1568806243082327124,duration=38127867,event=apt_get_update[0Ktravis_time:start:20278970[0Ktravis_time:end:20278970:start=1568806243086786146,finish=1568806243089558635,duration=2772489,event=deprecate_xcode_64[0Ktravis_time:start:0bcf29b0[0Ktravis_time:end:0bcf29b0:start=1568806243094132386,finish=1568806247765041476,duration=4670909090,event=update_heroku[0Ktravis_time:start:32d3296a[0Ktravis_time:end:32d3296a:start=1568806247770242778,finish=1568806247773052614,duration=2809836,event=shell_session_update[0Ktravis_time:start:0af60e6b[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3875
travis_fold:end:docker_mtu[0Ktravis_time:end:0af60e6b:start=1568806247777232025,finish=1568806248971093645,duration=1193861620,event=set_docker_mtu[0Ktravis_time:start:17fa319a[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:17fa319a:start=1568806248975423798,finish=1568806249037364114,duration=61940316,event=resolvconf[0Ktravis_time:start:06f81bb5[0Ktravis_time:end:06f81bb5:start=1568806249041730626,finish=1568806249139973172,duration=98242546,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:00102a44[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:00102a44:start=1568806249218062635,finish=1568806249650648823,duration=432586188,event=configure[0Ktravis_time:start:0f4e5d1d[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0f4e5d1d:start=1568806249655938762,finish=1568806259059052394,duration=9403113632,event=configure[0Ktravis_time:start:00641884[0Ktravis_fold:start:services[0Ktravis_time:start:1188519f[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1188519f:start=1568806259084472920,finish=1568806259100660459,duration=16187539,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1188519f:start=1568806259084472920,finish=1568806262105760957,duration=3021288037,event=services[0Ktravis_time:start:1343d060[0Ktravis_time:end:1343d060:start=1568806262110440829,finish=1568806262113443542,duration=3002713,event=fix_ps4[0Ktravis_time:start:04e2cd16[0K
travis_fold:start:git.checkout[0Ktravis_time:start:018d7dc0[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-users https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:018d7dc0:start=1568806262122152575,finish=1568806272297800602,duration=10175648027,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3c3e927952479f3d81847ce6139ede1bec7f9aff
travis_fold:end:git.checkout[0K
travis_time:end:018d7dc0:start=1568806262122152575,finish=1568806272544941533,duration=10422788958,event=checkout[0Ktravis_time:start:1db13c94[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1db13c94:start=1568806272549677061,finish=1568806272559629866,duration=9952805,event=env[0Ktravis_time:start:010c5e38[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:010c5e38:start=1568806272564285376,finish=1568806272570958226,duration=6672850,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:12ce1e7d[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {su2-ccx,of-ccx,nutils-of,fe-fe,of-ccx_fsi,of-of,of-of_np,bindings,dealii-of}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:12ce1e7d:start=1568806272910611285,finish=1568806272975796680,duration=65185395,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:05fa82ba[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586477747/log.txt)