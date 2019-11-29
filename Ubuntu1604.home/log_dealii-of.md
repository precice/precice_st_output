## Status: Passing 
Build: [1215](https://travis-ci.org/precice/systemtests/builds/618378110) 

Job: [1215.18](https://travis-ci.org/precice/systemtests/jobs/618378128) 

Triggered by: [push](https://github.com/precice/systemtests/compare/95fbdb5c2d24...03b1aca5c88d) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 0752dc8960ee
 ---> db27f21c9ec7
Removing intermediate container 0752dc8960ee
Step 3/12 : RUN apk add git
 ---> Running in ee2819395a0d
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
 ---> aa4432c15341
Removing intermediate container ee2819395a0d
Step 4/12 : ARG branch=develop
 ---> Running in 16d15f9909e1
 ---> e1008a75eac3
Removing intermediate container 16d15f9909e1
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 1fd0f0faf319
[91mCloning into 'tutorials'...
[0m ---> 982995dc3af6
Removing intermediate container 1fd0f0faf319
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 2a41fbcf1994
 ---> 3e22c7131184
Removing intermediate container 2a41fbcf1994
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 0fbf9f413b19
 ---> 463e2bcc79da
Removing intermediate container 0fbf9f413b19
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 6be44fd61ddc
 ---> b0ee7dfbd130
Removing intermediate container 6be44fd61ddc
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in b3ca63150e8e
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 9918079b1482
Removing intermediate container b3ca63150e8e
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 97dc1e06517a
 ---> 696e511a8753
Removing intermediate container 97dc1e06517a
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in f9f05cf249ec
 ---> 252afa1b93d9
Removing intermediate container f9f05cf249ec
Step 12/12 : USER [secure]
 ---> Running in 937706f8ce44
 ---> 038a84baf9b4
Removing intermediate container 937706f8ce44
Successfully built 038a84baf9b4
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e53292d98713aaab24a43c37f3df5ae3008cfab8a4d0c68d0a4db65ec1e3cad7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:b4dba3d8508078cb682019343f2f12b7d1ba65a7b975de27b6e358c1370faf4d
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
travis_time:end:20f725a6:start=1575001895918289671,finish=1575002162650941892,duration=266732652221,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0b8545fc[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0b8545fc:start=1575002167250102775,finish=1575002168850110980,duration=1600008205,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:150645ac[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/618378128/log.txt)