 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599812196) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/63f291b1fec7...efe9b440d9b6) 
## Last succesfull commits 
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/71eeed0aa3ca...d9a7dc3ed7e7)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [systemtests](https://github.com/precice/systemtests/compare/67d50405729725689cb7247b9b7b61e8cd0610e4...430ac8e48acf364daf6e1430ae60c277229d8f41) 
## Last 100 lines of the job log at the moment of push...
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
 ---> Running in 773f6dfbfd59
 ---> 7a6dc527c999
Removing intermediate container 773f6dfbfd59
Step 3/11 : RUN apk add git
 ---> Running in b8f0436f4de9
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
 ---> b12d47d13bf7
Removing intermediate container b8f0436f4de9
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 268816b78f82
[91mCloning into 'tutorials'...
[0m ---> a2c27858d3ea
Removing intermediate container 268816b78f82
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 22b93b4aa51e
 ---> e21dde0208cf
Removing intermediate container 22b93b4aa51e
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 75ee29063d8c
 ---> 4a760a994a56
Removing intermediate container 75ee29063d8c
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in b01c1b5269a3
 ---> 1dda5c6e4bd2
Removing intermediate container b01c1b5269a3
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 5716351ff2a9
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> c733ccd91d34
Removing intermediate container 5716351ff2a9
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 077021f2b05e
 ---> c942940fbe49
Removing intermediate container 077021f2b05e
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 2f9207c51872
 ---> bbc087dbbbb0
Removing intermediate container 2f9207c51872
Step 11/11 : USER [secure]
 ---> Running in 41b69bca4692
 ---> d49d1b2e1247
Removing intermediate container 41b69bca4692
Successfully built d49d1b2e1247
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:8e9ef052033a14d0f1539684ea21cf608caecbb20bc75664dcdb75cf1c3a9b4b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:fe2b0425bde41fbb8a6b13d5c114da7ad899c56c959350ad518fb506fc4ed414
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
travis_time:end:03e920b0:start=1571434971361242007,finish=1571435096177649710,duration=124816407703,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:02ffc169[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599812217/log.txt)