## Status: Passing 
Build: [1134](https://travis-ci.org/precice/systemtests/builds/616642276) 

Job: [1134.13](https://travis-ci.org/precice/systemtests/jobs/616642289) 

Triggered by: [push](https://github.com/precice/systemtests/commit/0d3b5a2c0bbe) 

---
Last 100 lines of the job log at the moment of push:
```
Building tutorial-data
Step 1/9 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/9 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in 7b329da39ca2
 ---> 51dde075d875
Removing intermediate container 7b329da39ca2
Step 3/9 : RUN apk add git bash
 ---> Running in 64b48ee888af
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
 ---> 775b926c4e1c
Removing intermediate container 64b48ee888af
Step 4/9 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in b3d4220c24ef
[91mCloning into 'tutorials'...
[0m ---> 281e5d4e4893
Removing intermediate container b3d4220c24ef
Step 5/9 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config_serial.xml  > configs/[secure]-config.xml
 ---> Running in 42ba01e5495d
 ---> d4da3041805e
Removing intermediate container 42ba01e5495d
Step 6/9 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 2d7b4f51509b
 ---> d5d3fd44b96c
Removing intermediate container 2d7b4f51509b
Step 7/9 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in ecb2856ca30a
 ---> ef516b19212f
Removing intermediate container ecb2856ca30a
Step 8/9 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in fb8e776a2fff
 ---> 5fa37afb7ed1
Removing intermediate container fb8e776a2fff
Step 9/9 : USER [secure]
 ---> Running in c7842a6b741d
 ---> e545a4fed20b
Removing intermediate container c7842a6b741d
Successfully built e545a4fed20b
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:0662464aa216afb229ee0f28dcf699e638117125e116527d57c65add6618ef2c
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:27c2a4eb0df234fc6abfb1a7f241ca58e9744ab3b046044d032646ae737e447a
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating calculix-adapter ... 
Creating su2-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating calculix-adapter ... [32mdone[0m[1B[1A[2KCreating su2-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:10f36603:start=1574686835176904118,finish=1574687123738981467,duration=288562077349,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0022dfc6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0022dfc6:start=1574687128466420558,finish=1574687130319491887,duration=1853071329,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:06809556[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/616642289/log.txt)