## Status: Passing 
Build: [1249](https://travis-ci.org/precice/systemtests/builds/620247918) 

Job: [1249.18](https://travis-ci.org/precice/systemtests/jobs/620247947) 

Triggered by: [push](https://github.com/precice/systemtests/compare/96bc06472339...f9c5ac902029) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 0004e35121cc
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
 ---> ca06cde8a42e
Removing intermediate container 0004e35121cc
Step 4/12 : ARG branch=develop
 ---> Running in 5a049149b3da
 ---> 3c0918960f75
Removing intermediate container 5a049149b3da
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in a2d195b8c659
[91mCloning into 'tutorials'...
[0m ---> b6212232ae43
Removing intermediate container a2d195b8c659
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 363873788dec
 ---> 74079ea026b5
Removing intermediate container 363873788dec
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 18c94960df8c
 ---> 8b1ce241d6b1
Removing intermediate container 18c94960df8c
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 3fc34705b30b
 ---> d95333469788
Removing intermediate container 3fc34705b30b
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 3156e93ca65a
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 2fa582b1c904
Removing intermediate container 3156e93ca65a
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 89c9c4211e0d
 ---> 451a58336910
Removing intermediate container 89c9c4211e0d
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 9338badf30dd
 ---> 543bb4f477d0
Removing intermediate container 9338badf30dd
Step 12/12 : USER [secure]
 ---> Running in e3b4de4ee42c
 ---> 7dbc8e7b932b
Removing intermediate container e3b4de4ee42c
Successfully built 7dbc8e7b932b
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:27f9c92f133bc04da46d7fb6b630ca9dba656907f0728f0a4fd2e27fc75c922f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:4205d732b1890d1166adc5a94569d023d5928b9cef9f16ee36fafac2ee6d62f3
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
travis_time:end:12f9d070:start=1575402586884539988,finish=1575402853623682998,duration=266739143010,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0459561c[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0459561c:start=1575402858903381416,finish=1575402860715675566,duration=1812294150,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1aaf19a0[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620247947/log.txt)