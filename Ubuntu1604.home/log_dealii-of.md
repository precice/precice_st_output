## Status: Passing 
Build: [1064](https://travis-ci.org/precice/systemtests/builds/609194596) 

Job: [1064.18](https://travis-ci.org/precice/systemtests/jobs/609194614) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e3f7960c948e...be03fa4f4575) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 69474f1939a4
 ---> a973596bc71a
Removing intermediate container 69474f1939a4
Step 3/11 : RUN apk add git
 ---> Running in 87dd7b8c962b
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
 ---> d2eef4920a3f
Removing intermediate container 87dd7b8c962b
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in ce679e4bcccb
[91mCloning into 'tutorials'...
[0m ---> a52bd9b0e320
Removing intermediate container ce679e4bcccb
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in e567e6ae49ea
 ---> e337d6274ed0
Removing intermediate container e567e6ae49ea
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 387b26186322
 ---> 8d911691198f
Removing intermediate container 387b26186322
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 115d8f126fba
 ---> 432de5c69782
Removing intermediate container 115d8f126fba
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 679df46336a4
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 62a772a68614
Removing intermediate container 679df46336a4
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 44f237a95ef3
 ---> 6314e6a9b549
Removing intermediate container 44f237a95ef3
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 02140503e16c
 ---> a13aaf2e54a1
Removing intermediate container 02140503e16c
Step 11/11 : USER [secure]
 ---> Running in ad869a70a3dc
 ---> 5cc57e104f67
Removing intermediate container ad869a70a3dc
Successfully built 5cc57e104f67
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e6cca2c606740a71adfe247662765329b4e2fa8282df5c61b4295aa4a293bc1b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:b0c20640b9e328330f8abcbcf868eccff461ea381d3262e3b065d03b42b7f2fb
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
travis_time:end:09b945cd:start=1573218497532131792,finish=1573218767923391319,duration=270391259527,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0fddf564[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0fddf564:start=1573218772589360841,finish=1573218774272150778,duration=1682789937,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0538ba38[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/609194614/log.txt)