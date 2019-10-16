 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/598541158) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/478596e1ce45...2f42d88d1871) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/92a2d96de651986b4a651cb923faf4ab421973a6...58fea094b8a40df0d7d8ea6b460b42ec6cd296d4)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/71eeed0aa3ca...d9a7dc3ed7e7) 
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
 ---> Running in a1939589ca15
 ---> e74f2abdf1be
Removing intermediate container a1939589ca15
Step 3/11 : RUN apk add git
 ---> Running in e41d6655f035
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
 ---> 339957244fd9
Removing intermediate container e41d6655f035
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 772814bd999a
[91mCloning into 'tutorials'...
[0m ---> 62c64ba1d536
Removing intermediate container 772814bd999a
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in ad9824c51c1e
 ---> fcb5dbb748b3
Removing intermediate container ad9824c51c1e
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 795cc6b05f34
 ---> 3fc31917cec6
Removing intermediate container 795cc6b05f34
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in eea82aadc0ad
 ---> 08e4da307b5e
Removing intermediate container eea82aadc0ad
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in baef5e031892
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 0229adeb8d5b
Removing intermediate container baef5e031892
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 7320d8d3a7c4
 ---> fedf6046661e
Removing intermediate container 7320d8d3a7c4
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0c1fc40d4953
 ---> 6dc1481f8606
Removing intermediate container 0c1fc40d4953
Step 11/11 : USER [secure]
 ---> Running in 07b8f8701a25
 ---> 87abf858411b
Removing intermediate container 07b8f8701a25
Successfully built 87abf858411b
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:7d002fc20b8a936e9af3f431707439657c2fb037fc483b62dc29cc6c0384e923
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:aa96fd65b12ebbce1518c3fafa7064e231f14c0a3413527ce69133f59eb23cef
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
travis_time:end:2879b0b2:start=1571218439654190353,finish=1571218523866686946,duration=84212496593,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:05d8415f[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/598541176/log.txt)