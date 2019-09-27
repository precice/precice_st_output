 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/590477881) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aac1a14c474b...0cb7c0ec452f) 
## Last 100 lines of the job log at the moment of push...
```
 travis_fold:end:system_info[0K
travis_time:end:022760c0:start=1569601961436766825,finish=1569601961442352140,duration=5585315,event=show_system_info[0Ktravis_time:start:10133650[0Ktravis_time:end:10133650:start=1569601961445404563,finish=1569601961472262985,duration=26858422,event=rm_riak_source[0Ktravis_time:start:0185e8e5[0Ktravis_time:end:0185e8e5:start=1569601961476354281,finish=1569601961482545840,duration=6191559,event=fix_rwky_redis[0Ktravis_time:start:132ba657[0Ktravis_time:end:132ba657:start=1569601961486915056,finish=1569601964089104888,duration=2602189832,event=wait_for_network[0Ktravis_time:start:0051738a[0Ktravis_time:end:0051738a:start=1569601964093689595,finish=1569601965661116859,duration=1567427264,event=update_apt_keys[0Ktravis_time:start:1c3d7e58[0Ktravis_time:end:1c3d7e58:start=1569601965665234811,finish=1569601966716160765,duration=1050925954,event=fix_hhvm_source[0Ktravis_time:start:03670eab[0Ktravis_time:end:03670eab:start=1569601966720419293,finish=1569601966731487784,duration=11068491,event=update_mongo_arch[0Ktravis_time:start:2b346808[0Ktravis_time:end:2b346808:start=1569601966735181751,finish=1569601966778320372,duration=43138621,event=fix_sudo_enabled_trusty[0Ktravis_time:start:04a0b368[0Ktravis_time:end:04a0b368:start=1569601966783068766,finish=1569601966786034929,duration=2966163,event=update_glibc[0Ktravis_time:start:13ba36db[0Ktravis_time:end:13ba36db:start=1569601966789971801,finish=1569601966798510677,duration=8538876,event=clean_up_path[0Ktravis_time:start:1b880470[0Ktravis_time:end:1b880470:start=1569601966803380975,finish=1569601966811914415,duration=8533440,event=fix_resolv_conf[0Ktravis_time:start:01ab8902[0Ktravis_time:end:01ab8902:start=1569601966816898070,finish=1569601966826756510,duration=9858440,event=fix_etc_hosts[0Ktravis_time:start:13019ba4[0Ktravis_time:end:13019ba4:start=1569601966832351076,finish=1569601966841169829,duration=8818753,event=fix_mvn_settings_xml[0Ktravis_time:start:022094d0[0Ktravis_time:end:022094d0:start=1569601966848037585,finish=1569601966858926218,duration=10888633,event=no_ipv6_localhost[0Ktravis_time:start:0b636534[0Ktravis_time:end:0b636534:start=1569601966864224631,finish=1569601966868440024,duration=4215393,event=fix_etc_mavenrc[0Ktravis_time:start:04cb3044[0Ktravis_time:end:04cb3044:start=1569601966873737308,finish=1569601966877439159,duration=3701851,event=fix_wwdr_certificate[0Ktravis_time:start:00e83bb0[0Ktravis_time:end:00e83bb0:start=1569601966882919352,finish=1569601966910549211,duration=27629859,event=put_localhost_first[0Ktravis_time:start:34d3722c[0Ktravis_time:end:34d3722c:start=1569601966915907722,finish=1569601966919711713,duration=3803991,event=home_paths[0Ktravis_time:start:20b1097c[0Ktravis_time:end:20b1097c:start=1569601966923838133,finish=1569601966937807737,duration=13969604,event=disable_initramfs[0Ktravis_time:start:011d657c[0Ktravis_time:end:011d657c:start=1569601966942776561,finish=1569601967258730805,duration=315954244,event=disable_ssh_roaming[0Ktravis_time:start:076ac6cd[0Ktravis_time:end:076ac6cd:start=1569601967263797063,finish=1569601967267007211,duration=3210148,event=debug_tools[0Ktravis_time:start:02aa1154[0Ktravis_time:end:02aa1154:start=1569601967272321407,finish=1569601967276328800,duration=4007393,event=uninstall_oclint[0Ktravis_time:start:046b956e[0Ktravis_time:end:046b956e:start=1569601967281633183,finish=1569601967285649312,duration=4016129,event=rvm_use[0Ktravis_time:start:053691cc[0Ktravis_time:end:053691cc:start=1569601967289935356,finish=1569601967299418762,duration=9483406,event=rm_etc_boto_cfg[0Ktravis_time:start:023b298e[0Ktravis_time:end:023b298e:start=1569601967303677298,finish=1569601967306399276,duration=2721978,event=rm_oraclejdk8_symlink[0Ktravis_time:start:079fb23e[0Ktravis_time:end:079fb23e:start=1569601967311683413,finish=1569601967379172338,duration=67488925,event=enable_i386[0Ktravis_time:start:0256358a[0Ktravis_time:end:0256358a:start=1569601967384866523,finish=1569601967390781512,duration=5914989,event=update_rubygems[0Ktravis_time:start:0cae8328[0Ktravis_time:end:0cae8328:start=1569601967396882842,finish=1569601968411702594,duration=1014819752,event=ensure_path_components[0Ktravis_time:start:3f59b82e[0Ktravis_time:end:3f59b82e:start=1569601968416824822,finish=1569601968420079967,duration=3255145,event=redefine_curl[0Ktravis_time:start:04f17000[0Ktravis_time:end:04f17000:start=1569601968424418665,finish=1569601968477030637,duration=52611972,event=nonblock_pipe[0Ktravis_time:start:010a3dd0[0Ktravis_time:end:010a3dd0:start=1569601968481856641,finish=1569601968548404473,duration=66547832,event=apt_get_update[0Ktravis_time:start:00897e36[0Ktravis_time:end:00897e36:start=1569601968553282120,finish=1569601968556035499,duration=2753379,event=deprecate_xcode_64[0Ktravis_time:start:1735bbfc[0Ktravis_time:end:1735bbfc:start=1569601968561832738,finish=1569601973137286955,duration=4575454217,event=update_heroku[0Ktravis_time:start:04ec0e6c[0Ktravis_time:end:04ec0e6c:start=1569601973141652360,finish=1569601973144419830,duration=2767470,event=shell_session_update[0Ktravis_time:start:029b5774[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3968
travis_fold:end:docker_mtu[0Ktravis_time:end:029b5774:start=1569601973149820178,finish=1569601974342915627,duration=1193095449,event=set_docker_mtu[0Ktravis_time:start:106bd095[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:106bd095:start=1569601974347474455,finish=1569601974415001235,duration=67526780,event=resolvconf[0Ktravis_time:start:009726a0[0Ktravis_time:end:009726a0:start=1569601974420221585,finish=1569601974514382579,duration=94160994,event=maven_central_mirror[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:04345bac[0K$ curl -sSf -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:04345bac:start=1569601974599885826,finish=1569601974970151301,duration=370265475,event=configure[0Ktravis_time:start:0d61ea8a[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:0d61ea8a:start=1569601974976454119,finish=1569601984743684514,duration=9767230395,event=configure[0Ktravis_time:start:0589944a[0Ktravis_fold:start:services[0Ktravis_time:start:0810ef1c[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0810ef1c:start=1569601984769085178,finish=1569601984783246429,duration=14161251,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0810ef1c:start=1569601984769085178,finish=1569601987789095328,duration=3020010150,event=services[0Ktravis_time:start:123d0740[0Ktravis_time:end:123d0740:start=1569601987793947157,finish=1569601987797523634,duration=3576477,event=fix_ps4[0Ktravis_time:start:02b82dc9[0K
travis_fold:start:git.checkout[0Ktravis_time:start:1caf3488[0K$ git clone --depth=50 --branch=master https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:1caf3488:start=1569601987807704101,finish=1569601993995611126,duration=6187907025,event=checkout[0K$ cd [secure]/systemtests
$ git checkout -qf 0cb7c0ec452fe910f18f20068ea48a8454783584
travis_fold:end:git.checkout[0K
travis_time:end:1caf3488:start=1569601987807704101,finish=1569601994947482900,duration=7139778799,event=checkout[0Ktravis_time:start:1ce5aa98[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:1ce5aa98:start=1569601994952479350,finish=1569601994964616223,duration=12136873,event=env[0Ktravis_time:start:0d4e1c7d[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0d4e1c7d:start=1569601994970706046,finish=1569601994977059764,duration=6353718,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:03bd101d[0K$ python system_testing.py -s of-of
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
Digest: sha256:4b82e4be1faab3a717869bbe4a1c5596b280ffc8b238f309af508227b7516916
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03bd101d:start=1569601995330231179,finish=1569602115702542815,duration=120372311636,event=script[0K[32;1mThe command "python system_testing.py -s of-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:26ee4ab8[0K$ python push.py -s -t of-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/590477895/log.txt)