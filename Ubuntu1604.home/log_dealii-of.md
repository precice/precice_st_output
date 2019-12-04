## Status: Passing 
Build: [1258](https://travis-ci.org/precice/systemtests/builds/620625719) 

Job: [1258.18](https://travis-ci.org/precice/systemtests/jobs/620625737) 

Triggered by: [push](https://github.com/precice/systemtests/compare/23fe0b4a3d6a...ff51dfcb2467) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 86b847c0e2a8
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
 ---> 70102c0697f2
Removing intermediate container 86b847c0e2a8
Step 4/12 : ARG branch=develop
 ---> Running in d2e729285bfc
 ---> ed630d579b48
Removing intermediate container d2e729285bfc
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 712cc40196f7
[91mCloning into 'tutorials'...
[0m ---> dd52251519e0
Removing intermediate container 712cc40196f7
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 33ac6a5d2201
 ---> 5264f224b37a
Removing intermediate container 33ac6a5d2201
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 4743f2f7dedc
 ---> e07c51ceead7
Removing intermediate container 4743f2f7dedc
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in a0f18d4a2b06
 ---> 5cda06dcf2b8
Removing intermediate container a0f18d4a2b06
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 1449b5e9e095
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 885d2200fa3e
Removing intermediate container 1449b5e9e095
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in d0f283cb1b73
 ---> ccd0a4706c1f
Removing intermediate container d0f283cb1b73
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in bac8f6ce0694
 ---> d4f28d505c87
Removing intermediate container bac8f6ce0694
Step 12/12 : USER [secure]
 ---> Running in f55ebdd07fd1
 ---> 2e8360151184
Removing intermediate container f55ebdd07fd1
Successfully built 2e8360151184
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:162b7e16d6efc49575dbb1dc4c8f56fc8352c96287ff665cb5d92ba503f014ef
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:acbba6bf10366bd2fa78129997d12fc77fc98eee6deeb35179a11d573b40cad0
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
travis_time:end:19b5a16c:start=1575471579352290279,finish=1575471845442504081,duration=266090213802,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0513fee0[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0513fee0:start=1575471850170228600,finish=1575471851852732054,duration=1682503454,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:306ad84b[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/620625737/log.txt)