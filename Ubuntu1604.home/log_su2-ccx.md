## Status: Passing 
Build: [1275](https://travis-ci.org/precice/systemtests/builds/621555096) 

Job: [1275.14](https://travis-ci.org/precice/systemtests/jobs/621555110) 

Triggered by: [push](https://github.com/precice/systemtests/compare/b8adc727aafb...aff84f792bf7) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in d6d4182b78a5
 ---> 4501569ae85c
Removing intermediate container d6d4182b78a5
Step 3/10 : RUN apk add git bash
 ---> Running in 46929b50813e
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
 ---> 5e6160f53450
Removing intermediate container 46929b50813e
Step 4/10 : ARG branch=develop
 ---> Running in c66743225bee
 ---> acef0ab5a99f
Removing intermediate container c66743225bee
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 440b176184ac
[91mCloning into 'tutorials'...
[0m ---> 77cbde5e3591
Removing intermediate container 440b176184ac
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 0146e7459b4f
 ---> 155ca49c1831
Removing intermediate container 0146e7459b4f
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d1bd88cabf6f
 ---> e1477bca6381
Removing intermediate container d1bd88cabf6f
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in ce418e677e27
 ---> dc48750063c5
Removing intermediate container ce418e677e27
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 972c229fd7e7
 ---> df62cd4407b7
Removing intermediate container 972c229fd7e7
Step 10/10 : USER [secure]
 ---> Running in 520c631fe112
 ---> b1d671fa2b62
Removing intermediate container 520c631fe112
Successfully built b1d671fa2b62
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:269804a9622691717a895d8830ebc3f06eec1d2773d180930eaf0d35171e0ef5
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:1ca9cf27c264d44919f37cb23bcd8356f1f9bdd08b03bfd6b7f12130fda2e435
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
######################this is now the newest commit!##################
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:063ca470:start=1575641085516851364,finish=1575641373513949160,duration=287997097796,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04c33c10[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04c33c10:start=1575641377606573455,finish=1575641378967111385,duration=1360537930,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:262645fb[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/621555110/log.txt)