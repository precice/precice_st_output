## Status: Passing 
Build: [1062](https://travis-ci.org/precice/systemtests/builds/609194087) 

Job: [1062.18](https://travis-ci.org/precice/systemtests/jobs/609194107) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f02cef114a79...c96d99257303) 

---
Last 100 lines of the job log at the moment of push:
```
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 81aebcfa2a34
 ---> 33de3f4ae53b
Removing intermediate container 81aebcfa2a34
Step 3/11 : RUN apk add git
 ---> Running in 35b2a4d19745
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
 ---> afb06c1f2453
Removing intermediate container 35b2a4d19745
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in cf62a7bc982b
[91mCloning into 'tutorials'...
[0m ---> c268a8d841f0
Removing intermediate container cf62a7bc982b
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 8097ec5535ef
 ---> 4df5ba3e9ae8
Removing intermediate container 8097ec5535ef
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 5882943713e3
 ---> 6ae38f6c29ba
Removing intermediate container 5882943713e3
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 13ddc81da7df
 ---> 4e7d867b0dd5
Removing intermediate container 13ddc81da7df
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in adb869f96374
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 963bfe9569b7
Removing intermediate container adb869f96374
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in ae350b3138ca
 ---> 1984329be1d6
Removing intermediate container ae350b3138ca
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 6580ef86f93e
 ---> 88e8d55b7385
Removing intermediate container 6580ef86f93e
Step 11/11 : USER [secure]
 ---> Running in 95d3e476ee89
 ---> f985e1c08ba7
Removing intermediate container 95d3e476ee89
Successfully built f985e1c08ba7
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:378ef6ba2ce11e83a8e56ce1b601e6708559dc7791caea54395add87de1e187d
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:6e6d8e026a38242b740ddc77b84c9c012a62a492cc2c4cc804db077848d351fb
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
travis_time:end:00694152:start=1573216721216205814,finish=1573216991393319892,duration=270177114078,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0939d080[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0939d080:start=1573216996729396926,finish=1573216998491156831,duration=1761759905,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0a41780c[0KSuccessfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/609194107/log.txt)