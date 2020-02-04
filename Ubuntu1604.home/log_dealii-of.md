## Status: Passing 
Build: [1598](https://travis-ci.org/precice/systemtests/builds/645892844) 

Job: [1598.22](https://travis-ci.org/precice/systemtests/jobs/645892872) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/07c487419fcd18bdb04b9d9fef13c8b1318f3bef...6213c52a25101c0051df0fbc215ba9f941209daa) 

---
Last 100 lines of the job log at the moment of push:
```
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
 ---> Running in c4505ead6fe4
 ---> 9dbda2a31cdf
Removing intermediate container c4505ead6fe4
Step 3/12 : RUN apk add git
 ---> Running in c9bc68b9203e
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
 ---> 947d416f2bba
Removing intermediate container c9bc68b9203e
Step 4/12 : ARG branch=develop
 ---> Running in a53f052767ac
 ---> 34e91eaf03e2
Removing intermediate container a53f052767ac
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 9f8ea2f127cd
[91mCloning into 'tutorials'...
[0m ---> 1c0c0951fed1
Removing intermediate container 9f8ea2f127cd
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in f6d1c374e4f2
 ---> 92db29a89842
Removing intermediate container f6d1c374e4f2
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 43e552bbbca6
 ---> e9f964c475f3
Removing intermediate container 43e552bbbca6
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in a57a7df4eb5a
 ---> 0b9a891c4cda
Removing intermediate container a57a7df4eb5a
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 54e4a758c10c
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 5e452a9f5a60
Removing intermediate container 54e4a758c10c
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 535dbfa6b929
 ---> 48cb963a375d
Removing intermediate container 535dbfa6b929
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in c0c33a34522b
 ---> 173cd7fe09d8
Removing intermediate container c0c33a34522b
Step 12/12 : USER [secure]
 ---> Running in 75e1313fa1ae
 ---> 057393678ee3
Removing intermediate container 75e1313fa1ae
Successfully built 057393678ee3
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ea8abdbefd367fb0c30630136b061c6189bb5ad3767d77bfd08372119fb5af39
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:cfbb6320e7d59f9e11bd559d13299250b7ec4383817dc7d0d838c68b22268009
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
travis_time:end:29fe00fa:start=1580817982285721382,finish=1580818240155953602,duration=257870232220,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:32605ae6[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
travis_fold:start:dpl.1[33mInstalling deploy dependencies[0m

```
[
Full job log](https://api.travis-ci.org/v3/job/645892872/log.txt)