## Status: Passing 
Build: [1256](https://travis-ci.org/precice/systemtests/builds/620607294) 

Job: [1256.14](https://travis-ci.org/precice/systemtests/jobs/620607314) 

Triggered by: [push](https://github.com/precice/systemtests/compare/db99b1df1818...f0c87c5da690) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in e872a75bd945
 ---> 1f4d87676ab5
Removing intermediate container e872a75bd945
Step 3/10 : RUN apk add git bash
 ---> Running in 8190db834eb2
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
 ---> dc4524de0c09
Removing intermediate container 8190db834eb2
Step 4/10 : ARG branch=develop
 ---> Running in c7cacd217a91
 ---> 2df69b532cad
Removing intermediate container c7cacd217a91
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in b9367063c7d7
[91mCloning into 'tutorials'...
[0m ---> 4f65aabcb7ca
Removing intermediate container b9367063c7d7
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 88155ca6e8c5
 ---> 2edb964fe6db
Removing intermediate container 88155ca6e8c5
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d1ea85e22ed8
 ---> edccf004bc6b
Removing intermediate container d1ea85e22ed8
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in f496ca0e2deb
 ---> 21fe65560d41
Removing intermediate container f496ca0e2deb
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in cd078d9a1cff
 ---> 9ab5cc3d03a3
Removing intermediate container cd078d9a1cff
Step 10/10 : USER [secure]
 ---> Running in 132431347a50
 ---> 36337b2e876b
Removing intermediate container 132431347a50
Successfully built 36337b2e876b
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:86c6e9db47764d2a510483b4e76acdef741f1ec728d8d7efb0e9387ed0eaec96
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:b426b427296a80b54cf73cd42f48b4711ff94a8debae4355ba0fbdaece726388
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0a49c09a:start=1575466694575964596,finish=1575466995861247707,duration=301285283111,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0f46dd3c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0f46dd3c:start=1575467000206598576,finish=1575467001809331025,duration=1602732449,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:00058610[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620607314/log.txt)