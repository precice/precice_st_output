## Status: Passing 
Build: [1177](https://travis-ci.org/precice/systemtests/builds/618293063) 

Job: [1177.18](https://travis-ci.org/precice/systemtests/jobs/618293083) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f42978edba8f...f6ac64c472af) 

---
Last 100 lines of the job log at the moment of push:
```
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 7350898cd6fa
 ---> b67dfd898753
Removing intermediate container 7350898cd6fa
Step 3/11 : RUN apk add git
 ---> Running in 0a0800cdf1e9
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.66.0-r0)
(4/6) Installing expat (2.2.8-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> f2542ba765b9
Removing intermediate container 0a0800cdf1e9
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 88237b42ef13
[91mCloning into 'tutorials'...
[0m ---> d894c76eeb8a
Removing intermediate container 88237b42ef13
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 3b0afaf9717e
 ---> 4829907c749c
Removing intermediate container 3b0afaf9717e
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 444c248c49f5
 ---> 7d92b7bf2d87
Removing intermediate container 444c248c49f5
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 9176d0dfaf3b
 ---> 293860668b00
Removing intermediate container 9176d0dfaf3b
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 0c8d4fd8362e
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> b66f064526c9
Removing intermediate container 0c8d4fd8362e
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in b7bc236cb81b
 ---> 95af628054b1
Removing intermediate container b7bc236cb81b
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c4eac1e3ec4e
 ---> 907b6cd8fe04
Removing intermediate container c4eac1e3ec4e
Step 11/11 : USER [secure]
 ---> Running in c9537d125ebe
 ---> b8b38542f21f
Removing intermediate container c9537d125ebe
Successfully built b8b38542f21f
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:3320cb415223ff3ee8fefb382544a974c922bd4a4bb2ef99bca16abea6b6983e
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:1c30f97c6e522b88538281e5bc22fdb5b0b7a61e93428f0dbd58256220ff58a8
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:2fa05a67:start=1574966370152298191,finish=1574966641734011323,duration=271581713132,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:06b52589[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:06b52589:start=1574966646373441670,finish=1574966648011617192,duration=1638175522,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:00b54b6d[0Ktravis_foSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618293083/log.txt)