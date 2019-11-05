## Status: Passing 
Build: [1057](https://travis-ci.org/precice/systemtests/builds/607431677) 

Job: [1057.18](https://travis-ci.org/precice/systemtests/jobs/607431695) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/9921a3e9e3f7596df67493847bbc01f17a3b226e...e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13) 

---
Last 100 lines of the job log at the moment of push:
```
travis_fold:end:system_info[0K
travis_time:end:013dbbee:start=1572921810253804362,finish=1572921810259913811,duration=6109449,event=show_system_info[0Ktravis_time:start:15d30edc[0Ktravis_time:end:15d30edc:start=1572921810263143569,finish=1572921810286524519,duration=23380950,event=rm_riak_source[0Ktravis_time:start:20a9b2ce[0Ktravis_time:end:20a9b2ce:start=1572921810290060449,finish=1572921810300121908,duration=10061459,event=fix_rwky_redis[0Ktravis_time:start:0b7b9d3c[0Ktravis_time:end:0b7b9d3c:start=1572921810303882283,finish=1572921810731019273,duration=427136990,event=wait_for_network[0Ktravis_time:start:09cea22c[0Ktravis_time:end:09cea22c:start=1572921810736620369,finish=1572921811673412227,duration=936791858,event=update_apt_keys[0Ktravis_time:start:050edf34[0Ktravis_time:end:050edf34:start=1572921811678852500,finish=1572921812865032163,duration=1186179663,event=fix_hhvm_source[0Ktravis_time:start:01501ecc[0Ktravis_time:end:01501ecc:start=1572921812868883378,finish=1572921812883339607,duration=14456229,event=update_mongo_arch[0Ktravis_time:start:0ab05d0c[0Ktravis_time:end:0ab05d0c:start=1572921812888922745,finish=1572921812935475928,duration=46553183,event=fix_sudo_enabled_trusty[0Ktravis_time:start:118f16f4[0Ktravis_time:end:118f16f4:start=1572921812940680086,finish=1572921812943697599,duration=3017513,event=update_glibc[0Ktravis_time:start:00c2e600[0Ktravis_time:end:00c2e600:start=1572921812951442269,finish=1572921812961427526,duration=9985257,event=clean_up_path[0Ktravis_time:start:09e82556[0Ktravis_time:end:09e82556:start=1572921812966227910,finish=1572921812979150416,duration=12922506,event=fix_resolv_conf[0Ktravis_time:start:0b0808d0[0Ktravis_time:end:0b0808d0:start=1572921812985534283,finish=1572921812996962981,duration=11428698,event=fix_etc_hosts[0Ktravis_time:start:064e587d[0Ktravis_time:end:064e587d:start=1572921813001809565,finish=1572921813012505140,duration=10695575,event=fix_mvn_settings_xml[0Ktravis_time:start:1de1fcb5[0Ktravis_time:end:1de1fcb5:start=1572921813019428437,finish=1572921813030107777,duration=10679340,event=no_ipv6_localhost[0Ktravis_time:start:04fc6a38[0Ktravis_time:end:04fc6a38:start=1572921813038550977,finish=1572921813041786027,duration=3235050,event=fix_etc_mavenrc[0Ktravis_time:start:008f247f[0Ktravis_time:end:008f247f:start=1572921813046697645,finish=1572921813050731136,duration=4033491,event=fix_wwdr_certificate[0Ktravis_time:start:05b3b6f9[0Ktravis_time:end:05b3b6f9:start=1572921813054644195,finish=1572921813086647889,duration=32003694,event=put_localhost_first[0Ktravis_time:start:09c19c98[0Ktravis_time:end:09c19c98:start=1572921813090760338,finish=1572921813095632880,duration=4872542,event=home_paths[0Ktravis_time:start:0236c800[0Ktravis_time:end:0236c800:start=1572921813099792944,finish=1572921813116964789,duration=17171845,event=disable_initramfs[0Ktravis_time:start:022d35aa[0Ktravis_time:end:022d35aa:start=1572921813124257772,finish=1572921813413840222,duration=289582450,event=disable_ssh_roaming[0Ktravis_time:start:088cfb9c[0Ktravis_time:end:088cfb9c:start=1572921813420810259,finish=1572921813424421099,duration=3610840,event=debug_tools[0Ktravis_time:start:1d0f6790[0Ktravis_time:end:1d0f6790:start=1572921813428554973,finish=1572921813432592111,duration=4037138,event=uninstall_oclint[0Ktravis_time:start:0ddd3e88[0Ktravis_time:end:0ddd3e88:start=1572921813436492154,finish=1572921813440355712,duration=3863558,event=rvm_use[0Ktravis_time:start:3a1b59f1[0Ktravis_time:end:3a1b59f1:start=1572921813444814915,finish=1572921813458555643,duration=13740728,event=rm_etc_boto_cfg[0Ktravis_time:start:2aeeafc8[0Ktravis_time:end:2aeeafc8:start=1572921813465039952,finish=1572921813468784930,duration=3744978,event=rm_oraclejdk8_symlink[0Ktravis_time:start:0072a5f6[0Ktravis_time:end:0072a5f6:start=1572921813475740677,finish=1572921813536628001,duration=60887324,event=enable_i386[0Ktravis_time:start:230aaa08[0Ktravis_time:end:230aaa08:start=1572921813543244999,finish=1572921813547731252,duration=4486253,event=update_rubygems[0Ktravis_time:start:1a27921a[0Ktravis_time:end:1a27921a:start=1572921813554040548,finish=1572921814684703244,duration=1130662696,event=ensure_path_components[0Ktravis_time:start:162305ee[0Ktravis_time:end:162305ee:start=1572921814693201532,finish=1572921814696634489,duration=3432957,event=redefine_curl[0Ktravis_time:start:00926703[0Ktravis_time:end:00926703:start=1572921814701186691,finish=1572921814766046834,duration=64860143,event=nonblock_pipe[0Ktravis_time:start:04499d0b[0Ktravis_time:end:04499d0b:start=1572921814774592343,finish=1572921817850272635,duration=3075680292,event=apt_get_update[0Ktravis_time:start:0669d7b8[0Ktravis_time:end:0669d7b8:start=1572921817855074299,finish=1572921817857929592,duration=2855293,event=deprecate_xcode_64[0Ktravis_time:start:261b48c6[0Ktravis_time:end:261b48c6:start=1572921817862911181,finish=1572921822582944599,duration=4720033418,event=update_heroku[0Ktravis_time:start:1c74ae93[0Ktravis_time:end:1c74ae93:start=1572921822587626154,finish=1572921822590894719,duration=3268565,event=shell_session_update[0Ktravis_time:start:322f76f4[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3954
travis_fold:end:docker_mtu[0Ktravis_time:end:322f76f4:start=1572921822595203725,finish=1572921823816176924,duration=1220973199,event=set_docker_mtu[0Ktravis_time:start:05b075a2[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:05b075a2:start=1572921823823437919,finish=1572921823904788622,duration=81350703,event=resolvconf[0Ktravis_time:start:0893132a[0Ktravis_time:end:0893132a:start=1572921823913162271,finish=1572921824026912723,duration=113750452,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0b4b923c[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0b4b923c:start=1572921824126132032,finish=1572921825584033133,duration=1457901101,event=configure[0Ktravis_time:start:0d74edb3[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d74edb3:start=1572921825590961865,finish=1572921836960250498,duration=11369288633,event=configure[0Ktravis_time:start:04b7ed74[0Ktravis_fold:start:services[0Ktravis_time:start:1942540e[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:1942540e:start=1572921836989523035,finish=1572921837007061987,duration=17538952,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:1942540e:start=1572921836989523035,finish=1572921840015297019,duration=3025773984,event=services[0Ktravis_time:start:0701d5cc[0Ktravis_time:end:0701d5cc:start=1572921840020639073,finish=1572921840024881824,duration=4242751,event=fix_ps4[0Ktravis_time:start:0b94bd96[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0120c84f[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0120c84f:start=1572921840037226817,finish=1572921847893644540,duration=7856417723,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf e3f7960c948ea9ade7a2b19f1bd7d3b6497a2c13
travis_fold:end:git.checkout[0K
travis_time:end:0120c84f:start=1572921840037226817,finish=1572921848558578012,duration=8521351195,event=checkout[0Ktravis_time:start:0588d080[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0588d080:start=1572921848565062595,finish=1572921848579316380,duration=14253785,event=env[0Ktravis_time:start:063471cc[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:063471cc:start=1572921848583773775,finish=1572921848593110433,duration=9336658,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:00627c9c[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
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

Creating network "testcomposeofof_default" with the default driver
Creating network "testcomposeofof_[secure]comm" with the default driver
Creating volume "testcomposeofof_output" with default driver
Creating volume "testcomposeofof_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:05fe1ccc5198ad34e3a536b114ccdb3c99481211760a11e8e6218a3edb849bae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating tutorial-data
Creating openfoam-adapter-solid
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:00627c9c:start=1572921848978912172,finish=1572921971287238943,duration=122308326771,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:1f2f1a33[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/607431695/log.txt)