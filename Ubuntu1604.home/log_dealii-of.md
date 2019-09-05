 # Status :  Passing 
 # [Job url](https://travis-ci.org/precice/systemtests/builds/581200523) 
## Triggered by: [push](https://github.com/precice/systemtests/compare/a5fe66e3237c...5b9de68efcd3) 
## Last 100 lines of the job log at the moment of push...
```
 
Creating network "testcomposedealiiof_default" with the default driver
Creating network "testcomposedealiiof_[secure]comm" with the default driver
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
 ---> Running in 450082be3f23
 ---> f39ef30a56cf
Removing intermediate container 450082be3f23
Step 3/11 : RUN apk add git
 ---> Running in 4f76aa0e85f0
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
(1/6) Installing ca-certificates (20190108-r0)
(2/6) Installing nghttp2-libs (1.39.2-r0)
(3/6) Installing libcurl (7.65.1-r0)
(4/6) Installing expat (2.2.7-r0)
(5/6) Installing pcre2 (10.33-r0)
(6/6) Installing git (2.22.0-r0)
Executing busybox-1.30.1-r2.trigger
Executing ca-certificates-20190108-r0.trigger
OK: 21 MiB in 20 packages
 ---> dd9d29518627
Removing intermediate container 4f76aa0e85f0
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 7a1e51829641
[91mCloning into 'tutorials'...
[0m ---> 39fe6ebb75fb
Removing intermediate container 7a1e51829641
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 341a378dadc8
 ---> 616e19d4be94
Removing intermediate container 341a378dadc8
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 6e6de5f1c7ae
 ---> 9bfd63225d12
Removing intermediate container 6e6de5f1c7ae
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 21f9650a5508
 ---> f104157392b4
Removing intermediate container 21f9650a5508
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 511ea11e2bdf
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> a2f757d76870
Removing intermediate container 511ea11e2bdf
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in cc297a26e09e
 ---> d29f5131b772
Removing intermediate container cc297a26e09e
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in f7678ae342f5
 ---> f9b25b6b628a
Removing intermediate container f7678ae342f5
Step 11/11 : USER [secure]
 ---> Running in 2d41cfbd2faa
 ---> 9e040d4a0dbb
Removing intermediate container 2d41cfbd2faa
Successfully built 9e040d4a0dbb
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:2a5c17d6760457aa74e81a12a9c7912e721c75583b56fa37e2e6cff4a845d72b
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:804ae28762439b0fbae6df6041556cbe09c564d4c5e14c904d07a578969fb530
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
                         bash ../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:0d787cbc:start=1567689749184922574,finish=1567690062030924655,duration=312846002081,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:after_success[0Ktravis_time:start:00c06f63[0K$ python push.py -s -t dealii-of
Cloning into '[secure]_st_output'...
 ```
[Full job log](https://api.travis-ci.org/v3/job/581200540/log.txt)