## Status: Passing 
Build: [1027](https://travis-ci.org/precice/systemtests/builds/603099773) 

Job: [1027.24](https://travis-ci.org/precice/systemtests/jobs/603099799) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/14ba7f61133053c5d9afcf1af31441555fb8dbf0...9921a3e9e3f7596df67493847bbc01f17a3b226e) 

---
Last 100 lines of the job log at the moment of push:
```
travis_time:end:024c0678:start=1572057692368950080,finish=1572057692375008217,duration=6058137,event=show_system_info[0Ktravis_time:start:0738c14c[0Ktravis_time:end:0738c14c:start=1572057692378218853,finish=1572057692403763288,duration=25544435,event=rm_riak_source[0Ktravis_time:start:1e27370a[0Ktravis_time:end:1e27370a:start=1572057692407177956,finish=1572057692414807879,duration=7629923,event=fix_rwky_redis[0Ktravis_time:start:0e443380[0Ktravis_time:end:0e443380:start=1572057692418477053,finish=1572057692888937724,duration=470460671,event=wait_for_network[0Ktravis_time:start:0a4eb42a[0Ktravis_time:end:0a4eb42a:start=1572057692893519183,finish=1572057694478623575,duration=1585104392,event=update_apt_keys[0Ktravis_time:start:07d52e40[0Ktravis_time:end:07d52e40:start=1572057694483914519,finish=1572057695535995135,duration=1052080616,event=fix_hhvm_source[0Ktravis_time:start:03249f82[0Ktravis_time:end:03249f82:start=1572057695540664231,finish=1572057695551033810,duration=10369579,event=update_mongo_arch[0Ktravis_time:start:0bf50494[0Ktravis_time:end:0bf50494:start=1572057695555782225,finish=1572057695599115435,duration=43333210,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0010e956[0Ktravis_time:end:0010e956:start=1572057695604113408,finish=1572057695607526858,duration=3413450,event=update_glibc[0Ktravis_time:start:0d1995f8[0Ktravis_time:end:0d1995f8:start=1572057695613047573,finish=1572057695622193012,duration=9145439,event=clean_up_path[0Ktravis_time:start:0c72e777[0Ktravis_time:end:0c72e777:start=1572057695626678714,finish=1572057695635823967,duration=9145253,event=fix_resolv_conf[0Ktravis_time:start:0597d9a2[0Ktravis_time:end:0597d9a2:start=1572057695640822148,finish=1572057695650853412,duration=10031264,event=fix_etc_hosts[0Ktravis_time:start:012519aa[0Ktravis_time:end:012519aa:start=1572057695657932980,finish=1572057695667358064,duration=9425084,event=fix_mvn_settings_xml[0Ktravis_time:start:07fc67a0[0Ktravis_time:end:07fc67a0:start=1572057695672295786,finish=1572057695682650656,duration=10354870,event=no_ipv6_localhost[0Ktravis_time:start:00b3bd4c[0Ktravis_time:end:00b3bd4c:start=1572057695688102126,finish=1572057695690783901,duration=2681775,event=fix_etc_mavenrc[0Ktravis_time:start:1516a994[0Ktravis_time:end:1516a994:start=1572057695696418128,finish=1572057695702415430,duration=5997302,event=fix_wwdr_certificate[0Ktravis_time:start:008082b1[0Ktravis_time:end:008082b1:start=1572057695707007372,finish=1572057695732380930,duration=25373558,event=put_localhost_first[0Ktravis_time:start:10440333[0Ktravis_time:end:10440333:start=1572057695737813711,finish=1572057695742751732,duration=4938021,event=home_paths[0Ktravis_time:start:17fb0780[0Ktravis_time:end:17fb0780:start=1572057695747938311,finish=1572057695762542530,duration=14604219,event=disable_initramfs[0Ktravis_time:start:04931ad8[0Ktravis_time:end:04931ad8:start=1572057695767547640,finish=1572057696108946229,duration=341398589,event=disable_ssh_roaming[0Ktravis_time:start:1e65ac00[0Ktravis_time:end:1e65ac00:start=1572057696114057635,finish=1572057696117194757,duration=3137122,event=debug_tools[0Ktravis_time:start:0328bc9e[0Ktravis_time:end:0328bc9e:start=1572057696122040426,finish=1572057696126653771,duration=4613345,event=uninstall_oclint[0Ktravis_time:start:08d777bb[0Ktravis_time:end:08d777bb:start=1572057696132120567,finish=1572057696135985242,duration=3864675,event=rvm_use[0Ktravis_time:start:0aaebae4[0Ktravis_time:end:0aaebae4:start=1572057696140787746,finish=1572057696151079704,duration=10291958,event=rm_etc_boto_cfg[0Ktravis_time:start:032f32b6[0Ktravis_time:end:032f32b6:start=1572057696156106566,finish=1572057696159475508,duration=3368942,event=rm_oraclejdk8_symlink[0Ktravis_time:start:29ecab00[0Ktravis_time:end:29ecab00:start=1572057696164583723,finish=1572057696221580495,duration=56996772,event=enable_i386[0Ktravis_time:start:0471e469[0Ktravis_time:end:0471e469:start=1572057696226672675,finish=1572057696231829547,duration=5156872,event=update_rubygems[0Ktravis_time:start:0873cfd7[0Ktravis_time:end:0873cfd7:start=1572057696238202479,finish=1572057697282523978,duration=1044321499,event=ensure_path_components[0Ktravis_time:start:16649890[0Ktravis_time:end:16649890:start=1572057697288177415,finish=1572057697292159655,duration=3982240,event=redefine_curl[0Ktravis_time:start:06baf490[0Ktravis_time:end:06baf490:start=1572057697298808190,finish=1572057697354112250,duration=55304060,event=nonblock_pipe[0Ktravis_time:start:0472ba92[0Ktravis_time:end:0472ba92:start=1572057697359613269,finish=1572057700406127192,duration=3046513923,event=apt_get_update[0Ktravis_time:start:1367894d[0Ktravis_time:end:1367894d:start=1572057700411471096,finish=1572057700414506879,duration=3035783,event=deprecate_xcode_64[0Ktravis_time:start:0994d703[0Ktravis_time:end:0994d703:start=1572057700419355124,finish=1572057705279942633,duration=4860587509,event=update_heroku[0Ktravis_time:start:0ca1e260[0Ktravis_time:end:0ca1e260:start=1572057705284895099,finish=1572057705287893494,duration=2998395,event=shell_session_update[0Ktravis_time:start:08495505[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3857
travis_fold:end:docker_mtu[0Ktravis_time:end:08495505:start=1572057705293805917,finish=1572057706489276528,duration=1195470611,event=set_docker_mtu[0Ktravis_time:start:07c62e70[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:07c62e70:start=1572057706492903627,finish=1572057706558914411,duration=66010784,event=resolvconf[0Ktravis_time:start:09d52660[0Ktravis_time:end:09d52660:start=1572057706564148401,finish=1572057706669864801,duration=105716400,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:2b1b56e0[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:2b1b56e0:start=1572057706756142150,finish=1572057707263739780,duration=507597630,event=configure[0Ktravis_time:start:0668325a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0668325a:start=1572057707269166991,finish=1572057717910056282,duration=10640889291,event=configure[0Ktravis_time:start:1e63fdc8[0Ktravis_fold:start:services[0Ktravis_time:start:06c0f8f5[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:06c0f8f5:start=1572057717937751281,finish=1572057717953877271,duration=16125990,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:06c0f8f5:start=1572057717937751281,finish=1572057720959046638,duration=3021295357,event=services[0Ktravis_time:start:1c2c3fb1[0Ktravis_time:end:1c2c3fb1:start=1572057720964560189,finish=1572057720967440599,duration=2880410,event=fix_ps4[0Ktravis_time:start:00ee10e0[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0cc381bc[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0cc381bc:start=1572057720975726685,finish=1572057727221012067,duration=6245285382,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 9921a3e9e3f7596df67493847bbc01f17a3b226e
travis_fold:end:git.checkout[0K
travis_time:end:0cc381bc:start=1572057720975726685,finish=1572057727394902290,duration=6419175605,event=checkout[0Ktravis_time:start:17b0d80e[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:17b0d80e:start=1572057727400080361,finish=1572057727413685111,duration=13604750,event=env[0Ktravis_time:start:059b4cec[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:059b4cec:start=1572057727421150318,finish=1572057727428295561,duration=7145243,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:02e37e4d[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0e7924ce4e1439b836b1bc657d21d9267c7ce1caa718cc2ed2379b53960d51d0
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[1A[2KCreating tutorial-data ... [32mdone[0m[1B[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:02e37e4d:start=1572057727791390631,finish=1572057848743235061,duration=120951844430,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:0c69c8da[0K$ python push.py -s -t of-of_np
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/603099799/log.txt)