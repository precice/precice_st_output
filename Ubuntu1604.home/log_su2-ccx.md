## Status: Passing 
Build: [1520](https://travis-ci.org/precice/systemtests/builds/641980444) 

Job: [1520.18](https://travis-ci.org/precice/systemtests/jobs/641980462) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in bb9627291761
 ---> 8f1f5b9f007d
Removing intermediate container bb9627291761
Step 3/10 : RUN apk add git bash
 ---> Running in 9cc93c0b6dcd
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/11) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/11) Installing ncurses-libs (6.1_p20191130-r0)
(4/11) Installing readline (8.0.1-r0)
(5/11) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/11) Installing ca-certificates (20191127-r0)
(7/11) Installing nghttp2-libs (1.40.0-r0)
(8/11) Installing libcurl (7.67.0-r0)
(9/11) Installing expat (2.2.9-r1)
(10/11) Installing pcre2 (10.34-r1)
(11/11) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 31 MiB in 25 packages
 ---> cb137109dfc8
Removing intermediate container 9cc93c0b6dcd
Step 4/10 : ARG branch=develop
 ---> Running in 88321f708ca7
 ---> 73f525c23df1
Removing intermediate container 88321f708ca7
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in a586729b193e
[91mCloning into 'tutorials'...
[0m ---> 7fef2fdce7aa
Removing intermediate container a586729b193e
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in 480cbee26fe7
 ---> 7df336c0ca75
Removing intermediate container 480cbee26fe7
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 41dbc576c46a
 ---> fd4d9922e053
Removing intermediate container 41dbc576c46a
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 4b0ab0b6de7f
 ---> 8b431bbeea67
Removing intermediate container 4b0ab0b6de7f
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ba93841122f4
 ---> 8ed46f1e7d5c
Removing intermediate container ba93841122f4
Step 10/10 : USER [secure]
 ---> Running in feb2a522504d
 ---> e7dbb1a75648
Removing intermediate container feb2a522504d
Successfully built e7dbb1a75648
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:4631907828a700b11554568e7a59c3d1b25032657373a9801cffe18ff92c7e6e
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:eefcb21a67e666ebfec12dec537830d6a1db814c72e5b02ee7661997fe9871df
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:0117f0f7:start=1580039820268576943,finish=1580040110472052679,duration=290203475736,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2864f24d[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2864f24d:start=1580040114688826268,finish=1580040116080577812,duration=1391751544,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:14174274[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/641980462/log.txt)