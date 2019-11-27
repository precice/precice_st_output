## Status: Passing 
Build: [1157](https://travis-ci.org/precice/systemtests/builds/617667611) 

Job: [1157.13](https://travis-ci.org/precice/systemtests/jobs/617667624) 

Triggered by: [push](https://github.com/precice/systemtests/compare/develop) 

---
Last 100 lines of the job log at the moment of push:
```
  input_solid: {}
  output: {}

Creating network "testcomposesu2ccx_default" with the default driver
Creating network "testcomposesu2ccx_[secure]comm" with the default driver
Creating volume "testcomposesu2ccx_output" with default driver
Creating volume "testcomposesu2ccx_configs" with default driver
Creating volume "testcomposesu2ccx_input_solid" with default driver
Creating volume "testcomposesu2ccx_input_fluid" with default driver
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/9 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 1796c61fea9b
 ---> 1023f268aee4
Removing intermediate container 1796c61fea9b
Step 3/9 : RUN apk add git bash
 ---> Running in 09ef988419c2
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20190518-r0)
(2/11) Installing ncurses-terminfo (6.1_p20190518-r0)
(3/11) Installing ncurses-libs (6.1_p20190518-r0)
(4/11) Installing readline (8.0.0-r0)
(5/11) Installing bash (5.0.0-r0)
Executing bash-5.0.0-r0.post-install
(6/11) Installing ca-certificates (20190108-r0)
(7/11) Installing nghttp2-libs (1.39.2-r0)
(8/11) Installing libcurl (7.66.0-r0)
(9/11) Installing expat (2.2.8-r0)
(10/11) Installing pcre2 (10.33-r0)
(11/11) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 30 MiB in 25 packages
 ---> 83172ed57ccb
Removing intermediate container 09ef988419c2
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in a307abbf5512
[91mCloning into 'tutorials'...
[0m ---> f3638b671f4c
Removing intermediate container a307abbf5512
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 0e3927faffaa
 ---> 0aeb4740aa04
Removing intermediate container 0e3927faffaa
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 2f774e8d9eb8
 ---> a085d8b24c24
Removing intermediate container 2f774e8d9eb8
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 648eef3f7ef0
 ---> 0109dc2935d9
Removing intermediate container 648eef3f7ef0
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 6efb4ff2420e
 ---> d681332bb9b3
Removing intermediate container 6efb4ff2420e
Step 9/9 : USER [secure]
 ---> Running in 1dbee106d966
 ---> c81148ddf42b
Removing intermediate container 1dbee106d966
Successfully built c81148ddf42b
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:438381be0f86cb7ffb170693a86c15d817cb5137d806df7610530392648f293e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:f04e59abcf38701a98708c43362cab6e9bcc0c03e49b1d34bec20fbf9235ff29
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0963e885:start=1574855928551124282,finish=1574856277471999630,duration=348920875348,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:033cb538[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:033cb538:start=1574856282531962197,finish=1574856284297972896,duration=1766010699,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:17c72d94[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/617667624/log.txt)