## Status: Failure 
Build: [1431](https://travis-ci.org/precice/systemtests/builds/635347829) 

Job: [1431.8](https://travis-ci.org/precice/systemtests/jobs/635347837) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/150) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e) 

---
Last 100 lines of the job log at the moment of push:
```
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:0089109e:start=1578782556940945430,finish=1578782556945929777,duration=4984347,event=show_system_info[0Ktravis_time:start:06f12f44[0Ktravis_time:end:06f12f44:start=1578782556948335410,finish=1578782556968116503,duration=19781093,event=rm_riak_source[0Ktravis_time:start:0c74f7a8[0Ktravis_time:end:0c74f7a8:start=1578782556970500394,finish=1578782556975116482,duration=4616088,event=fix_rwky_redis[0Ktravis_time:start:0ec98298[0Ktravis_time:end:0ec98298:start=1578782556979740130,finish=1578782557315404587,duration=335664457,event=wait_for_network[0Ktravis_time:start:180b2739[0Ktravis_time:end:180b2739:start=1578782557318647679,finish=1578782558563553368,duration=1244905689,event=update_apt_keys[0Ktravis_time:start:2190b6f6[0Ktravis_time:end:2190b6f6:start=1578782558567413533,finish=1578782559512033680,duration=944620147,event=fix_hhvm_source[0Ktravis_time:start:16a73108[0Ktravis_time:end:16a73108:start=1578782559516117446,finish=1578782559527162866,duration=11045420,event=update_mongo_arch[0Ktravis_time:start:04307c72[0Ktravis_time:end:04307c72:start=1578782559531611514,finish=1578782559565946508,duration=34334994,event=fix_sudo_enabled_trusty[0Ktravis_time:start:158e745c[0Ktravis_time:end:158e745c:start=1578782559570265887,finish=1578782559572526439,duration=2260552,event=update_glibc[0Ktravis_time:start:1370c7e4[0Ktravis_time:end:1370c7e4:start=1578782559575896867,finish=1578782559584273652,duration=8376785,event=clean_up_path[0Ktravis_time:start:0012c7d0[0Ktravis_time:end:0012c7d0:start=1578782559590526489,finish=1578782559597661611,duration=7135122,event=fix_resolv_conf[0Ktravis_time:start:06fcc7bc[0Ktravis_time:end:06fcc7bc:start=1578782559601258238,finish=1578782559609063759,duration=7805521,event=fix_etc_hosts[0Ktravis_time:start:2b0959f0[0Ktravis_time:end:2b0959f0:start=1578782559614168851,finish=1578782559621337292,duration=7168441,event=fix_mvn_settings_xml[0Ktravis_time:start:08277cb5[0Ktravis_time:end:08277cb5:start=1578782559624897920,finish=1578782559635506648,duration=10608728,event=no_ipv6_localhost[0Ktravis_time:start:21be553d[0Ktravis_time:end:21be553d:start=1578782559639289432,finish=1578782559641797379,duration=2507947,event=fix_etc_mavenrc[0Ktravis_time:start:08272f22[0Ktravis_time:end:08272f22:start=1578782559645429897,finish=1578782559648256884,duration=2826987,event=fix_wwdr_certificate[0Ktravis_time:start:0ecaeb68[0Ktravis_time:end:0ecaeb68:start=1578782559652525051,finish=1578782559676333128,duration=23808077,event=put_localhost_first[0Ktravis_time:start:01c291b4[0Ktravis_time:end:01c291b4:start=1578782559680510714,finish=1578782559683648493,duration=3137779,event=home_paths[0Ktravis_time:start:00d6e5ed[0Ktravis_time:end:00d6e5ed:start=1578782559687350495,finish=1578782559699292253,duration=11941758,event=disable_initramfs[0Ktravis_time:start:013f9044[0Ktravis_time:end:013f9044:start=1578782559702609434,finish=1578782559994969266,duration=292359832,event=disable_ssh_roaming[0Ktravis_time:start:044ba7b3[0Ktravis_time:end:044ba7b3:start=1578782559999751414,finish=1578782560002257772,duration=2506358,event=debug_tools[0Ktravis_time:start:04032fc0[0Ktravis_time:end:04032fc0:start=1578782560005595851,finish=1578782560008829981,duration=3234130,event=uninstall_oclint[0Ktravis_time:start:00d9cf00[0Ktravis_time:end:00d9cf00:start=1578782560011824858,finish=1578782560014744948,duration=2920090,event=rvm_use[0Ktravis_time:start:007901b8[0Ktravis_time:end:007901b8:start=1578782560017697797,finish=1578782560034324492,duration=16626695,event=rm_etc_boto_cfg[0Ktravis_time:start:03dd8b48[0Ktravis_time:end:03dd8b48:start=1578782560038423504,finish=1578782560041045693,duration=2622189,event=rm_oraclejdk8_symlink[0Ktravis_time:start:09e363c8[0Ktravis_time:end:09e363c8:start=1578782560045642008,finish=1578782560094562118,duration=48920110,event=enable_i386[0Ktravis_time:start:0168be80[0Ktravis_time:end:0168be80:start=1578782560098985804,finish=1578782560103214502,duration=4228698,event=update_rubygems[0Ktravis_time:start:288dfda1[0Ktravis_time:end:288dfda1:start=1578782560106922779,finish=1578782560959475820,duration=852553041,event=ensure_path_components[0Ktravis_time:start:1ad47dd5[0Ktravis_time:end:1ad47dd5:start=1578782560964061718,finish=1578782560966561736,duration=2500018,event=redefine_curl[0Ktravis_time:start:15c5ca80[0Ktravis_time:end:15c5ca80:start=1578782560970628203,finish=1578782561013269884,duration=42641681,event=nonblock_pipe[0Ktravis_time:start:2244be08[0Ktravis_time:end:2244be08:start=1578782561017334892,finish=1578782567046264966,duration=6028930074,event=apt_get_update[0Ktravis_time:start:09a17c84[0Ktravis_time:end:09a17c84:start=1578782567050348294,finish=1578782567052772822,duration=2424528,event=deprecate_xcode_64[0Ktravis_time:start:11070d2b[0Ktravis_time:end:11070d2b:start=1578782567056551991,finish=1578782570834054551,duration=3777502560,event=update_heroku[0Ktravis_time:start:01d48092[0Ktravis_time:end:01d48092:start=1578782570838536722,finish=1578782570841329533,duration=2792811,event=shell_session_update[0Ktravis_time:start:002ab7ff[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3884
travis_fold:end:docker_mtu[0Ktravis_time:end:002ab7ff:start=1578782570845791920,finish=1578782572038211453,duration=1192419533,event=set_docker_mtu[0Ktravis_time:start:02215254[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:02215254:start=1578782572042257088,finish=1578782572093867934,duration=51610846,event=resolvconf[0Ktravis_time:start:37aa64ad[0Ktravis_time:end:37aa64ad:start=1578782572097786198,finish=1578782572182917579,duration=85131381,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:071b341c[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:071b341c:start=1578782572250205095,finish=1578782572648662783,duration=398457688,event=configure[0Ktravis_time:start:04eb313e[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:04eb313e:start=1578782572653262622,finish=1578782580656657418,duration=8003394796,event=configure[0Ktravis_time:start:00506dc4[0Ktravis_fold:start:services[0Ktravis_time:start:03a747cc[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:03a747cc:start=1578782580680007591,finish=1578782580693898357,duration=13890766,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:03a747cc:start=1578782580680007591,finish=1578782583699561117,duration=3019553526,event=services[0Ktravis_time:start:038beea0[0Ktravis_time:end:038beea0:start=1578782583703493180,finish=1578782583706405180,duration=2912000,event=fix_ps4[0Ktravis_time:start:11266ef0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:023a10f3[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:023a10f3:start=1578782583716220945,finish=1578782589005576236,duration=5289355291,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:287d18a8[0K$ git fetch origin +refs/pull/150/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/150/merge -> FETCH_HEAD
travis_time:end:287d18a8:start=1578782589010964988,finish=1578782589372240194,duration=361275206,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:287d18a8:start=1578782589010964988,finish=1578782590354445005,duration=1343480017,event=checkout[0Ktravis_time:start:00c8146a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:00c8146a:start=1578782590358830578,finish=1578782590370823144,duration=11992566,event=env[0Ktravis_time:start:13bdf246[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:13bdf246:start=1578782590375619759,finish=1578782590381578213,duration=5958454,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2f5edb4f[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

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
      && sed -i ''s|<m2n:sockets from="Fluid" to="Solid"/>|<m2n:sockets from="Fluid"
      to="Solid" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

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
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BAttaching to openfoam-adapter-solid, openfoam-adapter-fluid, tutorial-data
[36mopenfoam-adapter-solid    |[0m sed: can't read [secure]-config.xml: No such file or directory
[33mopenfoam-adapter-fluid    |[0m sed: can't read [secure]-config.xml: No such file or directory
[36mopenfoam-adapter-solid exited with code 2
[0m[32mtutorial-data exited with code 0
[0m[33mopenfoam-adapter-fluid exited with code 2
[0m
```
[
Full job log](https://api.travis-ci.org/v3/job/635347837/log.txt)