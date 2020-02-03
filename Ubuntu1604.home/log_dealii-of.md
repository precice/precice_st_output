## Status: Passing 
Build: [1587](https://travis-ci.org/precice/systemtests/builds/645394789) 

Job: [1587.22](https://travis-ci.org/precice/systemtests/jobs/645394820) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 7643a01ce772
 ---> 6e0484143c7e
Removing intermediate container 7643a01ce772
Step 3/12 : RUN apk add git
 ---> Running in 211d09ec53d1
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> e291cebeb21e
Removing intermediate container 211d09ec53d1
Step 4/12 : ARG branch=develop
 ---> Running in 4ecb56b98656
 ---> 9660dd9f3ce7
Removing intermediate container 4ecb56b98656
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 7e8ec25cd186
[91mCloning into 'tutorials'...
[0m ---> 37eff62d9547
Removing intermediate container 7e8ec25cd186
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in 609578a19913
 ---> 3bdb7e8bb608
Removing intermediate container 609578a19913
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 6f38000686b0
 ---> dbe738fc2b02
Removing intermediate container 6f38000686b0
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 90980964f19e
 ---> ad2ac0bc2658
Removing intermediate container 90980964f19e
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 07bf9041a191
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 10a523ee2c3b
Removing intermediate container 07bf9041a191
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 245d8d6f8afd
 ---> 196abb06e8dd
Removing intermediate container 245d8d6f8afd
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 47f6b8b33823
 ---> 20fa50221006
Removing intermediate container 47f6b8b33823
Step 12/12 : USER [secure]
 ---> Running in e7145f16c16a
 ---> 409ec5409bed
Removing intermediate container e7145f16c16a
Successfully built 409ec5409bed
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:1bf7bfebac3582204fa43ff8841c901bd107b21d514963b85f521a8d27991f7b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:fea216f3155493421c86f38e3803edce09914deb7109ec554faf3585580fffbd
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:03f85a39:start=1580730369332768569,finish=1580730563923606020,duration=194590837451,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1a7b9be0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645394820/log.txt)