## Status: Passing 
Build: [1580](https://travis-ci.org/precice/systemtests/builds/645031917) 

Job: [1580.22](https://travis-ci.org/precice/systemtests/jobs/645031939) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/b42adf2e689a763071326fd2ccb4fad54589f1aa...0b61ba36cce94a5b89e38963d3eebc970dbfd8a0) 

---
Last 100 lines of the job log at the moment of push:
```
Removing intermediate container c61830dc885f
Step 3/12 : RUN apk add git
 ---> Running in 59094865afa0
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
 ---> 922d631e4420
Removing intermediate container 59094865afa0
Step 4/12 : ARG branch=develop
 ---> Running in 13bbd1d0d8e4
 ---> c78c57d07efd
Removing intermediate container 13bbd1d0d8e4
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 491b6ef7ef6c
[91mCloning into 'tutorials'...
[0m ---> 0529f7ffb034
Removing intermediate container 491b6ef7ef6c
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in 71b77a5c66d1
 ---> 8b43788e88ea
Removing intermediate container 71b77a5c66d1
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 36c399ce675a
 ---> 87287d9cefc3
Removing intermediate container 36c399ce675a
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in e0e203bad8e8
 ---> 39739f899870
Removing intermediate container e0e203bad8e8
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 7e65000999dd
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 51a53ed734a8
Removing intermediate container 7e65000999dd
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in be80a8f432b2
 ---> a4d0bfbcc9dc
Removing intermediate container be80a8f432b2
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 3106f98a4711
 ---> 10a2210f5c05
Removing intermediate container 3106f98a4711
Step 12/12 : USER [secure]
 ---> Running in 6baab7c07d9e
 ---> 08e34a286105
Removing intermediate container 6baab7c07d9e
Successfully built 08e34a286105
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:0f3098a7565f7c13fb013bff8dc52e2c2c3cdd94aca48d41865ca1d71096b7ae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:95f0d9a48236976815a2feae37b4a5068cff65302eff17822a25124e6f5bd76c
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
travis_time:end:01693032:start=1580643917107875803,finish=1580644112213537077,duration=195105661274,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0b332a6b[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0b332a6b:start=1580644116900969521,finish=1580644118395646753,duration=1494677232,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0a9c6c53[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/645031939/log.txt)