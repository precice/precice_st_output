## Status: Passing 
Build: [1650](https://travis-ci.org/precice/systemtests/builds/648350351) 

Job: [1650.22](https://travis-ci.org/precice/systemtests/jobs/648350373) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/6213c52a25101c0051df0fbc215ba9f941209daa...000ab5ae1cde5210e654ffa14b06aa7e98916477) 

---
Last 100 lines of the job log at the moment of push:
```
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 62bb7c5e9b99
 ---> 2c2d31d94964
Removing intermediate container 62bb7c5e9b99
Step 3/12 : RUN apk add git
 ---> Running in e5ac05ee3156
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r1)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r1.trigger
OK: 22 MiB in 20 packages
 ---> dbb29397fa20
Removing intermediate container e5ac05ee3156
Step 4/12 : ARG branch=develop
 ---> Running in 9863fb851d4e
 ---> 1446cc9f1c0c
Removing intermediate container 9863fb851d4e
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 997f6c2d34fe
[91mCloning into 'tutorials'...
[0m ---> 32ef202c9140
Removing intermediate container 997f6c2d34fe
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in aa557e8c702b
 ---> f44b6655afce
Removing intermediate container aa557e8c702b
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in d582e5437c47
 ---> 17c60a0d836f
Removing intermediate container d582e5437c47
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 3263c37fc5a6
 ---> 00fde795bd9d
Removing intermediate container 3263c37fc5a6
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 5bfad702d0c5
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 48ffb3eef261
Removing intermediate container 5bfad702d0c5
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 629910c0d22d
 ---> 305d5e4dcf25
Removing intermediate container 629910c0d22d
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 891e8225cad7
 ---> 5a028c0c5dd1
Removing intermediate container 891e8225cad7
Step 12/12 : USER [secure]
 ---> Running in 59127f29ba6f
 ---> cf115eeb7a25
Removing intermediate container 59127f29ba6f
Successfully built cf115eeb7a25
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:f4a35c80e3584b3e11b7da5bf50b88da768fe5fe965b027645946b3c174412f9
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:29902b295c1b0edcc5880417ed6b2f3275fd22ae301f4cee273903376453bbb8
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
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:21594eda:start=1581335456113096756,finish=1581335713933984541,duration=257820887785,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:16b8ca1a[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:16b8ca1a:start=1581335718621899659,finish=1581335720258455058,duration=1636555399,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:166185d8[0KCloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/648350373/log.txt)