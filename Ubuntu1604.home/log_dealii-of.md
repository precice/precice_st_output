## Status: Passing 
Build: [1161](https://travis-ci.org/precice/systemtests/builds/617683464) 

Job: [1161.18](https://travis-ci.org/precice/systemtests/jobs/617683483) 

Triggered by: [push](https://github.com/precice/systemtests/compare/ec4ef9d4aedd...6a636c04a7f9) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in a1da7cbb7507
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
 ---> d3556872b764
Removing intermediate container a1da7cbb7507
Step 4/12 : ARG branch=develop
 ---> Running in 76866750f1cd
 ---> e361f0917573
Removing intermediate container 76866750f1cd
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 5f649c69fa41
[91mCloning into 'tutorials'...
[0m ---> 630b433a2c6e
Removing intermediate container 5f649c69fa41
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 8aa15707aa93
 ---> 13accf6a461a
Removing intermediate container 8aa15707aa93
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 66578228702f
 ---> bc97f95e8b3d
Removing intermediate container 66578228702f
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 22077d5e1dc3
 ---> 505c5300df38
Removing intermediate container 22077d5e1dc3
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in f56be26ebcc3
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> 51f9f3d33706
Removing intermediate container f56be26ebcc3
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in d108092cf0c8
 ---> 58a48c4f313f
Removing intermediate container d108092cf0c8
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 1e48ddac0de0
 ---> db787a77955e
Removing intermediate container 1e48ddac0de0
Step 12/12 : USER [secure]
 ---> Running in 5453de43c2e7
 ---> 98db5b6c3e93
Removing intermediate container 5453de43c2e7
Successfully built 98db5b6c3e93
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:d1e3cf9fc21d38b0bd5071fdc517a74de9ad989536e3e0e143422b194b9b30a7
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:12d9c88825f3fec1acb27e580f5f569c8d598c6835f342bfa421391f0b371104
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
travis_time:end:0a18bfa0:start=1574861597800580379,finish=1574861864558037910,duration=266757457531,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:2847d4da[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:2847d4da:start=1574861869049389444,finish=1574861870755404645,duration=1706015201,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:0bafc200[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
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
Full job log](https://api.travis-ci.org/v3/job/617683483/log.txt)