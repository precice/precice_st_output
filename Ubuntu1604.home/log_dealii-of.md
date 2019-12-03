## Status: Passing 
Build: [1248](https://travis-ci.org/precice/systemtests/builds/620247509) 

Job: [1248.18](https://travis-ci.org/precice/systemtests/jobs/620247527) 

Triggered by: [push](https://github.com/precice/systemtests/commit/25da98cf068b) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 91cd6c311dda
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
 ---> c2ee5ba86cf0
Removing intermediate container 91cd6c311dda
Step 4/12 : ARG branch=develop
 ---> Running in 760712f709b1
 ---> f10c07ac7a89
Removing intermediate container 760712f709b1
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1768ece4ec47
[91mCloning into 'tutorials'...
[0m ---> 54f97e7fe25f
Removing intermediate container 1768ece4ec47
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in ac39119a3807
 ---> 0c9fd3ed86e2
Removing intermediate container ac39119a3807
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in bf4d92b63ab1
 ---> 5567b760b7b0
Removing intermediate container bf4d92b63ab1
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in ca16bfaea8b5
 ---> a0de2bc94c5e
Removing intermediate container ca16bfaea8b5
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 5290cbd0f311
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 98d4dabf8e91
Removing intermediate container 5290cbd0f311
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 2c7a054d3c26
 ---> 590e6818ea43
Removing intermediate container 2c7a054d3c26
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 273037cc236f
 ---> f6f3a1539afc
Removing intermediate container 273037cc236f
Step 12/12 : USER [secure]
 ---> Running in 86edd7b16c5d
 ---> 829fc8e828b0
Removing intermediate container 86edd7b16c5d
Successfully built 829fc8e828b0
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c6392f8479b0628d5026f531530b3fa6ba5a7f27506f57712b6f098558a846c7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:fcb9dda6dcee8fda244c6f8a971ef4a785b6fcbe7913bc07c0f425e3e447e4f0
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
travis_time:end:0ce34b3c:start=1575400424999805727,finish=1575400735823134979,duration=310823329252,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:059c7d47[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:059c7d47:start=1575400740197254678,finish=1575400741778519565,duration=1581264887,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0c43961a[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620247527/log.txt)