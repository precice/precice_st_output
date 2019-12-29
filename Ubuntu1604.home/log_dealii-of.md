## Status: Failure 
Build: [1370](https://travis-ci.org/precice/systemtests/builds/630566787) 

Job: [1370.22](https://travis-ci.org/precice/systemtests/jobs/630566809) 

Triggered by: [cron](https://github.com/precice/systemtests/compare/ff457bed2521c9ab78f7f6e490c7785219151c1e...968fe698268820917cf52199d2d3dcbaaf61fbaf) 
Last successful commits 
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/1cefd5edac2aea69ea37978eeb5479db3ada0042...d9a7dc3ed7e75c17e88adc4757c7bd5f44719b24)
* [systemtests](https://github.com/precice/systemtests/compare/4f15349af2e6b142f80dbeffbfffd5e75ea93b7e...ff457bed2521c9ab78f7f6e490c7785219151c1e)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/compare/7566319387fe...59b44bf3cbdc) 

---
Last 100 lines of the job log at the moment of push:
```
Creating volume "testcomposedealiiof_exchange" with default driver
Building tutorial-data
Step 1/12 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/12 : ENV tutorial_path tutorials/FSI/flap_perp/OpenFOAM-deal.II
 ---> Running in 26b37359fdc5
 ---> 459965922d4d
Removing intermediate container 26b37359fdc5
Step 3/12 : RUN apk add git
 ---> Running in 637b3e693b77
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20191127-r0)
(2/6) Installing nghttp2-libs (1.40.0-r0)
(3/6) Installing libcurl (7.67.0-r0)
(4/6) Installing expat (2.2.9-r1)
(5/6) Installing pcre2 (10.34-r1)
(6/6) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 22 MiB in 20 packages
 ---> 3de3be696e77
Removing intermediate container 637b3e693b77
Step 4/12 : ARG branch=develop
 ---> Running in 0f92cc6410e7
 ---> b9ec8919e21a
Removing intermediate container 0f92cc6410e7
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 966865144b6b
[91mCloning into 'tutorials'...
[0m ---> 7a5550c183f2
Removing intermediate container 966865144b6b
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in bf52de0e9bd5
 ---> d6f57f847695
Removing intermediate container bf52de0e9bd5
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 38f6e17dd953
 ---> 50877fd2d662
Removing intermediate container 38f6e17dd953
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 30d25f3de509
 ---> 50bc03eca699
Removing intermediate container 30d25f3de509
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 5d4f12fbbd3d
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 3c16a282d853
Removing intermediate container 5d4f12fbbd3d
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 9e93a898edcc
 ---> a5e59056e7e1
Removing intermediate container 9e93a898edcc
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 93dd8dfda481
 ---> 355506073beb
Removing intermediate container 93dd8dfda481
Step 12/12 : USER [secure]
 ---> Running in 0e55b19fbc0f
 ---> 43abac1bf9d2
Removing intermediate container 0e55b19fbc0f
Successfully built 43abac1bf9d2
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:44465d4255e3c47b043e030c3c8d52eacf4282d397c2100d6851f1ef21b87da9
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:da3b13b01bab6294fee4e904ada53107ce3ab0571fa0eeb55ed95d39e6840a14
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
travis_time:end:05bbc9d4:start=1577618961682037964,finish=1577619036922746631,duration=75240708667,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:15f737ff[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/630566809/log.txt)