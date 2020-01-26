## Status: Failure 
Build: [1519](https://travis-ci.org/precice/systemtests/builds/641972691) 

Job: [1519.21](https://travis-ci.org/precice/systemtests/jobs/641972712) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/161) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/pull/157) 

---
Last 100 lines of the job log at the moment of push:
```
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:0a1e0bcc:start=1580037733967366030,finish=1580037733972465119,duration=5099089,event=show_system_info[0Ktravis_time:start:083cbec0[0Ktravis_time:end:083cbec0:start=1580037733974913137,finish=1580037733998810446,duration=23897309,event=rm_riak_source[0Ktravis_time:start:3420c036[0Ktravis_time:end:3420c036:start=1580037734001501431,finish=1580037734007378187,duration=5876756,event=fix_rwky_redis[0Ktravis_time:start:09768168[0Ktravis_time:end:09768168:start=1580037734011418684,finish=1580037734403628140,duration=392209456,event=wait_for_network[0Ktravis_time:start:11ea0776[0Ktravis_time:end:11ea0776:start=1580037734408078726,finish=1580037736200798342,duration=1792719616,event=update_apt_keys[0Ktravis_time:start:0f7c2e3a[0Ktravis_time:end:0f7c2e3a:start=1580037736204943990,finish=1580037737120099784,duration=915155794,event=fix_hhvm_source[0Ktravis_time:start:0059c772[0Ktravis_time:end:0059c772:start=1580037737124704013,finish=1580037737134022374,duration=9318361,event=update_mongo_arch[0Ktravis_time:start:0c3287b8[0Ktravis_time:end:0c3287b8:start=1580037737138226204,finish=1580037737173315179,duration=35088975,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0b0550e5[0Ktravis_time:end:0b0550e5:start=1580037737178004745,finish=1580037737180707837,duration=2703092,event=update_glibc[0Ktravis_time:start:1e478a3c[0Ktravis_time:end:1e478a3c:start=1580037737185641388,finish=1580037737195873033,duration=10231645,event=clean_up_path[0Ktravis_time:start:03e12311[0Ktravis_time:end:03e12311:start=1580037737199564464,finish=1580037737207061682,duration=7497218,event=fix_resolv_conf[0Ktravis_time:start:03701afc[0Ktravis_time:end:03701afc:start=1580037737210992067,finish=1580037737219986115,duration=8994048,event=fix_etc_hosts[0Ktravis_time:start:00a3ef7c[0Ktravis_time:end:00a3ef7c:start=1580037737223398110,finish=1580037737231102514,duration=7704404,event=fix_mvn_settings_xml[0Ktravis_time:start:184a4a44[0Ktravis_time:end:184a4a44:start=1580037737234416057,finish=1580037737244997454,duration=10581397,event=no_ipv6_localhost[0Ktravis_time:start:020a5bec[0Ktravis_time:end:020a5bec:start=1580037737249383221,finish=1580037737251629151,duration=2245930,event=fix_etc_mavenrc[0Ktravis_time:start:25a96e82[0Ktravis_time:end:25a96e82:start=1580037737255643674,finish=1580037737260583861,duration=4940187,event=fix_wwdr_certificate[0Ktravis_time:start:08ac5908[0Ktravis_time:end:08ac5908:start=1580037737264523379,finish=1580037737285233759,duration=20710380,event=put_localhost_first[0Ktravis_time:start:0444d838[0Ktravis_time:end:0444d838:start=1580037737289206698,finish=1580037737292466526,duration=3259828,event=home_paths[0Ktravis_time:start:1bb5d0ba[0Ktravis_time:end:1bb5d0ba:start=1580037737296543142,finish=1580037737308860451,duration=12317309,event=disable_initramfs[0Ktravis_time:start:1d585b52[0Ktravis_time:end:1d585b52:start=1580037737312940770,finish=1580037737577602173,duration=264661403,event=disable_ssh_roaming[0Ktravis_time:start:0e4de818[0Ktravis_time:end:0e4de818:start=1580037737581444799,finish=1580037737584224329,duration=2779530,event=debug_tools[0Ktravis_time:start:0482611c[0Ktravis_time:end:0482611c:start=1580037737588218093,finish=1580037737592253161,duration=4035068,event=uninstall_oclint[0Ktravis_time:start:08c553a2[0Ktravis_time:end:08c553a2:start=1580037737596307821,finish=1580037737600133363,duration=3825542,event=rvm_use[0Ktravis_time:start:134dc8a3[0Ktravis_time:end:134dc8a3:start=1580037737609775013,finish=1580037737616851841,duration=7076828,event=rm_etc_boto_cfg[0Ktravis_time:start:1d4c2e38[0Ktravis_time:end:1d4c2e38:start=1580037737620960132,finish=1580037737623747543,duration=2787411,event=rm_oraclejdk8_symlink[0Ktravis_time:start:3861e210[0Ktravis_time:end:3861e210:start=1580037737627793275,finish=1580037737672813937,duration=45020662,event=enable_i386[0Ktravis_time:start:156c43d6[0Ktravis_time:end:156c43d6:start=1580037737676801748,finish=1580037737680566724,duration=3764976,event=update_rubygems[0Ktravis_time:start:0e338dc8[0Ktravis_time:end:0e338dc8:start=1580037737684938728,finish=1580037738528231202,duration=843292474,event=ensure_path_components[0Ktravis_time:start:1479cc00[0Ktravis_time:end:1479cc00:start=1580037738532620646,finish=1580037738535331739,duration=2711093,event=redefine_curl[0Ktravis_time:start:35883aa7[0Ktravis_time:end:35883aa7:start=1580037738538626519,finish=1580037738583256464,duration=44629945,event=nonblock_pipe[0Ktravis_time:start:216d77e0[0Ktravis_time:end:216d77e0:start=1580037738587401440,finish=1580037744616879276,duration=6029477836,event=apt_get_update[0Ktravis_time:start:06a48d9f[0Ktravis_time:end:06a48d9f:start=1580037744620918105,finish=1580037744623638771,duration=2720666,event=deprecate_xcode_64[0Ktravis_time:start:1306cf80[0Ktravis_time:end:1306cf80:start=1580037744627506137,finish=1580037748449324474,duration=3821818337,event=update_heroku[0Ktravis_time:start:06a90d80[0Ktravis_time:end:06a90d80:start=1580037748453283721,finish=1580037748455634787,duration=2351066,event=shell_session_update[0Ktravis_time:start:2205f6cf[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3886
travis_fold:end:docker_mtu[0Ktravis_time:end:2205f6cf:start=1580037748458597353,finish=1580037749636260159,duration=1177662806,event=set_docker_mtu[0Ktravis_time:start:0309c639[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0309c639:start=1580037749639558722,finish=1580037749692609518,duration=53050796,event=resolvconf[0Ktravis_time:start:065971ce[0Ktravis_time:end:065971ce:start=1580037749696622251,finish=1580037749779505182,duration=82882931,event=maven_central_mirror[0Ktravis_time:start:2a0ef58c[0Ktravis_time:end:2a0ef58c:start=1580037749783837036,finish=1580037749845836382,duration=61999346,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:21647538[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:21647538:start=1580037749916724385,finish=1580037750234090761,duration=317366376,event=configure[0Ktravis_time:start:0a2c6e36[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0a2c6e36:start=1580037750238423459,finish=1580037758226465366,duration=7988041907,event=configure[0Ktravis_time:start:00bcf3f1[0Ktravis_fold:start:services[0Ktravis_time:start:0041f266[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0041f266:start=1580037758248319253,finish=1580037758260687067,duration=12367814,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0041f266:start=1580037758248319253,finish=1580037761266496742,duration=3018177489,event=services[0Ktravis_time:start:02973630[0Ktravis_time:end:02973630:start=1580037761270539817,finish=1580037761273096475,duration=2556658,event=fix_ps4[0Ktravis_time:start:0e91a6ef[0K
travis_fold:start:git.checkout[0Ktravis_time:start:12f4ac40[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:12f4ac40:start=1580037761279781136,finish=1580037766757967256,duration=5478186120,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:058ef54f[0K$ git fetch origin +refs/pull/161/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/161/merge -> FETCH_HEAD
travis_time:end:058ef54f:start=1580037766762999729,finish=1580037767359059604,duration=596059875,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:058ef54f:start=1580037766762999729,finish=1580037768073469793,duration=1310470064,event=checkout[0Ktravis_time:start:03637608[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:03637608:start=1580037768077869587,finish=1580037768087815104,duration=9945517,event=env[0Ktravis_time:start:05fbc98c[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:05fbc98c:start=1580037768092085341,finish=1580037768097581258,duration=5495917,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00adc244[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|gather-scatter\"|gather-scatter\" exchange-directory=\"/home/[secure]/Data/Exchange/\"
      network=\"eth0\"|g'' [secure]-config_serial.xml && ./runFluid && cp -r Fluid/
      /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-fluid
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  openfoam-adapter-solid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|gather-scatter\"|gather-scatter\" exchange-directory=\"/home/[secure]/Data/Exchange/\"
      network=\"eth0\"|g'' [secure]-config_serial.xml && ./runSolid && cp -r Solid/
      /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-solid
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  tutorial-data:
    container_name: tutorial-data
    image: alpine
    volumes:
    - output:/Output:rw
version: '3.0'
volumes:
  exchange: {}
  output: {}

Creating network "testcomposeofofnp_default" with the default driver
Creating network "testcomposeofofnp_[secure]comm" with the default driver
Creating volume "testcomposeofofnp_output" with default driver
Creating volume "testcomposeofofnp_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ab232f3ec4153d1e6e56dc63acc9ebce94d07174940d32a6b37e4e1c545878e8
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B
```
[
Full job log](https://api.travis-ci.org/v3/job/641972712/log.txt)