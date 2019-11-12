## Status: Passing 
Build: [1082](https://travis-ci.org/precice/systemtests/builds/610801800) 

Job: [1082.19](https://travis-ci.org/precice/systemtests/jobs/610801830) 

Triggered by: [push](https://github.com/precice/systemtests/compare/2e77de77c876...846ecee12afc) 

---
Last 100 lines of the job log at the moment of push:
```
 ---> Running in b3fc4d739ee4
 ---> e1196d3b40b3
Removing intermediate container b3fc4d739ee4
Step 3/11 : RUN apk add git
 ---> Running in 09355c2be571
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
 ---> 743cffa1846c
Removing intermediate container 09355c2be571
Step 4/11 : RUN git clone https://github.com/[secure]/tutorials
 ---> Running in de2900e7d467
[91mCloning into 'tutorials'...
[0m ---> 4752fd2d9010
Removing intermediate container de2900e7d467
Step 5/11 : RUN mkdir configs && sed -e 's|gather-scatter"|gather-scatter" exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g' $tutorial_path/[secure]-config_serial.xml > configs/[secure]-config.xml
 ---> Running in d67845e930d3
 ---> 40ab7b3267e3
Removing intermediate container d67845e930d3
Step 6/11 : RUN sed -i '/application     pimpleFoam/d; s/\/\/ application     pimpleDyMFoam/application    pimpleDyMFoam/g'     $tutorial_path/Fluid/system/controlDict
 ---> Running in 588cd36fa661
 ---> abbe7963d19d
Removing intermediate container 588cd36fa661
Step 7/11 : RUN rm $tutorial_path/[secure]-config_serial.xml $tutorial_path/[secure]-config.xml
 ---> Running in 9808fc317188
 ---> 9c15c299381c
Removing intermediate container 9808fc317188
Step 8/11 : RUN rm -rfv $tutorial_path/Fluid/0/
 ---> Running in 387b44d7ef2a
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/p'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/phi'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/U'
removed 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0/pointDisplacement'
removed directory: 'tutorials/FSI/flap_perp/OpenFOAM-deal.II/Fluid/0'
 ---> f9c4fec6d0a2
Removing intermediate container 387b44d7ef2a
Step 9/11 : RUN cp -r $tutorial_path/Fluid/0.orig/ $tutorial_path/Fluid/0/
 ---> Running in 06f41ad45448
 ---> 3fa6734aefd8
Removing intermediate container 06f41ad45448
Step 10/11 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in d38fe621b0ba
 ---> b7a7feac9ca6
Removing intermediate container d38fe621b0ba
Step 11/11 : USER [secure]
 ---> Running in c1b20bf1218d
 ---> 63a9ae7d9b96
Removing intermediate container c1b20bf1218d
Successfully built 63a9ae7d9b96
Successfully tagged testcomposedealiiof_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:ddad88e6c8ca9df124b1d5d567ad25cc8568ef24531b552698669a691ae2eeae
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling dealii-adapter ([secure]/dealii-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/dealii-adapter-ubuntu1604.home-develop
Digest: sha256:a6557fd625214bb43943d73396b12096f8fbbfd0cc7508bfb50f7870a57350f4
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
travis_time:end:083c3d7c:start=1573559853942707269,finish=1573560118832505271,duration=264889798002,event=script[0K[32;1mThe command "python system_testing.py -s dealii-of" exited with 0.[0m

travis_fold:start:dpl_0[0Ktravis_time:start:0b87f19d[0K$ rvm $(travis_internal_ruby) --fuzzy do ruby -S gem install dpl
Successfully installed dpl-1.10.13
Parsing documentation for dpl-1.10.13
Installing ri documentation for dpl-1.10.13
Done installing documentation for dpl after 0 seconds
1 gem installed
travis_time:end:0b87f19d:start=1573560123463587765,finish=1573560125141716874,duration=1678129109,event=after_success[0Ktravis_fold:end:dpl_0[0Ktravis_time:start:211d7687[0Ktravis_fold:start:dpl.1[33mInstalling deploy dependencies[0m
Successfully installed dpl-script-1.10.13
Parsing documentation for dpl-script-1.10.13
Installing ri documentation for dpl-script-1.10.13
Done installing documentation for dpl-script after 0 seconds
1 gem installed

travis_fold:end:dpl.1travis_fold:start:dpl.2[33mPreparing deploy[0m

travis_fold:end:dpl.2travis_fold:start:dpl.3[33mDeploying application[0m
Cloning into '[secure]_st_output'...

```
[
Full job log](https://api.travis-ci.org/v3/job/610801830/log.txt)