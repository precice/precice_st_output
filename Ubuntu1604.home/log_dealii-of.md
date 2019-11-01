## Status: Passing 
Build: [1053](https://travis-ci.org/precice/systemtests/builds/606180964) 

Job: [1053.18](https://travis-ci.org/precice/systemtests/jobs/606180982) 

Triggered by: [push](https://github.com/precice/systemtests/compare/4d5c1a1b3cfb...f02cef114a79) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in e8a5acadc3ad
 ---> e81e7307a312
Removing intermediate container e8a5acadc3ad
Step 3/11 : RUN apk add git
 ---> Running in b6f224aec65d
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
 ---> 2598162a3864
Removing intermediate container b6f224aec65d
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 1f35ba914041
[91mCloning into 'tutorials'...
[0m ---> f12be73fb0ba
Removing intermediate container 1f35ba914041
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 40409a406b9d
 ---> b11a4e087840
Removing intermediate container 40409a406b9d
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 152b03eab335
 ---> 7d1c8954c096
Removing intermediate container 152b03eab335
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 3d48e8820cf3
 ---> ca8fec2ff4ab
Removing intermediate container 3d48e8820cf3
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in e4e5f0a3d2da
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 3a771f0b3064
Removing intermediate container e4e5f0a3d2da
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 820edaa50ddf
 ---> a2a4cb827b22
Removing intermediate container 820edaa50ddf
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 4265f4fe11c9
 ---> 76e5df8d9c3a
Removing intermediate container 4265f4fe11c9
Step 11/11 : USER [secure]
 ---> Running in 928d425af636
 ---> 889ca941f7c6
Removing intermediate container 928d425af636
Successfully built 889ca941f7c6
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:914638c131614e647c0780f831aae7d3efcff62515e7d50251f431eac2f2ec92
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:0f96831c4068110911f459872b4c7bb95696e163c1a679d2fee51905ba638f67
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
travis_time:end:0bee1147:start=1572642071605565729,finish=1572642344118724126,duration=272513158397,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:005c3700[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:005c3700:start=1572642348729957504,finish=1572642350355698727,duration=1625741223,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:34594714[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/606180982/log.txt)