## Status: Passing 
Build: [1243](https://travis-ci.org/precice/systemtests/builds/619873406) 

Job: [1243.18](https://travis-ci.org/precice/systemtests/jobs/619873424) 

Triggered by: [push](https://github.com/precice/systemtests/compare/e4ce4c7c44a4...33d01ce211d8) 

---
Last 100 lines of the job log at the moment of push:
```
Step 3/12 : RUN apk add git
 ---> Running in 9713d275660b
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
 ---> 042df941e794
Removing intermediate container 9713d275660b
Step 4/12 : ARG branch=develop
 ---> Running in 7c6b30d69eb4
 ---> 407d39e64735
Removing intermediate container 7c6b30d69eb4
Step 5/12 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in c3dcb433e7b9
[91mCloning into 'tutorials'...
[0m ---> acb094ecf2f4
Removing intermediate container c3dcb433e7b9
Step 6/12 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in 3678089675c1
 ---> fdad6acdb1ca
Removing intermediate container 3678089675c1
Step 7/12 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in dc64af0c9356
 ---> 420db6bfd760
Removing intermediate container dc64af0c9356
Step 8/12 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 76d4cde0d244
 ---> 5f2633e0d5ad
Removing intermediate container 76d4cde0d244
Step 9/12 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 4fb1f1ee53d1
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> c1285b1430cd
Removing intermediate container 4fb1f1ee53d1
Step 10/12 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 329ca6791f14
 ---> eaf8b1c1ea71
Removing intermediate container 329ca6791f14
Step 11/12 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 05e6816f8c6b
 ---> 1f21b2892799
Removing intermediate container 05e6816f8c6b
Step 12/12 : USER [secure]
 ---> Running in c4b55937bf37
 ---> c8f7c40898a9
Removing intermediate container c4b55937bf37
Successfully built c8f7c40898a9
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:515f7f059dd7d4248cca8001ecc183b3f67b5c97c6161f6b711f40a9ca96ed16
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:fcfd2206947e4332b9ecd236c3b12bf889932dea19a5741229c6add515fe6cca
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
travis_time:end:0515d4a9:start=1575333451873414501,finish=1575333718728030605,duration=266854616104,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:00a4d90f[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.14
Parsing documentation for dpl-1.10.14
Installing ri documentation for dpl-1.10.14
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:00a4d90f:start=1575333723404395768,finish=1575333725014815455,duration=1610419687,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:1204fd78[0KSuccessfully installed dpl-script-1.10.14
Parsing documentation for dpl-script-1.10.14
Installing ri documentation for dpl-script-1.10.14
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/619873424/log.txt)