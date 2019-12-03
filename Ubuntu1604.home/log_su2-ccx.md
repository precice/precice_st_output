## Status: Passing 
Build: [1248](https://travis-ci.org/precice/systemtests/builds/620247509) 

Job: [1248.13](https://travis-ci.org/precice/systemtests/jobs/620247522) 

Triggered by: [push](https://github.com/precice/systemtests/commit/25da98cf068b) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in b717af8cac18
 ---> 53d188fd51fb
Removing intermediate container b717af8cac18
Step 3/10 : RUN apk add git bash
 ---> Running in 54a67b331300
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
 ---> d7f04c655d93
Removing intermediate container 54a67b331300
Step 4/10 : ARG branch=develop
 ---> Running in 4a279b95812b
 ---> 8bad4ca13809
Removing intermediate container 4a279b95812b
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 6e0ce6dc9a4a
[91mCloning into 'tutorials'...
[0m ---> 9870ca71a7b7
Removing intermediate container 6e0ce6dc9a4a
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 50eaadfa3375
 ---> 08217448058c
Removing intermediate container 50eaadfa3375
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in fbb3b8ca8ff2
 ---> 7a2980b08c5b
Removing intermediate container fbb3b8ca8ff2
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in c163f7b7ba3b
 ---> 797bb2f23021
Removing intermediate container c163f7b7ba3b
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 81356e8a68f9
 ---> 9be0bdf65444
Removing intermediate container 81356e8a68f9
Step 10/10 : USER [secure]
 ---> Running in 84e49c94877a
 ---> 0f934d359ebc
Removing intermediate container 84e49c94877a
Successfully built 0f934d359ebc
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:b4c7818bd0a230a8636f7cdbfa8ca911d10becc540f4f4f8cd6e9e95dde365f4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:d69a881c6660af05bc7717504f64c5667dd18b20531c47908361869cf4ed3db9
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2a1ec70e:start=1575399298341647857,finish=1575399588073921222,duration=289732273365,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:04b48b28[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:04b48b28:start=1575399592704131506,finish=1575399594337294219,duration=1633162713,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:080a02ca[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620247522/log.txt)