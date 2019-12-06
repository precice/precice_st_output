## Status: Passing 
Build: [1275](https://travis-ci.org/precice/systemtests/builds/621555096) 

Job: [1275.19](https://travis-ci.org/precice/systemtests/jobs/621555115) 

Triggered by: [push](https://github.com/precice/systemtests/compare/b8adc727aafb...aff84f792bf7) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 2e37665be797
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
 ---> 90d960420b84
Removing intermediate container 2e37665be797
Step 4/12 : ARG branch=develop
 ---> Running in dad193850092
 ---> e9b598fc5917
Removing intermediate container dad193850092
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d4ea9995769a
[91mCloning into 'tutorials'...
[0m ---> a41d61a10048
Removing intermediate container d4ea9995769a
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 919c94121b89
 ---> 464b5860f0bf
Removing intermediate container 919c94121b89
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 525144da1f43
 ---> e38edea3d72b
Removing intermediate container 525144da1f43
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 4772c9e43167
 ---> 9c879553a438
Removing intermediate container 4772c9e43167
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in e3c19a0bc204
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> c74e5bc1ffdb
Removing intermediate container e3c19a0bc204
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 327a7643e361
 ---> 158cf56c59be
Removing intermediate container 327a7643e361
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0cdc797719d7
 ---> 786dbdf37cca
Removing intermediate container 0cdc797719d7
Step 12/12 : USER [secure]
 ---> Running in 77c740b4ca80
 ---> 0e360d12f6c2
Removing intermediate container 77c740b4ca80
Successfully built 0e360d12f6c2
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:c1abde63a3f30408a0d3b56eb42e37f48c944b979632774f42d419388ff36dec
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:6101ab4effa8dc9f79cc571ad406abe47a3b7e0d631f4671064ee55a60f67812
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
######################this is now the newest commit!##################
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:03b149c0:start=1575641293329792321,finish=1575641492466610227,duration=199136817906,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1e3a4769[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:1e3a4769:start=1575641496454289897,finish=1575641497907144890,duration=1452854993,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0e39df80[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/621555115/log.txt)