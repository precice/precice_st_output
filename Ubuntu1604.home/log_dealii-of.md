## Status: Passing 
Build: [1100](https://travis-ci.org/precice/systemtests/builds/612774159) 

Job: [1100.18](https://travis-ci.org/precice/systemtests/jobs/612774177) 

Triggered by: [push](https://github.com/precice/systemtests/compare/772d64248024...9566b8a963d8) 

---
Last 100 lines of the job log at the moment of push:
```
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in c9f75bba2280
 ---> 7ae819710f92
Removing intermediate container c9f75bba2280
Step 3/11 : RUN apk add git
 ---> Running in a28086714a95
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
 ---> c839910aa0f8
Removing intermediate container a28086714a95
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 84c35025a629
[91mCloning into 'tutorials'...
[0m ---> 931da32a4281
Removing intermediate container 84c35025a629
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 9e20f0ccf0c8
 ---> 52363245af9e
Removing intermediate container 9e20f0ccf0c8
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in c417a9945ec6
 ---> bea7d6274105
Removing intermediate container c417a9945ec6
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 9985a959aab5
 ---> 67b6379a8677
Removing intermediate container 9985a959aab5
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 9f0d5e61c508
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 4378e7c7277e
Removing intermediate container 9f0d5e61c508
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 88df1fc8a23e
 ---> fd974ce09287
Removing intermediate container 88df1fc8a23e
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e596dc572852
 ---> 4d5360f87b04
Removing intermediate container e596dc572852
Step 11/11 : USER [secure]
 ---> Running in d4abfd2396d0
 ---> 793013dbe175
Removing intermediate container d4abfd2396d0
Successfully built 793013dbe175
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:716de21b0369d6022c063dd3d1be49cb1424694a2ef78c353e3a2532fd4077da
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:f1c941e840d6ab9d97ac75687df612204f773d48ae33d3cf1a83130a56ea0c88
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
travis_time:end:26e28aaf:start=1573908208527125731,finish=1573908478804051252,duration=270276925521,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:036d9074[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:036d9074:start=1573908484028413467,finish=1573908485860336549,duration=1831923082,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:27d1cef8[0KSuccessfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/612774177/log.txt)