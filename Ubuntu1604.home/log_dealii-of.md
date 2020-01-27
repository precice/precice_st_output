## Status: Passing 
Build: [1521](https://travis-ci.org/precice/systemtests/builds/642317432) 

Job: [1521.23](https://travis-ci.org/precice/systemtests/jobs/642317455) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/41581e838945d44f597d37ae02844ddc5bcaa133...feb7379d4291423a8ea6ec40728f855e8268130b) 

---
Last 100 lines of the job log at the moment of push:
```
Creating network "testcomposedealiiof_[secure]comm" with the default driver
Creating volume "testcomposedealiiof_output" with default driver
Creating volume "testcomposedealiiof_configs" with default driver
Creating volume "testcomposedealiiof_input_dealii" with default driver
Creating volume "testcomposedealiiof_input_of" with default driver
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in ecf392ef5db1
 ---> 15f940498633
Removing intermediate container ecf392ef5db1
Step 3/12 : RUN apk add git
 ---> Running in aa26f8878b8a
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 843e878813d6
Removing intermediate container aa26f8878b8a
Step 4/12 : ARG branch=develop
 ---> Running in b4b81c268903
 ---> 15c97bd0f024
Removing intermediate container b4b81c268903
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in c59c4b637dbc
[91mCloning into 'tutorials'...
[0m ---> 4234ff0170c8
Removing intermediate container c59c4b637dbc
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in fb83a97a5204
 ---> 366895d4d8dd
Removing intermediate container fb83a97a5204
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 04d484ad9805
 ---> 9c167350d057
Removing intermediate container 04d484ad9805
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 97b4b14993cb
 ---> a9c900a2fdd2
Removing intermediate container 97b4b14993cb
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 776ee12bc128
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 6cca5cedae33
Removing intermediate container 776ee12bc128
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 77ab8ece717c
 ---> 085b2993279d
Removing intermediate container 77ab8ece717c
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 8ae9ada35c43
 ---> d2e6114b4bb1
Removing intermediate container 8ae9ada35c43
Step 12/12 : USER [secure]
 ---> Running in 194838f6eaac
 ---> 8f3305995791
Removing intermediate container 194838f6eaac
Successfully built 8f3305995791
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9c34ba59ce7def418b30f072762f1af26bfd19cd52917002802465bb132e1e52
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:c1a8b05d7fe4d3ddb8f88478a82a8b5ccb3126268f2e00bf35de3df1882c6fb5
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:0d7d065b:start=1580125433747770622,finish=1580125629128531213,duration=195380760591,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:1f208bcb[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl

```
[
Full job log](https://api.travis-ci.org/v3/job/642317455/log.txt)