## Status: Passing 
Build: [1071](https://travis-ci.org/precice/systemtests/builds/610072373) 

Job: [1071.18](https://travis-ci.org/precice/systemtests/jobs/610072395) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ffab6e4cf6eb...2e77de77c876) 

---
Last 100 lines of the job log at the moment of push:
```
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 88889a12c63d
 ---> 225bc389d16a
Removing intermediate container 88889a12c63d
Step 3/11 : RUN apk add git
 ---> Running in f9a55c2490a4
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
 ---> 40e3c06b1317
Removing intermediate container f9a55c2490a4
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 2c171b7dfe6a
[91mCloning into 'tutorials'...
[0m ---> 00c294f7acec
Removing intermediate container 2c171b7dfe6a
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 6f58a671947d
 ---> c44b063b8154
Removing intermediate container 6f58a671947d
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 15245b43e36a
 ---> fdb084feb331
Removing intermediate container 15245b43e36a
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 82c151d27c88
 ---> 33b392766506
Removing intermediate container 82c151d27c88
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 33de715bde04
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 14a90b04c646
Removing intermediate container 33de715bde04
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 5926b919a763
 ---> 4f228d3eeb26
Removing intermediate container 5926b919a763
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1ef6881e23bf
 ---> 296404f8228b
Removing intermediate container 1ef6881e23bf
Step 11/11 : USER [secure]
 ---> Running in 7ad43e34cc05
 ---> da7bc2f07733
Removing intermediate container 7ad43e34cc05
Successfully built da7bc2f07733
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:98e7b7fde8bd6b618c7ffe6b7ed9cd847d62e94c024d4c0ecdbd1eb70a3db786
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:bbed35e87df67ae25ee9a9beb4bb39e73d8085711c7ec99e7d0df298b62bf602
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
travis_time:end:0301ae76:start=1573425595377377564,finish=1573425864385915547,duration=269008537983,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1b9e17a0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1b9e17a0:start=1573425869173851846,finish=1573425870881833112,duration=1707981266,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:07010556[0KSuccessfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/610072395/log.txt)