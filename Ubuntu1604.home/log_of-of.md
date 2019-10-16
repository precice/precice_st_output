 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598777025) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/521ff68ed5cc...3211dcc17558) 
## Last 100 lines of the job log at the moment of push...
```
 [34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:167346c6:start=1571250993402625780,finish=1571250993408563755,duration=5937975,event=show_system_info[0Ktravis_time:start:30d9dd8f[0Ktravis_time:end:30d9dd8f:start=1571250993411470900,finish=1571250993438119444,duration=26648544,event=rm_riak_source[0Ktravis_time:start:0efb5330[0Ktravis_time:end:0efb5330:start=1571250993441466863,finish=1571250993447026662,duration=5559799,event=fix_rwky_redis[0Ktravis_time:start:046d9c16[0Ktravis_time:end:046d9c16:start=1571250993450292554,finish=1571250993862834953,duration=412542399,event=wait_for_network[0Ktravis_time:start:08160f30[0Ktravis_time:end:08160f30:start=1571250993867786915,finish=1571250995431313521,duration=1563526606,event=update_apt_keys[0Ktravis_time:start:18b392f2[0Ktravis_time:end:18b392f2:start=1571250995436332077,finish=1571250996512803017,duration=1076470940,event=fix_hhvm_source[0Ktravis_time:start:033c6b2b[0Ktravis_time:end:033c6b2b:start=1571250996517962961,finish=1571250996528353595,duration=10390634,event=update_mongo_arch[0Ktravis_time:start:126c5b74[0Ktravis_time:end:126c5b74:start=1571250996533116302,finish=1571250996575439834,duration=42323532,event=fix_sudo_enabled_trusty[0Ktravis_time:start:00ed2e1c[0Ktravis_time:end:00ed2e1c:start=1571250996580492451,finish=1571250996583402876,duration=2910425,event=update_glibc[0Ktravis_time:start:167d9e10[0Ktravis_time:end:167d9e10:start=1571250996588797340,finish=1571250996598258101,duration=9460761,event=clean_up_path[0Ktravis_time:start:016567fb[0Ktravis_time:end:016567fb:start=1571250996602540662,finish=1571250996612041737,duration=9501075,event=fix_resolv_conf[0Ktravis_time:start:003c8dc0[0Ktravis_time:end:003c8dc0:start=1571250996617592602,finish=1571250996627105856,duration=9513254,event=fix_etc_hosts[0Ktravis_time:start:17670dbc[0Ktravis_time:end:17670dbc:start=1571250996633446605,finish=1571250996642834769,duration=9388164,event=fix_mvn_settings_xml[0Ktravis_time:start:032210af[0Ktravis_time:end:032210af:start=1571250996647510106,finish=1571250996657997314,duration=10487208,event=no_ipv6_localhost[0Ktravis_time:start:0750aed6[0Ktravis_time:end:0750aed6:start=1571250996662528009,finish=1571250996665491934,duration=2963925,event=fix_etc_mavenrc[0Ktravis_time:start:19580e56[0Ktravis_time:end:19580e56:start=1571250996670043098,finish=1571250996675487587,duration=5444489,event=fix_wwdr_certificate[0Ktravis_time:start:20e0691d[0Ktravis_time:end:20e0691d:start=1571250996679648400,finish=1571250996704822082,duration=25173682,event=put_localhost_first[0Ktravis_time:start:0fa5c300[0Ktravis_time:end:0fa5c300:start=1571250996708722174,finish=1571250996713079436,duration=4357262,event=home_paths[0Ktravis_time:start:048783c4[0Ktravis_time:end:048783c4:start=1571250996719685070,finish=1571250996732146011,duration=12460941,event=disable_initramfs[0Ktravis_time:start:0533f01c[0Ktravis_time:end:0533f01c:start=1571250996737059413,finish=1571250997073722129,duration=336662716,event=disable_ssh_roaming[0Ktravis_time:start:1e2acdc4[0Ktravis_time:end:1e2acdc4:start=1571250997078630041,finish=1571250997082576546,duration=3946505,event=debug_tools[0Ktravis_time:start:1b556540[0Ktravis_time:end:1b556540:start=1571250997087148203,finish=1571250997091907700,duration=4759497,event=uninstall_oclint[0Ktravis_time:start:1d178fe1[0Ktravis_time:end:1d178fe1:start=1571250997097028661,finish=1571250997101289710,duration=4261049,event=rvm_use[0Ktravis_time:start:00bc8509[0Ktravis_time:end:00bc8509:start=1571250997104940232,finish=1571250997116757339,duration=11817107,event=rm_etc_boto_cfg[0Ktravis_time:start:102a42a4[0Ktravis_time:end:102a42a4:start=1571250997121565722,finish=1571250997124813441,duration=3247719,event=rm_oraclejdk8_symlink[0Ktravis_time:start:076527b0[0Ktravis_time:end:076527b0:start=1571250997128833521,finish=1571250997198937124,duration=70103603,event=enable_i386[0Ktravis_time:start:0700bd35[0Ktravis_time:end:0700bd35:start=1571250997204617852,finish=1571250997209012599,duration=4394747,event=update_rubygems[0Ktravis_time:start:117e6204[0Ktravis_time:end:117e6204:start=1571250997213759966,finish=1571250998244816719,duration=1031056753,event=ensure_path_components[0Ktravis_time:start:0822c670[0Ktravis_time:end:0822c670:start=1571250998249417681,finish=1571250998252566756,duration=3149075,event=redefine_curl[0Ktravis_time:start:09b2a49e[0Ktravis_time:end:09b2a49e:start=1571250998256416539,finish=1571250998313067965,duration=56651426,event=nonblock_pipe[0Ktravis_time:start:02cd0993[0Ktravis_time:end:02cd0993:start=1571250998318636317,finish=1571251000872821120,duration=2554184803,event=apt_get_update[0Ktravis_time:start:035c2387[0Ktravis_time:end:035c2387:start=1571251000878755044,finish=1571251000881760635,duration=3005591,event=deprecate_xcode_64[0Ktravis_time:start:2d456834[0Ktravis_time:end:2d456834:start=1571251000886281158,finish=1571251005871917391,duration=4985636233,event=update_heroku[0Ktravis_time:start:18711c00[0Ktravis_time:end:18711c00:start=1571251005877191167,finish=1571251005879998929,duration=2807762,event=shell_session_update[0Ktravis_time:start:063de8e1[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3949
travis_fold:end:docker_mtu[0Ktravis_time:end:063de8e1:start=1571251005884293516,finish=1571251007083807760,duration=1199514244,event=set_docker_mtu[0Ktravis_time:start:0128320b[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:0128320b:start=1571251007088467717,finish=1571251007154975428,duration=66507711,event=resolvconf[0Ktravis_time:start:09b5cdae[0Ktravis_time:end:09b5cdae:start=1571251007159403113,finish=1571251007265474313,duration=106071200,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:004e1ccb[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:004e1ccb:start=1571251007349004447,finish=1571251007732511498,duration=383507051,event=configure[0Ktravis_time:start:12114396[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:12114396:start=1571251007737716671,finish=1571251018050774188,duration=10313057517,event=configure[0Ktravis_time:start:03e1f51f[0Ktravis_fold:start:services[0Ktravis_time:start:005e1538[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:005e1538:start=1571251018076738765,finish=1571251018091271058,duration=14532293,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:005e1538:start=1571251018076738765,finish=1571251021097620610,duration=3020881845,event=services[0Ktravis_time:start:00837146[0Ktravis_time:end:00837146:start=1571251021102588029,finish=1571251021105902599,duration=3314570,event=fix_ps4[0Ktravis_time:start:1f35c290[0K
travis_fold:start:git.checkout[0Ktravis_time:start:121c598c[0K$ git clone --depth=50 --branch=EderK-allow_job_failure https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:121c598c:start=1571251021115139079,finish=1571251027487586343,duration=6372447264,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 3211dcc1755868c679464cbce21d403786e5efbd
travis_fold:end:git.checkout[0K
travis_time:end:121c598c:start=1571251021115139079,finish=1571251027881163171,duration=6766024092,event=checkout[0Ktravis_time:start:15b0153a[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:15b0153a:start=1571251027886124557,finish=1571251027896309433,duration=10184876,event=env[0Ktravis_time:start:1b044fcc[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:1b044fcc:start=1571251027900593803,finish=1571251027906279640,duration=5685837,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:2162ae38[0K$ python system_testing.py -s of-of
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
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1fbbe987a815dac9bffdd6008e7730aa1d4a6b6821756b69e4863d8965bd1dcd
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid
Creating openfoam-adapter-solid
Creating tutorial-data
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598777039/log.txt)