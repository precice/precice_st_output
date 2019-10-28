## Status: Passing 
Build: [1044](https://travis-ci.org/precice/systemtests/builds/603937404) 

Job: [1044.18](https://travis-ci.org/precice/systemtests/jobs/603937424) 

Triggered by: [push](https://github.com/precice/systemtests/compare/81ea09464169...4d5c1a1b3cfb) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in c52febcc18af
 ---> dd9ee4ee3d8c
Removing intermediate container c52febcc18af
Step 3/11 : RUN apk add git
 ---> Running in f64ab3be121b
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
 ---> 90b292c24d00
Removing intermediate container f64ab3be121b
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 449fca97c1ca
[91mCloning into 'tutorials'...
[0m ---> f6693906624d
Removing intermediate container 449fca97c1ca
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in b7649b65210f
 ---> 2e7a633d139f
Removing intermediate container b7649b65210f
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in eb2ba7a0eccf
 ---> f9a89fcbd52f
Removing intermediate container eb2ba7a0eccf
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in dd5885cb71ee
 ---> a592d3bfef3c
Removing intermediate container dd5885cb71ee
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 71860b12b5fd
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 6a18241e6ad3
Removing intermediate container 71860b12b5fd
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in abd366f14ee9
 ---> 1a3056ad6921
Removing intermediate container abd366f14ee9
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in ec96bcbc5a63
 ---> 1f71e98e9546
Removing intermediate container ec96bcbc5a63
Step 11/11 : USER [secure]
 ---> Running in d34d512d9ff3
 ---> 4aaa4328ed2d
Removing intermediate container d34d512d9ff3
Successfully built 4aaa4328ed2d
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:fbf7e03e88b589e5eecfdb836fb724bfb62537ee7ba51b3a30ccd8a75852d23f
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:af3ddc4169f62cec237a11b16e7aceb0954a7f050fb2364cf5e3e05aebad4c37
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
travis_time:end:0922a8e7:start=1572276023157150451,finish=1572276289850137769,duration=266692987318,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:13e93e52[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:13e93e52:start=1572276294649119627,finish=1572276296409754812,duration=1760635185,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:023bd93e[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/603937424/log.txt)