## Status: Passing 
Build: [1484](https://travis-ci.org/precice/systemtests/builds/641298046) 

Job: [1484.18](https://travis-ci.org/precice/systemtests/jobs/641298075) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/4c749ac41fec1ac0cc04f8e71fcd731e33705ab1...e37a006c80df4226e1d22b4d0f731f7780eae018) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 16f27b351d9a
 ---> e1da789e3213
Removing intermediate container 16f27b351d9a
Step 3/10 : RUN apk add git bash
 ---> Running in 6a2c67515178
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
 ---> 57b92a7766d4
Removing intermediate container 6a2c67515178
Step 4/10 : ARG branch=develop
 ---> Running in 4526f76ce23e
 ---> 1cb1183723b4
Removing intermediate container 4526f76ce23e
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 23ef4ccb8a93
[91mCloning into 'tutorials'...
[0m ---> 8dbbb99df287
Removing intermediate container 23ef4ccb8a93
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in 52e1b6c8fb92
 ---> 6c7ea5e9eada
Removing intermediate container 52e1b6c8fb92
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in c0ecfc601063
 ---> 78586f685859
Removing intermediate container c0ecfc601063
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in df16432426df
 ---> 91b3b70891e2
Removing intermediate container df16432426df
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 907f45309aa7
 ---> 7d6b8e4bbe5c
Removing intermediate container 907f45309aa7
Step 10/10 : USER [secure]
 ---> Running in 0095f14bd4bd
 ---> f54cccd475db
Removing intermediate container 0095f14bd4bd
Successfully built f54cccd475db
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:eed3979fbded39e8a23ede0f432ef6f195727d13ee124bb42462ecca63a1b1fe
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:148a65e6a226fb094545135eaf2d809db0a9e2ea819f1f171b3fa5e60f8ee190
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
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
Test succeeded! No difference to referenceOutput found.
travis_time:end:0bf9bf59:start=1579866571856843834,finish=1579866857323648492,duration=285466804658,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:02adb455[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:02adb455:start=1579866861364909577,finish=1579866862716273161,duration=1351363584,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:07da7868[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/641298075/log.txt)