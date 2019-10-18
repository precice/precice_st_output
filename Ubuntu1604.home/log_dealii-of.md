 # Status : Failing
 # [Job url](https://travis-ci.org/precice/systemtests/builds/599535277) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/aeaaaab693ed...bc601c6301d2) 
## Last succesfull commits 
* [systemtests](https://github.com/precice/systemtests/compare/3211dcc17558...521ff68ed5cc)
* [dealii-adapter](https://github.com/precice/dealii-adapter/compare/71eeed0aa3ca...d9a7dc3ed7e7)
* [openfoam-adapter](https://github.com/precice/openfoam-adapter/pull/96) 
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
 ---> Running in 2c78e616582d
 ---> 5b2d38777f01
Removing intermediate container 2c78e616582d
Step 3/11 : RUN apk add git
 ---> Running in 72a2925543fd
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
 ---> 0efec7141678
Removing intermediate container 72a2925543fd
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in b261a9de886f
[91mCloning into 'tutorials'...
[0m ---> 414161a3969a
Removing intermediate container b261a9de886f
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in ff0f72ec2508
 ---> d236a04d2d99
Removing intermediate container ff0f72ec2508
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 85f2152cd0ff
 ---> 68826e2fb2fe
Removing intermediate container 85f2152cd0ff
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in c40406c6b816
 ---> ce3eb9b33735
Removing intermediate container c40406c6b816
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in a9df89f45e4b
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 3a4ecc84a0fc
Removing intermediate container a9df89f45e4b
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in cde9cb4f1622
 ---> 9af8cfcb1cfb
Removing intermediate container cde9cb4f1622
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 302e188587c6
 ---> 0825e44aef6c
Removing intermediate container 302e188587c6
Step 11/11 : USER [secure]
 ---> Running in 6711322b9b26
 ---> 171cbb0c15a8
Removing intermediate container 6711322b9b26
Successfully built 171cbb0c15a8
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:9235d23d74933ab1c4a88a461f57e661efb920ded7187cf11181a207f0c7ea38
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:c5d40f0253edc1473e5b62667f1749580a358cddba958d3926ac237497c2d58b
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
travis_time:end:08c1e122:start=1571394444265640671,finish=1571394529782943101,duration=85517302430,event=script[0K[31;1mThe command "python system_testing.py -s dealii-of" exited with 1.[0m

travis_fold:start:after_failure[0Ktravis_time:start:0e2b99ca[0K$ python push.py -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/599535304/log.txt)