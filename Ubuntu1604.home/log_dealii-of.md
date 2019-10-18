## Status: Failure 
Build: [978](https://travis-ci.org/precice/systemtests/builds/599812617) 

Job: [978.18](https://travis-ci.org/precice/systemtests/jobs/599812635) 

Triggered by: [pull_request](https://github.com/precice/systemtests/pull/111) 
Last successful commits 
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/71eeed0aa3ca...d9a7dc3ed7e7)
* [systemtests](https://github.com/precice/systemtests/compare/67d50405729725689cb7247b9b7b61e8cd0610e4...430ac8e48acf364daf6e1430ae60c277229d8f41) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_output" with default driver
Creating volume "testcomposedealiiof_configs" with default driver
Creating volume "testcomposedealiiof_input_dealii" with default driver
Creating volume "testcomposedealiiof_input_of" with default driver
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/11 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/11 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in f2461e69dada
 ---> e18f0c5d2132
Removing intermediate container f2461e69dada
Step 3/11 : RUN apk add git
 ---> Running in aa3b096b86f7
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
 ---> 015e5b7b8ccd
Removing intermediate container aa3b096b86f7
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in c9c78f76a93d
[91mCloning into 'tutorials'...
[0m ---> c12268e338ae
Removing intermediate container c9c78f76a93d
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 02732e969e8a
 ---> 558da168a8e8
Removing intermediate container 02732e969e8a
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 9c663938c99d
 ---> 2d67f14619c8
Removing intermediate container 9c663938c99d
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 9ba2bcf82ce2
 ---> 8f680d57d767
Removing intermediate container 9ba2bcf82ce2
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 440f627ea5db
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> b74d438cb028
Removing intermediate container 440f627ea5db
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 81f5b1b7d675
 ---> acfe46931699
Removing intermediate container 81f5b1b7d675
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 25c8344f6970
 ---> a9c5df61930e
Removing intermediate container 25c8344f6970
Step 11/11 : USER [secure]
 ---> Running in ac556cdb2491
 ---> b5cff971b540
Removing intermediate container ac556cdb2491
Successfully built b5cff971b540
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:abc28e71defd133daf727eb6220447d4b2e15733a7d410a36239238646b31351
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:10999ca5f74dd6d6efef8eb6c00535ae19599c470fc701e42d03f7f372919f23
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
travis_time:end:0e903c00:start=1571438998358153939,finish=1571439089330966428,duration=90972812489,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:14cb6e06[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/599812635/log.txt)