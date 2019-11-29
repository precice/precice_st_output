## Status: Passing 
Build: [1227](https://travis-ci.org/precice/systemtests/builds/618560778) 

Job: [1227.18](https://travis-ci.org/precice/systemtests/jobs/618560798) 

Triggered by: [push](https://github.com/precice/systemtests/compare/d440b60eb25a...e486b1f8560f) 

---
Last 100 lines of the job log at the moment of push:
```
Step 3/12 : RUN apk add git
 ---> Running in 194cc07ded27
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
 ---> 47e31a0a5078
Removing intermediate container 194cc07ded27
Step 4/12 : ARG branch=develop
 ---> Running in ed6399e05f74
 ---> 661ccc7e7d38
Removing intermediate container ed6399e05f74
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in cee02159c642
[91mCloning into 'tutorials'...
[0m ---> d07c2c5b23dc
Removing intermediate container cee02159c642
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 1b8f75191051
 ---> 18531ce27086
Removing intermediate container 1b8f75191051
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in db084b8822d3
 ---> 6251c844d7a2
Removing intermediate container db084b8822d3
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in b64f91437fd5
 ---> bba780de8a1b
Removing intermediate container b64f91437fd5
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 96832bf474fe
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> da72f9c9789a
Removing intermediate container 96832bf474fe
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in f5355f9802c6
 ---> 2e8a9e7d00fc
Removing intermediate container f5355f9802c6
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in bc7a834140b1
 ---> 2f6ab297a343
Removing intermediate container bc7a834140b1
Step 12/12 : USER [secure]
 ---> Running in 5806cf7c3c43
 ---> 3f0649b37cd8
Removing intermediate container 5806cf7c3c43
Successfully built 3f0649b37cd8
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f0b435d58bc6bf4fb69c4f19af360da26c7b396f81e4bf8d437d7314c7188d74
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:b559827a149afba7ac8a568bc2f79bc2d7a9882003e90d17d9b30d2a8e03a717
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
travis_time:end:0c22f32c:start=1575030768703868828,finish=1575031040802369986,duration=272098501158,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0cb4b520[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0cb4b520:start=1575031045842350349,finish=1575031047572006799,duration=1729656450,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1f6532a0[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/618560798/log.txt)