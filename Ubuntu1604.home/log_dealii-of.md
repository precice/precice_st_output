## Status: Passing 
Build: [1614](https://travis-ci.org/precice/systemtests/builds/647676484) 

Job: [1614.22](https://travis-ci.org/precice/systemtests/jobs/647676506) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in a50c5393d326
 ---> 757dc1123575
Removing intermediate container a50c5393d326
Step 3/12 : RUN apk add git
 ---> Running in 3dce14892e55
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r1)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r1.trigger
OK: 22 MiB in 20 packages
 ---> 827dad1aacde
Removing intermediate container 3dce14892e55
Step 4/12 : ARG branch=develop
 ---> Running in 0a80781f8e15
 ---> a4b5af0e3ee4
Removing intermediate container 0a80781f8e15
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in a64046d66a1c
[91mCloning into 'tutorials'...
[0m ---> 9017d14ca102
Removing intermediate container a64046d66a1c
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in c98970fa5da1
 ---> 43ce92ea7db2
Removing intermediate container c98970fa5da1
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 1195ebf44ce9
 ---> b62ef28cdd20
Removing intermediate container 1195ebf44ce9
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in f0d89319e0a1
 ---> 9b20aa2617fc
Removing intermediate container f0d89319e0a1
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in bb39973d494e
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> b9886db295df
Removing intermediate container bb39973d494e
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 000b1e07d394
 ---> 63c5d57c5671
Removing intermediate container 000b1e07d394
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 3604b2c169d1
 ---> e1a814be6747
Removing intermediate container 3604b2c169d1
Step 12/12 : USER [secure]
 ---> Running in bc4e7cda430b
 ---> 3d6b1c5742a7
Removing intermediate container bc4e7cda430b
Successfully built 3d6b1c5742a7
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:08037ad0689fcc7b24aa612d394381d671f0d8ba40060fc9465f18a16d60da48
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:1ace89ad0bf22f00e97ed0153f976c55c3af7bb667fe6a5f8f5a9f8291985033
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
travis_time:end:19c6456b:start=1581163725102685599,finish=1581163921928561771,duration=196825876172,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:00176c40[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:00176c40:start=1581163925930118449,finish=1581163927251151223,duration=1321032774,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1324d940[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/647676506/log.txt)