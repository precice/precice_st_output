## Status: Passing 
Build: [1134](https://travis-ci.org/precice/systemtests/builds/616642276) 

Job: [1134.18](https://travis-ci.org/precice/systemtests/jobs/616642294) 

Triggered by: [push](https://github.com/precice/systemtests/commit/0d3b5a2c0bbe) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in 81f31fdc2e5b
 ---> 1ae615976ee0
Removing intermediate container 81f31fdc2e5b
Step 3/11 : RUN apk add git
 ---> Running in 957fbd21f16b
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
 ---> 6e6250d131fe
Removing intermediate container 957fbd21f16b
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in 993e8cabd608
[91mCloning into 'tutorials'...
[0m ---> 00e1257e42dd
Removing intermediate container 993e8cabd608
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 118defb91a98
 ---> b9bf5ccfc088
Removing intermediate container 118defb91a98
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 67a3a4f44f9d
 ---> b194f95877fe
Removing intermediate container 67a3a4f44f9d
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 458f32041ade
 ---> d6252738b05a
Removing intermediate container 458f32041ade
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 8d7384931741
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 132e9f5a5f30
Removing intermediate container 8d7384931741
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in b763fd490be8
 ---> 7bec1ade2e80
Removing intermediate container b763fd490be8
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0c0f31b91fde
 ---> 950aaf087fc2
Removing intermediate container 0c0f31b91fde
Step 11/11 : USER [secure]
 ---> Running in 2e817e8404b8
 ---> f79eb6664e98
Removing intermediate container 2e817e8404b8
Successfully built f79eb6664e98
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:841fbebfd0e95b69b4a71598fc5834714c1fe03a0af429fbffb0119c530d48ec
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:6e4c8bb715f5cd01983d5376e9675e26e75d806f94e372e8c28677f5512aaa8a
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
                         bash ../../silent_compose.sh
EXECUTING: docker cp tutorial-data:/Output .
travis_time:end:27aa221b:start=1574687702710184970,finish=1574687967609616785,duration=264899431815,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:01d4b2fe[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:01d4b2fe:start=1574687972788990817,finish=1574687974723658421,duration=1934667604,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:006fc59a[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/616642294/log.txt)