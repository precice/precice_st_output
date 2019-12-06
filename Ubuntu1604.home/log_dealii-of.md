## Status: Passing 
Build: [1274](https://travis-ci.org/precice/systemtests/builds/621545880) 

Job: [1274.18](https://travis-ci.org/precice/systemtests/jobs/621545898) 

Triggered by: [push](https://github.com/precice/systemtests/compare/f9c5ac902029...10d407970668) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:c19173c5ada610a5989151111163d28a67368362762534d8a8121ce95cf2bd5a
Status: Downloaded newer image for alpine:latest
 ---> 965ea09ff2eb
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 726152f221fb
 ---> f41f9a6660a4
Removing intermediate container 726152f221fb
Step 3/12 : RUN apk add git
 ---> Running in 3a27e1d7d4ed
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
 ---> 8915fa73719b
Removing intermediate container 3a27e1d7d4ed
Step 4/12 : ARG branch=develop
 ---> Running in 8c0905bf4458
 ---> b14a47a79841
Removing intermediate container 8c0905bf4458
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 347f9e3041e0
[91mCloning into 'tutorials'...
[0m ---> 9c4543655661
Removing intermediate container 347f9e3041e0
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 4d186d93deab
 ---> 92e354a6ff95
Removing intermediate container 4d186d93deab
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in efcdc1cd88a4
 ---> 766b274e5a02
Removing intermediate container efcdc1cd88a4
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in c08181c4fc65
 ---> 1cb974460e2a
Removing intermediate container c08181c4fc65
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 383f988c528e
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 72294148d7b7
Removing intermediate container 383f988c528e
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 31a1f14a4fe6
 ---> 1afd1f6e4268
Removing intermediate container 31a1f14a4fe6
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 646f59611a4f
 ---> f31fb7f8fdaa
Removing intermediate container 646f59611a4f
Step 12/12 : USER [secure]
 ---> Running in 5927ab55101b
 ---> 9b81751178db
Removing intermediate container 5927ab55101b
Successfully built 9b81751178db
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:55d4768db6e0e74ea7d9fc6591b2b09872272381689e13b496ba0454b83e3c28
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:f57815ea4d29576c7b8cd99c133a8b83c9e4695d154044ab053be71163221b23
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
travis_time:end:0fbed856:start=1575637323405764536,finish=1575637583197319491,duration=259791554955,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:271033bd[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:271033bd:start=1575637587179889939,finish=1575637588588107729,duration=1408217790,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0266e7fa[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/621545898/log.txt)