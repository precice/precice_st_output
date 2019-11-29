## Status: Passing 
Build: [1211](https://travis-ci.org/precice/systemtests/builds/618376977) 

Job: [1211.18](https://travis-ci.org/precice/systemtests/jobs/618377001) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f1e6a1b68d13...e4ce4c7c44a4) 

---
Last 100 lines of the job log at the moment of push:
```
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 6f9db0635cb5
 ---> 6ca47ee37e87
Removing intermediate container 6f9db0635cb5
Step 3/12 : RUN apk add git
 ---> Running in 9fb5cfd534ed
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
 ---> 5907b1715d2b
Removing intermediate container 9fb5cfd534ed
Step 4/12 : ARG branch=develop
 ---> Running in 50fc7e01f8a2
 ---> 0ac93b9d3e6e
Removing intermediate container 50fc7e01f8a2
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 82dbdcbe3a07
[91mCloning into 'tutorials'...
[0m ---> 2977711215c4
Removing intermediate container 82dbdcbe3a07
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 1ba05cd8d93b
 ---> 6155352d7f4f
Removing intermediate container 1ba05cd8d93b
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 8c86927694fd
 ---> a64645bd0d9d
Removing intermediate container 8c86927694fd
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in dc273d7cf884
 ---> e0d63bb2ad00
Removing intermediate container dc273d7cf884
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 5ccd886d9c37
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 07d7a14f9743
Removing intermediate container 5ccd886d9c37
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 6abca15e179c
 ---> d916a32ce3d4
Removing intermediate container 6abca15e179c
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in e6b797ab9582
 ---> dff3cd1d4bd8
Removing intermediate container e6b797ab9582
Step 12/12 : USER [secure]
 ---> Running in c7a1e6e901a5
 ---> a1a234c49191
Removing intermediate container c7a1e6e901a5
Successfully built a1a234c49191
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:621857c5b2f5d84275e432a812ae4700a596751767623e580112a305388d6eaa
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:5de9f8a4284c97ec435b3014b94472b2853598b02ab6330e649063c1685c66bc
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
travis_time:end:09df54bd:start=1574991748536924424,finish=1574992014733103878,duration=266196179454,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0d1f1fc4[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0d1f1fc4:start=1574992019135304109,finish=1574992020689813445,duration=1554509336,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1a49bc84[0K
```
[
Full job log](https://api.travis-ci.org/v3/job/618377001/log.txt)