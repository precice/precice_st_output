## Status: Passing 
Build: [1239](https://travis-ci.org/precice/systemtests/builds/619372101) 

Job: [1239.14](https://travis-ci.org/precice/systemtests/jobs/619372117) 

Triggered by: [push](https://github.com/precice/systemtests/compare/cf8e616f4d09...39aadec5ed5b) 

---
Last 100 lines of the job log at the moment of push:
```
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 27916fd7a924
 ---> ac9c93417d88
Removing intermediate container 27916fd7a924
Step 3/10 : RUN apk add git bash
 ---> Running in a8f2432f2dd7
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
 ---> 7d5814bd1580
Removing intermediate container a8f2432f2dd7
Step 4/10 : ARG branch=develop
 ---> Running in 59c01cd59ff3
 ---> 798573b7ce4d
Removing intermediate container 59c01cd59ff3
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1d3f2dc49330
[91mCloning into 'tutorials'...
[0m ---> b590ba355012
Removing intermediate container 1d3f2dc49330
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in b38c6637dec6
 ---> 5a30d2fef9a9
Removing intermediate container b38c6637dec6
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in db95db03230b
 ---> c486b5dadf64
Removing intermediate container db95db03230b
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in 0d0aa21a1fdd
 ---> 694c7bf454bf
Removing intermediate container 0d0aa21a1fdd
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 7d099539d685
 ---> 67869b132808
Removing intermediate container 7d099539d685
Step 10/10 : USER [secure]
 ---> Running in a3df1ba9f1d4
 ---> ee896e1a2f4e
Removing intermediate container a3df1ba9f1d4
Successfully built ee896e1a2f4e
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:cb9e751e559eb7451b60e08bf1b4564e9305cbb017696dc99bdf52617bb290c4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:02485269349d5c200cbb74f33f82824814adcebdc828bcea797e4d77d50808a5
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating calculix-adapter
Creating su2-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2c83b330:start=1575245159588649845,finish=1575245448319652319,duration=288731002474,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0KSuccessfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:17e7eba0:start=1575245453141605510,finish=1575245454813894474,duration=1672288964,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:15b35cc8[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/619372117/log.txt)