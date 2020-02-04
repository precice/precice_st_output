## Status: Passing 
Build: [1603](https://travis-ci.org/precice/systemtests/builds/646122956) 

Job: [1603.19](https://travis-ci.org/precice/systemtests/jobs/646122975) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646122956) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 3151eb1955dc
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
 ---> 8299ee09ca84
Removing intermediate container 3151eb1955dc
Step 4/12 : ARG branch=develop
 ---> Running in 50996ba2ba98
 ---> b5c9df39f244
Removing intermediate container 50996ba2ba98
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 049bd7abb36c
[91mCloning into 'tutorials'...
[0m ---> 8c305bda8bfb
Removing intermediate container 049bd7abb36c
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in d21b5391df26
 ---> cd877b4ed4c8
Removing intermediate container d21b5391df26
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 3f45d1267c57
 ---> 59582290f24b
Removing intermediate container 3f45d1267c57
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 58f617303b65
 ---> f4cf87cdf8d8
Removing intermediate container 58f617303b65
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in b5842d87974f
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 01f9e07c08df
Removing intermediate container b5842d87974f
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 42d21383cc88
 ---> e11fafd80898
Removing intermediate container 42d21383cc88
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e95fe933f549
 ---> 7c03faa05a2e
Removing intermediate container e95fe933f549
Step 12/12 : USER [secure]
 ---> Running in d1b9ee8056f9
 ---> fbd85c6c8ee3
Removing intermediate container d1b9ee8056f9
Successfully built fbd85c6c8ee3
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:72b3e3bb4c1db43896d6ca7bd81587cfce50fc735ba4f20791092f003beab7cb
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:d21704409267af81a4eb229ec01086b63f5bf18c1faf864b6dd2ce05d841c3d8
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:36b32218:start=1580851455103104947,finish=1580851711690947677,duration=256587842730,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:09f8d0e6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:09f8d0e6:start=1580851716240927340,finish=1580851717731508844,duration=1490581504,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:022ecde5[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646122975/log.txt)