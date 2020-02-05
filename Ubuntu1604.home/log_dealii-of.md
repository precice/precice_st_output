## Status: Passing 
Build: [1609](https://travis-ci.org/precice/systemtests/builds/646351628) 

Job: [1609.19](https://travis-ci.org/precice/systemtests/jobs/646351647) 

Triggered by: [website trigger](https://travis-ci.org/precice/systemtests/builds/646351628) 

---
Last 100 lines of the job log at the moment of push:
```
Step 3/12 : RUN apk add git
 ---> Running in 21c898ac63c5
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
 ---> b8bc1b27048d
Removing intermediate container 21c898ac63c5
Step 4/12 : ARG branch=develop
 ---> Running in e75565930d36
 ---> e2b93cb5b5fb
Removing intermediate container e75565930d36
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in b4b56150b7d5
[91mCloning into 'tutorials'...
[0m ---> 2a72877e4373
Removing intermediate container b4b56150b7d5
Step 6/12 : RUN mkdir configs && sed -e 's|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\" to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g' 		$tutorial_path/[secure]-config.xml > configs/[secure]-config.xml
 ---> Running in 6f35fec3893c
 ---> e138ebba7711
Removing intermediate container 6f35fec3893c
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 837c7c4296a4
 ---> 237e1dea2f7b
Removing intermediate container 837c7c4296a4
Step 8/12 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in 776f4077b226
 ---> 92b17b91fc84
Removing intermediate container 776f4077b226
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 81f8864232d7
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 3b8378a14ab2
Removing intermediate container 81f8864232d7
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 80f8d3febf42
 ---> d0327767508b
Removing intermediate container 80f8d3febf42
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 23d84a42a84a
 ---> 30d559d9ceb4
Removing intermediate container 23d84a42a84a
Step 12/12 : USER [secure]
 ---> Running in 9835b8666992
 ---> 1c85b728d172
Removing intermediate container 9835b8666992
Successfully built 1c85b728d172
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:e412e549a6a376d115044133965ff5c7d7a1fa08e65d438b4f1b92f4c0723a63
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:e571379a1435f054a3a92b6cc94325c8dd2474152d4ba9451d3ce41db30f0c24
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
travis_time:end:1e6c6c18:start=1580904368978744212,finish=1580904568889391298,duration=199910647086,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:00b75f82[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:00b75f82:start=1580904573308482935,finish=1580904574753874408,duration=1445391473,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:059f9c10[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/646351647/log.txt)