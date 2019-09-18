 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/586517772) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63e83084ff16...628c8f57e99a) 
## Last succesfull commits 
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
travis_time:end:0656a040:start=1568823141445600336,finish=1568823141451663114,duration=6062778,event=show_system_info[0Ktravis_time:start:08aeeaf4[0Ktravis_time:end:08aeeaf4:start=1568823141454757681,finish=1568823141481953838,duration=27196157,event=rm_riak_source[0Ktravis_time:start:061740b6[0Ktravis_time:end:061740b6:start=1568823141485020358,finish=1568823141490111716,duration=5091358,event=fix_rwky_redis[0Ktravis_time:start:121ffbf0[0Ktravis_time:end:121ffbf0:start=1568823141492944238,finish=1568823141907441604,duration=414497366,event=wait_for_network[0Ktravis_time:start:006e772f[0Ktravis_time:end:006e772f:start=1568823141912826479,finish=1568823142836580710,duration=923754231,event=update_apt_keys[0Ktravis_time:start:23f76fb8[0Ktravis_time:end:23f76fb8:start=1568823142841335270,finish=1568823143881630693,duration=1040295423,event=fix_hhvm_source[0Ktravis_time:start:1ae0cba2[0Ktravis_time:end:1ae0cba2:start=1568823143886170870,finish=1568823143896404391,duration=10233521,event=update_mongo_arch[0Ktravis_time:start:000fc725[0Ktravis_time:end:000fc725:start=1568823143900910906,finish=1568823143942085864,duration=41174958,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0ab0ee6e[0Ktravis_time:end:0ab0ee6e:start=1568823143946673446,finish=1568823143950023527,duration=3350081,event=update_glibc[0Ktravis_time:start:09ea5f7c[0Ktravis_time:end:09ea5f7c:start=1568823143954509004,finish=1568823143964980685,duration=10471681,event=clean_up_path[0Ktravis_time:start:152e08d2[0Ktravis_time:end:152e08d2:start=1568823143969425046,finish=1568823143978255355,duration=8830309,event=fix_resolv_conf[0Ktravis_time:start:292fee91[0Ktravis_time:end:292fee91:start=1568823143983459301,finish=1568823143993655181,duration=10195880,event=fix_etc_hosts[0Ktravis_time:start:02d25dd0[0Ktravis_time:end:02d25dd0:start=1568823143998462074,finish=1568823144007988850,duration=9526776,event=fix_mvn_settings_xml[0Ktravis_time:start:1073a52a[0Ktravis_time:end:1073a52a:start=1568823144012611965,finish=1568823144023367877,duration=10755912,event=no_ipv6_localhost[0Ktravis_time:start:1021bdd4[0Ktravis_time:end:1021bdd4:start=1568823144027889365,finish=1568823144031120978,duration=3231613,event=fix_etc_mavenrc[0Ktravis_time:start:19e51834[0Ktravis_time:end:19e51834:start=1568823144035461828,finish=1568823144039920086,duration=4458258,event=fix_wwdr_certificate[0Ktravis_time:start:029e9c2c[0Ktravis_time:end:029e9c2c:start=1568823144043906261,finish=1568823144071976259,duration=28069998,event=put_localhost_first[0Ktravis_time:start:02acee0b[0Ktravis_time:end:02acee0b:start=1568823144076381641,finish=1568823144080373854,duration=3992213,event=home_paths[0Ktravis_time:start:11a4e5f3[0Ktravis_time:end:11a4e5f3:start=1568823144084815930,finish=1568823144097566257,duration=12750327,event=disable_initramfs[0Ktravis_time:start:234552bc[0Ktravis_time:end:234552bc:start=1568823144102477724,finish=1568823144481590935,duration=379113211,event=disable_ssh_roaming[0Ktravis_time:start:150eeff6[0Ktravis_time:end:150eeff6:start=1568823144486167802,finish=1568823144489209801,duration=3041999,event=debug_tools[0Ktravis_time:start:134fdede[0Ktravis_time:end:134fdede:start=1568823144494207911,finish=1568823144497814526,duration=3606615,event=uninstall_oclint[0Ktravis_time:start:159d66c8[0Ktravis_time:end:159d66c8:start=1568823144502750596,finish=1568823144506182264,duration=3431668,event=rvm_use[0Ktravis_time:start:08da7ca0[0Ktravis_time:end:08da7ca0:start=1568823144511119012,finish=1568823144520036511,duration=8917499,event=rm_etc_boto_cfg[0Ktravis_time:start:00e32510[0Ktravis_time:end:00e32510:start=1568823144524612381,finish=1568823144527208377,duration=2595996,event=rm_oraclejdk8_symlink[0Ktravis_time:start:2202c720[0Ktravis_time:end:2202c720:start=1568823144531834405,finish=1568823144587431380,duration=55596975,event=enable_i386[0Ktravis_time:start:04613dea[0Ktravis_time:end:04613dea:start=1568823144592145090,finish=1568823144596599679,duration=4454589,event=update_rubygems[0Ktravis_time:start:292998fc[0Ktravis_time:end:292998fc:start=1568823144600947070,finish=1568823145627133341,duration=1026186271,event=ensure_path_components[0Ktravis_time:start:07fd39a3[0Ktravis_time:end:07fd39a3:start=1568823145632562219,finish=1568823145635871078,duration=3308859,event=redefine_curl[0Ktravis_time:start:06a897ac[0Ktravis_time:end:06a897ac:start=1568823145641490117,finish=1568823145692721388,duration=51231271,event=nonblock_pipe[0Ktravis_time:start:192fa200[0Ktravis_time:end:192fa200:start=1568823145697359999,finish=1568823145738108175,duration=40748176,event=apt_get_update[0Ktravis_time:start:0094a3a0[0Ktravis_time:end:0094a3a0:start=1568823145742094428,finish=1568823145744907368,duration=2812940,event=deprecate_xcode_64[0Ktravis_time:start:314a0b34[0Ktravis_time:end:314a0b34:start=1568823145748581375,finish=1568823150664759519,duration=4916178144,event=update_heroku[0Ktravis_time:start:16752068[0Ktravis_time:end:16752068:start=1568823150669579933,finish=1568823150672355322,duration=2775389,event=shell_session_update[0Ktravis_time:start:1a2a64fc[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3828
travis_fold:end:docker_mtu[0Ktravis_time:end:1a2a64fc:start=1568823150677597992,finish=1568823151878207263,duration=1200609271,event=set_docker_mtu[0Ktravis_time:start:15f517ca[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:15f517ca:start=1568823151882790182,finish=1568823151949431922,duration=66641740,event=resolvconf[0Ktravis_time:start:08493216[0Ktravis_time:end:08493216:start=1568823151954070909,finish=1568823152061394237,duration=107323328,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:300aecda[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:300aecda:start=1568823152144971234,finish=1568823152537304018,duration=392332784,event=configure[0Ktravis_time:start:04843434[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:04843434:start=1568823152542581777,finish=1568823162584888312,duration=10042306535,event=configure[0Ktravis_time:start:056532d1[0Ktravis_fold:start:services[0Ktravis_time:start:08134f92[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:08134f92:start=1568823162610487716,finish=1568823162625465941,duration=14978225,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:08134f92:start=1568823162610487716,finish=1568823165631497894,duration=3021010178,event=services[0Ktravis_time:start:14156ee6[0Ktravis_time:end:14156ee6:start=1568823165636237324,finish=1568823165639389902,duration=3152578,event=fix_ps4[0Ktravis_time:start:0315325b[0K
travis_fold:start:git.checkout[0Ktravis_time:start:14798911[0K$ git clone --depth=50 --branch=BenjaminRueth-patch-fixpip1804 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:14798911:start=1568823165648742164,finish=1568823175829293284,duration=10180551120,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 628c8f57e99ad5b8d85cdaca6e230b3407aa4aee
travis_fold:end:git.checkout[0K
travis_time:end:14798911:start=1568823165648742164,finish=1568823176607237990,duration=10958495826,event=checkout[0Ktravis_time:start:1673ba8e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1673ba8e:start=1568823176611260141,finish=1568823176623397503,duration=12137362,event=env[0Ktravis_time:start:0084cc45[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0084cc45:start=1568823176628665656,finish=1568823176634149333,duration=5483677,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:221f603a[0K$ python system_testing.py -s of-of
usage: system_testing.py [-h] [-l] -s
                         {of-ccx_fsi,of-of,of-of_np,su2-ccx,fe-fe,nutils-of,of-ccx,dealii-of,bindings}
                         [-b BRANCH]
                         [-f {[secure],tests} [{[secure],tests} ...]] --base
                         BASE
system_testing.py: error: the following arguments are required: --base
travis_time:end:221f603a:start=1568823176976946454,finish=1568823177040118656,duration=63172202,event=script[0K[31;1mThe command "python system_testing.py -s of-of" exited with 2.[0m

travis_fold:start:after_failure[0Ktravis_time:start:1f0d1efa[0K$ python push.py -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/586517792/log.txt)