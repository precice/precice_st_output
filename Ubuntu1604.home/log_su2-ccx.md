## Status: Passing 
Build: [1521](https://travis-ci.org/precice/systemtests/builds/642317432) 

Job: [1521.18](https://travis-ci.org/precice/systemtests/jobs/642317450) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in dac7431a25c3
 ---> 9f02a6c79437
Removing intermediate container dac7431a25c3
Step 3/10 : RUN apk add git bash
 ---> Running in a20651053b7c
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
 ---> f8dbce446801
Removing intermediate container a20651053b7c
Step 4/10 : ARG branch=develop
 ---> Running in 895d719c453c
 ---> 44573c136f0d
Removing intermediate container 895d719c453c
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 250f4ca87588
[91mCloning into 'tutorials'...
[0m ---> b85ed112238b
Removing intermediate container 250f4ca87588
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in b7ae74b23d95
 ---> 07a68b5f8db9
Removing intermediate container b7ae74b23d95
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 98e642191559
 ---> eb499ec6f6ba
Removing intermediate container 98e642191559
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in e483e027f36b
 ---> 9e851f0128f7
Removing intermediate container e483e027f36b
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0273322fa3ea
 ---> 87d5db7a2790
Removing intermediate container 0273322fa3ea
Step 10/10 : USER [secure]
 ---> Running in 505d7bbb513b
 ---> 4db5a6e0ca50
Removing intermediate container 505d7bbb513b
Successfully built 4db5a6e0ca50
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:024b3d5390dab7eec048726f52604ddf70756d8ec6c488d40035c127ca3de2ce
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:7ca57018cdb29450cf1279ee145a07e26994e6621d1a4a27ae52f87131d903f2
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:2170cfa4:start=1580125237376831042,finish=1580125527659650258,duration=290282819216,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:07359851[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:07359851:start=1580125531729985601,finish=1580125533145571252,duration=1415585651,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:3305c958[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/642317450/log.txt)