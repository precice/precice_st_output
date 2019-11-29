## Status: Passing 
Build: [1231](https://travis-ci.org/precice/systemtests/builds/618755773) 

Job: [1231.13](https://travis-ci.org/precice/systemtests/jobs/618755786) 

Triggered by: [push](https://github.com/precice/systemtests/compare/3b2ed1c3a41a...be71f6e722f0) 

---
Last 100 lines of the job log at the moment of push:
```
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in ccf3fb8e673c
 ---> 0e26c6295953
Removing intermediate container ccf3fb8e673c
Step 3/10 : RUN apk add git bash
 ---> Running in 389184df84db
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
 ---> 11438a4a6a04
Removing intermediate container 389184df84db
Step 4/10 : ARG branch=develop
 ---> Running in 93343143d837
 ---> 0fbcf1ef18d6
Removing intermediate container 93343143d837
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 213ab08aaa5c
[91mCloning into 'tutorials'...
[0m ---> ec69085a477f
Removing intermediate container 213ab08aaa5c
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in c0b51a495f19
 ---> edd7cb234d51
Removing intermediate container c0b51a495f19
Step 7/10 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in d41c35de1311
 ---> e15c9e1030aa
Removing intermediate container d41c35de1311
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in c37c29e5e38f
 ---> 9320bd298919
Removing intermediate container c37c29e5e38f
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 30df1be374e5
 ---> 900d55ca7cbe
Removing intermediate container 30df1be374e5
Step 10/10 : USER [secure]
 ---> Running in 45e3a52f948d
 ---> 7b1af094d37f
Removing intermediate container 45e3a52f948d
Successfully built 7b1af094d37f
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:7b00db50d3ec6c889cf70d30cf34496b571ea714099a139d0b85454c33a752b4
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:04fb9b45c463a12abc14385896740be7f480585561923e21b4c0aa930ecac960
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating su2-adapter
Creating calculix-adapter ... 
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:18814c38:start=1575065691834977971,finish=1575065980785700523,duration=288950722552,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2954f9ce[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2954f9ce:start=1575065985662433928,finish=1575065987351419800,duration=1688985872,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:305ffa81[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618755786/log.txt)