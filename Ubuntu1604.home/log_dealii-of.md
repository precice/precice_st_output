## Status: Passing 
Build: [1237](https://travis-ci.org/precice/systemtests/builds/619351844) 

Job: [1237.18](https://travis-ci.org/precice/systemtests/jobs/619351862) 

Triggered by: [push](https://github.com/precice/systemtests/compare/5cd65d21e48f...60b68152f174) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in a0f870a577d1
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
 ---> ab8e7b43a197
Removing intermediate container a0f870a577d1
Step 4/12 : ARG branch=develop
 ---> Running in 90f8819ddf00
 ---> b6b968ab802d
Removing intermediate container 90f8819ddf00
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in ea930dd44751
[91mCloning into 'tutorials'...
[0m ---> f5c0fd9555d7
Removing intermediate container ea930dd44751
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 12b84dc75775
 ---> 73bd1522cd8d
Removing intermediate container 12b84dc75775
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 88cda45df61e
 ---> 730d8ba38b9f
Removing intermediate container 88cda45df61e
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 31e14934e2ea
 ---> 913a4410df7e
Removing intermediate container 31e14934e2ea
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in d4becd3bc1ed
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> a1bc8f463ada
Removing intermediate container d4becd3bc1ed
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in c10e8f446d9b
 ---> 23cf3e94bbf4
Removing intermediate container c10e8f446d9b
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 0862c675dcc5
 ---> ad36361a7b28
Removing intermediate container 0862c675dcc5
Step 12/12 : USER [secure]
 ---> Running in 8a7fb35d6087
 ---> d33b36ed099a
Removing intermediate container 8a7fb35d6087
Successfully built d33b36ed099a
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:17df4e0778368c5680a67d4fbd568496224f149d9b071688dad9e92221715498
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:748c1102e777a7850c1c532a459f5f676a29798a670d72c13d28a0301a8f6c66
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
travis_time:end:07340628:start=1575240439520857432,finish=1575240703055262870,duration=263534405438,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0fdf8720[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0fdf8720:start=1575240707609864580,finish=1575240709242722654,duration=1632858074,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0885c4cd[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/619351862/log.txt)