## Status: Passing 
Build: [1162](https://travis-ci.org/precice/systemtests/builds/617695037) 

Job: [1162.13](https://travis-ci.org/precice/systemtests/jobs/617695050) 

Triggered by: [push](https://github.com/precice/systemtests/commit/e19c9061ae73) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 787422aa26a5
 ---> 1e85abb18678
Removing intermediate container 787422aa26a5
Step 3/10 : RUN apk add git bash
 ---> Running in f299d1a8f322
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
 ---> ad00ed50e876
Removing intermediate container f299d1a8f322
Step 4/10 : ARG branch=develop
 ---> Running in 5e21a788be20
 ---> 7f033d8a2377
Removing intermediate container 5e21a788be20
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in cda8869f4c1f
[91mCloning into 'tutorials'...
[0m ---> a3b0c90165bf
Removing intermediate container cda8869f4c1f
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 3c4344f9df5f
 ---> e54771fee656
Removing intermediate container 3c4344f9df5f
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in ba1d37b3fa31
 ---> 9856054cad4e
Removing intermediate container ba1d37b3fa31
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in c67a092f33ac
 ---> 3ab5db351e2d
Removing intermediate container c67a092f33ac
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0be0aa4b1c78
 ---> 8640a284d7be
Removing intermediate container 0be0aa4b1c78
Step 10/10 : USER [secure]
 ---> Running in 64792ffa5c0e
 ---> b4586abe82b5
Removing intermediate container 64792ffa5c0e
Successfully built b4586abe82b5
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:68fc44da63ef258f07b87a257fa01baaa5f488d5c5030214a78bd6713e180ded
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:aa54ec1ffc2a83414c7a6aad7975a5b4170b895f1768ba004529cd734f1e8d7e
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:20cba6af:start=1574867714081462417,finish=1574868002590150506,duration=288508688089,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0248996a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0248996a:start=1574868007167774793,finish=1574868008824191612,duration=1656416819,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:18c2e670[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/617695050/log.txt)