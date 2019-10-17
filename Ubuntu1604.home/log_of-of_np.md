 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599241988) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/58fea094b8a4...67d504057297) 
## Last 100 lines of the job log at the moment of push...
```
   hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:3dbcd2e4:start=1571334797683407063,finish=1571334797689242331,duration=5835268,event=show_system_info[0Ktravis_time:start:0b4af41c[0Ktravis_time:end:0b4af41c:start=1571334797691974632,finish=1571334797720027719,duration=28053087,event=rm_riak_source[0Ktravis_time:start:21269348[0Ktravis_time:end:21269348:start=1571334797723684637,finish=1571334797729922735,duration=6238098,event=fix_rwky_redis[0Ktravis_time:start:008030ec[0Ktravis_time:end:008030ec:start=1571334797735324345,finish=1571334798138175139,duration=402850794,event=wait_for_network[0Ktravis_time:start:2f7eb452[0Ktravis_time:end:2f7eb452:start=1571334798143650761,finish=1571334799699236603,duration=1555585842,event=update_apt_keys[0Ktravis_time:start:3c69b082[0Ktravis_time:end:3c69b082:start=1571334799704508502,finish=1571334800750046745,duration=1045538243,event=fix_hhvm_source[0Ktravis_time:start:0bdbb5e8[0Ktravis_time:end:0bdbb5e8:start=1571334800754806643,finish=1571334800765102886,duration=10296243,event=update_mongo_arch[0Ktravis_time:start:0005cf0e[0Ktravis_time:end:0005cf0e:start=1571334800769528992,finish=1571334800812588530,duration=43059538,event=fix_sudo_enabled_trusty[0Ktravis_time:start:038861b8[0Ktravis_time:end:038861b8:start=1571334800817050656,finish=1571334800819745663,duration=2695007,event=update_glibc[0Ktravis_time:start:058bcf6c[0Ktravis_time:end:058bcf6c:start=1571334800823981910,finish=1571334800833842232,duration=9860322,event=clean_up_path[0Ktravis_time:start:14c3a189[0Ktravis_time:end:14c3a189:start=1571334800838322310,finish=1571334800849953973,duration=11631663,event=fix_resolv_conf[0Ktravis_time:start:012acdc6[0Ktravis_time:end:012acdc6:start=1571334800854915277,finish=1571334800865298368,duration=10383091,event=fix_etc_hosts[0Ktravis_time:start:03568a8a[0Ktravis_time:end:03568a8a:start=1571334800872402194,finish=1571334800882084276,duration=9682082,event=fix_mvn_settings_xml[0Ktravis_time:start:04a433ec[0Ktravis_time:end:04a433ec:start=1571334800886911849,finish=1571334800898358499,duration=11446650,event=no_ipv6_localhost[0Ktravis_time:start:034891aa[0Ktravis_time:end:034891aa:start=1571334800903230679,finish=1571334800905898173,duration=2667494,event=fix_etc_mavenrc[0Ktravis_time:start:03d23534[0Ktravis_time:end:03d23534:start=1571334800910419925,finish=1571334800914042171,duration=3622246,event=fix_wwdr_certificate[0Ktravis_time:start:0eb7a352[0Ktravis_time:end:0eb7a352:start=1571334800919360655,finish=1571334800944708472,duration=25347817,event=put_localhost_first[0Ktravis_time:start:021cd5d8[0Ktravis_time:end:021cd5d8:start=1571334800950350335,finish=1571334800954404448,duration=4054113,event=home_paths[0Ktravis_time:start:06933ba7[0Ktravis_time:end:06933ba7:start=1571334800958756531,finish=1571334800972703730,duration=13947199,event=disable_initramfs[0Ktravis_time:start:0046ded2[0Ktravis_time:end:0046ded2:start=1571334800977043555,finish=1571334801328953094,duration=351909539,event=disable_ssh_roaming[0Ktravis_time:start:0dc23c42[0Ktravis_time:end:0dc23c42:start=1571334801333321578,finish=1571334801336097207,duration=2775629,event=debug_tools[0Ktravis_time:start:15f87008[0Ktravis_time:end:15f87008:start=1571334801340912845,finish=1571334801345436426,duration=4523581,event=uninstall_oclint[0Ktravis_time:start:25848546[0Ktravis_time:end:25848546:start=1571334801350300161,finish=1571334801355319188,duration=5019027,event=rvm_use[0Ktravis_time:start:0301c6a9[0Ktravis_time:end:0301c6a9:start=1571334801362720951,finish=1571334801371241161,duration=8520210,event=rm_etc_boto_cfg[0Ktravis_time:start:016942d0[0Ktravis_time:end:016942d0:start=1571334801376902289,finish=1571334801380828465,duration=3926176,event=rm_oraclejdk8_symlink[0Ktravis_time:start:1f670c6f[0Ktravis_time:end:1f670c6f:start=1571334801387715233,finish=1571334801444234790,duration=56519557,event=enable_i386[0Ktravis_time:start:0d39420f[0Ktravis_time:end:0d39420f:start=1571334801448747317,finish=1571334801453103401,duration=4356084,event=update_rubygems[0Ktravis_time:start:22897b28[0Ktravis_time:end:22897b28:start=1571334801458174740,finish=1571334802457784459,duration=999609719,event=ensure_path_components[0Ktravis_time:start:01437dc8[0Ktravis_time:end:01437dc8:start=1571334802462911562,finish=1571334802466182563,duration=3271001,event=redefine_curl[0Ktravis_time:start:02c9ba7e[0Ktravis_time:end:02c9ba7e:start=1571334802470971693,finish=1571334802527005614,duration=56033921,event=nonblock_pipe[0Ktravis_time:start:0c7cfb8a[0Ktravis_time:end:0c7cfb8a:start=1571334802531326132,finish=1571334802582719622,duration=51393490,event=apt_get_update[0Ktravis_time:start:0befae97[0Ktravis_time:end:0befae97:start=1571334802587845381,finish=1571334802591401275,duration=3555894,event=deprecate_xcode_64[0Ktravis_time:start:15b5cf65[0Ktravis_time:end:15b5cf65:start=1571334802595185317,finish=1571334807464316862,duration=4869131545,event=update_heroku[0Ktravis_time:start:2792658c[0Ktravis_time:end:2792658c:start=1571334807468202311,finish=1571334807470927414,duration=2725103,event=shell_session_update[0Ktravis_time:start:0b7c9ecb[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3859
travis_fold:end:docker_mtu[0Ktravis_time:end:0b7c9ecb:start=1571334807474581245,finish=1571334808675942112,duration=1201360867,event=set_docker_mtu[0Ktravis_time:start:01f19bc7[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:01f19bc7:start=1571334808680113165,finish=1571334808744578386,duration=64465221,event=resolvconf[0Ktravis_time:start:1cfb41b0[0Ktravis_time:end:1cfb41b0:start=1571334808749255612,finish=1571334808853325394,duration=104069782,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:006f5942[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:006f5942:start=1571334808935145055,finish=1571334809347520233,duration=412375178,event=configure[0Ktravis_time:start:00ac42e6[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:00ac42e6:start=1571334809353623621,finish=1571334819382437271,duration=10028813650,event=configure[0Ktravis_time:start:02b96100[0Ktravis_fold:start:services[0Ktravis_time:start:0d2eed82[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0d2eed82:start=1571334819408131751,finish=1571334819422614763,duration=14483012,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0d2eed82:start=1571334819408131751,finish=1571334822428281570,duration=3020149819,event=services[0Ktravis_time:start:181a385e[0Ktravis_time:end:181a385e:start=1571334822432996100,finish=1571334822435654756,duration=2658656,event=fix_ps4[0Ktravis_time:start:28ebebf5[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1a3ab280[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1a3ab280:start=1571334822445495338,finish=1571334828695045593,duration=6249550255,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 67d50405729725689cb7247b9b7b61e8cd0610e4
travis_fold:end:git.checkout[0K
travis_time:end:1a3ab280:start=1571334822445495338,finish=1571334829298666274,duration=6853170936,event=checkout[0Ktravis_time:start:102f102c[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:102f102c:start=1571334829303438564,finish=1571334829315586331,duration=12147767,event=env[0Ktravis_time:start:1d4e2e66[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1d4e2e66:start=1571334829320165945,finish=1571334829326478568,duration=6312623,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:16206bb8[0K$ python system_testing.py -s of-of_np
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9d0c3e1b98eaa8f1a730eb5f148bb2285fb17194b6695041112ff9c6279b21ed
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
 ```
[Full job log](https://api.travis-ci.org/v3/job/599242008/log.txt)