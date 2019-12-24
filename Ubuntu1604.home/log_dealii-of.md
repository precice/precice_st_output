## Status: Failure 
Build: [1360](https://travis-ci.org/precice/systemtests/builds/629054356) 

Job: [1360.22](https://travis-ci.org/precice/systemtests/jobs/629054384) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:7c92a2c6bbcb6b6beff92d0a940779769c2477b807c202954c537e2e0deb9bed
Status: Downloaded newer image for alpine:latest
 ---> c85b8f829d1f
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in bed2d4f25b6a
 ---> f77dc2f45803
Removing intermediate container bed2d4f25b6a
Step 3/12 : RUN apk add git
 ---> Running in 5f0a39d779a3
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r0)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 77fc7ce527d5
Removing intermediate container 5f0a39d779a3
Step 4/12 : ARG branch=develop
 ---> Running in 66c078bef585
 ---> b529b812a956
Removing intermediate container 66c078bef585
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 19de17ddd56b
[91mCloning into 'tutorials'...
[0m ---> 9b1c70bea153
Removing intermediate container 19de17ddd56b
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 0744f0b833cb
 ---> fc7742a6b0d4
Removing intermediate container 0744f0b833cb
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 9d74cc6ff0eb
 ---> 680b497ed19a
Removing intermediate container 9d74cc6ff0eb
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in f40d392ed645
 ---> 6598f252f263
Removing intermediate container f40d392ed645
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in d7f4bc179ca8
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 29b68ad2fec9
Removing intermediate container d7f4bc179ca8
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 089fc4c1976e
 ---> bc44bc75906e
Removing intermediate container 089fc4c1976e
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 040ab01773c4
 ---> 4ee7ab5c7a12
Removing intermediate container 040ab01773c4
Step 12/12 : USER [secure]
 ---> Running in 154952d83aa9
 ---> 5980262aa9e1
Removing intermediate container 154952d83aa9
Successfully built 5980262aa9e1
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:164e164435f8b470b0a42c8de4ccf6a8a760373ebebaf061ccea3235cb13a096
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:04fa64910a1eaad64a1f5d5b10b59dcebb41a5f44df0235f1945e3217fd92021
Status: Downloaded newer image for [secure]/dealii-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter ... 
Creating openfoam-adapter
[1A[2KCreating openfoam-adapter ... [32mdone[0m[1BCreating dealii-adapter ... 
Creating dealii-adapter
[1A[2KCreating dealii-adapter ... [32mdone[0m[1BAll adapters finished!
Only in /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput: Fluid
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop;  docker-compose config &&
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_dealii-of/Output
TESTS FAILED WITH: Output files do not match reference
Files differing               : []
Files only in reference (left): ['Fluid']
Files only in output(right)   : []
travis_time:end:0892f431:start=1577186781353616787,finish=1577186856721210746,duration=75367593959,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:13109998[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/629054384/log.txt)